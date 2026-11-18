---
name: indice
description: "Índice de los 42 formularios de jornada, permisos y conciliación (registro de jornada, adaptación de jornada, permisos, excedencias, trabajo a distancia, desconexión digital). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Jornada, permisos y conciliación: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/jornada-permisos-y-conciliacion:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Contratos, cláusulas y anexos (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 38 | Anexo de horas complementarias (contrato a tiempo parcial) (en valenciano) | 2024 | `anexo-horas-complementarias-contrato-tiempo-parcial-38` |
| 39 | Anexo de horas complementarias (contrato a tiempo parcial) (en euskera) | 2024 | `anexo-horas-complementarias-contrato-tiempo-parcial-39` |
| 40 | Anexo de horas complementarias (contrato a tiempo parcial) (en catalán) | 2024 | `anexo-horas-complementarias-contrato-tiempo-parcial-40` |
| 41 | Anexo de horas complementarias (contrato a tiempo parcial) (en gallego) | 2024 | `anexo-horas-complementarias-contrato-tiempo-parcial-41` |

## Cartas y comunicaciones a la plantilla (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 29 | Propuesta de turnos de guardia al trabajador | 2024 | `propuesta-turnos-guardia-trabajador-29` |
| 48 | Resumen mensual de horas de trabajo: comunicación | 2024 | `resumen-mensual-horas-trabajo-comunicacion-48` |
| 93 | Aviso de ausencia por fuerza mayor ante enfermedad o accidente de un familiar: carta | 2023 | `aviso-ausencia-fuerza-mayor-ante-enfermedad-accidente-93` |
| 130 | Suspensión del contrato por violencia de género o sexual: carta a la empresa | 2022 | `suspension-contrato-violencia-genero-sexual-carta-130` |
| 131 | Suspensión del contrato por nacimiento, adopción o acogimiento: carta a la empresa | 2022 | `suspension-contrato-nacimiento-adopcion-acogimiento-131` |
| 153 | Revertir el trabajo a distancia: comunicación de la decisión | 2021 | `revertir-trabajo-distancia-comunicacion-decision-153` |
| 243 | Reincorporación tras excedencia: comunicación del trabajador | 2019 | `reincorporacion-tras-excedencia-comunicacion-trabajador-243` |
| 334 | Pedir excedencia: carta | 2017 | `pedir-excedencia-carta-334` |
| 347 | Ausentarse o reducir jornada: aviso del trabajador | 2017 | `ausentarse-reducir-jornada-aviso-trabajador-347` |
| 374 | Disfrute de permiso retribuido: comunicación del trabajador | 2016 | `disfrute-permiso-retribuido-comunicacion-trabajador-374` |
| 381 | Distribución irregular de la jornada: carta al trabajador | 2016 | `distribucion-irregular-jornada-carta-trabajador-381` |

## Demandas, papeletas y reclamaciones previas (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 49 | Demanda de adaptación de jornada por conciliación | 2024 | `demanda-adaptacion-jornada-conciliacion-49` |
| 124 | Conciliación laboral, personal y familiar: demanda genérica de derechos | 2022 | `conciliacion-laboral-personal-familiar-demanda-generica-124` |
| 148 | Trabajo a distancia: demanda por acceso, revisión o modificación | 2021 | `trabajo-distancia-demanda-acceso-revision-modificacion-148` |
| 176 | Prórroga de excedencia voluntaria: demanda de reconocimiento | 2020 | `prorroga-excedencia-voluntaria-demanda-reconocimiento-176` |

## Recursos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 147 | Suplicación en procedimiento de acceso, reversión o modificación del trabajo a distancia: recurso | 2021 | `suplicacion-procedimiento-acceso-reversion-modificacion-147` |

## Escritos y solicitudes (14)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 14 | Pedir permiso retribuido por fallecimiento de familiar en incendios forestales | 2026 | `pedir-permiso-retribuido-fallecimiento-familiar-14` |
| 20 | Pedir adaptación de jornada por cuidado de familiares tras la DANA | 2024 | `pedir-adaptacion-jornada-cuidado-familiares-tras-dana-20` |
| 21 | Pedir permiso retribuido por la DANA | 2024 | `pedir-permiso-retribuido-dana-21` |
| 23 | Pedir trabajo a distancia por la DANA | 2024 | `pedir-trabajo-distancia-dana-23` |
| 67 | Pedir permiso por registro de pareja de hecho | 2023 | `pedir-permiso-registro-pareja-hecho-67` |
| 156 | Pedir trabajo a distancia como víctima de violencia de género | 2021 | `pedir-trabajo-distancia-como-victima-violencia-genero-156` |
| 157 | Pedir trabajo a distancia por estudios | 2021 | `pedir-trabajo-distancia-estudios-157` |
| 196 | Pedir adaptación de jornada por conciliación | 2020 | `pedir-adaptacion-jornada-conciliacion-196` |
| 231 | Pedir adaptación de jornada por violencia de género, sexual o terrorismo | 2019 | `pedir-adaptacion-jornada-violencia-genero-sexual-231` |
| 240 | Compensar horas extra con descanso: petición del trabajador | 2019 | `compensar-horas-extra-descanso-peticion-trabajador-240` |
| 245 | Pedir días de vacaciones | 2018 | `pedir-dias-vacaciones-245` |
| 397 | Pedir permiso para informes psicológicos y sociales de adopción | 2015 | `pedir-permiso-informes-psicologicos-sociales-adopcion-397` |
| 398 | Pedir permiso para sesiones informativas previas a la adopción | 2015 | `pedir-permiso-sesiones-informativas-previas-adopcion-398` |
| 400 | Pedir justificante de ausencia al trabajador | 2015 | `pedir-justificante-ausencia-trabajador-400` |

## Actas, acuerdos, planes y protocolos (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 127 | Desconexión digital: protocolo | 2022 | `desconexion-digital-protocolo-127` |
| 230 | Personal de libre disponibilidad y registro de jornada: acuerdo con la representación | 2019 | `personal-libre-disponibilidad-registro-jornada-acuerdo-230` |
| 234 | Distribución irregular de la jornada: acuerdo con la representación | 2019 | `distribucion-irregular-jornada-acuerdo-representacion-234` |
| 236 | Cambio de jornada completa a parcial o al revés: acuerdo | 2019 | `cambio-jornada-completa-parcial-reves-acuerdo-236` |
| 361 | Registro de jornada diaria | 2016 | `registro-jornada-diaria-361` |

## Documentos, certificados y modelos oficiales (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 24 | Declaración del hogar familiar sobre reducción de servicios por la DANA | 2024 | `declaracion-hogar-familiar-sobre-reduccion-servicios-24` |
| 197 | Declaración responsable de trabajadores fuera del permiso retribuido recuperable del RDL 10/2020 | 2020 | `declaracion-responsable-trabajadores-fuera-permiso-197` |

## Otros (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 22 | Respuesta de la empresa al permiso retribuido por la DANA | 2024 | `respuesta-empresa-permiso-retribuido-dana-22` |
