---
name: indice
description: "Índice de los 76 formularios de recursos civiles (apelación, casación, reposición, revisión, queja, nulidad de actuaciones). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Recursos civiles: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/recursos-civiles:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (27)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 50 | Interposición de casación civil por interés casacional (País Vasco, reforma RDL 5/2023) | 2023 | `interposicion-casacion-civil-interes-casacional-pais-50` |
| 51 | Interposición de casación por infracción procesal en la valoración de la prueba (reforma RDL 5/2023) | 2023 | `interposicion-casacion-infraccion-procesal-valoracion-51` |
| 55 | Interposición de casación por interés casacional: infracción del art. 20 LCS (reforma RDL 5/2023) | 2023 | `interposicion-casacion-interes-casacional-infraccion-art-55` |
| 285 | Recurso extraordinario por infracción procesal del art. 469.1.3º LEC (anterior al RDL 5/2023) | 2020 | `recurso-extraordinario-infraccion-procesal-art-469-1-3o-285` |
| 286 | Recurso extraordinario por infracción procesal del art. 469.1.4º LEC (anterior al RDL 5/2023) | 2020 | `recurso-extraordinario-infraccion-procesal-art-469-1-4o-286` |
| 287 | Recurso extraordinario por infracción procesal del art. 469.1.1º LEC (anterior al RDL 5/2023) | 2020 | `recurso-extraordinario-infraccion-procesal-art-469-1-1o-287` |
| 367 | Recurso de apelación contra sentencia de desahucio | 2019 | `recurso-apelacion-contra-sentencia-desahucio-367` |
| 444 | Casación por infracción procesal y vulneración del art. 24 CE (tutela judicial efectiva) | 2018 | `casacion-infraccion-procesal-vulneracion-art-24-ce-444` |
| 445 | Casación por infracción de normas procesales que rigen los actos y garantías del proceso | 2018 | `casacion-infraccion-normas-procesales-rigen-actos-445` |
| 447 | Casación por oposición a la doctrina jurisprudencial del Tribunal Supremo | 2018 | `casacion-oposicion-doctrina-jurisprudencial-tribunal-447` |
| 448 | Casación por interés casacional: normas sin doctrina jurisprudencial del Tribunal Supremo | 2018 | `casacion-interes-casacional-normas-sin-doctrina-448` |
| 449 | Casación por jurisprudencia contradictoria de Audiencias Provinciales | 2018 | `casacion-jurisprudencia-contradictoria-audiencias-449` |
| 450 | Casación por infracción de normas de jurisdicción y competencia | 2018 | `casacion-infraccion-normas-jurisdiccion-competencia-450` |
| 451 | Casación por infracción de norma procesal y sustantiva | 2018 | `casacion-infraccion-norma-procesal-sustantiva-451` |
| 452 | Casación por infracción de las normas procesales reguladoras de la sentencia | 2018 | `casacion-infraccion-normas-procesales-reguladoras-452` |
| 507 | Incidente excepcional de nulidad de actuaciones: interposición | 2017 | `incidente-excepcional-nulidad-actuaciones-interposicion-507` |
| 513 | Recurso contencioso contra la denegación de visado de régimen comunitario | 2016 | `recurso-contencioso-contra-denegacion-visado-regimen-513` |
| 640 | Apelación contra resolución definitiva en jurisdicción voluntaria | 2015 | `apelacion-contra-resolucion-definitiva-jurisdiccion-640` |
| 758 | Apelación en jurisdicción voluntaria: modelo genérico | 2015 | `apelacion-jurisdiccion-voluntaria-modelo-generico-758` |
| 759 | Reposición en jurisdicción voluntaria: modelo genérico | 2015 | `reposicion-jurisdiccion-voluntaria-modelo-generico-759` |
| 762 | Recurso de revisión en jurisdicción voluntaria (modelo genérico) | 2015 | `recurso-revision-jurisdiccion-voluntaria-modelo-generico-762` |
| 878 | Interponer el recurso de casación | 2013 | `interponer-recurso-casacion-878` |
| 1048 | Recurso de queja por inadmisión de la apelación | 2013 | `recurso-queja-inadmision-apelacion-1048` |
| 1063 | Recurso de queja por inadmisión de la casación | 2013 | `recurso-queja-inadmision-casacion-1063` |
| 1127 | Casación e infracción procesal conjuntas y simultáneas, previo al RDL 5/2023 (general) | 2013 | `casacion-e-infraccion-procesal-conjuntas-simultaneas-1127` |
| 1335 | Interposición de la apelación | 2013 | `interposicion-apelacion-1335` |
| 1463 | Apelación contra el auto que resuelve la oposición | 2014 | `apelacion-contra-auto-resuelve-oposicion-1463` |

## Recursos e impugnaciones (30)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 22 | Recurso de apelación contra la valoración de la prueba testifical | 2024 | `recurso-apelacion-contra-valoracion-prueba-testifical-22` |
| 135 | Recurso de apelación en la división de cosa común | 2022 | `recurso-apelacion-division-cosa-comun-135` |
| 142 | Reposición contra la diligencia que señala vista telemática | 2021 | `reposicion-contra-diligencia-senala-vista-telematica-142` |
| 155 | Oposición a la apelación sobre cláusula suelo | 2021 | `oposicion-apelacion-sobre-clausula-suelo-155` |
| 170 | Oposición a la apelación sobre gastos de constitución de hipoteca | 2021 | `oposicion-apelacion-sobre-gastos-constitucion-hipoteca-170` |
| 317 | Recurso de revisión contra decreto que resuelve la reposición | 2020 | `recurso-revision-contra-decreto-resuelve-reposicion-317` |
| 374 | Oposición a la acción de anulación del laudo arbitral | 2019 | `oposicion-accion-anulacion-laudo-arbitral-374` |
| 438 | Apelación contra el auto de inadmisión de demanda verbal | 2018 | `apelacion-contra-auto-inadmision-demanda-verbal-438` |
| 439 | Apelación contra el auto que tiene por desistido al actor | 2018 | `apelacion-contra-auto-tiene-desistido-actor-439` |
| 519 | Recurso de apelación sobre cláusula suelo | 2016 | `recurso-apelacion-sobre-clausula-suelo-519` |
| 666 | Revisión contra el decreto que inadmite un acto de conciliación | 2015 | `revision-contra-decreto-inadmite-acto-conciliacion-666` |
| 673 | Reposición contra resolución del LAJ en jurisdicción voluntaria | 2015 | `reposicion-contra-resolucion-laj-jurisdiccion-voluntaria-673` |
| 674 | Revisión contra decreto definitivo del LAJ en jurisdicción voluntaria | 2015 | `revision-contra-decreto-definitivo-laj-jurisdiccion-674` |
| 757 | Revisión contra el decreto que declara la caducidad | 2015 | `revision-contra-decreto-declara-caducidad-757` |
| 837 | Oposición a la infracción procesal extraordinaria: modelo general | 2013 | `oposicion-infraccion-procesal-extraordinaria-modelo-837` |
| 903 | Reposición contra el auto que rechaza la declinatoria | 2013 | `reposicion-contra-auto-rechaza-declinatoria-903` |
| 962 | Reposición por admisión o inadmisión de prueba | 2013 | `reposicion-admision-inadmision-prueba-962` |
| 965 | Reposición contra la inadmisión de prueba | 2013 | `reposicion-contra-inadmision-prueba-965` |
| 990 | Reposición contra la fijación de gastos de testigo | 2013 | `reposicion-contra-fijacion-gastos-testigo-990` |
| 1061 | Apelación contra la desestimación del recurso de revisión | 2013 | `apelacion-contra-desestimacion-recurso-revision-1061` |
| 1074 | Apelación contra el auto que suspende por prejudicialidad civil | 2013 | `apelacion-contra-auto-suspende-prejudicialidad-civil-1074` |
| 1075 | Reposición contra la denegación de suspensión por prejudicialidad civil | 2013 | `reposicion-contra-denegacion-suspension-prejudicialidad-1075` |
| 1076 | Impugnación de la reposición contra la denegación de suspensión por prejudicialidad civil | 2013 | `impugnacion-reposicion-contra-denegacion-suspension-1076` |
| 1079 | Impugnación de la reposición del demandado contra el auto que deniega suspender el procedimiento | 2013 | `impugnacion-reposicion-demandado-contra-auto-deniega-1079` |
| 1080 | Reposición contra la denegación de suspensión por prejudicialidad penal | 2013 | `reposicion-contra-denegacion-suspension-prejudicialidad-1080` |
| 1083 | Apelación contra el auto que suspende por prejudicialidad penal | 2013 | `apelacion-contra-auto-suspende-prejudicialidad-penal-1083` |
| 1088 | Apelación contra el auto que se abstiene por falta de competencia objetiva | 2013 | `apelacion-contra-auto-abstiene-falta-competencia-1088` |
| 1128 | Oponerse al recurso de casación | 2013 | `oponerse-recurso-casacion-1128` |
| 1352 | Apelación en propiedad horizontal (juicio ordinario o verbal) | 2013 | `apelacion-propiedad-horizontal-juicio-ordinario-verbal-1352` |
| 1354 | Reposición por no indicar si cabe enervación | 2013 | `reposicion-no-indicar-si-cabe-enervacion-1354` |

## Contestaciones, oposiciones y alegaciones (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 25 | Oposición al recurso de casación: modelo general (RDL 5/2023 y 6/2023) | 2024 | `oposicion-recurso-casacion-modelo-general-rdl-5-2023-6-25` |
| 653 | Oposición al recurso de apelación en jurisdicción voluntaria | 2015 | `oposicion-recurso-apelacion-jurisdiccion-voluntaria-653` |
| 927 | Alegaciones en el incidente de nulidad de actuaciones | 2013 | `alegaciones-incidente-nulidad-actuaciones-927` |
| 1071 | Oposición al mantenimiento de medidas cautelares al recurrir la sentencia (general) | 2013 | `oposicion-mantenimiento-medidas-cautelares-recurrir-1071` |
| 1072 | Alegaciones de disconformidad con la causa de inadmisión del recurso | 2013 | `alegaciones-disconformidad-causa-inadmision-recurso-1072` |
| 1073 | Alegaciones de conformidad con la causa de inadmisión del recurso | 2013 | `alegaciones-conformidad-causa-inadmision-recurso-1073` |

## Solicitudes y expedientes (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 276 | Nulidad de actuaciones en jurisdicción voluntaria | 2020 | `nulidad-actuaciones-jurisdiccion-voluntaria-276` |
| 836 | Certificación de la sentencia para recurrir en casación | 2013 | `certificacion-sentencia-recurrir-casacion-836` |
| 999 | Aclaraciones al perito en el juicio o vista | 2013 | `aclaraciones-perito-juicio-vista-999` |
| 1062 | Mantenimiento de medidas cautelares al recurrir la sentencia | 2013 | `mantenimiento-medidas-cautelares-recurrir-sentencia-1062` |
| 1126 | Certificación de la sentencia para casación e infracción procesal conjuntas | 2013 | `certificacion-sentencia-casacion-e-infraccion-procesal-1126` |

## Escritos de trámite (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 677 | Impugnación del recurso de revisión contra decreto en jurisdicción voluntaria | 2015 | `impugnacion-recurso-revision-contra-decreto-jurisdiccion-677` |
| 838 | Subsanar la falta de tasa judicial en la apelación | 2013 | `subsanar-falta-tasa-judicial-apelacion-838` |
| 959 | Otrosí de proposición de prueba en apelación | 2013 | `otrosi-proposicion-prueba-apelacion-959` |
| 1097 | Otrosí: ofrecimiento de abono, consignación, depósito o aval para preparar recursos | 2013 | `otrosi-ofrecimiento-abono-consignacion-deposito-aval-1097` |

## Otros (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 350 | Incidente excepcional de nulidad por defecto de emplazamiento telemático | 2019 | `incidente-excepcional-nulidad-defecto-emplazamiento-350` |
| 678 | Reposición oral contra resolución dictada en la comparecencia | 2015 | `reposicion-oral-contra-resolucion-dictada-comparecencia-678` |
| 925 | Nulidad de actuaciones por vía de recurso | 2013 | `nulidad-actuaciones-via-recurso-925` |
| 1098 | Adhesión a la apelación | 2013 | `adhesion-apelacion-1098` |
