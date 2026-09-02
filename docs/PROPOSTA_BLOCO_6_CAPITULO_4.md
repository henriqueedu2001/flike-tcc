# FLIKE — proposta do bloco 6 do Capítulo 4

**Estado:** aprovado pela equipe após revisão do PDF

**Rodada:** Fase B, passo 6, bloco 6

**Data:** 01/09/2026

**Progresso global:** 6 de 26 passos concluídos (23,1%)

## 1. Finalidade do bloco

Este bloco encerrará o catálogo funcional com a consulta administrativa de credenciais e acrescentará duas restrições de segurança aplicáveis às operações web e ao segredo criptográfico das trancas. Ele não tratará logs de entrada, saída ou ocupação, porque o FLIKE não possui sensores nem evidência capaz de produzir esses eventos físicos.

Com a exclusão do requisito autônomo de acionamento, a consulta administrativa será numerada como RF-14. O número mantém o catálogo funcional contínuo; o conteúdo excluído não será reaproveitado sob outro nome.

## 2. Consulta administrativa: o que o histórico representa

O responsável precisa consultar as credenciais emitidas no contexto das instituições que administra. Essa visão pode mostrar o usuário ao qual cada credencial foi atribuída, sua tranca destinatária e seus instantes de emissão e expiração. Ela representa um **histórico de emissões e autorizações concedidas**.

Esse histórico não será apresentado como registro de abertura da porta ou presença no espaço. A emissão comprova que o sistema criou uma credencial depois de uma aprovação; não comprova que o QR Code foi apresentado. Mesmo um registro de autorização produzido pela tranca demonstraria uma decisão positiva do dispositivo, mas não provaria abertura física, entrada, saída ou identidade da pessoa presente.

## 3. Requisito funcional proposto

### RF-14 — Consulta administrativa de credenciais

**Enunciado:** o responsável deve poder consultar os usuários que receberam credenciais e o histórico de credenciais emitidas para as trancas das instituições que administra.

**Justificativa:** a consulta permite acompanhar as autorizações concedidas dentro do escopo administrativo do proprietário sem transformá-las em evidência de acesso físico. O resultado precisa preservar os vínculos entre usuário, tranca e período autorizado.

**Critério de verificação:** emitir credenciais para trancas pertencentes a duas instituições com proprietários distintos; confirmar que cada responsável consulta somente os registros de sua instituição; verificar usuário, tranca, emissão e expiração; e confirmar que a interface não rotula a emissão como entrada, saída ou ocupação.

## 4. Requisitos não funcionais propostos

### RNF-02 — Autenticação e autorização administrativa

**Enunciado:** operações administrativas e decisões sobre solicitações devem exigir autenticação e respeitar a propriedade da instituição envolvida.

**Justificativa:** o papel administrativo é contextual. Estar autenticado não autoriza um usuário a administrar instituições de terceiros, e nenhuma operação administrativa sensível deve ser executada anonimamente.

**Critério de verificação:** para cada operação administrativa e decisão de solicitação, executar chamadas como proprietário, como usuário autenticado sem propriedade e sem autenticação; confirmar sucesso somente para o proprietário correto.

### RNF-03 — Não exposição do segredo da tranca

**Enunciado:** o segredo AES-CMAC associado a cada tranca não deve ser exposto a usuários, respostas da API ou registros da aplicação.

**Justificativa:** quem conhece o segredo pode calcular tags aceitas como autênticas pela tranca. O valor deve permanecer restrito ao servidor e ao dispositivo provisionado, conforme a premissa criptográfica do projeto. Esse requisito trata de exposição pelas interfaces do sistema; armazenamento seguro, rotação e provisionamento permanecem limitações e decisões arquiteturais próprias.

**Critério de verificação:** inspecionar respostas de cadastro, consulta e alteração de trancas, mensagens de erro e registros produzidos pela aplicação; confirmar que o segredo não aparece em nenhum desses canais destinados a usuários ou operadores comuns.

## 5. Relação com a implementação

O Capítulo 4 enunciará os comportamentos e as restrições sem antecipar seu estado de atendimento. A matriz de rastreabilidade registrará separadamente que existem consultas administrativas no frontend e no backend, mas seus contratos apresentam divergências, e que a versão examinada da API pode serializar o segredo da tranca em respostas. Assim, RNF-03 continuará sendo um requisito válido mesmo que a implementação preservada não o atenda.

O texto também distinguirá **credencial emitida**, **apresentação**, **autorização**, **sinal de acionamento**, **abertura**, **entrada**, **saída** e **ocupação**. O RF-14 cobrirá somente o primeiro desses elementos.

## 6. Figura ou diagrama

Não se propõe figura nem espaço reservado. A fronteira entre emissão e evento físico será explicada em texto, pois um diagrama acrescentaria pouco a este bloco curto. Uma eventual matriz de permissões será considerada posteriormente como quadro textual, não como figura, e somente se ajudar a matriz de rastreabilidade.

## 7. Portão de saída

Antes de implementar o bloco 6 na tese, a equipe deve decidir:

1. **aprovado em 01/09/2026:** reutilizar RF-14 para a consulta administrativa e manter a numeração contínua;
2. **aprovado em 01/09/2026:** limitar o histórico administrativo a credenciais emitidas e autorizações concedidas, sem alegar eventos físicos;
3. **aprovado em 01/09/2026:** inserir RNF-02, exigindo autenticação e propriedade para operações administrativas e decisões de solicitação;
4. **aprovado em 01/09/2026:** inserir RNF-03, proibindo a exposição do segredo em interfaces, respostas e registros da aplicação;
5. **aprovado em 01/09/2026:** escrever o bloco sem figura nem espaço reservado.

As cinco decisões foram aprovadas. O bloco 6 foi implementado, compilado e inspecionado visualmente e aguarda revisão da equipe.
