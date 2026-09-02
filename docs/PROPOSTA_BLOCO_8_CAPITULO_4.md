# FLIKE — proposta do bloco 8 do Capítulo 4

**Estado:** aprovado pela equipe após revisão do PDF

**Rodada:** Fase B, passo 6, bloco 8

**Data:** 01/09/2026

**Progresso global:** 6 de 26 passos concluídos (23,1%)

## 1. Finalidade do bloco

Este bloco registrará as restrições de escopo e as decisões arquiteturais necessárias para interpretar os requisitos. Ele não criará novos RF, RNF ou RA. Seu objetivo é impedir que tecnologias, formatos implementados e propostas abandonadas sejam confundidos com necessidades do produto.

O Capítulo 4 apresentará somente a decisão e sua consequência para o sistema. Componentes, bibliotecas, funções, esquemas elétricos, offsets e larguras de campos permanecerão no Capítulo 5.

## 2. Fronteira entre requisitos e implementação

Os requisitos anteriores descrevem comportamentos e restrições verificáveis. As decisões deste bloco explicam como a equipe delimitou a solução: aplicação exclusivamente web, credencial transportada por QR Code, autenticação local simétrica e dispositivo baseado em ESP32-CAM.

O texto não transformará automaticamente Next.js, FastAPI, MySQL, AES-CMAC, ESP32-CAM ou o circuito usado em requisitos. Essas tecnologias poderão ser substituídas por implementações equivalentes sem alterar, por si só, a necessidade de solicitar, emitir, apresentar e validar uma credencial.

## 3. Decisões propostas para registro

### 3.1 Aplicação web e dependência de internet

O produto final possui aplicação web, API e banco de dados. Cadastro, autenticação, gestão da estrutura, solicitação, decisão, emissão e obtenção inicial da credencial exigem conexão. Não existe aplicativo móvel nativo.

O termo “offline” será reservado ao momento da leitura: depois que a credencial foi obtida, a tranca decide localmente sem consultar o servidor. O QR Code pode ser exibido pelo painel, salvo no aparelho ou disponibilizado por solução equivalente durante sua validade; não será prometido funcionamento offline da aplicação web.

### 3.2 Credencial, tranca e janela temporal

Cada solicitação aprovada produz uma credencial destinada a uma única tranca. Em salas com várias trancas, a interface deve permitir a escolha daquela que receberá a solicitação. Compartilhar um segredo entre dispositivos pode ser uma alternativa de implantação, mas não altera a identificação lógica da tranca no fluxo.

A credencial é reutilizável no intervalo `issued_at <= agora < expires_at`. O valor padrão de 24 horas pertence à implementação administrativa quando nenhuma expiração é informada; não será apresentado como validade universal do domínio.

O formato binário, o total de 48 bytes, a ordem dos campos, os inteiros big-endian, os timestamps e a tag de 16 bytes serão detalhados no Capítulo 5. No Capítulo 4, basta registrar que a codificação compacta foi escolhida para transporte óptico e autenticação local.

### 3.3 Segredo compartilhado e provisionamento

O FLIKE usa um segredo simétrico associado a cada tranca para que servidor e dispositivo calculem e verifiquem AES-CMAC. Assume-se que o fornecedor ou mantenedor grave previamente no dispositivo o identificador da tranca e o segredo correspondente. Interface de configuração, rotação pelo usuário e recuperação do segredo estão fora do escopo.

Essa arquitetura exige proteger o mesmo material nos dois lados. Como o verificador também possui segredo capaz de gerar tags, o mecanismo não fornece assinatura assimétrica nem não repúdio perante terceiros.

### 3.4 Consequência da decisão offline

Depois que uma credencial válida foi entregue ao usuário, o servidor não consegue garantir sua revogação imediata enquanto a tranca opera sem receber atualizações. O projeto aceita esse risco e limita a autorização pela expiração autenticada no próprio payload.

Essa escolha favorece disponibilidade local, mas não será descrita como segurança absoluta. Queda de energia, perda do aparelho, cópia do QR Code e comprometimento do segredo permanecem limitações ou riscos a discutir nos capítulos posteriores.

### 3.5 Plataforma física demonstrada

O protótipo utiliza ESP32-CAM com câmera, circuito de acionamento, fonte e fechadura elétrica. A equipe demonstrou de ponta a ponta leitura do QR Code, verificação AES-CMAC, sinal `HIGH`, atuação do circuito e resposta da fechadura. O número do GPIO, o circuito, a alimentação e o modelo da fechadura serão detalhados no Capítulo 5, conforme as evidências disponíveis.

O acionamento físico permanece parte do escopo e da contribuição do protótipo, embora a equipe tenha excluído sua repetição como requisito funcional autônomo.

## 4. Propostas abandonadas

Aplicativo Flutter, Bluetooth, MQTT, gateway intermediário e armazenamento S3 não fazem parte da solução final. Eles poderão ser mencionados apenas para explicar a evolução do projeto, sem aparecer em diagramas da arquitetura final ou requisitos e sem serem tratados automaticamente como promessas de trabalho futuro.

Também ficam fora do escopo final bateria com autonomia determinada, MTTF mínimo, compatibilidade universal com qualquer fechadura, log físico persistente, sensores de porta, comprovação de entrada ou ocupação e interface dedicada para configurar o segredo.

## 5. Forma proposta para o texto da tese

O bloco será escrito em subseções curtas, seguindo a ordem:

1. fronteira entre aplicação conectada e decisão local;
2. credencial por solicitação, tranca destinatária e validade;
3. segredo compartilhado e provisionamento;
4. risco de revogação e demais limitações da operação local;
5. plataforma física demonstrada;
6. propostas abandonadas.

Não será criada uma tabela de 48 bytes neste capítulo. Ela será proposta no Capítulo 5, onde os campos poderão ser explicados junto do código e dos vetores de teste.

## 6. Figura ou diagrama

Não se propõe figura nem espaço reservado. O Capítulo 4 já possui definições e requisitos suficientes para compreender a fronteira do sistema. Os diagramas de arquitetura e do circuito serão avaliados no Capítulo 5, separadamente e com finalidade específica.

## 7. Portão de saída

Antes de implementar o bloco 8 na tese, a equipe deve decidir:

1. **aprovado em 01/09/2026:** registrar essas decisões no Capítulo 4, mantendo detalhes técnicos e o layout de 48 bytes no Capítulo 5;
2. **aprovado em 01/09/2026:** adotar a fronteira entre aplicação conectada e decisão local, sem prometer frontend offline;
3. **aprovado em 01/09/2026:** adotar a premissa de provisionamento pelo fornecedor e excluir configuração e rotação do segredo;
4. **aprovado em 01/09/2026:** registrar explicitamente a limitação de revogação e a lista de propostas abandonadas;
5. **aprovado em 01/09/2026:** escrever o bloco sem figura nem espaço reservado.

As cinco decisões foram aprovadas pela equipe em 01/09/2026. O bloco foi implementado conforme este portão, compilado, inspecionado visualmente e aprovado pela equipe após a revisão das Seções 4.4 a 4.4.6.
