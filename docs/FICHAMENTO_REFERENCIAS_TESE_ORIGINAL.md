# FLIKE — fichamento das referências da tese original

## 1. Finalidade e método

Este documento examina as oito obras que apareciam na bibliografia da versão original do TCC. Seu objetivo é indicar **o que cada referência realmente sustenta**, onde ela pode ser usada na nova monografia e quais afirmações não podem ser atribuídas a ela.

A versão original não continha chamadas de citação no corpo dos capítulos. As oito obras apareciam somente na lista bibliográfica. Por isso, este fichamento não tenta preservar associações inexistentes entre parágrafos e referências: ele reconstrói essas associações a partir da leitura das fontes.

O trabalho foi realizado em 1º de setembro de 2026 por meio de:

1. inventário da bibliografia em `FLIKE/capitulos/Cap6-Consideracoes.tex` e no PDF de referência;
2. busca de páginas oficiais, DOI, periódicos, repositórios institucionais ou cópias dos autores;
3. download sequencial e conservador dos documentos disponíveis publicamente;
4. validação técnica dos sete PDFs obtidos;
5. leitura integral do texto extraído e inspeção visual das páginas relevantes;
6. confronto entre objetivos, arquitetura, evidências, resultados e limitações de cada obra.

A ISO/IEC/IEEE 29148:2018 é a única fonte cujo texto completo não foi consultado: seu acesso integral é pago. A ficha R04 se limita ao catálogo, à introdução, ao sumário e aos termos públicos da plataforma oficial da ISO. Não devem ser atribuídas a essa norma cláusulas ou formulações que não tenham sido verificadas no texto integral.

Os arquivos, links, licenças e hashes estão documentados em `materiais/referencias-originais/README.md`. As entradas BibTeX preliminares estão em `materiais/referencias-originais/referencias-originais.bib`.

## 2. Resultado do inventário

| ID | Obra | Tipo e força da evidência | Uso principal recomendado |
| --- | --- | --- | --- |
| R01 | Lima (2022), *SmartLock Lite* | Relatório técnico institucional com protótipo e testes de funcionamento | Trabalho relacionado brasileiro, ESP32, RFID, servidor, circuito e limitações de recursos |
| R02 | Ho et al. (2016), *Smart Locks* | Artigo revisado por pares, análise de segurança e protótipo experimental | Segurança de fechaduras inteligentes, revogação, logs e disponibilidade em arquiteturas desconectadas |
| R03 | Gadupu et al. (2021), *ACCESS* | Artigo revisado por pares, protótipo IoT e medições de tempo | Comparação de arquitetura, permissões temporárias, conectividade, logging e atuação física |
| R04 | ISO/IEC/IEEE 29148:2018 | Norma vigente; somente conteúdo público oficial examinado | Autoridade principal para engenharia, qualidade e rastreabilidade de requisitos |
| R05 | Li et al. (2018), *An Intelligent Electronic Lock* | Artigo aberto com projeto de hardware e software, sem avaliação quantitativa | Circuito de acionamento, RFID, autorização centralizada e comparação com FLIKE offline |
| R06 | Asman et al. (2019), *A Prototype of Smart Lock* | Artigo aberto com maquete e testes de componentes | Integração elétrica, relé/solenoide, alimentação de reserva e cuidados de prototipação |
| R07 | IEEE Std 830-1998 | Norma histórica substituída, lida por espelho institucional | Formulações históricas sobre qualidades de uma SRS; uso secundário à R04 |
| R08 | Kamelia et al. (2014), *Door-Automation System* | Artigo com protótipo e testes qualitativos | Analogia simples entre sinal lógico, driver/relé e solenoide; histórico de soluções Bluetooth |

## 3. Fichas analíticas

### R01 — Lima (2022): *SmartLock Lite*

**Identificação corrigida.** G. Lima. *SmartLock Lite: um sistema de controle de acesso usando o microcontrolador ESP32*. Relatório Técnico IC-22-06, Instituto de Computação da Universidade Estadual de Campinas, novembro de 2022. A inicial “G.” é a única identificação autoral confirmada na obra; o prenome não deve ser inventado. O relatório está no [portal Smart Campus da Unicamp](https://smartcampus.prefeitura.unicamp.br/) e seu [PDF institucional](https://smartcampus.prefeitura.unicamp.br/pub/artigos_relatorios/Gabriel_SmartLock_ESP32.pdf) foi preservado como R01.

**Problema e proposta.** O trabalho adapta para ESP32, com MicroPython, uma fechadura anteriormente construída sobre Raspberry Pi. A motivação técnica é reduzir custo e tamanho, preservando um subconjunto funcional da solução anterior. O núcleo mínimo escolhido compreende leitura de cartões RFID e abertura programada por horário.

**Arquitetura e implementação.** O leitor MFRC522 obtém a identificação do cartão. O ESP32 consulta por Wi-Fi e HTTPS um servidor remoto para verificar autorização e faixas de horário. O dispositivo usa NTP para obter hora compatível com a validação de certificados. A implementação discute concorrência, interrupções, FreeRTOS e limitações das bibliotecas MicroPython; ao final, adota programação assíncrona cooperativa com `uasyncio`. O protótipo integra ESP32, MFRC522, relé, buzzer, LED RGB, botão e resistor de 150 Ω.

**Evidências apresentadas.** A montagem em protoboard permaneceu ligada por 14 dias. Depois, uma versão em placa perfurada permaneceu ligada por mais sete dias e foi montada em uma maquete. O autor relata funcionamento correto, mas não apresenta taxa de falhas, latência, consumo, amostra de leituras ou protocolo experimental detalhado.

**Uso recomendado no FLIKE.**

- No Capítulo 2, como trabalho relacionado brasileiro que demonstra a viabilidade de um controle de acesso baseado em ESP32, leitor de credenciais, servidor e relé.
- No Capítulo 5, para contextualizar restrições de memória, bibliotecas e concorrência em microcontroladores e para comparar a integração física por relé.
- Na comparação arquitetural, para destacar que o SmartLock Lite consulta o servidor no momento da autorização, enquanto o FLIKE valida localmente a credencial já emitida.

**Limites e cuidados.** O relatório **não demonstra leitura de QR Code**. A câmera aparece apenas como funcionalidade a estudar depois do atendimento aos requisitos mínimos. O trabalho não fundamenta AES-CMAC, acessibilidade, segurança criptográfica do FLIKE nem benefícios ao público autista. A alegação de redução de custo não vem acompanhada de valores.

### R02 — Ho et al. (2016): *Smart Locks: Lessons for Securing Commodity Internet of Things Devices*

**Identificação corrigida.** Grant Ho, Derek Leung, Pratyush Mishra, Ashkan Hosseini, Dawn Song e David Wagner. Artigo publicado na 11ª ACM Asia Conference on Computer and Communications Security, páginas 461–472, DOI [10.1145/2897845.2897886](https://doi.org/10.1145/2897845.2897886). A referência original omitia evento, ano, páginas e DOI.

**Problema e método.** Os autores constroem um modelo de segurança para fechaduras residenciais inteligentes e analisam cinco produtos comerciais: August, Danalock, Kevo, Okidokeys e Lockitron. O estudo considera adversário fisicamente presente, usuário revogado, ladrão de dispositivo e atacante de retransmissão. As propriedades centrais são impedir acessos incompatíveis com a intenção do usuário e preservar a integridade dos registros de acesso.

**Resultados conceituais.** O artigo separa duas arquiteturas. Na arquitetura dispositivo--gateway--nuvem, a fechadura depende do telefone do usuário como ponte; na conexão direta, a própria fechadura se comunica com o servidor. Os ataques encontrados se agrupam em inconsistência de estado — especialmente revogação e evasão de logs — e destravamento indesejado por interpretação incorreta da intenção ou retransmissão.

Um usuário revogado pode manter o telefone desconectado e impedir que a fechadura receba a revogação. Eventos também podem deixar de chegar ao servidor. A conexão direta reduz esses problemas, mas aumenta dependência de rede, consumo, custo e superfície de ataque remoto. Como mitigação intermediária, os autores propõem consistência eventual: atualizações de lista de controle de acesso assinadas e versionadas são entregues nas interações honestas, e a fechadura mantém uma fila local autenticada de eventos com números de sequência.

**Evidências experimentais.** O artigo também apresenta um protótipo chamado Vibrato para expressar melhor a intenção do usuário em destravamentos por proximidade. Foram executadas 100 tentativas legítimas e cenários de ataque; a avaliação mede êxito e latência. Essa parte sustenta as conclusões específicas do mecanismo Vibrato, não uma validação geral de todas as defesas propostas.

**Uso recomendado no FLIKE.**

- É a fonte mais forte do conjunto original para explicar o compromisso entre disponibilidade offline, revogação e integridade de logs.
- Sustenta a afirmação de que uma credencial ainda válida, já entregue, não pode ser revogada com confiabilidade por uma tranca que não recebe atualizações.
- Ajuda a distinguir registro local de um evento, sincronização posterior e confirmação autoritativa no servidor.
- Permite argumentar que a apresentação explícita do QR Code expressa uma ação do usuário melhor que um desbloqueio automático por mera proximidade. Isso não impede cópia ou compartilhamento do QR Code.

**Limites e cuidados.** Os produtos analisados eram fechaduras residenciais de 2016; o FLIKE tem contexto institucional e protocolo distintos. Parte dos ataques de retransmissão é inferida de trabalhos anteriores. A solução de consistência eventual pressupõe algum canal posterior de atualização, inexistente na decisão local do FLIKE no momento da leitura. O artigo não sustenta acessibilidade, AES-CMAC ou não repúdio de uma pessoa física.

### R03 — Gadupu et al. (2021): *ACCESS — IoT Enabled Smart Lock*

**Identificação.** Harshith Gadupu, Osa Mokharji, Raunak Kankaria, Shrey Kumar e Kayalvizhi Jayavel. *International Journal of Reconfigurable and Embedded Systems*, v. 10, n. 3, p. 176–185, DOI [10.11591/ijres.v10.i3.pp176-185](https://doi.org/10.11591/ijres.v10.i3.pp176-185).

**Proposta e arquitetura.** ACCESS é uma fechadura centralizada sobre Raspberry Pi, aplicação móvel e servidor em nuvem. O dispositivo aciona um relé ligado a um solenoide de 12 V, usa MQTT e HTTP, câmera, campainha, áudio e Bluetooth Low Energy. O banco representa usuários, fechaduras, permissões temporárias e logs. Há proprietário principal, proprietários secundários e convidados; convidados recebem prazo de acesso e operam apenas quando próximos à fechadura.

**Operação offline.** A contingência sem internet usa teclado e tela OLED. O usuário informa OTP ou código mestre armazenado localmente. O OTP só é renovado depois da reconexão do Raspberry Pi. Trata-se de um mecanismo diferente da credencial criptográfica offline do FLIKE.

**Evidências e resultados.** Os autores relatam 60 experimentos em rede Wi-Fi e apresentam tempos de quatro cenários: cerca de 1,30 s para campainha/vídeo, 1,25 s para comando remoto, 2,27 s para acesso de convidado BLE presente e 1,14 s para convidado ausente. Também listam causas de falha, como perda de internet, indisponibilidade da nuvem, sinal ruim, potência insuficiente do solenoide e Bluetooth desligado. O texto afirma três cenários, embora a tabela apresente quatro; a inconsistência deve ser preservada como limitação.

**Uso recomendado no FLIKE.**

- Comparar papéis, permissões com expiração, registros de operação e atuação por relé/solenoide.
- Mostrar uma alternativa fortemente dependente de servidor, MQTT, aplicativo e BLE, em contraste com a autorização local por QR Code do FLIKE.
- Inspirar a apresentação de cenários, tempos e causas de falha no capítulo de avaliação, sem copiar métricas que o FLIKE não mediu.

**Limites e cuidados.** Afirmações de segurança, acessibilidade e resistência à clonagem não são acompanhadas de avaliação adversarial suficiente. A rotação de UUID BLE não deve ser apresentada como solução comprovada contra clonagem. O estudo não trata de pessoas autistas, CMAC ou QR Code.

### R04 — ISO/IEC/IEEE 29148:2018

**Identificação e estado.** *Systems and software engineering — Life cycle processes — Requirements engineering*, 2ª edição, novembro de 2018. O [catálogo oficial da ISO](https://www.iso.org/standard/72089.html) informa 92 páginas, confirmação em 2024 e estágio de ciclo de vida “a ser revisada”. Em 1º de setembro de 2026, esta ainda é a edição vigente.

**Escopo verificável publicamente.** A norma organiza processos de engenharia de requisitos para sistemas e software, define itens de informação e orienta conteúdo e formato de especificações. O conteúdo público relaciona esses processos às normas de ciclo de vida ISO/IEC/IEEE 15288 e 12207. A plataforma pública define conceitos como requisito, restrição, requisito derivado, elicitação, gestão de requisitos, rastreabilidade, matriz de rastreabilidade, verificação, validação, parte interessada e especificação de requisitos.

**Uso recomendado no FLIKE.**

- Autoridade principal para justificar identificação única dos requisitos, origem, critérios verificáveis e rastreabilidade.
- Base para separar necessidade de parte interessada, requisito do sistema, restrição de projeto e decisão arquitetural.
- Base terminológica para distinguir validação em relação às necessidades de uso e verificação em relação às características especificadas.
- Referência metodológica nos capítulos 3 e 4 e na matriz entre requisitos, componentes e testes.

**Limites e cuidados.** Como o texto integral não foi obtido, qualquer citação de cláusula, página, formulação normativa ou lista de propriedades deve aguardar acesso legítimo pela USP ou aquisição. O fichamento não deve ser usado para alegar conformidade integral do TCC com a norma. O estado “a ser revisada” também não equivale a norma cancelada.

### R05 — Li et al. (2018): *An Intelligent Electronic Lock for Remote-Control System Based on the Internet of Things*

**Identificação.** Wei Li, Hongrui Li, Aini Gong, Yining Ou e Menglu Li. *Journal of Physics: Conference Series*, v. 1069, art. 012134, DOI [10.1088/1742-6596/1069/1/012134](https://doi.org/10.1088/1742-6596/1069/1/012134).

**Proposta e arquitetura.** O artigo apresenta uma fechadura conectada por NB-IoT. Um STM32F103 lê cartões RFID e envia ao servidor o identificador e o horário corrente. O servidor decide a autorização e retorna a resposta de abertura ou recusa. Um miniaplicativo WeChat permite consultar estado e registros. O dispositivo também reporta o resultado da tentativa ao servidor.

**Circuito e software.** O circuito separa a alimentação e o comando do microcontrolador da carga de 12 V. Transistores de chaveamento acionam a bobina/relé que comuta a fechadura, com diodos de proteção no estágio indutivo. O software em C organiza leitura do cartão, comunicação com a nuvem, pulso de abertura, retorno ao estado fechado e reporte do resultado. O artigo menciona XXTEA para proteger dados trocados e mantém o módulo NB-IoT ativo com tráfego periódico.

**Uso recomendado no FLIKE.**

- No Capítulo 2 ou em trabalhos relacionados, como exemplo de decisão de autorização centralizada por RFID e nuvem.
- No Capítulo 5, para explicar conceitualmente por que o pino lógico não alimenta diretamente a fechadura e por que há estágio de chaveamento e proteção para a carga indutiva.
- Na comparação, destacar que o servidor decide cada acesso nessa solução; no FLIKE, o servidor emite uma credencial e a tranca decide localmente se a autenticação e o período são válidos.

**Limites e cuidados.** Não há seção de testes quantitativos nem análise adversarial. As propriedades de segurança do XXTEA não são demonstradas. O texto não sustenta acessibilidade, baixo custo do FLIKE, robustez de produção ou a topologia exata do circuito construído pela equipe.

### R06 — Asman, Permata e Fatkhurrokhman (2019): *A Prototype of Smart Lock Based on IoT with ESP8266*

**Identificação corrigida.** Firza Fadlullah Asman, Endi Permata e Mohammad Fatkhurrokhman. *Jurnal Ilmiah Teknik Elektro Komputer dan Informatika*, v. 5, n. 2, p. 101–111, dezembro de 2019, DOI [10.26555/jiteki.v5i2.15317](https://doi.org/10.26555/jiteki.v5i2.15317). Embora o histórico editorial mostre recebimento e aceite em 2020, o volume e a paginação pertencem à edição de 2019.

**Proposta.** A maquete usa Wemos D1 R1/ESP8266, aplicativo Blynk, sensores PIR, relés, dois solenoides de 12 V, buzzer e bateria de reserva. A fechadura pode ser comandada pelo telefone; o PIR também participa do fluxo de detecção. Os autores descrevem o trabalho segundo o modelo ADDIE.

**Evidências.** O artigo testa individualmente componentes: dois pinos da placa não funcionaram por erro de tensão durante o desenvolvimento; o PIR foi observado a 90 cm e 120°; os solenoides são nominais de 12 V, mas a maquete recebeu 15 V para alimentar dois deles; e uma bateria inicialmente medida em 12,4 V permaneceu registrada como 12 V durante as sete horas seguintes de espera. A conclusão resume a autonomia como superior a cinco horas. O texto menciona avaliação por três especialistas com questionário de 20 itens, mas não apresenta os resultados desse questionário.

**Uso recomendado no FLIKE.**

- Contextualizar a separação entre controle, relé, alimentação e solenoide.
- Mostrar que integração elétrica exige conferir níveis de tensão, corrente e potência e que falhas de prototipação podem inutilizar pinos.
- Motivar, como trabalho futuro do FLIKE, avaliação de consumo, autonomia e alimentação de contingência.

**Limites e cuidados.** O estudo praticamente não avalia autenticação ou segurança e depende de Blynk e internet. As medições são limitadas e algumas decisões, como sobretensão dos solenoides, não devem ser copiadas. Não há avaliação de usuários nem base para alegações de acessibilidade.

### R07 — IEEE Std 830-1998

**Identificação corrigida.** *IEEE Recommended Practice for Software Requirements Specifications*, IEEE Std 830-1998, publicada em 20 de outubro de 1998. O [catálogo oficial IEEE](https://standards.ieee.org/ieee/830/1222/) registra reafirmação em 2009 e substituição posterior pela ISO/IEC/IEEE 29148:2011. A bibliografia original tratava 2009 de forma enganosa como ano da obra.

**Conteúdo.** A norma descreve características e organização de uma especificação de requisitos de software. Uma boa SRS deve ser correta, não ambígua, completa, consistente, classificada por importância ou estabilidade, verificável, modificável e rastreável. Requisitos vagos, como “boa interface” ou “funcionar bem”, não são verificáveis. A completude inclui respostas a entradas válidas e inválidas e definição de termos, figuras e tabelas. Itens pendentes precisam registrar motivo, responsável e condição de resolução.

A rastreabilidade deve apontar para a origem do requisito e permitir seguir sua implementação por identificadores únicos. A norma também recomenda separar comportamento externo requerido de decisões de projeto, admitindo restrições arquiteturais quando necessárias. Entre as categorias tratadas estão interfaces externas, funções, desempenho mensurável, necessidades lógicas de dados, restrições e atributos como confiabilidade, disponibilidade, segurança, manutenibilidade e portabilidade.

**Uso recomendado no FLIKE.** Pode explicar historicamente práticas clássicas de SRS e fornecer exemplos de verificabilidade, modificabilidade e rastreabilidade. É compatível com a remoção de requisitos vagos e com os identificadores RF/RNF adotados no Capítulo 4.

**Limites e cuidados.** A norma tem foco em software, enquanto o FLIKE inclui hardware, firmware, operação e partes interessadas. Ela está substituída. A ISO/IEC/IEEE 29148:2018 deve ser a autoridade principal; a R07 só deve permanecer se houver uma afirmação histórica ou formulação particular que realmente exija a fonte antiga. Não convém citar R04 e R07 juntas em todos os parágrafos.

### R08 — Kamelia et al. (2014): *Door-Automation System Using Bluetooth-Based Android for Mobile Phone*

**Identificação.** Lia Kamelia, Alfin Noorhassan S. R., Mada Sanjaya e Edi Mulyana. *ARPN Journal of Engineering and Applied Sciences*, v. 9, n. 10, p. 1759–1762, outubro de 2014.

**Proposta e implementação.** Um aplicativo Android envia comando pelo módulo Bluetooth HC-05 a um Arduino Uno. O microcontrolador coloca um pino em nível alto, o driver aciona o relé e o relé comuta um solenoide de 12 V. Um LED indica o estado. O software aplica atraso de um segundo depois do comando.

**Evidências.** Os testes verificam qualitativamente alimentação, conectividade, mudança de estado no pino, atuação do relé e abertura do solenoide. Os autores relatam comportamento conforme o projeto, mas não informam número de repetições, taxa de êxito, latência observada, consumo ou ensaios de segurança.

**Uso recomendado no FLIKE.** É uma referência visual e conceitual simples para a cadeia `sinal lógico -> driver/relé -> carga de 12 V`. Pode aparecer em trabalhos relacionados ou na fundamentação do circuito, sempre acompanhada do esquema real do FLIKE. Também ilustra uma arquitetura por Bluetooth e aplicativo móvel que o projeto FLIKE abandonou.

**Limites e cuidados.** O protótipo é antigo, preliminar e não demonstra autenticação, autorização temporária, auditoria ou criptografia. A frase de que o sistema seria seguro não é sustentada por testes de segurança. A obra não deve ser usada para justificar as escolhas criptográficas ou de acessibilidade do FLIKE.

## 4. Síntese para inserção das citações

| Parte futura da tese | Afirmações que as referências podem sustentar | Fontes prioritárias | Observação editorial |
| --- | --- | --- | --- |
| Cap. 2 — controle de acesso e fechaduras inteligentes | Fechaduras digitais combinam credenciais, decisão de autorização, comunicação, atuação e registro; soluções variam entre decisão local e centralizada | R02, R03, R05 | Não tratar todos os protótipos como equivalentes ao FLIKE. |
| Cap. 2 — disponibilidade, revogação e logs | Estado desatualizado em dispositivos desconectados cria janelas de revogação e lacunas de auditoria; conectividade direta também tem custos e riscos | R02 | Fonte central para explicar o risco aceito pela validação offline do FLIKE. |
| Cap. 2 — sistemas embarcados e atuação | Um microcontrolador comanda um estágio de potência/relé para acionar fechadura ou solenoide alimentado separadamente | R01, R05, R06, R08 | Usar como contexto; o circuito efetivamente construído deve ser descrito pelas evidências próprias do FLIKE. |
| Cap. 3 — método de requisitos | Requisitos devem ter origem, formulação controlada, verificação e rastreabilidade | R04; R07 somente como apoio histórico | Não alegar conformidade integral com a ISO sem auditoria e acesso completo. |
| Cap. 4 — especificação | Identificadores únicos, critérios verificáveis e matriz de rastreabilidade tornam os requisitos auditáveis | R04 | A fonte sustenta o método; cada requisito do FLIKE continua sendo elaboração dos autores. |
| Cap. 5 — trabalhos relacionados | ESP32/RFID/servidor; Raspberry Pi/MQTT/BLE; NB-IoT/RFID; ESP8266/Blynk; Arduino/Bluetooth | R01, R03, R05, R06, R08 | Recomenda-se quadro comparativo por credencial, conectividade, decisão, hardware, testes e limitações. |
| Cap. 5 — avaliação | Tempos por cenário, testes de duração, falhas elétricas e causas de indisponibilidade são exemplos de evidência mensurável | R01, R03, R06 | Servem para orientar o relato dos testes reais, não para transferir resultados ao FLIKE. |

### 4.1 Prioridade de uso

1. **R02 e R04:** fontes conceitualmente mais importantes. R02 sustenta a análise de segurança arquitetural; R04 sustenta o processo de requisitos.
2. **R01, R03, R05, R06 e R08:** trabalhos relacionados e contexto de implementação. Devem aparecer sobretudo no quadro comparativo e nas seções técnicas pertinentes.
3. **R07:** fonte histórica. Deve ser removida da bibliografia final se nenhuma afirmação exigir especificamente a prática antiga.

### 4.2 Formulações seguras

- “A ausência de um canal de atualização no momento da leitura impede que a tranca conheça de imediato a revogação de uma credencial ainda válida; trabalhos sobre fechaduras inteligentes mostram o mesmo problema geral de inconsistência de estado em dispositivos desconectados (HO et al., 2016).”
- “Protótipos acadêmicos empregam um estágio de acionamento entre a saída lógica do microcontrolador e a fechadura alimentada em tensão superior (LI et al., 2018; KAMELIA et al., 2014).”
- “A especificação adotou identificadores e critérios de verificação para permitir rastrear requisitos até componentes e testes, em alinhamento geral com as práticas de engenharia de requisitos da ISO/IEC/IEEE 29148:2018.” A expressão “alinhamento geral” é mais defensável que “conformidade”.
- “O SmartLock Lite demonstra uma solução com ESP32, RFID, consulta a servidor e acionamento por relé (LIMA, 2022).” Não acrescentar QR Code a essa enumeração.

## 5. Lacunas que estas referências não cobrem

O conjunto original é insuficiente para a fundamentação completa do TCC. Nenhuma das oito obras fornece base adequada para:

- autismo, neurodiversidade, salas de regulação sensorial ou barreiras institucionais de acesso;
- QR Code como formato óptico, capacidade, correção de erros, cópia ou ameaça de compartilhamento;
- definição e segurança do AES-CMAC;
- segurança de relógio e verificação temporal em credenciais offline;
- proteção e provisionamento de segredo no servidor e no ESP32-CAM;
- LGPD, minimização de dados e retenção de logs;
- avaliação de usabilidade ou acessibilidade do público-alvo;
- não repúdio ou irretratabilidade atribuída à pessoa física — especialmente porque um MAC simétrico prova posse do segredo entre componentes, não autoria exclusiva de uma pessoa;
- dados técnicos específicos da ESP32-CAM e da biblioteca usada para leitura de QR Code;
- normas e boas práticas atuais de segurança elétrica aplicáveis à maquete.

Essas lacunas devem gerar buscas bibliográficas dirigidas antes dos blocos que dependem delas. As referências originais podem ser reaproveitadas, mas não devem limitar a revisão de literatura futura.

## 6. Decisões para a redação futura

1. Nenhuma das oito obras será mantida na bibliografia apenas por herança da versão original.
2. Cada referência será migrada para o arquivo bibliográfico principal somente quando uma chamada for inserida no corpo da tese.
3. A citação será colocada no mesmo parágrafo da afirmação sustentada, com página ou seção quando a precisão exigir.
4. Resultados próprios do FLIKE serão sustentados por código, fotografias, registros e testes do projeto, não por resultados de outros protótipos.
5. R02 será a base inicial da discussão sobre revogação e logs offline; R04 será a base inicial do método de requisitos.
6. Antes de usar cláusulas normativas da ISO/IEC/IEEE 29148:2018, a equipe deverá obter acesso legítimo ao texto integral, preferencialmente pela USP.
7. O relatório da Unicamp será tratado com seu título e número corretos e não será confundido com o relatório anterior do portal Smart Campus.
