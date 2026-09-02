# FLIKE — proposta do bloco 1 do Capítulo 5

**Estado:** implementado e aprovado pela equipe em 01/09/2026

**Rodada:** Fase C, passo 9, bloco 1

**Conteúdo do bloco:** Seções 5.1, 5.2, 5.2.1–5.2.3 e 5.3.1 — visão geral, arquitetura e modelo de dados

**Data:** 01/09/2026

**Progresso global:** 10 de 26 passos concluídos (38,5%)

**Resultado:** conteúdo incorporado a `FLIKE/capitulos/Cap5-Desenvolvimento.tex`, compilado e aprovado no PDF da tese. As figuras F5-01 e F5-02 foram produzidas em SVG e PDF e integradas ao capítulo.

## 1. Objetivo da rodada

Este bloco substituirá a abertura provisória do Capítulo 5 por uma explicação que conduza o leitor do sistema completo ao modelo de dados. Ele estabelecerá a linguagem arquitetural usada no restante do capítulo e evitará que frontend, backend, credencial e dispositivo físico pareçam projetos independentes.

A redação será acompanhada pelas figuras F5-01 e F5-02, já autorizadas pela equipe no passo 8:

- **F5-01 — arquitetura geral do FLIKE:** fronteira conectada, transporte da credencial e decisão física local;
- **F5-02 — modelo entidade-relacionamento:** tabelas e relações efetivamente criadas pelo backend.

O bloco não descreverá em profundidade endpoints, páginas, layout binário ou firmware. Esses assuntos serão desenvolvidos nas Seções 5.3.2 em diante.

## 2. Modificação prevista no arquivo da tese

O conteúdo atual de `FLIKE/capitulos/Cap5-Desenvolvimento.tex` será removido gradualmente. Neste bloco serão eliminados:

- o parágrafo que ainda chama o sistema pelo nome descontinuado;
- a lista promocional e genérica de tecnologias;
- referências a HMI com LEDs e botões não sustentadas pela solução final;
- afirmações genéricas de segurança e eficiência;
- a seção isolada “Diagramas de arquitetura” e suas quatro figuras obsoletas.

O arquivo passará a começar pelas Seções 5.1, 5.2 e 5.3.1 propostas abaixo. As demais seções aprovadas no esqueleto poderão permanecer apenas com seus títulos estruturais ou ser acrescentadas nas rodadas correspondentes; não serão preenchidas com texto provisório.

## 3. Seção 5.1 — Visão geral do desenvolvimento

### 3.1 Sequência argumentativa

A seção terá aproximadamente quatro parágrafos:

1. apresentará o FLIKE como sistema integrado de gestão e controle de acesso físico;
2. explicará os quatro conjuntos da solução: aplicação web, API/banco, credencial visual e dispositivo físico;
3. distinguirá a etapa conectada, que vai da autenticação à obtenção do QR Code, da etapa local, que vai da leitura à atuação da fechadura;
4. explicará que o capítulo combina código preservado, documentação e demonstrações confirmadas pela equipe, remetendo testes e resultados à Seção 5.7.

### 3.2 Afirmações controladas

O texto poderá afirmar que os componentes foram implementados e que houve demonstrações do fluxo web e da integração física. Ele não dirá, nesta abertura, que todos os requisitos foram atendidos, que o sistema está pronto para produção ou que benefícios ao público-alvo foram medidos.

Não haverá figura própria na Seção 5.1. A arquitetura F5-01 aparecerá depois de ser introduzida na Seção 5.2.

## 4. Seção 5.2 — Arquitetura do FLIKE

### 4.1 Seção 5.2.1 — Componentes e responsabilidades

A explicação seguirá o caminho da credencial:

1. a pessoa usa o frontend Next.js/React;
2. o frontend envia e recebe dados da API FastAPI;
3. a API aplica regras e acessa o MySQL;
4. depois da aprovação, a API devolve o payload da credencial;
5. o frontend converte o hexadecimal recebido em bytes e renderiza o QR Code localmente;
6. a ESP32-CAM lê o símbolo e toma a decisão de autorização;
7. o sinal `HIGH` comanda o circuito e a fechadura.

Um quadro textual resumirá cada componente, sua responsabilidade e seu principal limite. O quadro evitará repetir os detalhes das seções posteriores.

#### Especificação da figura F5-01

A figura será redesenhada do zero e não reaproveitará visualmente os diagramas obsoletos. Ela conterá:

- uma pessoa com os papéis contextuais de solicitante e proprietário de instituição;
- navegador com frontend Next.js/React;
- API FastAPI;
- banco MySQL;
- credencial em QR Code apresentada pelo navegador ou por imagem previamente obtida;
- ESP32-CAM com câmera;
- circuito com transistor e relé;
- fechadura elétrica.

As ligações serão rotuladas:

- pessoa ↔ frontend: interação web;
- frontend ↔ API: HTTP/JSON;
- API ↔ MySQL: consultas e persistência SQL;
- API → frontend: payload binário representado em hexadecimal no JSON;
- frontend → QR Code: conversão para bytes e renderização local;
- QR Code → ESP32-CAM: canal óptico;
- ESP32-CAM → circuito: sinal lógico `HIGH`;
- circuito → fechadura: acionamento elétrico.

A fronteira visual separará **gestão conectada** de **validação e acionamento locais**. O desenho não conterá Flutter, MQTT, gateway, Bluetooth, S3, PostgreSQL, serviços externos ou um ator administrador global.

### 4.2 Seção 5.2.2 — Fronteira entre operação conectada e operação local

Esta subseção impedirá a interpretação errada de “offline”. Ela explicará que o usuário precisa de conectividade para cadastrar-se, autenticar-se, solicitar acesso, acompanhar a decisão e recuperar o QR Code. A tranca, por outro lado, não consulta a API quando recebe a credencial: usa dados, relógio e segredo disponíveis localmente.

O texto apresentará essa divisão como decisão arquitetural. As consequências de revogação, cópia e proteção do segredo serão apenas anunciadas e remetidas à Seção 5.6, evitando interromper a descrição da arquitetura com uma discussão de segurança extensa.

### 4.3 Seção 5.2.3 — Decisões tecnológicas

A subseção explicará por que cada tecnologia ocupa sua função, sem afirmar que ela é universalmente superior:

- **Next.js/React:** interface web organizada pelo App Router e componentes React;
- **FastAPI/Pydantic:** API em Python com modelos tipados para entradas e saídas;
- **MySQL:** persistência relacional das contas, estrutura institucional, solicitações, trancas e credenciais;
- **ESP32-CAM/OV2640:** aquisição visual e execução local do firmware;
- **QR Code e AES-CMAC:** transporte visual compacto e autenticação local do payload.

O uso concreto dessas tecnologias será sustentado pelos repositórios. Características gerais receberão citações de documentação oficial no próprio texto. Para esta seção foram selecionadas as documentações oficiais do App Router do Next.js, das funcionalidades do FastAPI e do manual do MySQL; as entradas BibTeX serão verificadas e acrescentadas durante a implementação.

Versões de dependências poderão aparecer em quadro ou nota somente quando forem relevantes para reproduzir o ambiente. Não será produzida uma lista integral de pacotes.

## 5. Seção 5.3.1 — Modelo de domínio e dados

### 5.1 Fonte de verdade

O diagrama será derivado de `scripts/create_db.py` no commit final `e9268cc...`, e não de `docs/database.dbml`. Esse script contém a **Linguagem de Definição de Dados** (DDL, do inglês *Data Definition Language*): os comandos SQL que criam tabelas, colunas, tipos, chaves primárias e chaves estrangeiras. O DBML está desatualizado: omite `digital_key_request`, registra campos antigos de `digital_key` e não representa todas as decisões dos comandos efetivamente usados para criar o banco.

### 5.2 Entidades e relações

A subseção explicará nove tabelas:

| Tabela | Papel no sistema |
| --- | --- |
| `auth` | credenciais de autenticação armazenadas como e-mail e senha transformados, além do sal |
| `user` | identidade lógica usada pelo domínio |
| `institution` | instituição pertencente a um usuário por `owner_id` |
| `building` | prédio pertencente a uma instituição |
| `room` | sala pertencente a um prédio |
| `digital_lock` | tranca lógica pertencente a uma sala e detentora do segredo |
| `digital_key_request` | solicitação de um usuário para uma tranca, com estado |
| `digital_key` | credencial emitida para um usuário e uma tranca |
| `event_log` | estrutura prevista para eventos associados à tranca |

As relações explícitas serão apresentadas com suas cardinalidades `1:N`: usuário–instituição, instituição–prédio, prédio–sala, sala–tranca, usuário–solicitação, tranca–solicitação, usuário–credencial, tranca–credencial e tranca–evento.

Duas ausências serão explicadas porque afetam a interpretação:

1. `auth` não possui chave estrangeira para `user`; a associação é tratada pela lógica de aplicação, não pelo esquema relacional;
2. `digital_key_request` não possui chave estrangeira para a `digital_key` gerada na aprovação.

O texto não criará classes separadas para cliente e administrador. `institution.owner_id` será apresentado como a relação que torna um usuário responsável por uma instituição.

#### Especificação da figura F5-02

O novo diagrama entidade-relacionamento mostrará:

- as nove tabelas do DDL efetivo;
- chaves primárias e estrangeiras;
- campos suficientes para compreender o domínio, omitindo detalhes repetitivos apenas se a legibilidade exigir;
- cardinalidades das relações declaradas no banco;
- uma ligação tracejada e rotulada entre `auth` e `user`, caso seja necessário representar a associação lógica, deixando explícito que não se trata de chave estrangeira;
- ausência de relação direta entre solicitação e credencial, sem inventar uma associação inexistente.

O diagrama antigo `relacionamentos.drawio.png` será removido do capítulo e não será usado como base factual.

## 6. Fontes planejadas

| Afirmação | Fonte principal |
| --- | --- |
| Componentes e contratos do FLIKE | commits finais dos três repositórios e inventário do passo 7 |
| Organização do frontend pelo diretório `app/` | commit `9005601...` e documentação oficial do Next.js |
| Modelos tipados e organização da API | commit `e9268cc...` e documentação oficial do FastAPI |
| Persistência relacional e tipos SQL | DDL do backend e manual oficial do MySQL |
| Fronteira conectada/local | requisitos e decisões arquiteturais aprovados no Capítulo 4 |
| Tabelas, campos e relações | `scripts/create_db.py` no commit `e9268cc...` |
| Integração física completa | confirmação da equipe consolidada no inventário de evidências |

O código do próprio projeto sustentará afirmações sobre o que foi implementado. Documentação externa sustentará somente conceitos e características gerais das tecnologias; ela não será usada como evidência de que o FLIKE funciona.

## 7. Resultado esperado

Depois da implementação, o leitor deverá conseguir responder:

1. quais componentes formam o FLIKE;
2. quais operações dependem do servidor;
3. o que ocorre localmente no instante da abertura;
4. como as entidades institucionais, solicitações, credenciais e trancas se relacionam;
5. por que o mesmo usuário pode ser responsável em um contexto e solicitante em outro.

O bloco deverá encerrar preparando a descrição detalhada do backend e do frontend na Seção 5.3.2.

## 8. Portão de saída

Antes de alterar a tese, a equipe deve validar:

1. a sequência das Seções 5.1, 5.2.1–5.2.3 e 5.3.1;
2. a composição e a fronteira conectado/local da figura F5-01;
3. o uso dos comandos SQL efetivos de criação do banco, com nove tabelas, na figura F5-02;
4. a apresentação explícita das duas ausências do esquema: `auth` sem FK para `user` e solicitação sem FK para credencial;
5. a remoção imediata dos quatro diagramas obsoletos do Capítulo 5;
6. a inclusão de referências oficiais para as características gerais de Next.js, FastAPI e MySQL.

As seis decisões foram aprovadas pela equipe em 01/09/2026. O bloco 1 está autorizado para redação, criação das duas figuras, compilação e inspeção do PDF.
