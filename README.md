# FLIKE — Trabalho de Conclusão de Curso

Fontes da monografia e documentação de apoio do projeto FLIKE.

## Organização

```text
FLIKE/
├── main.tex          # Documento principal
├── capitulos/        # Os seis capítulos da monografia
├── imagens/          # Diagramas e demais imagens
├── pre-textuais/     # Ficha catalográfica em PDF
├── referencias/      # Bibliografia da monografia
├── exemplos/         # Exemplos do modelo, fora do documento ativo
└── abntex2*          # Classe, estilos e opções locais do abnTeX2
docs/                 # Levantamento de arquitetura e documentação de apoio
pdfs/                 # PDF de referência recebido, preservado sem recompilação
```

O arquivo de entrada é `FLIKE/main.tex`. Os caminhos do LaTeX são relativos
ao diretório `FLIKE/`, que deve ser o diretório de trabalho de uma futura
compilação. As dependências locais do abnTeX2 permanecem junto ao arquivo
principal para preservar sua descoberta pelo LaTeX e pelo BibTeX.

Esta reorganização não inclui compilador, scripts de build ou recompilação.
Os nomes históricos no texto da tese foram preservados; a revisão editorial
da nomenclatura fica separada da organização dos arquivos.

O levantamento está em `docs/ARQUITETURA_E_ESTADO_DO_PROJETO.md`.
O PDF original foi realocado para `pdfs/FLIKE-referencia-2026-08-30.pdf`;
ele é uma referência histórica, não um resultado gerado dos fontes atuais.
