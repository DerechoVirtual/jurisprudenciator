---
name: indice
description: "Índice de los 59 formularios de recursos administrativos (alzada, reposición, revisión extraordinaria, revisión de oficio, lesividad). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Recursos administrativos: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Ordenanzas municipales** (tráfico, urbanismo, tributos locales, convivencia) → `buscar_ordenanzas` → `leer_ordenanza`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/recursos-administrativos:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 708 | Reposición contra acto de la Administración Local | 2009 | `reposicion-contra-acto-administracion-local-708` |
| 1300 | Interposición del recurso de reposición | 2006 | `interposicion-recurso-reposicion-1300` |
| 1321 | Interposición del recurso extraordinario de revisión | 2004 | `interposicion-recurso-extraordinario-revision-1321` |

## Recursos e impugnaciones (17)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 74 | Reposición contra desestimación por silencio negativo | 2019 | `reposicion-contra-desestimacion-silencio-negativo-74` |
| 106 | Alzada impropia | 2018 | `alzada-impropia-106` |
| 111 | Reposición potestativa genérica | 2018 | `reposicion-potestativa-generica-111` |
| 122 | Reposición con petición de suspensión, prueba y trámite de audiencia | 2017 | `reposicion-peticion-suspension-prueba-tramite-audiencia-122` |
| 256 | Reposición contra nómina por descuento indebido de haberes | 2016 | `reposicion-contra-nomina-descuento-indebido-haberes-256` |
| 303 | Reposición contra desestimación presunta por silencio administrativo | 2014 | `reposicion-contra-desestimacion-presunta-silencio-303` |
| 367 | Reposición contra resolución notificada por el Tablón Edictal Único | 2013 | `reposicion-contra-resolucion-notificada-tablon-edictal-367` |
| 455 | Reposición contra denegación de admisión en un centro educativo | 2012 | `reposicion-contra-denegacion-admision-centro-educativo-455` |
| 458 | Reposición contra denegación de beca de estudios | 2012 | `reposicion-contra-denegacion-beca-estudios-458` |
| 545 | Reposición potestativa contra corrección de errores | 2011 | `reposicion-potestativa-contra-correccion-errores-545` |
| 548 | Reposición potestativa contra resolución desfavorable sin motivación | 2011 | `reposicion-potestativa-contra-resolucion-desfavorable-548` |
| 572 | Reposición por omitir la audiencia al revocar y caducar una licencia | 2011 | `reposicion-omitir-audiencia-revocar-caducar-licencia-572` |
| 1010 | Alzada contra resolución administrativa | 2008 | `alzada-contra-resolucion-administrativa-1010` |
| 1212 | Reposición contra resolución administrativa | 2008 | `reposicion-contra-resolucion-administrativa-1212` |
| 1295 | Alzada sobre órganos de selección de personal | 2008 | `alzada-sobre-organos-seleccion-personal-1295` |
| 1348 | Alzada o reposición contra la declaración de caducidad del expediente | 2004 | `alzada-reposicion-contra-declaracion-caducidad-1348` |
| 1360 | Alzada contra el acuerdo de medidas provisionales | 2004 | `alzada-contra-acuerdo-medidas-provisionales-1360` |

## Solicitudes y expedientes (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 41 | Revisión de oficio de actos nulos por la STC sobre el estado de alarma | 2021 | `revision-oficio-actos-nulos-stc-sobre-estado-alarma-41` |
| 123 | Revisión de oficio de un acto nulo a instancia del interesado | 2017 | `revision-oficio-acto-nulo-instancia-interesado-123` |
| 156 | Nulidad de acto que vulnera derechos susceptibles de amparo constitucional | 2017 | `nulidad-acto-vulnera-derechos-susceptibles-amparo-156` |
| 157 | Nulidad de acto dictado por órgano manifiestamente incompetente | 2017 | `nulidad-acto-dictado-organo-manifiestamente-incompetente-157` |
| 158 | Nulidad de acto dictado prescindiendo totalmente del procedimiento | 2017 | `nulidad-acto-dictado-prescindiendo-totalmente-158` |
| 160 | Nulidad de acto contrario al ordenamiento que concede derechos sin requisitos esenciales | 2017 | `nulidad-acto-contrario-ordenamiento-concede-derechos-sin-160` |
| 161 | Nulidad de acto por causa prevista en una norma con rango de ley | 2017 | `nulidad-acto-causa-prevista-norma-rango-ley-161` |
| 162 | Nulidad de acto de contenido imposible | 2017 | `nulidad-acto-contenido-imposible-162` |
| 571 | Pedir rectificar errores materiales, de hecho y aritméticos | 2011 | `pedir-rectificar-errores-materiales-hecho-aritmeticos-571` |
| 629 | Pedir revocar un acto o resolución administrativa | 2010 | `pedir-revocar-acto-resolucion-administrativa-629` |
| 1410 | Pedir la rectificación de errores materiales o aritméticos | 2004 | `pedir-rectificacion-errores-materiales-aritmeticos-1410` |
| 1415 | Pedir que se declare de oficio la nulidad de pleno derecho | 2004 | `pedir-declare-oficio-nulidad-pleno-derecho-1415` |

## Escritos de trámite (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 335 | Reposición potestativa por nulidad de resolución que vulnera el derecho a la prueba | 2013 | `reposicion-potestativa-nulidad-resolucion-vulnera-335` |
| 553 | Reposición en disciplinario por falta de tipicidad de los hechos probados | 2011 | `reposicion-disciplinario-falta-tipicidad-hechos-probados-553` |
| 1299 | Propuesta de resolución en la reposición | 2006 | `propuesta-resolucion-reposicion-1299` |

## Actos y resoluciones de la Administración o del órgano judicial (19)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 33 | Inadmitir el recurso de alzada contra resolución presunta | 2022 | `inadmitir-recurso-alzada-contra-resolucion-presunta-33` |
| 34 | Inadmitir el recurso de alzada contra resolución expresa | 2022 | `inadmitir-recurso-alzada-contra-resolucion-expresa-34` |
| 124 | Resolver el expediente de nulidad de un acto | 2017 | `resolver-expediente-nulidad-acto-124` |
| 128 | Inadmitir la solicitud de nulidad de disposiciones y actos | 2017 | `inadmitir-solicitud-nulidad-disposiciones-actos-128` |
| 192 | Resolución que inicia el expediente de declaración de lesividad | 2016 | `resolucion-inicia-expediente-declaracion-lesividad-192` |
| 1012 | Resolución del recurso de alzada o reposición | 2008 | `resolucion-recurso-alzada-reposicion-1012` |
| 1073 | Traslado de la alzada o reposición a los demás interesados | 2008 | `traslado-alzada-reposicion-demas-interesados-1073` |
| 1236 | Traslado del recurso de alzada o reposición al resto de interesados | 2008 | `traslado-recurso-alzada-reposicion-resto-interesados-1236` |
| 1296 | Informe sobre ampliar el plazo para resolver la reposición | 2006 | `informe-sobre-ampliar-plazo-resolver-reposicion-1296` |
| 1297 | Resolución que amplía el plazo máximo para resolver la reposición | 2006 | `resolucion-amplia-plazo-maximo-resolver-reposicion-1297` |
| 1298 | Notificación de la ampliación de plazo en la reposición | 2006 | `notificacion-ampliacion-plazo-reposicion-1298` |
| 1302 | Acuerdo de declaración de lesividad | 2006 | `acuerdo-declaracion-lesividad-1302` |
| 1322 | Resolución que declara la nulidad de pleno derecho de un acto administrativo | 2004 | `resolucion-declara-nulidad-pleno-derecho-acto-1322` |
| 1403 | Acuerdo de inadmisión del recurso extraordinario de revisión | 2004 | `acuerdo-inadmision-recurso-extraordinario-revision-1403` |
| 1411 | Acuerdo de rectificación de errores materiales, de hecho o aritméticos | 2004 | `acuerdo-rectificacion-errores-materiales-hecho-1411` |
| 1412 | Resolución de revocación de actos de gravamen o desfavorables | 2004 | `resolucion-revocacion-actos-gravamen-desfavorables-1412` |
| 1414 | Acuerdo de inadmisión de la revisión de oficio de actos nulos | 2004 | `acuerdo-inadmision-revision-oficio-actos-nulos-1414` |
| 1749 | Resolución de revocación de actos de gravamen | 2004 | `resolucion-revocacion-actos-gravamen-1749` |
| 1761 | Resolución que estima total o parcialmente la reposición | 2004 | `resolucion-estima-total-parcialmente-reposicion-1761` |

## Contratos, escrituras y documentos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1234 | Modelo de informe del órgano instructor sobre el recurso de alzada o reposición | 2008 | `modelo-informe-organo-instructor-sobre-recurso-alzada-1234` |

## Comunicaciones, requerimientos y reclamaciones (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1029 | Aviso de audiencia tras la instrucción del recurso administrativo | 2008 | `aviso-audiencia-tras-instruccion-recurso-administrativo-1029` |

## Otros (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 127 | Revisión de oficio de disposiciones y actos nulos por iniciativa de la Administración | 2017 | `revision-oficio-disposiciones-actos-nulos-iniciativa-127` |
| 602 | Declarar la lesividad de un acto administrativo anulable | 2010 | `declarar-lesividad-acto-administrativo-anulable-602` |
| 1759 | Audiencia a los interesados para resolver el recurso administrativo | 2004 | `audiencia-interesados-resolver-recurso-administrativo-1759` |
