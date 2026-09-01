# FLIKE — critérios para análise das teses de referência

## 1. Objetivo

Este documento define, antes da leitura comparativa, o que será observado nas 50 monografias recentes do PCS. O objetivo não é atribuir nota acadêmica aos trabalhos nem declarar quais são “bons” de forma absoluta. A análise busca identificar escolhas editoriais que possam orientar a escrita do TCC do FLIKE.

As teses são avaliadas como **modelos de comunicação acadêmica**. A correção científica de resultados especializados fora do domínio do FLIKE não será reavaliada. Uma tese pode ser excelente em seu tema e ainda ter pouca utilidade como modelo para um projeto integrado de software, firmware e hardware.

## 2. Escala de observação

Cada aspecto recebe uma marca de 0 a 4 nas fichas individuais:

| Marca | Interpretação editorial |
| --- | --- |
| 0 | Ausente ou impossível de avaliar no arquivo |
| 1 | Muito fraco, fragmentário ou apenas declarado |
| 2 | Suficiente, mas com lacunas relevantes |
| 3 | Bom, claro e utilizável como referência |
| 4 | Excelente para a finalidade observada |

As marcas servem para comparação e triagem. Elas sempre devem ser acompanhadas de justificativa textual; não representam uma avaliação oficial da USP.

## 3. Critérios principais

### C01 — Delimitação do problema

Observar se a introdução apresenta contexto, problema concreto, público ou sistema afetado, consequências e fronteira do trabalho. Identificar se fatos externos estão apoiados por fontes e se relatos do projeto são distinguidos de evidências científicas.

### C02 — Objetivos e escopo

Verificar se objetivo geral e objetivos específicos são claros, verificáveis e compatíveis com o trabalho desenvolvido. Observar como exclusões, hipóteses e limitações iniciais são declaradas.

### C03 — Organização e progressão argumentativa

Avaliar se a ordem dos capítulos conduz o leitor do problema à fundamentação, método, desenvolvimento, resultados e conclusão. Registrar como a seção de organização do trabalho antecipa essa sequência.

### C04 — Fundamentação e trabalhos relacionados

Observar seleção, atualidade e função das referências. Distinguir revisão que apenas define tecnologias de revisão que compara alternativas, identifica lacunas e justifica decisões.

### C05 — Método do trabalho

Verificar se o método explica o processo real, as fases, decisões, ferramentas e critérios de avaliação de forma reproduzível. Identificar separação entre método e resultados.

### C06 — Requisitos e rastreabilidade

Nos trabalhos que especificam sistemas, observar identificação, fonte, prioridade, critérios de aceitação e ligação dos requisitos com arquitetura, implementação e testes.

### C07 — Arquitetura e decisões de projeto

Avaliar clareza das fronteiras, responsabilidades, interfaces, fluxos e alternativas consideradas. Observar se diagramas são fiéis à implementação e explicados no texto.

### C08 — Descrição da implementação

Verificar se o texto explica comportamento, módulos, integrações e decisões importantes sem se reduzir a tutorial, catálogo de bibliotecas ou reprodução de código.

### C09 — Avaliação e reprodutibilidade

Observar perguntas de avaliação, casos de teste, métricas, ambiente, versões, amostra, número de repetições, critérios de sucesso e disponibilidade de dados brutos.

### C10 — Apresentação e discussão dos resultados

Avaliar se resultados são apresentados com tabelas ou figuras adequadas, interpretados em relação aos objetivos e comparados com expectativas ou trabalhos relacionados. Identificar distinção entre observação, inferência e opinião.

### C11 — Limitações e honestidade acadêmica

Verificar se requisitos não atendidos, ameaças à validade, riscos, falhas e resultados negativos são registrados e incorporados às conclusões.

### C12 — Conclusões e contribuições

Observar se a conclusão responde aos objetivos usando resultados do próprio trabalho, separa contribuição, limitação e trabalho futuro e evita introduzir informação nova.

### C13 — Figuras, tabelas e legibilidade

Avaliar qualidade, tamanho, fonte, legenda, menção no texto e função argumentativa dos elementos visuais. Registrar bons tipos de diagramas para projetos de engenharia.

### C14 — Referências e normalização

Observar consistência de citações, qualidade das fontes, correspondência entre citações e bibliografia, elementos pré-textuais, siglas, referências cruzadas e apresentação geral.

### C15 — Aplicabilidade ao FLIKE

Avaliar quanto a tese ajuda especificamente a escrever um trabalho com aplicação web, backend, credencial criptográfica, firmware, circuito, operação offline, requisitos de acessibilidade e avaliação de protótipo.

## 4. Aspectos extraídos de cada tese

Cada ficha individual deve registrar:

1. ano, grupo, título e número de páginas;
2. autores e orientação, quando extraíveis com segurança;
3. objetivo declarado;
4. macroestrutura e capítulos;
5. natureza do trabalho e método usado;
6. artefatos produzidos;
7. forma de especificar requisitos e arquitetura;
8. procedimento de testes ou avaliação;
9. resultados e limitações declarados;
10. quantidade aproximada de figuras, tabelas e referências;
11. marcas C01–C15 com justificativa;
12. três escolhas editoriais que funcionam;
13. três cuidados ou problemas a evitar;
14. elementos diretamente aproveitáveis como inspiração para o FLIKE;
15. classificação de prioridade para leitura comparativa aprofundada.

## 5. Prioridade para aprofundamento

Depois da primeira leitura, cada trabalho será classificado:

- **A — modelo prioritário:** forte qualidade editorial e alta aplicabilidade ao FLIKE;
- **B — referência parcial:** contém seções ou técnicas úteis, mas não serve como modelo global;
- **C — contraste:** útil principalmente para reconhecer problemas, limitações ou estruturas pouco adequadas;
- **D — baixa aderência:** tema e forma oferecem pouco material comparável, embora a ficha básica seja preservada.

## 6. Comparações transversais planejadas

Ao final das 50 fichas, a síntese deve responder:

1. Quais macroestruturas são mais comuns nos trabalhos recentes do PCS?
2. Como objetivos são formulados e retomados nas conclusões?
3. Como projetos de software, hardware e sistemas embarcados distribuem o capítulo de desenvolvimento?
4. Quais trabalhos apresentam requisitos verificáveis e rastreáveis?
5. Quais diagramas realmente ajudam a compreender a solução?
6. Como testes são descritos e quais informações de reprodutibilidade aparecem?
7. Como limitações e resultados incompletos são comunicados?
8. Qual profundidade conceitual é usada antes da descrição técnica?
9. Como trabalhos com impacto social evitam ou cometem extrapolações sem avaliação com usuários?
10. Quais padrões devem compor o modelo editorial do FLIKE?

## 7. Controle de leitura e limite de uso

O progresso será persistido em `materiais/teses-referencia/pcs/analises/PROGRESSO.md`. Uma tese só contará como lida quando sua ficha individual estiver salva com os itens obrigatórios e quando suas seções de introdução, fundamentação, método, desenvolvimento, avaliação e conclusão tiverem sido examinadas, quando existentes.

O registro acumulará quantidade de teses, páginas dos PDFs concluídos e caracteres do texto extraído. Se a execução for interrompida por limite de uso, esses valores permitirão estimar a quantidade de páginas processada durante a sessão. A relação não mede tokens com precisão, pois páginas variam em densidade e ferramentas de extração também consomem contexto de formas diferentes.
