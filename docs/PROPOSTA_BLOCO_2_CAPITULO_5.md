# FLIKE — proposta do bloco 2 do Capítulo 5

**Estado:** implementado e aprovado pela equipe em 01/09/2026

**Rodada:** Fase C, passo 10, bloco 2

**Conteúdo do bloco:** Seções 5.3.2, 5.3.3 e 5.3.4 — backend, frontend e fluxo integrado de solicitação, decisão e emissão

**Data:** 01/09/2026

**Progresso global:** 11 de 26 passos concluídos (42,3%)

**Resultado:** as Seções 5.3.2--5.3.4 foram incorporadas à tese e aprovadas no PDF. A figura F5-03 foi produzida em SVG e PDF, e a RFC 7519 foi inserida como referência primária para JWT.

## 1. Objetivo da rodada

Este bloco explicará como a aplicação conectada transforma uma solicitação em uma credencial disponível no painel do solicitante. A exposição seguirá do geral para o particular: primeiro a API e suas regras, depois a interface e, por fim, a sequência que atravessa ambos os componentes.

O texto não será um catálogo de endpoints nem uma descrição de arquivos. Rotas, serviços, hooks e componentes serão mencionados apenas quando ajudarem a explicar uma responsabilidade, uma decisão de produto ou uma limitação relevante. O frontend considerado será exclusivamente a aplicação Next.js/React do commit final confirmado pela equipe.

## 2. Seção 5.3.2 — Backend

### 2.1 Organização da API

A seção começará apresentando quatro camadas identificáveis no código:

1. **rotas FastAPI**, que recebem requisições e aplicam as decisões dos casos de uso;
2. **modelos Pydantic**, que descrevem os corpos de entrada e parte das respostas;
3. **repositórios**, que concentram consultas e comandos SQL de cada entidade;
4. **infraestrutura de persistência**, que fornece conexões MySQL por meio de um pool e confirma ou desfaz transações.

Não será alegada uma camada de serviços ampla nem uso de ORM, pois essas estruturas não existem no commit examinado. O texto explicará que as regras estão distribuídas principalmente entre as funções de rota e os repositórios.

### 2.2 Cadastro, autenticação e sessão

O fluxo será descrito nesta ordem:

1. o cadastro cria os dados pessoais em `user` e as credenciais em `auth`;
2. o e-mail é armazenado em `auth` por seu hash, enquanto a senha recebe um salt aleatório antes da aplicação de SHA-256;
3. o login compara o valor calculado e, em caso de sucesso, emite um JSON Web Token (JWT);
4. o JWT usa HS256, contém o `user_id` e possui expiração de uma hora;
5. rotas protegidas recuperam o usuário a partir do token Bearer.

Esses mecanismos serão descritos como implementação observada, sem chamá-los de autenticação endurecida para produção. SHA-256 com salt não será apresentado como função adaptativa de derivação de senha. A semântica geral do JWT poderá ser sustentada pela RFC 7519; as escolhas concretas de algoritmo, conteúdo e duração serão sustentadas pelo código.

### 2.3 Autorização contextual e gestão administrativa

A API não consulta um papel global de administrador. Para cada operação administrativa, ela recupera o `user_id` do JWT e percorre a hierarquia até `institution.owner_id`. Essa verificação protege as rotas de criação, alteração e remoção de instituições, edifícios, salas e trancas, além da consulta e decisão sobre solicitações.

A exposição agrupará as rotas por responsabilidade, sem listar cada URL:

| Família | Responsabilidade descrita |
| --- | --- |
| conta | cadastro, login, perfil e troca de senha |
| catálogo de acesso | consulta de instituições, edifícios, salas e trancas |
| gestão contextual | manutenção da estrutura que pertence ao usuário autenticado |
| solicitações | criação pelo solicitante e consulta pelo responsável |
| decisões e emissão | aprovação, rejeição e criação da credencial |
| credenciais | consulta do payload usado pelo frontend para renderizar o QR Code |

### 2.4 Solicitação, decisão e emissão

Uma solicitação autenticada é criada com estado `pending`, o identificador do usuário obtido do JWT e a tranca escolhida. Ao decidir, o backend verifica se a tranca pertence a uma instituição do responsável e se a solicitação ainda está pendente.

Na rejeição, o estado passa a `rejected`. Na aprovação, a API cria uma credencial para o solicitante e a tranca, depois altera o estado para `approved`. Se a interface não fornecer uma expiração, o padrão do código é **24 horas contadas do instante da aprovação e emissão**. O payload é produzido com o segredo da tranca e persistido antes de ser recuperado pela interface.

O texto preservará duas limitações já identificadas no modelo: solicitação e credencial não possuem chave estrangeira entre si, e criação da credencial e atualização da solicitação são confirmadas em operações separadas. A tese poderá dizer que o fluxo aplica a política de uma credencial por solicitação aprovada, mas não afirmará que o banco impõe essa cardinalidade nem que a transição é atômica diante de concorrência ou falha intermediária.

## 3. Seção 5.3.3 — Frontend

### 3.1 Organização da interface

A aplicação será apresentada segundo a separação observada no código:

- páginas do App Router compõem as rotas visíveis;
- componentes reutilizáveis implementam tabelas, cartões, formulários e modais;
- hooks coordenam estado, carregamento, erros e ações;
- serviços concentram as chamadas HTTP à API;
- tipos TypeScript representam os contratos consumidos pela interface.

Essa organização será usada para explicar o fluxo sem transformar a seção em documentação interna do repositório.

### 3.2 Fluxo do solicitante

Depois do cadastro e do login, o token é guardado no `localStorage` do navegador. O solicitante percorre instituição, edifício e sala; ao escolher a sala, o código consulta suas trancas e seleciona a primeira tranca retornada. Em seguida, envia a solicitação autenticada.

O painel reúne credenciais emitidas e solicitações rejeitadas. Quando o usuário pede para visualizar uma credencial, o frontend consulta seu payload em hexadecimal, reconstrói os bytes e os entrega à biblioteca de QR Code no modo binário. A janela modal exibe a imagem enquanto a página permanece aberta. A versão 3 e o nível L serão apresentados na Seção 5.4.4, depois que o commit da correção informado pela equipe estiver disponível; a incompatibilidade temporária do commit examinado não será narrada como comportamento final do produto.

O texto não afirmará que há aplicativo móvel, download dedicado, service worker ou persistência própria da imagem após recarga. Também não chamará a marcação `used` da interface de consumo físico obrigatório, porque a política aprovada permite reapresentar a mesma credencial durante sua janela de validade.

### 3.3 Fluxo do responsável

O mesmo usuário acessa a área administrativa para manter instituições próprias, edifícios, salas e trancas. A tela de pedidos filtra solicitações por estado e permite aprovar ou rejeitar apenas as pendentes. Depois da ação, o hook atualiza a listagem para refletir o novo estado.

A narrativa usará “responsável pela instituição” ou “proprietário da instituição”. Rótulos de administrador poderão ser citados somente como nomes da interface, nunca como papel global do domínio.

## 4. Seção 5.3.4 — Fluxo integrado de solicitação e emissão

A subseção reunirá os dois lados em uma sequência única:

1. o usuário autentica-se e recebe o JWT;
2. o solicitante navega pela hierarquia e envia a tranca escolhida;
3. a API identifica o solicitante pelo token e persiste a solicitação pendente;
4. o responsável consulta somente os pedidos relacionados às instituições que possui;
5. a API valida essa propriedade quando recebe a aprovação ou rejeição;
6. uma aprovação cria a credencial, por padrão válida por 24 horas a partir daquele instante, e muda o pedido para `approved`;
7. o painel do solicitante recupera a credencial emitida;
8. ao abrir a credencial, o frontend converte o hexadecimal em bytes e renderiza o QR Code.

A emissão ocorrerá uma vez para a decisão de aprovação descrita. A credencial resultante poderá ser reapresentada enquanto estiver dentro da janela de validade. Solicitação, aprovação, emissão, obtenção do payload e apresentação física permanecerão como eventos distintos.

### 4.1 Proposta da figura F5-03

A figura F5-03 foi autorizada condicionalmente no passo 8. Após examinar o código, a recomendação é **incluí-la**, pois ela esclarece a separação entre o solicitante, o responsável e a emissão automática feita pela API.

O diagrama de sequência terá apenas cinco participantes:

1. solicitante;
2. aplicação web;
3. API;
4. banco MySQL;
5. responsável pela instituição.

Ele será dividido visualmente em duas etapas: **solicitação** e **decisão com emissão**. Não mostrará cadastro da estrutura, detalhes do payload, firmware ou circuito. O QR Code aparecerá somente como resultado disponibilizado pela aplicação, sem antecipar seu formato interno.

## 5. Fronteira real de proteção encontrada no código

A arquitetura pretende manter o segredo criptográfico dentro do backend e da tranca. O commit final examinado, porém, não cumpre integralmente essa fronteira. O texto da tese não poderá sugerir que todas as rotas estão protegidas ou que o segredo permanece confidencial na implementação atual.

Foram identificados os seguintes pontos:

1. as rotas administrativas sob `/admin` exigem JWT e verificam a propriedade contextual;
2. as rotas de perfil e de criação/consulta das próprias solicitações também exigem JWT;
3. listagens gerais de usuários, instituições, edifícios, salas e trancas são públicas;
4. as consultas de credenciais por usuário ou por identificador são públicas e devolvem o payload;
5. as respostas públicas de trancas serializam e devolvem `secret_key` em hexadecimal;
6. a criação direta e a marcação de uso de credenciais possuem rotas sem dependência de autenticação;
7. no frontend, a verificação de acesso às páginas testa a presença de um token no `localStorage`; a validação criptográfica efetiva acontece apenas quando uma rota protegida é chamada.

O item 5 é especialmente material: se o segredo de uma tranca for exposto, uma pessoa pode produzir tags AES-CMAC válidas para aquela tranca. A Seção 5.3.2 registrará de modo conciso que a cobertura de autenticação é parcial. As consequências para o modelo de ameaça, a impossibilidade de alegar proteção efetiva do segredo e as correções necessárias serão desenvolvidas na Seção 5.6.2 e consolidadas como limitação do protótipo.

Também será registrada a divergência semântica da interface que classifica como inativa uma credencial com `used = 1`, embora a política final permita reapresentações dentro da validade. Esse estado pertence ao mecanismo legado do servidor e não será usado para definir a política de autorização do FLIKE.

## 6. Fontes e citações

| Afirmação | Fonte prevista |
| --- | --- |
| organização concreta da API, rotas e repositórios | backend `e9268cc...` |
| JWT como formato de declarações entre partes | RFC 7519 |
| HS256, `user_id` e duração de uma hora | implementação de `jwt_token.py` |
| autorização pelo proprietário da instituição | rotas administrativas e consultas dos repositórios |
| padrão de 24 horas após aprovação | `DEFAULT_KEY_VALIDITY` e rota de aprovação |
| estrutura da interface e fluxos | frontend `9005601...` |
| fluxo completo demonstrado | relato aprovado da equipe e contratos presentes nos dois commits |
| limitações de proteção | dependências de autenticação e serializadores das rotas examinadas |

As características gerais do FastAPI e do Next.js já foram citadas na Seção 5.2.3 e não receberão citações redundantes. A RFC 7519 será conferida e inserida no BibTeX somente durante a redação aprovada deste bloco.

## 7. Limites editoriais

O bloco não irá:

- mencionar as páginas HTML antigas;
- apresentar `admin` como classe global de pessoa;
- detalhar os 48 bytes da credencial, o AES-CMAC ou a versão do QR Code antes da Seção 5.4;
- afirmar persistência offline ou download dedicado da imagem;
- tratar a existência do token no navegador como prova de autorização;
- esconder rotas públicas ou a exposição do segredo encontrada no código;
- antecipar que todas as limitações foram corrigidas;
- transformar nomes ruins de funções ou rotas em tema da tese quando não afetam o comportamento.

## 8. Portão de saída

Antes de alterar a tese, a equipe deve validar:

1. a divisão do bloco nas Seções 5.3.2, 5.3.3 e 5.3.4;
2. a explicação do backend por responsabilidades, sem inventário exaustivo de endpoints;
3. a descrição do padrão de validade como 24 horas contadas da aprovação e emissão;
4. o comportamento atual da interface, que escolhe a primeira tranca retornada para a sala;
5. a inclusão da figura F5-03 com cinco participantes e somente as etapas de solicitação, decisão e emissão;
6. o registro explícito da proteção parcial das rotas e da exposição de `secret_key`;
7. o tratamento de `used` como semântica legada incompatível com reapresentações durante a validade;
8. a inserção da RFC 7519 no parágrafo que define o JWT.

As oito decisões e a implementação resultante foram aprovadas pela equipe em 01/09/2026. As Seções 5.3.2, 5.3.3 e 5.3.4 e a Figura 3 estão concluídas.
