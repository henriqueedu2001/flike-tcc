# FLIKE — fichamento das referências complementares

## 1. Finalidade e escopo

Este documento registra a leitura crítica de **dez novas referências** escolhidas para complementar as oito obras herdadas da tese original. A seleção foi dirigida pelas lacunas já identificadas no projeto: motivação relacionada ao público autista, função da sala sensorial, acessibilidade da aplicação web, QR Code, autenticação offline com AES-CMAC, gestão do segredo simétrico, proteção dos registros de acesso e limites técnicos do ESP32.

O objetivo não é aumentar a bibliografia por volume. Cada ficha estabelece:

1. qual problema a obra estuda;
2. qual método ou natureza documental sustenta seus resultados;
3. quais afirmações ela permite fazer sobre o contexto do FLIKE;
4. quais inferências ela não autoriza;
5. em que capítulo e parágrafo sua citação poderá ser útil.

Nenhuma destas referências foi ainda inserida no texto da monografia. A migração para o arquivo bibliográfico principal ocorrerá durante a redação, no mesmo momento em que a afirmação sustentada for escrita. Uma obra que não venha a ser citada deverá ser retirada da bibliografia final.

## 2. Método de busca, obtenção e leitura

O trabalho foi realizado em 1º de setembro de 2026 com o seguinte procedimento:

1. tradução das lacunas do fichamento original em dez perguntas bibliográficas;
2. busca de fontes primárias, artigos revisados por pares, documentos oficiais e documentação do fabricante;
3. escolha de exatamente dez obras, sem multiplicar referências sobre o mesmo ponto;
4. download sequencial e conservador, com pausas e poucas tentativas por servidor;
5. validação do tipo de arquivo, paginação, metadados, DOI e página canônica;
6. extração e leitura do texto integral, complementadas por inspeção visual das tabelas, diagramas e páginas relevantes;
7. confronto dos resultados com a arquitetura e as evidências já registradas do FLIKE;
8. produção de entradas BibTeX preliminares, catálogo de procedência e hashes.

Uma cópia consolidada da LGPD produzida em 2020 foi inicialmente localizada, mas foi descartada por estar desatualizada. Em seu lugar, foi preservado o texto compilado oficial do Planalto vigente na data da coleta, que já registra alterações de 2026. Esse cuidado é necessário porque legislação e documentação técnica podem mudar depois desta leitura.

Os documentos locais, links e condições de acesso estão em `materiais/referencias-complementares/README.md`. As entradas bibliográficas estão em `materiais/referencias-complementares/referencias-complementares.bib`.

## 3. Resultado da seleção

| ID | Obra | Natureza e força da evidência | Lacuna principal coberta |
| --- | --- | --- | --- |
| C01 | MacLennan et al. (2023) | Estudo qualitativo participativo com 24 adultos autistas em sete grupos focais | Experiência sensorial, previsibilidade, comunicação e espaços de recuperação |
| C02 | Tola et al. (2021) | Revisão de escopo, método JBI e fluxo PRISMA, com 21 estudos incluídos | Ambiente construído, sala silenciosa, inteligibilidade e limites da literatura |
| C03 | Governo Federal (2014), eMAG 3.1 | Modelo técnico oficial brasileiro de acessibilidade digital | Requisitos e avaliação da aplicação web |
| C04 | NIST SP 800-38B | Recomendação técnica oficial para CMAC | Propriedades, tamanho de tag, repetição e limites do AES-CMAC |
| C05 | RFC 4493 | Especificação informativa com algoritmo e vetores de teste | Implementação interoperável do AES-CMAC-128 |
| C06 | NIST SP 800-57 Part 1 Rev. 5 | Recomendação técnica oficial de gestão de chaves | Proteção, ciclo de vida e comprometimento do segredo simétrico |
| C07 | DENSO ADC (2012) | Documento técnico do criador do QR Code | Estrutura, versões, capacidade, leitura e correção de erros |
| C08 | Kieseberg et al. (2010) | Artigo revisado por pares com análise de ameaça | QR Code como entrada não confiável e vetor de ataque |
| C09 | Brasil (2018), LGPD compilada | Lei federal em texto oficial vigente na coleta | Natureza pessoal dos logs, minimização, segurança e governança |
| C10 | Espressif Systems (2026) | Datasheet oficial do SoC ESP32, versão 5.3 | GPIO, alimentação, corrente e aceleração criptográfica |

## 4. Fichas analíticas

### C01 — MacLennan et al. (2023): experiências sensoriais de adultos autistas em espaços públicos

**Identificação.** Keren MacLennan, Catherine Woolley, Emily andsensory, Brett Heasman, Jess Starns, Becky George e Catherine Manning. *“It Is a Big Spider Web of Things”: Sensory Experiences of Autistic Adults in Public Spaces*. *Autism in Adulthood*, v. 5, n. 4, p. 411–422, 2023. DOI [10.1089/aut.2022.0024](https://doi.org/10.1089/aut.2022.0024). O artigo apareceu primeiro on-line em setembro de 2022 e foi publicado no fascículo de dezembro de 2023; o ano bibliográfico adotado é 2023.

**Pergunta e método.** O estudo pergunta quais espaços públicos são experimentados como sensorialmente incapacitantes ou facilitadores por adultos autistas e quais características produzem essas experiências. Foram recrutados 24 adultos autistas, distribuídos em sete grupos focais on-line com dois a quatro participantes. Os autores aplicaram análise de conteúdo, análise temática reflexiva e análise de casos. O estudo foi participativo: uma integrante da equipe era autista e um grupo de cinco adultos autistas revisou a interpretação dos resultados. Os participantes podiam usar fala, escrita ou ambas, manter a câmera desligada e fazer pausas.

**Resultados.** Supermercados, estabelecimentos de alimentação, centros urbanos, transporte público, serviços de saúde e lojas ou centros comerciais apareceram com frequência como ambientes incapacitantes. A análise produziu seis princípios interligados:

- **paisagem sensorial:** carga, duração, impossibilidade de escapar e falta de controle sobre estímulos;
- **espaço:** aglomeração e confinamento;
- **previsibilidade:** incerteza, inconsistência, falta de familiaridade e falta de informação prévia;
- **compreensão:** julgamento, incompreensão e ausência de apoio;
- **adaptações:** comunicação inflexível, pressão de tempo e soluções inadequadas;
- **recuperação:** inexistência de local de escape e dificuldade para se preparar ou recuperar.

Os participantes relataram que a exigência de comunicação falada pode ser difícil ou gerar ansiedade, sobretudo quando a sobrecarga sensorial reduz a capacidade de falar. Aplicativos, ferramentas on-line e sinalização foram mencionados como alternativas que podem permitir comunicação sem fala. Informações antecipadas sobre o ambiente e seus procedimentos aumentam a previsibilidade. Espaços silenciosos, com menos pessoas, ruído e iluminação, podem oferecer uma possibilidade de pausa e recuperação.

**Uso recomendado no FLIKE.** Esta é a principal referência para sustentar que um processo institucional dependente de negociação oral com funcionários pode constituir uma barreira para algumas pessoas autistas. Ela permite apresentar a solicitação web e a credencial previamente obtida como escolhas de projeto plausíveis para reduzir comunicação obrigatória e aumentar previsibilidade. Também fundamenta a importância da sala sensorial como espaço de recuperação.

**Limites.** O estudo não avaliou o FLIKE, fechaduras digitais nem a Faculdade de Direito da USP. Não demonstra que o sistema melhora acessibilidade ou reduz constrangimento; essa conclusão exige avaliação com usuários. A amostra foi recrutada on-line, concentrada no Reino Unido, composta majoritariamente por mulheres, quase toda abaixo de 35 anos e sem participantes que necessitassem de apoio por deficiência intelectual. As soluções devem ser codesenhadas e adaptadas à diversidade de pessoas autistas. Não se deve generalizar que toda pessoa autista rejeita fala, ruído ou interação humana.

**Formulação segura.** “Estudos qualitativos com adultos autistas associam a acessibilidade de espaços públicos à previsibilidade, à flexibilidade da comunicação e à disponibilidade de locais de recuperação; ferramentas digitais podem reduzir a exigência de comunicação falada em determinadas interações (MACLENNAN et al., 2023).”

**Inserção prevista.** Capítulo 1, contextualização do problema; Capítulo 2, acessibilidade e autismo; Capítulo 3, justificativa das decisões de interação; Capítulo 6, limites da ausência de avaliação com usuários.

### C02 — Tola et al. (2021): ambiente construído e pessoas autistas

**Identificação.** Giulia Tola, Valentina Talu, Tanja Congiu, Paul Bain e Jutta Lindert. *Built Environment Design and People with Autism Spectrum Disorder (ASD): A Scoping Review*. *International Journal of Environmental Research and Public Health*, v. 18, n. 6, art. 3203, 2021. DOI [10.3390/ijerph18063203](https://doi.org/10.3390/ijerph18063203).

**Pergunta e método.** A revisão de escopo mapeia a literatura sobre a relação entre autismo e projeto do ambiente construído e busca requisitos espaciais recorrentes. Seguiu a metodologia do Joanna Briggs Institute, documentou a seleção em fluxo PRISMA e pesquisou PubMed, Scopus, PsycINFO e Web of Science, além de busca manual. Dos 801 registros inicialmente identificados, apenas 21 estudos atenderam aos critérios.

**Resultados.** A síntese organiza o projeto de espaços amigáveis a pessoas autistas em três grupos principais: qualidade sensorial, inteligibilidade e orientação. Entre as recomendações recorrentes estão ambientes de baixa estimulação, espaços de transição, áreas silenciosas, organização espacial simples, relações visuais claras, previsibilidade, possibilidade de escolha de percurso e apoios de orientação. Espaços silenciosos são descritos, nas fontes revisadas, como pequenos, neutros, com poucas distrações e alguma possibilidade de personalização; uma relação visual controlada com o entorno pode permitir supervisão sem eliminar o refúgio.

**Uso recomendado no FLIKE.** A fonte ajuda a explicar a função arquitetônica de uma sala sensorial e por que acesso previsível e autônomo a esse espaço pode ser relevante. Também fornece uma base para distinguir a acessibilidade física ou sensorial do ambiente da acessibilidade digital do mecanismo de acesso.

**Limites.** A literatura encontrada é pequena, heterogênea e concentrada nos Estados Unidos, Reino Unido e Egito. Predominam crianças, ambientes educacionais, residenciais e de cuidado; há poucos estudos com adultos e nenhum estudo elegível sobre redesenho urbano. A revisão consultou quatro bases e excluiu autobiografias, teses e trabalhos de conferência. Os critérios não são prescrições universais e não fundamentam, por si, um sistema de controle de acesso.

**Formulação segura.** “Uma revisão de escopo identificou qualidade sensorial, inteligibilidade e orientação como dimensões recorrentes no projeto de ambientes para pessoas autistas, incluindo espaços silenciosos e organização previsível, mas ressaltou a limitação e a concentração da evidência disponível (TOLA et al., 2021).”

**Inserção prevista.** Capítulo 1, função da sala sensorial; Capítulo 2, ambiente construído e acessibilidade; Capítulo 6, necessidade de validação contextual com usuários da USP.

### C03 — Governo Federal (2014): eMAG 3.1

**Identificação.** Brasil, Ministério do Planejamento, Orçamento e Gestão, Secretaria de Logística e Tecnologia da Informação. *eMAG: Modelo de Acessibilidade em Governo Eletrônico*, versão 3.1. Brasília, 2014.

**Natureza e estrutura.** O eMAG adapta recomendações internacionais de acessibilidade web ao contexto do governo brasileiro. O processo proposto combina três ações: uso de padrões web e código semântico, aplicação de recomendações de acessibilidade e avaliação. O documento organiza 45 recomendações em marcação, comportamento, conteúdo, apresentação, multimídia e formulários.

**Avaliação.** Validadores automáticos ajudam a encontrar problemas, mas não determinam sozinhos se uma página é acessível. O eMAG recomenda verificação manual, navegação apenas por teclado, uso de leitores de tela e outras tecnologias assistivas. O teste final com pessoas com deficiência é apresentado como necessário para avaliar se o sítio é acessível, compreensível e utilizável. A acessibilidade deve ser mantida e reavaliada após mudanças.

**Critérios úteis ao FLIKE.** Para a aplicação web, o documento pode fundamentar:

- operação por teclado e ordem lógica de foco;
- foco visualmente perceptível;
- contraste entre texto e fundo;
- redimensionamento sem perda de funcionalidade;
- ausência de atualização ou redirecionamento automático inesperado;
- possibilidade de ajustar limites de tempo;
- rótulos associados a campos e instruções claras;
- identificação textual de erros e confirmação de envio;
- agrupamento lógico de campos;
- cautela com CAPTCHA inacessível.

**Uso recomendado no FLIKE.** O eMAG deve transformar requisitos vagos, como “interface acessível”, em critérios verificáveis no Capítulo 4 e em procedimentos de avaliação no Capítulo 5. Como o sistema atende uma instituição pública, o documento também fornece uma referência brasileira pertinente, embora o escopo jurídico específico da implantação ainda precise ser analisado.

**Limites.** A versão 3.1 é de 2014 e se baseia principalmente na WCAG 2.0. Ela não substitui a conferência dos critérios atuais da WCAG 2.2. O documento não é específico para autismo e a mera adoção de algumas recomendações não autoriza declarar conformidade integral. O frontend ainda precisa ser auditado e testado com usuários.

**Formulação segura.** “A avaliação de acessibilidade não se encerra em validadores automáticos; o eMAG combina inspeção manual, tecnologias assistivas e testes com pessoas com deficiência, além de prever manutenção contínua (BRASIL, 2014).”

**Inserção prevista.** Capítulo 2, acessibilidade digital; Capítulo 4, requisitos não funcionais de acessibilidade; Capítulo 5, método e resultados da auditoria do frontend.

### C04 — Dworkin (2005, atualização de 2016): NIST SP 800-38B

**Identificação.** Morris Dworkin. *Recommendation for Block Cipher Modes of Operation: The CMAC Mode for Authentication*. NIST Special Publication 800-38B, 2005, com atualização de 2016. DOI [10.6028/NIST.SP.800-38B](https://doi.org/10.6028/NIST.SP.800-38B).

**Conteúdo normativo.** A publicação especifica o CMAC, código de autenticação de mensagem baseado em cifra de bloco simétrica. O mecanismo busca dar garantia de autenticidade da origem que executou a geração do MAC e, por consequência, integridade dos dados binários. Ele detecta alterações intencionais ou acidentais com probabilidade associada ao tamanho da tag e aos limites de uso da chave.

**Operação.** Para AES, o bloco tem 128 bits. Duas subchaves são derivadas da cifração do bloco zero. Quando o último bloco da mensagem é completo, ele é combinado com a primeira subchave; quando é incompleto, recebe preenchimento e é combinado com a segunda. O encadeamento CBC produz a tag, que pode ser truncada conforme uma política fixa para a chave. Na verificação, o receptor calcula o CMAC da mensagem recebida e compara a tag produzida com a apresentada.

**Tamanho da tag e volume.** Tags maiores resistem melhor a tentativas de adivinhação. O documento indica que, para a maioria das aplicações, pelo menos 64 bits oferecem proteção suficiente e que comprimentos menores exigem análise cuidadosa e limite de tentativas inválidas. Para AES, a recomendação geral limita uma chave a no máximo `2^48` mensagens; dentro desse limite, e supondo ausência de fraqueza na cifra, a probabilidade esperada de colisão fica abaixo de uma em um bilhão. Esses limites gerais não substituem uma análise de risco do protocolo do FLIKE.

**Repetição.** O ponto mais importante para o projeto é que CMAC **não impede replay**. Um atacante pode copiar uma mensagem legítima e sua tag e apresentá-las novamente. A aplicação pode incorporar número sequencial, timestamp ou nonce ao início da mensagem para ajudar a detectar repetições, mensagens fora de ordem ou ausentes. No FLIKE, o intervalo temporal limita quando a credencial pode ser aceita, mas a reapresentação durante o intervalo é deliberadamente permitida. Isso corresponde à regra de múltiplas entradas e saídas enquanto a autorização estiver vigente.

**Uso recomendado no FLIKE.** C04 deve ser a autoridade principal para explicar o que AES-CMAC faz, por que a tag cobre todos os campos do payload e por que alteração do identificador da tranca ou da janela temporal invalida a credencial. Também sustenta a distinção entre autenticação do payload e prevenção de repetição.

**Limites.** CMAC não cifra o conteúdo, não fornece confidencialidade e não identifica sozinho a pessoa que apresentou o QR Code. Como servidor e tranca conhecem o mesmo segredo, o mecanismo não oferece não repúdio pessoal. A publicação não define provisionamento, armazenamento seguro, relógio confiável, autorização de negócio ou atuação elétrica. Em abril de 2025, o NIST anunciou que revisará a SP 800-38B; a versão final disponível deve ser conferida novamente antes da entrega.

**Formulação segura.** “O AES-CMAC permite que a tranca verifique localmente a integridade e a origem criptográfica do payload, desde que o segredo permaneça protegido; o mecanismo não cifra os dados e não impede por si só a reapresentação de uma credencial legítima (DWORKIN, 2005).”

**Inserção prevista.** Capítulo 2, autenticação de mensagens; Capítulo 4, requisitos de segurança e protocolo; Capítulo 5, implementação e testes de adulteração; Capítulo 6, limitações de replay, revogação e segredo compartilhado.

### C05 — Song et al. (2006): RFC 4493, algoritmo AES-CMAC

**Identificação.** Junhyuk Song, Radha Poovendran, Jicheol Lee e Tetsu Iwata. *The AES-CMAC Algorithm*. RFC 4493, junho de 2006. DOI [10.17487/RFC4493](https://doi.org/10.17487/RFC4493). O documento é informativo e não constitui um padrão da Internet.

**Finalidade.** O RFC torna a variante AES-CMAC-128 convenientemente disponível para implementadores. Ele define entradas, geração das subchaves, tratamento de mensagens vazias, divisão em blocos, preenchimento, geração da tag e verificação. A chave e o bloco do AES-128 têm 16 octetos; a constante usada na derivação das subchaves termina em `0x87`.

**Vetores de teste.** O documento fornece uma chave comum, as duas subchaves derivadas e quatro exemplos com mensagens de 0, 16, 40 e 64 octetos. As tags esperadas permitem testar se duas implementações independentes tratam blocos, preenchimento e ordem de bytes da mesma forma. O código C do apêndice é demonstrativo e o próprio RFC afirma que ele não foi concebido para produtos comerciais.

**Segurança.** O RFC distingue CMAC de checksum: o primeiro busca detectar modificações deliberadas, desde que o AES, o segredo e as implementações sejam confiáveis. Se a chave for comprometida ou compartilhada indevidamente, não resta garantia de autenticação nem de integridade. O comprimento padrão da tag é 128 bits; truncamento deve preservar os bits mais significativos, ser definido antes da comunicação e permanecer fixo durante a vida da chave.

**Uso recomendado no FLIKE.** C05 é a referência de implementação e interoperabilidade. Os vetores devem ser executados no backend e no firmware para demonstrar que ambos calculam AES-CMAC corretamente antes dos testes com o payload específico do FLIKE. A SP 800-38B permanece a referência conceitual principal.

**Limites.** Passar nos vetores demonstra correção do cálculo criptográfico para aquelas entradas, não a segurança do protocolo completo. O RFC não resolve proteção da chave, autorização, validade temporal, cópia do QR, revogação, logs ou acionamento físico.

**Formulação segura.** “A interoperabilidade entre backend e firmware foi verificada primeiro com os vetores de AES-CMAC-128 da RFC 4493 e depois com credenciais do formato definido pelo FLIKE (SONG et al., 2006).” Essa frase só poderá ser usada depois de os resultados dos vetores serem preservados.

**Inserção prevista.** Capítulo 4, formato do protocolo; Capítulo 5, implementação e plano de testes criptográficos.

### C06 — Barker (2020): NIST SP 800-57 Part 1 Rev. 5

**Identificação.** Elaine Barker. *Recommendation for Key Management: Part 1 — General*. NIST Special Publication 800-57 Part 1 Revision 5, maio de 2020. DOI [10.6028/NIST.SP.800-57pt1r5](https://doi.org/10.6028/NIST.SP.800-57pt1r5).

**Escopo.** A publicação reúne conceitos, tipos de chave, serviços de segurança, proteções, estados do ciclo de vida, períodos criptográficos e respostas a comprometimento. É uma orientação geral; a política concreta depende da sensibilidade dos dados, do ambiente, do volume e do risco da aplicação.

**Serviços de segurança.** O documento distingue confidencialidade, integridade, autenticação de identidade, autenticação de integridade, autenticação de origem, autorização e não repúdio. MACs simétricos podem oferecer autenticação de origem e de integridade quando a chave é exclusiva ao par de entidades. Assinaturas digitais podem, dependendo do contexto, apoiar uma decisão de não repúdio. O NIST ressalta que uma decisão real de não repúdio envolve aspectos legais e que a criptografia é apenas um elemento.

**Consequência para o vocabulário do FLIKE.** O AES-CMAC não prova que uma determinada pessoa física solicitou ou apresentou a credencial. Ele prova, sob as premissas do protocolo, que alguém com acesso ao segredo gerou o MAC. No FLIKE, servidor e ESP32-CAM compartilham esse segredo; além disso, o QR Code pode ser copiado ou compartilhado. Portanto, os logs podem oferecer **rastreabilidade operacional** e **evidência de apresentação de uma credencial associada a um usuário**, mas não irretratabilidade pessoal. A tese deve abandonar a alegação de não repúdio do usuário físico.

**Gestão do segredo.** A segurança depende de proteger a confidencialidade e a integridade da chave e sua associação ao uso correto. O NIST recomenda limitar período e volume de uso, separar chaves por finalidade e reagir a suspeita ou confirmação de comprometimento. Quando uma chave simétrica de autenticação vaza, um adversário pode modificar dados e recalcular MACs. Para uma chave desse tipo, a recomendação geral indica período de geração de MACs de no máximo dois anos e período de verificação que não se estenda mais de três anos além dele, admitindo ajustes conforme risco e ambiente.

**Uso recomendado no FLIKE.** A fonte deve sustentar os requisitos de proteção do segredo no servidor e no dispositivo, a necessidade de uma política de provisionamento e rotação e a análise das consequências de comprometimento. Mesmo que o projeto deixe a configuração ao fornecedor, a tese precisa declarar essa premissa e tratá-la como limite de implantação.

**Limites.** A publicação não prescreve a forma concreta de armazenar a chave no ESP32-CAM nem prova que o firmware atual a protege. Os períodos indicados são recomendações gerais, não uma política automaticamente adequada ao FLIKE. A implementação preservada não demonstra rotação, revogação de segredo ou resposta a comprometimento.

**Formulação segura.** “A segurança do MAC depende da proteção do segredo compartilhado; seu comprometimento permite que um terceiro produza credenciais com tags válidas. Por isso, período de uso, separação por finalidade e resposta a comprometimento integram o problema de gestão de chaves (BARKER, 2020).”

**Inserção prevista.** Capítulo 2, serviços de segurança; Capítulo 4, premissas e requisitos; Capítulo 5, provisionamento assumido; Capítulo 6, limitações e trabalhos futuros.

### C07 — DENSO ADC (2012): fundamentos do QR Code

**Identificação.** DENSO ADC. *QR Code Essentials*. 2012. Documento técnico do grupo associado ao criador do QR Code.

**Conteúdo técnico.** O QR Code é um código bidimensional matricial cujos módulos claros e escuros representam dados e padrões funcionais. Padrões de posição em três cantos permitem localizar e orientar o símbolo; padrões de alinhamento compensam distorção; o padrão de temporização ajuda a determinar o tamanho dos módulos; uma zona livre de quatro módulos separa o símbolo do entorno.

Há 40 versões, da versão 1 com 21 × 21 módulos à versão 40 com 177 × 177. Cada versão acrescenta quatro módulos por lado. Capacidade depende da versão, do modo de codificação e do nível de correção de erros. A correção Reed–Solomon possui quatro níveis aproximados: L, 7%; M, 15%; Q, 25%; H, 30%. Maior correção melhora tolerância a sujeira ou dano, mas aumenta o símbolo necessário para o mesmo payload. O documento recomenda geradores conformes à ISO/IEC 18004 e discute tamanho, resolução, contraste e qualidade de impressão ou exibição.

**Uso recomendado no FLIKE.** A fonte pode explicar por que o QR Code é um suporte adequado para transportar o payload binário e quais fatores afetam a leitura pela câmera. Pode orientar o registro, no Capítulo 5, da versão gerada, nível de correção, tamanho na tela, distância e iluminação usados nos testes.

**Limites.** Correção de erros restaura dados diante de dano; ela não autentica o emissor e não impede cópia. O documento é material do fabricante, não um artigo de segurança nem a própria norma ISO/IEC 18004. Alegações promocionais de velocidade devem ser evitadas se não forem necessárias.

**Formulação segura.** “O QR Code oferece capacidade binária, leitura multidirecional e correção de erros; essas propriedades favorecem a captura óptica, mas não fornecem autenticidade criptográfica ao conteúdo (DENSO ADC, 2012).”

**Inserção prevista.** Capítulo 2, codificação bidimensional; Capítulo 4, representação da credencial; Capítulo 5, condições dos ensaios de leitura.

### C08 — Kieseberg et al. (2010): QR Code como vetor de ataque

**Identificação.** Peter Kieseberg, Manuel Leithner, Martin Mulazzani, Lindsay Munroe, Sebastian Schrittwieser, Mayank Sinha e Edgar Weippl. *QR Code Security*. In: *Proceedings of the 8th International Conference on Advances in Mobile Computing and Multimedia*, p. 430–435, 2010. DOI [10.1145/1971519.1971593](https://doi.org/10.1145/1971519.1971593).

**Problema e método.** O artigo analisa a estrutura do QR Code sob a perspectiva de um atacante e propõe cenários contra pessoas e processos automatizados. O modelo considera tanto a substituição completa do símbolo por um adesivo quanto alterações de módulos, inclusive um caso restrito em que só módulos claros podem ser escurecidos.

**Resultados.** Como o conteúdo não é legível diretamente por pessoas, um usuário pode não perceber que um código foi substituído. Em aplicações gerais, isso permite phishing, redirecionamento e fraude. Em processos automatizados, dados decodificados e tratados sem validação podem alcançar bancos de dados ou comandos, criando possibilidades de injeção. O artigo também discute manipulação de máscara, modo, contador de caracteres, segmentos, dados e palavras de correção.

**Uso recomendado no FLIKE.** A referência sustenta duas decisões:

1. o QR Code deve ser tratado como canal e entrada não confiável, não como prova de autenticidade;
2. o firmware deve validar estritamente comprimento, estrutura, tipos, identificador da tranca, intervalo temporal e tag antes de qualquer sinal de abertura.

No FLIKE, a tag AES-CMAC é o mecanismo que detecta alteração do payload. Um código legítimo ainda pode ser fotografado ou compartilhado, e a correção de erros não evita esse risco. Ataques de URL e navegador discutidos no artigo não se aplicam diretamente ao parser binário fixo do firmware, mas ilustram o erro geral de confiar no dado decodificado.

**Limites.** O trabalho é de 2010, é predominantemente analítico e não avalia o protocolo do FLIKE. Nem toda técnica proposta foi demonstrada em um sistema real. A tese não deve afirmar que o artigo prova vulnerabilidades específicas no firmware sem teste correspondente.

**Formulação segura.** “O conteúdo de um QR Code deve ser tratado como entrada não confiável; a leitura óptica e a correção de erros não garantem autenticidade, e o dado decodificado precisa ser validado antes de acionar um processo automatizado (KIESEBERG et al., 2010).”

**Inserção prevista.** Capítulo 2, ameaças de QR Code; Capítulo 4, validações do protocolo; Capítulo 5, testes negativos de payload e de cópia.

### C09 — Brasil (2018): Lei Geral de Proteção de Dados Pessoais

**Identificação.** Brasil. Lei nº 13.709, de 14 de agosto de 2018, Lei Geral de Proteção de Dados Pessoais. Foi lido o texto compilado oficial do Planalto capturado em 1º de setembro de 2026, já com alterações da Lei nº 15.352/2026.

**Conceitos pertinentes.** Dado pessoal é informação relacionada a pessoa natural identificada ou identificável. Tratamento abrange coleta, acesso, processamento, armazenamento, comunicação, modificação e eliminação, entre outras operações. Assim, solicitações, permissões e eventos de acesso vinculados a uma conta ou pessoa constituem dados pessoais. Um log de acesso não se torna automaticamente dado pessoal sensível; essa classificação depende do conteúdo e das associações efetivamente armazenadas.

**Princípios.** Para o FLIKE, os princípios mais úteis do art. 6º são:

- finalidade específica e informada;
- adequação ao contexto;
- necessidade, limitada ao mínimo de dados pertinente e não excessivo;
- transparência e livre acesso;
- segurança contra acesso ou alteração não autorizados;
- prevenção de danos;
- responsabilização e prestação de contas.

O art. 37 exige que controlador e operador mantenham registro das operações de tratamento. Os arts. 46 e 49 exigem medidas técnicas e administrativas de segurança desde a concepção e sistemas estruturados segundo segurança, boas práticas, governança e princípios gerais. Os arts. 15, 16 e 18 tratam de término do tratamento, conservação permitida e direitos do titular.

**Uso recomendado no FLIKE.** A lei fundamenta requisitos para informar a finalidade dos logs, restringir os campos armazenados, controlar o acesso administrativo, definir retenção e permitir o exercício de direitos. Ela também ajuda a separar o registro técnico necessário da coleta excessiva. Se o sistema registrar vínculo com uma sala sensorial destinada a pessoas autistas, a equipe deve analisar cuidadosamente se combinações de dados podem revelar informação de saúde; isso não deve ser presumido nem descartado sem análise do caso de uso.

**Limites.** Este fichamento não é parecer jurídico e não determina a base legal do tratamento em uma futura implantação na USP. O responsável institucional, as finalidades, o regime aplicável ao poder público, a retenção e os procedimentos de atendimento ao titular ainda precisam ser definidos. O protótipo acadêmico não pode ser declarado conforme à LGPD sem essa análise e sem verificação técnica e organizacional.

**Formulação segura.** “Solicitações, permissões e eventos associados a uma pessoa identificada são dados pessoais; seu tratamento deve observar finalidade, necessidade, transparência, segurança e prevenção, além de uma política explícita de retenção e acesso (BRASIL, 2018).”

**Inserção prevista.** Capítulo 2, privacidade e proteção de dados; Capítulo 4, requisitos de logs e segurança; Capítulo 5, modelo de dados e controles; Capítulo 6, limites de implantação.

### C10 — Espressif Systems (2026): datasheet do ESP32

**Identificação.** Espressif Systems. *ESP32 Series Datasheet*, versão 5.3, julho de 2026. O documento cobre a família de SoCs ESP32; ele não é um datasheet específico da placa comercial ESP32-CAM nem da câmera OV2640.

**Recursos relevantes.** A família integra processadores Xtensa LX6 de 32 bits com uma ou duas unidades, até 240 MHz, 448 KB de ROM, 520 KB de SRAM e 16 KB de SRAM RTC. O SoC possui GPIOs programáveis, interfaces SPI, I2C, UART e I2S, além de aceleradores de AES, SHA e RSA e gerador de números aleatórios. Esses recursos contextualizam a execução local da leitura, do parser e do cálculo criptográfico, mas o uso real depende do módulo e do firmware.

**Condições elétricas.** Para os domínios de 3,3 V, a alimentação recomendada tem valor típico de 3,3 V e máximo de 3,6 V, com capacidade externa mínima indicada de 0,5 A. Em condições de 3,3 V e 25 °C, o datasheet informa corrente típica de fonte de nível alto de 40 mA para certos domínios de GPIO, 20 mA no domínio VDD_SDIO, e corrente típica de dreno de nível baixo de 28 mA, sob condições especificadas. Esses valores descrevem o SoC e não autorizam alimentar diretamente uma fechadura elétrica.

**Relação com o circuito.** A saída lógica do ESP32-CAM deve comandar um estágio de potência. O circuito de transistores do FLIKE recebe o nível lógico e fornece à tranca a corrente e tensão provenientes de sua fonte. O datasheet ajuda a justificar essa separação; o dimensionamento exato exige o esquema, os componentes, a corrente da tranca e a análise do circuito construído.

**Uso recomendado no FLIKE.** C10 deve fornecer dados do fabricante para a descrição do microcontrolador, interfaces e limites de GPIO. A evidência de que o protótipo leu a credencial e acionou a tranca continua sendo o ensaio próprio da equipe, não o datasheet.

**Limites.** O documento cobre chips da família e lista alguns números de peça como não recomendados para novos projetos ou encerrados. O módulo exato da placa precisa ser identificado antes de associar a ele um estado de ciclo de vida. A presença de acelerador AES não demonstra que a biblioteca de CMAC usada pelo firmware o aproveita. O datasheet não documenta a câmera, a placa ESP32-CAM completa, o circuito de transistores ou a fechadura.

**Formulação segura.** “A saída GPIO do ESP32 opera em níveis lógicos e correntes muito inferiores às exigidas por uma fechadura elétrica; por isso, o protótipo utiliza um estágio externo de potência comandado pelo sinal do microcontrolador (ESPRESSIF SYSTEMS, 2026).” A redação final deverá ser acompanhada dos valores do circuito real.

**Inserção prevista.** Capítulo 2, sistemas embarcados; Capítulo 5, hardware, circuito e implementação; Capítulo 6, limites de produto e dimensionamento.

## 5. Síntese transversal para a tese

### 5.1 Cadeia argumentativa recomendada

As fontes permitem construir uma sequência que conecta o problema social à solução técnica sem afirmar resultados ainda inexistentes:

1. Pessoas autistas podem enfrentar barreiras sensoriais, comunicacionais e de previsibilidade em espaços públicos (C01).
2. Espaços silenciosos e previsíveis aparecem na literatura de ambiente construído como recursos potencialmente úteis, embora a evidência seja limitada e heterogênea (C02).
3. No caso relatado pela equipe, o acesso à sala sensorial dependia de uma interação informal com funcionários; o FLIKE foi concebido para formalizar solicitação, autorização e apresentação da credencial. Essa é uma decisão dos autores, sustentada pelo relato do contexto, não um resultado de C01 ou C02.
4. A aplicação web precisa atender critérios verificáveis de acessibilidade e ser avaliada manualmente e com usuários (C03).
5. O QR Code transporta dados de forma legível por câmera e tolerante a dano, mas não autentica o conteúdo (C07 e C08).
6. O AES-CMAC fornece integridade e autenticação criptográfica do payload sob um segredo compartilhado, sem confidencialidade nem prevenção inerente de repetição (C04 e C05).
7. A validade por intervalo e a associação à tranca compõem a política do FLIKE. A mesma credencial pode ser reapresentada durante o período autorizado; credenciais expiradas devem ser rejeitadas. Isso deve ser chamado de **autorização temporária reutilizável durante sua vigência**, não “uso único”.
8. O segredo precisa de proteção, separação por finalidade, período de uso e resposta a comprometimento (C06).
9. Solicitações, permissões e logs vinculados a pessoas exigem finalidade, minimização, proteção e política de retenção (C09).
10. O ESP32 executa a decisão e emite um sinal lógico; o acionamento da tranca requer o estágio externo de potência construído pela equipe (C10 e evidências próprias do protótipo).

### 5.2 Vocabulário técnico controlado

| Expressão | Uso na tese | Justificativa |
| --- | --- | --- |
| **autenticação do payload** | Preferir | O CMAC verifica origem criptográfica e integridade sob a chave compartilhada. |
| **autorização temporária reutilizável durante a vigência** | Preferir | A chave pode ser apresentada várias vezes no intervalo autorizado e deve falhar fora dele. |
| **validação offline na tranca** | Preferir | A decisão local não consulta o servidor no momento da leitura. O usuário ainda precisa de internet para solicitar e obter a credencial. |
| **rastreabilidade operacional** | Preferir para logs | Os registros podem associar eventos a credenciais e contas, conforme os dados realmente coletados. |
| **evidência de apresentação da credencial** | Usar com ressalva | Um evento prova que uma credencial foi lida e aceita segundo as premissas do sistema; não prova presença física exclusiva do titular. |
| **assinatura digital** | Não usar para AES-CMAC | CMAC é um código simétrico de autenticação de mensagem. |
| **irretratabilidade ou não repúdio do usuário físico** | Não alegar | Servidor e tranca compartilham o segredo; o QR pode ser copiado; não há assinatura pessoal nem vínculo físico exclusivo. |
| **QR Code seguro** | Evitar | A segurança depende do protocolo e da validação do payload, não do suporte óptico isolado. |
| **conformidade com eMAG ou LGPD** | Não alegar sem auditoria | O projeto ainda não foi submetido à avaliação técnica, de usuários ou jurídica necessária. |

### 5.3 Mapa de citações por capítulo

| Parte futura da tese | Afirmações externas que podem ser sustentadas | Fontes prioritárias | Evidência própria que ainda será necessária |
| --- | --- | --- | --- |
| Cap. 1 — problema e justificativa | Barreiras sensoriais, comunicação inflexível, previsibilidade e função de espaços de recuperação | C01, C02 | Relato documentado do contexto da Sanfran e origem do problema |
| Cap. 2 — autismo e ambiente | Relação entre ambiente, qualidade sensorial, inteligibilidade, orientação e quiet spaces | C01, C02 | Nenhuma para conceitos; validação local para aplicação ao caso |
| Cap. 2 — acessibilidade digital | Processo de desenvolvimento e avaliação acessível | C03 | Auditoria do frontend e, idealmente, teste com público-alvo |
| Cap. 2 — QR Code | Estrutura, versões, zona livre, capacidade, correção de erros e riscos de entrada não confiável | C07, C08 | Parâmetros efetivos de geração e leitura no FLIKE |
| Cap. 2 — segurança criptográfica | Integridade, autenticação de origem, replay, tamanho de tag e gestão de segredo | C04, C05, C06 | Formato exato, tag adotada, chave, comparação e resultados dos testes |
| Cap. 2 — privacidade | Natureza pessoal dos registros e princípios de finalidade, necessidade e segurança | C09 | Inventário dos campos e política institucional de tratamento |
| Cap. 4 — requisitos | Critérios de acessibilidade, validação estrita, proteção da chave e logs mínimos | C03, C04, C06, C08, C09 | Matriz RF/RNF e critérios verificáveis do projeto |
| Cap. 5 — hardware | Recursos do ESP32 e necessidade de estágio externo para a carga | C10 | Esquema, componentes, valores e fotografias do circuito FLIKE |
| Cap. 5 — protocolo e testes | Algoritmo, vetores AES-CMAC e testes de adulteração, validade e tranca incorreta | C04, C05 | Logs e resultados reproduzíveis do backend e firmware |
| Cap. 6 — limitações | Revogação offline, cópia, comprometimento de chave, ausência de não repúdio e avaliação de usuários | C01, C04, C06, C08, C09 | Discussão honesta do estado e dos testes executados |

## 6. Afirmações permitidas e afirmações proibidas

### 6.1 Afirmações bem sustentadas

- Ambientes públicos podem se tornar incapacitantes para adultos autistas por combinação de estímulos, imprevisibilidade, comunicação inflexível e falta de espaço de recuperação (C01).
- Espaços silenciosos e organização previsível aparecem como recomendações recorrentes na literatura de projeto para pessoas autistas, ainda que a base empírica seja limitada (C02).
- Avaliação de acessibilidade exige mais que validadores automáticos e deve incluir inspeção manual e pessoas com deficiência (C03).
- CMAC autentica e protege a integridade de uma mensagem sob chave simétrica, mas não cifra o conteúdo e não impede replay por si só (C04).
- A RFC 4493 fornece vetores oficiais adequados para testar uma implementação AES-CMAC-128 (C05).
- Comprometimento da chave de MAC permite que um adversário produza tags válidas; gestão do ciclo de vida é parte da segurança (C06).
- Correção de erros do QR Code melhora a leitura de símbolos danificados, mas não fornece autenticidade (C07 e C08).
- Registros vinculados a pessoas identificadas são dados pessoais e devem observar finalidade, necessidade e segurança (C09).
- A saída lógica do ESP32 requer um estágio externo para controlar uma carga elétrica incompatível com seus limites de GPIO (C10, completada pelo circuito próprio).

### 6.2 Afirmações que as fontes não autorizam

- “O FLIKE comprovadamente melhora a acessibilidade de pessoas autistas.” Não houve estudo com usuários.
- “Toda pessoa autista prefere uma interface digital a falar com funcionários.” A população é heterogênea.
- “O FLIKE está conforme ao eMAG, à WCAG ou à LGPD.” Ainda faltam auditorias e definições institucionais.
- “O QR Code garante segurança, autenticidade ou sigilo.” Ele apenas codifica e transporta os dados.
- “O AES-CMAC impede que a credencial seja copiada ou reapresentada.” CMAC não impede replay.
- “A tag AES-CMAC é uma assinatura digital do usuário.” O mecanismo é simétrico e a chave não pertence exclusivamente ao usuário.
- “Os logs provam que a pessoa física entrou, saiu ou ocupou a sala.” O sistema observa leitura e aceitação da credencial e, dependendo do sensor existente, acionamento; não observa necessariamente passagem ou ocupação.
- “O datasheet comprova o funcionamento do protótipo.” A demonstração física precisa de evidência do ensaio da equipe.

## 7. Lacunas bibliográficas e probatórias remanescentes

O conjunto resolve grande parte das lacunas do fichamento original, mas não encerra a pesquisa transversal. Antes dos blocos correspondentes, ainda será necessário buscar ou produzir:

1. **WCAG 2.2:** fonte atual para critérios não cobertos ou atualizados desde o eMAG 3.1;
2. **relógio confiável em credenciais offline:** ameaça de atraso, reinicialização ou manipulação do relógio do dispositivo;
3. **provisionamento no ESP32-CAM:** documentação do mecanismo efetivamente adotado para gravar e proteger identificador e segredo;
4. **biblioteca de QR Code e de CMAC:** versão, documentação e comportamento das dependências concretas do firmware e backend;
5. **placa e câmera:** datasheets do módulo ESP32-CAM e do sensor OV2640 efetivamente usados;
6. **circuito elétrico:** datasheets dos transistores, fonte e fechadura e valores reais do esquema final;
7. **evidência institucional:** documento, ata, notícia ou relato formal sobre a sala sensorial da Faculdade de Direito e seu fluxo de acesso;
8. **avaliação com o público-alvo:** protocolo, consentimento, critérios éticos e resultados, se a equipe decidir realizar o estudo;
9. **política de dados da implantação:** controlador, base legal, retenção, direitos, controle de acesso e resposta a incidentes;
10. **resultados reproduzíveis:** vetores AES-CMAC, casos de QR válido e inválido, validade temporal, tranca incorreta, repetição permitida, latência e taxa de sucesso.

Esses itens não exigem adicionar todos os documentos agora. A regra do plano permanece: buscar a fonte necessária antes do bloco que depende dela e inserir a citação no mesmo parágrafo da alegação.

## 8. Decisões para a redação futura

1. C01 e C02 serão as fontes iniciais da motivação relacionada ao autismo, sempre sem atribuir ao FLIKE benefícios que não foram avaliados.
2. C03 será convertida em critérios verificáveis; a WCAG 2.2 será consultada antes da auditoria final do frontend.
3. C04 será a autoridade conceitual para CMAC, enquanto C05 será usada para algoritmo e vetores de teste.
4. C06 substitui a noção imprecisa de “irretratabilidade do usuário” por autenticação de origem, integridade e rastreabilidade operacional com limitações explícitas.
5. C07 e C08 serão citadas juntas quando for necessário distinguir robustez óptica de autenticidade criptográfica.
6. C09 fundamentará a modelagem mínima de logs, mas qualquer afirmação de conformidade dependerá de análise institucional e técnica posterior.
7. C10 será usado somente para o SoC ESP32. Placa, câmera, componentes e fechadura receberão fontes específicas quando seus modelos forem confirmados.
8. As referências complementarão, sem substituir automaticamente, as oito fontes originais. Trabalhos relacionados sobre outras fechaduras continuam úteis para comparação arquitetural.
9. Páginas ou seções serão indicadas quando a afirmação for técnica, normativa ou potencialmente controversa.
10. Antes da entrega, será conferida a vigência da LGPD compilada, a eventual nova revisão da NIST SP 800-38B e a versão atual da documentação do ESP32.
