---
name: indice
description: "Índice de los 23 formularios de condiciones de trabajo y salario (modificación sustancial, sucesión de empresa, salario, reclamación de cantidad, anticipos y préstamos). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Condiciones de trabajo y salario: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/condiciones-de-trabajo-y-salario:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Contratos, cláusulas y anexos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 346 | Préstamo de la empresa al trabajador: contrato | 2017 | `prestamo-empresa-trabajador-contrato-346` |

## Cartas y comunicaciones a la plantilla (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 101 | Modificación sustancial: comunicación de los miembros de la comisión negociadora | 2023 | `modificacion-sustancial-comunicacion-miembros-comision-101` |
| 356 | Sucesión en la contrata: aviso de la empresa a la representación de los trabajadores | 2013 | `sucesion-contrata-aviso-empresa-representacion-356` |
| 357 | Sucesión de empresa: aviso al trabajador | 2017 | `sucesion-empresa-aviso-trabajador-357` |
| 379 | Compensación y absorción sin subida de salario: aviso al trabajador | 2016 | `compensacion-absorcion-sin-subida-salario-aviso-379` |

## Demandas, papeletas y reclamaciones previas (10)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 28 | Demanda de traslado por violencia de género, sexual o terrorismo, salud o traslado del cónyuge | 2024 | `demanda-traslado-violencia-genero-sexual-terrorismo-28` |
| 31 | Reclamación de cantidad de la empresa al trabajador: demanda | 2024 | `reclamacion-cantidad-empresa-trabajador-demanda-31` |
| 120 | Extinguir el contrato por modificación sustancial de condiciones: demanda | 2023 | `extinguir-contrato-modificacion-sustancial-condiciones-120` |
| 145 | Daños en vehículo de empresa: demanda de indemnización | 2022 | `danos-vehiculo-empresa-demanda-indemnizacion-145` |
| 189 | Cambio de titularidad de la contrata: demanda de reconocimiento laboral | 2020 | `cambio-titularidad-contrata-demanda-reconocimiento-189` |
| 368 | Despido disciplinario o reclamación de cantidad: papeleta de conciliación en el SMAC | 2016 | `despido-disciplinario-reclamacion-cantidad-papeleta-368` |
| 371 | Reclamación de cantidad: demanda | 2016 | `reclamacion-cantidad-demanda-371` |
| 387 | Salarios contra grupo laboral de empresas: demanda | 2015 | `salarios-contra-grupo-laboral-empresas-demanda-387` |
| 405 | TRADE: demanda de reclamación de cantidad a la empresa cliente | 2015 | `trade-demanda-reclamacion-cantidad-empresa-cliente-405` |
| 407 | Negativa a la subrogación empresarial: demanda de extinción del trabajador | 2015 | `negativa-subrogacion-empresarial-demanda-extincion-407` |

## Escritos y solicitudes (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 102 | Modificación sustancial colectiva: petición de la empresa para constituir comisión negociadora | 2023 | `modificacion-sustancial-colectiva-peticion-empresa-102` |
| 171 | Pedir anticipo de salario | 2020 | `pedir-anticipo-salario-171` |
| 417 | Ascenso de categoría y diferencias salariales por funciones superiores: solicitud | 2014 | `ascenso-categoria-diferencias-salariales-funciones-417` |

## Actas, acuerdos, planes y protocolos (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 100 | Designación de trabajadores para negociar una modificación sustancial colectiva: acta | 2023 | `designacion-trabajadores-negociar-modificacion-100` |
| 174 | Reconocimiento de deuda de la empresa al trabajador: acuerdo | 2020 | `reconocimiento-deuda-empresa-trabajador-acuerdo-174` |
| 175 | Reconocimiento de deuda del trabajador a la empresa: acuerdo | 2020 | `reconocimiento-deuda-trabajador-empresa-acuerdo-175` |
| 183 | Cesión de vivienda al trabajador: acuerdo de uso | 2020 | `cesion-vivienda-trabajador-acuerdo-uso-183` |

## Otros (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 416 | Negativa de la empresa tras modificación sustancial de condiciones: resolución | 2014 | `negativa-empresa-tras-modificacion-sustancial-416` |
