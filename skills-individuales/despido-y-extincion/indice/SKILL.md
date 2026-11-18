---
name: indice
description: "Índice de los 36 formularios de despido y extinción del contrato (carta de despido, despido objetivo y disciplinario, nulidad, dimisión, extinción por incumplimiento de la empresa). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Despido y extinción del contrato: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/despido-y-extincion:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Contratos, cláusulas y anexos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 126 | Recolocación en contrato adscrito a obra de construcción: cláusula | 2022 | `recolocacion-contrato-adscrito-obra-construccion-126` |

## Cartas y comunicaciones a la plantilla (16)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 19 | Aviso de audiencia previa al despido disciplinario | 2024 | `aviso-audiencia-previa-despido-disciplinario-19` |
| 94 | Extinción del contrato por circunstancias de la producción (tras el RDL 32/2021): comunicación | 2023 | `extincion-contrato-circunstancias-produccion-tras-rdl-32-94` |
| 125 | Respuesta del trabajador a la recolocación tras el fin de la obra de construcción | 2022 | `respuesta-trabajador-recolocacion-tras-fin-obra-125` |
| 128 | Propuesta de recolocación al trabajador tras el fin de la obra de construcción | 2022 | `propuesta-recolocacion-trabajador-tras-fin-obra-128` |
| 129 | Recolocación de obra de un indefinido adscrito a obra: propuesta de la empresa | 2022 | `recolocacion-obra-indefinido-adscrito-obra-propuesta-129` |
| 134 | Baja voluntaria por jubilación: carta del trabajador | 2022 | `baja-voluntaria-jubilacion-carta-trabajador-134` |
| 142 | Extinción del contrato por edad de jubilación: carta de la empresa | 2022 | `extincion-contrato-edad-jubilacion-carta-empresa-142` |
| 159 | Respuesta a la baja voluntaria del trabajador: carta | 2021 | `respuesta-baja-voluntaria-trabajador-carta-159` |
| 242 | Aviso al trabajador del fin de la excedencia | 2019 | `aviso-trabajador-fin-excedencia-242` |
| 333 | Dimisión o baja voluntaria del trabajador: carta | 2017 | `dimision-baja-voluntaria-trabajador-carta-333` |
| 341 | Despido disciplinario: carta | 2017 | `despido-disciplinario-carta-341` |
| 344 | Despido por causas objetivas: carta | 2017 | `despido-causas-objetivas-carta-344` |
| 348 | Desistimiento del alto directivo: comunicación a la empresa | 2017 | `desistimiento-alto-directivo-comunicacion-empresa-348` |
| 349 | Extinción del contrato de empleada del hogar: comunicación del empleador | 2017 | `extincion-contrato-empleada-hogar-comunicacion-empleador-349` |
| 350 | Desistimiento de la empresa frente al alto directivo: comunicación | 2017 | `desistimiento-empresa-frente-alto-directivo-comunicacion-350` |
| 354 | Resolución del contrato de TRADE: comunicación | 2017 | `resolucion-contrato-trade-comunicacion-354` |

## Demandas, papeletas y reclamaciones previas (14)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 65 | Despido nulo por negar la reincorporación tras excedencia por cuidado de pareja de hecho: demanda | 2023 | `despido-nulo-negar-reincorporacion-tras-excedencia-65` |
| 107 | Despido nulo por discriminación por enfermedad o estado de salud: demanda | 2023 | `despido-nulo-discriminacion-enfermedad-estado-salud-107` |
| 123 | Despido de empleada del hogar: demanda | 2022 | `despido-empleada-hogar-demanda-123` |
| 140 | Despido nulo por vulneración de derechos fundamentales: demanda | 2022 | `despido-nulo-vulneracion-derechos-fundamentales-demanda-140` |
| 168 | Despido y reconocimiento de relación laboral: demanda | 2021 | `despido-reconocimiento-relacion-laboral-demanda-168` |
| 228 | Extinción por impago o retrasos de salario: papeleta de conciliación del trabajador | 2019 | `extincion-impago-retrasos-salario-papeleta-conciliacion-228` |
| 255 | Indemnización por extinción por causas objetivas: demanda | 2013 | `indemnizacion-extincion-causas-objetivas-demanda-255` |
| 257 | Despido verbal: demanda | 2013 | `despido-verbal-demanda-257` |
| 369 | Despido nulo por vulnerar derechos de conciliación: demanda | 2016 | `despido-nulo-vulnerar-derechos-conciliacion-demanda-369` |
| 370 | Despido improcedente: demanda | 2016 | `despido-improcedente-demanda-370` |
| 402 | Extinción por incumplimientos graves del empresario: demanda del trabajador | 2015 | `extincion-incumplimientos-graves-empresario-demanda-402` |
| 403 | Extinción a instancia del trabajador por el art. 41.3 ET: demanda | 2015 | `extincion-instancia-trabajador-art-41-3-et-demanda-403` |
| 406 | TRADE: demanda de extinción por incumplimiento de la empresa cliente | 2015 | `trade-demanda-extincion-incumplimiento-empresa-cliente-406` |
| 408 | Extinción del contrato de artista por incumplimiento del empresario: demanda | 2015 | `extincion-contrato-artista-incumplimiento-empresario-408` |

## Escritos y solicitudes (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 33 | Renuncia del fijo discontinuo al llamamiento | 2024 | `renuncia-fijo-discontinuo-llamamiento-33` |
| 119 | Ejecución del auto de readmisión irregular: escrito | 2023 | `ejecucion-auto-readmision-irregular-escrito-119` |
| 377 | Opción tras despido improcedente: escrito de la parte actora o representación | 2013 | `opcion-tras-despido-improcedente-escrito-parte-actora-377` |

## Actas, acuerdos, planes y protocolos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 241 | Transacción sobre el despido: acuerdo | 2019 | `transaccion-sobre-despido-acuerdo-241` |

## Documentos, certificados y modelos oficiales (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 352 | Fútbol sala: inicio del procedimiento abreviado de resolución contractual anticipada | 2017 | `futbol-sala-inicio-procedimiento-abreviado-resolucion-352` |
