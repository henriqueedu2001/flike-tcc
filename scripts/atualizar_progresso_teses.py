#!/usr/bin/env python3
"""Atualiza o registro persistente a partir das fichas individuais existentes."""

from __future__ import annotations

import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
ANALYSES = REPO / "materiais" / "teses-referencia" / "pcs" / "analises"
MANIFEST = ANALYSES / "CORPUS.json"
PROGRESS = ANALYSES / "PROGRESSO.md"


def main() -> None:
    theses = json.loads(MANIFEST.read_text(encoding="utf-8"))
    completed = []
    rows = []
    for order, thesis in enumerate(theses, start=1):
        sheet = ANALYSES / str(thesis["year"]) / f"{thesis['id']}.md"
        done = sheet.exists()
        if done:
            completed.append(thesis)
        relative_sheet = sheet.relative_to(ANALYSES).as_posix()
        link = f"[{relative_sheet}]({relative_sheet})" if done else "—"
        rows.append(
            f"| {order} | {thesis['id']} | {thesis['pages']} | "
            f"{'concluída' if done else 'pendente'} | {link} |"
        )

    pages = sum(item["pages"] for item in completed)
    words = sum(item["words"] for item in completed)
    characters = sum(item["characters"] for item in completed)
    state = "leitura concluída" if len(completed) == len(theses) else "leitura em andamento"
    content = f"""# Progresso da leitura das teses do PCS

- Início da leitura: 31/08/2026.
- Coleção: 50 PDFs, 4.064 páginas, 952.287 palavras extraídas.
- Critérios: `docs/CRITERIOS_ANALISE_TESES_REFERENCIA.md`.
- Teses com ficha concluída: **{len(completed)} de {len(theses)}**.
- Páginas correspondentes às fichas concluídas: **{pages} de 4.064**.
- Texto correspondente: **{words} palavras; {characters} caracteres extraídos**.
- Estado: **{state}**.

| Ordem | Ano-grupo | Páginas | Estado | Ficha |
| ---: | --- | ---: | --- | --- |
{chr(10).join(rows)}

Uma tese só entra na contagem quando sua ficha individual está salva. A relação entre
páginas, palavras e a cota de uso é apenas uma aproximação: densidade, figuras, tabelas e
complexidade analítica variam entre trabalhos, e a interface não expõe o consumo exato de
tokens desta execução.
"""
    PROGRESS.write_text(content, encoding="utf-8")
    print(f"{len(completed)}/{len(theses)} teses; {pages}/4064 páginas; {words} palavras")


if __name__ == "__main__":
    main()
