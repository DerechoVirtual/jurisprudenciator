---
name: indice
description: "Índice de los 29 formularios de régimen disciplinario laboral (faltas y sanciones, pliego de cargos, expediente contradictorio, cartas de sanción, prescripción). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Régimen disciplinario laboral: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/regimen-disciplinario:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Cartas y comunicaciones a la plantilla (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 308 | Cancelar antecedentes por sanción: comunicación del trabajador | 2017 | `cancelar-antecedentes-sancion-comunicacion-trabajador-308` |
| 311 | Sanción por faltas de asistencia o puntualidad: carta | 2017 | `sancion-faltas-asistencia-puntualidad-carta-311` |
| 312 | Sanción por transgresión de la buena fe y abuso de confianza: carta | 2017 | `sancion-transgresion-buena-fe-abuso-confianza-carta-312` |
| 313 | Sanción por ofensas verbales o físicas: carta | 2017 | `sancion-ofensas-verbales-fisicas-carta-313` |
| 314 | Sanción por indisciplina o desobediencia: carta | 2017 | `sancion-indisciplina-desobediencia-carta-314` |
| 315 | Sanción por otras infracciones del convenio: carta | 2017 | `sancion-otras-infracciones-convenio-carta-315` |
| 317 | Sanción por reincidencia o reiteración de faltas: carta | 2017 | `sancion-reincidencia-reiteracion-faltas-carta-317` |
| 318 | Sanción por bajo rendimiento: carta | 2017 | `sancion-bajo-rendimiento-carta-318` |
| 319 | Sanción por embriaguez habitual o toxicomanía: carta | 2017 | `sancion-embriaguez-habitual-toxicomania-carta-319` |
| 321 | Sanción impuesta: aviso a la representación de los trabajadores en el expediente sancionador | 2017 | `sancion-impuesta-aviso-representacion-trabajadores-321` |
| 322 | Apertura de expediente sancionador: aviso a representantes, sindicato y delegado de prevención | 2017 | `apertura-expediente-sancionador-aviso-representantes-322` |
| 343 | Apercibimiento sin sanción: carta | 2017 | `apercibimiento-sin-sancion-carta-343` |

## Escritos y solicitudes (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 310 | Pedir la cancelación de antecedentes por sanción | 2017 | `pedir-cancelacion-antecedentes-sancion-310` |
| 338 | Diligencias en el expediente sancionador | 2017 | `diligencias-expediente-sancionador-338` |
| 339 | Aceptación del cargo en el expediente sancionador | 2017 | `aceptacion-cargo-expediente-sancionador-339` |
| 340 | Nombramiento en el expediente sancionador | 2017 | `nombramiento-expediente-sancionador-340` |

## Expediente disciplinario (13)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 309 | Ficha de antecedentes por sanción | 2017 | `ficha-antecedentes-sancion-309` |
| 320 | Sobreseimiento del expediente sancionador: propuesta | 2017 | `sobreseimiento-expediente-sancionador-propuesta-320` |
| 323 | Sanción propuesta en el expediente disciplinario | 2017 | `sancion-propuesta-expediente-disciplinario-323` |
| 324 | Cargos por reincidencia o reiteración de faltas: pliego | 2017 | `cargos-reincidencia-reiteracion-faltas-pliego-324` |
| 325 | Cargos por otras infracciones del convenio: pliego | 2017 | `cargos-otras-infracciones-convenio-pliego-325` |
| 327 | Descargos del trabajador: pliego | 2017 | `descargos-trabajador-pliego-327` |
| 328 | Cargos por embriaguez habitual o toxicomanía: pliego | 2017 | `cargos-embriaguez-habitual-toxicomania-pliego-328` |
| 329 | Actuaciones no disciplinarias: propuesta | 2017 | `actuaciones-no-disciplinarias-propuesta-329` |
| 330 | Cargos por transgresión de la buena fe y abuso de confianza: pliego | 2017 | `cargos-transgresion-buena-fe-abuso-confianza-pliego-330` |
| 331 | Cargos por bajo rendimiento: pliego | 2017 | `cargos-bajo-rendimiento-pliego-331` |
| 332 | Cargos por ofensas verbales o físicas: pliego | 2017 | `cargos-ofensas-verbales-fisicas-pliego-332` |
| 336 | Cargos por indisciplina o desobediencia: pliego | 2017 | `cargos-indisciplina-desobediencia-pliego-336` |
| 337 | Cargos por faltas de asistencia o puntualidad: pliego | 2017 | `cargos-faltas-asistencia-puntualidad-pliego-337` |
