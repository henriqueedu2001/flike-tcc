#!/usr/bin/env python3
"""Build the FLIKE thesis with a project-local, checksum-pinned Tectonic."""

import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "FLIKE"
BUILD = ROOT / "build"
OUTPUT = ROOT / "pdfs" / "FLIKE.pdf"
VERSION = "0.17.0"
ENGINE = ROOT / ".tools" / f"tectonic-{VERSION}" / "tectonic"
STATE = BUILD / "state.json"
LOG = BUILD / "compile.log"
RELEASE = "https://github.com/tectonic-typesetting/tectonic/releases/download"
# SHA-256 digests published by the official GitHub release API.
ASSETS = {
    ("Linux", "x86_64"): (
        "x86_64-unknown-linux-musl",
        "8533d07f9ccbd7a65824b9e0459041bca34af1eb33daba48f59215593753a3b7",
    ),
    ("Linux", "aarch64"): (
        "aarch64-unknown-linux-musl",
        "b10954a95404f3ab2328d2fa59a5ebab8e657f893fab096f98be8db7c0c979b8",
    ),
    ("Darwin", "x86_64"): (
        "x86_64-apple-darwin",
        "7c90ef5b6ddb1eb1937e4337add5237b79338e4b9676459fa91187d24d6cdf80",
    ),
    ("Darwin", "arm64"): (
        "aarch64-apple-darwin",
        "a3f1cac7c5678f01661a92212f58480ae3b0634115d880dbc59e2953ded45667",
    ),
}


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest() if hasattr(
            hashlib, "file_digest"
        ) else hashlib.sha256(stream.read()).hexdigest()


def install_engine(offline):
    if ENGINE.is_file():
        return
    if offline:
        raise RuntimeError("Tectonic ainda não instalado. Execute ./compile.sh com internet uma vez.")
    target = ASSETS.get((platform.system(), platform.machine()))
    if target is None:
        raise RuntimeError("Plataforma sem binário configurado. Use Linux x86_64/ARM64 ou macOS x86_64/ARM64.")
    if not shutil.which("curl"):
        raise RuntimeError("Instale curl para o primeiro download do compilador.")
    triple, expected = target
    url = f"{RELEASE}/tectonic%40{VERSION}/tectonic-{VERSION}-{triple}.tar.gz"
    ENGINE.parent.mkdir(parents=True, exist_ok=True)
    print(f"Instalando Tectonic {VERSION} dentro do projeto...", flush=True)
    with tempfile.TemporaryDirectory(prefix="download-", dir=ENGINE.parent) as temp:
        archive = Path(temp) / "tectonic.tar.gz"
        subprocess.run([
            "curl", "--fail", "--location", "--silent", "--show-error",
            "--proto", "=https", "--proto-redir", "=https",
            "--retry", "2", "--connect-timeout", "20", "--max-time", "180",
            url, "--output", str(archive),
        ], check=True)
        if digest(archive) != expected:
            raise RuntimeError("Checksum do download não confere; binário não instalado.")
        candidate = Path(temp) / "tectonic"
        # Extract only the regular executable; never unpack arbitrary archive paths.
        with tarfile.open(archive, "r:gz") as bundle:
            member = bundle.getmember("tectonic")
            if not member.isfile():
                raise RuntimeError("Arquivo oficial não contém um executável regular.")
            with bundle.extractfile(member) as source, candidate.open("wb") as dest:
                shutil.copyfileobj(source, dest)
        candidate.chmod(0o755)
        candidate.replace(ENGINE)


def fingerprint():
    """Hash all project inputs, including additions/removals and the build code."""
    result = hashlib.sha256()
    paths = sorted(p for p in SOURCE.rglob("*") if p.is_file())
    paths += [Path(__file__).resolve(), ROOT / "compile.sh", ENGINE]
    for path in paths:
        result.update(str(path.relative_to(ROOT)).encode())
        result.update(b"\0")
        result.update(digest(path).encode())
    return result.hexdigest()


def up_to_date(key):
    try:
        saved = json.loads(STATE.read_text())
        return saved["inputs"] == key and saved["pdf"] == digest(OUTPUT)
    except (OSError, ValueError, KeyError, TypeError):
        return False


def build(args):
    install_engine(args.offline)
    if not (SOURCE / "main.tex").is_file():
        raise RuntimeError(f"Documento principal não encontrado: {SOURCE / 'main.tex'}")
    key = fingerprint()
    if not args.force and up_to_date(key):
        print(f"PDF atualizado; nenhuma recompilação necessária.\n{OUTPUT}")
        return

    # Keep generated chapter auxiliaries out of the source tree.
    for directory in SOURCE.rglob("*"):
        if directory.is_dir():
            (BUILD / directory.relative_to(SOURCE)).mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["TECTONIC_CACHE_DIR"] = str(ROOT / ".cache" / "tectonic")
    command = [
        str(ENGINE), "-X", "compile", "main.tex",
        "--outdir", str(BUILD), "--keep-logs", "--keep-intermediates",
        "--synctex", "--untrusted",
    ]
    if args.offline:
        command.append("--only-cached")
    generated = BUILD / "main.pdf"
    generated.unlink(missing_ok=True)
    # Remove old bibliography diagnostics so validation only sees this run.
    for old_log in BUILD.rglob("*.blg"):
        old_log.unlink()
    print("Compilando a tese (LaTeX, bibliografia e referências)...", flush=True)
    started = time.monotonic()
    with LOG.open("w") as log:
        process = subprocess.Popen(
            command, cwd=SOURCE, env=env, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True, errors="replace",
        )
        try:
            for line in process.stdout:
                print(line, end="", flush=True)
                log.write(line)
            code = process.wait()
        except BaseException:
            process.terminate()
            process.wait()
            raise
    if code:
        raise RuntimeError(f"Compilação falhou (código {code}). Consulte {LOG}. O último PDF válido foi preservado.")
    if not generated.is_file() or not generated.read_bytes().startswith(b"%PDF-"):
        raise RuntimeError("O compilador não produziu um PDF válido; saída final não substituída.")
    tex_log = (BUILD / "main.log").read_text(errors="replace")
    if "Missing character:" in tex_log or "There were undefined references" in tex_log:
        raise RuntimeError(f"Há caracteres ausentes ou referências indefinidas em {BUILD / 'main.log'}. Saída final não substituída.")
    for bib_log in BUILD.rglob("*.blg"):
        if re.search(r"There (?:was|were) .*error message", bib_log.read_text(errors="replace")):
            raise RuntimeError(f"BibTeX registrou erro em {bib_log}. Saída final não substituída.")
    if fingerprint() != key:
        raise RuntimeError("Os fontes mudaram durante a compilação. Execute novamente; saída final não substituída.")

    # Publish only after a successful build, with an atomic replace on the same filesystem.
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=OUTPUT.parent, prefix=".FLIKE-", delete=False) as temp:
        staged = Path(temp.name)
        try:
            with generated.open("rb") as source:
                shutil.copyfileobj(source, temp)
        except BaseException:
            staged.unlink(missing_ok=True)
            raise
    try:
        staged.replace(OUTPUT)
    finally:
        staged.unlink(missing_ok=True)
    STATE.write_text(json.dumps({"inputs": key, "pdf": digest(OUTPUT)}, indent=2) + "\n")
    print(f"\nPDF gerado em {time.monotonic() - started:.1f}s:\n{OUTPUT}\nLogs: {LOG}")


def main():
    parser = argparse.ArgumentParser(description="Compila a tese FLIKE em pdfs/FLIKE.pdf.")
    parser.add_argument("--force", action="store_true", help="Recompilar mesmo sem alterações nos fontes.")
    parser.add_argument("--offline", action="store_true", help="Usar somente o motor e os pacotes já baixados.")
    args = parser.parse_args()
    BUILD.mkdir(parents=True, exist_ok=True)
    with (BUILD / ".compile.lock").open("a") as lock:
        # A single writer protects downloads, intermediate files and the final PDF.
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Outra compilação está em andamento; aguardando...", flush=True)
            fcntl.flock(lock, fcntl.LOCK_EX)
        build(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCompilação interrompida.", file=sys.stderr)
        sys.exit(130)
    except (OSError, RuntimeError, subprocess.CalledProcessError, tarfile.TarError) as error:
        print(f"Erro: {error}", file=sys.stderr)
        sys.exit(1)
