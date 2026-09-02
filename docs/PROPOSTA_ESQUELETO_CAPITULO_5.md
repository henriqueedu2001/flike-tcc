# FLIKE — proposta de esqueleto do Capítulo 5

**Estado:** aprovado pela equipe em 01/09/2026

**Rodada:** Fase B, passo 8

**Data:** 01/09/2026

**Progresso global:** 10 de 26 passos concluídos (38,5%)

## 1. Função do capítulo

O Capítulo 5 será o núcleo técnico da monografia. Ele deverá explicar como o FLIKE foi projetado e implementado, conduzir o leitor da visão geral aos detalhes de cada subsistema e relacionar as decisões aos requisitos do Capítulo 4. A redação distinguirá código preservado, demonstrações confirmadas pela equipe, testes registrados e limitações.

O capítulo não deverá:

- repetir a lista de requisitos;
- apresentar tecnologias como um catálogo sem relação com decisões do projeto;
- misturar o produto FLIKE com seu antecedente histórico;
- transformar diagramas em uma galeria isolada;
- afirmar medições, testes com usuários ou propriedades de segurança que não foram avaliadas;
- tratar a ausência do GPIO, do código-fonte exato do ensaio ou dos modelos comerciais das fontes e do relé como impedimento para descrever o sistema.

O arquivo atual `FLIKE/capitulos/Cap5-Desenvolvimento.tex` contém texto provisório e diagramas obsoletos. Ele será substituído gradualmente somente depois da aprovação deste esqueleto.

## 2. Estrutura proposta

### 5.1 Visão geral do desenvolvimento

**Função:** abrir o capítulo com uma leitura única do sistema completo e explicar como o capítulo está organizado.

**Conteúdo:**

1. retomada breve do objetivo técnico, sem repetir a introdução;
2. apresentação dos quatro conjuntos principais: aplicação web, API e banco, credencial em QR Code e dispositivo físico;
3. distinção entre a etapa conectada de gestão e emissão e a etapa local de validação e abertura;
4. explicação das evidências usadas no capítulo: código, documentação, testes e relatos da equipe;
5. indicação de que os detalhes de tecnologias serão apresentados junto do subsistema em que são usados.

**Fontes:** Capítulo 4 aprovado, contrato acadêmico, inventário de evidências e repositórios finais.

**Limite:** não antecipar resultados de testes nem apresentar uma lista extensa de bibliotecas.

### 5.2 Arquitetura do FLIKE

#### 5.2.1 Componentes e responsabilidades

Apresentar frontend Next.js/React, API FastAPI, banco MySQL, QR Code, ESP32-CAM, câmera, circuito de acionamento e fechadura. Para cada componente, explicar responsabilidade, entradas, saídas e fronteira.

#### 5.2.2 Fronteira entre operação conectada e operação local

Explicar que cadastro, solicitação, aprovação e obtenção da credencial exigem acesso à aplicação e ao servidor. Depois que o QR Code está disponível, a decisão física é tomada pelo dispositivo sem consulta ao servidor.

#### 5.2.3 Decisões tecnológicas

Justificar as tecnologias somente no nível necessário para entender a implementação: Next.js/React na interface, FastAPI na API, MySQL na persistência, ESP32-CAM/OV2640 na aquisição óptica e AES-CMAC na autenticação. As características gerais que exigirem sustentação externa receberão referências primárias ou acadêmicas no próprio parágrafo.

**Fontes:** commits finais confirmados, arquivos de configuração, documentação oficial das tecnologias e referências já fichadas.

**Limite:** não reproduzir diagramas antigos que contenham Flutter, MQTT, gateway, Bluetooth, S3 ou PostgreSQL.

### 5.3 Aplicação conectada e persistência

#### 5.3.1 Modelo de domínio e dados

Explicar as entidades usuário, instituição, prédio, sala, tranca digital, solicitação e credencial. Mostrar que o papel administrativo decorre da propriedade da instituição e que o mesmo usuário pode administrar instituições próprias e solicitar acesso em instituições de terceiros.

#### 5.3.2 Backend

Descrever organização da API, autenticação JWT, autorização contextual, repositórios, rotas administrativas, solicitações, aprovação/rejeição e emissão. Diferenças relevantes entre intenção e código serão discutidas junto da operação afetada, sem transformar a seção em revisão linha a linha.

#### 5.3.3 Frontend

Descrever cadastro, login, dashboard, navegação hierárquica, solicitação, administração, consulta de pedidos e apresentação da credencial. O frontend oficial é a aplicação Next.js/React; as páginas HTML antigas não serão mencionadas.

#### 5.3.4 Fluxo de solicitação e emissão

Reunir os componentes anteriores em uma sequência: autenticação, escolha da tranca, criação do pedido, decisão do proprietário, emissão da credencial e disponibilização do QR Code. A política será uma credencial por solicitação, reutilizável durante a janela de validade.

**Fontes:** backend `e9268cc...`, frontend `9005601...`, DDL e relato da demonstração do fluxo completo.

**Limites:** não afirmar persistência offline ou download dedicado do QR Code; a correção para QR versão 3-L será vinculada ao commit futuro quando incorporada.

### 5.4 Credencial digital

Esta seção seguirá deliberadamente do conceito para a representação física dos bytes.

#### 5.4.1 Conceito e ciclo de vida

Explicar primeiro que a credencial é uma autorização temporária emitida após aprovação e destinada a uma tranca lógica. Distinguir credencial, solicitação, imagem do QR Code e segredo criptográfico.

#### 5.4.2 Informações autenticadas

Apresentar `user_id`, `digital_lock_id`, `issued_at` e `expires_at`, explicando o papel de cada campo na decisão local.

#### 5.4.3 Serialização e autenticação

Explicar a serialização big-endian, os 32 bytes de dados e a tag AES-CMAC de 16 bytes. A extensão total de 48 bytes aparecerá como consequência do formato, e não como decisão arbitrária. AES-CMAC será chamado de código de autenticação de mensagem com segredo simétrico, sem linguagem de assinatura assimétrica.

#### 5.4.4 Codificação em QR Code

Explicar a conversão do payload para modo binário e a escolha final de QR Code versão 3, nível L. A justificativa partirá da necessidade de reduzir a complexidade óptica para a câmera e da capacidade necessária para os 48 bytes.

#### 5.4.5 Decisão de aceitação

Organizar a ordem lógica: verificar leitura e comprimento, extrair campos, conferir a tranca destinatária, verificar `issued_at` e `expires_at`, recalcular o AES-CMAC e somente então autorizar o acionamento. Reapresentações são permitidas durante a janela; depois de `expires_at`, a credencial deve ser recusada.

**Fontes:** backend, frontend, firmware, NIST SP 800-38B, NIST SP 800-57 e referências de QR Code já fichadas.

**Limite:** o layout completo será explicado aqui, sem duplicá-lo integralmente nas seções de backend e firmware.

### 5.5 Dispositivo físico

#### 5.5.1 Plataforma embarcada e aquisição do QR Code

Apresentar ESP32-CAM, câmera OV2640, biblioteca de leitura e fluxo de aquisição e decodificação.

#### 5.5.2 Firmware de validação

Explicar processamento do payload, verificações estrutural, de destino, temporal e criptográfica e emissão do sinal `HIGH`. O texto distinguirá o código preservado no repositório do conjunto completo confirmado na demonstração final, sem exigir o código-fonte exato gravado no ensaio.

#### 5.5.3 Circuito de acionamento

Descrever funcionalmente ESP32-CAM, 2N2222, resistores, relé, fonte chaveada de 12 V, carregador de celular adaptado e fechadura elétrica. O projeto anterior será mencionado apenas como origem histórica da base elétrica reaproveitada.

#### 5.5.4 Demonstração física

Registrar categoricamente o ensaio ponta a ponta do FLIKE: leitura e decodificação do QR Code, verificações de comprimento, tranca, emissão e expiração, AES-CMAC, sinal `HIGH` e acionamento da fechadura.

**Fontes:** firmware preservado, inventário, material elétrico reaproveitado, ficha da fechadura e confirmação da equipe.

**Limites:** não afirmar sensores de porta, ocupação, entrada/saída, autonomia, MTTF, proteção elétrica de produto comercial ou adequação sensorial comprovada.

### 5.6 Operação local, segurança e auditoria

#### 5.6.1 Consequências da operação sem servidor

Explicar autonomia no instante da abertura, necessidade de relógio local coerente e impossibilidade de revogação imediata de uma credencial já emitida e ainda válida.

#### 5.6.2 Proteção do segredo e modelo de ameaça

Explicar o provisionamento prévio pelo fornecedor, o segredo compartilhado entre backend e tranca lógica, o risco de extração do segredo e a possibilidade de cópia do QR Code. Não prometer não repúdio criptográfico.

#### 5.6.3 Eventos e limites da auditoria

Separar leitura, autorização, acionamento, abertura física e passagem de pessoa. Esclarecer que, sem sensores adicionais, o FLIKE não comprova entrada, saída ou ocupação. A irretratabilidade será discutida apenas como propriedade sistêmica condicionada à proteção das contas, do segredo e dos registros, não como propriedade isolada do AES-CMAC.

**Fontes:** NIST, requisitos aprovados, código e decisões da equipe.

### 5.7 Verificação técnica e resultados

#### 5.7.1 Estratégia e ambiente

Definir versões, comandos, dados sintéticos, critérios e diferença entre inspeção, teste executado e demonstração relatada.

#### 5.7.2 Verificações dos subsistemas

Organizar resultados de compilação quando viável, protocolo, autorização web, validade, reutilização e tempo de leitura caso seja possível medi-lo. Casos não executados serão marcados como não avaliados.

#### 5.7.3 Fluxo integrado

Relacionar a demonstração completa do software e a demonstração física final aos requisitos correspondentes. A ausência de vídeo ou log novo não será apresentada como falha do produto.

#### 5.7.4 Rastreabilidade dos resultados

Apresentar quadro `requisito → evidência → resultado → observação`, usando os identificadores do Capítulo 4.

**Fontes:** artefatos produzidos nos passos 13 a 15, inventário de evidências e matriz do Capítulo 4.

**Limite:** esta seção será redigida depois da definição e execução dos testes possíveis; nenhum resultado será antecipado.

### 5.8 Limitações da implementação

Consolidar somente limitações materiais para interpretar os resultados: ausência de avaliação com usuários, revogação offline, provisionamento manual, ausência de sensores, segurança física não endurecida, divergência entre o firmware preservado e a versão demonstrada e funções de interface ainda incompletas. Cada limitação deverá indicar sua consequência, evitando uma lista genérica de trabalhos futuros.

O encerramento retomará a integração obtida e preparará a passagem para as considerações finais, sem repetir o Capítulo 6.

## 3. Distribuição pelas próximas rodadas

| Passo | Conteúdo do Capítulo 5 |
| --- | --- |
| 9 | Seções 5.1, 5.2 e 5.3.1: visão geral, arquitetura e modelo de dados |
| 10 | Seções 5.3.2 a 5.3.4: backend, frontend e fluxo conectado |
| 11 | Seções 5.4 e 5.6: credencial, operação local, segurança e auditoria |
| 12 | Seção 5.5: firmware, circuito e demonstração física |
| 13 | Planejamento da Seção 5.7 e dos testes possíveis |
| 14 | Execução e registro dos testes aprovados |
| 15 | Redação da Seção 5.7 com os resultados obtidos |
| 16 | Seção 5.8, revisão das transições e consolidação integral do capítulo |

Cada passo continuará dividido em blocos curtos. Toda referência a um bloco virá acompanhada de seu conteúdo e dos números das seções que deverão ser revisadas.

## 4. Propostas individuais de figuras

As seis figuras foram autorizadas pela equipe em 01/09/2026. Cada uma será produzida ou inserida somente na rodada da seção correspondente:

| Código | Figura proposta | Função | Material disponível | Recomendação |
| --- | --- | --- | --- | --- |
| **F5-01** | Arquitetura geral do FLIKE | Mostrar aplicação conectada, emissão do QR e validação local, sem tecnologias abandonadas | Diagramas antigos e arquitetura consolidada | **Aprovada** para a Seção 5.2 |
| **F5-02** | Modelo entidade-relacionamento fiel ao banco | Explicar propriedade contextual e relações entre solicitação, credencial e tranca | DBML antigo e DDL efetivo do backend | **Aprovada** para a Seção 5.3.1 |
| **F5-03** | Sequência de solicitação, aprovação e emissão | Tornar explícitas as chamadas entre usuário, frontend, API e banco | Código dos commits finais | **Aprovada**, condicionada à utilidade durante a redação da Seção 5.3.4 |
| **F5-04** | Fluxo local de validação da credencial | Mostrar separadamente leitura, validações e sinal `HIGH` | Protocolo e relato da demonstração | **Aprovada** para a Seção 5.4.5 ou 5.5.2 |
| **F5-05** | Esquema elétrico redesenhado | Explicar o estágio com 2N2222, relé, duas alimentações e fechadura | Diagrama e fotografias existentes | **Aprovada** para a Seção 5.5.3 |
| **F5-06** | Fotografia do protótipo | Mostrar a natureza de bancada da montagem | Fotografia original existente | **Aprovada**, com legenda de protótipo experimental |

O layout binário da credencial será um **quadro textual**, não uma figura. A matriz requisito–resultado também será um quadro. Eles não dependem de ativo gráfico externo.

## 5. Portão de saída do passo 8

O esqueleto, a distribuição dos passos 9 a 16 e as figuras F5-01 a F5-06 foram aprovados pela equipe em 01/09/2026. O antecedente histórico receberá somente uma menção breve na Seção 5.5.3 como origem da base elétrica, sem discussão de seu protocolo. O passo 8 está concluído.

O passo 9 começou pela proposta do bloco que abrange as Seções 5.1, 5.2 e 5.3.1. A tese será alterada depois da validação dessa proposta.
