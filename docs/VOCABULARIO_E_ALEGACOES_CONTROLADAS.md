# FLIKE — vocabulário e alegações controladas

**Estado:** aprovado pela equipe

**Rodada:** Fase A, passo 4

**Data:** 01/09/2026

## 1. Finalidade

Este documento controla os termos e as alegações usados na monografia do FLIKE. Seu objetivo é manter texto, figuras, tabelas, resumo, abstract e resultados tecnicamente consistentes com o contrato acadêmico e com as evidências disponíveis.

As regras se aplicam ao texto autoral da monografia. Nomes literais de classes, campos, rotas, diretórios e rótulos antigos de interface poderão ser reproduzidos quando necessários para explicar o código, desde que sejam identificados como nomes da implementação e não substituam o vocabulário acadêmico.

## 2. Regra geral de evidência

Cada verbo deverá corresponder ao nível de evidência realmente disponível:

| Verbo ou expressão | Significado permitido |
| --- | --- |
| **proposto**, **pretendido** | decisão ou objetivo de projeto sem prova de implementação |
| **especificado**, **modelado** | registrado em requisito, contrato, diagrama ou modelo |
| **implementado no código examinado** | mecanismo localizado por inspeção estática; não implica execução bem-sucedida |
| **verificado em teste reproduzível** | executado com procedimento, entrada, ambiente e resultado preservados |
| **demonstrado pela equipe** | observado historicamente segundo relato dos autores; usar essa atribuição quando faltarem registros suficientes |
| **integrado** | comunicação entre componentes foi executada e registrada; mera compatibilidade de interfaces não basta |
| **implantado** | operou no ambiente real de uso; não se aplica ao FLIKE atual |
| **validado com usuários** | avaliado com público-alvo e método documentado; não se aplica ao FLIKE atual |
| **comprovado** | sustentado por evidência forte e diretamente relacionada; evitar para benefícios, segurança ampla e confiabilidade |

Arquivos, dependências, diagramas e código não executado comprovam existência ou intenção de implementação. Eles não comprovam funcionamento, desempenho, integração ou impacto.

## 3. Nome do projeto e contexto institucional

| Usar | Não usar como nome do projeto | Regra |
| --- | --- | --- |
| **FLIKE** | CAUSP-LOCK, CAUSP Lock, CAUSP Lock System | FLIKE é o único nome oficial e não é uma sigla. |
| **Coletivo Autista da USP (CAUSP)** | expandir FLIKE como se fosse sigla | CAUSP aparece somente no contexto que motivou o projeto e na filiação de um dos autores. |
| **sala sensorial da Faculdade de Direito da USP** | generalizar automaticamente para todas as salas sensoriais | É o caso motivador. Quando necessário, explicar que também oferece apoio à amamentação conforme a denominação institucional disponível. |
| **Faculdade de Direito da USP** | Sanfran sem apresentação prévia | “Sanfran” pode aparecer apenas depois do nome formal e quando tiver função narrativa. |

A origem do nome FLIKE, homenagem ao gato de infância de um dos autores, poderá aparecer em apresentação, agradecimentos ou nota contextual se a equipe considerar apropriado. Ela não deverá ser inventada como acrônimo técnico.

## 4. Atores e permissões

| Termo controlado | Definição | Evitar |
| --- | --- | --- |
| **usuário** | pessoa cadastrada no sistema | separar todos os usuários em classes globais rígidas |
| **solicitante** | usuário enquanto solicita acesso a uma tranca de instituição alheia | “cliente” quando o contexto acadêmico não envolver relação comercial |
| **proprietário da instituição** | usuário associado como proprietário no modelo de dados | afirmar que existe papel global de administrador |
| **responsável pela instituição** | denominação narrativa do proprietário ao decidir solicitações | “superadministrador” ou vários administradores sem suporte no modelo |
| **portador da credencial** | usuário para quem uma credencial foi emitida | inferir que ele entrou ou ocupou o ambiente |

Um mesmo usuário pode administrar as instituições das quais é proprietário e solicitar acesso às instituições de outras pessoas. “Administrador” poderá aparecer ao descrever rótulos e caminhos da interface, mas a explicação do domínio deverá deixar claro que se trata de uma responsabilidade contextual, não de uma classe separada de pessoa nem de um campo global de papel.

## 5. Espaços e elementos da tranca

| Termo controlado | Definição |
| --- | --- |
| **instituição** | entidade organizacional possuída por um usuário no sistema |
| **edifício** | agrupamento físico pertencente a uma instituição |
| **sala** | espaço pertencente a um edifício |
| **tranca digital** | entidade lógica cadastrada no backend, associada a uma sala, a um identificador e a um segredo |
| **dispositivo embarcado de controle de acesso** | conjunto formado por ESP32-CAM, câmera, firmware e interface elétrica responsável pela leitura e pela decisão local pretendida |
| **fechadura elétrica** | atuador físico energizado para permitir o destravamento |
| **circuito de potência** | estágio com 2N2222, módulo de relé e caminho de 12 V usado para compatibilizar o comando da ESP32-CAM com o acionamento da fechadura |
| **porta** | elemento físico cujo estado não é sensoriado pelo protótipo |

Evitar usar “tranca”, “fechadura”, “porta” e “tranca digital” como sinônimos no mesmo trecho. Depois que o componente estiver inequívoco, uma forma curta poderá ser usada localmente.

## 6. Solicitação, permissão e credencial

| Termo controlado | Definição | Formulação que deve ser evitada |
| --- | --- | --- |
| **solicitação de acesso** | pedido criado por um usuário para obter acesso por uma tranca | autorização recorrente automática |
| **aprovação** ou **rejeição** | decisão do responsável sobre uma solicitação pendente | revogação de credencial já emitida |
| **emissão** | criação de uma credencial após aprovação ou pela rota administrativa correspondente | geração da imagem como se criasse nova credencial |
| **credencial digital** | payload binário emitido para um usuário e uma tranca | usar apenas “chave”, que pode significar chave mecânica ou criptográfica |
| **chave digital** | nome de domínio/interface legado; ao primeiro uso, explicar que corresponde à credencial digital | tratar como chave criptográfica |
| **uma credencial por solicitação aprovada** | política de emissão escolhida | “uma única utilização” |
| **janela de validade** | intervalo definido pelos timestamps de emissão e expiração | afirmar que o firmware preservado aplica esse intervalo sem ressalva |
| **reapresentação durante a validade** | a mesma credencial pode ser apresentada várias vezes dentro da janela | “uso único” ou “descartável após a primeira leitura” |
| **expiração** | término da janela de validade | confundir com uso anterior |
| **revogação** | invalidação antecipada de uma credencial ainda válida | afirmar que está implementada ou é confiável no modelo offline |

O frontend transforma os bytes codificados em hexadecimal em uma imagem QR. Portanto, a API emite o payload da credencial e o frontend renderiza sua representação em QR Code. Abrir novamente o modal não emite outra credencial.

## 7. QR Code e formato binário

| Termo controlado | Regra |
| --- | --- |
| **QR Code** | meio de transporte visual do payload; não é, por si só, mecanismo de segurança |
| **payload binário de 48 bytes** | 32 bytes de mensagem seguidos por 16 bytes de tag AES-CMAC |
| **identificador da tranca** | identifica a tranca digital destinatária; não chamar automaticamente de identificador da sala |
| **timestamp de emissão** e **timestamp de expiração** | campos temporais da credencial |
| **serialização** | conversão estruturada dos campos em bytes |
| **codificação hexadecimal** | representação textual dos bytes usada entre componentes; não é criptografia |
| **renderização do QR Code** | conversão do payload em imagem no frontend |
| **leitura** | captura visual de um QR Code pela câmera |
| **decodificação** | recuperação dos bytes contidos no símbolo visual |

Evitar “QR Code criptográfico” como se o símbolo tivesse uma propriedade criptográfica intrínseca. Preferir “QR Code que transporta uma credencial autenticada por AES-CMAC”.

## 8. Criptografia e autenticação da mensagem

| Usar | Significado | Não usar |
| --- | --- | --- |
| **AES-CMAC** | algoritmo de código de autenticação de mensagem baseado em AES | “algoritmo de assinatura digital” |
| **tag de autenticação** ou **tag CMAC** | valor de 16 bytes anexado à mensagem | assinatura digital |
| **chave criptográfica simétrica** ou **segredo compartilhado** | segredo de 32 bytes conhecido pelo backend e pelo dispositivo | chave privada, par público/privado |
| **gerar o CMAC** | calcular a tag sobre a mensagem | assinar digitalmente o QR Code |
| **verificar o CMAC** | recalcular e comparar a tag para verificar mensagem e segredo | descriptografar o QR Code |
| **autenticidade da mensagem** | evidência de que a tag foi produzida por quem conhece o segredo, sob as premissas do mecanismo | identidade individual do autor ou não repúdio |
| **integridade da mensagem** | detecção de alteração da mensagem sem tag válida | confidencialidade |

O payload não é cifrado e seus campos podem ser lidos por quem decodificar o QR Code. O AES-CMAC não oferece confidencialidade nem não repúdio. Como backend e dispositivo conhecem o mesmo segredo, o mecanismo não identifica qual deles produziu uma tag válida.

Não usar “assinatura eletrônica” como sinônimo frouxo. Se o requisito antigo com esse nome for discutido, classificá-lo como reformulado para autenticação simétrica de mensagem.

### 8.1 Protocolo histórico e protocolo final

O protótipo do Laboratório de Processadores usava HMAC-SHA1, tag de 20 bytes, mensagem variável e tipos de mensagem para acesso, sincronização, configuração e depuração. O protocolo final examinado usa AES-CMAC, tag de 16 bytes e payload fixo de 48 bytes com usuário, tranca, emissão e expiração.

Usar **HMAC-SHA1** ao descrever a etapa histórica e o vídeo correspondente. Usar **AES-CMAC** ao descrever a implementação e a demonstração final realizada em 31/08/2026. A formulação categórica autorizada é: **“O protótipo físico do FLIKE realizou, de ponta a ponta, a leitura do QR Code, a validação local por AES-CMAC, a emissão do sinal de comando e o acionamento da fechadura elétrica.”**

## 9. Operação local e dependência de rede

Formulação controlada:

> A arquitetura do FLIKE permite que o dispositivo embarcado verifique localmente a credencial, sem consultar o servidor no momento da leitura. Na demonstração física final, a ESP32-CAM leu o QR Code, validou localmente o payload por AES-CMAC, emitiu o sinal `HIGH` e acionou a fechadura por meio do circuito elétrico.

“Operação offline” deverá sempre indicar **qual componente** e **qual operação**. A aplicação web, a API, a solicitação, a aprovação e a obtenção inicial da credencial dependem de rede. A ausência de consulta no momento da leitura também impede revogação confiável de uma credencial já emitida, a menos que exista mecanismo adicional de atualização local, que não faz parte do protótipo.

Evitar as formulações absolutas “o sistema funciona offline” e “a tranca valida completamente a credencial offline”.

## 10. Estados físicos e eventos

| Etapa | O que significa | O que não comprova |
| --- | --- | --- |
| **leitura do QR Code** | a câmera capturou um símbolo reconhecível | autenticidade, autorização ou abertura |
| **decodificação do payload** | os bytes foram recuperados | integridade ou permissão |
| **verificação do AES-CMAC** | a tag é compatível com a mensagem e o segredo usado | validade temporal, tranca destinatária ou presença do usuário correto |
| **decisão de autorização** | todas as regras adotadas foram avaliadas | acionamento físico |
| **acionamento de destravamento** | o dispositivo emitiu o comando elétrico | movimento confirmado da porta |
| **fechadura acionada** | o atuador respondeu ao circuito | porta aberta ou pessoa presente |
| **porta aberta/fechada** | exige sensor ou observação específica | entrada, saída ou ocupação |
| **entrada/saída** | exige evidência da passagem de uma pessoa e de sua direção | ocupação atual sem controle adicional |
| **ocupação** | quantidade ou presença de pessoas no espaço | não pode ser inferida pelo protótipo atual |

O endpoint de “uso” e o campo `used_at` registram estado no servidor. Sem chamada autenticada e vinculada ao dispositivo físico, eles não comprovam leitura, autorização, acionamento, abertura ou entrada.

## 11. Tecnologias da arquitetura final

| Camada | Termo oficial | Não apresentar como solução final |
| --- | --- | --- |
| frontend | **aplicação web Next.js/React** | páginas HTML do MVP, aplicativo Flutter |
| backend | **API em Python com FastAPI** | API genérica sem identificar a tecnologia quando ela for relevante |
| persistência | **MySQL** | PostgreSQL, AWS S3 |
| dispositivo | **ESP32-CAM com câmera OV2640** | gateway, Bluetooth, MQTT |
| credencial | **payload autenticado por AES-CMAC e transportado por QR Code** | QR cifrado, assinatura digital |
| atuador | **fechadura Papaiz AA-ERL200P acionada por estágio com 2N2222 e módulo de relé de 12 V** | botão de saída previsto, mas não montado no protótipo |

As tecnologias abandonadas poderão aparecer na reconstrução histórica das decisões, claramente identificadas como propostas descartadas. Não deverão permanecer em diagramas da arquitetura final, resumo, abstract ou conclusões.

## 12. Acessibilidade, autonomia e segurança

### 12.1 Alegações permitidas

- O projeto **foi motivado** por barreiras percebidas no processo de acesso à sala sensorial.
- A equipe **buscou reduzir** a necessidade de retirada presencial de chave e de interação no momento da entrada.
- A interface e o fluxo **foram projetados com requisitos de acessibilidade definidos pela equipe**.
- A aprovação digital **pode reduzir** algumas interações presenciais, como hipótese de benefício.
- O AES-CMAC **protege a autenticidade e a integridade da mensagem sob a premissa de proteção do segredo compartilhado**.
- A decisão local **reduz a dependência de disponibilidade do servidor no instante da leitura**, dentro dos limites descritos.

### 12.2 Alegações que exigem ressalva

- “Acessível”: somente como intenção ou propriedade examinada por critérios técnicos; não como resultado validado com pessoas autistas.
- “Seguro”: somente com dimensão e mecanismo definidos, por exemplo integridade do payload; nunca como avaliação global do sistema.
- “Autônomo”: especificar autonomia em relação à retirada física de chaves ou à consulta do servidor; a aprovação administrativa continua necessária.
- “Baixo custo”: exige lista de materiais, valores, data e critério de comparação, ainda indisponíveis.
- “Eficiente”: exige métrica de tempo, recursos ou sucesso, ainda não consolidada.
- “Confiável”: exige protocolo e resultados de repetição, falha e recuperação.
- “Escalável”: exige análise de carga, crescimento ou arquitetura correspondente.

### 12.3 Alegações proibidas com a evidência atual

- O FLIKE promoveu bem-estar, inclusão ou acessibilidade comprovada.
- O FLIKE reduziu constrangimento, sobrecarga cognitiva ou subutilização da sala.
- O FLIKE impediu furtos ou aumentou mensuravelmente a segurança do espaço.
- O público-alvo aprovou ou validou o sistema.
- A solução está pronta para produção ou foi implantada na Faculdade de Direito.
- O sistema garante confidencialidade, disponibilidade, não repúdio ou segurança integral.
- A tranca atual controla entrada, saída ou ocupação.

## 13. Alegações controladas por nível de evidência

| Tema | Formulação autorizada | Condição |
| --- | --- | --- |
| fluxo web | “A equipe relata ter demonstrado o fluxo da solicitação à disponibilização da credencial; os componentes principais foram localizados nos repositórios.” | mencionar as divergências de contrato ao discutir reprodutibilidade |
| leitura física | “A equipe relata que a ESP32-CAM reconheceu e decodificou o QR Code.” | até haver registro preservado do ensaio |
| autenticação local histórica | “O relatório e o vídeo documentam autenticação HMAC-SHA1 no protótipo do Laboratório de Processadores.” | não atribuir AES-CMAC a esse ensaio |
| autenticação local final | “O firmware final examinado implementa verificação AES-CMAC, e a equipe relata diversos testes bem-sucedidos do protocolo com QR Codes.” | distinguir inspeção do código e relato de ensaio |
| acionamento | “O material histórico documenta que o estágio com 2N2222 e relé acionou a fechadura elétrica.” | não inferir abertura da porta ou entrada de uma pessoa |
| integração física completa | “O protótipo físico do FLIKE realizou, de ponta a ponta, a leitura do QR Code, a validação local por AES-CMAC, a emissão do sinal de comando e o acionamento da fechadura elétrica.” | resultado confirmado pela equipe em 01/09/2026; complementar com registro do ensaio, se disponível |
| validade | “A credencial contém emissão e expiração e foi concebida para uma janela de validade.” | declarar que a checagem temporal completa não foi localizada no firmware preservado |
| revogação | “A arquitetura aceita o risco de não revogar de forma confiável uma credencial já emitida.” | não prometer invalidação antecipada offline |
| requisitos | “A equipe derivou requisitos a partir de sua avaliação do cenário.” | não chamar de necessidade validada pelo público-alvo |
| caso motivador | “Um autor tomou conhecimento das dificuldades por experiência própria, reunião institucional e relatos informais.” | não transformar em resultado de pesquisa social |

## 14. Substituições obrigatórias na futura redação

| Expressão antiga | Substituição ou tratamento |
| --- | --- |
| CAUSP-LOCK | FLIKE |
| código de uso único | credencial reutilizável durante a janela de validade |
| QR Code assinado digitalmente | QR Code que transporta payload autenticado por AES-CMAC |
| assinatura criptográfica | tag de autenticação AES-CMAC |
| chave privada compartilhada | chave criptográfica simétrica provisionada previamente |
| QR Code criptografado | payload serializado e autenticado, sem confidencialidade |
| autenticidade, integridade e irretratabilidade garantidas | autenticidade e integridade da mensagem sob as premissas do AES-CMAC; sem não repúdio |
| sistema funciona offline | na demonstração física final, o dispositivo verificou localmente a credencial AES-CMAC e acionou a fechadura sem consultar o servidor; aplicação web e emissão inicial dependem de rede |
| administrador | proprietário ou responsável pela instituição, salvo rótulo literal da interface |
| cliente | solicitante ou usuário, conforme o estado do fluxo |
| backend gera o QR Code | backend emite o payload; frontend renderiza a imagem QR |
| controla a ocupação | apresenta registros de credenciais; não mede ocupação |
| aplicativo | aplicação web |
| frontend React | aplicação web Next.js/React |
| banco SQL/PostgreSQL | banco de dados MySQL |
| acesso garantido | acesso pretendido ou autorização concedida, conforme a evidência |

## 15. Vocabulário para o abstract

| Português | Inglês controlado |
| --- | --- |
| controle de acesso físico | physical access control |
| credencial digital temporária | temporary digital credential |
| solicitação de acesso | access request |
| janela de validade | validity window |
| código de autenticação de mensagem | message authentication code |
| segredo compartilhado | shared secret |
| verificação local | local verification |
| dispositivo embarcado de controle de acesso | embedded access-control device |
| fechadura elétrica | electric lock |
| acionamento de destravamento | unlock actuation |
| proprietário da instituição | institution owner |
| responsável pela instituição | person responsible for the institution |
| relato da equipe | team-reported demonstration |

Evitar *digital signature*, *single-use code*, *non-repudiation*, *encrypted QR Code*, *global administrator*, *occupancy control* e *fully offline system* ao descrever a implementação.

## 16. Auditoria inicial da tese atual

A busca foi feita nos arquivos `.tex` e `.bib` antes de qualquer reescrita dos capítulos. Os números servem para planejar as rodadas; uma ocorrência pode estar em contexto histórico ou bibliográfico e será revisada individualmente.

| Padrão encontrado | Ocorrências | Locais representativos | Ação futura |
| --- | ---: | --- | --- |
| `CAUSP-LOCK` | 7 | `main.tex`, Cap. 1 e Cap. 5 | substituir pelo nome FLIKE |
| “uso único” / *single-use* | 4 | resumo, abstract, Cap. 1 e requisito RF-07-00 | substituir pela política de janela de validade |
| assinatura digital / *digitally signed* | 2 | resumo e abstract | reformular como AES-CMAC |
| irretratabilidade / *non-repudiation* | 4 | resumo, abstract, Cap. 1 e RF-06-03 | remover como propriedade alcançada |
| formulações criptográficas imprecisas | 6 | resumo, abstract, palavras-chave, Cap. 1 e Cap. 5 | distinguir autenticação, codificação e cifragem |
| aplicativo inexistente | 1 | objetivo do Cap. 1 | manter somente aplicação web |
| controle de ocupação | 1 | Cap. 5 | remover; não há sensor ou inferência válida |
| sobrecarga cognitiva como resultado/requisito amplo | 3 | Cap. 1 e Cap. 4 | tratar como motivação ou requisito autoral não validado |
| verbos de garantia absoluta | 9 | resumo, abstract, Cap. 1 e requisitos | substituir por verbo ligado à evidência específica |

Os trechos mais críticos estão no resumo e no abstract de `FLIKE/main.tex`, na introdução, nos requisitos criptográficos do Capítulo 4 e na visão geral do Capítulo 5. Eles não serão corrigidos isoladamente agora: cada capítulo será reescrito em sua rodada, usando este documento como regra de aceitação.

## 17. Checklist editorial por seção

Antes de aprovar qualquer seção da monografia, verificar:

1. O projeto é chamado exclusivamente de FLIKE?
2. Atores e responsabilidades contextuais estão descritos sem inventar papéis globais?
3. Credencial digital, chave criptográfica e chave mecânica estão distinguidas?
4. AES-CMAC é descrito como autenticação simétrica, sem cifragem, assinatura digital ou não repúdio?
5. Leitura, decodificação, autenticação, autorização, acionamento, abertura e entrada estão separadas?
6. “Offline” identifica componente e operação?
7. Validade temporal e revogação estão acompanhadas de seus limites reais?
8. Demonstração relatada e execução reproduzível estão distinguidas?
9. Benefícios de acessibilidade aparecem como motivação ou hipótese, não como impacto medido?
10. Toda alegação de segurança, eficiência, confiabilidade ou baixo custo informa mecanismo, métrica ou limitação?
11. Tecnologias abandonadas aparecem apenas como histórico claramente marcado?
12. O texto em inglês preserva as mesmas restrições do texto em português?

## 18. Portão de aprovação do passo 4

Para concluir o passo 4, a equipe deverá aprovar ou corrigir:

1. os nomes dos atores e dos componentes físicos;
2. o uso de “credencial digital” como termo acadêmico principal;
3. a terminologia AES-CMAC;
4. a formulação controlada de operação local;
5. a separação entre eventos físicos;
6. as alegações permitidas, condicionais e proibidas;
7. o vocabulário português–inglês.

Com essa aprovação, a Fase A será encerrada e a próxima rodada será o passo 5: reconstruir e validar os requisitos do Capítulo 4 antes de reescrevê-lo.
