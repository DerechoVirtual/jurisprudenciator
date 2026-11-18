---
name: indice
description: "Índice de los 37 formularios de monitorio y cambiario (petición monitoria, oposición al monitorio, juicio cambiario). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Monitorio y cambiario: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Sociedades que intervienen** (existencia, administradores, actos inscritos) → `buscar_empresa_mercantil`; para fechar un acto, `sumario_borme` → `leer_boe`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/monitorio-y-cambiario:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 49 | Petición inicial de monitorio contra la comunidad por honorarios del administrador | 2023 | `peticion-inicial-monitorio-contra-comunidad-honorarios-49` |
| 555 | Demanda ordinaria contra el propietario tras oposición al monitorio | 2016 | `demanda-ordinaria-contra-propietario-tras-oposicion-555` |
| 637 | Oposición por abusividad al juicio cambiario: demanda | 2015 | `oposicion-abusividad-juicio-cambiario-demanda-637` |
| 876 | Monitorio con procurador y abogado | 2013 | `monitorio-procurador-abogado-876` |
| 880 | Monitorio con intereses moratorios ya liquidados | 2013 | `monitorio-intereses-moratorios-ya-liquidados-880` |
| 890 | Monitorio encabezado por el acreedor | 2013 | `monitorio-encabezado-acreedor-890` |
| 1035 | Oposición al juicio cambiario: demanda | 2013 | `oposicion-juicio-cambiario-demanda-1035` |
| 1240 | Monitorio tipo por rentas atrasadas | 2013 | `monitorio-tipo-rentas-atrasadas-1240` |
| 1332 | Monitorio de la comunidad por certificado de impago de gastos, presentado por el presidente | 2013 | `monitorio-comunidad-certificado-impago-gastos-presentado-1332` |
| 1370 | Monitorio por cuotas pendientes y gastos de requerimiento | 2013 | `monitorio-cuotas-pendientes-gastos-requerimiento-1370` |
| 1404 | Monitorio por derramas extraordinarias | 2013 | `monitorio-derramas-extraordinarias-1404` |
| 1405 | Monitorio de propiedad horizontal con procurador y abogado | 2013 | `monitorio-propiedad-horizontal-procurador-abogado-1405` |

## Recursos e impugnaciones (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 623 | Impugnación de la oposición al monitorio | 2016 | `impugnacion-oposicion-monitorio-623` |
| 635 | Apelación contra el auto que rechaza cláusulas abusivas en el monitorio | 2015 | `apelacion-contra-auto-rechaza-clausulas-abusivas-635` |
| 716 | Impugnación de la oposición al monitorio por el trámite del verbal | 2015 | `impugnacion-oposicion-monitorio-tramite-verbal-716` |

## Contestaciones, oposiciones y alegaciones (10)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 103 | Oposición al monitorio por prescripción de la deuda | 2022 | `oposicion-monitorio-prescripcion-deuda-103` |
| 180 | Oposición al monitorio por cláusula rebus sic stantibus | 2021 | `oposicion-monitorio-clausula-rebus-sic-stantibus-180` |
| 238 | Oposición al monitorio por cláusulas abusivas | 2020 | `oposicion-monitorio-clausulas-abusivas-238` |
| 636 | Alegaciones del deudor en el incidente de abusividad de oficio en el monitorio | 2015 | `alegaciones-deudor-incidente-abusividad-oficio-monitorio-636` |
| 719 | Alegaciones del demandado sobre cláusulas abusivas en el monitorio | 2015 | `alegaciones-demandado-sobre-clausulas-abusivas-monitorio-719` |
| 1025 | Oposición al monitorio con paso al juicio ordinario | 2013 | `oposicion-monitorio-paso-juicio-ordinario-1025` |
| 1326 | Oposición al monitorio por pluspetición | 2013 | `oposicion-monitorio-pluspeticion-1326` |
| 1327 | Oposición al monitorio | 2013 | `oposicion-monitorio-1327` |
| 1342 | Oposición al monitorio en propiedad horizontal | 2013 | `oposicion-monitorio-propiedad-horizontal-1342` |
| 1369 | Oposición al monitorio por pluspetitio | 2013 | `oposicion-monitorio-pluspetitio-1369` |

## Solicitudes y expedientes (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 275 | Inicio de expediente de título de crédito: cheque | 2020 | `inicio-expediente-titulo-credito-cheque-275` |
| 492 | Monitorio por deuda de alquiler impagado | 2017 | `monitorio-deuda-alquiler-impagado-492` |
| 711 | Inicio de expediente de título de crédito: letra de cambio | 2015 | `inicio-expediente-titulo-credito-letra-cambio-711` |
| 1254 | Monitorio: petición | 2013 | `monitorio-peticion-1254` |

## Escritos de trámite (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 76 | Impugnación de la oposición al monitorio (financiación de vehículo) | 2023 | `impugnacion-oposicion-monitorio-financiacion-vehiculo-76` |
| 77 | Petición inicial de monitorio por contrato de financiación de vehículos | 2023 | `peticion-inicial-monitorio-contrato-financiacion-77` |
| 78 | Petición inicial de monitorio por contrato de renting | 2023 | `peticion-inicial-monitorio-contrato-renting-78` |
| 511 | Impugnación de la oposición cambiaria | 2017 | `impugnacion-oposicion-cambiaria-511` |
| 1448 | Apelación contra el auto de inadmisión del monitorio | 2014 | `apelacion-contra-auto-inadmision-monitorio-1448` |

## Contratos, escrituras y documentos (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 610 | Modelo normalizado de reclamación monitoria | 2016 | `modelo-normalizado-reclamacion-monitoria-610` |
| 612 | Modelo normalizado de reclamación monitoria de gastos comunes de comunidad | 2016 | `modelo-normalizado-reclamacion-monitoria-gastos-comunes-612` |
| 852 | Monitorio simplificado con documentación mercantil habitual | 2013 | `monitorio-simplificado-documentacion-mercantil-habitual-852` |
