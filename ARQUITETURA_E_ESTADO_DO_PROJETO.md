# FLIKE / CAUSP-LOCK — arquitetura e estado do projeto

Documento de trabalho para orientar a redação do TCC e receber correções da equipe. Levantamento realizado em 30–31/08/2026, a partir do PDF, dos fontes LaTeX, dos diagramas e das versões locais dos repositórios. **Não é uma declaração de homologação, segurança ou conclusão do sistema.**

## 1. Como interpretar este levantamento

O projeto propõe controle de acesso físico com credenciais em QR Code, emissão centralizada e validação criptográfica local no ESP32-CAM. Há implementação de backend, aplicação web em Next.js/React e firmware de leitura/verificação de QR. Entretanto, as versões disponíveis não permitem afirmar que todo o percurso até a abertura física, uso único, expiração e auditoria esteja integrado e validado.

A distinção entre versões é essencial: a branch aberta do frontend contém um protótipo HTML antigo; a aplicação React está na referência local `origin/frontend_prototype`. Ela foi lida diretamente do Git, sem checkout. O backend aberto está em `massive-vibe-code-session`, e não em `main`. O firmware possui mudanças locais ainda não commitadas. Portanto, “o código do projeto” não corresponde simplesmente às quatro branches `main`.

As afirmações usam estas categorias:

- **Implementado no código:** existe lógica concreta nos arquivos examinados. Não significa execução bem-sucedida em ambiente real.
- **Parcial:** há componentes, mas faltam integração, controles ou evidência de funcionamento completo.
- **Previsto:** aparece na tese, nos diagramas ou em documentação de intenção, sem implementação correspondente localizada.
- **Não confirmado:** depende de montagem física, ambiente, versões não disponíveis, decisões da equipe ou ensaios não registrados.
- **Divergência:** duas fontes disponíveis descrevem comportamentos diferentes.

Não foram alterados frontend, backend ou firmware; não foram executados scripts de banco, servidores, deploys, instalação de dependências, gravação de placa ou atualização de referências remotas. Não foram consultados dados reais de usuários nem arquivos de credenciais. O levantamento não confirma o estado atual do GitHub: `origin/...` designa a referência já existente localmente.

### 1.1 Versões examinadas

| Repositório / fonte | Referência | Commit / estado |
| --- | --- | --- |
| Backend principal desta análise | `massive-vibe-code-session` | `6f9efd40f019efd659fcb5f4f382f775300cacdd`, commit de 28/07/2026 |
| Backend anterior, consultado para comparação | `main` / referência `origin/main` | `ae703ad4b4af9ac207f523df63cf87510899239b` na referência remota local; API mais antiga |
| Frontend HTML | `main` | `844a30cc98b74e49678e39c49f745c283be8aac0`, 08/04/2026 |
| Frontend Next.js, principal desta análise | `origin/frontend_prototype` | `9005601719e98b5cac1c3586d07ef79b06a28a00`, 20/08/2026 |
| Firmware | `main` + arquivos locais | `c2983f4ce6e02fd4ce68c212a54e8c5fd6ef1e78`, 09/03/2026, com mudanças descritas abaixo |
| TCC | `main` | `ae922115f778c18a81b581697026d122a94adab4`, 30/08/2026 |
| PDF recebido | arquivo local ainda não rastreado | `TCC___CAUSP_LOCK-1.pdf`, 45 páginas; metadados de criação em 30/08/2026, 22:35:27, UTC−03 |

Alterações já existentes antes deste trabalho: backend `scripts/run_server.sh` modificado; firmware `src/digital_key.cpp` e `src/digital_key.h` modificados, além de `sdkconfig.defaults`, `src/digital_lock.cpp` e `src/digital_lock.h` não rastreados. O PDF também já estava não rastreado. Esses arquivos foram preservados.

### 1.2 Convenção de evidências

Nas referências abaixo, **B** significa backend na versão principal acima; **F** significa frontend **no commit Next.js**, não o diretório HTML aberto; **W** significa firmware com as mudanças locais; **T** significa TCC. A seção 15 relaciona caminhos e símbolos para localizar cada evidência. Para F, a consulta reproduzível é `git show 9005601719e98b5cac1c3586d07ef79b06a28a00:caminho/do/arquivo`, executada no repositório do frontend.

## 2. Problema, contexto e fronteira do sistema

A tese tem o título **“Desenvolvimento e implementação de um sistema de controle de acesso a espaços públicos acessível a neurodivergentes”**. Os autores são Hélcio Prado de Lima, Henrique Eduardo dos Santos de Souza e Mateus Kosicov Perugini; o orientador é o Prof. Dr. Reginaldo Arakaki, no Departamento de Engenharia de Computação e Sistemas Digitais da Escola Politécnica da USP. [T01]

O cenário descrito é a sala de apoio à amamentação e regulação sensorial da Faculdade de Direito da USP, no prédio histórico do Largo de São Francisco. O problema apresentado é a dependência de retirada manual de chaves com funcionários, associada a constrangimento, barreiras sociais e cognitivas, subutilização e dificuldades de controle. Isso é o **contexto relatado pela equipe na tese**, não resultado de pesquisa de campo realizada neste levantamento. [T01, cap. 1]

O objetivo é proporcionar autonomia a usuários autorizados e reduzir interações obrigatórias para entrar no espaço, mantendo controle e rastreabilidade. A aprovação administrativa continua existindo no fluxo implementado; a proposta não elimina toda intervenção humana na concessão de acesso. O cadastro não comprova por si só vínculo com a USP nem pertencimento ao público-alvo.

**Nomenclatura:** CAUSP-LOCK aparece na tese e no HTML; FLIKE aparece nos repositórios e na interface Next.js. O resumo explica CAUSP como referência ao Coletivo Autista da USP. Não foi encontrada explicação inequívoca da sigla FLIKE nem decisão formal de renomeação; a equipe deve fixar a terminologia final.

Embora o caso de uso seja uma sala específica, o modelo implementado suporta múltiplas instituições, prédios, salas e fechaduras. Isso é capacidade estrutural do modelo, não evidência de implantação em vários locais.

### 2.1 Atores e conceitos

| Conceito | Significado no projeto |
| --- | --- |
| Usuário | Pessoa cadastrada, identificada por `user.id`, nome e e-mail |
| Responsável / administrador | Usuário que é `owner_id` de uma instituição; seus poderes decorrem dessa propriedade |
| Instituição | Agrupamento de prédios administrado por um usuário |
| Prédio | Unidade com endereço vinculada a uma instituição |
| Sala | Espaço físico, com nome e número, vinculado a um prédio |
| Tranca física | Conjunto embarcado, câmera, interface e mecanismo elétrico proposto |
| Tranca elétrica | Atuador que efetivamente impede ou permite a abertura |
| Tranca digital | Registro `digital_lock`, associado a uma sala e a um segredo criptográfico |
| Chave digital de acesso | Credencial binária emitida para um usuário e uma tranca digital |
| Chave secreta criptográfica | Segredo simétrico de 32 bytes usado para gerar e verificar o CMAC; não é a credencial entregue ao usuário |
| Solicitação | Pedido de uma chave, com estado `pending`, `approved` ou `rejected` |

O banco não tem classes/tabelas separadas de cliente e administrador nem campo de papel em `user`. Uma pessoa pode possuir instituições e também receber chaves. Não há evidência de um superadministrador global ou de múltiplos administradores associados à mesma instituição. [B02, B03, B04]

## 3. Visão arquitetural

### 3.1 Componentes e responsabilidades

| Componente | Responsabilidade encontrada | Limites da evidência |
| --- | --- | --- |
| Frontend Next.js/React | Cadastro/login, navegação, solicitações, administração, consultas e renderização do QR | Há incompatibilidades de contrato e páginas incompletas |
| API FastAPI | Identidade, recursos físicos lógicos, propriedade administrativa, emissão de credenciais e registro de uso no banco | Nem todas as rotas exigem autenticação; não há integração embarcada localizada |
| MySQL | Persistência relacional de contas, infraestrutura, segredos, chaves e solicitações | DDL examinado; banco em execução não inspecionado |
| Firmware Arduino/C++ | Aquisição de QR e cálculo/comparação de AES-CMAC via mbedTLS | Validador parcial; árvore local tem incompatibilidade de chamada |
| ESP32-CAM / câmera | Plataforma alvo e aquisição óptica | Modelo AI-Thinker no código; OV2640 declarada na tese; montagem não inspecionada |
| Fechadura elétrica / energia / HMI | Abertura física, continuidade elétrica e feedback pretendidos | Sem circuito ou lógica completa de atuação encontrados |

```mermaid
flowchart LR
    U[Usuário ou responsável] --> F[Frontend Next.js / React]
    F <-->|HTTP + JSON| B[API FastAPI]
    B <-->|SQL pelo mysql.connector| D[(MySQL)]
    B -->|Credencial de 48 bytes em hexadecimal JSON| F
    F -->|QR em modo byte gerado no navegador| Q[QR Code]
    Q -->|Captura óptica prevista na integração| W[ESP32-CAM: leitura e CMAC]
    W --> S[Resultado no monitor serial]
    W -.->|Atuação não localizada| E[Fechadura elétrica]
    W -.->|Sincronização não localizada| B
```

As ligações com API e banco são implementadas nos fontes. O diagrama não afirma que a combinação dessas versões executou de ponta a ponta. O percurso óptico tem emissor e leitor implementados separadamente, mas não foi ensaiado neste levantamento. [B01–B08, F01–F08, W01–W03]

### 3.2 O que “offline” significa aqui

A proposta permite que o dispositivo confira uma credencial sem consultar o servidor no instante da leitura, desde que já possua o segredo correto. A função de CMAC do firmware não usa rede.

Isso não demonstra operação completa da tranca offline: ainda são necessários decisão de autorização, checagem temporal, proteção contra repetição e acionamento físico. Também não significa que emissão, solicitação e gestão web funcionem sem internet. O frontend consulta a API para recuperar o payload ao abrir o QR; não foi localizado service worker ou armazenamento persistente de credenciais para uso offline. Depois de renderizado, o QR é uma imagem local no navegador; a persistência após recarga não está implementada como funcionalidade dedicada.

Uma tranca sem contato com o servidor não toma conhecimento imediato de revogações ou mudanças administrativas. A arquitetura final precisa explicitar como distribui segredos, mantém horário confiável, preserva o conjunto de credenciais consumidas e reconcilia eventos. Esses mecanismos não devem ser inferidos apenas da palavra “offline”.

## 4. Backend

### 4.1 Organização e tecnologias

O backend é uma aplicação FastAPI com routers por domínio. Os endpoints chamam repositórios em `app/database/repositories.py`, que executam SQL diretamente por `mysql.connector`. Os modelos Pydantic descrevem entradas e algumas respostas. Os módulos de autenticação, CMAC e conversão binária são utilizados pelas rotas e repositórios. Não há ORM encontrado nem uma camada ampla de serviços intermediando os casos de uso: `app/services/env.py` concentra configuração de ambiente. [B01–B09]

`docs/project_structure.md` contém exemplos genéricos de predição/ML e uma estrutura idealizada; não descreve fielmente os módulos efetivos. Não há razão para apresentar aprendizado de máquina como parte deste projeto.

Versões declaradas em `requirements.txt`: FastAPI `0.133.1`, Pydantic `2.12.5`, Uvicorn `0.41.0`, `mysql-connector-python` `9.7.0`, `cryptography` `46.0.5`, PyJWT `2.13.0` e `python-dotenv` `1.2.1`. `segno` `1.6.6` está declarado, mas não foi localizado uso na aplicação ativa para renderizar QR. Dependência listada não é prova de funcionalidade utilizada.

### 4.2 Configuração e banco

As variáveis esperadas são `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_DATABASE`, `DB_PORT` e `JWT_SECRET`; são lidas por `python-dotenv`/`os.getenv`. O pool MySQL é global, criado na importação, com 16 conexões e `pool_reset_session=True`. A classe `Database` obtém conexão do pool e cursor com resultados em dicionários. [B09]

A dependência `get_database()` fornece a conexão por requisição, executa rollback em exceções e fecha cursor/conexão ao final. Os repositórios realizam commits explícitos. Isso dá transações a operações individuais, mas não garante atomicidade de um caso de uso que invoque vários métodos com commits separados.

O script local `scripts/run_server.sh` inicia Uvicorn em `0.0.0.0:8000` com `--reload`. É configuração de desenvolvimento, não evidência de implantação de produção. CORS admite `http://localhost:3000` e `http://127.0.0.1:3000`, permite credenciais e todos os métodos/headers. Não foram encontrados configuração de TLS, proxy reverso, domínio, containers ou infraestrutura de nuvem nos arquivos examinados. [B01, B09]

### 4.3 Identidade e sessão

1. `POST /user/new` cadastra nome/e-mail e cria credenciais.
2. `user` armazena e-mail legível; `auth` armazena SHA-256 do e-mail, salt e SHA-256 de `salt + password`.
3. O salt é gerado com `secrets.token_hex(16)`, isto é, 16 bytes aleatórios representados por 32 caracteres hexadecimais.
4. `POST /auth/user` verifica as credenciais e retorna JSON com campo **`token`**.
5. O JWT usa HS256, contém `user_id` e expira em uma hora. O segredo de JWT é configuração distinta do segredo AES de cada tranca.
6. As rotas protegidas recebem `Authorization: Bearer ...`; `verify_token()` verifica assinatura e expiração.
7. Perfil próprio pode ser consultado/alterado, e a troca de senha exige a senha atual. A mudança de e-mail atualiza o hash correspondente em `auth`.

Não foram localizados login federado USP, verificação de e-mail, restrição efetiva a `@usp.br`, autenticação multifator, recuperação de senha, refresh token ou revogação de sessões. O uso de SHA-256 com salt é o comportamento observado; não equivale a um esquema de derivação de senha com custo adaptativo. A troca de senha reutiliza o salt e não invalida explicitamente JWTs emitidos. [B06]

### 4.4 Autorização administrativa

O router `/admin` exige token. Para operações nos recursos, o backend percorre a hierarquia até `institution.owner_id` e o compara com `user_id` do token. As listagens administrativas retornam recursos das instituições do usuário. Ao mover prédio, sala ou tranca, também verifica a propriedade do destino. Exclusões impedidas por referências no banco são traduzidas em conflito HTTP 409. [B03, B04]

Qualquer usuário autenticado pode criar uma instituição e tornar-se seu responsável. Não existe verificação adicional de uma função global de administrador no código examinado. O menu da interface também apresenta entradas administrativas sem derivar um papel global. Isso pode ser uma decisão do modelo de produto, mas não deve ser descrito como cadastro institucional previamente homologado.

Essa proteção não cobre toda a API: continuam registradas rotas públicas de criação de trancas e emissão direta de chaves. Portanto, a política de propriedade implementada em `/admin` não constitui, por si só, uma barreira completa de autorização. A seção 11 detalha a consequência.

### 4.5 Inventário de endpoints registrados

“Público” significa que não foi encontrada dependência de autenticação na rota nem globalmente em `app/main.py`; não afirma como um eventual proxy externo estaria configurado.

| Método e caminho | Função | Controle no código |
| --- | --- | --- |
| `POST /` | Resposta de saudação para verificação básica | Público; não testa banco/câmera |
| `POST /auth/user` | Login | Credenciais no corpo |
| `POST /auth/token` | Validação de JWT fornecido no parâmetro `jwt_token` | Público |
| `GET /auth/request` | Demonstração de rota protegida | Bearer |
| `POST /user/new` | Cadastro | Público |
| `GET /user/all`, `GET /user?id=...` | Listagem e consulta de usuários | Público |
| `GET /user/me`, `PUT /user/me` | Perfil próprio | Bearer |
| `POST /user/change-password` | Troca de senha | Bearer + senha atual |
| `GET /institution/all`, `/building/all`, `/room/all` | Catálogo global | Público |
| `GET /institutions/search?q=...` | Busca textual de instituições | Público |
| `GET /buildings/search?q=...&institution_id=...` | Busca de prédios, filtro institucional opcional | Público |
| `GET /rooms/search?q=...&building_id=...` | Busca por nome/número de sala, filtro de prédio opcional | Público |
| `GET /digital_lock/all`, `GET /digital_lock?room_id=...` | Consulta de trancas, incluindo segredo serializado | Público |
| `POST /digital_lock/new` | Cria tranca e segredo | Público |
| `GET /digital_key/all` | Lista credenciais | Público |
| `GET /digital_key?id=...` | Lista credenciais do usuário informado | Público; `id` é ID do usuário |
| `GET /digital_key?key_id=...` | Recupera uma credencial | Público; `key_id` tem precedência se ambos presentes |
| `POST /digital_key/new` | Emissão direta com usuário, tranca e expiração | Público |
| `POST /digital_key/use` | Confere payload e marca uso no banco | Público |
| `POST /digital_key/request` | Solicita chave para `lock_id` | Bearer; usuário obtido do token |
| `GET`, `POST /admin/institutions` | Lista instituições próprias / cria instituição | Bearer |
| `PUT`, `DELETE /admin/institutions/{id}` | Edita/exclui instituição | Bearer + proprietário |
| `GET`, `POST /admin/buildings` | Lista/cria prédios | Bearer + escopo/propriedade |
| `PUT`, `DELETE /admin/buildings/{id}` | Edita/exclui prédio | Bearer + proprietário |
| `GET`, `POST /admin/rooms` | Lista/cria salas | Bearer + escopo/propriedade |
| `PUT`, `DELETE /admin/rooms/{id}` | Edita/exclui sala | Bearer + proprietário |
| `GET`, `POST /admin/locks` | Lista/cria trancas | Bearer + escopo/propriedade |
| `PUT`, `DELETE /admin/locks/{id}` | Edita/exclui tranca | Bearer + proprietário |
| `GET /admin/rooms/{id}/key-holders` | Portadores de chaves da sala | Bearer + proprietário |
| `GET /admin/key-holders` | Portadores de chaves das instituições próprias | Bearer + escopo |
| `GET /admin/key-holders/{id}/history` | Histórico de chaves de um usuário nessas instituições | Bearer + escopo |
| `POST /admin/keys/issue` | Emite chave para usuário/tranca | Bearer + proprietário da instituição da tranca |
| `GET /admin/keys/requests` | Lista solicitações, com filtro opcional `status` | Bearer + escopo |
| `POST /admin/keys/requests/{id}/approve` | Aprova pedido pendente e emite chave | Bearer + proprietário |
| `POST /admin/keys/requests/{id}/reject` | Rejeita pedido pendente | Bearer + proprietário |

`event_log.py` está vazio; não há router de eventos incluído. O router auxiliar de conversão binária existe em arquivo, mas não é registrado em `app/main.py`. Não foi localizada rota `GET /digital_key/requests`, apesar de o frontend mais recente solicitá-la. [B01, B04–B07, F04]

## 5. Modelo de dados

O esquema abaixo foi reconstruído de `scripts/create_db.py`, não dos diagramas antigos. O script cria tabelas `IF NOT EXISTS`; não oferece migração de uma tabela já existente para uma definição nova. Não foi verificado o esquema de um banco real. [B02]

| Tabela | Campos centrais | Relações e observações |
| --- | --- | --- |
| `auth` | `id`, `hashed_email`, `hashed_password`, `salt` | `hashed_email` é único; não há FK direta para `user` |
| `user` | `id`, `name`, `email`, `created_at` | E-mail não tem `UNIQUE` no DDL; duplicidade é checada no fluxo de cadastro e em `auth` |
| `institution` | `id`, `owner_id`, `name`, `created_at` | FK para usuário responsável; `owner_id` não é único |
| `building` | `id`, `institution_id`, `name`, endereço, `created_at` | Endereço: duas linhas, cidade, estado, CEP e país |
| `room` | `id`, `building_id`, `name`, `number`, `created_at` | FK para prédio |
| `digital_lock` | `id`, `room_id`, `secret_key BINARY(32)`, `created_at` | Uma sala pode ter várias trancas; não há unicidade de `room_id` |
| `digital_key` | `id`, `user_id`, `digital_lock_id`, `payload BINARY(48)`, `expires_at`, `used`, `used_at`, `created_at` | `used` começa falso; expiração e instante de uso podem ser nulos no DDL |
| `digital_key_request` | `id`, `user_id`, `digital_lock_id`, `status`, `created_at` | `status` é texto, default `pending`; não há FK para chave emitida nem aprovador registrado |
| `event_log` | `id`, `digital_lock_id`, `type`, `log`, `created_at` | Estrutura prevista para eventos; sem gravação/consulta na aplicação examinada |

IDs no banco são `INT AUTO_INCREMENT`; os identificadores no protocolo são serializados em oito bytes. `created_at` normalmente é `TIMESTAMP DEFAULT CURRENT_TIMESTAMP`. O esquema não impõe enums para status, identificador único de payload, nonce da credencial, papel de usuário, número USP, telefone, diagnóstico, documento comprobatório, ocupação da sala ou estado online/bateria do dispositivo.

```mermaid
erDiagram
    USER ||--o{ INSTITUTION : possui
    INSTITUTION ||--o{ BUILDING : contem
    BUILDING ||--o{ ROOM : contem
    ROOM ||--o{ DIGITAL_LOCK : possui
    USER ||--o{ DIGITAL_KEY : recebe
    DIGITAL_LOCK ||--o{ DIGITAL_KEY : autentica
    USER ||--o{ DIGITAL_KEY_REQUEST : solicita
    DIGITAL_LOCK ||--o{ DIGITAL_KEY_REQUEST : recebe_pedido
    DIGITAL_LOCK ||--o{ EVENT_LOG : referencia_prevista
```

`auth` foi omitida das arestas porque a associação com usuário é feita pela aplicação usando o hash do e-mail, não por uma FK. As relações são estruturais; `EVENT_LOG` não representa um fluxo ativo comprovado.

O arquivo DBML do backend não inclui `digital_key_request`, `used` e `used_at`, usa `expiration` em vez de `expires_at` e tem cardinalidades que não reproduzem todas as restrições do DDL. Os diagramas do TCC também trazem entidades como `history`, `client` e `admin` que não existem como tabelas nessa implementação. [B10, T02]

## 6. Protocolo da credencial e criptografia

### 6.1 Formato efetivamente emitido pela API

Em `app/modules/cmac/key.py`, `DigitalKey.get_digital_key_payload()` serializa quatro inteiros sem sinal em big-endian e concatena uma tag AES-CMAC. [B08]

| Offset, começando em zero | Tamanho | Conteúdo |
| --- | --- | --- |
| 0–7 | 8 bytes | `user_id` |
| 8–15 | 8 bytes | **`digital_lock_id`** |
| 16–23 | 8 bytes | Timestamp POSIX de emissão, em segundos inteiros |
| 24–31 | 8 bytes | Timestamp POSIX de expiração, em segundos inteiros |
| 32–47 | 16 bytes | Tag CMAC calculada sobre os primeiros 32 bytes |
| Total | **48 bytes** | Mensagem de 32 bytes + tag de 16 bytes |

O segredo normalmente é gerado por `Key()` com `os.urandom(32)`, armazenado por tranca e usado como chave AES de 256 bits. A tag tem 128 bits. A função auxiliar `generate_random_key()` tem outro default quando chamada diretamente, mas o fluxo ativo de criação de tranca fornece o tamanho configurado de 32 bytes; não se deve confundir esse default auxiliar com o protocolo real.

O código antigo em `src/digital_key/` chama o segundo campo de **`room_id`**. A API ativa importa o módulo de `app/`, que usa **`digital_lock_id`**. Essa diferença semântica importa mesmo com layout binário idêntico. O firmware local contém uma variável `roomID`, mas ainda não interpreta nem verifica esse campo. [B08, B11, W03]

Não há versão de protocolo, tipo de mensagem, número da chave do banco, nonce aleatório ou contador no payload. **Inferência do algoritmo:** emissões para o mesmo usuário/tranca com os mesmos segundos de emissão e expiração produzem o mesmo payload. `digital_key.id` não está autenticado na mensagem. Logo, “uma linha nova no banco” não assegura “uma credencial binária inédita”.

### 6.2 Transporte até o QR

O banco guarda bytes; a API converte o payload para string hexadecimal com espaços/quebras de linha no JSON. O hook `useKeyQrCode` faz a conversão inversa para `Uint8Array` e passa à biblioteca `qrcode` um segmento explícito `mode: "byte"`. O QR é gerado localmente como data URL, com largura 260 e margem 1. [B05, F05]

Essa separação evita confundir representação textual do JSON com o conteúdo binário do QR. Passar o hexadecimal literalmente, ou transformar bytes arbitrários em texto UTF-8, não reproduziria os mesmos 48 bytes. O firmware trabalha com o payload bruto e seu comprimento.

A implementação do hook não fixa versão do QR nem nível de correção de erros. A tese exige leitura de QR versão 3, mas essa configuração/compatibilidade não foi demonstrada por ensaio. Não foi localizado botão dedicado de download, persistência offline ou geração de QR pela API ativa.

### 6.3 Propriedades que podem ser afirmadas

AES-CMAC é autenticação simétrica de mensagem. Permite verificar integridade e autenticidade em relação a quem possui o segredo; não oferece não repúdio. Esse enquadramento é confirmado pelo [NIST SP 800-38B](https://csrc.nist.gov/pubs/sp/800/38/b/upd1/final) e pelo [glossário de MAC do NIST](https://csrc.nist.gov/glossary/term/message_authentication_code).

O código concatena dados legíveis por decodificação binária e tag; **não cifra o payload**. O nome `private_key` não indica um par assimétrico público/privado. Para a tese, a formulação precisa é “credencial autenticada por AES-CMAC com segredo simétrico compartilhado”, evitando apresentar esse mecanismo como assinatura digital assimétrica.

**Inferências para este sistema:** quem conhece o segredo compartilhado pode gerar tags; um QR pode ser copiado e apresentado por outra pessoa; conter `user_id` não prova presença física do titular; um CMAC válido não comprova que uma porta abriu ou que uma pessoa entrou. Assim, a “irretratabilidade dos acessos” afirmada no resumo e no requisito RF-06-03 não é sustentada por esse mecanismo isolado.

### 6.4 Expiração e uso único

- **Emissão:** a expiração é incluída na mensagem autenticada e armazenada no banco. As rotas administrativas usam 24 horas por padrão quando não há expiração informada.
- **Interface:** `useClientDashboard` considera ativa uma chave com `used === 0` e expiração futura, segundo o relógio do navegador. Essa condição é recalculada no carregamento/refresh, não continuamente por um timer no hook.
- **Consumo na API:** `use_digital_key()` procura o payload no banco, rejeita se já marcado como usado, verifica CMAC e atualiza `used`/`used_at`. Não compara expiração com o horário atual.
- **Firmware:** só calcula/confere CMAC; não extrai timestamps nem controla reutilização.
- **Unicidade local:** não foram encontrados armazenamento persistente de credenciais consumidas ou proteção contra replay após reinicialização.

Logo, campos de expiração e uso estão implementados, mas **a garantia de expiração e uso único na abertura física não está implementada nos arquivos examinados**. A flag no servidor não é consultada pelo firmware. [B03, B04, F04, W02]

Também há limites transacionais: o consumo faz leitura de `used` seguida de atualização, sem um `UPDATE ... WHERE used = FALSE` ou bloqueio explícito nessa rotina. Não se deve afirmar proteção comprovada contra dois consumos concorrentes. Na aprovação, emissão da chave e atualização de status têm commits separados; falha intermediária pode deixar chave emitida e pedido ainda pendente. Esses cenários são inferências estáticas, não falhas reproduzidas por teste.

Os timestamps são construídos com `datetime.now()` sem timezone explícito no fluxo de chaves e convertidos por `datetime.timestamp()`. O JWT, em contraste, usa UTC explícito. Fuso do servidor, sessão MySQL, interpretação no navegador e relógio embarcado precisam ser definidos e testados; este levantamento não assume que coincidam.

## 7. Frontend

### 7.1 Aplicação Next.js encontrada fora da branch aberta

O commit `9005601...` declara Next.js `16.2.9`, React/React DOM `19.2.4`, `qrcode` `^1.5.4`, TypeScript `^5`, Tailwind CSS `^4` e ESLint `^9`. Existe `package-lock.json`. A estrutura usa App Router, componentes TSX, hooks para estado/carregamento e serviços de chamadas HTTP. São versões declaradas na fonte, não versões instaladas verificadas. [F01]

As chamadas usam `fetch` com base em `NEXT_PUBLIC_API_URL`. O login armazena `data.token` em `localStorage` sob a chave `access_token`; endpoints protegidos recebem Bearer. Várias páginas verificam apenas a existência local do token para redirecionar ao login, enquanto a validação criptográfica ocorre na API. Não foi encontrado middleware de autenticação global nem refresh de sessão. O login redireciona para `/dashboard`, sem distinguir um campo `type` de usuário. [F02–F04]

Os hooks carregam conjuntos de dados e fazem associações por ID no navegador. A busca de acesso usa listas globais e filtros locais por nome/hierarquia, embora a API também ofereça endpoints `/search`. Ao selecionar sala, `useAccessRequest` usa a **primeira tranca retornada**, não uma seleção explícita entre todas. Isso é uma limitação de interface diante da cardinalidade de várias trancas por sala.

### 7.2 Páginas e funcionalidades concretas

| Rota Next.js | Estado encontrado |
| --- | --- |
| `/` | Redireciona a `/login`; não contém a landing page institucional descrita no README |
| `/login` | Formulário ligado a `/auth/user`; feedback de carregamento/erro |
| `/signup` | Nome, e-mail, senha e confirmação; cadastro via API e redirecionamento ao login |
| `/dashboard` | Cards de chaves ativas, tabela de chaves/recusas pretendida e modal de QR; depende de endpoint ausente na versão atual do backend |
| `/access/request` | Seleção de instituição, prédio e sala; envia pedido e informa que depende de aprovação; retorna ao dashboard |
| `/access/[key_id]` | Arquivo vazio; o QR efetivamente implementado está no modal do dashboard |
| `/admin/dashboard` | CRUD de instituições, prédios, salas e trancas com modais e serviços administrativos |
| `/admin/keys` | Filtra pedidos pendentes/aprovados/rejeitados/todos e permite aprovar/rejeitar |
| `/admin/rooms/[id]/key-holders` | Lista portadores de chaves da sala e filtros por uso/data |
| `/users` | Portadores de chaves das instituições próprias e formulário de criação de usuário |
| `/users/[id]/history` | Histórico de chaves do usuário nas instituições do responsável |
| `/profile` | Perfil, edição de nome/e-mail e troca de senha |
| `/settings` | Texto provisório, sem painel funcional de preferências |
| `/logs` | Estrutura inicial de página, sem consulta de eventos |

O histórico administrativo é derivado de `digital_key`, incluindo chaves ainda não usadas. As agregações de portadores usam `MAX(used)` e `MAX(used_at)`: indicam existência de uso e último instante registrado, não ocupação atual, contagem de entradas ou um log completo por evento. Criar um usuário por esse painel não o torna automaticamente portador de chave nem membro formal de instituição. [B03, F06–F08]

Não foi localizada interface de emissão administrativa direta conectada a `/admin/keys/issue`; a página de gestão examinada trata solicitações. Também não há fluxo de revogação de credencial no backend examinado. Itens do README sobre emissão/revogação, landing page, papéis e rotas em português não devem ser adotados como prova da implementação.

### 7.3 Incompatibilidades concretas com o backend disponível

**D01 — Consulta de solicitações do próprio usuário.** `services/digitalKey.service.ts` chama `GET /digital_key/requests?status=rejected`, mas essa rota não existe no backend principal. `useClientDashboard` inclui essa chamada no mesmo `Promise.all` das chaves e catálogos. **Inferência de integração:** com essas versões, a resposta de rota inexistente faz o carregamento cair no erro e impede a montagem normal das listas, mesmo se as demais consultas funcionarem.

**D02 — Detalhes de solicitações administrativas.** O frontend declara/consome `user_name`, `user_email`, `room_name` e `building_name` nos pedidos. O backend retorna `digital_key_request.*`, sem selecionar esses campos dos JOINs. A consulta usa JOINs para limitar proprietário, não para enriquecer o resultado. A interface não receberá esses detalhes no contrato examinado. [F04, F07, B03]

**D03 — “Expirada” e “utilizada”.** O dashboard classifica qualquer chave não ativa como `used`, inclusive uma chave apenas expirada, e a tabela apresenta “Já utilizada”. Além disso, mantém a ação de gerar QR para chaves não rejeitadas, inclusive usadas/expiradas. O hook de QR não impõe validação temporal ou de uso. A interface não pode ser tratada como autoridade de autorização. [F04–F06]

**D04 — Página de acesso vazia.** A rota dinâmica anunciada em documentação não é a implementação do QR. A descrição da tese deve apontar o modal efetivo, sem afirmar que essa página está concluída. [F06]

### 7.4 Protótipo HTML da branch `main`

Contém doze páginas HTML: seis de usuário e seis administrativas, com CSS embutido e JavaScript principalmente para menu lateral. Mostra nomes, métricas, bateria, logs e salas de exemplo; não foram encontradas chamadas à API da aplicação nessas páginas. O formulário de login não implementa autenticação com o backend.

Em `gerar_qr.html`, `generateKey()` requisita a um serviço externo de QR uma imagem para **texto fixo de demonstração**, sem payload AES-CMAC. O contador de cinco minutos só altera a exibição e não invalida criptograficamente nada. A página de configuração apresenta MQTT/IP/porta como campos estáticos. Isso é material de prototipação de interface, não evidência de integração, broker ativo, telemetria ou política de expiração final.

O serviço externo usado nesse HTML não deve ser confundido com a aplicação Next.js, que gera o QR no navegador. Não foi acessado esse serviço durante a análise. [F09]

## 8. Firmware e hardware

### 8.1 Plataforma e configuração

O projeto usa PlatformIO com `platform = espressif32`, `board = esp32cam`, `framework = arduino`, dependência `ESP32QRCodeReader` e modelo `CAMERA_MODEL_AI_THINKER`. A configuração declara PSRAM habilitada, monitor serial a 115200, upload a 921600 e porta `/dev/ttyUSB0`. A plataforma e a biblioteca não têm versão fixada no arquivo. O arquivo local `sdkconfig.defaults` contém `CONFIG_MBEDTLS_CMAC_C=y`; sua presença não prova que essa opção tenha sido aplicada ao build Arduino. [W01]

OV2640 é a câmera indicada na tese e no diagrama físico. Não foi inspecionado o hardware para confirmar câmera instalada, revisão da placa, memória efetiva, alimentação ou pinagem do circuito externo.

### 8.2 Aquisição óptica e tarefas

`setupQRCodeReader()` inicializa a biblioteca, chama `beginOnCore(1)`, cria a tarefa FreeRTOS `onQrCodeTask` com pilha configurada como `4 * 1024` e prioridade 4 e habilita leitura. A tarefa recebe resultados com timeout 100 e usa atraso configurável, inicialmente 50 ms. [W02]

O resultado é exposto por uma estrutura global `QRCodePayload` com ponteiro para bytes, comprimento e flag de sucesso. `readQRCode()` retorna essa estrutura. Há funções de pausar/retomar e ajustar intervalo.

A tarefa compartilha dados com `loop()` sem mutex/fila próprios na camada escrita pela equipe. O ponteiro aponta para o buffer de `qrCodeData` na tarefa, e não para uma cópia imutável entregue ao consumidor. Isso exige cuidado com sobrescrita/consistência entre leituras; não é correto assumir isolamento entre tarefas apenas porque a biblioteca fornece uma interface de recepção.

### 8.3 Validação e saída atuais

O validador copia os primeiros 32 bytes para a mensagem e os 16 seguintes para a tag; usa `MBEDTLS_CIPHER_AES_256_ECB` como identificador do primitivo AES para `mbedtls_cipher_cmac`. Esse identificador não significa que a credencial seja cifrada em ECB. O objetivo da função é CMAC.

A função compara os 16 bytes da tag calculada com a recebida. Não verifica o comprimento passado em `messageLength`, não interpreta IDs/timestamps e não mantém estado de consumo. Uma entrada menor que 48 bytes pode provocar leitura além do conteúdo válido; uma entrada maior não é rejeitada por tamanho. O retorno de `mbedtls_cipher_cmac` não é tratado, e a ausência de `cipher_info` faz a função auxiliar retornar sem resultado válido explicitamente propagado. [W02]

`setup()` configura serial, define GPIO 4 como saída e inicializa a leitura. No caminho de QR lido, `loop()` imprime o payload em hexadecimal e a mensagem `Digital Key Valid: Yes/No`, seguida de atraso de um segundo. Não há escrita de GPIO para abrir/fechar atuador nem feedback luminoso de sucesso/erro nessa rotina. Configurar `pinMode` não equivale a acionar uma fechadura. [W02]

### 8.4 Mudanças locais e incompatibilidade de compilação

**D05 — Assinatura divergente:** o cabeçalho/implementação local de `validateDigitalKey` exige três argumentos — mensagem, tamanho e segredo — mas `main.cpp` chama com dois. Não há overload ou argumento default localizado. É uma incompatibilidade identificada estaticamente, suficiente para impedir essa chamada de compilar conforme os arquivos apresentados; não foi executado build de placa.

`digital_lock.cpp`, ainda não rastreado, define segredo fixo de 32 bytes, `roomID`, `setPrivateKey()` e `setRoomID()`. O cabeçalho correspondente só inclui headers, sem declarar essa interface. Não foi localizada conexão dessas funções ao fluxo de `main.cpp`, comunicação de provisionamento ou persistência do segredo. O valor do segredo não é reproduzido neste documento. [W03]

### 8.5 Elementos físicos/embarcados não confirmados

Não foram localizados nos fontes examinados: driver de relé/solenoide, circuito de potência, sensores de porta, botão de saída, controle de travamento, RTC/sincronização de horário, cliente MQTT, configuração Bluetooth, provisionamento seguro, rotação de segredo, persistência NVS/arquivo de credenciais consumidas, log auditável local ou envio de eventos ao backend.

Também faltam evidências de modelo da fechadura elétrica, chave mecânica de contingência, fonte/bateria, autonomia de seis horas, consumo, comportamento em queda de energia, MTTF, ruído e adequação sensorial. Essas funções podem existir em montagem ou versões externas; não foram demonstradas pelos repositórios disponíveis.

## 9. Fluxos funcionais reconstruídos

### 9.1 Cadastro e login

O navegador envia cadastro à API; ela cria usuário/credenciais e retorna `user_id`. O frontend leva ao login. Após autenticação, guarda JWT e navega ao dashboard. Os nomes de contrato reais são `user_id` para cadastro e `token` para login, embora textos antigos falem em `id`/`access_token` como resposta.

### 9.2 Preparação administrativa

O usuário autenticado cria instituição da qual se torna responsável; cadastra prédio, sala e tranca. A criação de tranca gera segredo no backend. **Este fluxo termina no registro lógico:** não foi localizado procedimento implementado que entregue automaticamente esse segredo ao ESP32 correspondente.

### 9.3 Solicitação e aprovação

1. Usuário seleciona instituição/prédio/sala na interface.
2. Frontend consulta trancas da sala e escolhe a primeira.
3. `POST /digital_key/request` cria pedido `pending`, com usuário do JWT.
4. Responsável consulta pedidos de suas instituições e decide.
5. Aprovação confere propriedade e estado pendente, emite chave e altera pedido para `approved`.
6. Rejeição altera pedido para `rejected`, sem emitir chave.
7. Chave aprovada pode ser consultada pelo ID de usuário/chave; a exibição de recusas no dashboard depende do endpoint ausente descrito em D01.

A aprovação sem data explícita usa 24 horas contadas da aprovação/emissão. Não há permissão recorrente, agenda por dias da semana ou concessão de acesso para intervalo com geração autônoma de várias credenciais. O README Next.js registra essa ampliação como possibilidade futura.

### 9.4 Exibição e leitura

Abrir o modal consulta uma chave **já emitida**, converte o hexadecimal para bytes e renderiza QR. O botão “Gerar chave de acesso”, nesse contexto, gera a representação gráfica, não uma nova credencial no banco. O leitor embarcado extrai bytes e foi escrito para conferir CMAC localmente. A passagem desse resultado para abertura física não está implementada nos arquivos observados.

### 9.5 Registro de uso e histórico

`POST /digital_key/use` recebe hexadecimal, recupera a chave, verifica estado/CMAC e registra horário do servidor. Não há chamada a esse endpoint no firmware ou nos serviços frontend examinados. Portanto, a existência de `used_at` não demonstra ingestão automática de um evento físico. Também não diferencia leitura de QR, autorização, destravamento, abertura da porta, entrada, saída ou fechamento.

Uma auditoria física precisaria definir esses eventos e suas fontes de verdade. Não é possível deduzir ocupação da sala a partir de chaves emitidas ou `MAX(used)`.

## 10. Tese e diagramas: correspondências e diferenças

### 10.1 Estado do texto recebido

O PDF possui introdução, motivação/objetivos, requisitos e uma descrição breve das tecnologias. Os capítulos de conceitos e método ainda contêm instruções do modelo; projeto/implementação, testes/avaliação e considerações finais também têm conteúdo provisório. A ficha catalográfica, agradecimentos, siglas e símbolos contêm material de preenchimento. Há duas seções de referências no final, sendo a última sem entradas no texto extraído. [T01]

As figuras 1–4 aparecem no PDF como caixas com os nomes dos arquivos; isso foi corroborado visualmente na página física 39, numerada 37. Os PNGs originais foram abertos separadamente para analisar o conteúdo. Não se atribuiu ao PDF informação que só está nesses PNGs. As páginas citadas por capítulo neste documento usam a numeração impressa da tese.

### 10.2 Diagramas existentes

| Fonte | O que representa | Situação perante o código |
| --- | --- | --- |
| `contexto_c4.drawio.png` | Cliente, admin, aplicação, serviços externos, tranca física e gateway | Gateway e integração com serviços externos não localizados como componentes ativos |
| `application_container_c4.drawio.png` | Next.js, Flutter, FastAPI, AWS S3 e PostgreSQL | Next.js/FastAPI correspondem ao código; banco implementado é MySQL; Flutter/S3 não encontrados |
| `physical_lock_container_c4.drawio.png` | OV2640, ESP32-CAM, HMI, tranca, saída, Bluetooth e MQTT | Leitura/CMAC têm código; demais integrações precisam ser confirmadas |
| `relacionamentos.drawio.png` | Cliente/admin, instituição/prédio/sala, chave/tranca e histórico/evento | Modelo conceitual anterior; não corresponde literalmente ao DDL |
| `uml.png` | Herança de usuário, campos de tipo/status, chave e histórico | Não representa as tabelas/classes ativas em vários pontos; não é uma das quatro figuras incluídas no cap. 5 |

No diagrama físico, existem setas MQTT envolvendo botão de saída e tranca elétrica. O circuito real não foi fornecido; não se deve reproduzir essas setas como descrição de cabeamento ou afirmar que o atuador tem cliente MQTT. “Contêiner” no C4 também não implica Docker; não há configuração Docker encontrada.

### 10.3 Quadro de reconciliação para a escrita

| Afirmação ou expectativa | Conclusão sustentada |
| --- | --- |
| “Frontend em React” | Correto para a referência Next.js; incorreto se considerado apenas o checkout HTML |
| “PostgreSQL e AWS S3” | Proposta dos diagramas; implementação examinada usa MySQL e não integra S3 |
| “Aplicativo Flutter” | Previsto em diagrama, não encontrado nos quatro repositórios |
| “Backend gera QR” | Backend gera/autentica bytes; Next.js renderiza imagem QR |
| “QR contém ID da sala” | Código antigo usa sala; API ativa usa ID da tranca digital |
| “Códigos únicos e temporários” | Campos e partes do controle existem; garantia física de uso único/expiração não comprovada |
| “Assinatura e irretratabilidade” | Implementação é MAC simétrico; não sustenta não repúdio isoladamente |
| “Segredo compartilhado assincronamente” | Não foi localizado protocolo implementado de distribuição |
| “Tranca funciona offline” | Verificação CMAC pode ocorrer sem rede; abertura offline completa não demonstrada |
| “Auditoria e ocupação” | Há tabelas/campos e consultas parciais; falta cadeia de eventos físicos |
| “QR vale 5 minutos” | Texto do HTML antigo; padrão administrativo atual é 24 horas |
| “Projeto praticamente concluído” | Pode refletir versões ou montagem não disponíveis; requer confirmação diante das lacunas e incompatibilidades identificadas |

## 11. Segurança e confiabilidade: limites observados

Estes pontos são relevantes para escrever com precisão, não uma auditoria exaustiva nem exploração de um serviço em operação. Nenhuma correção foi aplicada aos outros repositórios.

| ID | Evidência estática | Implicação para as alegações da tese |
| --- | --- | --- |
| S01 | Consultas públicas de trancas retornam `secret_key` em hexadecimal [B07] | O segredo usado para autenticar credenciais é exposto pelo contrato da API; confidencialidade da chave não está garantida |
| S02 | `/digital_key/new` não exige token/propriedade [B05] | Há caminho para emissão fora do fluxo de aprovação administrativa |
| S03 | Consulta pública de chaves por usuário/chave e listagem global [B05] | Payloads que funcionam como credenciais podem ser obtidos fora do perfil proprietário |
| S04 | `/digital_key/use` público e sem identidade de dispositivo [B05] | Registro de uso não comprova origem no hardware nem evento físico |
| S05 | Consumo não verifica expiração; firmware não verifica uso/tempo [B03, W02] | Não afirmar proteção completa contra expiração e replay |
| S06 | `messageLength` ignorado e falhas de CMAC não propagadas corretamente [W02] | Entrada malformada/erro de biblioteca não têm tratamento defensivo suficiente |
| S07 | Leitura/atualização de uso e aprovação sem atomicidade completa [B03, B04] | Concorrência e falhas intermediárias precisam de tratamento/ensaio |
| S08 | Segredo fixo no fonte local de firmware, sem provisionamento integrado [W03] | Não alegar gestão segura de ciclo de vida de chaves |
| S09 | Senhas com SHA-256 simples + salt; JWT em `localStorage` [B06, F03] | Descrever escolhas reais e avaliar proteção de credenciais/sessão sem presumir endurecimento de produção |
| S10 | Ausência de sincronização de relógio e log físico persistente [W01–W03] | Não garantir autonomia temporal, recuperação após reinício ou auditoria offline |

Também não foram localizados controles de rate limiting, política de retenção, backups, monitoramento operacional, proteção física do segredo ou configuração de criptografia em repouso. A ausência nos fontes não demonstra ausência em infraestrutura externa. Em sentido inverso, não autoriza afirmar que tais controles existam.

Nome, e-mail e histórico de chaves são dados pessoais no contexto do projeto. O esquema examinado não solicita diagnóstico ou laudo. Não se deve importar para a descrição do banco campos de documentos/Nº USP do HTML antigo. Qualquer alegação de conformidade jurídica ou normativa demanda avaliação própria; este documento não a estabelece.

## 12. Acessibilidade e experiência de uso

A contribuição pretendida é reduzir dependência de portaria/chaves físicas e tornar o acesso mais previsível para pessoas neurodivergentes. Isso é finalidade do projeto; não há estudo de usuários ou medição de redução de sobrecarga cognitiva nos materiais examinados. [T01]

A interface Next.js implementa feedback textual de carregamento/erro, seleção hierárquica, indicação de status, formulários e QR em destaque. Porém, existem menus acionados por `div`/`span`, card clicável sem controle de teclado explícito, modais sem tratamento de foco identificado nesses componentes e `lang="en"` no layout raiz apesar do conteúdo em português. Esses pontos merecem avaliação, sem confundir inspeção de código com teste completo de acessibilidade. [F02, F06, F08]

Não foram encontradas preferências funcionais de alto contraste, redução de estímulos, tamanho de fonte ou outro perfil de acessibilidade; `/settings` é provisória. Responsividade, contraste, navegação por teclado, leitores de tela, altura/posição da câmera, iluminação e esforço motor/cognitivo precisam de evidências de avaliação. Não há evidência para afirmar conformidade com um nível específico de WCAG.

O fluxo atual aprova pedidos um a um. Pode reduzir a retirada presencial da chave, mas ainda exige espera administrativa para cada credencial solicitada. A tese deve discutir essa diferença entre autonomia na entrada e dependência na autorização, incluindo contingência para indisponibilidade de celular, bateria ou conexão na obtenção do QR.

## 13. Rastreabilidade dos requisitos do PDF

A classificação corresponde às fontes disponíveis, não ao estado de uma instalação desconhecida. IDs repetidos foram preservados conforme o documento recebido. [T01, pp. 31–33]

| Requisito | Evidência e situação |
| --- | --- |
| RF-00-00 — controle seguro, auditável e automatizado | **Parcial:** API, credenciais e leitor; segurança, atuação e auditoria têm lacunas |
| RNF-00-00 — confidencialidade, integridade e disponibilidade | **Parcial/não demonstrado:** CMAC presente, mas exposição de segredos e ausência de avaliação global |
| RF-01-00 — destravar sem internet | **Parcial:** cálculo de CMAC sem rede; destravamento não localizado |
| RF-01-01 — agnóstico ao modelo de tranca elétrica | **Previsto:** falta interface elétrica/driver comprovado |
| RF-01-02 — operar após queda de energia | **Não confirmado:** alimentação/contingência não documentadas |
| RF-01-03 — autonomia mínima de seis horas | **Não confirmado:** sem especificação de bateria ou ensaio |
| RNF-01-00 — MTTF maior que seis meses | **Não confirmado:** sem cálculo/ensaio/evidência de confiabilidade |
| RF-02-00 — abertura por chave física | **Não confirmado:** depende da fechadura/montagem |
| RF-03-00 — destravar após leitura legítima | **Parcial:** leitura/CMAC, sem atuação localizada; chamada local incompatível |
| RF-03-01 — registrar leitura, abertura, fechamento, configurações e envio | **Previsto/parcial:** serial e tabela de eventos não equivalem a registro completo |
| RF-03-02 — histórico interno auditável | **Não localizado:** sem persistência local de eventos |
| RF-04-00 — ler QR versão 3 | **Não demonstrado:** leitor presente; geração não fixa versão e faltam ensaios |
| RF-05-00 — HMI com feedback claro | **Parcial:** monitor serial técnico; HMI física não implementada nos fontes |
| RF-06-00 — usuário, sala, emissão e expiração na credencial | **Parcial/divergência:** usuário, tranca, emissão e expiração; sala é obtida pela relação com tranca |
| RF-06-01 — autenticidade | **Mecanismo implementado:** CMAC; garantia sistêmica depende de proteção do segredo/autorização |
| RF-06-02 — integridade | **Mecanismo implementado:** tag sobre os 32 bytes; integração e erros ainda precisam de testes |
| RF-06-03 — irretratabilidade | **Não sustentado:** MAC simétrico não oferece não repúdio isoladamente |
| RF-06-04 — assinatura eletrônica | **Reformular tecnicamente:** autenticação simétrica por CMAC; não afirmar assinatura assimétrica |
| RNF-06-00 — leitura em menos de dois segundos | **Não confirmado:** intervalos de polling/delay não são medição de latência |
| RF-07-00 — autenticidade, integridade, expiração e uso único antes de abrir | **Parcial:** validação embarcada só de CMAC |
| RF-09-00 — web responsiva, cadastro/login/solicitação/chaves/admin | **Parcial:** Next.js implementa várias funções; D01/D02, armazenamento e avaliação responsiva pendentes |
| RF-10-00 — autenticação, autorização, emissão, persistência e auditoria | **Parcial:** núcleo API implementado; rotas públicas contornam política e auditoria física falta |
| REQ-FUNC-01 — não hiperestimular sensorialmente | **Não confirmado:** depende de avaliação da tranca/HMI |
| REQ-FUNC-01 — minimizar sobrecarga cognitiva | **Objetivo previsto:** sem evidência de avaliação com usuários |
| REQ-FUNC-01 — minimizar interações humanas obrigatórias | **Parcial:** fluxo web reduz retirada presencial, mas aprovação é individual por pedido |

O PDF repete `RF-10-00` na própria linha e usa `REQ-FUNC-01` para três requisitos distintos. Vale normalizar os identificadores antes de produzir a matriz final de verificação.

## 14. Base para os próximos capítulos e perguntas à equipe

### 14.1 Conteúdo que já pode sustentar a redação

- **Introdução:** problema e público descritos no PDF, separando motivação de benefícios medidos.
- **Conceitos:** controle de acesso, autenticação/autorização, credencial versus segredo, MAC simétrico, transporte binário por QR, operação offline e suas limitações.
- **Projeto:** frontend Next.js, API FastAPI, MySQL, domínio hierárquico, modelo de proprietário e formato de 48 bytes.
- **Implementação:** rotas/repositórios, geração CMAC, conversão hex↔bytes, hooks/serviços, tarefa de leitura embarcada e estágio real de integração.
- **Resultados:** funcionalidades demonstradas por ensaios que a equipe fornecer; não usar dados fixos do HTML como resultados.
- **Discussão:** autonomia versus aprovação individual, segurança do segredo, expiração/replay, sincronização, acessibilidade e limitações.

Não foram encontrados relatórios de testes automatizados ou ensaios físicos nos arquivos inventariados, nem pipeline de CI que forneça seus resultados. Este levantamento realizou inspeção estática, não teste funcional da aplicação ou da placa. A falta de relatório no repositório não significa que a equipe nunca testou o sistema.

### 14.2 Evidências que faltam para fechar a tese

| Área | Evidência a produzir ou localizar — não executada neste levantamento |
| --- | --- |
| Versões | Identificar os commits realmente usados em demonstração e corrigir divergências entre cópias |
| Integração web | Cadastro/login, consulta de recusas, aprovação/rejeição e exibição de QR com os contratos efetivos |
| Protocolo | Vetores comuns Python/C++, bytes ≥128/zero, tamanho inválido, tag alterada, chave de outra tranca e segredo errado |
| Autorização | Usuário sem token, não proprietário, tentativa de emissão/consulta indevida e não exposição de segredos |
| Tempo/uso único | Expiração nas fronteiras, fusos, relógio incorreto, replay, reinício, concorrência e falha após autorização |
| Hardware | Esquema elétrico, lista de materiais, modelo de tranca, alimentação, driver, proteção e contingência mecânica |
| Óptica | Latência e taxa de sucesso por brilho, distância, ângulo, tamanho de QR e condições de iluminação |
| Energia/confiabilidade | Ensaio de autonomia, comportamento em queda de energia e fundamento de MTTF |
| Auditoria | Origem dos eventos, timestamps, persistência offline, sincronização e distinção entre autorização e abertura real |
| Acessibilidade | Procedimento de avaliação, tarefas, participantes/consentimento quando aplicável, resultados e limitações |

### 14.3 Questões prioritárias para revisão da equipe

1. A aplicação final é mesmo a de `origin/frontend_prototype`? Há backend mais recente com `/digital_key/requests` e detalhes enriquecidos de solicitações?
2. Existe firmware mais novo, fora desta pasta, que aciona a tranca, controla expiração/uso único e registra eventos? As mudanças locais representam uma refatoração em andamento?
3. Qual é o nome final do projeto e o significado de FLIKE? A denominação CAUSP-LOCK permanece na monografia?
4. Qual fechadura/circuito/bateria foi montado, e quais funções foram demonstradas fisicamente?
5. Como o segredo por tranca é instalado no dispositivo e como o dispositivo identifica sua tranca digital?
6. A política final será uma chave por solicitação, acesso recorrente ou autorização por intervalo? Qual validade deve prevalecer?
7. O segundo campo do protocolo deve identificar sala ou tranca? Como ficam salas com múltiplas trancas?
8. MQTT, gateway, Bluetooth, Flutter e S3 foram abandonados, adiados ou implementados em fontes ainda não fornecidas?
9. Como serão distinguidos leitura, autorização, destravamento, entrada, saída e ocupação?
10. Quais resultados de testes e avaliação com o público-alvo já existem fora do Git?

Correções podem indicar os IDs D01–D05/S01–S10, a seção afetada e o commit/arquivo ou evidência física correspondente. Assim, o documento pode evoluir sem converter hipóteses em fatos.

## 15. Índice de fontes para conferência

As raízes dos repositórios nesta máquina são:

- Backend: `/home/hsouza/Projects/flike-backend-api`.
- Frontend: `/home/hsouza/Projects/flike-frontend-webpage`.
- Firmware: `/home/hsouza/Projects/flike-firmware`.
- TCC: `/home/hsouza/Projects/flike-tcc`.

Os caminhos abaixo são relativos à raiz identificada pelo prefixo, para permitir consulta também em outras máquinas. **As fontes F01–F08 precisam ser lidas no commit Next.js indicado na seção 1; não se encontram no checkout `main` atual.**

| ID | Arquivo(s) / símbolos principais |
| --- | --- |
| B01 | `app/main.py`: routers incluídos e CORS |
| B02 | `scripts/create_db.py`: funções `create_*_table` |
| B03 | `app/database/repositories.py`: repositórios de usuário, infraestrutura, chave e solicitação; especialmente `create_digital_key`, `use_digital_key`, `get_requests_by_owner`, `get_key_usage_history` |
| B04 | `app/api/routes/admin.py`: verificações de proprietário, `DEFAULT_KEY_VALIDITY`, `approve_key_request`, `reject_key_request` |
| B05 | `app/api/routes/digital_key.py` e `app/schemas/digital_key_models.py`: serialização, emissão, consumo e solicitação |
| B06 | `app/api/routes/auth.py`, `app/api/routes/user.py`, `app/modules/auth/{jwt_token,hashes,salt_gen}.py`, schemas correspondentes |
| B07 | `app/api/routes/digital_lock.py`: `_serialize_digital_lock`; routers de instituição, prédio, sala, health check, evento e binário |
| B08 | `app/modules/cmac/key.py`: `Key`, `AES_CMAC`, `DigitalKey`; `app/modules/utils/binary_handler.py`: serialização |
| B09 | `app/database/{pool,database_manager,connection}.py`, `app/services/env.py`, `requirements.txt`, `scripts/run_server.sh` |
| B10 | `docs/database.dbml`, `docs/project_structure.md` |
| B11 | `src/digital_key/digital_key.py`, `src/digital_key/auth/auth.py`, `src/digital_key/binary_handler/binary_handler.py`: versão alternativa/antiga |
| F01 | `package.json`, `package-lock.json`, `next.config.ts`, `tsconfig.json` |
| F02 | `app/layout.tsx`, `app/page.tsx`, `app/(main_pages)/layout.tsx`, páginas login/signup e hooks `useLogin`/`useSignup` |
| F03 | `services/auth.service.ts`, `services/user.service.ts` |
| F04 | `services/digitalKey.service.ts`, `services/digitalLock.service.ts`, `hooks/useClientDashboard.ts`, `hooks/useAccessRequest.ts`, `types/digitalKey.ts` |
| F05 | `hooks/useKeyQrCode.ts`, `components/QrCodeModal.tsx` |
| F06 | `app/(main_pages)/dashboard/page.tsx`, `app/(main_pages)/access/request/page.tsx`, `app/(main_pages)/access/[key_id]/page.tsx`, `components/{ActiveKeyCard,DigitalKeysTable}.tsx` |
| F07 | `services/{admin,keyRequest}.service.ts`, `hooks/{useAdminData,useMyAdminData,useKeyRequests,useKeyHolders}.ts`, páginas administrativas, `components/KeyRequestsTable.tsx` |
| F08 | Páginas `profile`, `settings`, `logs`, `users`, histórico individual e portadores por sala; `components/modals/`, `components/Sidebar.tsx`, `components/KeyUsageHistoryTable.tsx`; `README.md`, `docs/pages.md` |
| F09 | **Frontend `main`**: `paginas_html/user/*.html` e `paginas_html/admin/*.html`; especialmente `gerar_qr.html`, `login_user.html` e `config.html` |
| W01 | `platformio.ini`, arquivo local `sdkconfig.defaults` |
| W02 | `src/main.cpp`, `src/qr_code.{cpp,h}`, `src/digital_key.{cpp,h}`, `src/binutils.{cpp,h}` |
| W03 | Arquivos locais `src/digital_lock.{cpp,h}` e mudanças locais de `digital_key` |
| T01 | `TCC___CAUSP_LOCK-1.pdf`; `TCC___CAUSP_LOCK/main.tex`, `Cap1-Intro.tex` a `Cap6-Consideracoes.tex` |
| T02 | PNGs de contexto, aplicação, tranca física, relacionamentos e `uml.png` em `TCC___CAUSP_LOCK/` |

Referências conceituais externas usadas apenas para qualificar a terminologia criptográfica: [NIST SP 800-38B — CMAC](https://csrc.nist.gov/pubs/sp/800/38/b/upd1/final) e [NIST — Message Authentication Code](https://csrc.nist.gov/glossary/term/message_authentication_code). A bibliografia acadêmica já presente no TCC não foi validada bibliograficamente neste trabalho; suas entradas não devem ser consideradas verificadas por este documento.
