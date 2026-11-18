---
name: indice
description: "Índice de los 28 formularios de proceso laboral (conciliación previa, demanda, ejecución, suplicación, revisión, medidas cautelares, LRJS). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Proceso laboral: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Convenio colectivo aplicable** (salario, jornada, categorías, faltas y sanciones) → `buscar_convenio` → `leer_convenio`; si sigue vigente o está denunciado, `vigencia_convenio`.
- **Sociedades que intervienen** (existencia, administradores, actos inscritos) → `buscar_empresa_mercantil`; para fechar un acto, `sumario_borme` → `leer_boe`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/proceso-laboral:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, papeletas y reclamaciones previas (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 47 | Monitorio laboral: escrito del demandante tras la oposición de la empresa | 2024 | `monitorio-laboral-escrito-demandante-tras-oposicion-47` |
| 117 | Falso autónomo: demanda de reconocimiento de relación laboral | 2023 | `falso-autonomo-demanda-reconocimiento-relacion-laboral-117` |
| 181 | Falso autónomo: papeleta de conciliación previa en el SMAC | 2020 | `falso-autonomo-papeleta-conciliacion-previa-smac-181` |
| 187 | Revisión y declaración de error judicial: demanda | 2020 | `revision-declaracion-error-judicial-demanda-187` |
| 244 | Incumplimiento de precontrato de trabajo: demanda de daños y perjuicios | 2018 | `incumplimiento-precontrato-trabajo-demanda-danos-244` |
| 303 | Reconocimiento de relación laboral con una entidad pública: demanda | 2017 | `reconocimiento-relacion-laboral-entidad-publica-demanda-303` |
| 304 | Personal laboral temporal irregular de entidades públicas: demanda para ser fijo | 2017 | `personal-laboral-temporal-irregular-entidades-publicas-304` |

## Recursos (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 188 | Revisión contra decretos del LAJ: recurso | 2020 | `revision-contra-decretos-laj-recurso-188` |
| 351 | Suplicación: formalización del recurso | 2017 | `suplicacion-formalizacion-recurso-351` |
| 367 | Anunciar recurso de suplicación | 2016 | `anunciar-recurso-suplicacion-367` |
| 401 | Reposición contra la acumulación indebida de acciones: recurso | 2015 | `reposicion-contra-acumulacion-indebida-acciones-recurso-401` |
| 404 | Reposición contra la acumulación de procesos: recurso | 2015 | `reposicion-contra-acumulacion-procesos-recurso-404` |

## Escritos y solicitudes (16)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 17 | Pedir la conciliación anticipada ante el tribunal | 2025 | `pedir-conciliacion-anticipada-ante-tribunal-17` |
| 18 | Reiniciar la ejecución laboral: escrito | 2025 | `reiniciar-ejecucion-laboral-escrito-18` |
| 122 | Embargo preventivo de bienes tras la demanda: medida cautelar | 2022 | `embargo-preventivo-bienes-tras-demanda-medida-cautelar-122` |
| 163 | Impugnar la liquidación de intereses en la ejecución laboral | 2021 | `impugnar-liquidacion-intereses-ejecucion-laboral-163` |
| 254 | Ejecución del acuerdo de conciliación judicial (decreto del LAJ) | 2018 | `ejecucion-acuerdo-conciliacion-judicial-decreto-laj-254` |
| 260 | Conclusiones complementarias sucintas | 2017 | `conclusiones-complementarias-sucintas-260` |
| 359 | Pedir embargo | 2017 | `pedir-embargo-359` |
| 360 | Cambio de partes en la ejecución por sucesión empresarial: escrito | 2016 | `cambio-partes-ejecucion-sucesion-empresarial-escrito-360` |
| 362 | Pedir declaración de insolvencia | 2016 | `pedir-declaracion-insolvencia-362` |
| 363 | Pedir apremio pecuniario o multa coercitiva | 2016 | `pedir-apremio-pecuniario-multa-coercitiva-363` |
| 364 | Pedir suspensión o aplazamiento de la ejecución | 2016 | `pedir-suspension-aplazamiento-ejecucion-364` |
| 365 | Ejecución de sentencia o acta de conciliación firme: solicitud | 2016 | `ejecucion-sentencia-acta-conciliacion-firme-solicitud-365` |
| 366 | Ejecución provisional de sentencia: solicitud | 2016 | `ejecucion-provisional-sentencia-solicitud-366` |
| 372 | Pedir acumulación de procesos ante el mismo o distinto tribunal | 2016 | `pedir-acumulacion-procesos-ante-mismo-distinto-tribunal-372` |
| 373 | Pedir actos preparatorios o prueba anticipada | 2016 | `pedir-actos-preparatorios-prueba-anticipada-373` |
| 411 | Multas coercitivas a terceros por incumplir en la ejecución de sentencia laboral: solicitud | 2015 | `multas-coercitivas-terceros-incumplir-ejecucion-411` |
