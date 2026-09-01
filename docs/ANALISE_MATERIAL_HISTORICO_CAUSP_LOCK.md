# FLIKE — análise do material histórico do Laboratório de Processadores

**Estado:** análise concluída em 01/09/2026

**Fonte principal:** `materiais/CAUSP_LOCK/`

**Papel no TCC:** documentação histórica e evidência do protótipo físico que antecedeu o FLIKE

## 1. Finalidade e regra de nomenclatura

O diretório contém o projeto Overleaf produzido anteriormente para a disciplina Laboratório de Processadores, identificada no vídeo como PCS3732. O relatório usa o nome antigo “CAUSP-LOCK”. Na monografia atual, o projeto será chamado **FLIKE**. O nome antigo aparecerá apenas ao identificar literalmente o título, os arquivos ou a etapa histórica.

O material é valioso sobretudo por preservar:

- um diagrama elétrico completo;
- uma fotografia original da bancada;
- uma versão anotada da fotografia;
- a descrição textual da alimentação e do acionamento;
- um vídeo público de demonstração;
- a declaração explícita de que o ensaio não verificou a expiração da credencial;
- o protocolo HMAC-SHA1 usado naquela etapa do projeto.

## 2. Integridade e inventário

O arquivo `materiais/CAUSP_LOCK.zip` contém 11 arquivos. Cada arquivo do ZIP foi comparado por SHA-256 com a versão extraída em `materiais/CAUSP_LOCK/`; todos são idênticos. O ZIP e o diretório são, portanto, cópias redundantes do mesmo pacote.

| ID | Fonte | Conteúdo relevante |
| --- | --- | --- |
| H01 | `materiais/CAUSP_LOCK/main.tex` | relatório da disciplina, circuito, protocolo antigo, descrição do ensaio e link do vídeo |
| H02 | `images/causp-lock-protocol-ELETRIC_DIAGRAM.png` | diagrama de alimentação, interface com transistor, relé, fechadura e saída manual |
| H03 | `images/protótipo.jpg` | fotografia original em 4624 × 3468 pixels |
| H04 | `images/protótipo_anotado.png` | fotografia com identificação dos componentes |
| H05 | [vídeo da demonstração](https://youtu.be/gl5iByZ4_28) | sequência de apresentação do QR Code, explicação do circuito e acionamento da fechadura |
| H06 | [ficha técnica oficial da fechadura Papaiz](https://www.papaiz.com.br/content/dam/assa-abloy/americas/latam/papaiz/br/pt/fichas-t%C3%A9cnicas/Ficha%20t%C3%A9cnica%20-%20Fechadura%20El%C3%A9trica%20Sobrepor.pdf) | modelo, tensão, potência, pulso, dimensões e ausência de sensor |
| H07 | [documentação oficial da botoeira Papaiz](https://www.segurancaeletronica.papaiz.com.br/content/dam/assa-abloy/americas/latam/papaiz/br/pt/seguran%C3%A7a-eletr%C3%B4nica/aa-bp01na/Datasheet%20-%20AA-BP01NA.pdf) | exemplo de saída manual em paralelo com sistemas de controle de acesso |
| H08 | [notícia oficial da FDUSP](https://direito.usp.br/noticia/e59450c2bb90-fdusp-tera-sala-de-apoio-a-amamentacao-e-de-regulacao-sensorial) | localização, finalidade, inauguração e contexto institucional da sala |

As fontes H06–H08 não faziam parte do ZIP. Elas foram localizadas em páginas oficiais para conferir afirmações do relatório e poderão entrar futuramente na bibliografia do TCC.

## 3. Reconstrução do sistema elétrico

### 3.1 Componentes identificados

| Componente | Informação preservada | Força da evidência |
| --- | --- | --- |
| ESP32-CAM | módulo com câmera OV2640; saída lógica de 3,3 V; alimentação descrita como 5 V/1 A máximo | texto, diagrama, foto e vídeo |
| transistor NPN 2N2222 | interface entre GPIO e entrada do módulo de relé | texto, diagrama, foto e vídeo |
| resistor de base | 1 kΩ entre GPIO `UNLOCK` e base do 2N2222 | diagrama; resistor visível na foto |
| resistor de pull-up | 1 kΩ entre 12 V e o nó de controle do relé | diagrama; resistor visível na foto |
| módulo de relé | módulo de 12 V; a marcação fotografada é compatível com `SRD-12VDC-SL-C` | diagrama, foto e vídeo |
| fonte chaveada | saída identificada no relatório e na fotografia anotada como 12 V/5 A | texto, foto e vídeo; modelo não identificado |
| fechadura elétrica | Papaiz AA-ERL200P, de sobrepor, sem sensor | diagrama, foto, vídeo e ficha oficial |
| botão de saída | contato manual em paralelo com o contato do relé | apenas projeto e documentação externa; omitido na montagem |
| protoboard e cabeamento | montagem experimental da interface | foto e vídeo |

### 3.2 Caminho de energia e comando

O circuito pode ser descrito em cinco etapas:

1. A ESP32-CAM recebe alimentação de 5 V e executa a leitura e o processamento do QR Code.
2. Um GPIO denominado `UNLOCK` aplica seu sinal de 3,3 V à base do 2N2222 por um resistor de 1 kΩ.
3. O 2N2222 opera como chave de baixa lateral. Quando conduz, ele drena corrente do nó de controle para o terra. Um resistor de 1 kΩ conecta esse nó aos 12 V quando o transistor não conduz.
4. Esse nó controla a entrada de um módulo de relé alimentado em 12 V. A topologia desenhada inverte o sinal e sugere uma entrada ativa em nível baixo.
5. O contato comum do relé recebe 12 V. Quando o contato normalmente aberto fecha, o pulso é aplicado à fechadura AA-ERL200P, que realiza o destravamento mecânico.

Os símbolos de terra no diagrama indicam referência comum entre a ESP32-CAM, o transistor, o módulo de relé e a fonte de 12 V no lado de controle. Os contatos eletromecânicos separam o caminho de comando do caminho de corrente da fechadura, mas o material não sustenta a alegação de isolamento galvânico completo do sistema.

### 3.3 Correção da expressão “amplificador de sinal”

O relatório afirma que o 2N2222 “amplifica” o sinal de 3,3 V para aproximadamente 11 V. Essa descrição não representa adequadamente a topologia desenhada. O transistor:

- não entrega uma versão linear amplificada da tensão do GPIO;
- atua como chave saturada;
- converte o comando de 3,3 V em um nó referenciado à alimentação de 12 V;
- inverte o nível lógico;
- permite que o GPIO controle uma entrada que não deve ser ligada diretamente a ele.

Na tese, a formulação recomendada é **“estágio de chaveamento e conversão de nível com transistor NPN 2N2222”**. “Circuito de potência” pode nomear o conjunto formado pela interface, pelo relé e pelo caminho de alimentação da fechadura.

### 3.4 Fechadura e dimensionamento

A fotografia e o diagrama identificam a fechadura como **Papaiz AA-ERL200P sem sensor**. A ficha técnica oficial informa:

- compatibilidade com controle de acesso de 12 V;
- pulso de alimentação de 12 V a 18 Vac;
- potência de 12 W;
- tempo de acionamento de 1 s;
- instalação sobreposta;
- ausência de sensor no modelo documentado.

Em 12 V, 12 W correspondem nominalmente a 1 A, coerente com o valor registrado no relatório. A fonte de 12 V/5 A oferece capacidade nominal superior à demanda indicada da fechadura, mas o material não contém medições de corrente, queda de tensão, aquecimento ou transitórios.

A ficha técnica e o catálogo do fabricante apresentam redações ligeiramente diferentes para a faixa de alimentação. A tese deverá descrever o **uso de 12 V no protótipo** e citar a ficha adotada, sem generalizar uma faixa não ensaiada.

### 3.5 Saída manual e comportamento de contingência

O diagrama prevê um botão normalmente aberto entre 12 V e a entrada da fechadura, em paralelo com o contato normalmente aberto do relé. Enquanto pressionado, esse botão permite destravamento independente da ESP32-CAM. A função é coerente com as botoeiras auxiliares documentadas pela Papaiz para sistemas de controle de acesso.

O próprio relatório afirma que esse botão **não foi montado no protótipo**, por simplicidade. Portanto:

- ele pode ser apresentado como decisão de segurança prevista;
- não pode ser apresentado como funcionalidade demonstrada;
- o protótipo de bancada não deve ser descrito como sistema de saída de emergência completo.

## 4. O que o vídeo demonstra

O vídeo público possui aproximadamente 97 segundos e apresenta no mesmo ensaio:

1. a fechadura, a fonte, o relé, a protoboard e a ESP32-CAM;
2. um QR Code exibido em um telefone;
3. a aproximação do QR Code à câmera;
4. a explicação do caminho do sinal da ESP32-CAM para o transistor e o relé;
5. a afirmação verbal de que o código é lido, decodificado e autenticado;
6. o acionamento final atribuído à leitura do QR Code.

O vídeo e o relatório formam evidência de uma **demonstração integrada histórica**. Eles sustentam que a equipe montou o circuito e obteve resposta física da fechadura a partir do fluxo embarcado. Entretanto, não fornecem:

- log serial legível junto ao acionamento;
- payload e chave usados no ensaio;
- caso negativo com QR inválido;
- medição de latência ou taxa de sucesso;
- verificação de identidade da tranca;
- verificação temporal;
- ensaio repetido ou protocolo estatístico;
- sensor que confirme estado da porta, entrada ou ocupação.

O relatório é explícito ao dizer que o teste decodificou as informações e acionou a fechadura **sem se preocupar com a expiração**. Isso aumenta a utilidade da fonte, pois permite descrever corretamente tanto o sucesso quanto a fronteira do ensaio.

## 5. Distinção entre o protocolo histórico e o protocolo final

O protocolo do Laboratório de Processadores não é o protocolo final do FLIKE.

| Aspecto | Protótipo histórico | Implementação final examinada |
| --- | --- | --- |
| autenticação | HMAC-SHA1 | AES-CMAC |
| tag | 20 bytes | 16 bytes |
| mensagem | cabeçalho de 1 byte + corpo variável | mensagem fixa de 32 bytes |
| tamanho total | 5 a 41 bytes, segundo o relatório | 48 bytes |
| identificação principal | `user_id` e instante de geração no acesso | `user_id`, `digital_lock_id`, emissão e expiração |
| tipos de mensagem | acesso, sincronização, configuração e depuração | não há campo de tipo de mensagem |
| operações | entrada, saída, acesso bidirecional e comandos de configuração | uma credencial de acesso por solicitação |
| configuração de segredo | mensagens QR de configuração foram propostas | provisionamento prévio pelo fornecedor é a premissa final |
| expiração no ensaio físico | não verificada | campo presente; checagem não localizada no firmware preservado |
| acionamento elétrico | demonstrado no material histórico | rotina ausente no checkout final examinado |

O vídeo comprova diretamente a integração física ponta a ponta da etapa histórica baseada em HMAC-SHA1. Depois da migração, a equipe realizou diversos testes bem-sucedidos de leitura de QR Code, decodificação do payload, extração dos campos e verificação por AES-CMAC. O circuito elétrico adotado no FLIKE é exatamente o mesmo da demonstração histórica, e seu contrato com o firmware permaneceu inalterado: uma autorização bem-sucedida produz um sinal lógico `HIGH` na saída da ESP32-CAM, que comanda o estágio com 2N2222, o relé e a fechadura.

Segundo confirmação da equipe em 01/09/2026, um de seus integrantes remontou a maquete na noite anterior e executou com sucesso uma demonstração ponta a ponta do sistema físico com o protocolo AES-CMAC final. O ensaio integrou leitura do QR Code, validação local por AES-CMAC, emissão do sinal de comando, circuito elétrico e acionamento da fechadura.

A tese deverá afirmar categoricamente: **“O protótipo físico do FLIKE realizou, de ponta a ponta, a leitura do QR Code, a validação local por AES-CMAC, a emissão do sinal de comando e o acionamento da fechadura elétrica.”** O relatório e o vídeo antigos continuam sendo evidências da evolução histórica com HMAC-SHA1; a demonstração final com AES-CMAC é um resultado técnico posterior confirmado pela equipe.

## 6. Elementos diretamente aproveitáveis no TCC

### 6.1 Capítulo 1 — contexto

A notícia oficial da FDUSP sustenta a existência, localização no terceiro andar, finalidade e inauguração da sala em abril de 2024. Ela também registra a parceria institucional e declarações sobre acolhimento e regulação sensorial. Os problemas de liberação de chave, protocolo e constrangimento continuam sendo relato do autor e de colegas; não aparecem confirmados na notícia institucional.

### 6.2 Capítulo 3 — método e evolução do projeto

O trabalho da disciplina fornece um marco verificável na cronologia: concepção inicial, protocolo HMAC-SHA1, circuito de bancada e demonstração física. Ele permite explicar que o TCC evoluiu um protótipo anterior, separando o que foi herdado, alterado e abandonado.

### 6.3 Capítulo 5 — hardware e implementação

São aproveitáveis:

- fotografia original da bancada, preferencialmente com nova legenda e fonte “acervo dos autores”;
- fotografia anotada, após substituir o nome antigo e revisar os rótulos;
- diagrama elétrico como fonte para um esquema redesenhado em português;
- modelo e ficha técnica da fechadura;
- tabela de componentes e suas funções;
- explicação do estágio com 2N2222 e do relé;
- distinção entre botão de saída previsto e protótipo efetivamente montado;
- link ou quadro selecionado do vídeo como evidência complementar.

O diagrama original não deve ser simplesmente copiado como arquitetura final porque chama o 2N2222 de amplificador, usa rótulos em inglês e não distingue claramente alimentação, sinal lógico e contato seco. Um novo esquema deverá preservar a topologia comprovada e corrigir a terminologia.

### 6.4 Capítulo 5 — testes e resultados

O ensaio histórico pode ser descrito como teste funcional qualitativo de integração. O resultado observado é leitura do QR Code, processamento local e acionamento da fechadura no protocolo antigo. A ausência de expiração, casos negativos, repetições e instrumentação deverá constar na mesma seção.

Uma tabela de resultado apropriada poderá usar:

| Etapa | Evidência histórica | Conclusão permitida |
| --- | --- | --- |
| QR apresentado | vídeo | entrada visual foi fornecida à câmera |
| leitura e decodificação | relatório, narração e firmware histórico se localizado | equipe relatou recuperação do payload |
| HMAC-SHA1 | relatório e narração | autenticador do protocolo histórico foi usado |
| sinal de comando | narração e resposta do circuito | comando alcançou a interface elétrica |
| relé | vídeo e fotografia | módulo participou do acionamento |
| fechadura | vídeo e relatório | fechadura respondeu no ensaio |
| expiração | relatório declara que foi ignorada | propriedade não testada |

## 7. Conteúdo que não deve ser reaproveitado como estado final

- nome antigo do projeto;
- HMAC-SHA1 como algoritmo atual;
- mensagens de sincronização, configuração e depuração via QR;
- `CHECK_IN`, `CHECK_OUT` e inferência de ocupação;
- aplicativo móvel;
- divisão fixa entre cliente e administrador;
- registro local de entrada e saída sem sensor;
- alegações de uso único, assinatura digital e irretratabilidade;
- garantias absolutas de segurança, inclusão ou conveniência;
- detalhes genéricos do pipeline Xtensa e comparações com ARM/RISC-V sem relação direta com as decisões do FLIKE;
- números de desempenho do ESP32 sem confirmação em documentação primária e sem uso na avaliação.

## 8. Lacunas e riscos elétricos a declarar

O material demonstra uma prova de conceito em bancada, não uma instalação pronta para uso. Não estão documentados:

- número do GPIO `UNLOCK`;
- modelo da fonte de 5 V da ESP32-CAM;
- modelo completo da fonte de 12 V/5 A;
- esquema interno e nível ativo confirmado do módulo de relé;
- medições de tensão e corrente;
- proteção por fusível;
- supressão do transitório da fechadura no caminho de 12 V;
- proteção contra inversão, curto-circuito ou sobretemperatura;
- isolamento e aterramento da fonte ligada à rede;
- caixa, terminais protegidos, alívio de tração e dimensionamento de cabos;
- botão de saída montado;
- comportamento após falta e retorno de energia;
- ciclo de trabalho e aquecimento em acionamentos repetidos;
- conformidade com normas de instalação elétrica, incêndio, acessibilidade ou saída de emergência.

A fotografia mostra fonte aberta, protoboard e condutores expostos, adequados a uma demonstração supervisionada de laboratório. Ela não deve ilustrar uma solução pronta para instalação permanente sem legenda que identifique o caráter experimental.

## 9. Decisões para as próximas rodadas

1. Manter o pacote original intacto em `materiais/CAUSP_LOCK/` como fonte histórica.
2. Não usar o ZIP e a pasta como duas fontes independentes; eles são cópias idênticas.
3. Citar o relatório e o vídeo como artefatos produzidos pelos autores.
4. Redesenhar o circuito somente na rodada de hardware do Capítulo 5.
5. Copiar fotografias para `FLIKE/imagens/` apenas quando a subseção correspondente for autorizada.
6. Incluir a ficha oficial da fechadura e a página institucional da sala na futura bibliografia.
7. Registrar como concluída a demonstração ponta a ponta com AES-CMAC realizada em 31/08/2026, segundo confirmação da equipe.
8. Reunir, se disponível, evidência documental complementar do ensaio final — configuração, versão do firmware, sequência observada, fotografia, vídeo ou log — para fortalecer sua reprodutibilidade.
9. Registrar que o circuito elétrico é o mesmo nas duas etapas e recebe apenas o sinal `HIGH` da ESP32-CAM.
