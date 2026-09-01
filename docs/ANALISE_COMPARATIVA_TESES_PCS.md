# FLIKE — análise comparativa de 50 teses recentes do PCS

## 1. Finalidade e alcance

Este documento transforma a leitura das 50 monografias selecionadas do PCS em decisões úteis para a escrita do TCC do FLIKE. As fichas individuais permanecem como registro da evidência; esta síntese identifica padrões, referências prioritárias, erros recorrentes e uma proposta de padrão editorial para a equipe validar.

A análise cobre 30 trabalhos de 2025 e 20 de 2024, totalizando **4.064 páginas, 952.287 palavras e 7.410.670 caracteres extraídos**. Cada tese recebeu uma ficha após exame estruturado do texto integral e leitura de suas partes centrais, quando existentes: introdução, fundamentação, método, requisitos, arquitetura, implementação, avaliação, resultados e conclusão. Esse processo não equivale a uma leitura linear e igualmente minuciosa de cada frase; a profundidade foi concentrada nas seções que sustentam a comparação editorial.

As notas de 0 a 4 avaliam a utilidade da monografia como modelo de comunicação acadêmica para o FLIKE. Elas não são avaliações oficiais dos trabalhos nem reavaliações científicas de seus domínios especializados.

## 2. Visão quantitativa do corpus

Das 50 teses, 29 foram classificadas como prioridade A, 14 como B e 7 como C. Nenhuma recebeu D, pois a seleção inicial já privilegiava trabalhos com alguma aderência editorial ou técnica. A média indicativa global foi **3,52/4**.

| Critério | Média | Leitura do resultado |
| --- | ---: | --- |
| C01 — problema | 3,76 | Em geral, os trabalhos contextualizam bem o problema. |
| C02 — objetivos e escopo | 3,74 | Objetivos costumam ser claros; entregas parciais nem sempre aparecem cedo. |
| C03 — progressão argumentativa | 3,84 | É o ponto mais forte do corpus e confirma a macroestrutura do PCS. |
| C04 — fundamentação | 3,46 | Muitas revisões explicam tecnologias, mas poucas constroem comparação crítica. |
| C05 — método | 3,56 | A maioria registra etapas; a reprodutibilidade varia bastante. |
| C06 — requisitos | 3,42 | Listas são comuns, rastreabilidade completa é rara. |
| C07 — arquitetura | 3,62 | Bons trabalhos deixam fronteiras e responsabilidades explícitas. |
| C08 — implementação | 3,76 | É outro ponto forte, por vezes detalhado além do necessário. |
| C09 — avaliação | 3,00 | É a principal fragilidade: faltam métricas, repetição, ambiente ou amostra. |
| C10 — resultados | 3,32 | Demonstrações são frequentes; discussão comparativa é menos comum. |
| C11 — limitações | 3,66 | Os melhores trabalhos assumem falhas, escopo reduzido e resultados negativos. |
| C12 — conclusões | 3,38 | Há extrapolações recorrentes de protótipo para impacto ou eficácia. |
| C13 — elementos visuais | 3,64 | Diagramas e fotografias ajudam, mas capturas de tela são usadas em excesso. |
| C14 — normalização | 3,14 | Revisão textual, referências e consistência formal são frágeis em muitos casos. |
| C15 — aplicação ao FLIKE | 3,42 | Há um conjunto expressivo de referências diretas para o projeto. |

O corpus é forte para ensinar **como organizar e descrever um artefato**. Ele é menos confiável como padrão de **como demonstrar que o artefato cumpre suas promessas**. O FLIKE deve conservar a estrutura clara dos melhores exemplos e dedicar atenção adicional ao vínculo entre requisito, teste, resultado e conclusão.

## 3. Referências prioritárias

### 3.1 Melhores modelos globais

| Tese | Média | Principal valor editorial |
| --- | ---: | --- |
| 2025-C27 — *Attention-Based Deep Learning for Predicting Recurrent Hospital Readmissions* | 4,00 | Declara requisitos atendidos, parciais e não atendidos e limita a conclusão à evidência. |
| 2025-C28 — *Projeto COCAD* | 4,00 | Organiza arquitetura em visões adaptadas e mantém rastreabilidade entre requisitos e componentes. |
| 2025-S01 — *Análise de Público por Visão Computacional na Indústria 4.0* | 4,00 | Define contratos entre etapas e instrumenta o fluxo inteiro. |
| 2025-C04 — *Sensoriamento e Comunicação Wi-Fi Integrados para Monitoramento da Umidade do Solo* | 3,93 | Formula hipóteses, documenta aparato físico e trata a rejeição da hipótese como resultado. |
| 2025-C22 — *Solução Criptográfica para Mobilidade Segura em Eleições Brasileiras* | 3,93 | Separa protocolo, aplicação, criptografia e integração incompleta. |
| 2025-C24 — *Simulating Spiking Neural Networks* | 3,93 | Relaciona requisitos a testes, usa baselines e discute resultados quantitativos. |
| 2024-S01 — *MarmoNet* | 3,93 | Integra restrições físicas, firmware, energia, testes de campo e resultados negativos. |

As notas iguais não tornam as teses intercambiáveis. O padrão do FLIKE deve ser uma combinação: arquitetura de 2025-C28; rastreabilidade e honestidade de 2025-C27; experimento físico de 2025-C04 e 2024-S01; separação criptográfica de 2025-C22; instrumentação de 2025-S01.

### 3.2 Modelos por necessidade do FLIKE

| Necessidade | Referências | O que aproveitar | Cuidado |
| --- | --- | --- | --- |
| Arquitetura de sistema integrado | 2025-C28, 2025-C02, 2025-S01 | Fronteiras, responsabilidades, interfaces e visões adequadas ao leitor | Não desenhar componentes abandonados nem qualidades futuras como atuais. |
| Requisitos e rastreabilidade | 2025-C27, 2025-C24, 2024-S04 | Estado por requisito e ligação com casos de teste | Uma lista extensa sem critério observável não produz rastreabilidade. |
| Criptografia e modelo de ameaça | 2025-C22, 2025-C21, 2024-C06 | Separar propriedade, mecanismo, vetor de teste e limitação | Não chamar CMAC de assinatura digital nem inferir segurança de produção. |
| Firmware e protótipo físico | 2025-C04, 2024-S01, 2024-S11, 2024-C10, 2025-S04 | Aparato, alimentação, sinais, montagem, campo e integração | Esquema, firmware e acionamento físico são evidências diferentes. |
| Aplicação web e backend | 2025-C02, 2024-S04, 2024-C13 | Fluxos, papéis, endpoints, persistência e testes de integração | Capturas de telas não substituem arquitetura nem resultado. |
| Acessibilidade e usuários | 2024-S02, 2024-C13, 2024-C08, 2025-C23 | Protocolo com público, ética, feedback e limites da amostra | Intenção inclusiva e opinião de usuário não provam impacto social. |
| Resultado incompleto ou negativo | 2025-C04, 2025-C27, 2024-C20, 2024-S04, 2024-S07 | Nomear a falha, explicar consequência e reduzir a conclusão | Não transferir para “trabalhos futuros” algo alegado como entrega atual. |
| Demonstração em ambiente real | 2024-C10, 2024-S01, 2024-C13 | Condições reais revelam falhas ausentes na bancada | Uma demonstração isolada não mede confiabilidade. |

## 4. Macroestrutura recomendada

A estrutura de seis capítulos do TCC atual é compatível com os trabalhos recentes e deve ser preservada:

1. **Introdução:** problema, motivação, pergunta, objetivo, escopo e organização.
2. **Aspectos conceituais:** conceitos necessários e trabalhos relacionados.
3. **Método do trabalho:** processo real de levantamento, projeto, implementação e avaliação.
4. **Especificação de requisitos:** contrato verificável do sistema.
5. **Desenvolvimento do trabalho:** arquitetura, implementação, integração, testes e discussão.
6. **Considerações finais:** resposta aos objetivos, contribuições, limitações e continuidade.

O ganho editorial não virá de mudar esses capítulos, mas de dar uma função inequívoca a cada um. Conceitos não devem antecipar o manual da implementação; método não deve conter resultados; desenvolvimento não deve virar catálogo de bibliotecas; conclusão não deve introduzir alegações ou tecnologias novas.

O capítulo 5 pode manter resultados no próprio capítulo porque o FLIKE é um projeto integrado de engenharia. Cada subsistema deve ser descrito e, em seguida, ligado à evidência correspondente. Uma seção final deve reunir o fluxo de ponta a ponta e a matriz de resultados.

## 5. Padrões editoriais extraídos

### 5.1 Problema, pergunta e objetivos

Os melhores trabalhos partem de uma situação concreta, demonstram por que ela importa e formulam um objetivo que o artefato pode responder. Os mais fracos saltam de um problema social amplo diretamente para “desenvolver uma plataforma”.

No FLIKE, o encadeamento deve ser:

1. existe um processo físico de acesso e uma barreira de interação;
2. a equipe propõe reduzir interações obrigatórias por meio de uma credencial digital;
3. a decisão técnica distintiva é a validação local pela tranca;
4. o trabalho avalia o protótipo e seus limites;
5. impacto sobre autonomia ou acessibilidade permanece motivação enquanto não houver estudo com pessoas.

Objetivos específicos devem terminar em verbos verificáveis, como caracterizar, especificar, projetar, implementar, integrar e avaliar. “Promover inclusão”, “garantir segurança” e “assegurar confiabilidade” exigiriam evidências que o projeto ainda não possui.

### 5.2 Fundamentação

Uma boa fundamentação responde a três perguntas: qual conceito é necessário, qual decisão do FLIKE ele sustenta e qual limite ajuda a interpretar. A revisão deve cobrir acessibilidade, controle de acesso, QR Code, autenticação de mensagens, sistemas embarcados e validação offline. Tecnologias específicas pertencem ao desenvolvimento quando sua função é apenas explicar a implementação.

Trabalhos relacionados devem aparecer em quadro comparativo com, no mínimo:

- contexto e público;
- tipo de credencial;
- necessidade de conectividade no acesso;
- mecanismo de segurança;
- hardware;
- forma de avaliação;
- limitação relevante;
- diferença em relação ao FLIKE.

### 5.3 Método

O método deve ser retrospectivo e fiel. Diversas teses enfraquecem quando atribuem ao projeto um processo formal que não pode ser reconhecido nas evidências. O FLIKE não deve inventar entrevistas, sprints, validação com usuários ou uma sequência experimental que não aconteceu.

O capítulo deve registrar:

- como o problema chegou à equipe;
- de onde vieram os requisitos;
- como o sistema foi decomposto;
- como os três integrantes dividiram o trabalho;
- quais decisões reduziram o escopo;
- quais repositórios e ambientes materializam cada componente;
- como será feita a avaliação técnica restante;
- quais fontes são contemporâneas ao projeto e quais foram reconstruídas depois.

### 5.4 Requisitos

As melhores monografias tratam requisito como uma afirmação verificável. Para o FLIKE, cada requisito deve conter identificador, descrição, fonte, prioridade, componente, critério de aceitação, método de verificação e estado final.

Os estados recomendados são:

- **atendido e testado**;
- **implementado sem teste suficiente**;
- **parcialmente atendido**;
- **não atendido**;
- **removido do escopo**;
- **não avaliado**.

Essa classificação impede que código existente seja confundido com comportamento demonstrado e permite que um protótipo incompleto produza uma conclusão rigorosa.

### 5.5 Arquitetura e implementação

Diagramas devem mostrar somente componentes reais e receber uma pergunta clara. O conjunto mínimo recomendado é:

1. contexto e atores;
2. contêineres da aplicação web, API, banco e tranca;
3. modelo de dados;
4. sequência da solicitação, aprovação e emissão;
5. sequência da leitura e validação local;
6. blocos do dispositivo embarcado;
7. esquema elétrico e fotografia identificada;
8. layout binário da credencial.

Cada seção de implementação deve explicar responsabilidade, entradas, saídas, decisão importante, estado real e limitação. Trechos de código só devem aparecer quando o próprio algoritmo ou representação de bytes for indispensável ao argumento.

### 5.6 Avaliação e resultados

O maior aprendizado do corpus é que cada tipo de evidência responde a uma pergunta diferente:

| Nível | Evidência | O que permite afirmar |
| ---: | --- | --- |
| E0 | intenção, requisito ou diagrama | O comportamento foi projetado. |
| E1 | inspeção de código ou configuração | Existe uma implementação correspondente. |
| E2 | teste de componente | O componente responde nos casos ensaiados. |
| E3 | teste de integração | Componentes determinados interoperam no ambiente descrito. |
| E4 | demonstração física de ponta a ponta | O protótipo executa o fluxo observado naquela montagem. |
| E5 | teste repetido, de campo ou com usuários | Há evidência de desempenho, robustez ou usabilidade nas condições medidas. |
| E6 | avaliação de efeito | Há evidência do benefício humano ou organizacional definido pelo estudo. |

Não se deve pular níveis na redação. Um teste E2 de reconhecimento do QR não demonstra E4, isto é, o destravamento físico completo. Uma avaliação heurística de interface não demonstra E5 com o público-alvo. Uma pesquisa de satisfação não demonstra E6 sobre autonomia ou inclusão.

### 5.7 Conclusão

A conclusão mais segura usa os objetivos específicos como índice. Para cada objetivo, deve informar entrega, evidência, estado e limite. Em seguida, responde à pergunta geral e separa contribuições de continuidade.

Resultados negativos não diminuem automaticamente o trabalho. 2025-C04, 2025-C27, 2024-C20 e 2024-S04 se destacam justamente porque mostram onde o artefato falhou ou ficou incompleto e transformam isso em conhecimento de engenharia.

## 6. Matriz de alegações e evidências para o FLIKE

| Alegação possível | Evidência mínima adequada | Formulação segura antes da evidência |
| --- | --- | --- |
| O frontend executa cadastro, solicitação e consulta | Testes dos fluxos com API e banco, incluindo erros de autorização | “Os fluxos estão implementados no código examinado.” |
| A credencial possui 48 bytes e é interoperável | Vetores comuns entre emissor e firmware, incluindo bytes nulos e altos | “O formato projetado possui 48 bytes.” |
| A tag detecta alteração do payload | Casos válido, byte alterado, segredo incorreto e tranca incorreta | “AES-CMAC foi escolhido para autenticar a mensagem.” |
| A janela de validade é aplicada localmente | Relógio controlado e casos antes, durante e depois do intervalo | “A credencial contém campos temporais destinados a essa verificação.” |
| A tranca opera sem consultar servidor | Fluxo no dispositivo com rede desativada e estado inicial conhecido | “A arquitetura prevê validação local; a obtenção do QR continua online.” |
| O sistema destrava fisicamente | QR emitido, lido, validado e atuador acionado repetidas vezes | “Há uma montagem com ESP32-CAM, transistores, fonte e tranca elétrica.” |
| O leitor é confiável | Repetições por distância, ângulo, brilho, tela e tamanho, com taxa e latência | “A leitura funciona nos casos demonstrados.” |
| A solução é segura | Modelo de ameaça, propriedades delimitadas e ensaios correspondentes | “O protótipo usa autenticação simétrica e assume riscos declarados.” |
| A interface é acessível | Critérios técnicos e, para experiência real, estudo com público-alvo | “A interface foi projetada com requisitos de acessibilidade ainda não avaliados com usuários.” |
| O FLIKE melhora autonomia ou inclusão | Estudo ético e método capaz de medir esse efeito | “Reduzir interações obrigatórias é a motivação da solução.” |

## 7. Plano editorial capítulo a capítulo

### Capítulo 1 — Introdução

- Começar pelo processo concreto de acesso, não pela história geral da Internet das Coisas.
- Sustentar fatos externos com fontes e identificar relatos da equipe como relatos.
- Formular uma pergunta de projeto respondível pelo protótipo.
- Apresentar objetivo geral e objetivos específicos verificáveis.
- Declarar logo no capítulo que a tranca valida localmente, o usuário precisa de internet para obter o QR e não houve estudo com o público-alvo.
- Usar sempre o nome FLIKE.

### Capítulo 2 — Aspectos conceituais

- Definir identificação, autenticação, autorização, credencial, destravamento e entrada.
- Explicar QR Code como transporte, sem atribuir segurança ao código visual.
- Explicar AES-CMAC como autenticação simétrica, incluindo ausência de não repúdio.
- Discutir relógio, validade, cópia, segredo embarcado e revogação no modelo offline.
- Construir quadro de trabalhos relacionados em lugar de resumos independentes.
- Encerrar cada seção com a decisão do FLIKE que o conceito sustenta.

### Capítulo 3 — Método

- Registrar cronologia e divisão real do trabalho.
- Distinguir decisões tomadas durante o projeto da reconstrução documental atual.
- Explicar como escopo e requisitos mudaram.
- Definir antecipadamente os testes que ainda serão executados.
- Não reivindicar metodologia ou participação de usuários sem registro.

### Capítulo 4 — Requisitos

- Normalizar identificadores e termos.
- Separar aplicação, backend, credencial, firmware, circuito e qualidades.
- Dar critério observável a cada requisito.
- Criar matriz requisito–componente–teste–resultado.
- Preservar requisitos removidos ou não atendidos com seu estado, sem apresentá-los como entrega.

### Capítulo 5 — Desenvolvimento

- Abrir com contexto, arquitetura e fluxos; detalhar subsistemas depois.
- Descrever o modelo em que uma pessoa administra instituições próprias e é cliente nas instituições de terceiros.
- Especificar o payload campo a campo e seu processo de autenticação.
- Separar leitura, parsing, autenticação, decisão temporal e acionamento.
- Distinguir API, banco, frontend, firmware, circuito e tranca física em toda afirmação.
- Apresentar testes por requisito, com ambiente, versão, repetição, unidade e resultado.
- Fechar com fluxo integrado, modelo de ameaça e limitações.

### Capítulo 6 — Considerações finais

- Responder a cada objetivo usando apenas resultados já apresentados.
- Denominar o produto como protótipo e declarar o nível de integração alcançado.
- Separar contribuição implementada, aprendizado técnico e promessa futura.
- Registrar ausência de revogação confiável, provisionamento fixo do segredo e falta de avaliação com usuários.
- Não transformar motivação social em impacto demonstrado.

## 8. Vocabulário e controle de alegações

| Preferir | Evitar | Motivo |
| --- | --- | --- |
| FLIKE | CAUSP-LOCK | FLIKE é o nome final do projeto. |
| credencial ou chave temporária | chave de uso único | Ela pode ser reutilizada durante a janela autorizada. |
| autenticação de mensagem por AES-CMAC | assinatura digital, assinatura eletrônica, irretratabilidade | As propriedades criptográficas são diferentes. |
| validação local ou offline pela tranca | sistema inteiro offline | Frontend e emissão dependem da API e da internet. |
| autorizar o destravamento | comprovar entrada, saída ou ocupação | O hardware descrito não mede presença. |
| proprietário ou administrador da instituição | administrador global | O modelo não possui papel global nem campo fixo de função. |
| requisito implementado, testado, parcial ou não atendido | sistema completo | Os subsistemas estão em estados diferentes. |
| risco aceito de revogação | credencial irrevogável ou sempre revogável | A operação offline impede revogação confiável após emissão. |
| aplicação web | aplicativo Flutter | O aplicativo móvel foi abandonado. |

## 9. Elementos visuais e tabelas indispensáveis

1. Diagrama de contexto com usuário, instituição, aplicação e tranca.
2. Diagrama de contêineres fiel aos componentes finais.
3. Modelo entidade-relacionamento fiel ao banco.
4. Sequência de solicitação, aprovação e emissão.
5. Sequência de leitura, autenticação, validação temporal e atuação.
6. Quadro dos 48 bytes da credencial, com tipo, tamanho, endianness e semântica.
7. Diagrama de blocos do ESP32-CAM, câmera, estágio de potência e tranca.
8. Esquema elétrico e fotografia anotada da montagem.
9. Matriz de rastreabilidade dos requisitos.
10. Tabelas dos testes, com caso, condições, repetições, esperado, observado e estado.
11. Quadro final de limitações e consequências.

Cada elemento deve ser citado antes de aparecer, ter fonte e legenda informativa e permanecer legível no tamanho final. Capturas de tela devem demonstrar um fluxo ou estado relevante; não devem ocupar páginas apenas para provar que uma interface existe.

## 10. Erros recorrentes a evitar

- Transformar a fundamentação em catálogo promocional de frameworks.
- Declarar segurança, escala, robustez ou acessibilidade sem métrica correspondente.
- Usar dados fictícios e concluir sobre a integração real.
- Apresentar questionário planejado como avaliação executada.
- Confundir recompensa de modelo, satisfação ou funcionamento interno com efeito externo.
- Omitir ambiente, versões, número de repetições e critérios de aprovação.
- Mostrar somente testes que passaram.
- Empurrar para trabalhos futuros uma função tratada antes como resultado atual.
- Usar porcentagens de redução sem base correta ou acima de 100% para grandezas inadequadas.
- Concluir que o artefato “resolve” o problema social porque o protótipo funciona.
- Inserir longos blocos de código, capturas de ferramentas e diagramas sem interpretação.
- Introduzir tecnologia ou resultado novo na conclusão.
- Alternar futuro e passado de modo que o leitor não saiba o que foi feito.

## 11. Padrão editorial aprovado pela equipe

O padrão sugerido combina seis compromissos:

1. **Estrutura:** seguir a clareza arquitetural de 2025-C28.
2. **Rastreabilidade:** classificar cada requisito como em 2025-C27 e ligá-lo a testes como em 2025-C24 e 2024-S04.
3. **Segurança:** separar mecanismo, propriedade e ameaça como em 2025-C22 e 2024-C06.
4. **Artefato físico:** documentar montagem, condições e falhas como em 2025-C04 e 2024-S01.
5. **Acessibilidade:** distinguir intenção de evidência com o rigor observado em 2024-S02.
6. **Conclusão:** tratar resultados incompletos e negativos como conhecimento de engenharia, sem exagero.

Esse padrão foi aprovado pela equipe em 01/09/2026, com preferência por texto técnico e detalhado e uso abundante de diagramas, tabelas, esquemas e fotografias. Ele deve orientar as rodadas seguintes e servir como lista de verificação na revisão de cada seção.

## 12. Informações que ainda dependem da equipe

As teses de referência ajudam a decidir como escrever, mas não suprem fatos ausentes do FLIKE. Antes dos capítulos correspondentes, a equipe deverá fornecer ou confirmar:

- cronologia real e divisão de responsabilidades;
- fonte institucional e descrição do processo anterior de acesso;
- detalhes do circuito, componentes, alimentação e demonstração física;
- fotos, vídeos, esquemas, logs e versões disponíveis;
- decisões de protocolo que não estejam inequívocas no código;
- testes já realizados fora dos repositórios;
- prazo, normas e orientações específicas da banca ou do orientador.

Informação ausente deverá permanecer como pendência, limitação ou trabalho futuro. Ela não será preenchida por suposição.

## 13. Registro de volume e limite de uso

A leitura foi concluída antes de uma interrupção por limite: **50 teses, 4.064 páginas e 952.287 palavras extraídas** receberam análise. A interface da execução não expõe a quantidade exata de tokens consumida nem a fração da cota antes e depois do trabalho; por isso, não é possível calcular páginas por token ou páginas por cota com rigor.

Este corpus oferece apenas uma referência operacional: uma execução comportou a análise estruturada das 4.064 páginas com extração local e aprofundamento seletivo das seções relevantes. Isso não significa que as 952.287 palavras tenham sido inseridas integralmente no contexto do modelo. Uma estimativa quantitativa futura exigiria registrar na interface a cota no início e no fim de uma sessão equivalente.
