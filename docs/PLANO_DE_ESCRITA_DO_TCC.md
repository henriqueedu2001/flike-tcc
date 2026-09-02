# FLIKE — plano de escrita do TCC

## 1. Finalidade deste documento

Este documento organiza a produção da monografia do FLIKE. Ele preserva a estrutura geral do trabalho atual — seis capítulos, além dos elementos pré-textuais e pós-textuais — e transforma essa estrutura em um roteiro de pesquisa, redação, coleta de evidências e revisão.

O plano será validado pela equipe antes da reescrita dos capítulos. Ele não substitui as orientações formais da Escola Politécnica da USP nem decisões do orientador. Teses de referência fornecidas pela equipe serão usadas para calibrar profundidade, extensão, organização visual e estilo argumentativo, sem copiar texto, resultados ou estrutura de forma mecânica. A estrutura de seis capítulos foi confirmada pelas recomendações do PCS de 2024, com possibilidade de adaptação em acordo com o orientador.

As duas fontes internas centrais são:

- `pdfs/FLIKE-referencia-2026-08-30.pdf`, que registra a estrutura atual do TCC;
- `docs/ARQUITETURA_E_ESTADO_DO_PROJETO.md`, que consolida a arquitetura, o estado do código, as decisões confirmadas e as lacunas de evidência.

As regras editoriais e institucionais extraídas dos materiais fornecidos pela equipe estão consolidadas em `docs/ORIENTACOES_INSTITUCIONAIS_TCC.md`. Esse documento deverá integrar a verificação de todas as rodadas.

O projeto do Laboratório de Processadores que antecedeu o FLIKE foi analisado em `docs/ANALISE_MATERIAL_HISTORICO_CAUSP_LOCK.md`. Ele será citado somente como origem histórica e como base do circuito elétrico reaproveitado. O produto descrito nesta monografia é o FLIKE, com credenciais autenticadas por AES-CMAC. Segundo confirmação da equipe, o protótipo realizou uma demonstração física ponta a ponta em 31/08/2026.

### 1.1 Estado da execução em 01/09/2026

| Passo | Estado | Registro |
| --- | --- | --- |
| Fase A, passo 0 | aprovado | Processo incremental aprovado pela equipe. |
| Fase A, passo 1 | concluído | 50 monografias de 2024 e 2025 coletadas e validadas. |
| Fase A, passo 2 | aprovado | 50 fichas concluídas; padrão técnico, detalhado e visual aprovado pela equipe. |
| Fase A, passo 3 | aprovado | Contrato acadêmico aprovado pela equipe em 01/09/2026. |
| Fase A, passo 4 | aprovado | Vocabulário e alegações controladas revisados e aprovados pela equipe em 01/09/2026. |
| Pesquisa transversal de referências — conjunto original | aprovado | Oito obras inventariadas; sete PDFs lidos integralmente e a norma ISO analisada pelos conteúdos oficiais públicos. Fichamento aceito pela equipe em 01/09/2026. |
| Pesquisa transversal de referências — conjunto complementar | aprovado | Dez fontes selecionadas, obtidas, validadas e fichadas para cobrir autismo e ambiente, acessibilidade web, QR Code, AES-CMAC, gestão de chaves, LGPD e ESP32. Fichamento aceito pela equipe em 01/09/2026. |

## 2. Tese central proposta

A formulação completa e aprovada deste bloco está em `docs/CONTRATO_ACADEMICO_TCC.md`. Esse documento prevalece em caso de diferença de detalhamento.

A monografia deve apresentar o FLIKE como o **projeto e protótipo de um sistema de controle de acesso físico**, composto por aplicação web, API, banco de dados, credenciais temporárias em QR Code e uma tranca baseada em ESP32-CAM. Sua decisão arquitetural característica é autenticar a credencial localmente, sem consultar o servidor no momento da leitura. A janela temporal faz parte do formato e da política pretendida, mas sua verificação completa não foi localizada no firmware preservado.

A contribuição acadêmica não deve ser formulada como a comprovação de que o sistema resolveu o problema de acessibilidade ou atingiu segurança de produção. Não houve avaliação com o público-alvo. A equipe realizou testes bem-sucedidos de QR Code e AES-CMAC. Em 31/08/2026, o protótipo executou em uma única demonstração a leitura e decodificação do QR Code, a validação do comprimento, do identificador da tranca, da janela temporal e do AES-CMAC, a emissão do sinal `HIGH` e o acionamento da fechadura. A integração física completa está demonstrada e deverá ser afirmada categoricamente na tese. O checkout atualmente preservado não contém todo o firmware usado no ensaio. A contribuição defensável é:

1. a especificação de uma solução de acesso voltada à redução de interações humanas obrigatórias;
2. a arquitetura integrada de frontend, backend, protocolo de credencial e dispositivo embarcado;
3. a implementação dos componentes descritos no estado real do projeto;
4. a análise técnica dos resultados, das limitações e dos riscos da validação offline.

### 2.1 Pergunta de pesquisa proposta

> Como projetar e implementar um protótipo de controle de acesso físico para espaços institucionais compartilhados que integre a gestão web de permissões a credenciais temporárias em QR Code autenticadas localmente por uma tranca eletrônica, sem consulta ao servidor no momento da leitura?

Essa formulação deve ser validada com o orientador. Ela evita prometer benefícios humanos não medidos e mantém no centro os dois aspectos distintivos do trabalho: acessibilidade como motivação de projeto e validação local como decisão técnica.

### 2.2 Objetivo geral sugerido

Projetar, implementar e documentar tecnicamente o FLIKE, um protótipo de controle de acesso físico que gerencia solicitações e permissões por meio de uma aplicação web e utiliza credenciais temporárias em QR Code autenticadas localmente por um dispositivo baseado em ESP32-CAM para acionar uma fechadura elétrica.

### 2.3 Objetivos específicos sugeridos

1. Caracterizar o cenário de acesso à sala sensorial que motivou o projeto e explicitar a origem e os limites das informações usadas nessa caracterização.
2. Especificar os requisitos funcionais, não funcionais e de acessibilidade derivados pela equipe para o protótipo.
3. Projetar a arquitetura, o modelo de dados e os fluxos de interação entre usuários, proprietários de instituições, aplicação web, API e trancas.
4. Implementar os fluxos de software para cadastro e autenticação, gestão de instituições, edifícios e trancas, solicitação e decisão de acesso, emissão da credencial e disponibilização do QR Code.
5. Definir e implementar um formato binário de credencial que identifique a tranca e a janela de validade e que seja autenticado por AES-CMAC antes de ser codificado em QR Code.
6. Desenvolver um protótipo embarcado capaz de ler e decodificar o QR Code, verificar localmente sua autenticidade e produzir o sinal necessário para acionar uma fechadura elétrica por meio de um circuito de potência.
7. Confrontar os requisitos e objetivos com o código, a documentação e as demonstrações disponíveis, registrando o nível de realização, as limitações, os riscos e os elementos que não puderam ser reproduzidos ou avaliados.

## 3. Delimitação editorial do escopo

### 3.1 Incluído

- Caso de uso da sala de apoio à amamentação e regulação sensorial da Faculdade de Direito da USP.
- Aplicação web oficial em Next.js/React.
- API FastAPI e persistência em MySQL.
- Modelo em que o mesmo usuário pode administrar instituições próprias e solicitar acesso a instituições de terceiros.
- Uma credencial por solicitação, reutilizável durante sua janela de validade.
- Protocolo binário de 48 bytes autenticado por AES-CMAC.
- Leitura de QR Code e validação local no ESP32-CAM.
- Circuito físico com ESP32-CAM, transistores, fonte de alimentação e tranca elétrica.
- Limitações de segurança, confiabilidade, integração e acessibilidade encontradas.
- Testes técnicos que possam ser executados ou documentados com evidências reproduzíveis.

### 3.2 Excluído ou abandonado

- Aplicativo móvel.
- MQTT, gateway, Bluetooth e armazenamento S3.
- Revogação confiável de uma credencial já emitida e ainda válida.
- Configuração ou rotação do segredo pelo usuário; assume-se programação prévia pelo fornecedor.
- Contagem de entrada, saída ou ocupação sem sensores capazes de fornecer essa evidência.
- Alegação de conformidade integral com normas de segurança, acessibilidade ou proteção de dados sem avaliação específica.
- Alegação de benefício comprovado ao público-alvo, pois não houve estudo com usuários.

### 3.3 Protocolo de trabalho conjunto

A escrita será incremental e colaborativa. **Não será produzido um capítulo inteiro de uma vez para a equipe revisar somente no final.** Cada alteração substantiva na tese seguirá uma rodada curta:

1. **Proposta:** antes de editar, o assistente apresenta a seção que será alterada, sua função, as fontes disponíveis, as decisões pendentes e o resultado esperado.
2. **Contexto da equipe:** a equipe corrige premissas, fornece documentos ou relatos e decide as alternativas que não podem ser resolvidas pelo código ou pela literatura.
3. **Escopo acordado:** assistente e equipe fixam quais arquivos e quais trechos pertencem à rodada. Informações ainda ausentes ficam marcadas; não serão preenchidas por suposição.
4. **Modificação:** o assistente altera somente o escopo acordado, preservando as demais partes da tese.
5. **Verificação:** o assistente compila o TCC, inspeciona o PDF e apresenta um resumo do que mudou, das fontes usadas, das verificações realizadas e das pendências.
6. **Revisão da equipe:** a equipe lê a entrega e aprova ou envia correções.
7. **Consolidação:** o assistente incorpora o feedback, repete a verificação e marca a seção como aprovada. Só então propõe a rodada seguinte.

Uma rodada deve produzir uma unidade fácil de revisar: uma decisão editorial, um conjunto pequeno de requisitos, uma subseção, um diagrama ou uma tabela de resultados. Quando uma etapa do plano envolver várias subseções, cada subseção será tratada em uma rodada própria.

#### Indicador de progresso

Toda abertura e todo encerramento de rodada informarão explicitamente a fase, o número do passo atual e o progresso global. Como o plano é numerado de 0 a 25, o denominador fixo é de **26 passos**. O percentual será calculado por `número de passos integralmente concluídos / 26 × 100`; blocos internos de um passo em andamento não aumentarão o numerador até a conclusão de todo o passo.

#### Identificação dos blocos e trechos para revisão

Toda menção a um bloco interno deverá vir acompanhada de uma frase que relembre seu conteúdo. Um pedido de revisão não poderá indicar apenas “bloco 8”, por exemplo: deverá informar também o tema e relacioná-lo aos números das seções e subseções correspondentes na tese.

Como a numeração impressa nas páginas da tese difere da posição física das páginas no arquivo PDF, os portões de revisão usarão prioritariamente números e títulos de seções, subseções, quadros e requisitos. Páginas poderão aparecer apenas como informação auxiliar, nunca como única forma de localizar o trecho.

Toda entrega que exija revisão começará por indicar inequivocamente o artefato a abrir, com uma chamada direta no formato **“Veja este documento: [link]”** ou **“Veja este PDF: [link]”**. Quando houver Markdown e PDF relacionados, o assistente declarará qual deles é o objeto principal da revisão e para que serve o outro. O pedido também repetirá as seções específicas que devem ser examinadas.

#### Figuras, diagramas e espaços reservados

As figuras não serão priorizadas durante a redação atual. Cada proposta de bloco deverá declarar se uma imagem ou diagrama contribuiria materialmente para o trecho. Antes de inserir uma figura existente, produzir um diagrama novo ou criar um espaço reservado, o assistente deverá explicar sua função e perguntar à equipe se o material existe e se sua inclusão está autorizada. Na ausência de confirmação, o bloco será escrito sem a figura. Tabelas e quadros textuais necessários à especificação poderão ser produzidos normalmente, pois não dependem de um ativo visual externo.

O documento `ARQUITETURA_E_ESTADO_DO_PROJETO.md` continuará funcionando como base factual. Se a equipe fornecer informação técnica nova, primeiro será avaliado se essa base precisa ser atualizada; depois a informação será convertida em texto acadêmico. Assim, correções factuais não ficam escondidas apenas dentro de um capítulo.

#### Registro de cada rodada

Cada entrega deverá informar:

- número e nome da rodada;
- objetivo e escopo autorizado;
- arquivos alterados;
- fontes e decisões utilizadas;
- resumo do conteúdo produzido;
- compilação e verificações executadas;
- pontos que exigem revisão humana;
- estado: `aguardando revisão`, `correções solicitadas` ou `aprovada`.

Commits poderão acompanhar os marcos aprovados pela equipe. Não será misturada no mesmo commit uma alteração editorial aprovada com experimentos ou mudanças de código sem relação.

#### Protocolo de referências durante a redação

As referências serão inseridas **no corpo do texto durante a redação de cada bloco**, junto das afirmações que sustentam. A etapa final de referências não será usada para acrescentar citações retrospectivamente em massa; ela servirá para auditar, padronizar e eliminar inconsistências no conjunto já construído.

Cada rodada seguirá estas regras:

1. antes da redação, identificar as afirmações que exigem fonte e relacioná-las às fontes disponíveis;
2. inserir a chamada de citação no mesmo parágrafo da afirmação sustentada e criar ou revisar a respectiva entrada BibTeX na própria rodada;
3. preferir a fonte primária e registrar página, seção, versão, DOI ou URL quando esses dados forem necessários para localizar a evidência;
4. não usar uma referência apenas por proximidade temática: a fonte deve sustentar precisamente a afirmação associada a ela;
5. distinguir quatro formas de sustentação: literatura ou norma recebe citação bibliográfica; comportamento implementado recebe evidência de código ou teste e remissão ao capítulo correspondente; relato da equipe é identificado como relato e explicado no método; requisito ou decisão concebida pelos autores é apresentado como elaboração dos autores;
6. manter na bibliografia somente obras efetivamente citadas e não citar uma obra que não tenha sido examinada;
7. impedir a aprovação de um bloco que contenha afirmação externa relevante sem fonte, citação quebrada ou referência bibliográfica incompleta.

Ao apresentar uma rodada para revisão, o assistente deverá informar também quais citações foram inseridas, qual afirmação cada uma sustenta e quais trechos não exigem referência externa por descreverem o próprio projeto. O resumo e o abstract permanecem sem citações, conforme o padrão editorial já definido.

A busca de referências é uma **atividade transversal**, executada antes de cada bloco de redação dos passos 6 a 21. Ela começa no passo 6, antes do bloco 3 do Capítulo 4, e inclui uma auditoria dos blocos 1 e 2 já aprovados. O passo 18 tem uma função mais ampla: realizar a pesquisa bibliográfica dirigida e organizar a fundamentação e os trabalhos relacionados do Capítulo 2. Portanto, o passo 18 aprofunda e sistematiza a bibliografia, mas não adia até esse momento as citações necessárias aos capítulos escritos anteriormente.

## 4. Estrutura planejada da monografia

A macroestrutura atual será mantida. Subseções podem ser criadas, removidas ou reordenadas para construir uma sequência argumentativa clara. As proporções abaixo são referências editoriais, não metas formais de páginas; deverão ser recalibradas após a leitura das boas teses fornecidas pela equipe e das regras do curso.

| Parte | Função no argumento | Proporção indicativa do texto principal |
| --- | --- | --- |
| 1. Introdução | Apresentar problema, motivação, objetivos, escopo e organização | 8–12% |
| 2. Aspectos Conceituais | Dar a base necessária para compreender e avaliar as decisões | 18–25% |
| 3. Método do Trabalho | Explicar como requisitos, projeto, implementação e avaliação foram conduzidos | 10–15% |
| 4. Especificação de Requisitos | Fixar o que o sistema deveria fazer e como verificar cada requisito | 12–18% |
| 5. Desenvolvimento do Trabalho | Descrever arquitetura, implementação, integração, testes e resultados | 30–40% |
| 6. Considerações Finais | Responder aos objetivos e registrar contribuições, limitações e continuidade | 6–10% |

### 4.1 Capítulo 1 — Introdução

**Objetivo do capítulo:** conduzir o leitor do problema concreto à pergunta do trabalho e aos objetivos, sem antecipar detalhes de implementação ou afirmar resultados ainda não demonstrados.

Estrutura proposta:

1. **Contextualização e problema:** apresentar a sala, seu propósito, o processo de retirada manual de chaves e as barreiras que motivaram o projeto. Distinguir relato da equipe, fonte institucional e evidência de pesquisa.
2. **Motivação:** explicar por que autonomia, previsibilidade e redução de interações obrigatórias são relevantes. Evitar tratar intenção de acessibilidade como benefício já medido.
3. **Objetivos:** substituir a lista atual por um objetivo geral e objetivos específicos verificáveis.
4. **Justificativa:** relacionar relevância social, contribuição de engenharia e viabilidade de uma solução de baixo custo.
5. **Escopo e limitações iniciais:** delimitar protótipo, operação offline da tranca, necessidade de internet para obter a credencial e ausência de avaliação com usuários.
6. **Organização do trabalho:** resumir a função de cada capítulo em um parágrafo coeso.

Evidências necessárias:

- fonte institucional sobre a sala e sua finalidade;
- descrição confirmada do procedimento anterior de acesso;
- fontes acadêmicas sobre barreiras e acessibilidade para pessoas neurodivergentes;
- confirmação final da pergunta, do objetivo geral e do recorte do trabalho.

Critério de conclusão: o capítulo deve permitir que um leitor externo compreenda qual problema foi escolhido, o que a equipe se propôs a construir e quais resultados seriam suficientes para avaliar o projeto.

### 4.2 Capítulo 2 — Aspectos Conceituais

**Objetivo do capítulo:** apresentar somente os conceitos necessários para justificar decisões e interpretar os resultados. O capítulo não será um catálogo de tecnologias.

Estrutura proposta:

1. **Acessibilidade, neurodiversidade e interação com espaços institucionais:** conceitos e barreiras pertinentes ao caso, com fontes acadêmicas e institucionais confiáveis.
2. **Sistemas de controle de acesso:** identificação, autenticação, autorização, credencial, auditoria e diferença entre destravamento e entrada efetiva.
3. **Fechaduras eletrônicas e sistemas embarcados:** componentes gerais, restrições de energia, atuação e confiabilidade.
4. **QR Code como transporte de credenciais:** estrutura, capacidade, correção de erros, leitura óptica e limitações de cópia.
5. **Fundamentos de segurança aplicados:** integridade, autenticidade, confidencialidade, disponibilidade e não repúdio, usando os termos com precisão.
6. **AES-CMAC e autenticação simétrica de mensagens:** finalidade, funcionamento conceitual, propriedades e limites. Explicar por que CMAC não é assinatura digital assimétrica.
7. **Validação offline de credenciais temporárias:** relógio confiável, janela de validade, reutilização autorizada e consequência para revogação.
8. **Trabalhos relacionados:** comparar soluções acadêmicas semelhantes por arquitetura, conectividade, mecanismo de credencial, hardware, avaliação e limitações.

Estratégia de pesquisa bibliográfica:

- priorizar artigos revisados por pares, normas, documentação oficial e publicações institucionais;
- usar fontes primárias para QR Code, AES-CMAC, requisitos e acessibilidade;
- registrar consulta, DOI/URL, data de acesso e a afirmação sustentada por cada fonte;
- criar um quadro comparativo de trabalhos relacionados, em vez de resumos isolados;
- não manter referências que não sejam citadas nem citar textos que a equipe não tenha lido.

Critério de conclusão: todo conceito usado nos capítulos 4 e 5 deve estar definido aqui ou ser conhecimento comum de engenharia; cada seção deve terminar conectando a teoria a uma decisão do FLIKE.

### 4.3 Capítulo 3 — Método do Trabalho

**Objetivo do capítulo:** explicar de forma retrospectiva e verificável como a equipe chegou aos requisitos, à arquitetura, à implementação e à avaliação. Não inventar Scrum, entrevistas, experimentos ou etapas que não ocorreram.

Estrutura proposta:

1. **Natureza do trabalho:** caracterizar, após validação do orientador, o projeto como desenvolvimento aplicado de um protótipo de engenharia.
2. **Levantamento do problema e dos requisitos:** fontes utilizadas, decisões da equipe e forma de priorização/revisão do escopo.
3. **Projeto da solução:** decomposição entre frontend, backend, protocolo, firmware e circuito.
4. **Implementação:** ambientes, repositórios, tecnologias, integração e controle de versões.
5. **Procedimento de avaliação:** testes definidos, métricas, equipamentos, versões e critérios de aprovação.
6. **Tratamento das limitações:** ausência de estudo com participantes, lacunas de preservação e reprodutibilidade e distinção entre inspeção estática, testes isolados e a demonstração física ponta a ponta final.

Informações que a equipe deverá fornecer:

- cronologia real do projeto;
- divisão de responsabilidades entre os três autores;
- decisões relevantes e alternativas descartadas;
- como requisitos foram levantados e por quem;
- ambientes, ferramentas e versões usados na demonstração;
- registros de reuniões, fotos, vídeos ou anotações que sustentem a retrospectiva.

Critério de conclusão: outra equipe deve conseguir compreender e, na medida do possível, reproduzir o processo técnico sem confundir método com resultado.

### 4.4 Capítulo 4 — Especificação de Requisitos

**Objetivo do capítulo:** substituir a lista atual por uma especificação consistente, rastreável e compatível com o escopo final.

Estrutura proposta:

1. **Contexto, atores e fronteira do sistema.**
2. **Convenções e critérios:** identificadores únicos, prioridade, fonte, método de verificação e estado.
3. **Requisitos gerais do sistema.**
4. **Requisitos da aplicação web e do backend.**
5. **Requisitos da credencial e da tranca digital.**
6. **Requisitos do firmware, da câmera, do circuito e da tranca elétrica.**
7. **Requisitos não funcionais:** segurança, desempenho, confiabilidade e acessibilidade.
8. **Matriz de rastreabilidade:** requisito → componente → evidência de implementação → teste → resultado.

Revisões obrigatórias:

- normalizar IDs repetidos e eliminar o `RF-10-00` duplicado;
- substituir “uso único” por reutilização dentro da janela de validade;
- associar a credencial à tranca digital;
- substituir “assinatura eletrônica” e “irretratabilidade” pelas propriedades realmente fornecidas por AES-CMAC;
- separar requisito, decisão arquitetural e expectativa futura;
- retirar ou reclassificar requisitos abandonados ou sem base, preservando transparência sobre o que não foi atendido;
- dar a cada requisito um critério observável de verificação.

Critério de conclusão: nenhum requisito deve depender de interpretação subjetiva para ser avaliado, e todo resultado relatado no capítulo 5 deve apontar para um requisito ou objetivo.

### 4.5 Capítulo 5 — Desenvolvimento do Trabalho

**Objetivo do capítulo:** constituir o núcleo técnico da monografia, mostrando decisões, implementação, integração, evidências e limitações. Diagramas devem aparecer junto da explicação correspondente, não como uma coleção isolada ao final.

Estrutura proposta:

1. **Visão geral da solução:** contexto do sistema, componentes e fronteiras.
2. **Tecnologias utilizadas e justificativas:** Next.js/React, FastAPI, MySQL, ESP32-CAM, OV2640, QR Code e bibliotecas relevantes. Explicar escolha e função, sem transformar a seção em documentação promocional.
3. **Arquitetura de software:** responsabilidades, comunicação frontend/API/banco e modelo contextual de administração.
4. **Modelo de dados:** entidades, relações e decisões centrais.
5. **Fluxos da aplicação:** cadastro/login, criação da estrutura física, solicitação, aprovação, emissão e consulta do QR.
6. **Protocolo da credencial:** layout de 48 bytes, serialização, timestamps, identificador da tranca e tag AES-CMAC.
7. **Frontend:** páginas e fluxos efetivamente implementados, incluindo limites de persistência da credencial.
8. **Backend:** rotas, autenticação, autorização, emissão, persistência e incompatibilidades relevantes.
9. **Firmware:** aquisição do QR, tratamento dos bytes, validação CMAC, decisão temporal pretendida e estado real da integração.
10. **Hardware:** circuito, componentes, alimentação, acionamento da tranca e montagem demonstrada, conforme evidências que a equipe fornecer.
11. **Operação offline e modelo de ameaça:** o que funciona sem rede, necessidade de relógio, cópia do QR, proteção do segredo e ausência de revogação confiável.
12. **Testes e avaliação técnica:** procedimento, resultados e análise por requisito.
13. **Limitações da implementação:** divergências entre componentes, requisitos não atendidos, riscos aceitos e impacto nas conclusões.

#### Figuras e quadros planejados

- diagrama de contexto atualizado;
- diagrama de contêineres da aplicação, somente com componentes finais;
- diagrama de blocos do conjunto embarcado;
- diagrama entidade-relacionamento fiel ao banco;
- diagrama de sequência da solicitação e aprovação;
- diagrama de sequência da apresentação e validação do QR;
- quadro do layout binário da credencial;
- esquema elétrico e fotografia identificada do protótipo;
- matriz requisito–teste–resultado;
- tabelas de resultados com unidade, ambiente, número de repetições e limitações.

Os diagramas atuais que contêm tecnologias abandonadas devem ser redesenhados. Toda figura deverá ser legível no tamanho final, ser citada antes de aparecer e receber legenda que explique sua função no argumento.

#### Plano mínimo de avaliação técnica

O conjunto final dependerá do estado executável dos componentes e da disponibilidade do hardware. A prioridade é produzir evidência honesta, não uma grande quantidade de testes superficiais.

| Grupo | Casos prioritários | Evidência esperada |
| --- | --- | --- |
| Compilação | frontend, backend e firmware nas versões declaradas | comandos, versões, logs resumidos e resultado |
| Protocolo | vetor comum Python/C++, 48 bytes, bytes nulos/altos, tamanho inválido e tag alterada | entradas, saídas esperadas e observadas |
| Validação | segredo correto/incorreto, tranca correta/incorreta, antes/durante/depois da validade | tabela de decisões e timestamps controlados |
| Autorização web | usuário comum, proprietário, acesso indevido e rotas sensíveis | requisição, resposta e requisito relacionado |
| Fluxo integrado | solicitação → aprovação → QR → leitura → validação AES-CMAC → sinal `HIGH` → acionamento da fechadura | demonstração confirmada pela equipe e verificações adicionais que forem executadas sobre os artefatos disponíveis |
| Leitura óptica | tempo de leitura, se a medição for viável | procedimento, repetições e latência observada |
| Hardware | acionamento, alimentação e comportamento observado da tranca | descrição funcional, material já disponível e demonstração confirmada pela equipe |
| Acessibilidade | inspeção heurística/técnica da interface, claramente separada de teste com usuários | critérios, achados e limitações |

Não serão fabricados resultados retroativos. Se um teste não puder ser executado, o texto indicará “não avaliado” e explicará a consequência.

Critério de conclusão: o capítulo deve permitir distinguir, em cada subsistema, o que foi projetado, implementado, testado, demonstrado apenas por relato e deixado como limitação.

### 4.6 Capítulo 6 — Considerações Finais

**Objetivo do capítulo:** responder à pergunta do trabalho e fazer o balanço entre objetivos, resultados e limites, sem introduzir tecnologia ou resultado novo.

Estrutura proposta, preservando as três seções atuais:

1. **Conclusões do Projeto de Formatura:** retomar problema e objetivo geral; sintetizar os resultados por objetivo específico; declarar o nível de integração alcançado e os requisitos não atendidos.
2. **Contribuições:** separar contribuição da equipe, artefatos produzidos e aprendizados técnicos. Não atribuir ao FLIKE impacto social não avaliado.
3. **Perspectivas de Continuidade:** validação temporal confiável, endurecimento de segurança, provisionamento do segredo, auditoria física e avaliação futura com o público-alvo. A integração já demonstrada entre firmware e atuador será apresentada como resultado do trabalho, não como perspectiva futura.

Critério de conclusão: cada afirmação de sucesso deverá estar apoiada por uma evidência apresentada no capítulo 5; cada limitação material deverá aparecer explicitamente.

## 5. Elementos pré-textuais e pós-textuais

Esses elementos serão finalizados depois do corpo principal, quando contribuições e resultados estiverem estáveis.

### 5.1 Pré-textuais

- **Título:** manter o título acadêmico atual até decisão da equipe/orientador; usar FLIKE como nome do sistema no texto.
- **Ficha catalográfica e folha de aprovação:** substituir os arquivos provisórios nos momentos institucionais adequados.
- **Dedicatória e agradecimentos:** coletar versão final dos três autores.
- **Resumo:** redigir por último, cobrindo problema, objetivo, método, solução, principais resultados e conclusão, sem citações.
- **Abstract:** traduzir e revisar a partir do resumo final, mantendo equivalência de conteúdo.
- **Palavras-chave/keywords:** escolher termos específicos e consistentes com vocabulários acadêmicos quando possível.
- **Listas de figuras, quadros, tabelas, siglas e símbolos:** manter somente listas com conteúdo real; remover exemplos do modelo.

### 5.2 Pós-textuais

- auditar e padronizar no mecanismo único BibTeX/ABNT as referências que já terão sido inseridas durante cada rodada de redação;
- remover a bibliografia manual atualmente inserida no capítulo 6;
- incluir apenas referências efetivamente citadas;
- considerar apêndices para protocolo detalhado, matriz completa de testes ou material produzido pela equipe;
- considerar anexos somente para documentos externos indispensáveis;
- registrar endereço e versão dos repositórios se a política do curso permitir.

## 6. Passo a passo de trabalho

A ordem de escrita não seguirá a ordem de leitura. Primeiro será definido o contrato acadêmico e estabilizado o núcleo técnico; introdução, resumo e conclusões serão escritos quando os resultados estiverem claros. A coluna “portão de saída” indica o que a equipe precisa validar antes do passo seguinte.

### Fase A — Alinhamento e padrão editorial

| Passo | Participação da equipe | Ação do assistente | Entrega e portão de saída |
| --- | --- | --- | --- |
| 0. Validar o processo | Revisar este plano e corrigir a dinâmica de colaboração | Incorporar o feedback sem editar os capítulos | Plano de trabalho aprovado |
| 1. Receber referências | Enviar boas teses, normas, prazos e feedback do orientador | Organizar e identificar o papel de cada material | Inventário de referências confirmado |
| 2. Analisar as boas teses | Indicar o que agrada ou incomoda em cada exemplo | Produzir fichas comparativas de estrutura, profundidade, figuras, testes e estilo | Padrão editorial escolhido pela equipe |
| 3. Fechar o contrato do TCC | Decidir com o assistente a pergunta, os objetivos, o escopo e as limitações | Preparar uma proposta curta com alternativas e impactos | Pergunta, objetivo geral, objetivos específicos e escopo aprovados |
| 4. Fixar vocabulário e alegações | Corrigir termos e promessas que não representam o projeto | Produzir lista controlada de termos e afirmações permitidas/proibidas | Vocabulário aprovado e arquitetura factual atualizada, se necessário |

Nenhum capítulo será reescrito antes da aprovação do passo 4.

### Fase B — Requisitos e núcleo técnico

| Passo | Participação da equipe | Ação do assistente | Entrega e portão de saída |
| --- | --- | --- | --- |
| 5. Planejar o Capítulo 4 | Confirmar quais requisitos ainda representam o produto | Apresentar nova organização, IDs e critérios de verificação, sem editar o capítulo | Estrutura e decisões dos requisitos aprovadas |
| 6. Reescrever o Capítulo 4 | Revisar os requisitos em pequenos grupos | Antes de cada grupo, buscar e validar as fontes necessárias; depois editar, inserir as citações no texto, compilar e apresentar o diff | Capítulo 4 aprovado, citado e com requisitos rastreáveis |
| 7. Preparar evidências do Capítulo 5 | Fornecer commits, fotos, circuito, componentes, demonstrações e decisões | Classificar cada item como código, relato, teste ou evidência física | Inventário técnico validado; lacunas explicitadas |
| 8. Aprovar o esqueleto do Capítulo 5 | Revisar ordem e profundidade das subseções | Propor títulos, função de cada seção, figuras e fontes | Esqueleto detalhado aprovado, ainda sem redação extensa |
| 9. Escrever visão geral e arquitetura | Validar fronteiras, componentes e diagramas | Redigir a visão geral e produzir diagramas atualizados | Subseções e diagramas aprovados |
| 10. Escrever software | Corrigir descrições funcionais e decisões de produto | Redigir modelo de dados, backend, frontend e fluxos; uma subseção por rodada | Bloco de software aprovado |
| 11. Escrever credencial e segurança | Validar política de validade e riscos aceitos | Redigir protocolo, AES-CMAC, operação offline, segredo e modelo de ameaça | Bloco de credencial e segurança aprovado |
| 12. Escrever firmware e hardware | Fornecer detalhes da montagem e dizer exatamente o que funcionou | Redigir firmware, circuito e integração física, separando estado atual e intenção | Bloco embarcado aprovado |
| 13. Consolidar limitações | Confirmar que nenhuma lacuna ou promessa foi disfarçada | Relacionar incompatibilidades, requisitos não atendidos e efeitos nas conclusões | Parte descritiva do Capítulo 5 aprovada |

Nos passos 9 a 13, cada linha representa várias rodadas pequenas. Por exemplo, backend e frontend não serão entregues juntos se isso impedir uma revisão cuidadosa.

### Fase C — Avaliação e resultados

| Passo | Participação da equipe | Ação do assistente | Entrega e portão de saída |
| --- | --- | --- | --- |
| 14. Definir testes possíveis | Informar hardware, ambientes e tempo disponíveis | Propor casos, métricas, repetições e critérios ligados aos requisitos | Protocolo de testes aprovado antes da execução |
| 15. Produzir evidências | Participar de montagens ou procedimentos que dependam de acesso físico e fornecer registros existentes | Executar os testes acessíveis no workspace, organizar resultados e registrar falhas | Dados brutos e condições de teste conferidos pela equipe |
| 16. Escrever testes e resultados | Verificar se a interpretação corresponde ao que foi observado | Redigir uma família de testes por rodada, com tabelas e limitações | Seção de avaliação e matriz de rastreabilidade aprovadas |

Se algum teste não puder ser feito, a equipe decidirá entre reduzir o requisito, registrá-lo como não avaliado ou tratá-lo como trabalho futuro. O texto nunca receberá um resultado presumido.

### Fase D — Fundamentação e narrativa acadêmica

| Passo | Participação da equipe | Ação do assistente | Entrega e portão de saída |
| --- | --- | --- | --- |
| 17. Reconstruir o método | Relatar cronologia, responsabilidades e decisões reais | Preparar perguntas objetivas e redigir uma etapa do método por rodada | Capítulo 3 aprovado, sem processo inventado |
| 18. Planejar a revisão bibliográfica ampla | Validar os temas e fornecer fontes já usadas | Sistematizar perguntas de busca, fundamentação e trabalhos relacionados; consolidar uma bibliografia comentada | Fontes e estrutura do Capítulo 2 aprovadas |
| 19. Escrever os conceitos | Revisar clareza e pertinência ao FLIKE | Redigir uma seção conceitual por rodada, com citações verificadas | Capítulo 2 aprovado e bibliografia consistente |
| 20. Reescrever a introdução | Confirmar contexto, motivação e tom das contribuições | Redigir uma seção por rodada, alinhada aos capítulos já aprovados | Capítulo 1 aprovado |
| 21. Escrever as considerações finais | Validar o balanço dos três autores | Relacionar cada conclusão a objetivo e evidência | Capítulo 6 aprovado |

### Fase E — Fechamento do manuscrito

| Passo | Participação da equipe | Ação do assistente | Entrega e portão de saída |
| --- | --- | --- | --- |
| 22. Finalizar pré-textuais | Fornecer agradecimentos e dados institucionais pendentes | Redigir resumo, abstract, palavras-chave e limpar listas provisórias | Elementos pré-textuais aprovados |
| 23. Finalizar pós-textuais | Confirmar materiais suplementares e referências | Auditar e padronizar o BibTeX já construído durante a redação, além de consolidar apêndices e anexos | Referências e materiais complementares aprovados |
| 24. Revisar o todo | Cada autor faz leitura integral e registra correções | Fazer revisão técnica, editorial e de consistência; compilar e inspecionar o PDF | Versão candidata aprovada pelos autores |
| 25. Incorporar orientação formal | Enviar retorno do orientador ou banca | Aplicar cada correção em rodadas rastreáveis e repetir QA | Versão final autorizada para entrega |

### Próxima ação

O **passo 8** foi concluído em 01/09/2026 com a aprovação das Seções 5.1 a 5.8, da distribuição dos passos 9 a 16 e das figuras F5-01 a F5-06. O **passo 9** está em andamento: `PROPOSTA_BLOCO_1_CAPITULO_5.md` detalha a visão geral, a arquitetura, o modelo de dados e as duas primeiras figuras.

### Acompanhamento da Fase A

| Passo | Estado | Registro | Próxima ação |
| --- | --- | --- | --- |
| 0. Validar o processo | **Aprovado** | Plano de trabalho aprovado pela equipe em 31/08/2026 | Concluído |
| 1. Receber referências | **Concluído** | 50 monografias, sete materiais institucionais e o projeto histórico do Laboratório de Processadores organizados e examinados | Incorporar futuros documentos quando fornecidos |
| 2. Analisar as boas teses | **Aprovado** | 50 fichas e síntese comparativa; equipe escolheu padrão técnico, detalhado e visual em 01/09/2026 | Concluído |
| 3. Fechar o contrato do TCC | **Aprovado** | Pergunta, objetivo geral, sete objetivos específicos, escopo e limitações aprovados em 01/09/2026 | Concluído |
| 4. Fixar vocabulário e alegações | **Aprovado** | Dicionário editorial, identidade exclusiva do FLIKE, AES-CMAC como protocolo vigente e demonstração física ponta a ponta registrados e aprovados em 01/09/2026 | Concluído |

### Acompanhamento da Fase B

| Passo | Estado | Registro | Próxima ação |
| --- | --- | --- | --- |
| 5. Planejar o Capítulo 4 | **Aprovado** | Estrutura, 14 requisitos funcionais, cinco não funcionais, quatro de acessibilidade, critérios de verificação e decisões P1–P8 aprovados em 01/09/2026 | Concluído |
| 6. Reescrever o Capítulo 4 | **Aprovado** | Capítulo 4 completo: RF-01 a RF-14, RNF-01 a RNF-05, RA-01 a RA-04, decisões arquiteturais e Seção 4.8 aprovados em 01/09/2026 | Concluído |
| 7. Preparar evidências do Capítulo 5 | **Aprovado** | `INVENTARIO_EVIDENCIAS_CAPITULO_5.md` consolida código, documentação, demonstrações e relatos; commits finais confirmados e nível de detalhe do hardware aprovado em 01/09/2026 | Concluído |
| 8. Aprovar o esqueleto do Capítulo 5 | **Aprovado** | Seções 5.1–5.8, distribuição dos passos 9–16 e figuras F5-01 a F5-06 aprovadas em 01/09/2026 | Concluído |
| 9. Arquitetura e modelo de dados | **Em andamento — proposta do bloco 1 produzida** | `PROPOSTA_BLOCO_1_CAPITULO_5.md` especifica as Seções 5.1, 5.2 e 5.3.1 e as figuras F5-01/F5-02 | Equipe validar o bloco antes da redação e compilação |

## 7. Fontes e informações a solicitar à equipe

A lista abaixo é um mapa de dependências, não um pedido para que tudo seja reunido de uma vez. Em cada passo, o assistente solicitará apenas o material necessário para a rodada seguinte e explicará como ele será usado.

### 7.1 Prioridade imediata — antes da redação substantiva

1. Teses consideradas boas, preferencialmente do mesmo curso, orientador ou área.
2. Normas, guia de TCC, rubrica de avaliação e prazo oficial aplicáveis.
3. Feedback já fornecido pelo orientador ou pela banca intermediária.
4. Confirmação da pergunta, objetivo geral e objetivos específicos.
5. Cronologia real do projeto e divisão de responsabilidades entre os autores.
6. Versões finais disponíveis de cada componente, quando sua identificação for necessária à rastreabilidade do texto.

### 7.2 Prioridade técnica — antes de concluir o capítulo 5

1. Esquema ou desenho do circuito montado.
2. Lista funcional dos componentes do circuito, sem exigir modelos comerciais das fontes e do relé.
3. Fotos e vídeos existentes do protótipo, sem transformar a ausência de novo registro em bloqueio.
4. Descrição exata do que foi demonstrado fisicamente.
5. Procedimento adotado para gravar identificador e segredo no ESP32-CAM.
6. Logs, capturas de tela ou roteiros que já existam ou possam ser produzidos durante os testes planejados.
7. Ambiente disponível para executar testes novos.

### 7.3 Prioridade contextual — antes de fechar introdução e método

1. Fonte sobre a criação, finalidade e funcionamento da sala.
2. Relato factual do processo anterior de retirada de chaves.
3. Origem dos requisitos e pessoas envolvidas em sua definição.
4. Decisões tomadas durante o desenvolvimento e razões para redução de escopo.
5. Qualquer pesquisa, reunião ou documento não presente no Git.

Informações fornecidas oralmente pela equipe serão registradas como relato de projeto e não convertidas automaticamente em evidência de desempenho ou de impacto.

## 8. Uso das teses de referência

Para cada tese recebida, será produzida uma ficha breve com:

- estrutura de capítulos e extensão relativa;
- forma de apresentar problema, objetivos e contribuições;
- profundidade da fundamentação;
- organização do capítulo técnico;
- tipos de diagramas, tabelas e testes;
- estilo de discussão de limitações;
- padrão de citações e referências;
- escolhas úteis ao FLIKE e escolhas que não se aplicam.

As teses servirão para formar um padrão editorial comum. Nenhuma delas será tratada como fonte técnica quando apenas demonstrar estilo ou organização.

## 9. Regras de escrita e integridade acadêmica

1. Usar **FLIKE** como único nome do projeto.
2. Escrever em português acadêmico claro, com parágrafos argumentativos e termos técnicos definidos.
3. Separar explicitamente intenção, implementação, teste, resultado e inferência.
4. Não afirmar que um componente funciona porque há um arquivo, uma dependência ou um diagrama correspondente.
5. Não inventar entrevistas, testes, métricas, referências, datas, decisões ou resultados.
6. Não apresentar acessibilidade pretendida como impacto comprovado.
7. Não chamar AES-CMAC de criptografia do conteúdo, assinatura digital assimétrica ou garantia de não repúdio.
8. Usar “credencial temporária reutilizável durante a janela de validade”; evitar “uso único”.
9. Distinguir tranca física, tranca elétrica e tranca digital.
10. Distinguir leitura do QR, autorização, acionamento, abertura da porta, entrada, saída e ocupação.
11. Tratar operação offline como propriedade da validação na tranca; obtenção e gestão da credencial continuam dependentes da aplicação web.
12. Expor limitações relevantes junto dos resultados afetados e retomá-las na conclusão.
13. Preferir fontes primárias e acadêmicas; verificar cada referência antes de incluí-la.
14. Manter uma única terminologia em texto, figuras, tabelas, código citado, resumo e abstract.
15. Usar os IDs de evidência do documento de arquitetura apenas como ferramenta interna; a tese final deve converter essa rastreabilidade em texto, referências, figuras e resultados compreensíveis ao leitor.

## 10. Controle editorial

### 10.1 Estado atual dos capítulos

| Parte | Estado inicial | Próxima ação |
| --- | --- | --- |
| Pré-textuais | Provisórios e com afirmações antigas | Reescrever somente após estabilizar resultados |
| Cap. 1 — Introdução | Parcial, com listas e promessas excessivas | Validar pergunta/objetivos e reescrever |
| Cap. 2 — Aspectos Conceituais | Conteúdo do modelo | Pesquisa bibliográfica dirigida |
| Cap. 3 — Método | Conteúdo do modelo | Reconstruir processo real com a equipe |
| Cap. 4 — Requisitos | Lista substantiva, porém inconsistente | Normalizar, recortar e tornar verificável |
| Cap. 5 — Desenvolvimento | Descrição curta e diagramas obsoletos | Redigir a partir da arquitetura e das evidências |
| Cap. 6 — Considerações Finais | Conteúdo do modelo | Escrever depois dos resultados |
| Referências | Fontes dispersas e mecanismo duplicado | Verificar e consolidar em BibTeX |

### 10.2 Estados de acompanhamento

Cada seção poderá receber um dos seguintes estados no acompanhamento editorial:

- **Bloqueada:** depende de decisão, documento ou evidência externa.
- **Pronta para redigir:** escopo e fontes suficientes.
- **Em redação:** primeira versão em produção.
- **Em revisão técnica:** conferência de fatos, termos e resultados.
- **Em revisão editorial:** clareza, coesão, citações e formatação.
- **Aprovada pela equipe:** conteúdo aceito pelos três autores.
- **Aprovada pelo orientador:** incorporou o retorno formal recebido.

### 10.3 Critério de pronto para uma seção

Uma seção só será considerada pronta quando:

- cumprir uma função clara no argumento do capítulo;
- não contiver instruções do modelo ou marcadores pendentes silenciosos;
- tiver todas as afirmações factuais sustentadas por fonte, código, teste ou relato identificado;
- usar a terminologia oficial;
- citar e explicar todas as figuras e tabelas;
- compilar sem referências ou citações quebradas;
- declarar limitações materiais;
- passar por revisão de ao menos outro integrante da equipe.

## 11. Verificação final do manuscrito

Antes de qualquer versão candidata à entrega:

1. Compilar o projeto do zero com o comando oficial do repositório.
2. Conferir erros, referências indefinidas, citações ausentes, conteúdo provisório e texto fora das margens.
3. Buscar automaticamente nomenclatura antiga, tecnologias abandonadas apresentadas como ativas e expressões tecnicamente incorretas.
4. Conferir correspondência entre objetivos, requisitos, testes, resultados e conclusões.
5. Verificar consistência entre resumo e abstract.
6. Verificar numeração e menção de capítulos, seções, figuras, quadros, tabelas, equações e apêndices.
7. Revisar visualmente todas as páginas do PDF.
8. Conferir legibilidade de diagramas e tabelas no tamanho de página.
9. Validar referências bibliográficas e conformidade ABNT aplicável.
10. Fazer revisão final separada de conteúdo técnico, português e apresentação.

## 12. Registro da validação da equipe

A equipe aprovou a dinâmica de trabalho e o padrão editorial:

1. trabalhar em rodadas pequenas e verificáveis;
2. receber uma proposta de escopo antes de cada modificação substantiva na tese;
3. revisar a entrega de cada rodada antes de avançarmos;
4. preservar as partes já aprovadas enquanto outra seção é trabalhada;
5. seguir os passos 0–25, admitindo reordenação quando uma dependência prática exigir;
6. começar pelas teses de referência, sem modificar os capítulos nessa primeira análise;
7. adotar texto técnico e detalhado;
8. usar diagramas, tabelas, esquemas e fotografias em quantidade suficiente para documentar o projeto.
9. no início e no encerramento de cada passo, informar explicitamente o que a equipe precisa fornecer, revisar, decidir ou aprovar; quando nenhuma ação for necessária, declarar isso de forma direta.

As teses de referência e as orientações institucionais já foram analisadas. A tese central, a pergunta, os objetivos e o escopo foram aprovados no passo 3. O vocabulário e as alegações controladas foram aprovados no passo 4. Cada parte do conteúdo continuará sujeita aos portões específicos descritos na seção 6.
