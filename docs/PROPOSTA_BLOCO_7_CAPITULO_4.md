# FLIKE — proposta do bloco 7 do Capítulo 4

**Estado:** aprovado pela equipe após revisão do PDF

**Rodada:** Fase B, passo 6, bloco 7

**Data:** 01/09/2026

**Progresso global:** 6 de 26 passos concluídos (23,1%)

## 1. Finalidade do bloco

Este bloco completará os requisitos não funcionais com a responsividade da aplicação web e substituirá os três enunciados legados de acessibilidade, todos identificados como `REQ-FUNC-01`, por quatro critérios únicos e verificáveis.

Esses requisitos foram derivados pela equipe a partir do problema que motivou o projeto e de referências sobre acessibilidade. Como não houve avaliação com participantes, eles expressam intenções técnicas do projeto. Seu atendimento não permitirá afirmar que o FLIKE reduziu efetivamente sobrecarga cognitiva, constrangimento ou estímulos sensoriais para pessoas autistas.

## 2. Responsividade e acessibilidade não são sinônimos

A responsividade garante que as funções permaneçam utilizáveis em telas com dimensões diferentes. Ela não demonstra, isoladamente, acessibilidade: uma página pode adaptar seu layout e ainda apresentar problemas de teclado, foco, contraste, semântica ou compreensão.

RNF-04 será limitado à preservação de conteúdo e controles essenciais em larguras representativas de celular e computador. Os valores exatos dos viewports e o roteiro serão definidos no protocolo de avaliação, sem transformar dimensões arbitrárias em requisito de produto.

## 3. Requisito não funcional proposto

### RNF-04 — Responsividade da aplicação web

**Enunciado:** a aplicação web deve manter suas funções principais utilizáveis em telas representativas de celular e computador, sem perda de conteúdo ou de controles essenciais.

**Justificativa:** solicitação, acompanhamento, decisão e consulta do QR Code podem ocorrer em dispositivos diferentes. A adaptação do layout deve preservar a execução desses fluxos, sem exigir um aplicativo móvel separado.

**Critério de verificação:** executar cadastro, autenticação, solicitação, decisão administrativa e consulta da credencial nos viewports definidos para celular e computador; confirmar que textos e controles essenciais permanecem visíveis, acionáveis e sem sobreposição.

## 4. Requisitos de acessibilidade propostos

### RA-01 — Entrada sem interação humana obrigatória

**Enunciado:** depois de receber uma credencial válida, o usuário deve conseguir apresentá-la e obter o destravamento sem interação obrigatória com funcionários no momento da entrada.

**Justificativa:** o FLIKE foi concebido para eliminar a necessidade de negociar presencialmente a liberação de uma chave no momento de usar o espaço. O requisito começa depois da emissão da credencial: a solicitação inicial ainda depende da decisão do responsável pela instituição.

**Critério de verificação:** com uma credencial previamente aprovada e disponível, executar sua apresentação, a decisão local e o destravamento sem intervenção de funcionário, contato com portaria ou consulta ao servidor.

### RA-02 — Comunicação textual dos estados

**Enunciado:** a aplicação web deve comunicar por texto os estados de carregamento, sucesso e erro e a situação das solicitações e credenciais, sem depender exclusivamente de cor.

**Justificativa:** rótulos textuais tornam o estado explícito e evitam que uma diferença cromática seja o único meio de transmitir informação. O eMAG recomenda que cor e outras características sensoriais não sejam usadas isoladamente para comunicar conteúdo, e que erros e orientações sejam apresentados de forma clara.

**Critério de verificação:** percorrer os fluxos principais e provocar estados de carregamento, sucesso e erro; verificar mensagens textuais correspondentes; e confirmar que `pending`, `approved`, `rejected`, credencial válida e credencial expirada podem ser distinguidos sem interpretar apenas cores.

### RA-03 — Sequência previsível da solicitação

**Enunciado:** o fluxo de solicitação deve apresentar instituição, edifício, sala, tranca e estado do pedido em uma sequência previsível e identificada.

**Justificativa:** a seleção progressiva explicita o contexto e o destino da solicitação. Estudos com adultos autistas relacionam previsibilidade, informação antecipada e flexibilidade de comunicação à acessibilidade de espaços públicos; essa referência orienta a decisão, mas não comprova efeito do FLIKE sobre seus usuários.

**Critério de verificação:** percorrer o fluxo desde a escolha da instituição até o acompanhamento do pedido; verificar ordem e rótulos das etapas, seleção explícita da tranca, confirmação da solicitação, retorno de erro e apresentação posterior do estado.

### RA-04 — Ausência de feedback sensorial acessório

**Enunciado:** o protótipo físico não deve utilizar alarmes sonoros, música ou luzes intermitentes como feedback de acesso.

**Justificativa:** esses estímulos não são necessários para a função principal e podem aumentar a carga sensorial. Permanecem fora dessa proibição a iluminação necessária para a câmera e o ruído inerente ao relé e à fechadura elétrica; o projeto não alega que esses estímulos inevitáveis sejam confortáveis ou tenham sido avaliados com usuários.

**Critério de verificação:** inventariar os sinais produzidos durante inicialização, espera, leitura, aceitação e rejeição; confirmar a ausência de alarmes, música e luz intermitente usada como feedback; e identificar separadamente iluminação funcional e ruído eletromecânico inevitável.

## 5. Fontes e limites das alegações

O texto utilizará o eMAG como referência técnica brasileira para feedback textual, uso não exclusivo de cor e necessidade de avaliação manual. A pesquisa de MacLennan et al. sustentará a relevância de previsibilidade e informação antecipada para a motivação de RA-03.

Nenhuma dessas fontes autoriza declarar conformidade integral com eMAG ou WCAG. Também não substitui teste com pessoas autistas ou outras pessoas com deficiência. A futura matriz poderá classificar cada requisito por inspeção técnica, preservando a ausência de validação humana.

## 6. Figura ou diagrama

Não se propõe figura nem espaço reservado. Os requisitos tratam de comportamento e critérios de inspeção e não dependem de uma representação visual adicional. Capturas de tela poderão ser consideradas somente no capítulo de avaliação, caso existam e ajudem a documentar resultados específicos.

## 7. Portão de saída

Antes de implementar o bloco 7 na tese, a equipe deve decidir:

1. **aprovado em 01/09/2026:** inserir RNF-04 sem fixar dimensões de viewport no enunciado;
2. **aprovado em 01/09/2026:** inserir RA-01 com a fronteira posterior à emissão da credencial;
3. **aprovado em 01/09/2026:** inserir RA-02 e RA-03 com feedback textual, uso não exclusivo de cor e sequência explícita até a tranca;
4. **aprovado em 01/09/2026:** inserir RA-04, proibindo alarmes, música e luzes intermitentes e ressalvando iluminação da câmera e ruído eletromecânico;
5. **aprovado em 01/09/2026:** escrever o bloco sem figura nem espaço reservado.

As cinco decisões foram aprovadas. O bloco 7 foi implementado, compilado, inspecionado visualmente e aprovado pela equipe após revisão do PDF.
