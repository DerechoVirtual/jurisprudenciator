---
name: indice
description: "Índice de los 11 formularios de protección de datos y control empresarial (RGPD, LOPDGDD, videovigilancia, geolocalización, dispositivos digitales, códigos de conducta). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Protección de datos y control empresarial: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/datos-y-control-empresarial:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Contratos, cláusulas y anexos (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 172 | Protección de datos en contratos de trabajo: cláusula | 2020 | `proteccion-datos-contratos-trabajo-clausula-172` |
| 173 | Confidencialidad, control de medios y desconexión digital: cláusula | 2020 | `confidencialidad-control-medios-desconexion-digital-173` |
| 251 | Protección de datos en contratos con empresa subcontratista: cláusula | 2018 | `proteccion-datos-contratos-empresa-subcontratista-251` |
| 252 | Información sobre protección de datos en la geolocalización: cláusula | 2018 | `informacion-sobre-proteccion-datos-geolocalizacion-252` |

## Cartas y comunicaciones a la plantilla (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 223 | Aviso emergente sobre el uso laboral de los medios de la empresa | 2019 | `aviso-emergente-sobre-uso-laboral-medios-empresa-223` |
| 253 | Instalación de cámaras de videovigilancia: aviso a la representación de los trabajadores | 2018 | `instalacion-camaras-videovigilancia-aviso-representacion-253` |
| 376 | Aviso al trabajador de videovigilancia, control de jornada o geolocalización | 2016 | `aviso-trabajador-videovigilancia-control-jornada-376` |

## Actas, acuerdos, planes y protocolos (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 222 | Información sobre protección de datos a los empleados | 2019 | `informacion-sobre-proteccion-datos-empleados-222` |
| 232 | Código de conducta en la relación empresa-trabajador | 2019 | `codigo-conducta-relacion-empresa-trabajador-232` |
| 233 | Vestimenta en la empresa: código | 2019 | `vestimenta-empresa-codigo-233` |
| 239 | Normas de uso del sistema informático y las comunicaciones electrónicas | 2019 | `normas-uso-sistema-informatico-comunicaciones-239` |
