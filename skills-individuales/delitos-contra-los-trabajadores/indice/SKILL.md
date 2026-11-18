---
name: indice
description: "Índice de los 22 formularios de delitos contra los derechos de los trabajadores (condiciones ilegales, discriminación en el empleo, riesgos laborales, acoso laboral). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Delitos contra los derechos de los trabajadores: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/delitos-contra-los-trabajadores:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 165 | Condiciones laborales ilegales (contratación irregular o pese a sanción): conformidad de la defensa | 2023 | `condiciones-laborales-ilegales-contratacion-irregular-165` |
| 296 | Discriminación grave en el empleo: conformidad de la defensa | 2021 | `discriminacion-grave-empleo-conformidad-defensa-296` |
| 459 | Infracción de normas de riesgos laborales por imprudencia grave: defensa con conformidad | 2020 | `infraccion-normas-riesgos-laborales-imprudencia-grave-459` |
| 464 | Infracción de normas de riesgos laborales: defensa con conformidad | 2019 | `infraccion-normas-riesgos-laborales-defensa-conformidad-464` |

## Recursos e impugnaciones (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 163 | Condiciones laborales ilegales (contratación irregular o pese a sanción): apelación de la condena | 2023 | `condiciones-laborales-ilegales-contratacion-irregular-163` |
| 294 | Discriminación grave en el empleo: apelación contra la condena | 2021 | `discriminacion-grave-empleo-apelacion-contra-condena-294` |
| 462 | Apelación contra la condena por infracción de normas de riesgos laborales por imprudencia grave | 2020 | `apelacion-contra-condena-infraccion-normas-riesgos-462` |
| 465 | Apelación contra la condena por infracción de normas de riesgos laborales | 2019 | `apelacion-contra-condena-infraccion-normas-riesgos-465` |

## Querellas y denuncias (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 161 | Condiciones laborales ilegales (contratación irregular o pese a sanción): querella | 2023 | `condiciones-laborales-ilegales-contratacion-irregular-161` |
| 292 | Discriminación grave en el empleo: querella | 2021 | `discriminacion-grave-empleo-querella-292` |
| 460 | Infracción de normas de riesgos laborales por imprudencia grave: querella | 2020 | `infraccion-normas-riesgos-laborales-imprudencia-grave-460` |
| 467 | Infracción de normas de riesgos laborales: querella | 2019 | `infraccion-normas-riesgos-laborales-querella-467` |
| 830 | Acoso laboral: querella | 2016 | `acoso-laboral-querella-830` |

## Escritos de acusación (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 162 | Condiciones laborales ilegales (contratación irregular o pese a sanción): escrito de acusación | 2023 | `condiciones-laborales-ilegales-contratacion-irregular-162` |
| 293 | Discriminación grave en el empleo: escrito de acusación | 2021 | `discriminacion-grave-empleo-escrito-acusacion-293` |
| 461 | Infracción de normas de riesgos laborales por imprudencia grave: acusación | 2020 | `infraccion-normas-riesgos-laborales-imprudencia-grave-461` |
| 832 | Acoso laboral: acusación | 2016 | `acoso-laboral-acusacion-832` |

## Escritos de defensa (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 164 | Condiciones laborales ilegales (contratación irregular o pese a sanción): escrito de defensa | 2023 | `condiciones-laborales-ilegales-contratacion-irregular-164` |
| 295 | Discriminación grave en el empleo: escrito de defensa | 2021 | `discriminacion-grave-empleo-escrito-defensa-295` |
| 466 | Infracción de normas de riesgos laborales: defensa | 2019 | `infraccion-normas-riesgos-laborales-defensa-466` |
| 686 | Infracción de normas de riesgos laborales por imprudencia grave: defensa | 2017 | `infraccion-normas-riesgos-laborales-imprudencia-grave-686` |
| 833 | Acoso laboral: defensa | 2016 | `acoso-laboral-defensa-833` |
