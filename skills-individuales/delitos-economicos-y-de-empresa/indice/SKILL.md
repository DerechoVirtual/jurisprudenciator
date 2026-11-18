---
name: indice
description: "Índice de los 52 formularios de delitos económicos y de empresa (blanqueo, delitos societarios, secretos de empresa, mercado y consumidores, delito contable tributario). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Delitos económicos y de empresa: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Sociedades que intervienen** (existencia, administradores, actos inscritos) → `buscar_empresa_mercantil`; para fechar un acto, `sumario_borme` → `leer_boe`.
- **Criterio de Hacienda y del TEAC** → `buscar_consultas_hacienda` → `leer_consulta_hacienda`; `buscar_doctrina_teac` → `leer_resolucion_teac`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/delitos-economicos-y-de-empresa:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (10)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 269 | Difusión, revelación o cesión de secretos de empresa: conformidad de la defensa | 2022 | `difusion-revelacion-cesion-secretos-empresa-conformidad-269` |
| 413 | Imposición de acuerdo societario abusivo: conformidad de la defensa | 2020 | `imposicion-acuerdo-societario-abusivo-conformidad-413` |
| 429 | Delito contable tributario para aplazar renta del local (COVID-19): conformidad (hasta el 2/4/2025) | 2020 | `delito-contable-tributario-aplazar-renta-local-covid-19-429` |
| 471 | Falseamiento de cuentas o documentos sociales (delito societario): defensa con conformidad | 2019 | `falseamiento-cuentas-documentos-sociales-delito-471` |
| 495 | Blanqueo de capitales imprudente y estafa: conformidad del abogado acusado | 2019 | `blanqueo-capitales-imprudente-estafa-conformidad-abogado-495` |
| 525 | Blanqueo de capitales tecnológico y estafa informática: defensa con conformidad | 2018 | `blanqueo-capitales-tecnologico-estafa-informatica-525` |
| 537 | Publicidad engañosa por internet: defensa con conformidad | 2018 | `publicidad-enganosa-internet-defensa-conformidad-537` |
| 543 | Falseamiento de información financiera: defensa con conformidad | 2018 | `falseamiento-informacion-financiera-defensa-conformidad-543` |
| 549 | Alteración de precios en el mercado: defensa con conformidad | 2018 | `alteracion-precios-mercado-defensa-conformidad-549` |
| 613 | Espionaje informático para descubrir secretos de empresa: defensa con conformidad | 2018 | `espionaje-informatico-descubrir-secretos-empresa-defensa-613` |

## Recursos e impugnaciones (10)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 268 | Difusión, revelación o cesión de secretos de empresa: apelación contra la condena | 2022 | `difusion-revelacion-cesion-secretos-empresa-apelacion-268` |
| 411 | Imposición de acuerdo societario abusivo: apelación contra la condena | 2020 | `imposicion-acuerdo-societario-abusivo-apelacion-contra-411` |
| 432 | Delito contable tributario para aplazar renta del local (COVID-19): apelación contra la condena | 2020 | `delito-contable-tributario-aplazar-renta-local-covid-19-432` |
| 469 | Apelación contra la condena por falseamiento de cuentas o documentos sociales (delito societario) | 2019 | `apelacion-contra-condena-falseamiento-cuentas-documentos-469` |
| 498 | Apelación contra la condena de un abogado por blanqueo imprudente y estafa | 2019 | `apelacion-contra-condena-abogado-blanqueo-imprudente-498` |
| 522 | Apelación contra la condena por blanqueo de capitales tecnológico y estafa informática | 2018 | `apelacion-contra-condena-blanqueo-capitales-tecnologico-522` |
| 536 | Apelación contra la condena por publicidad engañosa por internet | 2018 | `apelacion-contra-condena-publicidad-enganosa-internet-536` |
| 545 | Apelación contra la condena por falseamiento de información financiera por internet | 2018 | `apelacion-contra-condena-falseamiento-informacion-545` |
| 546 | Apelación contra la condena por alteración de precios en el mercado | 2018 | `apelacion-contra-condena-alteracion-precios-mercado-546` |
| 615 | Apelación contra la condena por espionaje informático para descubrir secretos de empresa | 2018 | `apelacion-contra-condena-espionaje-informatico-descubrir-615` |

## Querellas y denuncias (9)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 271 | Difusión, revelación o cesión de secretos de empresa: querella | 2022 | `difusion-revelacion-cesion-secretos-empresa-querella-271` |
| 415 | Imposición de acuerdo societario abusivo: querella | 2020 | `imposicion-acuerdo-societario-abusivo-querella-415` |
| 430 | Delito contable tributario para aplazar renta del local (COVID-19): querella | 2020 | `delito-contable-tributario-aplazar-renta-local-covid-19-430` |
| 497 | Blanqueo de capitales imprudente y estafa: querella contra el abogado y su cliente | 2019 | `blanqueo-capitales-imprudente-estafa-querella-contra-497` |
| 521 | Blanqueo de capitales tecnológico y estafa informática: querella | 2018 | `blanqueo-capitales-tecnologico-estafa-informatica-521` |
| 539 | Publicidad engañosa por internet: querella | 2018 | `publicidad-enganosa-internet-querella-539` |
| 542 | Falseamiento de información financiera por internet: querella | 2018 | `falseamiento-informacion-financiera-internet-querella-542` |
| 547 | Alteración de precios en el mercado: querella | 2018 | `alteracion-precios-mercado-querella-547` |
| 612 | Espionaje informático para descubrir secretos de empresa: querella | 2018 | `espionaje-informatico-descubrir-secretos-empresa-612` |

## Escritos de acusación (10)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 270 | Difusión, revelación o cesión de secretos de empresa: escrito de acusación | 2022 | `difusion-revelacion-cesion-secretos-empresa-escrito-270` |
| 414 | Imposición de acuerdo societario abusivo: escrito de acusación | 2020 | `imposicion-acuerdo-societario-abusivo-escrito-acusacion-414` |
| 428 | Delito contable tributario para aplazar renta del local (COVID-19): escrito de acusación | 2020 | `delito-contable-tributario-aplazar-renta-local-covid-19-428` |
| 468 | Falseamiento de cuentas o documentos sociales (delito societario): acusación | 2019 | `falseamiento-cuentas-documentos-sociales-delito-468` |
| 496 | Blanqueo de capitales imprudente y estafa: acusación contra el abogado y su cliente | 2019 | `blanqueo-capitales-imprudente-estafa-acusacion-contra-496` |
| 523 | Blanqueo de capitales tecnológico y estafa informática: acusación | 2018 | `blanqueo-capitales-tecnologico-estafa-informatica-523` |
| 538 | Publicidad engañosa por internet: acusación | 2018 | `publicidad-enganosa-internet-acusacion-538` |
| 541 | Falseamiento de información financiera: acusación | 2018 | `falseamiento-informacion-financiera-acusacion-541` |
| 550 | Alteración de precios en el mercado: acusación | 2018 | `alteracion-precios-mercado-acusacion-550` |
| 614 | Espionaje informático para descubrir secretos de empresa: acusación | 2018 | `espionaje-informatico-descubrir-secretos-empresa-614` |

## Escritos de defensa (13)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 155 | Detracción de materias primas o productos de primera necesidad: defensa alegando exención | 2023 | `detraccion-materias-primas-productos-primera-necesidad-155` |
| 156 | Alteración de precios en el mercado: defensa alegando exención | 2023 | `alteracion-precios-mercado-defensa-alegando-exencion-156` |
| 157 | Alteración de precios en concursos y subastas públicas: defensa alegando exención | 2023 | `alteracion-precios-concursos-subastas-publicas-defensa-157` |
| 267 | Difusión, revelación o cesión de secretos de empresa: escrito de defensa | 2022 | `difusion-revelacion-cesion-secretos-empresa-escrito-267` |
| 412 | Imposición de acuerdo societario abusivo: escrito de defensa | 2020 | `imposicion-acuerdo-societario-abusivo-escrito-defensa-412` |
| 431 | Delito contable tributario para aplazar renta del local (COVID-19): escrito de defensa | 2020 | `delito-contable-tributario-aplazar-renta-local-covid-19-431` |
| 470 | Falseamiento de cuentas o documentos sociales (delito societario): defensa | 2019 | `falseamiento-cuentas-documentos-sociales-delito-470` |
| 494 | Blanqueo de capitales imprudente y estafa: defensa del abogado acusado | 2019 | `blanqueo-capitales-imprudente-estafa-defensa-abogado-494` |
| 524 | Blanqueo de capitales tecnológico y estafa informática: defensa | 2018 | `blanqueo-capitales-tecnologico-estafa-informatica-524` |
| 540 | Publicidad engañosa por internet: defensa | 2018 | `publicidad-enganosa-internet-defensa-540` |
| 544 | Falseamiento de información financiera por internet: defensa | 2018 | `falseamiento-informacion-financiera-internet-defensa-544` |
| 548 | Alteración de precios en el mercado: defensa | 2018 | `alteracion-precios-mercado-defensa-548` |
| 616 | Espionaje informático para descubrir secretos de empresa: defensa | 2018 | `espionaje-informatico-descubrir-secretos-empresa-defensa-616` |
