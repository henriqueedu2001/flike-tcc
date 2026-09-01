# Referências da versão original do TCC

Este diretório preserva as oito obras listadas na bibliografia da versão de referência da monografia, `pdfs/FLIKE-referencia-2026-08-30.pdf`. A lista original foi conferida também em `FLIKE/capitulos/Cap6-Consideracoes.tex`.

A coleta foi realizada em 1º de setembro de 2026. Os documentos foram requisitados individualmente, com intervalo entre downloads e no máximo uma nova tentativa por arquivo, para reduzir o risco de bloqueio dos servidores. Foram priorizadas páginas oficiais, páginas dos periódicos e repositórios institucionais. Cada PDF foi verificado pelo cabeçalho do arquivo e pelo `pdfinfo`; os hashes deste diretório permitem verificar sua integridade.

## Inventário

| ID | Referência abreviada | Arquivo local | Páginas | Origem conferida | Situação de acesso |
| --- | --- | --- | ---: | --- | --- |
| R01 | Lima (2022), *SmartLock Lite* | [`R01_lima_2022_smartlock_lite.pdf`](pdfs/R01_lima_2022_smartlock_lite.pdf) | 14 | [Smart Campus Unicamp](https://smartcampus.prefeitura.unicamp.br/pub/artigos_relatorios/Gabriel_SmartLock_ESP32.pdf) | Relatório técnico público; licença de redistribuição não identificada. |
| R02 | Ho et al. (2016), *Smart Locks* | [`R02_ho_et_al_2016_smart_locks.pdf`](pdfs/R02_ho_et_al_2016_smart_locks.pdf) | 12 | [PDF disponibilizado pelo autor](https://people.csail.mit.edu/dtl/pdf/ho-smartlocks.pdf); [DOI](https://doi.org/10.1145/2897845.2897886) | Cópia pública dos autores; publicação ACM sem licença aberta indicada no PDF. |
| R03 | Gadupu et al. (2021), *ACCESS* | [`R03_gadupu_et_al_2021_access_iot_smart_lock.pdf`](pdfs/R03_gadupu_et_al_2021_access_iot_smart_lock.pdf) | 10 | [página do periódico](https://ijres.iaescore.com/index.php/IJRES/article/view/20344); [DOI](https://doi.org/10.11591/ijres.v10.i3.pp176-185) | Acesso aberto, CC BY-SA. |
| R04 | ISO/IEC/IEEE 29148:2018 | — | 92 | [catálogo ISO](https://www.iso.org/standard/72089.html); [Online Browsing Platform](https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:29148:ed-2:v1:en) | Texto integral pago; foram examinados somente metadados, resumo, sumário e termos públicos oficiais. |
| R05 | Li et al. (2018), *An Intelligent Electronic Lock* | [`R05_li_et_al_2018_intelligent_electronic_lock.pdf`](pdfs/R05_li_et_al_2018_intelligent_electronic_lock.pdf) | 8 | [DOI/IOP Publishing](https://doi.org/10.1088/1742-6596/1069/1/012134) | Acesso aberto, CC BY 3.0. |
| R06 | Asman, Permata e Fatkhurrokhman (2019), *A Prototype of Smart Lock* | [`R06_asman_et_al_2019_esp8266_smart_lock.pdf`](pdfs/R06_asman_et_al_2019_esp8266_smart_lock.pdf) | 11 | [PDF do periódico](https://journal.uad.ac.id/index.php/JITEKI/article/download/15317/pdf_35); [DOI](https://doi.org/10.26555/jiteki.v5i2.15317) | Acesso aberto, CC BY-SA 4.0. |
| R07 | IEEE Std 830-1998 | [`R07_ieee_830_1998_srs.pdf`](pdfs/R07_ieee_830_1998_srs.pdf) | 37 | [metadados oficiais IEEE](https://standards.ieee.org/ieee/830/1222/); [espelho institucional da University of Kansas](https://people.eecs.ku.edu/~hossein/Teaching/Stds/0830.pdf) | Norma substituída; cópia integral obtida de espelho universitário, sem licença aberta. |
| R08 | Kamelia et al. (2014), *Door-Automation System* | [`R08_kamelia_et_al_2014_door_automation.pdf`](pdfs/R08_kamelia_et_al_2014_door_automation.pdf) | 4 | [arquivo oficial do periódico](https://arpnjournals.com/jeas/volume_10_2014.htm); [PDF](https://www.arpnjournals.com/jeas/research_papers/rp_2014/jeas_1014_1247.pdf) | Acesso público; licença de redistribuição não identificada. |

## Observações de procedência

- O documento da Unicamp citado pela tese é o relatório técnico **IC-22-06, de novembro de 2022**, intitulado *SmartLock Lite: um sistema de controle de acesso usando o microcontrolador ESP32*. O portal possui outro relatório anterior com título semelhante; eles não são a mesma obra.
- A ISO/IEC/IEEE 29148:2018 continua sendo a edição vigente confirmada pela ISO, embora o catálogo indique que ela será revisada. O PDF integral não foi obtido por fonte não autorizada.
- O IEEE Std 830 foi publicado em 1998 e apenas reafirmado em 2009. A data “2009” usada como ano da obra na bibliografia original deve ser corrigida. A norma foi substituída pela família ISO/IEC/IEEE 29148.
- Alguns PDFs são públicos para leitura, mas não declaram licença aberta. Antes de publicar ou redistribuir este diretório, a equipe deve revisar os direitos de R01, R02, R07 e R08. Os links e hashes permitem reconstruir o acervo mesmo que esses arquivos sejam mantidos apenas localmente.
- O fichamento analítico e as recomendações de uso estão em [`docs/FICHAMENTO_REFERENCIAS_TESE_ORIGINAL.md`](../../docs/FICHAMENTO_REFERENCIAS_TESE_ORIGINAL.md). Entradas BibTeX preliminares e normalizadas estão em [`referencias-originais.bib`](referencias-originais.bib).

## Verificação

No diretório atual, execute:

```bash
sha256sum -c SHA256SUMS
```
