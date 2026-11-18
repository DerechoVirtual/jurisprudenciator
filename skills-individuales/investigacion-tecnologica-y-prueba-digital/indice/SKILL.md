---
name: indice
description: "Índice de los 28 formularios de investigación tecnológica y prueba digital (intervención de comunicaciones, registro de dispositivos, prueba digital, pericial informática, prueba ilícita). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Investigación tecnológica y prueba digital: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/investigacion-tecnologica-y-prueba-digital:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Recursos e impugnaciones (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 701 | Apelación contra una condena basada en prueba ilícita | 2017 | `apelacion-contra-condena-basada-prueba-ilicita-701` |

## Escritos de acusación (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 703 | Prueba digital y pericial informática: propuesta en el escrito de acusación | 2017 | `prueba-digital-pericial-informatica-propuesta-escrito-703` |

## Escritos de defensa (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 562 | Nulidad de las intervenciones telefónicas: defensa | 2018 | `nulidad-intervenciones-telefonicas-defensa-562` |
| 563 | Tráfico de drogas con intervenciones telefónicas nulas: defensa | 2018 | `trafico-drogas-intervenciones-telefonicas-nulas-defensa-563` |
| 704 | Impugnar una prueba digital en el escrito de defensa | 2017 | `impugnar-prueba-digital-escrito-defensa-704` |

## Resoluciones, actas y documentos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 735 | Computación en la nube (cloud computing): contrato de acceso a datos por cuenta de terceros | 2016 | `computacion-nube-cloud-computing-contrato-acceso-datos-735` |

## Solicitudes y escritos de trámite (22)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 60 | Prueba ilícita: el acusado pide audiencia preliminar (antes y después del 3 de abril de 2025) | 2025 | `prueba-ilicita-acusado-pide-audiencia-preliminar-antes-60` |
| 61 | Intervenciones telefónicas: negarse a dar al juez el patrón del móvil para el volcado | 2024 | `intervenciones-telefonicas-negarse-dar-juez-patron-movil-61` |
| 65 | Excluir del proceso las comunicaciones entre abogados defensores aportadas sin autorización | 2024 | `excluir-proceso-comunicaciones-entre-abogados-defensores-65` |
| 68 | Aportar como prueba comunicaciones o documentos entre defensores con autorización | 2024 | `aportar-como-prueba-comunicaciones-documentos-entre-68` |
| 702 | Querellante: aportar acta notarial del contenido de una web como prueba preconstituida | 2017 | `querellante-aportar-acta-notarial-contenido-web-como-702` |
| 705 | Defensa: pedir la nulidad de la prueba digital aportada | 2017 | `defensa-pedir-nulidad-prueba-digital-aportada-705` |
| 706 | Querellante: pedir que se reproduzca una grabación y aportarla como prueba preconstituida | 2017 | `querellante-pedir-reproduzca-grabacion-aportarla-como-706` |
| 707 | Querellante: proponer o aportar pericial informática en instrucción ante prueba digital impugnada | 2017 | `querellante-proponer-aportar-pericial-informatica-707` |
| 708 | Querellante: aportar prueba digital en la instrucción | 2017 | `querellante-aportar-prueba-digital-instruccion-708` |
| 709 | Querellado: impugnar la prueba digital (WhatsApp u otros) aportada en la instrucción | 2017 | `querellado-impugnar-prueba-digital-whatsapp-u-otros-709` |
| 711 | Deducir testimonio por posible delito hallado en correspondencia o correo electrónico intervenidos | 2017 | `deducir-testimonio-posible-delito-hallado-711` |
| 712 | Pedir el registro remoto de equipos informáticos por delitos cometidos con ellos | 2017 | `pedir-registro-remoto-equipos-informaticos-delitos-712` |
| 713 | Pedir datos de comunicaciones electrónicas para averiguar un delito | 2017 | `pedir-datos-comunicaciones-electronicas-averiguar-delito-713` |
| 714 | Pedir la apertura de la correspondencia ya intervenida | 2017 | `pedir-apertura-correspondencia-ya-intervenida-714` |
| 715 | Pedir la instalación de dispositivos técnicos de localización y seguimiento | 2017 | `pedir-instalacion-dispositivos-tecnicos-localizacion-715` |
| 716 | Pedir la captación de imágenes del investigado o de su entorno en lugar público | 2017 | `pedir-captacion-imagenes-investigado-entorno-lugar-716` |
| 720 | Sexting: pedir el registro de equipos informáticos para determinar la autoría | 2017 | `sexting-pedir-registro-equipos-informaticos-determinar-720` |
| 763 | Pedir al fiscal que solicite al juez intervenir las comunicaciones | 2016 | `pedir-fiscal-solicite-juez-intervenir-comunicaciones-763` |
| 764 | Pedir al fiscal que solicite al juez intervenir la correspondencia del investigado | 2016 | `pedir-fiscal-solicite-juez-intervenir-correspondencia-764` |
| 765 | Grabaciones y transcripciones intervenidas: pedir que se incluya información | 2016 | `grabaciones-transcripciones-intervenidas-pedir-incluya-765` |
| 766 | Grabaciones y transcripciones intervenidas: retirar lo que afecte a la vida privada | 2016 | `grabaciones-transcripciones-intervenidas-retirar-lo-766` |
| 767 | Usar en otro proceso penal lo obtenido al intervenir correspondencia o comunicaciones | 2016 | `usar-otro-proceso-penal-lo-obtenido-intervenir-767` |
