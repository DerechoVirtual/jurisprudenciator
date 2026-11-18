---
name: indice
description: "Índice de los 55 formularios de inspección de trabajo y sanciones (actas de infracción, alegaciones, recurso de alzada, requerimientos, LISOS, RD 928/1998). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Inspección de Trabajo y sanciones: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Convenio colectivo aplicable** (salario, jornada, categorías, faltas y sanciones) → `buscar_convenio` → `leer_convenio`; si sigue vigente o está denunciado, `vigencia_convenio`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/inspeccion-de-trabajo-y-sanciones:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, papeletas y reclamaciones previas (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 345 | Impugnar la sanción de Seguridad Social a un empresario: demanda | 2013 | `impugnar-sancion-seguridad-social-empresario-demanda-345` |

## Recursos (23)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 246 | Contencioso contra actas de la Inspección de Trabajo | 2018 | `contencioso-contra-actas-inspeccion-trabajo-246` |
| 263 | Alzada por caducidad de las actuaciones de comprobación de la Inspección | 2017 | `alzada-caducidad-actuaciones-comprobacion-inspeccion-263` |
| 264 | Alzada por prescripción de infracciones | 2017 | `alzada-prescripcion-infracciones-264` |
| 265 | Alzada por concurrencia de sanciones | 2017 | `alzada-concurrencia-sanciones-265` |
| 267 | Alzada contra sanción por obstrucción a la labor inspectora | 2017 | `alzada-contra-sancion-obstruccion-labor-inspectora-267` |
| 268 | Alzada contra sanción a empresas colaboradoras en la gestión de la Seguridad Social | 2017 | `alzada-contra-sancion-empresas-colaboradoras-gestion-268` |
| 269 | Alzada contra sanción en materia de movimientos migratorios | 2017 | `alzada-contra-sancion-materia-movimientos-migratorios-269` |
| 270 | Alzada contra sanción en materia de cooperativas | 2017 | `alzada-contra-sancion-materia-cooperativas-270` |
| 271 | Alzada contra sanción muy grave por autorización de trabajo de extranjeros | 2017 | `alzada-contra-sancion-muy-grave-autorizacion-trabajo-271` |
| 277 | Alzada contra sanción de Seguridad Social a trabajadores y beneficiarios de prestaciones | 2017 | `alzada-contra-sancion-seguridad-social-trabajadores-277` |
| 278 | Alzada contra sanción a las Mutuas de AT y EP | 2017 | `alzada-contra-sancion-mutuas-at-ep-278` |
| 281 | Alzada contra sanción de Seguridad Social (empresarios, entidades de formación y autónomos) | 2017 | `alzada-contra-sancion-seguridad-social-empresarios-281` |
| 282 | Alzada contra sanción a empresas de inserción | 2017 | `alzada-contra-sancion-empresas-insercion-282` |
| 285 | Alzada contra sanción a empresas de trabajo temporal | 2017 | `alzada-contra-sancion-empresas-trabajo-temporal-285` |
| 286 | Alzada contra sanción a empresas usuarias | 2017 | `alzada-contra-sancion-empresas-usuarias-286` |
| 287 | Alzada contra sanción a trabajadores | 2017 | `alzada-contra-sancion-trabajadores-287` |
| 291 | Alzada contra sanción en materia de empleo y fomento del empleo | 2017 | `alzada-contra-sancion-materia-empleo-fomento-empleo-291` |
| 293 | Alzada contra sanción de la Inspección por prevención de riesgos | 2017 | `alzada-contra-sancion-inspeccion-prevencion-riesgos-293` |
| 295 | Alzada contra sanción por actividad transnacional de empresas de trabajo temporal | 2017 | `alzada-contra-sancion-actividad-transnacional-empresas-295` |
| 297 | Alzada contra sanción por incumplir las normas sobre desplazamiento de trabajadores a España | 2017 | `alzada-contra-sancion-incumplir-normas-sobre-297` |
| 298 | Alzada contra sanción por información y consulta en sociedades anónimas y cooperativas europeas | 2017 | `alzada-contra-sancion-informacion-consulta-sociedades-298` |
| 301 | Alzada contra sanción por información y consulta en empresas y grupos de dimensión comunitaria | 2017 | `alzada-contra-sancion-informacion-consulta-empresas-301` |
| 305 | Alzada contra sanción en materia de relaciones laborales individuales y colectivas | 2017 | `alzada-contra-sancion-materia-relaciones-laborales-305` |

## Escritos y solicitudes (28)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 30 | Pedir ampliación del plazo del requerimiento de la Inspección de Trabajo | 2024 | `pedir-ampliacion-plazo-requerimiento-inspeccion-trabajo-30` |
| 152 | Reconocer la responsabilidad y pagar voluntariamente la sanción de la Inspección | 2021 | `reconocer-responsabilidad-pagar-voluntariamente-sancion-152` |
| 221 | Autorización para representar ante la Inspección de Trabajo | 2019 | `autorizacion-representar-ante-inspeccion-trabajo-221` |
| 261 | Caducidad de las actuaciones de comprobación de la Inspección: alegaciones | 2017 | `caducidad-actuaciones-comprobacion-inspeccion-261` |
| 262 | Prescripción de infracciones: alegaciones | 2017 | `prescripcion-infracciones-alegaciones-262` |
| 266 | Concurrencia de sanciones: alegaciones | 2017 | `concurrencia-sanciones-alegaciones-266` |
| 272 | Alegaciones al acta de infracción de movimientos migratorios | 2017 | `alegaciones-acta-infraccion-movimientos-migratorios-272` |
| 273 | Alegaciones al acta de infracción de empresas colaboradoras en la gestión de la Seguridad Social | 2017 | `alegaciones-acta-infraccion-empresas-colaboradoras-273` |
| 274 | Alegaciones al acta de infracción muy grave por autorización de trabajo de extranjeros | 2017 | `alegaciones-acta-infraccion-muy-grave-autorizacion-274` |
| 275 | Alegaciones al acta de infracción en materia de cooperativas | 2017 | `alegaciones-acta-infraccion-materia-cooperativas-275` |
| 276 | Alegaciones al acta de infracción por obstrucción a la labor inspectora | 2017 | `alegaciones-acta-infraccion-obstruccion-labor-inspectora-276` |
| 279 | Alegaciones al acta de infracción de Seguridad Social (trabajadores, beneficiarios y solicitantes) | 2017 | `alegaciones-acta-infraccion-seguridad-social-279` |
| 280 | Alegaciones al acta de infracción de las Mutuas de AT y EP | 2017 | `alegaciones-acta-infraccion-mutuas-at-ep-280` |
| 283 | Alegaciones al acta de Seguridad Social (empresarios, entidades de formación y autónomos) | 2017 | `alegaciones-acta-seguridad-social-empresarios-entidades-283` |
| 284 | Alegaciones al acta de infracción de empresas de inserción | 2017 | `alegaciones-acta-infraccion-empresas-insercion-284` |
| 288 | Alegaciones al acta de infracción de empresas usuarias | 2017 | `alegaciones-acta-infraccion-empresas-usuarias-288` |
| 289 | Alegaciones al acta de infracción de trabajadores | 2017 | `alegaciones-acta-infraccion-trabajadores-289` |
| 290 | Alegaciones al acta de infracción de empresas de trabajo temporal | 2017 | `alegaciones-acta-infraccion-empresas-trabajo-temporal-290` |
| 292 | Alegaciones al acta de infracción en materia de empleo y fomento del empleo | 2017 | `alegaciones-acta-infraccion-materia-empleo-fomento-292` |
| 294 | Alegaciones al acta de infracción de prevención de riesgos laborales | 2017 | `alegaciones-acta-infraccion-prevencion-riesgos-laborales-294` |
| 296 | Alegaciones al acta de infracción por actividad transnacional de empresas de trabajo temporal | 2017 | `alegaciones-acta-infraccion-actividad-transnacional-296` |
| 299 | Alegaciones al acta de infracción por desplazamiento de trabajadores a España | 2017 | `alegaciones-acta-infraccion-desplazamiento-trabajadores-299` |
| 300 | Alegaciones al acta de infracción por información y consulta en sociedades europeas | 2017 | `alegaciones-acta-infraccion-informacion-consulta-300` |
| 302 | Alegaciones al acta de infracción por información y consulta en grupos de dimensión comunitaria | 2017 | `alegaciones-acta-infraccion-informacion-consulta-grupos-302` |
| 306 | Alegaciones al acta de infracción de relaciones laborales individuales y colectivas | 2017 | `alegaciones-acta-infraccion-relaciones-laborales-306` |
| 358 | Pedir certificado de silencio administrativo | 2017 | `pedir-certificado-silencio-administrativo-358` |
| 396 | Caducidad de las actuaciones previas de la ITSS: declaración | 2015 | `caducidad-actuaciones-previas-itss-declaracion-396` |
| 399 | Alegaciones negando la relación laboral y pidiendo comunicación de oficio (art. 151 LJS) | 2012 | `alegaciones-negando-relacion-laboral-pidiendo-399` |

## Documentos, certificados y modelos oficiales (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 393 | Citación oficial del Inspector de Trabajo y Seguridad Social | 2015 | `citacion-oficial-inspector-trabajo-seguridad-social-393` |
| 394 | Citación oficial del Subinspector Laboral de Empleo y Seguridad Social | 2015 | `citacion-oficial-subinspector-laboral-empleo-seguridad-394` |
| 395 | Requerimiento normalizado de la ITSS | 2015 | `requerimiento-normalizado-itss-395` |
