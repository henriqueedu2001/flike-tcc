# FLIKE — proposta revisada do bloco 4 do Capítulo 4

**Estado:** aprovado pela equipe após revisão do PDF

**Rodada:** Fase B, passo 6, bloco 4

**Data:** 01/09/2026

**Progresso global:** 6 de 26 passos concluídos (23,1%)

## 1. Motivo da revisão

A primeira proposta foi rejeitada porque começava pelo formato de 48 bytes, acumulava decisões de implementação em um único requisito e não explicava a função da credencial antes de apresentar seus campos e seu mecanismo de autenticação. A implementação produzida a partir dela foi integralmente desfeita antes desta revisão; RF-01 a RF-08 permanecem como o último estado aprovado da tese.

A nova proposta separa quatro níveis que não devem ser confundidos:

1. **conceito:** o que a credencial representa no sistema;
2. **informação:** quais dados são necessários para representar a autorização;
3. **autenticação:** como a tranca distingue uma credencial emitida pelo FLIKE de dados fabricados ou alterados;
4. **representação:** como dados e autenticador são codificados de forma compacta e transportados pelo QR Code.

O tamanho de 48 bytes deixa de ser requisito funcional. Ele será tratado como resultado do formato binário implementado e explicado no Capítulo 5, depois que os requisitos que motivaram essa escolha forem apresentados.

## 2. Explicação proposta, do alto nível para o baixo nível

### 2.1 Ideia geral

A credencial digital é o artefato que materializa uma autorização já concedida. Depois que o responsável aprova uma solicitação, o sistema emite uma credencial para que o solicitante possa demonstrar à tranca que existe uma autorização válida. A credencial é apresentada como QR Code porque a ESP32-CAM precisa recebê-la por um canal visual, sem consultar o servidor naquele momento.

Essa explicação vem antes de payload, bytes, timestamps ou AES-CMAC. Ela estabelece a função da credencial no fluxo: **transportar uma autorização do servidor até a tranca**.

### 2.2 Dados da autorização

Para representar a autorização, a credencial precisa responder a quatro perguntas:

1. **para quem** o acesso foi autorizado: identificador do usuário;
2. **para onde** o acesso foi autorizado: identificador da tranca;
3. **a partir de qual referência temporal** a credencial foi emitida: instante de emissão;
4. **até quando** ela pode autorizar acesso: instante de expiração.

Esses campos descrevem a autorização, mas não impedem que alguém os altere. Um QR Code contendo apenas esses valores permitiria substituir a tranca, o usuário ou a expiração sem que o dispositivo detectasse a modificação.

### 2.3 “Assinatura” da credencial

Para que a tranca detecte fabricação ou alteração, o servidor calcula um código de autenticação sobre todos os dados da credencial. O FLIKE usa AES-CMAC e um segredo compartilhado exclusivamente entre o servidor e a tranca destinatária. A tranca recalcula o código com sua cópia do segredo e compara o resultado com o código recebido.

O texto poderá chamar esse valor de **tag de autenticação** ou **código de autenticação**. A expressão “assinatura” só poderá aparecer entre aspas ao explicar informalmente a ideia, seguida da correção terminológica: AES-CMAC é um mecanismo simétrico e não uma assinatura digital. Ele permite verificar integridade e origem criptográfica sob a premissa de segredo protegido; não cifra os dados, não impede cópia e não prova quem apresentou o QR Code.

### 2.4 Codificação e transporte

Dados da autorização e tag precisam ser convertidos em uma sequência que o gerador de QR Code e a tranca interpretem da mesma maneira. O projeto adotou uma codificação binária, porque representar os valores como texto consumiria mais espaço e produziria um símbolo visualmente mais denso.

Somente depois dessa justificativa o Capítulo 5 explicará o formato implementado: ordem dos campos, largura de cada inteiro, big-endian, timestamps Unix, mensagem de 32 bytes, tag de 16 bytes e total de 48 bytes. Esses números descrevem **como o protótipo foi construído**; eles não constituem, isoladamente, a necessidade que orientou a implementação.

## 3. Decomposição recomendada dos requisitos

A primeira proposta reunia conteúdo semântico, autenticação criptográfica, serialização e transporte em RF-09. Recomenda-se dividir o comportamento em dois requisitos funcionais e deslocar a restrição de densidade óptica para um requisito não funcional.

Essa alteração acrescenta um requisito funcional ao catálogo. Os antigos RF-10 a RF-14 passam a RF-11 a RF-15. Nenhum requisito já inserido na tese precisa ser renumerado, pois ela termina atualmente em RF-08.

### RF-09 — Conteúdo da credencial

**Enunciado:** cada credencial deve identificar o usuário autorizado e a tranca destinatária e delimitar sua janela de validade por meio dos instantes de emissão e expiração.

**Justificativa:** esses dados permitem relacionar a autorização ao seu titular lógico, ao atuador correto e ao período em que poderá ser aceita. O identificador do usuário vincula a credencial a uma conta; não comprova a identidade física da pessoa que a apresenta.

**Critério de verificação:** emitir uma credencial a partir de uma solicitação aprovada; recuperar seus dados; e confirmar que usuário, tranca, emissão e expiração correspondem à autorização que originou a emissão.

### RF-10 — Autenticação da credencial

**Enunciado:** o sistema deve autenticar conjuntamente todos os dados da credencial com um código verificável localmente pela tranca destinatária.

**Justificativa:** a tranca precisa detectar credenciais fabricadas e alterações no usuário, na tranca ou na janela temporal sem consultar o servidor. No FLIKE, esse comportamento é realizado por AES-CMAC com segredo compartilhado por tranca; o algoritmo é uma decisão arquitetural, e não precisa tornar o enunciado funcional dependente de uma biblioteca ou largura específica.

**Critério de verificação:** emitir uma credencial; validar seu código de autenticação com o segredo da tranca correta; modificar separadamente cada dado protegido sem recalcular o código; e confirmar que todas as versões modificadas falham na autenticação.

### RNF-05 — Compatibilidade óptica do QR Code

Em 01/09/2026, a equipe decidiu adotar QR Code versão 3, nível L, para a credencial final do FLIKE. Propõe-se a seguinte redação definitiva:

**Enunciado:** a representação completa da credencial deve ser codificada em modo binário como QR Code versão 3, com nível L de correção de erros.

**Justificativa:** aumentar a versão acrescenta módulos e torna o símbolo mais denso para o mesmo tamanho físico, o que pode prejudicar a leitura pela ESP32-CAM. A versão 3 limita a matriz a 29 × 29 módulos e comporta os 48 bytes da credencial somente no nível L. Essa escolha formaliza a restrição de compacidade que orientou o formato binário e aceita menor redundância de correção de erros como compromisso do projeto.

**Critério de verificação:** gerar uma credencial completa; confirmar que o símbolo resultante possui matriz de 29 × 29 módulos e nível L, sem promoção automática para versão superior; e demonstrar sua leitura pela ESP32-CAM. Não serão exigidas medidas de distância, tamanho físico, ângulo ou iluminação; caso seja tomada uma medida experimental, ela se limitará ao tempo de leitura.

## 4. Divergência descoberta entre 48 bytes e versões 2/3

A quantidade de dados que cabe em um QR Code depende simultaneamente da versão, do modo de codificação e do nível de correção de erros. A fonte da DENSO confirma essa relação e explica que aumentar a correção reduz a capacidade disponível.

Para a biblioteca `qrcode` 1.5.4 usada pelo frontend, as capacidades em modo binário são:

| Versão | Nível L | Nível M | Nível Q | Nível H |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 32 bytes | 26 bytes | 20 bytes | 14 bytes |
| 3 | 53 bytes | 42 bytes | 32 bytes | 24 bytes |
| 4 | 78 bytes | 62 bytes | 46 bytes | 34 bytes |

Consequências:

1. 48 bytes não cabem em QR Code versão 2 em nenhum nível;
2. 48 bytes cabem em versão 3 somente no nível L;
3. o frontend não escolhe nível explicitamente;
4. a biblioteca usa nível M por padrão;
5. portanto, o frontend preservado gera versão 4 para o payload binário de 48 bytes.

Essa divergência não invalida a demonstração física, mas impede afirmar simultaneamente, sem qualificação, que o protocolo implementado possui 48 bytes e que a interface atual gera QR Code versão 2 ou 3.

### 4.1 Auditoria do gerador histórico do CAUSP-LOCK

O repositório histórico `henriqueedu2001/causp-lock-server`, examinado no commit `f5b1026`, usa Segno 1.6.6 e chama `segno.make_qr(payload)` sem informar versão nem nível de correção. Portanto, o código não fixa “versão 3-L”: a biblioteca escolhe automaticamente a menor versão capaz de conter a mensagem e eleva o nível de correção enquanto isso não exigir uma versão maior.

A reprodução do gerador com as dependências e os dados de teste do próprio repositório produziu estes resultados:

| Mensagem histórica | Payload | Versão e nível | Matriz |
| --- | ---: | --- | ---: |
| acesso (`CHECK_IN`, `CHECK_OUT` e `BI_ACCESS`) | 29 bytes | 2-L | 25 × 25 módulos |
| sincronização de relógio (`SET_TIME`) | 25 bytes | 2-M | 25 × 25 módulos |
| configuração de segredo | 41 bytes | 3-M | 29 × 29 módulos |
| depuração curta | 5 bytes | 1-H | 21 × 21 módulos |

Os PNGs versionados no repositório confirmam as dimensões obtidas na reprodução. Com escala de 25 pixels e borda de cinco módulos em cada lado, os símbolos de acesso medem 875 × 875 pixels: `(25 + 2 × 5) × 25`, o que corresponde inequivocamente à matriz 25 × 25 da versão 2.

A credencial histórica de acesso tinha 29 bytes: um byte de cabeçalho, quatro bytes para o usuário, quatro para o instante de geração e vinte para o HMAC-SHA1. Ela só cabe na versão 2 com correção L. A lembrança de uma versão 3 provavelmente se refere aos QR Codes de configuração, cujo payload de 41 bytes gera versão 3-M, e não à credencial de acesso.

O resultado histórico não pode ser transplantado diretamente para o FLIKE. A credencial atual substituiu o formato de 29 bytes por quatro campos de oito bytes e uma tag AES-CMAC de dezesseis bytes, totalizando 48 bytes. Com esse tamanho, a menor representação possível é 3-L; com o nível M usado por padrão no frontend atual, a biblioteca promove o símbolo para 4-M.

### 4.2 Decisão da equipe

Em 01/09/2026, a equipe aprovou **QR Code versão 3, nível L**, como especificação final do FLIKE. A decisão corresponde à antiga Alternativa B desta proposta.

O frontend examinado ainda não continha a configuração no commit preservado. Em 01/09/2026, a equipe informou que a correção para `version: 3` e `errorCorrectionLevel: "L"` já foi preparada e será incorporada por pull request. A incompatibilidade transitória entre o commit examinado e a decisão final não integrará o texto da tese.

A especificação final não reproduz literalmente a credencial histórica 2-L. Ela preserva o objetivo de baixa densidade visual dentro do novo protocolo de 48 bytes. A adoção do nível L reduz a redundância disponível para recuperar módulos danificados; esse compromisso deverá aparecer na tese e nos ensaios.

## 5. Organização proposta no Capítulo 4

O bloco conterá:

1. explicação conceitual em quatro parágrafos curtos, seguindo as Seções 2.1 a 2.4;
2. RF-09, limitado ao conteúdo semântico da autorização;
3. RF-10, limitado à autenticação conjunta dos dados;
4. um parágrafo que explica que a codificação binária compacta é decisão arquitetural motivada pela leitura óptica;
5. RNF-05 com a especificação aprovada de QR Code 3-L.

O bloco não conterá tabela de offsets, larguras ou bytes. Essa tabela será proposta posteriormente para o Capítulo 5, na descrição da implementação do protocolo.

Os requisitos funcionais posteriores serão renumerados assim:

| Novo ID | Conteúdo anteriormente aprovado |
| --- | --- |
| RF-11 | Leitura do QR Code e recuperação do payload |
| RF-12 | Verificação local de formato, tag, tranca e janela temporal |
| RF-13 | Reapresentação dentro e rejeição fora da janela |
| RF-14 | Sinal elétrico e acionamento da fechadura |
| RF-15 | Consulta administrativa de portadores e histórico de credenciais |

## 6. Fontes e evidências

| Afirmação | Sustentação | Uso planejado |
| --- | --- | --- |
| CMAC autentica origem criptográfica e integridade sob segredo protegido. | Dworkin (2005), `nist2005cmac`. | Explicação de RF-10. |
| CMAC não cifra, não impede reapresentação e não fornece não repúdio pessoal. | Dworkin (2005), Barker (2020) e decisão P8. | Limites após RF-10. |
| QR Code transporta dados binários; capacidade varia com versão e correção. | DENSO ADC (2012), `denso2012qressentials`. | Motivação da codificação compacta. |
| O frontend usa `qrcode` 1.5.4, modo binário e correção M por padrão. | `package-lock.json`, `useKeyQrCode.ts` e documentação/código oficial da biblioteca 1.5.4. | Auditoria da divergência; não será generalizado como propriedade do QR Code. |
| A credencial de acesso do CAUSP-LOCK possui 29 bytes e gera QR Code 2-L; mensagens de configuração de 41 bytes geram 3-M. | `generator.py`, `encoder.py`, `requirements.txt`, `generate_test_qrcodes.py` e PNGs do repositório histórico, reproduzidos com Segno 1.6.6. | Antecedente técnico e esclarecimento da origem da restrição de densidade. |
| O formato implementado tem 48 bytes. | Backend `DigitalKey.get_digital_key_payload`, tabela `digital_key` e firmware. | Capítulo 5, como implementação. |

## 7. Figura ou diagrama

Uma figura conceitual poderia mostrar a progressão “dados da autorização → cálculo da tag → credencial → QR Code”. Ela ajudaria mais no Capítulo 5, junto da arquitetura do protocolo, do que neste pequeno grupo de requisitos.

**Recomendação:** escrever o bloco sem figura e reservar o diagrama para o Capítulo 5.

**Pergunta obrigatória à equipe:** existe algum diagrama do protocolo que deva ser aproveitado ou a equipe autoriza, futuramente, a criação de um espaço reservado para esse fluxo? Nenhuma figura ou espaço reservado será inserido sem resposta explícita.

## 8. Portão de saída

Antes de voltar à redação da tese, a equipe deve decidir:

1. **aprovado em 01/09/2026:** dividir RF-09 e RF-10 e renumerar os requisitos seguintes;
2. **aprovado em 01/09/2026:** tratar o layout de 48 bytes como implementação no Capítulo 5, e não como requisito;
3. **decidido em 01/09/2026:** adotar QR Code versão 3, nível L, e registrar a necessidade de corrigir posteriormente o frontend;
4. **aprovado em 01/09/2026:** inserir RNF-05 sem exigir medidas experimentais além de eventual tempo de leitura;
5. **aprovado em 01/09/2026:** escrever este bloco sem figura.

As cinco decisões foram aprovadas. O bloco 4 está autorizado para implementação e compilação.
