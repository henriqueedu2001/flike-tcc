# FLIKE — orientações institucionais para a monografia

## 1. Finalidade

Este documento consolida as regras e recomendações encontradas na pasta `orientações-tcc`. Ele funciona como checklist institucional para a escrita, compilação e revisão do TCC do FLIKE. Não substitui decisões do orientador nem uma eventual atualização das regras do PCS para 2026.

Foram examinados os quatro PDFs, com leitura completa dos documentos curtos e leitura dirigida das seções pertinentes da diretriz de 95 páginas, além do conteúdo do arquivo ZIP, do link para a apresentação da professora Cíntia e dos 31 minutos do vídeo da professora Selma. A apresentação em vídeo foi confrontada com os slides e com o documento textual para separar explicações orais de regras escritas.

## 2. Fontes e autoridade

| Fonte | Data indicada | Função |
| --- | --- | --- |
| [`DiretrizesTesesDissertacoes rev 4 (6).pdf`](<../orientações-tcc/DiretrizesTesesDissertacoes rev 4 (6).pdf>) | 2013 | Regras de estrutura, apresentação gráfica, citações e referências da Escola Politécnica. |
| [`Recomendacoes para monografia 2024.pdf`](<../orientações-tcc/Recomendacoes para monografia 2024.pdf>) | material de 2024, cabeçalho de 2023 | Recomendação específica do PCS para conteúdo e capítulos da monografia de Projeto de Formatura. |
| [`Projeto de Formatura 2024.pdf`](<../orientações-tcc/Projeto de Formatura 2024.pdf>) | 2024 | Slides que resumem as recomendações específicas do PCS. |
| [`TCC-Documentacao-20240226(ProfaCintia).pdf`](<../orientações-tcc/TCC-Documentacao-20240226(ProfaCintia).pdf>) | 26/02/2024 | Uso das diretrizes, do LaTeX, do abnTeX2 e do projeto oficial TCC-PCS-EPUSP. |
| [`TCC-Documentação-20240226(ProfaSelma).mp4`](<../orientações-tcc/TCC-Documentação-20240226(ProfaSelma).mp4>) | 2024 | Explicação oral do conteúdo recomendado e perguntas dos alunos. |
| [`TCC-PCS-EPUSP (ArquivosLatexProfaCintia).zip`](<../orientações-tcc/TCC-PCS-EPUSP (ArquivosLatexProfaCintia).zip>) | arquivos de 22/05/2023 | Modelo LaTeX fornecido para a monografia do PCS. |
| [`LinkApresentaçãoProfaCintia.txt`](<../orientações-tcc/LinkApresentaçãoProfaCintia.txt>) | sem data interna | Link da aula sobre LaTeX, ABNT e abnTeX2 no e-Aulas USP. |

### 2.1 Ordem prática de precedência

1. Decisões expressas do orientador e regras vigentes da disciplina.
2. Recomendações específicas do PCS de 2024.
3. Modelo LaTeX TCC-PCS-EPUSP fornecido pela professora Cíntia.
4. Diretrizes da Poli, revisão 4, para assuntos de forma, citações e referências.

O vídeo registra que os docentes decidiram continuar usando a revisão 4 da Poli no Projeto de Formatura, apesar de existir uma publicação posterior da USP. Também reforça que o sumário é uma sugestão e deve ser adaptado ao trabalho em acordo com o orientador.

Como os materiais específicos são de 2024 e as diretrizes gerais são de 2013, prazos, procedimento de entrega, ficha catalográfica, folha de aprovação e eventual norma atualizada devem ser confirmados para 2026. Regras de depósito de pós-graduação presentes nas diretrizes — número de exemplares, capa dura e CD — não devem ser aplicadas automaticamente ao TCC.

## 3. Estrutura de conteúdo recomendada pelo PCS

Os documentos confirmam a macroestrutura já adotada no plano do FLIKE:

1. Introdução;
2. Aspectos Conceituais;
3. Método do Trabalho;
4. Especificação de Requisitos;
5. Desenvolvimento do Trabalho;
6. Considerações Finais.

Essa estrutura não é uma imposição invariável. O tipo de produto e o orientador determinam as adaptações. Para o FLIKE, que é um sistema com software, firmware e hardware, a divisão é adequada e foi aprovada pela equipe como base editorial.

### 3.1 Introdução

#### Motivação

- Apresentar o contexto e um estado da arte resumido.
- Citar trabalhos que sustentem o contexto; o contexto não deve ser inventado pela equipe.
- Reservar a discussão aprofundada das referências para Aspectos Conceituais.

#### Objetivo

- Responder de forma precisa e concisa à pergunta “o que é o trabalho?”.
- A explicação oral recomenda tornar inequívoca a frase “o objetivo do trabalho é...”.
- Formular um objetivo compatível com o produto efetivamente desenvolvido.

#### Justificativa

- Responder por que o trabalho é importante.
- Sustentar importância social ou técnica com referências e comparação com trabalhos relevantes.
- Não usar como justificativa principal o aprendizado pessoal dos integrantes.

#### Organização do trabalho

- Descrever brevemente capítulos e demais partes.
- Escrever quando a estrutura estiver estável; a apresentação oral recomenda deixar essa subseção para depois se o sumário ainda não estiver decidido.

### 3.2 Aspectos Conceituais

- Apresentar os conceitos empregados e a revisão da literatura.
- Selecionar tópicos específicos para compreender o artefato e seus resultados.
- Discutir criticamente os trabalhos relevantes, em vez de transcrever definições ou produzir um catálogo de tecnologias.
- Definir o conteúdo em acordo com o orientador.

### 3.3 Método do Trabalho

- Apresentar o processo e suas fases: levantamento, requisitos, projeto, implementação e testes, conforme o processo real.
- Manter a descrição objetiva e preferencialmente cronológica.
- Não antecipar especificações, arquitetura, implementação ou resultados.
- Os detalhes e resultados de cada fase pertencem aos capítulos seguintes.

A professora Selma destacou esse ponto porque monografias anteriores concentraram quase todo o trabalho no capítulo de método e deixaram os capítulos 4 e 5 vazios. Para o FLIKE, o capítulo 3 deverá explicar **como** a equipe trabalhou; os produtos e evidências ficarão nos capítulos 4 e 5.

### 3.4 Especificação de Requisitos

- Definir o produto do trabalho e seus requisitos.
- Adaptar a especificação ao tipo de produto.
- Para um desenvolvimento de sistema, registrar o comportamento e as qualidades esperadas.
- Definir os requisitos em acordo com o orientador.

As orientações não exigem uma notação específica. A matriz rastreável proposta no plano do FLIKE é compatível com a regra e acrescenta o rigor observado nas melhores teses.

### 3.5 Desenvolvimento do Trabalho

- Mostrar como requisitos foram transformados em produtos.
- Adaptar seções ao processo real.
- Apresentar apenas tecnologias relevantes.
- Descrever projeto e implementação com justificativa das decisões.
- Para sistemas, considerar arquitetura, banco de dados e interface humano-computador.
- Incluir testes e avaliação com estratégia, plano e procedimentos.

O exemplo do PCS separa testes de hardware, software, módulo, integração e validação. Para o FLIKE, isso confirma a necessidade de testar protocolo, frontend/backend, firmware, leitura óptica, integração e acionamento físico em níveis distintos.

### 3.6 Considerações Finais

#### Conclusões

- Fazer o balanço do que foi e do que não foi atingido, com justificativas.
- Responder ao problema e aos objetivos usando resultados já apresentados.
- Não ocultar resultados desfavoráveis.

O vídeo alerta contra remover silenciosamente objetivos não atingidos e deslocar tudo para trabalhos futuros. Mudanças de escopo precisam de acordo com o orientador, e o trabalho ainda precisa preservar uma contribuição mínima coerente.

#### Contribuições

- Distinguir de forma explícita o que já existia do que foi produzido pela equipe.
- Identificar artefatos, decisões e conhecimento de autoria dos integrantes.
- Antecipar a pergunta provável da banca: “qual parte é de vocês?”.

#### Perspectivas de continuidade

- Registrar atividades que podem continuar o projeto.
- Não apresentar promessa futura como entrega atual.

## 4. Requisitos formais principais

### 4.1 Elementos pré-textuais

O conjunto aplicável ao TCC deve seguir as diretrizes e o modelo fornecido. Os materiais tratam como centrais:

- capa;
- folha de rosto;
- ficha catalográfica;
- folha ou termo de aprovação, conforme o procedimento institucional;
- resumo em português;
- abstract em inglês;
- sumário.

Dedicatória, agradecimentos e epígrafe são opcionais. Listas de figuras, tabelas, quadros, abreviaturas, siglas e símbolos devem existir apenas quando houver conteúdo que justifique cada lista.

Itens de aprovação e catalogação dependem do momento institucional. A versão final deve substituir documentos provisórios fornecidos pelo modelo.

### 4.2 Resumo e abstract

O resumo deve:

- apresentar objetivo, método, resultados mais significativos e conclusões;
- ser preferencialmente redigido na terceira pessoa do singular e na voz ativa;
- formar um único parágrafo;
- conter no máximo 500 palavras;
- ser seguido por palavras-chave separadas por ponto e finalizadas por ponto.

O abstract deve ter o mesmo conteúdo e as mesmas características, em inglês, seguido de keywords. Ambos devem ser escritos ou revisados quando resultados e conclusões estiverem estáveis.

### 4.3 Página e tipografia

As diretrizes estabelecem:

- papel A4;
- margens no anverso: esquerda e superior de 3 cm, direita e inferior de 2 cm;
- fonte de corpo em tamanho 12;
- espaçamento de 1,5 no corpo;
- espaço simples em citações longas, notas, referências, legendas e fontes;
- fonte menor, usualmente tamanho 10, nesses elementos especiais;
- capítulos primários iniciando em nova página;
- contagem desde a folha de rosto e exibição dos algarismos a partir da parte textual;
- paginação contínua em apêndices e anexos.

A revisão 4 menciona Arial, enquanto o modelo oficial do PCS usa Latin Modern por meio do abnTeX2. Como os próprios docentes afirmam que o modelo fornecido evita a configuração manual de título, página e margens, o projeto LaTeX oficial deve prevalecer sobre uma substituição manual de fonte, salvo orientação expressa em contrário.

### 4.4 Redação e seções

- Usar linguagem clara, objetiva, concisa, precisa e terminologicamente consistente.
- Numerar progressivamente as seções.
- Escrever a forma completa antes da primeira ocorrência de uma sigla.
- Não antecipar resultados na introdução.
- Apresentar resultados de forma objetiva, inclusive quando contrariem a expectativa da equipe.
- Fundamentar conclusões nos resultados e na discussão.

## 5. Citações e referências

### 5.1 Regra de correspondência

- Todo trabalho listado nas referências deve ser citado no texto.
- Toda citação deve possuir uma entrada bibliográfica correspondente.
- O PCS recomenda o sistema autor-data.
- Com autor-data, a lista deve ser ordenada alfabeticamente.
- Sites podem ser usados quando adequados e referenciados segundo as regras.
- Informações informais podem ser citadas no texto e registradas em nota de rodapé, não misturadas à bibliografia formal.

### 5.2 Citações diretas

As recomendações desaconselham um texto composto por muitas citações diretas. A equipe deve compreender a fonte, redigir uma síntese própria e preservar a referência.

- Citação direta de até três linhas: no parágrafo, entre aspas, com autoria, ano e página.
- Citação direta com mais de três linhas: bloco com recuo de 4 cm, fonte menor, espaçamento simples e sem aspas.
- Traduções devem ser identificadas conforme a regra aplicável.
- Citação de citação (`apud`) deve ser excepcional; a fonte original é preferível.

## 6. Figuras, quadros, tabelas e equações

### 6.1 Ilustrações

- Citar cada elemento no texto antes ou próximo de sua aparição.
- Posicioná-lo perto do parágrafo relevante.
- Colocar identificação, número e título na parte superior.
- Colocar obrigatoriamente a fonte na parte inferior, inclusive quando for “elaborado pelos autores”.
- Traduzir figuras e tabelas incorporadas de trabalhos estrangeiros.
- Explicar a função do elemento; a imagem não deve ser decorativa.

### 6.2 Tabelas

- Fazer a tabela compreensível por si mesma.
- Usar título na parte superior e fonte ou notas abaixo.
- Evitar linhas verticais.
- Repetir cabeçalho quando houver continuação em outra página.
- Identificar `continua`, `continuação` e `conclusão` quando a tabela atravessar páginas.

### 6.3 Equações

- Destacar e centralizar quando separadas do texto.
- Numerar entre parênteses quando necessário.
- Fazer referência explícita às equações no texto.

## 7. Apêndices e anexos

| Elemento | Autoria | Uso recomendado |
| --- | --- | --- |
| Apêndice | elaborado pela equipe | Casos de uso detalhados, protocolo completo, dados de teste e documentação que complementa o argumento. |
| Anexo | produzido externamente | Documento institucional, legenda normativa ou material externo necessário à comprovação. |

Ambos são opcionais, usam letras maiúsculas consecutivas e mantêm a paginação contínua. A explicação oral oferece um critério editorial simples: se o detalhe interromper o raciocínio do capítulo, mover para apêndice ou anexo e manter no corpo apenas o necessário.

## 8. Compatibilidade do repositório com o modelo oficial

O ZIP contém `main.tex`, seis arquivos de capítulos, referências, exemplos, ficha provisória e os arquivos do abnTeX2. A comparação com `FLIKE/` mostrou que:

- `abntex2.cls`, `abntex2cite.sty`, `abntex2-num.bst` e `abntex2-alf.bst` são byte a byte idênticos aos arquivos oficiais;
- os capítulos, referências, exemplos e pré-textuais apenas foram organizados em subdiretórios;
- `main.tex` foi adaptado para Tectonic/XeTeX, Unicode, caminhos organizados e bibliografia global;
- as adaptações preservam a base institucional.

Conclusão: **não é necessário substituir ou migrar o template atual**. Devemos manter a compatibilidade e validar visualmente o PDF após cada alteração relevante.

## 9. Pendências já visíveis no TCC atual

Estas pendências foram apenas registradas; os capítulos não foram alterados nesta etapa.

### Obrigatórias antes da versão final

- Substituir a ficha catalográfica provisória pela emitida no procedimento aplicável de 2026.
- Confirmar e incluir a folha ou termo de aprovação correto.
- Remover ou completar o agradecimento de exemplo.
- Validar a dedicatória dos três autores ou removê-la.
- Atualizar os metadados PDF, que ainda usam palavras genéricas de `abnt`, `latex` e `abntex`.
- Reconstruir resumo, abstract, palavras-chave e keywords em parágrafo e pontuação adequados.
- Remover CAUSP-LOCK e usar FLIKE.
- Eliminar alegações incorretas de uso único, assinatura digital, irretratabilidade e segurança garantida.
- Remover referências de exemplo e manter somente obras citadas.
- Verificar se todas as figuras e tabelas possuem título, fonte, chamada no texto e tradução quando necessária.
- Garantir que listas pré-textuais vazias ou desnecessárias não sejam emitidas.

### Pendências de conteúdo já conhecidas

- A organização do Capítulo 1 ainda contém texto de exemplo.
- O Capítulo 3 ainda contém instruções do modelo no lugar do método real.
- Requisitos antigos ainda contêm “uso único”, “irretratabilidade” e “assinatura eletrônica”.
- Os capítulos ainda alternam FLIKE e CAUSP-LOCK.
- Contribuições próprias dos três integrantes ainda precisam ser identificadas.

## 10. Checklist de revisão de cada rodada

Além da compilação técnica, cada rodada futura deverá verificar:

1. a seção cumpre a função institucional de seu capítulo;
2. fatos externos possuem fontes;
3. todas as citações têm referências e vice-versa;
4. figuras e tabelas são chamadas, traduzidas quando necessário e têm fonte;
5. termos e siglas são definidos e usados de forma consistente;
6. método, resultado e conclusão não são misturados;
7. contribuição da equipe está distinguível de trabalho anterior;
8. resultados negativos ou não atingidos permanecem explícitos;
9. detalhe excessivo foi movido para apêndice ou anexo quando apropriado;
10. o PDF compilado mantém margens, paginação, legibilidade e referências cruzadas corretas.

## 11. Confirmações que ainda devem ser obtidas

- Qual versão das diretrizes e normas será considerada vigente para a entrega de 2026?
- O orientador aprova formalmente a estrutura proposta para o FLIKE?
- Qual é o procedimento atual para ficha catalográfica e folha de aprovação?
- Há modelo atualizado posterior ao pacote de 2023?
- Quais são os prazos, formato de entrega e regras da apresentação final de 2026?
- Existe limite ou recomendação de páginas específico da disciplina ou do orientador?

Nenhum dos documentos fornecidos fixa limite mínimo ou máximo de páginas para a monografia.
