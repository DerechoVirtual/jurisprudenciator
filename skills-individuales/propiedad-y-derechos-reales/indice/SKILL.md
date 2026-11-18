---
name: indice
description: "Índice de los 15 formularios de propiedad y derechos reales (posesión, obra nueva, deslinde, tercería de dominio, retracto, usufructo, servidumbres). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Propiedad y derechos reales: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Inmuebles** (referencia catastral, superficie, uso) → `consultar_catastro` (y `callejero_catastro` para localizar la dirección).

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/propiedad-y-derechos-reales:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 426 | Demanda de disolución y liquidación de comunidad de bienes de pareja estable | 2008 | `demanda-disolucion-liquidacion-comunidad-bienes-pareja-426` |
| 883 | Demanda posesoria para retener o recuperar la posesión | 2013 | `demanda-posesoria-retener-recuperar-posesion-883` |
| 1150 | Demanda de suspensión de obra nueva que pone en peligro la edificación del demandante | 2013 | `demanda-suspension-obra-nueva-pone-peligro-edificacion-1150` |

## Contestaciones, oposiciones y alegaciones (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 157 | Oposición al deslinde de fincas no escritas | 2021 | `oposicion-deslinde-fincas-no-escritas-157` |
| 178 | Contestación a la demanda de tercería de dominio | 2021 | `contestacion-demanda-terceria-dominio-178` |
| 280 | Oposición a la demanda de retracto | 2020 | `oposicion-demanda-retracto-280` |

## Solicitudes y expedientes (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 701 | Autorización al usufructuario para poner a interés el capital cobrado del crédito vencido | 2015 | `autorizacion-usufructuario-poner-interes-capital-cobrado-701` |
| 708 | Autorización al usufructuario para reclamar créditos vencidos del usufructo | 2015 | `autorizacion-usufructuario-reclamar-creditos-vencidos-708` |
| 739 | Inscripción registral de resolución extranjera de jurisdicción voluntaria | 2015 | `inscripcion-registral-resolucion-extranjera-jurisdiccion-739` |
| 1058 | Declaración judicial de falta de derecho para ocupar | 2013 | `declaracion-judicial-falta-derecho-ocupar-1058` |

## Escritos de trámite (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 709 | Oposición del dueño de finca colindante al deslinde antes de la comparecencia | 2015 | `oposicion-dueno-finca-colindante-deslinde-antes-709` |

## Actos y resoluciones de la Administración o del órgano judicial (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 583 | Notificación de retracto gentilicio (Navarra) | 2016 | `notificacion-retracto-gentilicio-navarra-583` |

## Contratos, escrituras y documentos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 536 | Escritura de usufructo vidual universal recíproco (Galicia) | 2016 | `escritura-usufructo-vidual-universal-reciproco-galicia-536` |

## Otros (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 546 | Servidumbre de paso por pacto (Galicia) | 2016 | `servidumbre-paso-pacto-galicia-546` |
| 1417 | Consentimiento del propietario a una servidumbre | 2013 | `consentimiento-propietario-servidumbre-1417` |
