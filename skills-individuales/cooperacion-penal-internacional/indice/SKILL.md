---
name: indice
description: "Índice de los 33 formularios de cooperación penal internacional (orden europea de investigación, euroorden, reconocimiento mutuo (Ley 23/2014), indemnizaciones transfronterizas). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Cooperación penal internacional: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/cooperacion-penal-internacional:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Recursos e impugnaciones (15)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 575 | Transmisión por reconocimiento mutuo UE: reforma y subsidiaria apelación (Sección de Instrucción) | 2018 | `transmision-reconocimiento-mutuo-ue-reforma-subsidiaria-575` |
| 577 | Denegar la ejecución de una resolución UE: reforma (Sección de Instrucción) | 2018 | `denegar-ejecucion-resolucion-ue-reforma-seccion-577` |
| 578 | Transmisión por reconocimiento mutuo UE: súplica (Audiencia Provincial) | 2018 | `transmision-reconocimiento-mutuo-ue-suplica-audiencia-578` |
| 579 | Denegar la ejecución de una resolución UE: apelación (Sección de lo Penal) | 2018 | `denegar-ejecucion-resolucion-ue-apelacion-seccion-lo-579` |
| 580 | Denegar la ejecución de una resolución UE: apelación (Sección de Instrucción) | 2018 | `denegar-ejecucion-resolucion-ue-apelacion-seccion-580` |
| 581 | Denegar la ejecución de una resolución UE: súplica (Audiencia Provincial) | 2018 | `denegar-ejecucion-resolucion-ue-suplica-audiencia-581` |
| 582 | Denegar la ejecución de una resolución UE: reforma (Sección de lo Penal) | 2018 | `denegar-ejecucion-resolucion-ue-reforma-seccion-lo-penal-582` |
| 583 | Denegar la ejecución de una resolución UE: reforma y subsidiaria apelación (Sección de lo Penal) | 2018 | `denegar-ejecucion-resolucion-ue-reforma-subsidiaria-583` |
| 584 | Transmisión por reconocimiento mutuo UE: reforma (Sección de lo Penal) | 2018 | `transmision-reconocimiento-mutuo-ue-reforma-seccion-lo-584` |
| 586 | Transmisión por reconocimiento mutuo UE: apelación (Sección de Instrucción) | 2018 | `transmision-reconocimiento-mutuo-ue-apelacion-seccion-586` |
| 587 | Transmisión por reconocimiento mutuo UE: reforma (juez de instrucción) | 2018 | `transmision-reconocimiento-mutuo-ue-reforma-juez-587` |
| 589 | Transmisión por reconocimiento mutuo UE: reforma y subsidiaria apelación (Sección de lo Penal) | 2018 | `transmision-reconocimiento-mutuo-ue-reforma-subsidiaria-589` |
| 590 | Denegar la ejecución de una resolución UE: reforma y subsidiaria apelación (Sección de Instrucción) | 2018 | `denegar-ejecucion-resolucion-ue-reforma-subsidiaria-590` |
| 595 | Transmisión por reconocimiento mutuo UE: apelación (Sección de lo Penal) | 2018 | `transmision-reconocimiento-mutuo-ue-apelacion-seccion-lo-595` |
| 602 | Euroorden de entrega al Estado requirente: apelación | 2018 | `euroorden-entrega-estado-requirente-apelacion-602` |

## Resoluciones, actas y documentos (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 395 | Indemnización en casos transfronterizos: impreso para transmitir la solicitud | 2020 | `indemnizacion-casos-transfronterizos-impreso-transmitir-395` |
| 396 | Indemnización en casos transfronterizos: impreso para transmitir la decisión sobre la solicitud | 2020 | `indemnizacion-casos-transfronterizos-impreso-transmitir-396` |
| 488 | Formulario para saber qué Estado miembro tiene antecedentes penales de un nacional de tercer país | 2019 | `formulario-saber-estado-miembro-tiene-antecedentes-488` |
| 519 | Transacción judicial en regímenes económicos matrimoniales: certificación | 2019 | `transaccion-judicial-regimenes-economicos-matrimoniales-519` |
| 558 | Formulario de orden europea de investigación (OEI) | 2018 | `formulario-orden-europea-investigacion-oei-558` |
| 559 | Notificar a otro Estado de la UE las intervenciones de telecomunicaciones en su territorio | 2018 | `notificar-otro-estado-ue-intervenciones-559` |
| 560 | Acuse de recibo de una orden europea de investigación | 2018 | `acuse-recibo-orden-europea-investigacion-560` |

## Solicitudes y escritos de trámite (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 397 | Justicia gratuita en otro Estado miembro de la UE: solicitud | 2020 | `justicia-gratuita-otro-estado-miembro-ue-solicitud-397` |
| 398 | Justicia gratuita transfronteriza: formulario para transmitir la solicitud | 2020 | `justicia-gratuita-transfronteriza-formulario-transmitir-398` |
| 574 | Ejecución en la UE de una resolución de la Sección de Instrucción: pedir su transmisión | 2018 | `ejecucion-ue-resolucion-seccion-instruccion-pedir-574` |
| 576 | Reconocimiento de resolución penal UE: personación con Abogado ante la Sección de Instrucción | 2018 | `reconocimiento-resolucion-penal-ue-personacion-abogado-576` |
| 585 | Ejecución en la UE de una resolución de la Audiencia Provincial: pedir su transmisión | 2018 | `ejecucion-ue-resolucion-audiencia-provincial-pedir-585` |
| 588 | Ejecución en la UE de una resolución de la Sección de lo Penal: pedir su transmisión | 2018 | `ejecucion-ue-resolucion-seccion-lo-penal-pedir-588` |
| 591 | Reconocimiento de resolución penal UE: personación con Abogado ante la Audiencia Provincial | 2018 | `reconocimiento-resolucion-penal-ue-personacion-abogado-591` |
| 592 | Reconocimiento de resolución penal UE: personación con Procurador ante la Audiencia Provincial | 2018 | `reconocimiento-resolucion-penal-ue-personacion-592` |
| 593 | Reconocimiento de resolución penal UE: personación con Procurador ante la Sección de lo Penal | 2018 | `reconocimiento-resolucion-penal-ue-personacion-593` |
| 594 | Reconocimiento de resolución penal UE: personación con Abogado ante la Sección de lo Penal | 2018 | `reconocimiento-resolucion-penal-ue-personacion-abogado-594` |
| 596 | Reconocimiento de resolución penal UE: personación con Procurador ante la Sección de Instrucción | 2018 | `reconocimiento-resolucion-penal-ue-personacion-596` |
