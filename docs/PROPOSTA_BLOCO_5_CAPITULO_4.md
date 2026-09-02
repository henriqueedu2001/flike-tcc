# FLIKE — proposta do bloco 5 do Capítulo 4

**Estado:** aprovado pela equipe após revisão do PDF

**Rodada:** Fase B, passo 6, bloco 5

**Data:** 01/09/2026

**Progresso global:** 6 de 26 passos concluídos (23,1%)

## 1. Finalidade do bloco

Este bloco especificará o caminho executado no dispositivo embarcado depois que o usuário apresenta o QR Code: recuperação do payload binário, decisão local de autorização e tratamento da janela temporal. Ele substituirá as seções legadas separadas por microcontrolador, câmera, HMI e tranca digital por um fluxo único, coerente com o funcionamento do sistema.

O bloco não descreverá offsets, larguras de campos, funções C++, GPIO, duração do pulso, modelo do relé ou código da biblioteca de leitura. Esses são detalhes de implementação destinados ao Capítulo 5. Também não classificará antecipadamente cada requisito como atendido: a demonstração e as lacunas do código preservado serão relacionadas na matriz de rastreabilidade.

## 2. Explicação proposta, do alto nível para o baixo nível

### 2.1 Da imagem aos bytes

A câmera não decide se o acesso está autorizado. Ela captura o símbolo, e o leitor de QR Code recupera a sequência binária transportada. Essa etapa precisa preservar os bytes exatamente como emitidos pelo servidor, inclusive valores nulos e valores que não formam texto UTF-8.

### 2.2 Dos bytes à decisão local

Depois da decodificação, o dispositivo interpreta a credencial e aplica verificações antes de produzir qualquer comando elétrico. A ordem lógica proposta é:

1. rejeitar tamanho ou estrutura incompatíveis com o protocolo;
2. verificar a tag de autenticação;
3. confirmar que o identificador recebido corresponde à própria tranca;
4. comparar o relógio local com os instantes de emissão e expiração;
5. produzir uma decisão positiva somente quando todas as condições forem satisfeitas.

Essa enumeração descreve dependências da decisão, sem impor que o firmware execute internamente cada função nessa mesma ordem. Uma falha em qualquer condição deve impedir a autorização.

### 2.3 Janela de autorização

A credencial não é consumida na primeira apresentação. Enquanto o instante atual pertencer à janela autorizada, o mesmo QR Code pode ser reapresentado para permitir entradas e saídas. Propõe-se representar o intervalo como **fechado na emissão e aberto na expiração**, isto é, `issued_at <= agora < expires_at`. Assim, a credencial ainda não vale antes da emissão e deixa de valer exatamente no instante de expiração.

Essa política elimina “uso único” e não depende da flag de uso existente no servidor. Como a decisão física é local, o dispositivo não consulta nem atualiza essa flag no momento da apresentação.

## 3. Requisitos funcionais propostos

### RF-11 — Recuperação do payload binário

**Enunciado:** o dispositivo embarcado deve ler o QR Code e recuperar integralmente o payload binário da credencial.

**Justificativa:** a autenticação e a interpretação dos campos dependem de os bytes recebidos serem idênticos aos emitidos. Tratá-los como texto, representação hexadecimal ou cadeia terminada por byte nulo pode alterar ou truncar a credencial.

**Critério de verificação:** gerar uma credencial contendo também bytes nulos e valores superiores a `0x7f`; apresentá-la à câmera; comparar comprimento e conteúdo recuperados no dispositivo com a sequência emitida; e rejeitar símbolos que não forneçam uma credencial completa.

### RF-12 — Validação local da credencial

**Enunciado:** antes de autorizar o acionamento, o dispositivo deve verificar localmente a estrutura da credencial, seu código de autenticação, a identidade da tranca destinatária e sua janela de validade.

**Justificativa:** uma tag válida demonstra que os campos protegidos não foram alterados sem conhecimento do segredo, mas não basta quando a credencial se destina a outra tranca ou está fora do período autorizado. Todas as condições precisam compor uma única decisão local.

**Critério de verificação:** apresentar uma credencial válida e, separadamente, casos com estrutura, tag, identificador da tranca, emissão ou expiração inválidos; confirmar que somente o caso integralmente válido produz autorização.

### RF-13 — Reapresentação durante a janela de autorização

**Enunciado:** uma credencial autêntica destinada à tranca deve poder ser reapresentada enquanto estiver em sua janela de autorização e deve ser rejeitada antes da emissão e a partir da expiração.

**Justificativa:** cada solicitação aprovada produz uma credencial temporária, e não um passe consumível. O usuário pode apresentá-la quantas vezes forem necessárias dentro do período concedido; credenciais antigas não devem autorizar acessos posteriores.

**Critério de verificação:** apresentar a mesma credencial ao menos duas vezes dentro do intervalo e confirmar duas autorizações; apresentá-la antes da emissão, exatamente na expiração e depois dela; e confirmar a rejeição nos três casos.

## 4. Requisito não funcional proposto

### RNF-01 — Decisão local sem consulta ao servidor

**Enunciado:** a decisão de autorização e o acionamento da fechadura não devem depender de consulta ao servidor no momento da leitura.

**Justificativa:** a operação local permite avaliar uma credencial já emitida mesmo quando a tranca está sem conectividade. Para isso, identificador, segredo e referência temporal precisam estar disponíveis no dispositivo. Solicitação, aprovação, emissão e obtenção inicial do QR Code continuam dependentes da aplicação web e da API.

**Critério de verificação:** deixar o dispositivo sem conexão de rede e, com identificador, segredo e relógio disponíveis localmente, apresentar uma credencial válida; confirmar que leitura, validação, decisão e acionamento são concluídos sem comunicação com o servidor.

## 5. Relação com a implementação e com a evidência

A tese afirmará categoricamente que houve demonstração física ponta a ponta com QR Code, AES-CMAC, sinal `HIGH`, circuito de acionamento e fechadura conectada, conforme confirmação da equipe. Essa demonstração sustenta RF-11, a verificação criptográfica de RF-12 e o núcleo de RNF-01. Por decisão da equipe, o acionamento não será repetido como requisito funcional autônomo; ele permanecerá no escopo, na arquitetura, na implementação e na avaliação do protótipo.

A redação dos requisitos não ocultará que a versão atualmente preservada do firmware não contém todas as verificações semânticas e temporais. O atendimento específico de formato, identificador da tranca e janela temporal será classificado com as evidências disponíveis na matriz de rastreabilidade. Isso não transforma a lacuna do checkout em uma incompatibilidade conceitual do requisito.

## 6. Figura ou diagrama

O bloco será escrito sem figura e sem espaço reservado. A equipe rejeitou a proposta de reunir leitura, autenticação, verificação semântica, tempo, sinal e fechadura em um único fluxograma por considerá-la excessivamente carregada. A enumeração textual da Seção 2.2 será suficiente para este trecho.

## 7. Portão de saída

Antes de implementar o bloco 5 na tese, a equipe deve decidir:

1. **aprovado em 01/09/2026:** inserir RF-11 a RF-13; excluir o requisito autônomo de acionamento anteriormente proposto como RF-14;
2. **aprovado em 01/09/2026:** adotar a janela `issued_at <= agora < expires_at`, válida no instante de emissão e inválida a partir da expiração;
3. **aprovado em 01/09/2026:** manter o tamanho exato e o layout do payload somente no Capítulo 5;
4. **aprovado em 01/09/2026:** inserir RNF-01 com as precondições locais de identificador, segredo e relógio;
5. **aprovado em 01/09/2026:** escrever o bloco sem figura nem espaço reservado.

Em revisão posterior, a equipe questionou a classificação de RNF-01 e aceitou mantê-lo como requisito não funcional: RF-12 define o comportamento de validação, enquanto RNF-01 impõe a restrição operacional de realizá-lo sem consulta ao servidor.

As cinco decisões foram encerradas. O bloco 5 foi implementado, compilado, revisado no PDF e aprovado pela equipe.
