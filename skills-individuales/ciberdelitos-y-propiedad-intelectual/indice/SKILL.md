---
name: indice
description: "Índice de los 61 formularios de ciberdelitos y propiedad intelectual (estafa informática (phishing, vishing, pharming), criptomonedas, acceso ilegal, daños informáticos, propiedad intelectual e industrial). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Ciberdelitos y propiedad intelectual: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/ciberdelitos-y-propiedad-intelectual:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (10)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 132 | Estafa con criptomonedas: conformidad de la defensa | 2023 | `estafa-criptomonedas-conformidad-defensa-132` |
| 490 | Estafa informática (vishing): defensa con conformidad | 2019 | `estafa-informatica-vishing-defensa-conformidad-490` |
| 552 | Facilitar fraudulentamente el acceso a un servicio de radiodifusión: defensa con conformidad | 2018 | `facilitar-fraudulentamente-acceso-servicio-radiodifusion-552` |
| 621 | Propiedad industrial por internet: defensa con conformidad | 2018 | `propiedad-industrial-internet-defensa-conformidad-621` |
| 628 | Propiedad intelectual por internet: defensa con conformidad | 2018 | `propiedad-intelectual-internet-defensa-conformidad-628` |
| 629 | Acceso ilegal a sistemas informáticos (allanamiento o intrusismo): defensa con conformidad | 2018 | `acceso-ilegal-sistemas-informaticos-allanamiento-629` |
| 665 | Pharming y estafa informática (phishing): defensa con conformidad del scammer o del mulero | 2017 | `pharming-estafa-informatica-phishing-defensa-conformidad-665` |
| 680 | Daños informáticos (ciberataque): defensa con conformidad | 2017 | `danos-informaticos-ciberataque-defensa-conformidad-680` |
| 688 | Suplantación de identidad (falsedad en documento privado): defensa con conformidad | 2017 | `suplantacion-identidad-falsedad-documento-privado-688` |
| 876 | Propiedad intelectual: defensa con conformidad | 2016 | `propiedad-intelectual-defensa-conformidad-876` |

## Recursos e impugnaciones (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 133 | Estafa con criptomonedas: apelación contra la condena | 2023 | `estafa-criptomonedas-apelacion-contra-condena-133` |
| 491 | Apelación contra la condena por estafa informática (vishing) | 2019 | `apelacion-contra-condena-estafa-informatica-vishing-491` |
| 551 | Apelación contra la condena por facilitar fraudulentamente el acceso a un servicio de radiodifusión | 2018 | `apelacion-contra-condena-facilitar-fraudulentamente-551` |
| 605 | Apelación contra la condena por falsificación de moneda con alta tecnología | 2018 | `apelacion-contra-condena-falsificacion-moneda-alta-605` |
| 620 | Apelación contra la condena por delito contra la propiedad industrial por internet | 2018 | `apelacion-contra-condena-delito-contra-propiedad-620` |
| 625 | Apelación contra la condena por delito contra la propiedad intelectual por internet | 2018 | `apelacion-contra-condena-delito-contra-propiedad-625` |
| 630 | Apelación contra la condena por acceso ilegal a sistemas informáticos (allanamiento o intrusismo) | 2018 | `apelacion-contra-condena-acceso-ilegal-sistemas-630` |
| 668 | Pharming y estafa informática (phishing): apelación del scammer o del mulero contra la condena | 2017 | `pharming-estafa-informatica-phishing-apelacion-scammer-668` |
| 677 | Apelación contra la condena por daños informáticos (ciberataque) | 2017 | `apelacion-contra-condena-danos-informaticos-ciberataque-677` |
| 689 | Apelación contra la condena por falsedad en documento privado por suplantación en redes sociales | 2017 | `apelacion-contra-condena-falsedad-documento-privado-689` |
| 692 | Apelación contra la condena por estafa informática (phishing) | 2017 | `apelacion-contra-condena-estafa-informatica-phishing-692` |
| 875 | Apelación contra la condena por delito contra la propiedad intelectual | 2016 | `apelacion-contra-condena-delito-contra-propiedad-875` |

## Querellas y denuncias (13)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 134 | Estafa con criptomonedas: querella | 2023 | `estafa-criptomonedas-querella-134` |
| 434 | Estafa informática (phishing) en cuenta bancaria: querella | 2020 | `estafa-informatica-phishing-cuenta-bancaria-querella-434` |
| 492 | Estafa informática (vishing): querella | 2019 | `estafa-informatica-vishing-querella-492` |
| 555 | Facilitar fraudulentamente el acceso a un servicio de radiodifusión: querella | 2018 | `facilitar-fraudulentamente-acceso-servicio-radiodifusion-555` |
| 606 | Falsificación de moneda con alta tecnología: querella | 2018 | `falsificacion-moneda-alta-tecnologia-querella-606` |
| 623 | Propiedad industrial por internet: querella | 2018 | `propiedad-industrial-internet-querella-623` |
| 624 | Propiedad intelectual por internet: querella | 2018 | `propiedad-intelectual-internet-querella-624` |
| 633 | Acceso a sistemas informáticos sin autorización del titular (allanamiento o intrusismo): querella | 2018 | `acceso-sistemas-informaticos-sin-autorizacion-titular-633` |
| 666 | Pharming y estafa informática (phishing): querella | 2017 | `pharming-estafa-informatica-phishing-querella-666` |
| 678 | Daños informáticos (ciberataque): querella | 2017 | `danos-informaticos-ciberataque-querella-678` |
| 691 | Suplantación de identidad en redes sociales (falsedad en documento privado): denuncia | 2017 | `suplantacion-identidad-redes-sociales-falsedad-documento-691` |
| 696 | Estafa informática (phishing): denuncia | 2017 | `estafa-informatica-phishing-denuncia-696` |
| 848 | Tenencia de programas informáticos para falsificar tarjetas bancarias: querella | 2016 | `tenencia-programas-informaticos-falsificar-tarjetas-848` |

## Escritos de acusación (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 135 | Estafa con criptomonedas: escrito de acusación | 2023 | `estafa-criptomonedas-escrito-acusacion-135` |
| 493 | Estafa informática (vishing): acusación | 2019 | `estafa-informatica-vishing-acusacion-493` |
| 554 | Facilitar fraudulentamente el acceso a un servicio de radiodifusión: acusación | 2018 | `facilitar-fraudulentamente-acceso-servicio-radiodifusion-554` |
| 604 | Falsificación de moneda con alta tecnología: calificación provisional de la acusación particular | 2018 | `falsificacion-moneda-alta-tecnologia-calificacion-604` |
| 622 | Propiedad industrial por internet: acusación | 2018 | `propiedad-industrial-internet-acusacion-622` |
| 626 | Propiedad intelectual por internet: acusación | 2018 | `propiedad-intelectual-internet-acusacion-626` |
| 632 | Acceso ilegal a sistemas informáticos (allanamiento o intrusismo): acusación | 2018 | `acceso-ilegal-sistemas-informaticos-allanamiento-632` |
| 664 | Pharming y estafa informática (phishing): acusación | 2017 | `pharming-estafa-informatica-phishing-acusacion-664` |
| 679 | Daños informáticos (ciberataque): acusación | 2017 | `danos-informaticos-ciberataque-acusacion-679` |
| 690 | Suplantación de identidad en redes sociales (falsedad en documento privado): acusación | 2017 | `suplantacion-identidad-redes-sociales-falsedad-documento-690` |
| 693 | Estafa informática (phishing): acusación | 2017 | `estafa-informatica-phishing-acusacion-693` |
| 877 | Propiedad intelectual: acusación | 2016 | `propiedad-intelectual-acusacion-877` |

## Escritos de defensa (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 131 | Estafa con criptomonedas: escrito de defensa | 2023 | `estafa-criptomonedas-escrito-defensa-131` |
| 489 | Estafa informática (vishing): defensa | 2019 | `estafa-informatica-vishing-defensa-489` |
| 553 | Facilitar fraudulentamente el acceso a un servicio de radiodifusión: defensa | 2018 | `facilitar-fraudulentamente-acceso-servicio-radiodifusion-553` |
| 603 | Falsificación de moneda con alta tecnología: calificación provisional de la defensa | 2018 | `falsificacion-moneda-alta-tecnologia-calificacion-603` |
| 619 | Propiedad industrial por internet: defensa | 2018 | `propiedad-industrial-internet-defensa-619` |
| 627 | Propiedad intelectual por internet: defensa | 2018 | `propiedad-intelectual-internet-defensa-627` |
| 631 | Acceso ilegal a sistemas informáticos (allanamiento o intrusismo): defensa | 2018 | `acceso-ilegal-sistemas-informaticos-allanamiento-631` |
| 667 | Pharming y estafa informática (phishing): defensa del scammer o del mulero | 2017 | `pharming-estafa-informatica-phishing-defensa-scammer-667` |
| 676 | Daños informáticos (ciberataque): defensa | 2017 | `danos-informaticos-ciberataque-defensa-676` |
| 687 | Suplantación de identidad en redes sociales (falsedad en documento privado): defensa | 2017 | `suplantacion-identidad-redes-sociales-falsedad-documento-687` |
| 694 | Estafa informática (phishing): defensa | 2017 | `estafa-informatica-phishing-defensa-694` |
| 874 | Propiedad intelectual: defensa | 2016 | `propiedad-intelectual-defensa-874` |

## Solicitudes y escritos de trámite (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 695 | Estafa informática (phishing): pedir oficio al banco para identificar al autor | 2017 | `estafa-informatica-phishing-pedir-oficio-banco-695` |
| 849 | Avisar al banco de un crédito no formalizado por el cliente y del cargo de su cuota en cuenta | 2016 | `avisar-banco-credito-no-formalizado-cliente-cargo-cuota-849` |
