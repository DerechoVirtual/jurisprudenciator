---
name: indice
description: "Índice de los 84 formularios de contratación laboral (contratos indefinidos, temporales y formativos, fijos discontinuos, información al trabajador, ETT, relaciones especiales). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Contratación laboral: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/contratacion-laboral:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Contratos, cláusulas y anexos (59)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 46 | Novación de fijo discontinuo a indefinido ordinario: acuerdo | 2024 | `novacion-fijo-discontinuo-indefinido-ordinario-acuerdo-46` |
| 66 | Contrato indefinido del Plan de Recuperación (en valenciano) | 2023 | `contrato-indefinido-plan-recuperacion-valenciano-66` |
| 68 | Contrato de trabajo de pescadores (en inglés) | 2023 | `contrato-trabajo-pescadores-ingles-68` |
| 69 | Contrato de trabajo de pescadores (en euskera) | 2023 | `contrato-trabajo-pescadores-euskera-69` |
| 70 | Contrato de trabajo de pescadores (en catalán) | 2023 | `contrato-trabajo-pescadores-catalan-70` |
| 71 | Contrato de trabajo de pescadores (en gallego) | 2023 | `contrato-trabajo-pescadores-gallego-71` |
| 72 | Contrato de trabajo de pescadores (en valenciano) | 2023 | `contrato-trabajo-pescadores-valenciano-72` |
| 74 | Contrato indefinido del Plan de Recuperación (en catalán) | 2023 | `contrato-indefinido-plan-recuperacion-catalan-74` |
| 75 | Contrato indefinido del Plan de Recuperación (en euskera) | 2023 | `contrato-indefinido-plan-recuperacion-euskera-75` |
| 76 | Contrato indefinido del Plan de Recuperación (en gallego) | 2023 | `contrato-indefinido-plan-recuperacion-gallego-76` |
| 77 | Contrato indefinido del Plan de Recuperación | 2023 | `contrato-indefinido-plan-recuperacion-77` |
| 78 | Contrato de formación en alternancia del Plan de Recuperación (en valenciano) | 2023 | `contrato-formacion-alternancia-plan-recuperacion-78` |
| 79 | Contrato formativo de práctica profesional del Plan de Recuperación (en valenciano) | 2023 | `contrato-formativo-practica-profesional-plan-79` |
| 80 | Contrato formativo de práctica profesional del Plan de Recuperación (en catalán) | 2023 | `contrato-formativo-practica-profesional-plan-80` |
| 81 | Contrato de formación en alternancia del Plan de Recuperación (en euskera) | 2023 | `contrato-formacion-alternancia-plan-recuperacion-euskera-81` |
| 82 | Contrato de formación en alternancia del Plan de Recuperación (en catalán) | 2023 | `contrato-formacion-alternancia-plan-recuperacion-catalan-82` |
| 83 | Contrato de formación en alternancia del Plan de Recuperación (en gallego) | 2023 | `contrato-formacion-alternancia-plan-recuperacion-gallego-83` |
| 84 | Contrato formativo de práctica profesional del Plan de Recuperación (en euskera) | 2023 | `contrato-formativo-practica-profesional-plan-84` |
| 85 | Contrato formativo de práctica profesional del Plan de Recuperación (en gallego) | 2023 | `contrato-formativo-practica-profesional-plan-85` |
| 86 | Contrato formativo de práctica profesional del Plan de Recuperación | 2023 | `contrato-formativo-practica-profesional-plan-86` |
| 87 | Contrato de formación en alternancia del Plan de Recuperación | 2023 | `contrato-formacion-alternancia-plan-recuperacion-87` |
| 88 | Contrato temporal del Plan de Recuperación (en valenciano) | 2023 | `contrato-temporal-plan-recuperacion-valenciano-88` |
| 89 | Contrato temporal del Plan de Recuperación (en gallego) | 2023 | `contrato-temporal-plan-recuperacion-gallego-89` |
| 90 | Contrato temporal del Plan de Recuperación (en euskera) | 2023 | `contrato-temporal-plan-recuperacion-euskera-90` |
| 91 | Contrato temporal del Plan de Recuperación (en catalán) | 2023 | `contrato-temporal-plan-recuperacion-catalan-91` |
| 92 | Contrato temporal del Plan de Recuperación | 2023 | `contrato-temporal-plan-recuperacion-92` |
| 96 | Contrato formativo para la práctica profesional (en valenciano) | 2023 | `contrato-formativo-practica-profesional-valenciano-96` |
| 97 | Contrato formativo para la práctica profesional (en catalán) | 2023 | `contrato-formativo-practica-profesional-catalan-97` |
| 98 | Contrato formativo para la práctica profesional (en gallego) | 2023 | `contrato-formativo-practica-profesional-gallego-98` |
| 99 | Contrato formativo para la práctica profesional (en euskera) | 2023 | `contrato-formativo-practica-profesional-euskera-99` |
| 103 | Contrato formativo en alternancia (en catalán) | 2023 | `contrato-formativo-alternancia-catalan-103` |
| 104 | Contrato formativo en alternancia (en gallego) | 2023 | `contrato-formativo-alternancia-gallego-104` |
| 105 | Contrato formativo en alternancia (en euskera) | 2023 | `contrato-formativo-alternancia-euskera-105` |
| 106 | Contrato formativo en alternancia (en valenciano) | 2023 | `contrato-formativo-alternancia-valenciano-106` |
| 109 | Contrato laboral temporal (en valenciano) | 2023 | `contrato-laboral-temporal-valenciano-109` |
| 110 | Contrato laboral temporal (en gallego) | 2023 | `contrato-laboral-temporal-gallego-110` |
| 111 | Contrato laboral temporal (en euskera) | 2023 | `contrato-laboral-temporal-euskera-111` |
| 112 | Contrato laboral temporal (en catalán) | 2023 | `contrato-laboral-temporal-catalan-112` |
| 113 | Contrato laboral indefinido (en gallego) | 2023 | `contrato-laboral-indefinido-gallego-113` |
| 114 | Contrato laboral indefinido (en euskera) | 2023 | `contrato-laboral-indefinido-euskera-114` |
| 115 | Contrato laboral indefinido (en valenciano) | 2023 | `contrato-laboral-indefinido-valenciano-115` |
| 116 | Contrato laboral indefinido (en catalán) | 2023 | `contrato-laboral-indefinido-catalan-116` |
| 132 | Contrato de actuación de toreros, novilleros y rejoneadores | 2022 | `contrato-actuacion-toreros-novilleros-rejoneadores-132` |
| 133 | Contrato laboral de colaboración para formar una cuadrilla | 2022 | `contrato-laboral-colaboracion-formar-cuadrilla-133` |
| 135 | Plan individual de formación | 2022 | `plan-individual-formacion-135` |
| 137 | Contrato de artistas de duración determinada (relación laboral especial) | 2022 | `contrato-artistas-duracion-determinada-relacion-laboral-137` |
| 138 | Contrato de personal técnico y auxiliar artístico de duración determinada | 2022 | `contrato-personal-tecnico-auxiliar-artistico-duracion-138` |
| 144 | Contrato de servicios profesionales | 2022 | `contrato-servicios-profesionales-144` |
| 178 | Contrato de trabajo de pescadores | 2020 | `contrato-trabajo-pescadores-178` |
| 207 | Plan formativo | 2019 | `plan-formativo-207` |
| 229 | Cláusulas adicionales del contrato de grupo | 2019 | `clausulas-adicionales-contrato-grupo-229` |
| 248 | Contrato del autónomo económicamente dependiente (TRADE) | 2018 | `contrato-autonomo-economicamente-dependiente-trade-248` |
| 342 | Cláusulas adicionales del contrato de trabajo | 2017 | `clausulas-adicionales-contrato-trabajo-342` |
| 378 | Contrato de patrón de embarcaciones de recreo | 2016 | `contrato-patron-embarcaciones-recreo-378` |
| 385 | Puesta a disposición: contrato | 2015 | `puesta-disposicion-contrato-385` |
| 412 | Acuerdo con voluntarios | 2015 | `acuerdo-voluntarios-412` |
| 413 | Contrato de interinidad de profesor de religión | 2015 | `contrato-interinidad-profesor-religion-413` |
| 414 | Contrato indefinido de profesor de religión | 2015 | `contrato-indefinido-profesor-religion-414` |
| 415 | Contrato de personal civil de establecimientos militares | 2015 | `contrato-personal-civil-establecimientos-militares-415` |

## Cartas y comunicaciones a la plantilla (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 9 | Información al trabajador sobre los elementos esenciales del contrato: carta | 2026 | `informacion-trabajador-sobre-elementos-esenciales-9` |
| 32 | Llamamiento a la actividad del fijo discontinuo: comunicación de la empresa | 2024 | `llamamiento-actividad-fijo-discontinuo-comunicacion-32` |
| 34 | Prórroga del contrato de trabajo acogida al Real Decreto: comunicación (en valenciano) | 2024 | `prorroga-contrato-trabajo-acogida-real-decreto-34` |
| 35 | Prórroga del contrato de trabajo acogida al Real Decreto: comunicación (en euskera) | 2024 | `prorroga-contrato-trabajo-acogida-real-decreto-35` |
| 36 | Prórroga del contrato de trabajo acogida al Real Decreto: comunicación (en gallego) | 2024 | `prorroga-contrato-trabajo-acogida-real-decreto-36` |
| 37 | Prórroga del contrato de trabajo acogida al Real Decreto: comunicación (en catalán) | 2024 | `prorroga-contrato-trabajo-acogida-real-decreto-37` |
| 42 | Llamamiento a la actividad de fijos discontinuos: comunicación (en catalán) | 2024 | `llamamiento-actividad-fijos-discontinuos-comunicacion-42` |
| 43 | Llamamiento a la actividad de fijos discontinuos: comunicación (en gallego) | 2024 | `llamamiento-actividad-fijos-discontinuos-comunicacion-43` |
| 44 | Llamamiento a la actividad de fijos discontinuos: comunicación (en euskera) | 2024 | `llamamiento-actividad-fijos-discontinuos-comunicacion-44` |
| 45 | Llamamiento a la actividad de fijos discontinuos: comunicación (en valenciano) | 2024 | `llamamiento-actividad-fijos-discontinuos-comunicacion-45` |
| 353 | Interrupción de actividad del TRADE: comunicación | 2017 | `interrupcion-actividad-trade-comunicacion-353` |

## Escritos y solicitudes (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 10 | Pedir información sobre los elementos esenciales de la relación laboral | 2026 | `pedir-informacion-sobre-elementos-esenciales-relacion-10` |
| 182 | Pedir trabajar a distancia | 2020 | `pedir-trabajar-distancia-182` |
| 237 | Pedir que el contrato de trabajo conste por escrito | 2019 | `pedir-contrato-trabajo-conste-escrito-237` |

## Documentos, certificados y modelos oficiales (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1 | Información al trabajador sobre los elementos esenciales del contrato | 2026 | `informacion-trabajador-sobre-elementos-esenciales-1` |
| 2 | Información al trabajador sobre los elementos esenciales del contrato (en valenciano) | 2026 | `informacion-trabajador-sobre-elementos-esenciales-2` |
| 3 | Información al trabajador sobre los elementos esenciales del contrato (en euskera) | 2026 | `informacion-trabajador-sobre-elementos-esenciales-3` |
| 4 | Información al trabajador sobre los elementos esenciales del contrato (en gallego) | 2026 | `informacion-trabajador-sobre-elementos-esenciales-4` |
| 5 | Información al trabajador sobre los elementos esenciales del contrato (en catalán) | 2026 | `informacion-trabajador-sobre-elementos-esenciales-5` |
| 202 | Asistencia a formación: hoja de firmas | 2020 | `asistencia-formacion-hoja-firmas-202` |
| 204 | Autónomo que contrata a un familiar: declaración jurada | 2019 | `autonomo-contrata-familiar-declaracion-jurada-204` |
| 210 | Currículum anónimo | 2019 | `curriculum-anonimo-210` |
| 247 | Declaración responsable de cumplimiento de la reserva de empleo para personas con discapacidad | 2018 | `declaracion-responsable-cumplimiento-reserva-empleo-247` |
| 258 | Memoria sobre la organización de una empresa de trabajo temporal | 2017 | `memoria-sobre-organizacion-empresa-trabajo-temporal-258` |
| 386 | Registro de contratos de puesta a disposición (CPD) | 2015 | `registro-contratos-puesta-disposicion-cpd-386` |
