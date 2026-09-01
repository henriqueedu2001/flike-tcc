# FLIKE — Trabalho de Conclusão de Curso

Fontes da monografia e documentação de apoio do projeto FLIKE.

## Compilar a tese

Na raiz do repositório, execute:

```bash
./compile.sh
```

O PDF final fica em `pdfs/FLIKE.pdf`. O script encontra o projeto pelo próprio
caminho, portanto também pode ser chamado de outro diretório.

Requisitos: **Python 3.9+**, Bash e `curl` para o primeiro download. Não precisa
de Overleaf, Docker, sudo nem de uma distribuição TeX instalada. Há binários
configurados para Linux x86_64/ARM64 e macOS Intel/Apple Silicon; a validação
deste projeto foi feita em Linux x86_64.

Na primeira execução, o script baixa o **Tectonic 0.17.0** oficial, confere seu
SHA-256 e o instala em `.tools/`. O motor baixa os pacotes/fontes LaTeX de que
a tese precisa para `.cache/tectonic/`. Essa preparação requer internet e pode
demorar mais; os fontes da tese não são enviados a um serviço de compilação.

O Tectonic executa as passagens necessárias de LaTeX e BibTeX automaticamente.
O preâmbulo seleciona fontes Unicode por arquivo no Tectonic/XeTeX, preservando
acentos e travessões sem depender das fontes do sistema. Os capítulos usam
`\input` com quebras de página, mantendo uma única bibliografia global e
evitando execuções desnecessárias de BibTeX em auxiliares de cada capítulo.
Os arquivos auxiliares, logs e SyncTeX ficam em `build/`, sem poluir os fontes.
Se nenhum arquivo de `FLIKE/`, o motor ou os scripts mudou e o PDF permanece
intacto, o comando retorna imediatamente, sem recompilar.

```bash
./compile.sh --force            # Recompila mesmo sem mudanças
./compile.sh --offline          # Não permite downloads
./compile.sh --force --offline  # Refaz o PDF usando apenas o cache local
./compile.sh --help
```

O modo offline requer o motor e todos os pacotes necessários já baixados. Um
pacote novo adicionado ao texto pode exigir outra execução com internet.
Use `--force` quando quiser atualizar conteúdo dependente da data/hora ou de
recursos externos a `FLIKE/`; mantenha os arquivos da tese dentro dessa pasta
para que sejam considerados na detecção de alterações.

Se houver erro, o comando retorna código diferente de zero e preserva o último
`pdfs/FLIKE.pdf` válido. Veja `build/compile.log`, `build/main.log` e os logs
de bibliografia em `build/`. O PDF só é substituído após compilação bem-sucedida;
não confunda um PDF anterior preservado com o resultado da tentativa que falhou.
Erros reportados pelo BibTeX, caracteres ausentes e referências indefinidas
também impedem a publicação do PDF, mesmo se o motor encerrar com sucesso.
Execuções simultâneas são serializadas. O modo `--untrusted` do Tectonic é usado
para desabilitar recursos perigosos, como shell escape.

O motor, cache, auxiliares e PDF gerado estão no `.gitignore`. O PDF histórico
`pdfs/FLIKE-referencia-2026-08-30.pdf` permanece separado e não é sobrescrito.
Avisos editoriais dos fontes, como bibliografia vazia ou linhas largas, precisam
ser revisados na escrita da tese; compilar não valida seu conteúdo acadêmico.

Referências do motor: [instalação oficial](https://tectonic-typesetting.github.io/book/latest/installation/)
e [comando de compilação](https://tectonic-typesetting.github.io/book/latest/v2cli/compile.html).

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
pdfs/                 # PDF final gerado e PDF histórico de referência
scripts/compile.py    # Instalação local, cache e orquestração da compilação
compile.sh            # Comando único de entrada
build/                # Auxiliares e logs gerados (ignorado pelo Git)
.tools/               # Motor Tectonic local (ignorado pelo Git)
.cache/               # Pacotes/fontes baixados (ignorado pelo Git)
```

O arquivo de entrada é `FLIKE/main.tex`. Os caminhos do LaTeX são relativos
ao diretório `FLIKE/`, usado automaticamente pelo script como diretório de
trabalho. As dependências locais do abnTeX2 permanecem junto ao arquivo
principal para preservar sua descoberta pelo LaTeX e pelo BibTeX.

Os nomes históricos no texto da tese foram preservados; a revisão editorial
da nomenclatura fica separada da organização dos arquivos.

O levantamento está em `docs/ARQUITETURA_E_ESTADO_DO_PROJETO.md`.
O PDF original foi realocado para `pdfs/FLIKE-referencia-2026-08-30.pdf`;
ele é uma referência histórica, não um resultado gerado dos fontes atuais.
