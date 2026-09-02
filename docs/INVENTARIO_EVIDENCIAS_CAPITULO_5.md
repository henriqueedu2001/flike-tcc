# FLIKE — inventário de evidências para o Capítulo 5

**Estado:** aprovado pela equipe em 01/09/2026

**Rodada:** Fase B, passo 7

**Data:** 01/09/2026

**Progresso global:** 8 de 26 passos concluídos (30,8%)

## 1. Finalidade

Este documento organiza as fontes que poderão sustentar a descrição do desenvolvimento, da integração e das limitações do FLIKE. Ele não substitui testes e não converte a existência de código em funcionamento demonstrado.

O inventário distingue cinco naturezas de evidência:

| Código | Natureza | O que permite afirmar |
| --- | --- | --- |
| **CV** | Código versionado | Uma lógica foi preservada em um commit identificável. |
| **DL** | Documento ou artefato local | Um diagrama, relatório, fotografia ou configuração foi preservado. |
| **TR** | Teste registrado | Entradas, procedimento e resultados observados foram preservados. |
| **EF** | Evidência física | Fotografia, vídeo ou registro mostra a montagem ou uma ação física. |
| **RE** | Relato da equipe | Um integrante confirmou um fato, mas ainda não foi localizado registro independente. |

Uma mesma alegação pode combinar categorias. A demonstração final do FLIKE, por exemplo, foi confirmada pela equipe e pode ser relacionada ao código e à documentação dos subsistemas, embora não tenha fotografia, vídeo ou log próprio preservado.

## 2. Referências de software identificadas

### 2.1 Backend

| Campo | Registro |
| --- | --- |
| Repositório | `flike-backend-api` |
| Referência final disponível | `origin/massive-vibe-code-session` |
| Commit | `e9268ccfcbd94e16deb4f0eb641c18b5195b63b9` |
| Data | 20/08/2026, 13:53:40, UTC−03 |
| Natureza | CV |
| Observação do checkout | A branch aberta está no commit pai `6f9efd4...`; a referência final foi lida com `git show`, sem checkout. A única alteração local é o bit executável de `scripts/run_server.sh`. |

O commit final acrescenta `GET /digital_key/requests`, consulta das solicitações do próprio usuário e os campos `user_name`, `user_email`, `room_name` e `building_name` usados pela interface administrativa. Ele é temporalmente correspondente ao commit final do frontend e corrige duas incompatibilidades registradas no levantamento anterior.

**Fontes principais:** `app/main.py`, `app/api/routes/`, `app/database/repositories.py`, `app/modules/cmac/key.py`, `app/modules/utils/binary_handler.py`, `scripts/create_db.py`, schemas e documentação do banco.

**Sustenta estaticamente:** FastAPI, MySQL, autenticação JWT, responsabilidade derivada da propriedade da instituição, hierarquia institucional, solicitações, aprovação/rejeição, emissão de credenciais, formato binário e AES-CMAC.

**Não demonstra sozinho:** servidor iniciado, migração aplicada, integração com o navegador, proteção completa das rotas, ausência de falhas de concorrência ou comportamento de um banco real.

### 2.2 Frontend

| Campo | Registro |
| --- | --- |
| Repositório | `flike-frontend-webpage` |
| Referência final disponível | `origin/frontend_prototype` |
| Commit | `9005601719e98b5cac1c3586d07ef79b06a28a00` |
| Data | 20/08/2026, 13:52:07, UTC−03 |
| Natureza | CV |
| Observação do checkout | `main` contém apenas o MVP HTML descontinuado. O commit Next.js foi lido diretamente do Git, sem alterar o checkout. |

**Fontes principais:** páginas em `app/`, componentes, hooks, serviços, tipos, `package.json` e `package-lock.json`.

**Sustenta estaticamente:** aplicação Next.js/React, cadastro e login, dashboard, seleção hierárquica, solicitação de credencial, administração da estrutura, aprovação/rejeição, consulta de chaves e geração do QR Code em modo binário.

**Não demonstra sozinho:** execução conjunta com a API, responsividade, acessibilidade, persistência offline, download da imagem ou correção final para QR Code versão 3-L. O commit examinado ainda usa os parâmetros automáticos da biblioteca; a equipe informou que a correção 3-L está preparada para um pull request posterior.

### 2.3 Firmware

| Campo | Registro |
| --- | --- |
| Repositório | `flike-firmware` |
| Commit preservado | `c2983f4ce6e02fd4ce68c212a54e8c5fd6ef1e78` |
| Data | 09/03/2026, 21:25:26, UTC−03 |
| Natureza | CV + arquivos locais de origem desconhecida |
| Estado remoto | `main` local está um commit à frente de `origin/main`. |

O commit preservado contém leitura de QR Code e validação AES-CMAC de uma mensagem de 48 bytes. O `loop()` imprime o payload e o resultado no monitor serial. Ele não interpreta os quatro campos, não verifica identificador da tranca ou janela temporal e não aciona a fechadura.

As mudanças locais alteram a assinatura de `validateDigitalKey`, removem o segredo do arquivo original e acrescentam `sdkconfig.defaults` e `digital_lock.{cpp,h}`. O `main.cpp` ainda chama a assinatura antiga, portanto esse conjunto local é estaticamente incompatível. A equipe já informou que não reconhece essas alterações como refatoração ativa; elas não serão tratadas como versão final nem modificadas por este trabalho.

**Sustenta estaticamente:** plataforma ESP32-CAM/Arduino, biblioteca de leitura, transporte binário, cálculo e comparação AES-CMAC e saída serial.

**Não demonstra sozinho:** build reproduzível, segredo e tranca provisionados corretamente, rejeição por tamanho, verificação temporal, sinal `HIGH` ou integração elétrica. A equipe confirmou que essas decisões e o acionamento foram exercitados na demonstração final, cujo código-fonte exato não está preservado no repositório examinado.

## 3. Evidências do protocolo

| Evidência | Natureza | Força e uso permitido |
| --- | --- | --- |
| `app/modules/cmac/key.py` no backend final | CV | Define 32 bytes de dados, tag AES-CMAC de 16 bytes e payload total de 48 bytes. |
| `app/modules/utils/binary_handler.py` | CV | Define serialização big-endian dos inteiros. |
| `useKeyQrCode.ts` no frontend final | CV | Converte o hexadecimal recebido em bytes e solicita modo `byte` à biblioteca de QR Code. |
| `digital_key.cpp` no firmware preservado | CV | Recalcula e compara a tag AES-CMAC dos 32 primeiros bytes. |
| NIST SP 800-38B e SP 800-57 | DL bibliográfico | Sustentam terminologia de CMAC e proteção do segredo; não testam o FLIKE. |
| Testes relatados de QR Code e AES-CMAC | RE | A equipe confirmou leituras e validações bem-sucedidas, inclusive comprimento, identificador da tranca, `issued_at`, `expires_at` e AES-CMAC na demonstração final; entradas e saídas ainda não foram preservadas como vetores de teste. |

Ainda não há TR que atravesse Python e C++ com um mesmo vetor e registre: bytes nulos e altos, tamanho inválido, campo adulterado, segredo incorreto, tranca incorreta e fronteiras temporais.

## 4. Evidência física e elétrica

### 4.1 Base técnica do circuito

| Artefato | Natureza | Conteúdo aproveitável |
| --- | --- | --- |
| `materiais/CAUSP_LOCK/main.tex` | DL | Relatório do projeto que antecedeu o FLIKE, aproveitado somente para recuperar o circuito e sua montagem. |
| `causp-lock-protocol-ELETRIC_DIAGRAM.png` | DL | Topologia do estágio com 2N2222, resistores, relé e fechadura. |
| `protótipo.jpg` | EF | Fotografia original da bancada; EXIF registra Samsung SM-A536E e 07/08/2025, 14:10:27. |
| `protótipo_anotado.png` | DL + EF derivada | Identificação visual dos componentes, sujeita à revisão dos rótulos. |
| Vídeo público PCS3732 | EF | Registro da montagem elétrica que serviu de base para o FLIKE. |
| `materiais/CAUSP_LOCK.zip` | DL duplicada | Arquivo versionado que contém os mesmos 11 itens da pasta; não deve ser contado como evidência independente. |

Esse material pertence a um projeto anterior e não será apresentado como uma versão do FLIKE nem usado para discutir o protocolo atual. Sua utilidade para a monografia limita-se à origem histórica da solução e à documentação do circuito elétrico reaproveitado. A análise consolidada identifica:

- ESP32-CAM com câmera OV2640 declarada;
- transistor NPN 2N2222 usado como chave e conversor de nível;
- resistor de base de 1 kΩ;
- resistor de pull-up de 1 kΩ;
- módulo de relé de 12 V;
- fonte chaveada de 12 V para o circuito de potência;
- carregador de celular adaptado para alimentar a eletrônica de controle;
- fechadura Papaiz AA-ERL200P sem sensor;
- protoboard e cabeamento de bancada;
- botão de saída previsto no diagrama, mas omitido da montagem.

### 4.2 Demonstração final do FLIKE

A equipe confirmou que, em 31/08/2026, realizou uma demonstração física ponta a ponta do FLIKE. O dispositivo leu e decodificou o QR Code, verificou o comprimento do payload, o identificador da tranca, `issued_at`, `expires_at` e o AES-CMAC, emitiu o sinal lógico `HIGH` e acionou a fechadura por meio do circuito elétrico. A integração física completa será registrada como resultado do projeto.

A demonstração final possui natureza **RE**, complementada por CV dos subsistemas e DL do circuito. Não há fotografia, vídeo ou log próprio do ensaio, e a equipe determinou que registros adicionais, o GPIO utilizado e o código-fonte exato gravado no dispositivo não serão exigidos para a redação.

## 5. Evidência do fluxo de software

A equipe relatou ter demonstrado o fluxo completo: usuário solicita acesso; responsável cadastra a estrutura e aprova ou rejeita; uma aprovação emite a credencial; o titular a recebe no dashboard.

Os commits finais de frontend e backend contêm os dois lados dos contratos centrais desse fluxo, inclusive consulta de solicitações recusadas e detalhes administrativos. A combinação de **CV + RE** permite descrever o fluxo como implementado e demonstrado pela equipe, deixando claro que este inventário ainda não o reproduziu.

Não foram localizados capturas de tela, gravação, exportação do banco, requisições preservadas, testes automatizados, coleção Postman/Insomnia, relatório de cobertura ou pipeline de CI. Esses registros poderão ser produzidos nos passos de avaliação se o ambiente ainda puder ser executado.

## 6. Diagramas existentes

Os arquivos em `FLIKE/imagens/` são documentação de arquitetura já presente na tese:

- `contexto_c4.drawio.png`;
- `application_container_c4.drawio.png`;
- `physical_lock_container_c4.drawio.png`;
- `relacionamentos.drawio.png`;
- `uml.png`.

Eles constituem DL de intenção e documentação, não prova de implementação. Também podem conter tecnologias ou relações antigas. Nenhum será reutilizado automaticamente no Capítulo 5. Cada figura será proposta separadamente e só será inserida após autorização da equipe.

## 7. Evidências por objetivo técnico

| Objetivo | Evidência disponível | Limite atual |
| --- | --- | --- |
| Arquitetura do sistema | CV nos três repositórios, modelo de dados e diagramas DL | Diagramas precisam ser reconciliados com a arquitetura final. |
| Fluxo web | CV dos commits finais + RE da demonstração | Execução reproduzível e registros visuais ainda ausentes. |
| Credencial binária | CV no backend, frontend e firmware | Vetor comum e casos negativos ainda ausentes. |
| Validação local | CV do CMAC + RE de testes e da demonstração final | O firmware preservado não contém todas as verificações confirmadas no ensaio final. |
| Circuito elétrico | DL e EF da base reaproveitada | Modelos comerciais exatos e medições elétricas não serão exigidos. |
| Integração física final | RE combinado a CV dos subsistemas e DL do circuito | Não há fotografia, vídeo ou log próprio do ensaio. |
| Acessibilidade técnica | Requisitos, código da interface e literatura | Não houve avaliação com participantes; inspeção ainda será executada. |
| Desempenho e confiabilidade | Nenhum resultado consolidado | Não afirmar taxa de sucesso, autonomia, MTTF ou resistência a ataques. |

## 8. Materiais que não serão usados como evidência do produto final

- checkout `main` do frontend e suas páginas HTML;
- protocolo do projeto que antecedeu o FLIKE;
- Flutter, Bluetooth, MQTT, gateway e S3;
- diagrams antigos como prova de implementação;
- campos `used` e `used_at` como consumo offline obrigatório da credencial;
- registro de acionamento como prova de entrada, saída ou ocupação;
- vídeo local `orientações-tcc/TCC-Documentação-20240226(ProfaSelma).mp4`, que é material de orientação acadêmica, permanece ignorado e **não será versionado**;
- o ZIP e a pasta do projeto anterior como duas evidências diferentes.

## 9. Lacunas priorizadas

### 9.1 Decisões fechadas para firmware e hardware

1. A demonstração final verificou comprimento, identificador da tranca, `issued_at`, `expires_at` e AES-CMAC antes do acionamento.
2. Não há fotografia, vídeo ou log adicional da demonstração, e esses registros não serão solicitados novamente.
3. O GPIO e o código-fonte exato gravado na ESP32-CAM não serão necessários para a descrição acadêmica.
4. O circuito será descrito no nível funcional: ESP32-CAM, transistor, relé, fonte chaveada de 12 V, carregador de celular adaptado e fechadura elétrica.
5. Modelos comerciais exatos das fontes e do relé não serão tratados como lacunas.

### 9.2 Necessárias antes dos testes de integração

1. As referências `e9268cc...` e `9005601...` foram confirmadas pela equipe como versões finais de backend e frontend, salvo o futuro commit da correção QR 3-L.
2. Registrar o commit do frontend que fixará `version: 3` e `errorCorrectionLevel: "L"` quando o pull request estiver incorporado.
3. Definir um ambiente de teste sem dados pessoais reais e verificar se MySQL, API e frontend ainda podem ser executados.
4. Produzir vetores comuns para emissão e verificação da credencial.

### 9.3 Podem permanecer como limitações

- ausência de testes com o público-alvo;
- ausência de medições elétricas, consumo, autonomia e MTTF;
- ausência de implantação na Faculdade de Direito;
- ausência de certificação, endurecimento de produção ou análise formal de segurança;
- ausência de revogação imediata durante operação local;
- ausência de sensores de porta, direção ou ocupação.

## 10. Portão de saída do passo 7

O inventário foi aprovado pela equipe em 01/09/2026. Foram confirmados os commits finais do backend e do frontend, o conjunto de verificações da demonstração física e o nível de detalhe adequado para o circuito. A equipe também determinou que o projeto anterior seja mencionado apenas como antecedente histórico do FLIKE e origem da base elétrica, sem comparação de protocolos na narrativa do produto atual.

Com essas decisões, o passo 7 está concluído. O passo 8 deverá propor o esqueleto detalhado do Capítulo 5 e consultar a equipe individualmente antes de incluir qualquer figura ou diagrama.
