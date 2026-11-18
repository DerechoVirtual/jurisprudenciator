---
name: indice
description: "Índice de los 87 formularios de sucesiones (testamentos, partición, legítimas, declaración de herederos, desheredación). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Sucesiones: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/sucesiones:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (30)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 31 | Demanda declarativa de prescripción de los derechos legitimarios | 2024 | `demanda-declarativa-prescripcion-derechos-legitimarios-31` |
| 41 | Demanda contra el cuaderno particional del contador-partidor dativo de notaría | 2024 | `demanda-contra-cuaderno-particional-contador-partidor-41` |
| 42 | Nulidad de la partición hereditaria: demanda | 2024 | `nulidad-particion-hereditaria-demanda-42` |
| 75 | Demanda de rendición de cuentas contra un coheredero | 2023 | `demanda-rendicion-cuentas-contra-coheredero-75` |
| 108 | Casación del art. 477.2 LEC por derechos fundamentales: intromisión en el honor | 2022 | `casacion-art-477-2-lec-derechos-fundamentales-108` |
| 129 | Demanda por intromisión en la intimidad personal y familiar (art. 18.1 CE) | 2022 | `demanda-intromision-intimidad-personal-familiar-art-18-1-129` |
| 181 | Impugnación de testamento por desheredación (Cataluña) | 2021 | `impugnacion-testamento-desheredacion-cataluna-181` |
| 186 | Demanda de ejecución de sentencia contra herencia yacente | 2021 | `demanda-ejecucion-sentencia-contra-herencia-yacente-186` |
| 205 | Acción rescisoria de herencia por lesión de más de una cuarta parte | 2020 | `accion-rescisoria-herencia-lesion-mas-cuarta-parte-205` |
| 212 | Impugnación de testamento por preterición | 2020 | `impugnacion-testamento-pretericion-212` |
| 213 | Impugnación de testamento por desheredación (acción general) | 2020 | `impugnacion-testamento-desheredacion-accion-general-213` |
| 325 | Demanda ordinaria de reducción de legado | 2020 | `demanda-ordinaria-reduccion-legado-325` |
| 330 | Demanda de declaración de indignidad del heredero | 2020 | `demanda-declaracion-indignidad-heredero-330` |
| 343 | Demanda de petición de herencia | 2019 | `demanda-peticion-herencia-343` |
| 345 | Demanda de reclamación de legítima (Galicia) | 2019 | `demanda-reclamacion-legitima-galicia-345` |
| 352 | Demanda verbal de complemento de legítima | 2019 | `demanda-verbal-complemento-legitima-352` |
| 356 | Demanda de un coheredero en beneficio de la comunidad hereditaria | 2019 | `demanda-coheredero-beneficio-comunidad-hereditaria-356` |
| 376 | Demanda ordinaria de complemento de legítima | 2019 | `demanda-ordinaria-complemento-legitima-376` |
| 416 | Demanda de cantidad por venta de acciones sin el consentimiento de todos los coherederos | 2018 | `demanda-cantidad-venta-acciones-sin-consentimiento-todos-416` |
| 431 | Demanda ordinaria de reducción de legado por inoficioso | 2018 | `demanda-ordinaria-reduccion-legado-inoficioso-431` |
| 446 | Casación del art. 477.2 LEC por derechos fundamentales: intromisión en la intimidad | 2018 | `casacion-art-477-2-lec-derechos-fundamentales-446` |
| 454 | Demanda verbal de cantidad contra herencia yacente | 2018 | `demanda-verbal-cantidad-contra-herencia-yacente-454` |
| 464 | Demanda por intromisión en el honor por injurias leves | 2017 | `demanda-intromision-honor-injurias-leves-464` |
| 504 | Demanda por inclusión indebida en registro de morosos (honor) | 2017 | `demanda-inclusion-indebida-registro-morosos-honor-504` |
| 508 | Desahucio por precario entre coherederos: demanda | 2017 | `desahucio-precario-entre-coherederos-demanda-508` |
| 572 | Demanda de ejecución hipotecaria contra herencia yacente | 2016 | `demanda-ejecucion-hipotecaria-contra-herencia-yacente-572` |
| 1183 | Demanda de reclamación de legítima (Derecho civil de Cataluña) | 2014 | `demanda-reclamacion-legitima-derecho-civil-cataluna-1183` |
| 1466 | Ejecución de tasación de costas contra la herencia yacente | 2014 | `ejecucion-tasacion-costas-contra-herencia-yacente-1466` |
| 1468 | Demanda de cantidad contra herencia yacente | 2014 | `demanda-cantidad-contra-herencia-yacente-1468` |
| 1498 | Demanda de remoción del albacea testamentario | 2014 | `demanda-remocion-albacea-testamentario-1498` |

## Contestaciones, oposiciones y alegaciones (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 17 | Contestación a la demanda de nulidad de testamento (juicio ordinario) | 2024 | `contestacion-demanda-nulidad-testamento-juicio-ordinario-17` |
| 18 | Contestación a la demanda de adición a la partición hereditaria | 2024 | `contestacion-demanda-adicion-particion-hereditaria-18` |
| 263 | Oposición a la división judicial de la herencia e intervención del caudal | 2020 | `oposicion-division-judicial-herencia-e-intervencion-263` |
| 328 | Contestación a la demanda de indignidad del heredero | 2020 | `contestacion-demanda-indignidad-heredero-328` |
| 329 | Contestación a la demanda de indignidad con rehabilitación tácita o expresa del causante | 2020 | `contestacion-demanda-indignidad-rehabilitacion-tacita-329` |
| 351 | Contestación a demanda de complemento de legítima con reconvención de nulidad de la partición | 2019 | `contestacion-demanda-complemento-legitima-reconvencion-351` |
| 428 | Contestación oponiendo falta de legitimación pasiva | 2018 | `contestacion-oponiendo-falta-legitimacion-pasiva-428` |

## Solicitudes y expedientes (19)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 46 | Pedir al contador-partidor un nuevo cuaderno particional adaptado a la sentencia de apelación | 2023 | `pedir-contador-partidor-nuevo-cuaderno-particional-46` |
| 111 | Requerimiento para aceptar o repudiar la herencia (Aragón) | 2022 | `requerimiento-aceptar-repudiar-herencia-aragon-111` |
| 262 | Cese de la intervención judicial de la herencia | 2020 | `cese-intervencion-judicial-herencia-262` |
| 264 | Intervención judicial de la herencia | 2020 | `intervencion-judicial-herencia-264` |
| 316 | Administrador judicial de herencia abintestato sin declaración de herederos | 2020 | `administrador-judicial-herencia-abintestato-sin-316` |
| 631 | Renuncia de un albacea ante notario | 2015 | `renuncia-albacea-ante-notario-631` |
| 662 | Requerimiento notarial para presentar un testamento cerrado | 2015 | `requerimiento-notarial-presentar-testamento-cerrado-662` |
| 671 | Adveración, apertura y protocolización de testamento oral | 2015 | `adveracion-apertura-protocolizacion-testamento-oral-671` |
| 723 | Renuncia del contador-partidor o prórroga de su plazo | 2015 | `renuncia-contador-partidor-prorroga-plazo-723` |
| 724 | Renuncia del albacea o prórroga del albaceazgo | 2015 | `renuncia-albacea-prorroga-albaceazgo-724` |
| 726 | Remoción del albacea | 2015 | `remocion-albacea-726` |
| 727 | Autorización al albacea para disponer de bienes de la herencia | 2015 | `autorizacion-albacea-disponer-bienes-herencia-727` |
| 728 | Rendición de cuentas del albacea | 2015 | `rendicion-cuentas-albacea-728` |
| 730 | Aprobación de la partición del contador-partidor no confirmada por todos los herederos y legatarios | 2015 | `aprobacion-particion-contador-partidor-no-confirmada-730` |
| 732 | Designación de contador-partidor dativo (art. 1057 CC) | 2015 | `designacion-contador-partidor-dativo-art-1057-cc-732` |
| 736 | Aprobación judicial de la repudiación de herencia por asociaciones, corporaciones y fundaciones | 2015 | `aprobacion-judicial-repudiacion-herencia-asociaciones-736` |
| 860 | Intervención judicial de la herencia tras la declaración de herederos | 2013 | `intervencion-judicial-herencia-tras-declaracion-860` |
| 1041 | Exhibición de acto de última voluntad: petición | 2013 | `exhibicion-acto-ultima-voluntad-peticion-1041` |
| 1145 | Sobreseimiento por acuerdo de los herederos | 2013 | `sobreseimiento-acuerdo-herederos-1145` |

## Escritos de trámite (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 278 | Sucesión del fiador en la posición procesal del ejecutante | 2020 | `sucesion-fiador-posicion-procesal-ejecutante-278` |
| 735 | Autorización al acreedor para aceptar la herencia | 2015 | `autorizacion-acreedor-aceptar-herencia-735` |
| 1467 | Jura de cuentas del procurador contra la herencia yacente | 2014 | `jura-cuentas-procurador-contra-herencia-yacente-1467` |

## Actos y resoluciones de la Administración o del órgano judicial (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 540 | Acta de sorteo del contador-partidor por acuerdo mayoritario (Galicia) | 2016 | `acta-sorteo-contador-partidor-acuerdo-mayoritario-540` |
| 541 | Acta de requerimiento para designar contador-partidor por acuerdo mayoritario (Galicia) | 2016 | `acta-requerimiento-designar-contador-partidor-acuerdo-541` |

## Contratos, escrituras y documentos (18)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 214 | Designación del delegado de protección de datos en el sector público | 2020 | `designacion-delegado-proteccion-datos-sector-publico-214` |
| 215 | Designación del delegado de protección de datos en el sector privado | 2020 | `designacion-delegado-proteccion-datos-sector-privado-215` |
| 303 | Testamento en caso de epidemia | 2020 | `testamento-caso-epidemia-303` |
| 539 | Partija de los coherederos en documento privado (Galicia) | 2016 | `partija-coherederos-documento-privado-galicia-539` |
| 542 | Partija por acuerdo mayoritario protocolizada en escritura (Galicia) | 2016 | `partija-acuerdo-mayoritario-protocolizada-escritura-542` |
| 545 | Otorgamiento de testamento mancomunado correspectivo (Galicia) | 2016 | `otorgamiento-testamento-mancomunado-correspectivo-545` |
| 549 | Partija conjunta extratestamentaria en documento privado | 2016 | `partija-conjunta-extratestamentaria-documento-privado-549` |
| 565 | Partija conjunta extratestamentaria para protocolizar (Galicia) | 2016 | `partija-conjunta-extratestamentaria-protocolizar-galicia-565` |
| 567 | Partija del contador-partidor en documento privado (Galicia) | 2016 | `partija-contador-partidor-documento-privado-galicia-567` |
| 568 | Partija del testador en documento privado extratestamentario (Galicia) | 2016 | `partija-testador-documento-privado-extratestamentario-568` |
| 569 | Escritura de pacto de mejora sin entrega de presente (Galicia) | 2016 | `escritura-pacto-mejora-sin-entrega-presente-galicia-569` |
| 570 | Escritura de pacto de mejora con entrega de presente (Galicia) | 2016 | `escritura-pacto-mejora-entrega-presente-galicia-570` |
| 571 | Escritura de pacto de apartación (Galicia) | 2016 | `escritura-pacto-apartacion-galicia-571` |
| 579 | Otorgamiento de testamento mancomunado cerrado (Aragón) | 2016 | `otorgamiento-testamento-mancomunado-cerrado-aragon-579` |
| 586 | Otorgamiento de testamento ológrafo mancomunado (Aragón) | 2016 | `otorgamiento-testamento-olografo-mancomunado-aragon-586` |
| 1185 | Testamento con desheredación | 2014 | `testamento-desheredacion-1185` |
| 1445 | Testamento con cláusula de cautela socini | 2014 | `testamento-clausula-cautela-socini-1445` |
| 1450 | Contrato de servicios entre sociedad y consejero delegado | 2014 | `contrato-servicios-entre-sociedad-consejero-delegado-1450` |

## Comunicaciones, requerimientos y reclamaciones (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 462 | Honorarios de abogado contra herencia yacente: reclamación | 2017 | `honorarios-abogado-contra-herencia-yacente-reclamacion-462` |
| 1147 | Requerir al contador-partidor | 2013 | `requerir-contador-partidor-1147` |

## Otros (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 210 | Ineficacia sobrevenida del testamento por premoriencia de los herederos | 2020 | `ineficacia-sobrevenida-testamento-premoriencia-herederos-210` |
| 543 | Revocar conjuntamente el testamento mancomunado correspectivo (Galicia) | 2016 | `revocar-conjuntamente-testamento-mancomunado-543` |
| 544 | Revocar unilateralmente el testamento mancomunado correspectivo (Galicia) | 2016 | `revocar-unilateralmente-testamento-mancomunado-544` |
| 566 | Protocolización de partija conjunta y testamento paralelo (Galicia) | 2016 | `protocolizacion-partija-conjunta-testamento-paralelo-566` |
| 580 | Revocar unilateralmente testamento mancomunado (País Vasco) | 2016 | `revocar-unilateralmente-testamento-mancomunado-pais-580` |
| 581 | Revocar conjuntamente testamento mancomunado (País Vasco) | 2016 | `revocar-conjuntamente-testamento-mancomunado-pais-vasco-581` |
