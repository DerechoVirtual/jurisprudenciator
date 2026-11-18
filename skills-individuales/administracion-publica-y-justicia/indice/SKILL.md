---
name: indice
description: "Índice de los 58 formularios de delitos contra la administración pública y de justicia (malversación, prevaricación, fraude, enriquecimiento ilícito, urbanismo, falso testimonio, denuncia falsa, diputados y senadores). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Delitos contra la Administración pública y de justicia: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Ordenanzas municipales** (tráfico, urbanismo, tributos locales, convivencia) → `buscar_ordenanzas` → `leer_ordenanza`.
- **Inmuebles** (referencia catastral, superficie, uso) → `consultar_catastro` (y `callejero_catastro` para localizar la dirección).

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/administracion-publica-y-justicia:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 124 | Enriquecimiento ilícito: conformidad de la defensa | 2023 | `enriquecimiento-ilicito-conformidad-defensa-124` |
| 243 | Intrusismo profesional: conformidad de la defensa | 2022 | `intrusismo-profesional-conformidad-defensa-243` |
| 281 | Funcionario que deniega una prestación por discriminación: conformidad de la defensa | 2021 | `funcionario-deniega-prestacion-discriminacion-281` |
| 382 | Falso testimonio: conformidad de la defensa | 2021 | `falso-testimonio-conformidad-defensa-382` |
| 443 | Infidelidad en la custodia de documentos: defensa con conformidad | 2020 | `infidelidad-custodia-documentos-defensa-conformidad-443` |
| 472 | Fraude a la Administración: defensa con conformidad | 2019 | `fraude-administracion-defensa-conformidad-472` |

## Recursos e impugnaciones (9)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 126 | Enriquecimiento ilícito: apelación contra la condena | 2023 | `enriquecimiento-ilicito-apelacion-contra-condena-126` |
| 242 | Intrusismo profesional: apelación contra la condena | 2022 | `intrusismo-profesional-apelacion-contra-condena-242` |
| 278 | Funcionario que deniega una prestación por discriminación: apelación contra la condena | 2021 | `funcionario-deniega-prestacion-discriminacion-apelacion-278` |
| 380 | Falso testimonio: apelación contra la condena | 2021 | `falso-testimonio-apelacion-contra-condena-380` |
| 439 | Infidelidad en la custodia de documentos: apelación contra la condena | 2020 | `infidelidad-custodia-documentos-apelacion-contra-condena-439` |
| 453 | Prevaricación urbanística: apelación de la autoridad o funcionario condenado (todas las CCAA) | 2020 | `prevaricacion-urbanistica-apelacion-autoridad-453` |
| 456 | Delito urbanístico: apelación del constructor condenado (todas las CCAA) | 2020 | `delito-urbanistico-apelacion-constructor-condenado-todas-456` |
| 475 | Apelación contra la condena por fraude a la Administración | 2019 | `apelacion-contra-condena-fraude-administracion-475` |
| 501 | Apelación contra la condena por malversación | 2019 | `apelacion-contra-condena-malversacion-501` |

## Querellas y denuncias (16)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 96 | Diputado o senador: querella ante el juez de instrucción | 2023 | `diputado-senador-querella-ante-juez-instruccion-96` |
| 97 | Diputado o senador: querella ante el Tribunal Supremo | 2023 | `diputado-senador-querella-ante-tribunal-supremo-97` |
| 125 | Enriquecimiento ilícito: querella | 2023 | `enriquecimiento-ilicito-querella-125` |
| 245 | Intrusismo profesional: denuncia | 2022 | `intrusismo-profesional-denuncia-245` |
| 280 | Funcionario que deniega una prestación por discriminación: querella | 2021 | `funcionario-deniega-prestacion-discriminacion-querella-280` |
| 403 | Falso testimonio: querella | 2020 | `falso-testimonio-querella-403` |
| 442 | Infidelidad en la custodia de documentos: querella | 2020 | `infidelidad-custodia-documentos-querella-442` |
| 455 | Prevaricación urbanística de autoridad o funcionario: querella (todas las CCAA) | 2020 | `prevaricacion-urbanistica-autoridad-funcionario-querella-455` |
| 463 | Delito urbanístico: querella contra el constructor (todas las CCAA) | 2020 | `delito-urbanistico-querella-contra-constructor-todas-463` |
| 473 | Fraude a la Administración Pública: querella | 2019 | `fraude-administracion-publica-querella-473` |
| 502 | Malversación: querella | 2019 | `malversacion-querella-502` |
| 838 | Prevaricación judicial: querella | 2016 | `prevaricacion-judicial-querella-838` |
| 840 | Omisión del deber de impedir delitos: querella | 2016 | `omision-deber-impedir-delitos-querella-840` |
| 842 | Encubrimiento: querella | 2016 | `encubrimiento-querella-842` |
| 845 | Denuncia falsa: querella | 2016 | `denuncia-falsa-querella-845` |
| 878 | Desobediencia a la autoridad: querella | 2016 | `desobediencia-autoridad-querella-878` |

## Escritos de acusación (13)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 127 | Enriquecimiento ilícito: escrito de acusación | 2023 | `enriquecimiento-ilicito-escrito-acusacion-127` |
| 244 | Intrusismo profesional: escrito de acusación | 2022 | `intrusismo-profesional-escrito-acusacion-244` |
| 279 | Funcionario que deniega una prestación por discriminación: escrito de acusación | 2021 | `funcionario-deniega-prestacion-discriminacion-escrito-279` |
| 379 | Falso testimonio: escrito de acusación | 2021 | `falso-testimonio-escrito-acusacion-379` |
| 440 | Infidelidad en la custodia de documentos: calificación provisional de la acusación | 2020 | `infidelidad-custodia-documentos-calificacion-provisional-440` |
| 454 | Prevaricación urbanística de autoridad o funcionario: acusación (todas las CCAA) | 2020 | `prevaricacion-urbanistica-autoridad-funcionario-454` |
| 458 | Delito urbanístico: acusación contra el constructor (todas las CCAA) | 2020 | `delito-urbanistico-acusacion-contra-constructor-todas-458` |
| 474 | Fraude a la Administración: calificación provisional de la acusación | 2019 | `fraude-administracion-calificacion-provisional-acusacion-474` |
| 500 | Malversación: calificación provisional de la acusación | 2019 | `malversacion-calificacion-provisional-acusacion-500` |
| 839 | Prevaricación judicial: acusación | 2016 | `prevaricacion-judicial-acusacion-839` |
| 841 | Omisión del deber de impedir delitos: acusación | 2016 | `omision-deber-impedir-delitos-acusacion-841` |
| 843 | Denuncia falsa: acusación | 2016 | `denuncia-falsa-acusacion-843` |
| 844 | Encubrimiento: acusación | 2016 | `encubrimiento-acusacion-844` |

## Escritos de defensa (13)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 123 | Enriquecimiento ilícito: escrito de defensa | 2023 | `enriquecimiento-ilicito-escrito-defensa-123` |
| 241 | Intrusismo profesional: escrito de defensa | 2022 | `intrusismo-profesional-escrito-defensa-241` |
| 282 | Funcionario que deniega una prestación por discriminación: escrito de defensa | 2021 | `funcionario-deniega-prestacion-discriminacion-escrito-282` |
| 381 | Falso testimonio: escrito de defensa | 2021 | `falso-testimonio-escrito-defensa-381` |
| 441 | Infidelidad en la custodia de documentos: calificación provisional de la defensa | 2020 | `infidelidad-custodia-documentos-calificacion-provisional-441` |
| 452 | Prevaricación urbanística: defensa de la autoridad o funcionario (todas las CCAA) | 2020 | `prevaricacion-urbanistica-defensa-autoridad-funcionario-452` |
| 457 | Delito urbanístico: defensa del constructor (todas las CCAA) | 2020 | `delito-urbanistico-defensa-constructor-todas-ccaa-457` |
| 476 | Fraude a la Administración: calificación provisional de la defensa | 2019 | `fraude-administracion-calificacion-provisional-defensa-476` |
| 499 | Malversación: calificación provisional de la defensa | 2019 | `malversacion-calificacion-provisional-defensa-499` |
| 836 | Omisión del deber de impedir delitos: defensa | 2016 | `omision-deber-impedir-delitos-defensa-836` |
| 837 | Prevaricación judicial: defensa | 2016 | `prevaricacion-judicial-defensa-837` |
| 846 | Denuncia falsa: defensa | 2016 | `denuncia-falsa-defensa-846` |
| 847 | Encubrimiento: defensa | 2016 | `encubrimiento-defensa-847` |

## Solicitudes y escritos de trámite (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 99 | Diputado o senador: la acusación pide remitir la causa al Tribunal Supremo | 2023 | `diputado-senador-acusacion-pide-remitir-causa-tribunal-99` |
