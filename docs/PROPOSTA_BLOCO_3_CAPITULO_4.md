# FLIKE — proposta do bloco 3 do Capítulo 4

**Estado:** aprovado pela equipe

**Rodada:** Fase B, passo 6, bloco 3

**Data:** 01/09/2026

## 1. Objetivo e limite da rodada

O bloco 3 tratará do fluxo que começa na escolha da tranca e termina na disponibilização da credencial ao solicitante. Ele substituirá parte do conteúdo legado do Capítulo 4 pelos requisitos **RF-04 a RF-08**, já aprovados no passo 5:

1. identificação da tranca destinatária;
2. criação e acompanhamento da solicitação;
3. decisão pelo responsável da instituição;
4. emissão de uma credencial por solicitação aprovada;
5. consulta e apresentação do QR Code pelo usuário.

O escopo e o mapa de fontes abaixo foram autorizados pela equipe em 01/09/2026. A implementação da rodada está registrada na Seção 9.

Não integrarão este bloco:

- o layout de 48 bytes e o AES-CMAC, que formarão o bloco seguinte com RF-09;
- leitura, validação local, janela temporal e acionamento físico, tratados em RF-10 a RF-13;
- consultas administrativas sobre credenciais e portadores, tratadas em RF-14;
- responsividade, segurança, proteção do segredo e acessibilidade, reservadas aos requisitos RNF e RA;
- a matriz de atendimento, que será consolidada depois do catálogo completo.

## 2. Estrutura proposta

### 2.1 Subseção “Solicitação e decisão de acesso”

Um parágrafo introdutório explicará que o FLIKE converte a obtenção do acesso em um fluxo explícito e consultável. A escolha foi feita pela equipe para tornar o processo mais previsível e reduzir a necessidade de negociação presencial no momento da entrada. A literatura será usada somente para mostrar que previsibilidade, informação antecipada e alternativas à comunicação falada podem ser relevantes para algumas pessoas autistas; o texto preservará expressamente que esse efeito não foi avaliado no FLIKE.

Em seguida serão apresentados:

- **RF-04 — Identificação da tranca destinatária**;
- **RF-05 — Solicitação e acompanhamento**;
- **RF-06 — Decisão pelo responsável**.

### 2.2 Subseção “Emissão e apresentação da credencial”

O texto distinguirá a decisão administrativa da criação da credencial. Aprovar gera uma credencial; rejeitar não gera. A credencial ficará associada ao usuário e à tranca da solicitação. A expressão “uma credencial por solicitação” será preservada sem sugerir uso único: a credencial aprovada poderá ser reapresentada durante a sua janela de validade, conforme RF-12.

Em seguida serão apresentados:

- **RF-07 — Emissão condicionada à aprovação**;
- **RF-08 — Consulta e apresentação da credencial**.

## 3. Redação-base dos requisitos

### RF-04 — Identificação da tranca destinatária

**Enunciado:** toda solicitação de acesso deve identificar exatamente uma tranca digital destinatária.

**Justificativa:** a credencial é autenticada para uma tranca, não genericamente para uma sala. A identificação explícita evita que o sistema escolha silenciosamente um atuador quando uma sala possuir mais de uma tranca.

**Critério de verificação:** criar uma solicitação e confirmar o identificador da tranca selecionada; em sala com várias trancas, exigir escolha explícita e verificar que a solicitação preserva essa escolha.

### RF-05 — Solicitação e acompanhamento

**Enunciado:** o usuário autenticado deve poder solicitar uma credencial para uma tranca e acompanhar o estado `pending`, `approved` ou `rejected` da solicitação.

**Justificativa:** o estado torna visível se o pedido aguarda decisão, foi aceito ou foi recusado. A consulta deve estar disponível ao solicitante e não pressupõe que a aprovação seja automática.

**Critério de verificação:** submeter uma solicitação autenticada; consultar o pedido na conta que o criou; observar as três transições previstas; e impedir que outro solicitante altere o estado.

### RF-06 — Decisão pelo responsável

**Enunciado:** o responsável pela instituição destinatária deve poder consultar e aprovar ou rejeitar solicitações pendentes.

**Justificativa:** a autorização administrativa pertence ao usuário proprietário da instituição à qual a tranca está vinculada. Um papel global de administrador não faz parte do domínio.

**Critério de verificação:** confirmar que o proprietário correto visualiza e decide o pedido uma única vez; que usuário sem propriedade não consegue decidi-lo; e que uma solicitação já decidida não retorna ao estado pendente por repetição da operação.

### RF-07 — Emissão condicionada à aprovação

**Enunciado:** cada solicitação aprovada deve gerar uma credencial digital, enquanto uma solicitação rejeitada não deve gerar credencial.

**Justificativa:** a credencial materializa a autorização concedida e precisa manter relação inequívoca com o pedido, o usuário e a tranca destinatária. A redação define o comportamento esperado mesmo que a implementação atual ainda possua lacunas de atomicidade e relacionamento no banco.

**Critério de verificação:** comparar solicitações e credenciais antes e depois de aprovar e rejeitar pedidos; verificar a existência de exatamente uma credencial para a aprovação e nenhuma para a rejeição; e confirmar os vínculos com solicitante e tranca.

### RF-08 — Consulta e apresentação da credencial

**Enunciado:** o usuário deve poder consultar suas credenciais emitidas e apresentar o QR Code correspondente durante a janela de validade.

**Justificativa:** depois da aprovação, o titular precisa recuperar a representação visual usada pela tranca. O requisito permite exibição persistente no painel, download para o aparelho ou solução equivalente, desde que a credencial permaneça acessível durante sua vigência. Ele não exige aplicativo móvel e não implica funcionamento offline da aplicação web.

**Critério de verificação:** autenticar o solicitante após a aprovação; recuperar a credencial emitida; renderizar o QR Code correto; confirmar sua disponibilidade durante a janela; e impedir que outra conta consulte a credencial sem autorização.

## 4. Mapa de afirmações, fontes e evidências

| Afirmação planejada | Sustentação | Inserção prevista | Limite editorial |
| --- | --- | --- | --- |
| Previsibilidade, informação antecipada e comunicação flexível podem influenciar a acessibilidade de espaços públicos para alguns adultos autistas. | MacLennan et al. (2023), seções “Predictability” e “Inflexible communication”, chave `maclennan2023sensory`. | Parágrafo introdutório do bloco 3. | Não afirmar que o FLIKE produziu esses benefícios; não generalizar a toda pessoa autista. |
| O FLIKE transformou a obtenção do acesso em solicitação, decisão e consulta digital. | Requisitos aprovados, modelo de dados, frontend, backend e relato da equipe. | Introdução e RF-04 a RF-08. | É descrição e decisão do projeto; não recebe citação bibliográfica externa. |
| Cada solicitação se destina a uma tranca, e não genericamente à sala. | Decisão P5, entidade `digital_lock` e payload implementado. | RF-04 e RF-07. | Evidência de projeto; a atual escolha implícita da primeira tranca será classificada como atendimento parcial. |
| O responsável decorre da propriedade da instituição. | Modelo de autorização implementado e decisão aprovada sobre administração contextual. | RF-06. | Não inventar papel global ou múltiplos administradores por instituição. |
| Uma aprovação gera uma credencial e uma rejeição não gera. | Fluxo do backend e política final de uma credencial por solicitação. | RF-07. | O requisito esperado não oculta as lacunas atuais de atomicidade e chave estrangeira. |
| O usuário precisa de internet para solicitar, acompanhar e obter inicialmente o QR Code. | Fronteira arquitetural aprovada e comportamento do frontend/API. | RF-05, RF-08 e remissão à seção de escopo. | “Offline” continua restrito à decisão da tranca. |
| Exibição no painel, download ou solução equivalente são alternativas aceitáveis de disponibilidade. | Promessa aprovada do produto e estado atual da interface. | Justificativa de RF-08. | Não afirmar que download ou persistência dedicada já foram implementados. |
| A credencial pode ser reapresentada durante sua vigência. | Política aprovada P6 e RF-12. | Remissão curta em RF-07/RF-08. | Não usar “uso único”; a verificação temporal pertence ao bloco de RF-11/RF-12. |

## 5. Auditoria de citações dos blocos 1 e 2

A primeira auditoria identificou três pontos que deverão receber fontes quando o bloco 3 for redigido. Essas inserções não alteram as decisões de conteúdo já aprovadas:

| Trecho atual | Fonte a inserir | Função da citação |
| --- | --- | --- |
| Origem dos requisitos e escolha de reduzir interação presencial e aumentar previsibilidade. | MacLennan et al. (2023), `maclennan2023sensory`. | Mostrar que a direção de projeto é coerente com experiências relatadas por adultos autistas, sem alegar validação do FLIKE. |
| Impossibilidade de revogar imediatamente uma credencial ainda válida em dispositivo sem atualizações. | Ho et al. (2016), `ho2016smartlocks`, seção 3.3. | Sustentar o compromisso geral entre operação desconectada e consistência do estado de autorização. |
| A apresentação do QR e o acionamento não provam autoria pessoal, entrada ou ocupação. | Dworkin (2005), `nist2005cmac`; Barker (2020), `barker2020keymanagement`; Kieseberg et al. (2010), `kieseberg2010qrcode`. | Distinguir autenticação do payload, segredo simétrico, possibilidade de cópia e evento físico não observado. |

Os seguintes trechos não precisam de citação externa:

- relato do autor, reunião institucional e relatos informais, pois serão identificados como origem declarada pela equipe;
- enumeração do escopo e das propostas abandonadas;
- definição dos atores e entidades do domínio;
- política de uma credencial por solicitação;
- requisitos RF-01 a RF-08 e respectivos critérios, pois são requisitos concebidos pelos autores;
- estados de atendimento, que deverão apontar para código, banco, demonstração ou teste em vez de literatura.

## 6. Alterações bibliográficas previstas

Na redação do bloco, as entradas efetivamente citadas foram integradas a `FLIKE/referencias/abntex2-modelo-references.bib`. A compilação confirmou:

1. ausência de chaves indefinidas;
2. formatação pelo estilo ABNT já usado no projeto;
3. citação no mesmo parágrafo da afirmação sustentada;
4. nenhuma obra presente apenas na bibliografia sem chamada no texto.

## 7. Verificação da edição

Depois da autorização desta proposta, a redação do bloco 3 passou por:

1. conferência de RF-04 a RF-08 contra o catálogo aprovado;
2. auditoria das afirmações externas e das citações dos blocos 1 a 3;
3. compilação integral pelo comando `./compile.sh`;
4. inspeção de referências indefinidas, avisos bibliográficos e conteúdo legado remanescente;
5. apresentação do diff e do PDF para revisão da equipe.

## 8. Portão de revisão

Para aprovar a redação produzida, a equipe deve revisar:

1. se RF-04 a RF-08 representam corretamente o fluxo desejado;
2. se exibição no painel, download ou solução equivalente devem continuar aceitos em RF-08;
3. se o mapa distingue adequadamente literatura, decisões dos autores e evidências do projeto.

Com a aprovação desses três pontos no PDF compilado, o bloco 3 poderá ser consolidado e a proposta do bloco seguinte será preparada.

## 9. Registro da implementação

**Data:** 01/09/2026

**Arquivos da tese alterados:**

- `FLIKE/capitulos/Cap4-Especificacao.tex`;
- `FLIKE/referencias/abntex2-modelo-references.bib`;
- `FLIKE/capitulos/Cap6-Consideracoes.tex`, apenas para remover a bibliografia manual legada que duplicava a bibliografia gerada pelo BibTeX.

**Conteúdo produzido:**

- inserção de RF-04 a RF-08, com enunciado, justificativa e critério de verificação;
- criação das subseções “Solicitação e decisão de acesso” e “Emissão e apresentação da credencial”;
- auditoria e inserção das citações necessárias nos blocos 1 a 3;
- integração de cinco entradas bibliográficas efetivamente citadas;
- remoção da segunda seção de referências, que continha entradas manuais antigas e sem chamadas no texto.

**Citações inseridas:**

- `maclennan2023sensory`: previsibilidade, informação antecipada e alternativas à comunicação falada;
- `ho2016smartlocks`: compromisso entre disponibilidade local e consistência de revogação;
- `nist2005cmac` e `barker2020keymanagement`: autenticação de mensagens e premissa de proteção do segredo simétrico;
- `kieseberg2010qrcode`: possibilidade de copiar ou redistribuir a representação em QR Code.

**Verificações executadas:**

- compilação integral por `./compile.sh`, concluída em 6,3 segundos;
- PDF final com 49 páginas e cinco referências bibliográficas, todas citadas no texto;
- nenhuma citação, referência ou chave BibTeX indefinida;
- inspeção visual do Capítulo 4 e da bibliografia sem texto cortado, sobreposição ou referência duplicada;
- um aviso não bloqueante de `Underfull \vbox` próximo a RF-01, sem defeito visual observado.

**Estado da rodada:** aprovado pela equipe em 01/09/2026. O conteúdo legado posterior a RF-08 permanece no capítulo de propósito e será substituído nos próximos blocos do passo 6.
