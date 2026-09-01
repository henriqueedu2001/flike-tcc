# FLIKE — contrato acadêmico do TCC

**Estado:** aprovado pela equipe

**Rodada:** Fase A, passo 3

**Data:** 01/09/2026

## 1. Função deste documento

Este documento fixa o problema acadêmico, a contribuição central, a pergunta de pesquisa, os objetivos, o escopo e as limitações da monografia. Ele será a referência para decidir o que cada capítulo deve demonstrar e para impedir que a redação atribua ao FLIKE resultados que não foram avaliados.

O texto ainda não é conteúdo definitivo da monografia. Suas formulações aprovadas orientam a revisão do vocabulário no passo 4 e, somente depois disso, a reescrita dos capítulos.

## 2. Decisões fornecidas pela equipe

1. Não haverá ampliação funcional do produto. A equipe concluiu a integração e demonstrou ponta a ponta o sistema físico com o protocolo AES-CMAC final. A monografia reconstruirá as evidências disponíveis e poderá executar verificações dos componentes existentes.
2. A aplicação web e a API realizaram, segundo a equipe, o fluxo de cadastro e autenticação, solicitação de acesso, aprovação ou rejeição pelo proprietário e disponibilização da credencial no painel do usuário. O proprietário também conseguia cadastrar edifícios e trancas.
3. A equipe confirmou que o protótipo físico reconheceu o QR Code, decodificou o payload, extraiu seus campos, verificou localmente o autenticador e produziu o sinal elétrico de abertura. O material histórico preservado comprova uma demonstração ponta a ponta com HMAC-SHA1. Em 31/08/2026, um integrante da equipe remontou a maquete e concluiu com sucesso uma nova demonstração ponta a ponta com o protocolo AES-CMAC final e a fechadura conectada.
4. Um estágio de chaveamento e conversão de nível com transistor 2N2222 controlou um módulo de relé de 12 V, cujo contato normalmente aberto aplicou o pulso de alimentação à fechadura elétrica.
5. O relatório, o diagrama, as fotografias e o vídeo do Laboratório de Processadores documentam a montagem e a demonstração histórica. O circuito elétrico é o mesmo adotado na etapa final e recebe do firmware apenas o sinal lógico `HIGH`. As versões exatas do firmware usadas no vídeo histórico e na demonstração final ainda deverão ser identificadas, se possível.
6. O projeto foi motivado pela sala sensorial da Faculdade de Direito da USP, conhecida como Sanfran.
7. Um dos autores é autista e integra o Coletivo Autista da USP (CAUSP). Ele tomou conhecimento do problema em reunião com dirigentes da Faculdade e por relatos informais de colegas sobre dificuldade de acesso, ausência de protocolo e dependência da liberação por funcionários da segurança.
8. Os requisitos foram elaborados pela própria equipe a partir de sua avaliação do cenário. Não houve levantamento formal com usuários, validação sistemática dos requisitos nem avaliação do produto com o público-alvo.
9. Não há retorno substantivo do orientador disponível para sustentar ou restringir o escopo. A redução de escopo deverá permanecer explícita e poderá ser submetida ao orientador posteriormente.
10. A contribuição central escolhida pela equipe é o projeto e a implementação do sistema integrado. A verificação local é seu diferencial técnico, e autonomia e redução de interações obrigatórias constituem a motivação.

### 2.1 Precisão terminológica sobre o mecanismo criptográfico

O mecanismo implementado é o **AES-CMAC**, um código de autenticação de mensagem simétrico. A tese poderá afirmar que ele permite verificar a autenticidade e a integridade do payload a quem possui o segredo compartilhado. Não deverá chamá-lo de assinatura digital, criptografia do conteúdo ou mecanismo de não repúdio.

## 3. Alternativas de enquadramento

### 3.1 Sistema integrado de controle de acesso — escolhida

O objeto principal é o FLIKE como sistema composto por aplicação web, API, banco de dados, formato de credencial, dispositivo embarcado, circuito de acionamento e fechadura elétrica.

**Vantagens:** representa todo o trabalho produzido; permite documentar software, firmware e hardware; acomoda resultados parciais sem transformar uma única característica em toda a contribuição.

**Consequência editorial:** a monografia deverá rastrear cada objetivo até um artefato ou uma evidência e declarar separadamente o que foi projetado, implementado, demonstrado e apenas relatado.

### 3.2 Verificação offline como objeto principal — não escolhida

Essa alternativa concentraria a pergunta na autenticação local da credencial. Ela destacaria o principal diferencial técnico, mas reduziria excessivamente o papel do sistema web e exigiria evidências mais fortes sobre verificação temporal, identidade da tranca, relógio e comportamento diante de ataques.

### 3.3 Impacto sobre acessibilidade e autonomia — não escolhida

Essa alternativa perguntaria se o FLIKE melhorou o acesso à sala sensorial. Ela não é defensável com as evidências existentes, pois não houve implantação, estudo com usuários, linha de base ou medição de impacto. Acessibilidade e autonomia permanecerão como motivação e requisitos de projeto, não como benefícios comprovados.

## 4. Contrato proposto

### 4.1 Tese central

O FLIKE materializa uma arquitetura de controle de acesso físico que combina gestão web de permissões, credenciais temporárias transportadas por QR Code e autenticação criptográfica local no ponto de acesso. O trabalho contribui pela especificação e construção do protótipo integrado e pela análise explícita do que foi alcançado, das lacunas entre a arquitetura pretendida e os artefatos preservados e dos riscos assumidos pela operação sem consulta ao servidor no momento da leitura.

### 4.2 Pergunta de pesquisa

> Como projetar e implementar um protótipo de controle de acesso físico para espaços institucionais compartilhados que integre a gestão web de permissões a credenciais temporárias em QR Code autenticadas localmente por uma tranca eletrônica, sem consulta ao servidor no momento da leitura?

### 4.3 Objetivo geral

Projetar, implementar e documentar tecnicamente o FLIKE, um protótipo de controle de acesso físico que gerencia solicitações e permissões por meio de uma aplicação web e utiliza credenciais temporárias em QR Code autenticadas localmente por um dispositivo baseado em ESP32-CAM para acionar uma fechadura elétrica.

### 4.4 Objetivos específicos

1. Caracterizar o cenário de acesso à sala sensorial que motivou o projeto e explicitar a origem e os limites das informações usadas nessa caracterização.
2. Especificar os requisitos funcionais, não funcionais e de acessibilidade derivados pela equipe para o protótipo.
3. Projetar a arquitetura, o modelo de dados e os fluxos de interação entre usuários, proprietários de instituições, aplicação web, API e trancas.
4. Implementar os fluxos de software para cadastro e autenticação, gestão de instituições, edifícios e trancas, solicitação e decisão de acesso, emissão da credencial e disponibilização do QR Code.
5. Definir e implementar um formato binário de credencial que identifique a tranca e a janela de validade e que seja autenticado por AES-CMAC antes de ser codificado em QR Code.
6. Desenvolver um protótipo embarcado capaz de ler e decodificar o QR Code, verificar localmente sua autenticidade e produzir o sinal necessário para acionar uma fechadura elétrica por meio de um circuito de potência.
7. Confrontar os requisitos e objetivos com o código, a documentação e as demonstrações disponíveis, registrando o nível de realização, as limitações, os riscos e os elementos que não puderam ser reproduzidos ou avaliados.

O sexto objetivo não afirma, por si só, que o firmware preservado verifica a janela temporal ou a identidade da tranca. Essas propriedades serão avaliadas separadamente ao confrontar a arquitetura, o relato da demonstração e o estado do código.

## 5. Escopo incluído

- A sala sensorial da Faculdade de Direito da USP como caso motivador.
- A experiência de um autor e os relatos informais recebidos por ele como origem contextual do problema, identificados como relato e não como estudo empírico.
- O FLIKE como plataforma aplicável a instituições, edifícios, salas e trancas.
- A aplicação web em Next.js/React, a API em FastAPI e a persistência relacional em MySQL.
- O modelo contextual de permissões no qual uma pessoa administra as instituições que possui e solicita acesso às instituições de outras pessoas.
- O fluxo de solicitação, aprovação ou rejeição e emissão de uma credencial por solicitação aprovada.
- A credencial reutilizável durante a janela autorizada e destinada a uma tranca.
- O payload binário de 48 bytes e sua autenticação por AES-CMAC.
- A leitura e a decodificação do QR Code pela ESP32-CAM.
- A implementação final da verificação local por AES-CMAC, distinguida da demonstração física histórica com HMAC-SHA1.
- A geração do sinal elétrico, o estágio com 2N2222, o módulo de relé de 12 V e o acionamento da fechadura Papaiz AA-ERL200P documentados no material histórico.
- A análise técnica do estado preservado dos componentes e da integração.
- A documentação honesta de requisitos atendidos, parcialmente atendidos, não atendidos e não avaliados.

## 6. Escopo excluído

- Desenvolvimento de novas funcionalidades depois da integração física final já concluída.
- Aplicativo móvel, MQTT, gateway, Bluetooth e armazenamento S3.
- Implantação operacional na Faculdade de Direito ou em outra instituição.
- Revogação confiável de uma credencial já emitida antes do término de sua validade.
- Interface de provisionamento, troca ou rotação do segredo da tranca.
- Proteção do segredo em hardware especializado ou análise criptográfica formal.
- Operação offline da aplicação web, da API ou da obtenção inicial do QR Code.
- Identificação de entrada, saída ou ocupação sem sensores adicionais.
- Produto endurecido para produção, certificação ou conformidade integral com normas de segurança, acessibilidade, instalações elétricas ou proteção de dados.
- Avaliação com usuários, estudo de usabilidade com o público-alvo ou comprovação de impacto social.
- Comprovação de redução de constrangimento, sobrecarga cognitiva, subutilização da sala, furtos ou interações humanas obrigatórias.

## 7. Limitações que deverão aparecer na monografia

1. **Origem dos requisitos:** os requisitos foram derivados pela equipe com base na experiência de um autor, em uma reunião institucional e em relatos informais. Não houve procedimento formal de elicitação ou validação com usuários.
2. **Evidência humana:** não houve pesquisa, teste ou avaliação com o público-alvo. Benefícios de acessibilidade e autonomia são resultados esperados do projeto, não resultados medidos.
3. **Evidência do protótipo físico:** relatório, diagrama, fotografias e vídeo documentam leitura, decodificação, autenticação HMAC-SHA1 e acionamento elétrico no protótipo histórico. A equipe confirmou que, em 31/08/2026, também realizou com sucesso a demonstração física ponta a ponta com QR Code, AES-CMAC e a fechadura conectada. Esse resultado autoriza a alegação categórica de integração física completa.
4. **Reprodutibilidade do firmware:** o estado atualmente preservado no repositório implementa AES-CMAC, não contém a rotina de acionamento documentada historicamente e possui incompatibilidades já identificadas. A versão integrada usada na demonstração final deverá ser preservada ou identificada por commit, se ainda estiver disponível.
5. **Validade temporal:** a emissão contém informação de validade, mas a inspeção do firmware preservado não encontrou a checagem temporal completa na decisão física. Portanto, não se afirmará que essa propriedade foi demonstrada sem evidência adicional.
6. **Revogação:** uma tranca que decide localmente e não recebe atualizações não consegue revogar com confiabilidade uma credencial ainda válida. Esse é um risco arquitetural aceito.
7. **Segredo compartilhado:** o AES-CMAC depende de segredo previamente gravado no dispositivo. Provisionamento e rotação estão fora do escopo, e o mecanismo não fornece não repúdio.
8. **Avaliação quantitativa:** não há resultados consolidados de latência, taxa de leitura, iluminação, distância, consumo, autonomia, confiabilidade ou resistência a ataques.
9. **Generalização:** a arquitetura admite outras instituições, mas o problema motivador veio de um único contexto e não sustenta conclusões sobre todas as instituições ou pessoas autistas.
10. **Acompanhamento acadêmico:** não há feedback substantivo do orientador incorporado até esta versão. Eventuais orientações posteriores poderão exigir ajuste explícito deste contrato.

## 8. Tratamento acadêmico do caso motivador

A narrativa poderá declarar que o projeto surgiu da participação de um dos autores, pessoa autista e integrante do CAUSP, em uma reunião com dirigentes da Faculdade de Direito da USP, combinada a relatos informais de colegas sobre dificuldades de acesso à sala sensorial. Essa informação explica por que o problema foi escolhido e como a equipe formou sua percepção inicial.

O texto não deverá transformar esses relatos em estatística, diagnóstico institucional ou consenso do público-alvo. Formulações como “segundo o relato de um dos autores” e “a equipe identificou como problema de projeto” preservarão a origem da informação. Afirmações gerais sobre autismo, acessibilidade ou barreiras institucionais exigirão literatura apropriada.

## 9. Critério de cumprimento dos objetivos

| Objetivo | Evidência mínima para a monografia | Limite de interpretação |
| --- | --- | --- |
| Caracterizar o cenário | relato identificado, contexto da reunião e documentação institucional disponível | não equivale a estudo com usuários |
| Especificar requisitos | tabela com origem, justificativa e estado de cada requisito | requisito autoral não é necessidade validada pelo público |
| Projetar a arquitetura | diagramas, modelo de dados, contratos e decisões | desenho não comprova implementação |
| Implementar o software | código, rotas, telas e verificações reproduzíveis ou registros preservados | fluxo relatado será distinguido do fluxo reproduzido |
| Implementar a credencial | formato, código de emissão e verificação e exemplos controlados | AES-CMAC não cifra nem produz assinatura digital |
| Desenvolver o protótipo físico | firmware, circuito, fotografias ou relato técnico identificado | sinal elétrico não comprova entrada de uma pessoa no espaço |
| Analisar o resultado | matriz atendido/parcial/não atendido/não avaliado | ausência de teste não será convertida em sucesso |

## 10. Aprovação do passo 3

A equipe aprovou em 01/09/2026:

1. a pergunta de pesquisa;
2. o objetivo geral;
3. os sete objetivos específicos;
4. o escopo incluído e excluído;
5. as dez limitações registradas.

Com essa aprovação, o passo 4 passa a consolidar o vocabulário e as alegações permitidas antes de qualquer reescrita dos capítulos.
