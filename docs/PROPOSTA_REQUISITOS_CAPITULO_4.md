# FLIKE — proposta de reconstrução dos requisitos do Capítulo 4

**Estado:** aprovado pela equipe

**Rodada:** Fase B, passo 5

**Data:** 01/09/2026

> **Adendo da Fase B:** a revisão colaborativa do passo 6 substituiu o RF-09 original por RF-09 (conteúdo da credencial) e RF-10 (autenticação da credencial), acrescentou RNF-05 para fixar QR Code versão 3-L e reorganizou os requisitos seguintes. A equipe posteriormente excluiu o requisito autônomo de acionamento da fechadura. A decisão sobre 3-L substitui, somente nesse ponto, a recomendação P4 registrada neste documento. Os documentos de proposta de cada bloco registram a redação vigente.

## 1. Finalidade e limite desta rodada

Este documento propõe a organização, os identificadores, a redação e os critérios de verificação dos requisitos do FLIKE. Ele é o portão de decisão anterior à reescrita do Capítulo 4. Nesta rodada, `FLIKE/capitulos/Cap4-Especificacao.tex` permanece inalterado.

A proposta segue quatro regras:

1. cada requisito deve expressar comportamento ou qualidade verificável;
2. decisões arquiteturais, tecnologias e detalhes de implementação não serão apresentados automaticamente como requisitos;
3. requisitos derivados pela equipe serão identificados como requisitos de projeto, sem alegar validação pelo público-alvo;
4. o estado de cumprimento será separado da redação do requisito: um requisito pode representar corretamente o produto e ainda estar parcial, não atendido ou não avaliado.

## 2. Fontes usadas

A reconstrução confronta:

- o Capítulo 4 atual;
- o contrato acadêmico aprovado;
- o vocabulário e as alegações controladas aprovados;
- o levantamento da arquitetura e dos repositórios;
- o relato da equipe sobre o fluxo completo de software;
- a demonstração física ponta a ponta com AES-CMAC confirmada em 01/09/2026;
- o protocolo final de uma credencial por solicitação, reutilizável durante sua janela de validade.

## 3. Diagnóstico do capítulo atual

O capítulo contém 25 enunciados, contando separadamente os três itens repetidos como `REQ-FUNC-01`. Os principais problemas são:

- IDs repetidos e lacuna de numeração;
- requisitos amplos que agregam vários comportamentos independentes;
- mistura de requisitos funcionais, qualidades, componentes e decisões de implementação;
- propriedades absolutas sem critério de teste, como “seguro”, “auditável” e “qualquer tipo ou modelo”;
- metas sem base ou evidência, como autonomia de seis horas e MTTF superior a seis meses;
- termos incompatíveis com o protocolo final, como sala, uso único, assinatura eletrônica e irretratabilidade;
- ausência de requisitos explícitos para solicitação, decisão administrativa e emissão de uma credencial por solicitação;
- acessibilidade formulada como efeito humano amplo, embora não tenha havido avaliação com usuários.

## 4. Estrutura proposta para o Capítulo 4

### 4.1 Origem, método e limites dos requisitos

Explicar que os requisitos foram derivados pela equipe a partir da experiência de um autor, da reunião institucional, de relatos informais, do protótipo anterior e das decisões tomadas durante a implementação. Declarar que não houve elicitação formal nem validação com o público-alvo.

### 4.2 Escopo, atores e entidades

Definir usuário, responsável por instituição, instituição, prédio, sala, tranca digital, tranca física, solicitação e credencial digital. Explicar que o papel administrativo é contextual e decorre da propriedade da instituição.

### 4.3 Requisitos funcionais

Organizar pelos fluxos do produto, em vez de criar uma seção para cada peça de hardware ou camada de software:

1. identidade e responsabilidade contextual;
2. cadastro da estrutura física;
3. solicitação e decisão de acesso;
4. emissão e apresentação da credencial;
5. validação local e acionamento físico;
6. consulta administrativa.

### 4.4 Requisitos não funcionais

Registrar qualidades verificáveis de operação local, autorização, proteção do segredo e responsividade da interface. Metas numéricas só permanecerão quando houver justificativa e protocolo de avaliação.

### 4.5 Requisitos de acessibilidade definidos pela equipe

Apresentar critérios técnicos que possam ser inspecionados, sem afirmar redução comprovada de sobrecarga cognitiva ou impacto social.

### 4.6 Restrições e decisões arquiteturais

Descrever separadamente plataforma ESP32-CAM, circuito usado, AES-CMAC, payload de 48 bytes, segredo provisionado pelo fornecedor e dependência de internet para gestão e obtenção inicial do QR Code. Esses elementos explicam como a solução foi construída; não precisam ser transformados em requisitos redundantes.

### 4.7 Matriz de rastreabilidade

Para cada requisito, relacionar origem, critério de verificação, evidência e estado: **atendido**, **parcialmente atendido**, **não atendido** ou **não avaliado**.

## 5. Catálogo funcional proposto

Os estados abaixo são uma classificação inicial para orientar a futura matriz. Eles não substituem os testes dos passos 14–16.

| ID | Redação proposta | Critério observável de verificação | Estado inicial |
| --- | --- | --- | --- |
| **RF-01** | O sistema deve permitir o cadastro e a autenticação de usuários. | Criar uma conta válida, autenticar com suas credenciais e obter uma sessão aceita em rota protegida. | Atendido no código e no relato do fluxo. |
| **RF-02** | Um usuário autenticado deve poder administrar as instituições das quais é proprietário e solicitar acesso a instituições pertencentes a outros usuários. | Com duas contas, verificar administração apenas da instituição própria e criação de solicitação para tranca de instituição alheia. | Parcialmente atendido: modelo contextual existe, mas há rotas públicas que contornam a política. |
| **RF-03** | O responsável deve poder cadastrar e administrar instituições, prédios, salas e trancas digitais em uma hierarquia coerente. | Criar, consultar, alterar e excluir cada nível, verificando vínculos e autorização do proprietário. | Atendido no fluxo principal, sujeito às divergências já catalogadas. |
| **RF-04** | Toda solicitação de acesso deve identificar exatamente uma tranca digital destinatária. | Criar solicitação e confirmar o `digital_lock_id`; em sala com várias trancas, exigir escolha explícita ou política documentada de segredo compartilhado. | Parcialmente atendido: o frontend escolhe implicitamente a primeira tranca. |
| **RF-05** | O usuário autenticado deve poder solicitar uma credencial para uma tranca e acompanhar o estado `pending`, `approved` ou `rejected` da solicitação. | Submeter pedido e consultar cada transição de estado no painel do solicitante. | Implementação estática localizada: criação e consulta do próprio usuário estão nas referências finais; execução ainda deve ser avaliada. |
| **RF-06** | O responsável pela instituição destinatária deve poder consultar e aprovar ou rejeitar solicitações pendentes. | Garantir que o proprietário correto veja e decida o pedido uma única vez e que outro usuário não consiga fazê-lo. | Atendido no núcleo da API e no relato da demonstração; contratos de detalhes divergem. |
| **RF-07** | Cada solicitação aprovada deve gerar uma credencial digital, enquanto uma solicitação rejeitada não deve gerar credencial. | Comparar banco e resposta antes/depois das duas decisões e verificar relação inequívoca com o pedido. | Parcialmente atendido: o fluxo existe, mas emissão e mudança de estado não são atômicas e não há FK da solicitação para a credencial. |
| **RF-08** | O usuário deve poder consultar suas credenciais emitidas e apresentar o QR Code correspondente durante a janela de validade. | Abrir o painel após aprovação, recuperar o payload e renderizar o QR; verificar disponibilidade durante toda a janela. | Parcialmente atendido: modal existe; carregamento integrado e persistência/download têm lacunas. |
| **RF-09** | A credencial deve transportar, em 48 bytes, os identificadores do usuário e da tranca, os instantes de emissão e expiração e uma tag AES-CMAC calculada sobre os campos anteriores. | Comparar o payload emitido com o layout de 32 bytes de mensagem e 16 bytes de tag e validar um vetor comum entre backend e firmware. | Implementado no backend; teste cruzado reproduzível ainda deve ser registrado. |
| **RF-10** | A tranca física deve ler o QR Code e recuperar exatamente o payload binário da credencial. | Apresentar QR com os 48 bytes esperados e comparar os bytes decodificados no dispositivo. | Demonstrado fisicamente pela equipe. |
| **RF-11** | Antes do acionamento, a tranca deve verificar localmente o tamanho e o formato do payload, a tag AES-CMAC, a identidade da tranca destinatária e a janela de validade. | Testar payload válido e casos com tamanho, tag, tranca, emissão e expiração inválidos; somente o caso válido pode autorizar. | Parcialmente atendido: AES-CMAC foi demonstrado; o firmware preservado não contém todas as verificações. |
| **RF-12** | Uma credencial válida deve poder ser reapresentada durante sua janela de autorização e deve ser rejeitada fora dela. | Apresentar a mesma credencial mais de uma vez dentro do intervalo e antes/depois do intervalo; observar as decisões esperadas. | Política aprovada; implementação preservada diverge por usar a flag `used` e não verificar toda a janela. |
| **RF-13** | Quando a autorização local for concedida, a ESP32-CAM deve emitir o sinal elétrico que comanda o circuito e aciona a fechadura. | Observar, em uma execução ponta a ponta, QR válido, decisão positiva, sinal `HIGH`, atuação do relé e resposta da fechadura. | Atendido e demonstrado de ponta a ponta em 31/08/2026, segundo confirmação da equipe. |
| **RF-14** | O responsável deve poder consultar os portadores e o histórico de credenciais referentes às instituições que administra. | Consultar apenas registros dentro do escopo do proprietário e distinguir credencial emitida de evento físico. | Parcialmente atendido: consultas existem, mas não constituem auditoria de abertura, entrada ou ocupação. |

## 6. Catálogo não funcional proposto

| ID | Redação proposta | Critério observável de verificação | Estado inicial |
| --- | --- | --- | --- |
| **RNF-01** | A decisão de autorização e o acionamento da fechadura não devem depender de consulta ao servidor no momento da leitura. | Desconectar a rede do dispositivo e executar leitura, validação AES-CMAC e acionamento com segredo e relógio previamente disponíveis. | Atendido quanto à validação e ao acionamento demonstrados; a decisão temporal completa deve ser verificada separadamente. |
| **RNF-02** | Operações administrativas e decisões sobre solicitações devem exigir autenticação e respeitar a propriedade da instituição. | Executar matriz de acesso com proprietário, usuário autenticado sem propriedade e chamada sem token. | Parcialmente atendido: `/admin` aplica a regra, mas rotas públicas sensíveis permanecem. |
| **RNF-03** | O segredo AES-CMAC de cada tranca não deve ser exposto a usuários, respostas públicas ou registros de aplicação. | Inspecionar contratos e respostas e confirmar que nenhum endpoint ou log devolve `secret_key`. | Não atendido no estado examinado: consultas públicas serializam o segredo. |
| **RNF-04** | A aplicação web deve manter suas funções principais utilizáveis em larguras de tela representativas de celular e computador. | Executar cadastro, solicitação, decisão e consulta do QR nos viewports definidos no protocolo de avaliação, sem perda de conteúdo ou controle essencial. | Não avaliado. |

A meta antiga de leitura em menos de dois segundos será tratada como **métrica de avaliação**, não como requisito obrigatório, até que a equipe forneça justificativa para o limite e aceite executar um ensaio de latência com repetições.

## 7. Requisitos de acessibilidade propostos

Esses requisitos são derivados pela equipe e não foram validados com participantes. Seu atendimento poderá ser avaliado tecnicamente; nenhum deles autoriza afirmar redução comprovada de sobrecarga cognitiva.

| ID | Redação proposta | Critério observável de verificação | Estado inicial |
| --- | --- | --- | --- |
| **RA-01** | Depois de receber uma credencial válida, o usuário deve conseguir acionar a tranca sem interação obrigatória com funcionários no momento da entrada. | Executar o percurso do QR Code ao acionamento sem intervenção humana adicional nem consulta ao servidor. | Atendido na demonstração física; a autorização inicial continua dependendo do responsável. |
| **RA-02** | A aplicação web deve comunicar carregamento, sucesso, erro e estado das solicitações e credenciais por texto compreensível, sem depender apenas de cor. | Inspecionar e executar os fluxos principais, verificando rótulos textuais para todos os estados e erros relevantes. | Parcialmente atendido; requer inspeção sistemática. |
| **RA-03** | O fluxo de solicitação deve apresentar instituição, prédio, sala, tranca e estado do pedido em uma sequência previsível e identificada. | Percorrer o fluxo e verificar ordem, rótulos, retorno de erro e confirmação da ação. | Parcialmente atendido; a escolha da tranca é implícita. |
| **RA-04** | A interface física deve evitar estímulos luminosos ou sonoros desnecessários além daqueles inerentes ao acionamento eletromecânico. | Inventariar sinais emitidos pelo protótipo e verificar ausência de luz intermitente intensa, alarme ou som acessório não necessário. | Não avaliado; o requisito depende de aprovação da equipe. |

## 8. Tratamento proposto para cada requisito antigo

| Requisito antigo | Decisão recomendada | Destino |
| --- | --- | --- |
| `RF-00-00` — controle seguro, auditável e automatizado | Dividir; remover adjetivos absolutos. | RF-01 a RF-14 e RNF-01 a RNF-03. |
| `RNF-00-00` — confidencialidade, integridade e disponibilidade globais | Dividir e limitar ao que pode ser verificado; não alegar conformidade geral. | RNF-02 e RNF-03; integridade da mensagem em RF-09/RF-11. |
| `RF-01-00` — destravar sem internet | Manter com fronteira explícita. | RF-13 e RNF-01. |
| `RF-01-01` — aceitar qualquer tranca elétrica | Remover a universalidade; descrever o relé e a fechadura demonstrada como decisão arquitetural. | Capítulos 4.6 e 5. |
| `RF-01-02` e `RF-01-03` — queda de energia e seis horas | Remover do produto final. | Poderão aparecer como limitação ou continuidade. |
| `RNF-01-00` — MTTF maior que seis meses | Remover por ausência de fundamento e de ensaio de confiabilidade. | Limitação, se relevante. |
| `RF-02-00` — abertura por chave física | Remover, salvo confirmação de que a contingência mecânica faz parte do protótipo final. | Decisão pendente P4. |
| `RF-03-00` — leitura legítima destrava | Manter e decompor a decisão. | RF-10 a RF-13. |
| `RF-03-01` e `RF-03-02` — eventos e histórico interno | Remover do escopo implementado; o protótipo não possui sensores nem log local persistente. | Limitação e continuidade. |
| `RF-04-00` — QR Code versão 3 | Remover a versão fixa; exigir recuperação correta do payload. | RF-10. |
| `RF-05-00` — HMI física com feedback | Remover como componente autônomo; manter feedback web e critério sensorial. | RA-02 e RA-04. |
| `RF-06-00` — usuário, sala, geração e expiração | Reformular com identificação da tranca e layout exato. | RF-09. |
| `RF-06-01` e `RF-06-02` — autenticidade e integridade | Manter com mecanismo e premissas explícitos. | RF-09 e RF-11. |
| `RF-06-03` — irretratabilidade | Remover; AES-CMAC simétrico não fornece não repúdio. | Limitação de segurança. |
| `RF-06-04` — assinatura eletrônica | Reformular como tag de autenticação AES-CMAC. | RF-09 e RF-11. |
| `RNF-06-00` — leitura em menos de dois segundos | Converter em métrica de avaliação até haver justificativa para o limite. | Passos 14–16. |
| `RF-07-00` — expiração e uso único | Substituir “uso único” pela política de reutilização dentro da janela. | RF-11 e RF-12. |
| `RF-09-00` — todas as funções do frontend em um item | Dividir pelos casos de uso e separar responsividade. | RF-01, RF-03 a RF-08, RF-14 e RNF-04. |
| `RF-10-00` — todas as funções do backend em um item | Dividir; remover assinatura e auditoria absolutas. | RF-01 a RF-09, RF-14, RNF-02 e RNF-03. |
| três itens `REQ-FUNC-01` | Substituir por IDs únicos e critérios técnicos sem alegar impacto medido. | RA-01 a RA-04. |

## 9. Decisões aprovadas pela equipe

| ID | Recomendação | Consequência da aprovação |
| --- | --- | --- |
| **P1** | Aprovar os 14 requisitos funcionais propostos. | Eles formarão o núcleo da reescrita do Capítulo 4. |
| **P2** | Aprovar os quatro requisitos não funcionais propostos. | Segurança global, disponibilidade absoluta e outras promessas vagas deixam de aparecer. |
| **P3** | Aprovar RA-01 a RA-03 e decidir se RA-04 representa a interface física desejada. | Acessibilidade passa a ter critérios técnicos, preservando a ausência de avaliação com usuários. |
| **P4** | Remover do escopo: bateria/seis horas, MTTF, compatibilidade com qualquer tranca, log físico persistente, QR versão 3 e HMI física dedicada. Remover também a abertura por chave mecânica, salvo confirmação contrária. | O capítulo deixa de prometer funções abandonadas ou não demonstradas. |
| **P5** | Exigir que cada solicitação identifique uma tranca; quando houver várias trancas na sala, a interface deverá permitir escolha explícita. | Elimina a seleção silenciosa da primeira tranca e mantém a credencial vinculada ao atuador correto. |
| **P6** | Não fixar 24 horas como requisito universal; permitir que a aprovação defina `expires_at` e usar, quando essa data não for informada, 24 horas contadas do processamento da aprovação e da emissão da credencial — não da criação da solicitação nem do primeiro uso. | Reproduz o comportamento atual da API sem transformar o valor padrão em regra de domínio definitiva. |
| **P7** | Tratar dois segundos como métrica de avaliação, não requisito obrigatório. | A latência será medida e relatada sem classificar o sistema como falho por um limite arbitrário. |
| **P8** | Substituir irretratabilidade do usuário físico por rastreabilidade da conta e da credencial: registrar que uma conta autenticada originou uma solicitação e que uma credencial emitida para essa conta foi apresentada e autorizada pela tranca. Remover assinatura eletrônica, uso único e auditoria de entrada/ocupação. | Preserva as evidências produzidas pelo sistema sem concluir que a pessoa física titular executou a ação ou entrou no espaço. |

### 9.1 Limite de atribuição em P8

Mesmo sob a premissa de que os segredos permaneçam protegidos no servidor e na ESP32-CAM, o FLIKE não produz irretratabilidade criptográfica da pessoa física:

Essa distinção segue a terminologia do NIST: um [MAC](https://csrc.nist.gov/glossary/term/message_authentication_code) fornece autenticidade e integridade, mas não proteção de não repúdio; [não repúdio](https://csrc.nist.gov/glossary/term/non_repudiation) exige evidência atribuível a uma entidade específica e verificável por terceiros.

1. o pedido autenticado sustenta que uma sessão vinculada à conta submeteu a solicitação, mas não prova por si só quem operava o navegador;
2. o QR Code funciona como credencial de apresentação e pode ser copiado ou compartilhado;
3. o `user_id` dentro do payload identifica o titular da credencial, não a pessoa presente diante da câmera;
4. AES-CMAC usa segredo simétrico compartilhado; quem verifica a tag também possui material capaz de gerar uma tag válida;
5. o log do dispositivo pode registrar leitura, autorização e acionamento, mas, sem sensor ou mecanismo adicional de identidade, não comprova abertura da porta, entrada, saída ou ocupação.

A alegação controlada recomendada é:

> Os registros do FLIKE permitem associar uma solicitação à conta autenticada que a submeteu e associar uma apresentação na tranca à credencial emitida para essa conta. Essa rastreabilidade não comprova que a pessoa física titular operou a sessão, apresentou o QR Code ou entrou no espaço.

Para sustentar irretratabilidade forte seriam necessários mecanismos que não fazem parte do protótipo, como assinatura assimétrica sob controle exclusivo do usuário, verificação mais forte de identidade, proteção contra compartilhamento e repetição da credencial, timestamps e logs invioláveis e evidência física adicional do evento alegado.

## 10. Aprovação do passo 5

Em 01/09/2026, a equipe aprovou integralmente:

1. as recomendações P1–P8;
2. os 14 requisitos funcionais, os quatro requisitos não funcionais e os quatro requisitos de acessibilidade propostos;
3. os estados iniciais como ponto de partida para a matriz de rastreabilidade;
4. a estrutura proposta para a reescrita incremental do Capítulo 4 no passo 6.

O passo 5 está concluído. Alterações posteriores deverão ser registradas como correções explícitas aos requisitos aprovados, preservando a rastreabilidade das decisões.
