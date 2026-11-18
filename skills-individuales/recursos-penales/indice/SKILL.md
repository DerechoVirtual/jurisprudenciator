---
name: indice
description: "Índice de los 24 formularios de recursos penales (reforma, apelación, queja, casación, impugnaciones, amparo). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Recursos penales: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/recursos-penales:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 54 | Procedimiento común: apelación de la defensa contra la sentencia de conformidad | 2025 | `procedimiento-comun-apelacion-defensa-contra-sentencia-54` |

## Recursos e impugnaciones (21)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 24 | Oponerse al recurso de reforma y subsidiario de apelación contra un auto del abreviado | 2026 | `oponerse-recurso-reforma-subsidiario-apelacion-contra-24` |
| 53 | Abreviado: apelación contra el auto que le pone fin tras la audiencia preliminar | 2025 | `abreviado-apelacion-contra-auto-le-pone-fin-tras-53` |
| 70 | Recurso de amparo (Acuerdo TC de 15 de marzo de 2023, válido hasta el 14 de septiembre de 2026) | 2024 | `recurso-amparo-acuerdo-tc-15-marzo-2023-valido-hasta-14-70` |
| 101 | Abreviado: oposición a la apelación contra la denegación de apertura del juicio oral | 2023 | `abreviado-oposicion-apelacion-contra-denegacion-apertura-101` |
| 103 | Abreviado: apelación contra el auto que deniega la apertura del juicio oral | 2023 | `abreviado-apelacion-contra-auto-deniega-apertura-juicio-103` |
| 121 | Querella inadmitida: reforma y subsidiario de apelación | 2023 | `querella-inadmitida-reforma-subsidiario-apelacion-121` |
| 153 | Recurso de anulación: impugnación de la parte acusadora | 2023 | `recurso-anulacion-impugnacion-parte-acusadora-153` |
| 154 | Abreviado: oposición a la adhesión a la apelación contra la sentencia | 2023 | `abreviado-oposicion-adhesion-apelacion-contra-sentencia-154` |
| 159 | Paso del abreviado a jurado denegado tácitamente: queja de la acusación particular | 2023 | `paso-abreviado-jurado-denegado-tacitamente-queja-159` |
| 160 | Paso del ordinario al abreviado denegado: queja del investigado | 2023 | `paso-ordinario-abreviado-denegado-queja-investigado-160` |
| 167 | Prisión provisional en el abreviado: reforma y subsidiario de apelación | 2022 | `prision-provisional-abreviado-reforma-subsidiario-167` |
| 169 | Sobreseimiento provisional: oposición a la apelación | 2022 | `sobreseimiento-provisional-oposicion-apelacion-169` |
| 251 | Sobreseimiento libre de la AP o la AN: recurso de casación | 2022 | `sobreseimiento-libre-ap-an-recurso-casacion-251` |
| 479 | Sobreseimiento provisional tras las diligencias previas: reforma y subsidiaria apelación | 2019 | `sobreseimiento-provisional-tras-diligencias-previas-479` |
| 486 | Prórroga de la instrucción: reforma y subsidiaria apelación | 2019 | `prorroga-instruccion-reforma-subsidiaria-apelacion-486` |
| 556 | Prueba de la defensa denegada en el procedimiento abreviado: queja (hasta el 2 de abril de 2025) | 2018 | `prueba-defensa-denegada-procedimiento-abreviado-queja-556` |
| 617 | Auto de libertad provisional del investigado o encausado: reforma y subsidiaria apelación | 2018 | `auto-libertad-provisional-investigado-encausado-reforma-617` |
| 618 | Auto de libertad provisional del investigado o encausado: apelación | 2018 | `auto-libertad-provisional-investigado-encausado-618` |
| 742 | Denegación de traductor o intérprete: reforma de la defensa del investigado | 2016 | `denegacion-traductor-interprete-reforma-defensa-742` |
| 770 | Auto de la Audiencia Provincial: apelación penal | 2016 | `auto-audiencia-provincial-apelacion-penal-770` |
| 18 (Procesal) | Revisión penal tras una sentencia del TEDH: interposición del recurso | 2025 | `revision-penal-tras-sentencia-tedh-interposicion-recurso-p18` |

## Resoluciones, actas y documentos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 158 | Casación desierta: decreto del Letrado de la Administración de Justicia | 2023 | `casacion-desierta-decreto-letrado-administracion-158` |

## Solicitudes y escritos de trámite (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 19 (Procesal) | Revisión penal tras una sentencia del TEDH: pedir autorización para recurrir | 2025 | `revision-penal-tras-sentencia-tedh-pedir-autorizacion-p19` |
