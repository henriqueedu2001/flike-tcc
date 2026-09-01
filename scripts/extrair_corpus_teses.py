#!/usr/bin/env python3
"""Extrai texto e prepara pacotes de leitura das teses de referência do PCS.

Os textos integrais e pacotes são temporários para evitar duplicar centenas de
megabytes no Git. O manifesto estrutural permanece no repositório.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import unicodedata
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
COLLECTION = REPO / "materiais" / "teses-referencia" / "pcs"
README = COLLECTION / "README.md"
ANALYSES = COLLECTION / "analises"
TEMP_ROOT = Path("/tmp/flike-teses-corpus")
TEXT_DIR = TEMP_ROOT / "textos"
PACKET_DIR = TEMP_ROOT / "pacotes"
MANIFEST = ANALYSES / "CORPUS.json"


def run(command: list[str]) -> str:
    completed = subprocess.run(command, check=True, capture_output=True, text=True)
    return completed.stdout


def selected_items() -> list[dict[str, str | int]]:
    pattern = re.compile(r"^\| ([CS]\d+) \| (.+?) \| `(20\d{2})/(.+?\.pdf)` \|$")
    items: list[dict[str, str | int]] = []
    for line in README.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if not match:
            continue
        group, title, year, filename = match.groups()
        items.append(
            {
                "year": int(year),
                "group": group,
                "id": f"{year}-{group}",
                "title": title,
                "filename": filename,
                "relative_pdf": f"{year}/{filename}",
            }
        )
    return items


def count_unique_numbers(text: str, label: str) -> int:
    numbers = {
        int(number)
        for number in re.findall(rf"(?im)^\s*{label}\s+(\d+)\s*[–—-]", text)
    }
    return len(numbers)


def normalize(value: str) -> str:
    """Normaliza uma linha para localizar títulos em português ou inglês."""
    value = unicodedata.normalize("NFKD", value)
    value = "".join(character for character in value if not unicodedata.combining(character))
    return " ".join(value.casefold().split())


def heading_candidates(pages: list[str]) -> list[dict[str, str | int]]:
    candidates: list[dict[str, str | int]] = []
    heading = re.compile(
        r"^\s*(?:(\d+(?:\.\d+)*)\s+)?"
        r"([A-ZÁÀÂÃÉÊÍÓÔÕÚÜÇ][A-ZÁÀÂÃÉÊÍÓÔÕÚÜÇ0-9 /,:()\-–—]{2,100})\s*$"
    )
    ignored = {"SUMÁRIO", "LISTA DE FIGURAS", "LISTA DE TABELAS", "ABSTRACT", "RESUMO"}
    for page_index, page in enumerate(pages, start=1):
        for line in page.splitlines():
            clean = " ".join(line.split())
            if ". . ." in clean or "....." in clean or len(clean) > 110:
                continue
            match = heading.match(clean)
            if not match:
                continue
            number, title = match.groups()
            if title in ignored or len(title.split()) > 14:
                continue
            candidates.append({"page": page_index, "number": number or "", "title": title.title()})
    # Preserve order while removing repeated headers.
    seen: set[tuple[int, str, str]] = set()
    result = []
    for candidate in candidates:
        key = (int(candidate["page"]), str(candidate["number"]), str(candidate["title"]))
        if key not in seen:
            seen.add(key)
            result.append(candidate)
    return result


def find_page(pages: list[str], titles: list[str], *, last: bool = False) -> int | None:
    matches: list[int] = []
    normalized_titles = [normalize(title) for title in titles]
    for page_index, page in enumerate(pages, start=1):
        if page_index <= 5:
            continue
        for raw_line in page.splitlines():
            if "....." in raw_line or ". . ." in raw_line:
                continue
            line = normalize(raw_line)
            # Remove the chapter number and an optional "chapter/capítulo" prefix.
            line = re.sub(r"^(?:chapter|capitulo)\s+", "", line)
            line = re.sub(r"^\d+(?:\.\d+)*\s*[.:-]?\s*", "", line)
            for title in normalized_titles:
                # A heading may carry a short complement, e.g. "Results and discussion".
                if line == title or line.startswith(title + " and ") or line.startswith(title + " e "):
                    matches.append(page_index)
                    break
            else:
                continue
            break
    if not matches:
        return None
    return matches[-1] if last else matches[0]


def page_excerpt(pages: list[str], start: int | None, count: int, limit: int) -> str:
    if start is None:
        return "[seção não localizada automaticamente]"
    excerpt = "\n\n".join(
        f"--- página física {index} ---\n{pages[index - 1].strip()}"
        for index in range(start, min(start + count, len(pages) + 1))
    )
    return excerpt[:limit]


def first_matching_block(text: str, start_patterns: list[str], end_patterns: list[str], limit: int) -> str:
    starts = []
    for pattern in start_patterns:
        starts.extend(match.start() for match in re.finditer(pattern, text, re.I | re.M))
    if not starts:
        return "[bloco não localizado automaticamente]"
    start = min(starts)
    tail = text[start:]
    ends = []
    for pattern in end_patterns:
        ends.extend(match.start() for match in re.finditer(pattern, tail[100:], re.I | re.M))
    end = (min(ends) + 100) if ends else min(len(tail), limit)
    return tail[: min(end, limit)].strip()


def build_packet(item: dict[str, str | int], pages: list[str], metrics: dict[str, int | str], headings: list[dict[str, str | int]]) -> str:
    text = "\n".join(pages)
    abstract = first_matching_block(
        text,
        [r"^\s*(?:Resumo|Abstract)\s*$"],
        [r"^\s*(?:Palavras[- ]chave|Keywords|Resumo|Abstract)\s*[:.]?"],
        4_500,
    )
    toc_page = find_page(pages, ["sumário", "contents", "table of contents"])
    intro_page = find_page(pages, ["introdução", "introduction"])
    method_page = find_page(
        pages,
        [
            "método",
            "metodologia",
            "materiais e métodos",
            "materiais e método do trabalho",
            "method",
            "methods",
            "methodology",
            "materials and methods",
            "project methodology",
        ],
    )
    development_page = find_page(
        pages,
        [
            "desenvolvimento",
            "desenvolvimento do trabalho",
            "projeto e implementação",
            "implementação",
            "implementation",
            "development",
            "system architecture",
            "solution architecture",
            "project development",
        ],
    )
    results_page = find_page(
        pages,
        [
            "resultados",
            "testes e avaliação",
            "avaliação",
            "resultados e discussão",
            "results",
            "evaluation",
            "experiments",
            "experimental results",
            "results and discussion",
            "testing and validation",
        ],
    )
    conclusion_page = find_page(
        pages,
        [
            "conclusão",
            "conclusões",
            "considerações finais",
            "conclusão e trabalhos futuros",
            "conclusões e trabalhos futuros",
            "conclusion",
            "conclusions",
            "conclusion and future work",
            "conclusions and future work",
            "final considerations",
        ],
        last=True,
    )
    heading_text = "\n".join(
        f"- p. {entry['page']}: {entry['number']} {entry['title']}".replace(":  ", ": ")
        for entry in headings[:120]
    )
    return f"""# Pacote de leitura — {item['id']}

## Identificação automática

- Título do catálogo: {item['title']}
- PDF: {item['relative_pdf']}
- Páginas: {metrics['pages']}
- Palavras extraídas: {metrics['words']}
- Caracteres extraídos: {metrics['characters']}
- Figuras identificadas: {metrics['figures']}
- Tabelas identificadas: {metrics['tables']}

## Resumo

{abstract}

## Sumário e estrutura inicial

{page_excerpt(pages, toc_page, 3, 8_000)}

## Mapa de títulos detectados

{heading_text or '[nenhum título detectado]'}

## Introdução

{page_excerpt(pages, intro_page, 3, 6_000)}

## Método

{page_excerpt(pages, method_page, 3, 6_000)}

## Desenvolvimento ou implementação

{page_excerpt(pages, development_page, 3, 6_000)}

## Testes, avaliação ou resultados

{page_excerpt(pages, results_page, 4, 8_000)}

## Conclusão ou considerações finais

{page_excerpt(pages, conclusion_page, 3, 7_000)}
"""


def main() -> None:
    ANALYSES.mkdir(parents=True, exist_ok=True)
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    items = selected_items()
    if len(items) != 50:
        raise RuntimeError(f"Esperadas 50 teses no índice; encontradas {len(items)}")

    corpus = []
    for position, item in enumerate(items, start=1):
        pdf = COLLECTION / str(item["relative_pdf"])
        text_file = TEXT_DIR / f"{item['id']}.txt"
        packet_file = PACKET_DIR / f"{item['id']}.md"
        run(["pdftotext", "-layout", str(pdf), str(text_file)])
        text = text_file.read_text(encoding="utf-8", errors="replace")
        pages = text.split("\f")
        if pages and not pages[-1].strip():
            pages.pop()
        info = run(["pdfinfo", str(pdf)])
        page_match = re.search(r"^Pages:\s+(\d+)", info, re.M)
        declared_pages = int(page_match.group(1)) if page_match else len(pages)
        if abs(declared_pages - len(pages)) > 1:
            raise RuntimeError(f"Contagem de páginas divergente em {pdf}")
        headings = heading_candidates(pages)
        metrics: dict[str, int | str] = {
            "pages": declared_pages,
            "characters": len(text),
            "words": len(re.findall(r"\b\w+\b", text, re.UNICODE)),
            "figures": max(count_unique_numbers(text, "Figura"), count_unique_numbers(text, "Figure")),
            "tables": max(count_unique_numbers(text, "Tabela"), count_unique_numbers(text, "Table")),
            "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
        }
        packet_file.write_text(build_packet(item, pages, metrics, headings), encoding="utf-8")
        corpus.append({**item, **metrics, "headings": headings, "packet": str(packet_file)})
        print(f"[{position:02d}/50] {item['id']}: {declared_pages} páginas, {metrics['words']} palavras")

    MANIFEST.write_text(json.dumps(corpus, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Manifesto: {MANIFEST}")
    print(f"Textos temporários: {TEXT_DIR}")
    print(f"Pacotes temporários: {PACKET_DIR}")


if __name__ == "__main__":
    main()
