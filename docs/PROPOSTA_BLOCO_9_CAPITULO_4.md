# FLIKE — proposta do bloco 9 do Capítulo 4

**Estado:** aprovado pela equipe após revisão da tese compilada

**Rodada:** Fase B, passo 6, bloco 9

**Data:** 01/09/2026

**Progresso global:** 6 de 26 passos concluídos (23,1%)

## 1. O que este bloco contém

O bloco 9 encerrará o Capítulo 4 com a **Seção 4.8 — Rastreabilidade para verificação**. Ele relacionará individualmente os 23 requisitos consolidados — RF-01 a RF-14, RNF-01 a RNF-05 e RA-01 a RA-04 — à origem de cada decisão e à evidência necessária para avaliá-la.

O bloco também incluirá um fechamento curto do capítulo. Esse texto distinguirá o que foi especificado do que já foi demonstrado e encaminhará a descrição da implementação e das evidências para o Capítulo 5.

## 2. Separação entre especificação e resultado

O Capítulo 4 define comportamentos, restrições e critérios de verificação. Ele não deve declarar um requisito atendido somente porque existe código relacionado, porque a equipe relatou um teste ou porque foi escrito um critério plausível.

Por isso, a matriz deste bloco não usará ainda os estados `atendido`, `parcialmente atendido`, `não atendido` e `não avaliado`. Esses estados dependem do inventário técnico do passo 7 e dos protocolos e resultados dos passos 14 a 16. A matriz final de atendimento será apresentada na avaliação, confrontando cada requisito com evidência efetivamente disponível.

Nesta etapa, a rastreabilidade terá duas direções:

1. **origem → requisito:** mostra por que o requisito entrou no catálogo;
2. **requisito → verificação planejada:** mostra qual evidência será necessária para decidir posteriormente seu atendimento.

## 3. Organização proposta para a Seção 4.8

A seção começará com um parágrafo apoiado pela ISO/IEC/IEEE 29148 sobre identificação única, verificabilidade e rastreabilidade. Em seguida, apresentará quatro quadros textuais:

1. **RF-01 a RF-08 — aplicação web e fluxo de autorização;**
2. **RF-09 a RF-14 — credencial, decisão local e consulta administrativa;**
3. **RNF-01 a RNF-05 — restrições operacionais e técnicas;**
4. **RA-01 a RA-04 — critérios de acessibilidade definidos pela equipe.**

Cada linha corresponderá a um requisito, sem agrupar identificadores. Os quadros terão três colunas:

| Coluna | Função |
| --- | --- |
| **ID** | Permitir localizar sem ambiguidade o requisito no catálogo. |
| **Origem** | Registrar o problema, decisão de projeto, artefato implementado ou referência que motivou o requisito. |
| **Evidência necessária** | Resumir o teste, inspeção ou registro que permitirá avaliar seu atendimento. |

O critério de verificação completo não será repetido. Ele continuará junto do enunciado de cada requisito; a terceira coluna apenas apontará a família de evidência correspondente.

## 4. Conteúdo proposto dos quadros

### 4.1 RF-01 a RF-08 — aplicação web e fluxo de autorização

| ID | Origem resumida | Evidência necessária |
| --- | --- | --- |
| RF-01 | Fluxo implementado de identidade e necessidade de associar operações a contas. | Cadastro, autenticação, rejeição de credenciais incorretas e acesso a operação protegida. |
| RF-02 | Modelo contextual no qual a propriedade da instituição define a responsabilidade administrativa. | Cenário com duas contas e instituições próprias e alheias. |
| RF-03 | Modelo hierárquico implementado e necessidade de identificar os recursos físicos administrados. | Operações da hierarquia e tentativas autorizadas e não autorizadas. |
| RF-04 | Decisão de associar cada solicitação e credencial a uma única tranca lógica. | Sala com múltiplas trancas e confirmação do destino escolhido. |
| RF-05 | Fluxo de solicitação definido pela equipe para substituir a retirada informal de chaves. | Criação de pedido, acompanhamento dos três estados e isolamento entre usuários. |
| RF-06 | Responsabilidade do proprietário da instituição sobre pedidos destinados às suas trancas. | Aprovação e rejeição pelo proprietário e bloqueio de terceiros. |
| RF-07 | Política de uma credencial por solicitação aprovada. | Emissão após aprovação, ausência após rejeição e inexistência de emissão duplicada. |
| RF-08 | Necessidade de o titular obter e apresentar a credencial emitida. | Consulta do próprio QR Code durante a validade e bloqueio para outra conta. |

### 4.2 RF-09 a RF-14 — credencial, decisão local e consulta administrativa

| ID | Origem resumida | Evidência necessária |
| --- | --- | --- |
| RF-09 | Protocolo final de autorização temporal para usuário e tranca identificados. | Decodificação e comparação dos quatro dados da autorização. |
| RF-10 | Necessidade de detectar fabricação ou alteração sem consulta ao servidor; AES-CMAC conforme NIST. | Vetor válido e adulteração individual de cada campo protegido. |
| RF-11 | Transporte binário pelo QR Code e restrições observadas na leitura embarcada. | Comparação byte a byte, incluindo bytes nulos e superiores a `0x7f`. |
| RF-12 | Arquitetura de decisão local e necessidade de combinar estrutura, autenticação, destino e validade. | Casos válidos e inválidos para cada condição da decisão. |
| RF-13 | Política de credencial temporária reutilizável durante a janela concedida. | Reapresentação e testes antes da emissão, na expiração e depois dela. |
| RF-14 | Fluxo administrativo implementado para acompanhar autorizações concedidas. | Consultas cruzadas entre instituições e conferência dos dados exibidos. |

### 4.3 RNF-01 a RNF-05 — restrições operacionais e técnicas

| ID | Origem resumida | Evidência necessária |
| --- | --- | --- |
| RNF-01 | Decisão arquitetural de manter a autorização disponível sem comunicação da tranca com a API. | Execução de leitura, decisão e acionamento com o dispositivo sem rede. |
| RNF-02 | Modelo de responsabilidade contextual e proteção das operações administrativas. | Matriz proprietário, usuário sem propriedade e chamada anônima. |
| RNF-03 | Premissa de segurança do AES-CMAC e recomendações de proteção do segredo. | Inspeção de respostas, erros e registros produzidos pela aplicação. |
| RNF-04 | Uso da aplicação web em celular e computador sem aplicativo móvel nativo. | Execução dos fluxos principais em viewports representativos. |
| RNF-05 | Decisão experimental de limitar a densidade óptica a QR Code versão 3-L. | Inspeção da matriz e dos parâmetros do símbolo e leitura pela ESP32-CAM. |

### 4.4 RA-01 a RA-04 — acessibilidade definida pela equipe

| ID | Origem resumida | Evidência necessária |
| --- | --- | --- |
| RA-01 | Problema relatado de dependência de funcionários para obter acesso à sala. | Fluxo posterior à emissão executado sem intervenção humana. |
| RA-02 | Decisão de projeto apoiada pelo eMAG sobre comunicação textual e uso não exclusivo de cor. | Inspeção dos estados, mensagens e distinções sem interpretação cromática. |
| RA-03 | Fluxo progressivo da interface e literatura sobre previsibilidade e informação antecipada. | Inspeção da sequência completa, dos rótulos e dos retornos ao usuário. |
| RA-04 | Decisão da equipe de evitar feedback sensorial acessório no protótipo físico. | Inventário dos sinais durante inicialização, leitura, aceitação e rejeição. |

## 5. Fechamento proposto do Capítulo 4

Depois dos quadros, um parágrafo esclarecerá que:

- os requisitos representam o contrato técnico adotado pela equipe;
- a origem em código ou relato não equivale a atendimento demonstrado;
- o Capítulo 5 descreverá os componentes e a integração realizados;
- a avaliação posterior confrontará critérios e evidências e atribuirá o estado de cada requisito;
- requisitos de acessibilidade continuarão classificados como decisões técnicas não validadas com participantes.

Com a aprovação desse fechamento, o passo 6 poderá ser concluído depois que a Seção 4.8 for implementada, compilada e aprovada na tese.

## 6. Referências

A introdução da seção usará a ISO/IEC/IEEE 29148 como referência metodológica para requisitos verificáveis, identificação única e rastreabilidade. NIST, eMAG, MacLennan et al. e DENSO continuarão citados nos trechos em que sustentam decisões específicas; os quadros poderão remeter aos requisitos sem repetir chamadas bibliográficas em todas as linhas.

Nenhuma fonte será usada para afirmar que o FLIKE atende a um requisito. Atendimento dependerá de evidência própria do projeto.

## 7. Figura, diagrama e quadros

Não se propõe figura, diagrama nem espaço reservado. Os quatro quadros são a própria matriz de rastreabilidade e serão produzidos diretamente em LaTeX. Eles poderão continuar em mais de uma página se isso for necessário para preservar legibilidade, sem converter a matriz em imagem.

## 8. Portão de saída

Antes de implementar o bloco 9 — matriz de rastreabilidade e fechamento do Capítulo 4 — a equipe deve decidir:

1. **aprovado em 01/09/2026:** criar a Seção 4.8 com rastreabilidade entre origem, requisito e evidência necessária;
2. **aprovado em 01/09/2026:** manter uma linha por requisito e dividir a matriz nos quatro quadros propostos;
3. **aprovado em 01/09/2026:** não repetir os critérios completos nos quadros;
4. **aprovado em 01/09/2026:** adiar a classificação `atendido`, `parcialmente atendido`, `não atendido` ou `não avaliado` para os passos de avaliação;
5. **aprovado em 01/09/2026:** usar o fechamento que encaminha implementação e evidências ao Capítulo 5;
6. **aprovado em 01/09/2026:** escrever o bloco sem figura, diagrama ou espaço reservado.

As seis decisões foram aprovadas pela equipe em 01/09/2026. A Seção 4.8 foi implementada conforme este portão, compilada, inspecionada visualmente e aprovada pela equipe. Com essa aprovação, o passo 6 foi concluído.
