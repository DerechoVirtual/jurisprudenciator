---
name: indice
description: "Índice de los 36 formularios de despido colectivo y erte (periodo de consultas, comisión negociadora, ERTE por causas ETOP y fuerza mayor, Mecanismo RED, autoridad laboral). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Despido colectivo y ERTE: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/despido-colectivo-y-erte:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Cartas y comunicaciones a la plantilla (17)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 55 | Mecanismo RED: inicio del procedimiento comunicado a la representación de los trabajadores | 2023 | `mecanismo-red-inicio-procedimiento-comunicado-55` |
| 57 | Mecanismo RED: decisión sin acuerdo comunicada a la autoridad laboral | 2023 | `mecanismo-red-decision-sin-acuerdo-comunicada-autoridad-57` |
| 58 | Mecanismo RED: acuerdo comunicado a la autoridad laboral | 2023 | `mecanismo-red-acuerdo-comunicado-autoridad-laboral-58` |
| 60 | Mecanismo RED: inicio del periodo de consultas comunicado a la autoridad laboral | 2023 | `mecanismo-red-inicio-periodo-consultas-comunicado-60` |
| 61 | Mecanismo RED: apertura del periodo de consultas comunicada a la plantilla | 2023 | `mecanismo-red-apertura-periodo-consultas-comunicada-61` |
| 63 | Mecanismo RED: designación de miembros de la comisión negociadora comunicada a la empresa | 2023 | `mecanismo-red-designacion-miembros-comision-negociadora-63` |
| 73 | Cierre de centro en un despido colectivo: aviso a la autoridad laboral | 2023 | `cierre-centro-despido-colectivo-aviso-autoridad-laboral-73` |
| 180 | Prórroga de la suspensión o reducción de jornada por ETOP (ERTE): aviso al trabajador | 2020 | `prorroga-suspension-reduccion-jornada-etop-erte-aviso-180` |
| 185 | Despido colectivo: miembros de la comisión negociadora comunicados a la empresa | 2020 | `despido-colectivo-miembros-comision-negociadora-185` |
| 186 | Despido colectivo: carta a la plantilla para nombrar la comisión negociadora | 2020 | `despido-colectivo-carta-plantilla-nombrar-comision-186` |
| 194 | Fin del ERTE y reincorporación al trabajo: carta al trabajador | 2020 | `fin-erte-reincorporacion-trabajo-carta-trabajador-194` |
| 195 | Fin de las medidas de ERTE: comunicación a la autoridad laboral | 2020 | `fin-medidas-erte-comunicacion-autoridad-laboral-195` |
| 200 | ERTE por fuerza mayor temporal: comunicación al trabajador | 2020 | `erte-fuerza-mayor-temporal-comunicacion-trabajador-200` |
| 250 | ERTE por ETOP: apertura del periodo de consultas comunicada a los trabajadores | 2012 | `erte-etop-apertura-periodo-consultas-comunicada-250` |
| 335 | ERTE por ETOP: suspensión o reducción de jornada comunicada al trabajador | 2017 | `erte-etop-suspension-reduccion-jornada-comunicada-335` |
| 420 | Despido colectivo: inicio del periodo de consultas comunicado a la autoridad laboral | 2014 | `despido-colectivo-inicio-periodo-consultas-comunicado-420` |
| 421 | Reducción de jornada o suspensión de contratos sin representantes: aviso a todos los trabajadores | 2014 | `reduccion-jornada-suspension-contratos-sin-421` |

## Demandas, papeletas y reclamaciones previas (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 179 | Demanda contra la denegación de ERTE por fuerza mayor temporal o Mecanismo RED | 2020 | `demanda-contra-denegacion-erte-fuerza-mayor-temporal-179` |
| 249 | Despido colectivo por fuerza mayor sin resolución administrativa: demanda | 2012 | `despido-colectivo-fuerza-mayor-sin-resolucion-249` |
| 375 | Despido colectivo en grupo mercantil sin cuentas consolidadas: nulidad por falta de documentación | 2015 | `despido-colectivo-grupo-mercantil-sin-cuentas-375` |
| 388 | Despido colectivo: demanda de nulidad por falta de documentación | 2015 | `despido-colectivo-demanda-nulidad-falta-documentacion-388` |
| 389 | Despido colectivo en grupo mercantil con cuentas consolidadas: nulidad por falta de documentación | 2015 | `despido-colectivo-grupo-mercantil-cuentas-consolidadas-389` |
| 391 | Despido colectivo con acuerdo: demanda de sindicatos que no lo firmaron | 2015 | `despido-colectivo-acuerdo-demanda-sindicatos-no-lo-391` |
| 392 | Despido colectivo en grupo laboral: nulidad por tramitarse solo en una empresa | 2015 | `despido-colectivo-grupo-laboral-nulidad-tramitarse-solo-392` |

## Escritos y solicitudes (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 64 | Mecanismo RED: petición de la empresa para constituir la comisión negociadora | 2023 | `mecanismo-red-peticion-empresa-constituir-comision-64` |

## Actas, acuerdos, planes y protocolos (8)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 56 | Mecanismo RED: acta final del periodo de consultas | 2023 | `mecanismo-red-acta-final-periodo-consultas-56` |
| 59 | Mecanismo RED: acuerdo en el periodo de consultas con la representación de los trabajadores | 2023 | `mecanismo-red-acuerdo-periodo-consultas-representacion-59` |
| 62 | Mecanismo RED: acta de designación de la comisión ad hoc | 2023 | `mecanismo-red-acta-designacion-comision-ad-hoc-62` |
| 184 | Despido colectivo: acta de constitución de la comisión negociadora | 2020 | `despido-colectivo-acta-constitucion-comision-negociadora-184` |
| 193 | ERTE por ETOP: acta de designación de la comisión ad hoc | 2020 | `erte-etop-acta-designacion-comision-ad-hoc-193` |
| 198 | Calendario del expediente de regulación de empleo | 2020 | `calendario-expediente-regulacion-empleo-198` |
| 201 | ERTE suspensivo por fuerza mayor temporal: acta de reunión con la representación | 2020 | `erte-suspensivo-fuerza-mayor-temporal-acta-reunion-201` |
| 418 | Acta de consultas del despido colectivo | 2014 | `acta-consultas-despido-colectivo-418` |

## Documentos, certificados y modelos oficiales (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 192 | Declaración responsable de exención de cuotas en ERTE y Mecanismo RED | 2020 | `declaracion-responsable-exencion-cuotas-erte-mecanismo-192` |
| 199 | Lista de trabajadores afectados por expedientes de regulación de empleo | 2020 | `lista-trabajadores-afectados-expedientes-regulacion-199` |
| 419 | Memoria de ejemplo sobre causa productiva en un despido colectivo | 2014 | `memoria-ejemplo-sobre-causa-productiva-despido-colectivo-419` |
