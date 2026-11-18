---
name: indice
description: "Índice de los 39 formularios de seguridad vial (alcoholemia, negativa a las pruebas, conducción sin permiso, temeraria, velocidad, abandono del lugar del accidente, juicio rápido). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Seguridad vial: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/seguridad-vial:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (10)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 240 | Grave riesgo vial por colocar obstáculos en la vía: conformidad de la defensa | 2022 | `grave-riesgo-vial-colocar-obstaculos-via-conformidad-240` |
| 247 | Conducción sin permiso y bajo los efectos de drogas o alcohol: conformidad de la defensa | 2022 | `conduccion-sin-permiso-bajo-efectos-drogas-alcohol-247` |
| 359 | Conducción a velocidad excesiva: conformidad de la defensa | 2021 | `conduccion-velocidad-excesiva-conformidad-defensa-359` |
| 366 | Conducción temeraria con manifiesto desprecio por la vida ajena: conformidad de la defensa | 2021 | `conduccion-temeraria-manifiesto-desprecio-vida-ajena-366` |
| 371 | Conducción temeraria: conformidad de la defensa | 2021 | `conduccion-temeraria-conformidad-defensa-371` |
| 505 | Abandono del lugar del accidente y lesiones imprudentes de tráfico: defensa con conformidad | 2019 | `abandono-lugar-accidente-lesiones-imprudentes-trafico-505` |
| 796 | Conducción bajo la influencia del alcohol: defensa con conformidad en juicio rápido | 2016 | `conduccion-bajo-influencia-alcohol-defensa-conformidad-796` |
| 798 | Conducción bajo la influencia del alcohol y lesiones: defensa con conformidad en el abreviado | 2016 | `conduccion-bajo-influencia-alcohol-lesiones-defensa-798` |
| 801 | Negativa a las pruebas de alcoholemia: defensa con conformidad en el abreviado | 2016 | `negativa-pruebas-alcoholemia-defensa-conformidad-801` |
| 802 | Negativa a las pruebas de alcoholemia: defensa con conformidad en juicio rápido | 2016 | `negativa-pruebas-alcoholemia-defensa-conformidad-juicio-802` |

## Recursos e impugnaciones (9)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 118 | Lesiones en accidente de tráfico: oposición a la reforma contra el sobreseimiento | 2023 | `lesiones-accidente-trafico-oposicion-reforma-contra-118` |
| 238 | Grave riesgo vial por colocar obstáculos en la vía: apelación contra la condena | 2022 | `grave-riesgo-vial-colocar-obstaculos-via-apelacion-238` |
| 248 | Conducción sin permiso y bajo los efectos de drogas o alcohol: apelación contra la condena | 2022 | `conduccion-sin-permiso-bajo-efectos-drogas-alcohol-248` |
| 360 | Conducción a velocidad excesiva: apelación contra la condena | 2021 | `conduccion-velocidad-excesiva-apelacion-contra-condena-360` |
| 363 | Conducción temeraria con manifiesto desprecio por la vida ajena: apelación contra la condena | 2021 | `conduccion-temeraria-manifiesto-desprecio-vida-ajena-363` |
| 368 | Conducción temeraria: apelación contra la condena | 2021 | `conduccion-temeraria-apelacion-contra-condena-368` |
| 504 | Apelación contra la condena por abandono del lugar del accidente y lesiones imprudentes de tráfico | 2019 | `apelacion-contra-condena-abandono-lugar-accidente-504` |
| 797 | Apelación contra la condena por conducir bajo la influencia del alcohol | 2016 | `apelacion-contra-condena-conducir-bajo-influencia-797` |
| 800 | Apelación contra la condena por negarse a las pruebas de alcoholemia | 2016 | `apelacion-contra-condena-negarse-pruebas-alcoholemia-800` |

## Querellas y denuncias (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 250 | Conducción sin permiso y bajo los efectos de drogas o alcohol: querella | 2022 | `conduccion-sin-permiso-bajo-efectos-drogas-alcohol-250` |
| 370 | Conducción temeraria: denuncia | 2021 | `conduccion-temeraria-denuncia-370` |
| 372 | Delito leve de lesiones por imprudencia menos grave con vehículo a motor: denuncia | 2021 | `delito-leve-lesiones-imprudencia-menos-grave-vehiculo-372` |
| 506 | Abandono del lugar del accidente y lesiones imprudentes de tráfico: querella | 2019 | `abandono-lugar-accidente-lesiones-imprudentes-trafico-506` |
| 794 | Conducción bajo la influencia del alcohol y lesiones: querella | 2016 | `conduccion-bajo-influencia-alcohol-lesiones-querella-794` |

## Escritos de acusación (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 105 | Accidente con vehículo a motor: acusación del actor civil en el abreviado | 2023 | `accidente-vehiculo-motor-acusacion-actor-civil-abreviado-105` |
| 249 | Conducción sin permiso y bajo los efectos de drogas o alcohol: escrito de acusación | 2022 | `conduccion-sin-permiso-bajo-efectos-drogas-alcohol-249` |
| 361 | Conducción a velocidad excesiva: escrito de acusación | 2021 | `conduccion-velocidad-excesiva-escrito-acusacion-361` |
| 365 | Conducción temeraria con manifiesto desprecio por la vida ajena: escrito de acusación | 2021 | `conduccion-temeraria-manifiesto-desprecio-vida-ajena-365` |
| 369 | Conducción temeraria: escrito de acusación | 2021 | `conduccion-temeraria-escrito-acusacion-369` |
| 507 | Abandono del lugar del accidente y lesiones imprudentes de tráfico: acusación | 2019 | `abandono-lugar-accidente-lesiones-imprudentes-trafico-507` |
| 795 | Conducción bajo la influencia del alcohol y lesiones: acusación | 2016 | `conduccion-bajo-influencia-alcohol-lesiones-acusacion-795` |

## Escritos de defensa (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 239 | Grave riesgo vial por colocar obstáculos en la vía: escrito de defensa | 2022 | `grave-riesgo-vial-colocar-obstaculos-via-escrito-defensa-239` |
| 246 | Conducción sin permiso y bajo los efectos de drogas o alcohol: escrito de defensa | 2022 | `conduccion-sin-permiso-bajo-efectos-drogas-alcohol-246` |
| 358 | Conducción a velocidad excesiva: escrito de defensa | 2021 | `conduccion-velocidad-excesiva-escrito-defensa-358` |
| 364 | Conducción temeraria con manifiesto desprecio por la vida ajena: escrito de defensa | 2021 | `conduccion-temeraria-manifiesto-desprecio-vida-ajena-364` |
| 367 | Conducción temeraria: escrito de defensa | 2021 | `conduccion-temeraria-escrito-defensa-367` |
| 503 | Abandono del lugar del accidente y lesiones imprudentes de tráfico: defensa | 2019 | `abandono-lugar-accidente-lesiones-imprudentes-trafico-503` |

## Solicitudes y escritos de trámite (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 362 | Allegado del perjudicado: reclamación a la aseguradora | 2021 | `allegado-perjudicado-reclamacion-aseguradora-362` |
| 799 | Negativa a las pruebas de alcoholemia: la defensa pide el proceso por aceptación de decreto | 2016 | `negativa-pruebas-alcoholemia-defensa-pide-proceso-799` |
