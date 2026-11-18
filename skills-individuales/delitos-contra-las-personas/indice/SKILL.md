---
name: indice
description: "Índice de los 63 formularios de delitos contra las personas (homicidio, lesiones, omisión del deber de socorro, amenazas, coacciones, acoso, trata, delitos contra menores por internet). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Delitos contra las personas: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/delitos-contra-las-personas:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (8)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 151 | Ocultación del paradero de un cadáver: conformidad de la defensa | 2023 | `ocultacion-paradero-cadaver-conformidad-defensa-151` |
| 303 | Promover por internet la autolesión de menores o discapacitados: conformidad de la defensa | 2021 | `promover-internet-autolesion-menores-discapacitados-303` |
| 309 | Promover por internet trastornos alimenticios en menores o discapacitados: conformidad de la defensa | 2021 | `promover-internet-trastornos-alimenticios-menores-309` |
| 315 | Promover por internet el suicidio de menores o discapacitados: conformidad de la defensa | 2021 | `promover-internet-suicidio-menores-discapacitados-315` |
| 436 | Lesiones: conformidad de la defensa | 2020 | `lesiones-conformidad-defensa-436` |
| 535 | Amenazas informáticas: defensa con conformidad | 2018 | `amenazas-informaticas-defensa-conformidad-535` |
| 636 | Acoso en una comunidad de propietarios (blocking): defensa con conformidad | 2018 | `acoso-comunidad-propietarios-blocking-defensa-636` |
| 684 | Amenazas en redes sociales: defensa con conformidad | 2017 | `amenazas-redes-sociales-defensa-conformidad-684` |

## Recursos e impugnaciones (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 148 | Ocultación del paradero de un cadáver: apelación contra la condena | 2023 | `ocultacion-paradero-cadaver-apelacion-contra-condena-148` |
| 265 | Omisión del deber de socorro: apelación contra la condena | 2022 | `omision-deber-socorro-apelacion-contra-condena-265` |
| 306 | Promover por internet la autolesión de menores o discapacitados: apelación contra la condena | 2021 | `promover-internet-autolesion-menores-discapacitados-306` |
| 311 | Promover por internet trastornos alimenticios en menores o discapacitados: apelación de la condena | 2021 | `promover-internet-trastornos-alimenticios-menores-311` |
| 313 | Promover por internet el suicidio de menores o discapacitados: apelación contra la condena | 2021 | `promover-internet-suicidio-menores-discapacitados-313` |
| 387 | Lesiones por esterilización de discapacitada: apelación contra la condena | 2020 | `lesiones-esterilizacion-discapacitada-apelacion-contra-387` |
| 435 | Lesiones: apelación contra la condena | 2020 | `lesiones-apelacion-contra-condena-435` |
| 533 | Apelación contra la condena por amenazas informáticas | 2018 | `apelacion-contra-condena-amenazas-informaticas-533` |
| 634 | Apelación contra la condena por acoso en una comunidad de propietarios (blocking) | 2018 | `apelacion-contra-condena-acoso-comunidad-propietarios-634` |
| 681 | Apelación contra la condena por amenazas en redes sociales | 2017 | `apelacion-contra-condena-amenazas-redes-sociales-681` |
| 700 | Apelación contra la condena por coacciones por mensajes de WhatsApp | 2017 | `apelacion-contra-condena-coacciones-mensajes-whatsapp-700` |

## Querellas y denuncias (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 150 | Ocultación del paradero de un cadáver: querella | 2023 | `ocultacion-paradero-cadaver-querella-150` |
| 266 | Omisión de socorro por no prestar asistencia sanitaria: querella | 2022 | `omision-socorro-no-prestar-asistencia-sanitaria-querella-266` |
| 302 | Promover por internet la autolesión de menores o discapacitados: denuncia | 2021 | `promover-internet-autolesion-menores-discapacitados-302` |
| 310 | Promover por internet trastornos alimenticios en menores o discapacitados: querella | 2021 | `promover-internet-trastornos-alimenticios-menores-310` |
| 316 | Promover por internet el suicidio de menores o discapacitados: denuncia | 2021 | `promover-internet-suicidio-menores-discapacitados-316` |
| 388 | Lesiones por esterilización de discapacitada: querella | 2020 | `lesiones-esterilizacion-discapacitada-querella-388` |
| 531 | Amenazas informáticas: querella | 2018 | `amenazas-informaticas-querella-531` |
| 638 | Acoso en una comunidad de propietarios (blocking): querella | 2018 | `acoso-comunidad-propietarios-blocking-querella-638` |
| 685 | Amenazas en redes sociales: querella | 2017 | `amenazas-redes-sociales-querella-685` |
| 710 | Homicidio o lesiones por imprudencia médica: querella | 2017 | `homicidio-lesiones-imprudencia-medica-querella-710` |
| 719 | Coacciones por mensajes de WhatsApp: querella | 2017 | `coacciones-mensajes-whatsapp-querella-719` |
| 817 | Amenazas: querella | 2016 | `amenazas-querella-817` |

## Escritos de acusación (17)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 104 | Lesiones dolosas o imprudentes: acusación con conclusiones alternativas | 2023 | `lesiones-dolosas-imprudentes-acusacion-conclusiones-104` |
| 149 | Ocultación del paradero de un cadáver: escrito de acusación | 2023 | `ocultacion-paradero-cadaver-escrito-acusacion-149` |
| 263 | Omisión del deber de socorro: calificación provisional de la acusación | 2022 | `omision-deber-socorro-calificacion-provisional-acusacion-263` |
| 272 | Trata de seres humanos: calificación provisional de la acusación | 2022 | `trata-seres-humanos-calificacion-provisional-acusacion-272` |
| 277 | Lesiones con agravante de aporofobia o exclusión social: escrito de acusación | 2022 | `lesiones-agravante-aporofobia-exclusion-social-escrito-277` |
| 297 | Lesiones a menor de edad: escrito de acusación | 2021 | `lesiones-menor-edad-escrito-acusacion-297` |
| 304 | Promover por internet la autolesión de menores o discapacitados: escrito de acusación | 2021 | `promover-internet-autolesion-menores-discapacitados-304` |
| 308 | Promover por internet trastornos alimenticios en menores o discapacitados: escrito de acusación | 2021 | `promover-internet-trastornos-alimenticios-menores-308` |
| 314 | Promover por internet el suicidio de menores o discapacitados: escrito de acusación | 2021 | `promover-internet-suicidio-menores-discapacitados-314` |
| 386 | Lesiones por esterilización de discapacitada: calificación provisional de la acusación particular | 2020 | `lesiones-esterilizacion-discapacitada-calificacion-386` |
| 437 | Lesiones: escrito de acusación | 2020 | `lesiones-escrito-acusacion-437` |
| 532 | Amenazas informáticas: calificación provisional de la acusación | 2018 | `amenazas-informaticas-calificacion-provisional-acusacion-532` |
| 637 | Acoso en una comunidad de propietarios (blocking): acusación | 2018 | `acoso-comunidad-propietarios-blocking-acusacion-637` |
| 682 | Amenazas en redes sociales: calificación provisional de la acusación | 2017 | `amenazas-redes-sociales-calificacion-provisional-682` |
| 698 | Coacciones por mensajes de WhatsApp: acusación | 2017 | `coacciones-mensajes-whatsapp-acusacion-698` |
| 814 | Amenazas: calificación provisional de la acusación | 2016 | `amenazas-calificacion-provisional-acusacion-814` |
| 816 | Acoso telefónico o stalking: acusación | 2016 | `acoso-telefonico-stalking-acusacion-816` |

## Escritos de defensa (13)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 152 | Ocultación del paradero de un cadáver: escrito de defensa | 2023 | `ocultacion-paradero-cadaver-escrito-defensa-152` |
| 264 | Omisión del deber de socorro: calificación provisional de la defensa | 2022 | `omision-deber-socorro-calificacion-provisional-defensa-264` |
| 307 | Promover por internet la autolesión de menores o discapacitados: escrito de defensa | 2021 | `promover-internet-autolesion-menores-discapacitados-307` |
| 312 | Promover por internet trastornos alimenticios en menores o discapacitados: escrito de defensa | 2021 | `promover-internet-trastornos-alimenticios-menores-312` |
| 317 | Promover por internet el suicidio de menores o discapacitados: escrito de defensa | 2021 | `promover-internet-suicidio-menores-discapacitados-317` |
| 385 | Lesiones por esterilización de discapacitada: calificación provisional de la defensa | 2020 | `lesiones-esterilizacion-discapacitada-calificacion-385` |
| 438 | Lesiones: escrito de defensa | 2020 | `lesiones-escrito-defensa-438` |
| 534 | Amenazas informáticas: calificación provisional de la defensa | 2018 | `amenazas-informaticas-calificacion-provisional-defensa-534` |
| 635 | Acoso en una comunidad de propietarios (blocking): defensa | 2018 | `acoso-comunidad-propietarios-blocking-defensa-635` |
| 683 | Amenazas en redes sociales: calificación provisional de la defensa | 2017 | `amenazas-redes-sociales-calificacion-provisional-defensa-683` |
| 699 | Coacciones por mensajes de WhatsApp: defensa | 2017 | `coacciones-mensajes-whatsapp-defensa-699` |
| 815 | Acoso o stalking: defensa | 2016 | `acoso-stalking-defensa-815` |
| 818 | Amenazas: calificación provisional de la defensa | 2016 | `amenazas-calificacion-provisional-defensa-818` |

## Medidas cautelares y protección (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 737 | Acoso o stalking: pedir medida cautelar de no aproximación y no comunicación | 2016 | `acoso-stalking-pedir-medida-cautelar-no-aproximacion-no-737` |

## Resoluciones, actas y documentos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 35 | Trata en tránsito: auto de inhibición a favor del Tribunal Central de Instancia | 2025 | `trata-transito-auto-inhibicion-favor-tribunal-central-35` |
