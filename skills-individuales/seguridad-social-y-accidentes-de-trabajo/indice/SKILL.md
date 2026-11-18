---
name: indice
description: "Índice de los 37 formularios de seguridad social y accidentes de trabajo (incapacidad permanente, accidente de trabajo, cese de actividad, jubilación, ingreso mínimo vital). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Seguridad Social y accidentes de trabajo: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/seguridad-social-y-accidentes-de-trabajo:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Cartas y comunicaciones a la plantilla (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 149 | Respuesta de la empresa a la petición de jubilación parcial | 2021 | `respuesta-empresa-peticion-jubilacion-parcial-149` |
| 150 | Pedir jubilación parcial a la empresa | 2021 | `pedir-jubilacion-parcial-empresa-150` |
| 170 | Imposibilidad de embargar salarios: aviso al INSS | 2020 | `imposibilidad-embargar-salarios-aviso-inss-170` |

## Demandas, papeletas y reclamaciones previas (23)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 11 | Demanda a la Mutua por cese de autónomos tras la entrada de migrantes en Ceuta (julio 2026) | 2026 | `demanda-mutua-cese-autonomos-tras-entrada-migrantes-11` |
| 12 | Demanda a la Mutua por cese de actividad de autónomos por incendios forestales | 2026 | `demanda-mutua-cese-actividad-autonomos-incendios-12` |
| 16 | Demanda al INSS contra devolver la prestación de cese de autónomos en la COVID-19 | 2025 | `demanda-inss-contra-devolver-prestacion-cese-autonomos-16` |
| 25 | Demanda de reconocimiento de accidente de trabajo por la DANA (28 octubre a 4 noviembre de 2024) | 2024 | `demanda-reconocimiento-accidente-trabajo-dana-28-octubre-25` |
| 26 | Demanda a la Mutua por cese de actividad de autónomos por la DANA (28 octubre a 4 noviembre de 2024) | 2024 | `demanda-mutua-cese-actividad-autonomos-dana-28-octubre-4-26` |
| 27 | Demanda a la Mutua por prestación de cese de actividad de autónomos | 2024 | `demanda-mutua-prestacion-cese-actividad-autonomos-27` |
| 121 | Incapacidad permanente: demanda genérica | 2022 | `incapacidad-permanente-demanda-generica-121` |
| 139 | Demanda por efectos económicos de la incapacidad temporal tras un proceso anterior | 2022 | `demanda-efectos-economicos-incapacidad-temporal-tras-139` |
| 143 | Demanda por complemento de maternidad en pensión de jubilación contributiva | 2022 | `demanda-complemento-maternidad-pension-jubilacion-143` |
| 151 | Muerte por amianto: demanda de responsabilidad contra la empresa | 2021 | `muerte-amianto-demanda-responsabilidad-contra-empresa-151` |
| 154 | Ingreso mínimo vital denegado: demanda al INSS | 2021 | `ingreso-minimo-vital-denegado-demanda-inss-154` |
| 155 | Ingreso mínimo vital denegado: reclamación previa | 2021 | `ingreso-minimo-vital-denegado-reclamacion-previa-155` |
| 190 | Demanda de la empresa contra la responsabilidad por pensión de jubilación en contrato de relevo | 2020 | `demanda-empresa-contra-responsabilidad-pension-190` |
| 235 | Daños y perjuicios por accidente de trabajo: papeleta de conciliación | 2019 | `danos-perjuicios-accidente-trabajo-papeleta-conciliacion-235` |
| 259 | Riesgo durante la lactancia natural: demanda contra la Mutua | 2011 | `riesgo-durante-lactancia-natural-demanda-contra-mutua-259` |
| 307 | Prestación por maternidad: demanda de reclamación | 2011 | `prestacion-maternidad-demanda-reclamacion-307` |
| 380 | Impugnar la prestación por desempleo: demanda | 2008 | `impugnar-prestacion-desempleo-demanda-380` |
| 382 | Accidente de trabajo por falta de seguridad en contrata o subcontrata: demanda de indemnización | 2013 | `accidente-trabajo-falta-seguridad-contrata-subcontrata-382` |
| 383 | Determinar la contingencia de la incapacidad temporal: demanda | 2015 | `determinar-contingencia-incapacidad-temporal-demanda-383` |
| 390 | Pensión de viudedad del cónyuge separado judicialmente: demanda | 2015 | `pension-viudedad-conyuge-separado-judicialmente-demanda-390` |
| 409 | Autónomo: demanda de prestación económica por incapacidad | 2015 | `autonomo-demanda-prestacion-economica-incapacidad-409` |
| 410 | Gastos médicos por asistencia urgente y vital: demanda de reintegro (modelo 1) | 2015 | `gastos-medicos-asistencia-urgente-vital-demanda-410` |
| 202 (Procesal) | Prestaciones de la Seguridad Social: demanda de reconocimiento | 2020 | `prestaciones-seguridad-social-demanda-reconocimiento-p202` |

## Recursos (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 166 | Suplicación para elevar la incapacidad permanente de parcial a total | 2021 | `suplicacion-elevar-incapacidad-permanente-parcial-total-166` |
| 167 | Suplicación para elevar la incapacidad permanente de total a absoluta | 2021 | `suplicacion-elevar-incapacidad-permanente-total-absoluta-167` |

## Escritos y solicitudes (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 15 | Pedir suspensión del contrato por incendios forestales | 2026 | `pedir-suspension-contrato-incendios-forestales-15` |
| 218 | Pedir cambio de puesto por embarazo o lactancia | 2019 | `pedir-cambio-puesto-embarazo-lactancia-218` |
| 384 | Certificación negativa de descubiertos de la subcontratista: solicitud a la Tesorería | 2003 | `certificacion-negativa-descubiertos-subcontratista-384` |

## Documentos, certificados y modelos oficiales (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 6 | Certificado del club deportivo sobre periodos de actividad como deportista profesional | 2026 | `certificado-club-deportivo-sobre-periodos-actividad-como-6` |
| 7 | Certificado de ministro de culto evangélico y tiempo de actividad en España | 2026 | `certificado-ministro-culto-evangelico-tiempo-actividad-7` |
| 8 | Certificado de la federación deportiva sobre periodos de actividad como deportista profesional | 2026 | `certificado-federacion-deportiva-sobre-periodos-8` |
| 256 | Convenios bilaterales de Seguridad Social de España con otros países | 2018 | `convenios-bilaterales-seguridad-social-espana-otros-256` |
| 355 | Aptitud tras el reconocimiento médico: declaración | 2013 | `aptitud-tras-reconocimiento-medico-declaracion-355` |

## Otros (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 13 | Respuesta de la empresa a suspensión o permiso por fallecimiento en incendios forestales | 2026 | `respuesta-empresa-suspension-permiso-fallecimiento-13` |
