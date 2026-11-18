---
name: indice
description: "Índice de los 187 formularios de arrendamientos y desahucio (LAU, RDL 29/2026, renta, fianza, prórrogas, desahucio, vulnerabilidad). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Arrendamientos y desahucio: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/arrendamientos:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (42)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 27 | Desahucio por precario del gran tenedor (adaptada a la Ley 12/2023) | 2024 | `desahucio-precario-gran-tenedor-adaptada-ley-12-2023-27` |
| 28 | Desahucio y rentas del gran tenedor sin enervación (adaptada a la Ley 12/2023) | 2024 | `desahucio-rentas-gran-tenedor-sin-enervacion-adaptada-28` |
| 29 | Desahucio por expiración del plazo del gran tenedor (adaptada a la Ley 12/2023) | 2024 | `desahucio-expiracion-plazo-gran-tenedor-adaptada-ley-12-29` |
| 61 | Desahucio por impago y rentas del gran tenedor, con enervación (finca urbana) | 2023 | `desahucio-impago-rentas-gran-tenedor-enervacion-finca-61` |
| 79 | Desahucio por precario contra un copropietario: demanda | 2023 | `desahucio-precario-contra-copropietario-demanda-79` |
| 88 | Demanda del arrendatario para resolver el arrendamiento por incumplimiento del arrendador | 2023 | `demanda-arrendatario-resolver-arrendamiento-88` |
| 94 | Demanda por daños en la vivienda tras finalizar el arrendamiento | 2022 | `demanda-danos-vivienda-tras-finalizar-arrendamiento-94` |
| 156 | Demanda para declarar subsistente el arrendamiento de uso distinto del de vivienda | 2021 | `demanda-declarar-subsistente-arrendamiento-uso-distinto-156` |
| 182 | Desahucio por expiración del plazo y reclamación de rentas impagadas (juicio verbal) | 2021 | `desahucio-expiracion-plazo-reclamacion-rentas-impagadas-182` |
| 219 | Demanda por pérdida de la cosa arrendada en arrendamiento sujeto al Código Civil | 2020 | `demanda-perdida-cosa-arrendada-arrendamiento-sujeto-219` |
| 242 | Resolución de arrendamiento de vivienda por falta de reparaciones, con daños (posterior a 1995) | 2020 | `resolucion-arrendamiento-vivienda-falta-reparaciones-242` |
| 253 | Demanda ordinaria de cantidad por arrendamiento de servicios | 2020 | `demanda-ordinaria-cantidad-arrendamiento-servicios-253` |
| 254 | Demanda verbal de cantidad por arrendamiento de servicios | 2020 | `demanda-verbal-cantidad-arrendamiento-servicios-254` |
| 320 | Desahucio por expiración del plazo en aparcería sujeta a la LAR 49/2003 | 2020 | `desahucio-expiracion-plazo-aparceria-sujeta-lar-49-2003-320` |
| 323 | Impugnar la transmisión de la vivienda arrendada: demanda | 2020 | `impugnar-transmision-vivienda-arrendada-demanda-323` |
| 327 | Demanda de extinción de arrendamiento rústico por circunstancia sobrevenida | 2020 | `demanda-extincion-arrendamiento-rustico-circunstancia-327` |
| 336 | Desahucio por expiración del arrendamiento rústico histórico (LARH 1/1992) | 2019 | `desahucio-expiracion-arrendamiento-rustico-historico-336` |
| 353 | Demanda de devolución de la fianza arrendaticia con prueba digital | 2019 | `demanda-devolucion-fianza-arrendaticia-prueba-digital-353` |
| 380 | Desahucio por expiración del plazo y cantidad por enriquecimiento injusto (juicio verbal) | 2019 | `desahucio-expiracion-plazo-cantidad-enriquecimiento-380` |
| 402 | Demanda de resolución del arrendamiento por no ser residencia habitual (posterior a 1995) | 2019 | `demanda-resolucion-arrendamiento-no-ser-residencia-402` |
| 409 | Demanda ordinaria de resolución de arrendamiento de local de negocio por incumplimiento | 2018 | `demanda-ordinaria-resolucion-arrendamiento-local-negocio-409` |
| 410 | Demanda verbal de precario por jubilación del portero | 2018 | `demanda-verbal-precario-jubilacion-portero-410` |
| 430 | Desahucio por expiración del término en alquiler de plaza de garaje | 2018 | `desahucio-expiracion-termino-alquiler-plaza-garaje-430` |
| 475 | Desahucio de alquiler de temporada por expiración del término | 2017 | `desahucio-alquiler-temporada-expiracion-termino-475` |
| 500 | Desahucio por expiración del plazo e indemnización de daños (juicio verbal) | 2017 | `desahucio-expiracion-plazo-e-indemnizacion-danos-juicio-500` |
| 554 | Demanda de desahucio por impago del trastero | 2016 | `demanda-desahucio-impago-trastero-554` |
| 829 | Demanda de retracto en arrendamiento rústico | 2015 | `demanda-retracto-arrendamiento-rustico-829` |
| 1151 | Demanda por incumplir prestaciones del arrendamiento de obra | 2013 | `demanda-incumplir-prestaciones-arrendamiento-obra-1151` |
| 1187 | Demanda verbal de desahucio por impago y reclamación de cantidades de plaza de garaje | 2014 | `demanda-verbal-desahucio-impago-reclamacion-cantidades-1187` |
| 1238 | Cesación de actividad e indemnización por perjuicios en vivienda arrendada | 2013 | `cesacion-actividad-e-indemnizacion-perjuicios-vivienda-1238` |
| 1239 | Demanda de rentas debidas acumulada contra fiador o avalista | 2013 | `demanda-rentas-debidas-acumulada-contra-fiador-avalista-1239` |
| 1244 | Demanda de rentas o cantidades debidas | 2013 | `demanda-rentas-cantidades-debidas-1244` |
| 1248 | Desahucio por expiración del plazo en arrendamiento para uso distinto de vivienda | 2013 | `desahucio-expiracion-plazo-arrendamiento-uso-distinto-1248` |
| 1256 | Demanda de desahucio y rentas atrasadas en arrendamiento para uso distinto de vivienda | 2013 | `demanda-desahucio-rentas-atrasadas-arrendamiento-uso-1256` |
| 1279 | Desahucio y rentas contra arrendatario y fiador (uso distinto de vivienda) | 2013 | `desahucio-rentas-contra-arrendatario-fiador-uso-distinto-1279` |
| 1288 | Demanda de desahucio por impago en arrendamiento para uso distinto de vivienda | 2013 | `demanda-desahucio-impago-arrendamiento-uso-distinto-1288` |
| 1318 | Demanda de indemnización por desistimiento del arrendatario | 2013 | `demanda-indemnizacion-desistimiento-arrendatario-1318` |
| 1319 | Demanda de determinación de la renta | 2013 | `demanda-determinacion-renta-1319` |
| 1459 | Demanda verbal de precario de finca rústica | 2014 | `demanda-verbal-precario-finca-rustica-1459` |
| 1460 | Demanda ordinaria por incumplimiento de contrato de renta vitalicia | 2014 | `demanda-ordinaria-incumplimiento-contrato-renta-1460` |
| 1495 | Demanda de resolución de arrendamiento de local con daños y consignación de rentas (LAU 94) | 2014 | `demanda-resolucion-arrendamiento-local-danos-1495` |
| 1499 | Demanda para exigir obras al arrendador (LAU 94) | 2014 | `demanda-exigir-obras-arrendador-lau-94-1499` |

## Contestaciones, oposiciones y alegaciones (23)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 23 | Alegaciones del arrendador gran tenedor en el incidente de suspensión del arrendatario | 2024 | `alegaciones-arrendador-gran-tenedor-incidente-suspension-23` |
| 73 | Contestación a la demanda de desahucio por precario | 2023 | `contestacion-demanda-desahucio-precario-73` |
| 93 | Contestación a la demanda por daños en la vivienda arrendada tras el arrendamiento | 2022 | `contestacion-demanda-danos-vivienda-arrendada-tras-93` |
| 282 | Contestación del arrendador a la moratoria excepcional del art. 8 RD 15/2020 | 2020 | `contestacion-arrendador-moratoria-excepcional-art-8-rd-282` |
| 298 | Contestación del arrendador a la moratoria excepcional del art. 8 RDL 11/2020 | 2020 | `contestacion-arrendador-moratoria-excepcional-art-8-rdl-298` |
| 300 | Contestación al desahucio por fin de plazo con prórroga extraordinaria (art. 2 RDL 11/2020) | 2020 | `contestacion-desahucio-fin-plazo-prorroga-extraordinaria-300` |
| 309 | Contestación a la demanda ordinaria de cantidad por arrendamiento de obra | 2020 | `contestacion-demanda-ordinaria-cantidad-arrendamiento-309` |
| 406 | Contestación al desahucio por extinción del plazo contractual | 2019 | `contestacion-desahucio-extincion-plazo-contractual-406` |
| 459 | Contestación al desahucio por fin de plazo en arrendamiento de uso distinto de vivienda | 2017 | `contestacion-desahucio-fin-plazo-arrendamiento-uso-459` |
| 522 | Contestación a la demanda de precario alegando comodato | 2016 | `contestacion-demanda-precario-alegando-comodato-522` |
| 810 | Contestación al requerimiento del arrendador: extinción por fallecimiento del arrendatario | 2015 | `contestacion-requerimiento-arrendador-extincion-810` |
| 813 | Contestación del arrendatario al requerimiento de extinción por jubilación | 2015 | `contestacion-arrendatario-requerimiento-extincion-813` |
| 814 | Oposición del arrendatario persona física a la extinción por los veinte años | 2015 | `oposicion-arrendatario-persona-fisica-extincion-veinte-814` |
| 1252 | Oposición del arrendatario a la repercusión del coste de obras | 2013 | `oposicion-arrendatario-repercusion-coste-obras-1252` |
| 1255 | Contestación a demanda de reclamación de rentas | 2013 | `contestacion-demanda-reclamacion-rentas-1255` |
| 1262 | Contestar oralmente en el desahucio por impago de rentas | 2013 | `contestar-oralmente-desahucio-impago-rentas-1262` |
| 1290 | Contestación al requerimiento de extinción de local de persona física anterior a 1985 | 2013 | `contestacion-requerimiento-extincion-local-persona-1290` |
| 1291 | Oposición del arrendatario de local a la actualización de la renta | 2013 | `oposicion-arrendatario-local-actualizacion-renta-1291` |
| 1296 | Oposición del arrendatario de vivienda a la actualización de renta por error de cálculo | 2013 | `oposicion-arrendatario-vivienda-actualizacion-renta-1296` |
| 1298 | Oposición del arrendatario de vivienda a la actualización de renta sin causa | 2013 | `oposicion-arrendatario-vivienda-actualizacion-renta-sin-1298` |
| 1299 | Oposición del arrendatario de vivienda a la actualización de renta por ingresos insuficientes | 2013 | `oposicion-arrendatario-vivienda-actualizacion-renta-1299` |
| 1315 | Oposición del arrendador a la reparación del inmueble | 2013 | `oposicion-arrendador-reparacion-inmueble-1315` |
| 1328 | Contestar a la demanda de desahucio por precario | 2013 | `contestar-demanda-desahucio-precario-1328` |

## Solicitudes y expedientes (16)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 60 | Solicitud de prórroga extraordinaria del arrendamiento (Ley 12/2023) | 2023 | `solicitud-prorroga-extraordinaria-arrendamiento-ley-12-60` |
| 192 | Moratoria automática de renta en uso distinto de vivienda (arts. 1 y 2 RDL 35/2020) | 2021 | `moratoria-automatica-renta-uso-distinto-vivienda-arts-1-192` |
| 196 | Suspensión del desahucio de vulnerables sin alternativa habitacional (art. 1 RDL 11/2020) | 2021 | `suspension-desahucio-vulnerables-sin-alternativa-196` |
| 283 | Moratoria automática de renta (art. 4 RDL 11/2020, COVID-19) | 2020 | `moratoria-automatica-renta-art-4-rdl-11-2020-covid-19-283` |
| 284 | Moratoria excepcional de renta (art. 8 RDL 11/2020, COVID-19) | 2020 | `moratoria-excepcional-renta-art-8-rdl-11-2020-covid-19-284` |
| 304 | Solicitud del arrendatario de prórroga extraordinaria de vivienda habitual (art. 2 RDL 11/2020) | 2020 | `solicitud-arrendatario-prorroga-extraordinaria-vivienda-304` |
| 817 | Reclamar indemnización al arrendatario por desistimiento tácito pasados seis meses | 2015 | `reclamar-indemnizacion-arrendatario-desistimiento-tacito-817` |
| 818 | Reclamar indemnización al arrendatario tras su aviso de desistimiento pasados seis meses | 2015 | `reclamar-indemnizacion-arrendatario-tras-aviso-818` |
| 819 | Reposición del arrendatario en la vivienda por no haberla ocupado el arrendador | 2015 | `reposicion-arrendatario-vivienda-no-haberla-ocupado-819` |
| 821 | Reclamar indemnización al arrendatario cuando el arrendador no ocupó la vivienda por necesidad | 2015 | `reclamar-indemnizacion-arrendatario-cuando-arrendador-no-821` |
| 1154 | Mediación solicitada por una parte en controversias de arrendamiento | 2013 | `mediacion-solicitada-parte-controversias-arrendamiento-1154` |
| 1208 | Traspaso de la consignación del Servicio Común de Registro y Reparto al tribunal de la impugnación | 2013 | `traspaso-consignacion-servicio-comun-registro-reparto-1208` |
| 1249 | Solicitud conjunta de varios arrendatarios para hacer obras | 2013 | `solicitud-conjunta-varios-arrendatarios-hacer-obras-1249` |
| 1267 | Solicitud de consentimiento para ceder el arrendamiento de vivienda | 2013 | `solicitud-consentimiento-ceder-arrendamiento-vivienda-1267` |
| 1306 | Solicitud del inquilino al presidente para frenar actividades molestas o prohibidas de un vecino | 2013 | `solicitud-inquilino-presidente-frenar-actividades-1306` |
| 1361 | Obras necesarias solicitadas por el arrendatario | 2013 | `obras-necesarias-solicitadas-arrendatario-1361` |

## Escritos de trámite (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1218 | Desistir el arrendatario en contratos prorrogados | 2013 | `desistir-arrendatario-contratos-prorrogados-1218` |
| 1266 | Propuesta de prueba en juicio verbal de desahucio por impago | 2013 | `propuesta-prueba-juicio-verbal-desahucio-impago-1266` |
| 1269 | Propuesta de prueba en juicio de reclamación de rentas | 2013 | `propuesta-prueba-juicio-reclamacion-rentas-1269` |
| 1360 | Prueba en el juicio de precario | 2013 | `prueba-juicio-precario-1360` |

## Actos y resoluciones de la Administración o del órgano judicial (14)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 281 | Acuerdo de moratoria y pago de renta con cargo a la fianza en local de negocio | 2020 | `acuerdo-moratoria-pago-renta-cargo-fianza-local-negocio-281` |
| 302 | Desistimiento del arrendatario en arrendamiento de uso distinto del de vivienda | 2020 | `desistimiento-arrendatario-arrendamiento-uso-distinto-302` |
| 804 | Acuerdo de extinción del arrendamiento con arrendatario persona jurídica | 2015 | `acuerdo-extincion-arrendamiento-arrendatario-persona-804` |
| 820 | Acuerdo de desalojo de la vivienda por necesidad del arrendador | 2015 | `acuerdo-desalojo-vivienda-necesidad-arrendador-820` |
| 831 | Resolución por mutuo acuerdo del arrendamiento rústico | 2015 | `resolucion-mutuo-acuerdo-arrendamiento-rustico-831` |
| 1200 | Notificación del arrendatario: ejercicio del derecho de tanteo | 2013 | `notificacion-arrendatario-ejercicio-derecho-tanteo-1200` |
| 1236 | Aviso del arrendador de venta de la vivienda: derecho de tanteo | 2013 | `aviso-arrendador-venta-vivienda-derecho-tanteo-1236` |
| 1250 | Aviso al arrendatario: vivienda necesaria para el arrendador o un familiar | 2013 | `aviso-arrendatario-vivienda-necesaria-arrendador-1250` |
| 1282 | Aviso al arrendador del subarriendo para uso distinto de vivienda | 2013 | `aviso-arrendador-subarriendo-uso-distinto-vivienda-1282` |
| 1287 | Aviso del arrendador: causa de exoneración de ingresos a cuenta | 2013 | `aviso-arrendador-causa-exoneracion-ingresos-cuenta-1287` |
| 1308 | Aviso del arrendador de venta de la vivienda: derecho de retracto | 2013 | `aviso-arrendador-venta-vivienda-derecho-retracto-1308` |
| 1317 | Comprador notifica al arrendatario las condiciones de la compraventa | 2013 | `comprador-notifica-arrendatario-condiciones-compraventa-1317` |
| 1324 | Notificación del arrendatario: ejercicio del derecho de retracto | 2013 | `notificacion-arrendatario-ejercicio-derecho-retracto-1324` |
| 1325 | Notificación del arrendador de venta del inmueble para el tanteo del arrendatario | 2013 | `notificacion-arrendador-venta-inmueble-tanteo-1325` |

## Contratos, escrituras y documentos (28)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 62 | Cláusula de no vulnerabilidad económica del arrendatario | 2023 | `clausula-no-vulnerabilidad-economica-arrendatario-62` |
| 140 | Arrendamiento de servicios de administración de fincas en propiedad vertical | 2021 | `arrendamiento-servicios-administracion-fincas-propiedad-140` |
| 200 | Arrendamiento de derechos de caza | 2020 | `arrendamiento-derechos-caza-200` |
| 255 | Contrato tipo de arrendamiento de vivienda vacacional | 2020 | `contrato-tipo-arrendamiento-vivienda-vacacional-255` |
| 266 | Arrendamiento de un edificio completo | 2020 | `arrendamiento-edificio-completo-266` |
| 344 | Arrendamiento de trastero: contrato | 2019 | `arrendamiento-trastero-contrato-344` |
| 489 | Subarriendo de vivienda o local de negocio | 2017 | `subarriendo-vivienda-local-negocio-489` |
| 535 | Arrendamiento rústico de lugar acasarado | 2016 | `arrendamiento-rustico-lugar-acasarado-535` |
| 578 | Arrendamiento de cuarto trastero (Navarra) | 2016 | `arrendamiento-cuarto-trastero-navarra-578` |
| 808 | Resolución del contrato con entrega de llaves y posesión del local al arrendador | 2015 | `resolucion-contrato-entrega-llaves-posesion-local-808` |
| 1167 | Arrendamiento de solar para actividad industrial | 2015 | `arrendamiento-solar-actividad-industrial-1167` |
| 1168 | Contrato de servicios de administración de comunidad de propietarios | 2015 | `contrato-servicios-administracion-comunidad-propietarios-1168` |
| 1170 | Aval de las obligaciones de un arrendamiento | 2015 | `aval-obligaciones-arrendamiento-1170` |
| 1180 | Arrendamiento civil de bienes muebles | 2015 | `arrendamiento-civil-bienes-muebles-1180` |
| 1210 | Arrendamiento de vivienda por comunidad de propietarios | 2013 | `arrendamiento-vivienda-comunidad-propietarios-1210` |
| 1213 | Arrendamiento para uso distinto de vivienda por comunidad de propietarios | 2013 | `arrendamiento-uso-distinto-vivienda-comunidad-1213` |
| 1217 | Arrendamiento para uso distinto de vivienda con garantías | 2013 | `arrendamiento-uso-distinto-vivienda-garantias-1217` |
| 1226 | Arrendamiento de vivienda a un familiar | 2013 | `arrendamiento-vivienda-familiar-1226` |
| 1228 | Alquiler de vivienda: contrato tipo | 2013 | `alquiler-vivienda-contrato-tipo-1228` |
| 1231 | Arrendamiento de vivienda de promoción pública | 2013 | `arrendamiento-vivienda-promocion-publica-1231` |
| 1257 | Opción de compra de vivienda arrendada: cláusula | 2013 | `opcion-compra-vivienda-arrendada-clausula-1257` |
| 1264 | Pacto de cesión del arrendamiento de vivienda | 2013 | `pacto-cesion-arrendamiento-vivienda-1264` |
| 1281 | Recibo de arrendamiento de vivienda | 2013 | `recibo-arrendamiento-vivienda-1281` |
| 1284 | Subarriendo total de inmueble (uso distinto de vivienda) | 2013 | `subarriendo-total-inmueble-uso-distinto-vivienda-1284` |
| 1285 | Pacto de subarriendo parcial de vivienda | 2013 | `pacto-subarriendo-parcial-vivienda-1285` |
| 1286 | Subarriendo parcial de inmueble (uso distinto de vivienda) | 2013 | `subarriendo-parcial-inmueble-uso-distinto-vivienda-1286` |
| 1307 | Recibo de arrendamiento para uso distinto de vivienda | 2013 | `recibo-arrendamiento-uso-distinto-vivienda-1307` |
| 1447 | Arrendamiento de vivienda adaptado a la Ley 12/2023 por el derecho a la vivienda | 2014 | `arrendamiento-vivienda-adaptado-ley-12-2023-derecho-1447` |

## Comunicaciones, requerimientos y reclamaciones (37)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 259 | Requerimiento al fiador o avalista del arrendamiento por incumplimiento del arrendatario | 2020 | `requerimiento-fiador-avalista-arrendamiento-259` |
| 553 | Entrega de llaves con desacuerdo en arrendamiento de uso distinto de vivienda | 2016 | `entrega-llaves-desacuerdo-arrendamiento-uso-distinto-553` |
| 803 | Aviso del arrendador a persona jurídica: extinción a los veinte años (actividad no comercial) | 2015 | `aviso-arrendador-persona-juridica-extincion-veinte-anos-803` |
| 805 | Extinción de arrendamiento de local posterior al 9-5-1985 con prórroga forzosa | 2015 | `extincion-arrendamiento-local-posterior-9-5-1985-805` |
| 806 | Aviso del arrendador a persona jurídica: extinción a los veinte años (actividad comercial) | 2015 | `aviso-arrendador-persona-juridica-extincion-veinte-anos-806` |
| 807 | Aviso del arrendatario persona física: extinción por jubilación | 2015 | `aviso-arrendatario-persona-fisica-extincion-jubilacion-807` |
| 809 | Aviso al arrendatario: extinción del arrendamiento por traspaso del local de negocio | 2015 | `aviso-arrendatario-extincion-arrendamiento-traspaso-809` |
| 811 | Comunicación de extinción del arrendamiento por fallecimiento del arrendatario persona física | 2015 | `comunicacion-extincion-arrendamiento-fallecimiento-811` |
| 812 | Requerimiento de extinción de arrendamiento de local (1985 a LAU 1994) acogido a tácita reconducción | 2015 | `requerimiento-extincion-arrendamiento-local-1985-lau-812` |
| 815 | Aviso del arrendador: extinción por fallecimiento del arrendatario persona física | 2015 | `aviso-arrendador-extincion-fallecimiento-arrendatario-815` |
| 816 | Aviso del arrendador: extinción por jubilación del arrendatario persona física | 2015 | `aviso-arrendador-extincion-jubilacion-arrendatario-816` |
| 824 | Entrega del certificado de eficiencia energética al futuro arrendatario | 2015 | `entrega-certificado-eficiencia-energetica-futuro-824` |
| 1171 | Requerimiento al inquilino sobre causas de posposición frente a la denegación de prórroga | 2015 | `requerimiento-inquilino-sobre-causas-posposicion-frente-1171` |
| 1201 | Requerimiento para formalizar el contrato de arrendamiento | 2013 | `requerimiento-formalizar-contrato-arrendamiento-1201` |
| 1203 | Comunicación del arrendatario de resolución administrativa que obliga a hacer obras | 2013 | `comunicacion-arrendatario-resolucion-administrativa-1203` |
| 1222 | Aviso del arrendatario de su nueva dirección | 2013 | `aviso-arrendatario-nueva-direccion-1222` |
| 1233 | Aviso al arrendador: instalación de punto de recarga eléctrica en garaje | 2013 | `aviso-arrendador-instalacion-punto-recarga-electrica-1233` |
| 1277 | Nueva dirección del arrendatario de local de negocio | 2013 | `nueva-direccion-arrendatario-local-negocio-1277` |
| 1278 | Requerimiento previo al fiador o avalista de arrendamiento de local | 2013 | `requerimiento-previo-fiador-avalista-arrendamiento-local-1278` |
| 1292 | Extinción por fallecimiento de arrendamiento de local de persona física anterior al 9-5-1985 | 2013 | `extincion-fallecimiento-arrendamiento-local-persona-1292` |
| 1293 | Extinción de arrendamientos de vivienda anteriores al 9-5-1985 | 2013 | `extincion-arrendamientos-vivienda-anteriores-9-5-1985-1293` |
| 1294 | Extinción por jubilación de arrendamiento de local de persona física anterior al 9-5-1985 | 2013 | `extincion-jubilacion-arrendamiento-local-persona-fisica-1294` |
| 1295 | Actualización de renta en arrendamientos de local anteriores al 9-5-1985 | 2013 | `actualizacion-renta-arrendamientos-local-anteriores-9-5-1295` |
| 1300 | Requerimiento al arrendatario para que entregue las llaves | 2013 | `requerimiento-arrendatario-entregue-llaves-1300` |
| 1302 | Requerimiento al arrendador para que reciba las llaves | 2013 | `requerimiento-arrendador-reciba-llaves-1302` |
| 1303 | Entrega de llaves con la fianza afecta a las rentas atrasadas | 2013 | `entrega-llaves-fianza-afecta-rentas-atrasadas-1303` |
| 1305 | Aviso del arrendatario: ejercicio del derecho de retracto | 2013 | `aviso-arrendatario-ejercicio-derecho-retracto-1305` |
| 1313 | Aviso al arrendador de reparaciones ordinarias hechas por el arrendatario | 2013 | `aviso-arrendador-reparaciones-ordinarias-hechas-1313` |
| 1316 | Aviso del arrendatario de rebaja de renta por obras de conservación | 2013 | `aviso-arrendatario-rebaja-renta-obras-conservacion-1316` |
| 1320 | Entrega de llaves con la fianza afecta a reparaciones | 2013 | `entrega-llaves-fianza-afecta-reparaciones-1320` |
| 1321 | Actualización de renta en arrendamientos de vivienda anteriores al 9-5-1985 | 2013 | `actualizacion-renta-arrendamientos-vivienda-anteriores-9-1321` |
| 1322 | Actualización de renta en arrendamientos de local posteriores al 9-5-1985 vigentes con la LAU 1994 | 2013 | `actualizacion-renta-arrendamientos-local-posteriores-9-5-1322` |
| 1323 | Actualización de renta en vivienda posterior al 9-5-1985 vigente con la LAU 1994 | 2013 | `actualizacion-renta-vivienda-posterior-9-5-1985-vigente-1323` |
| 1366 | Traslado del requerimiento del arrendador al arrendatario | 2013 | `traslado-requerimiento-arrendador-arrendatario-1366` |
| 1411 | Aviso a propietarios y arrendatarios del inicio de obras | 2013 | `aviso-propietarios-arrendatarios-inicio-obras-1411` |
| 1432 | Aviso del arrendatario de no prorrogar el arrendamiento de vivienda | 2013 | `aviso-arrendatario-no-prorrogar-arrendamiento-vivienda-1432` |
| 1446 | Aviso del arrendador de extinción del arrendamiento de local | 2014 | `aviso-arrendador-extincion-arrendamiento-local-1446` |

## Otros (23)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 59 | Negativa del arrendador no gran tenedor a la prórroga extraordinaria (Ley 12/2023) | 2023 | `negativa-arrendador-no-gran-tenedor-prorroga-59` |
| 193 | Declaración responsable del arrendatario para la moratoria del RDL 35/2020 | 2021 | `declaracion-responsable-arrendatario-moratoria-rdl-35-193` |
| 391 | Prórroga del arrendamiento de vivienda | 2019 | `prorroga-arrendamiento-vivienda-391` |
| 443 | Demanda verbal de rentas impagadas y daños en la vivienda arrendada | 2018 | `demanda-verbal-rentas-impagadas-danos-vivienda-arrendada-443` |
| 506 | Reserva previa al arrendamiento de vivienda habitual | 2017 | `reserva-previa-arrendamiento-vivienda-habitual-506` |
| 1202 | Repercusión de obras necesarias al arrendatario de vivienda anterior al 9-5-1985 | 2013 | `repercusion-obras-necesarias-arrendatario-vivienda-1202` |
| 1216 | Repercusión de obras necesarias al arrendatario de local anterior al 9-5-1985 | 2013 | `repercusion-obras-necesarias-arrendatario-local-anterior-1216` |
| 1247 | Consignación de renta para enervar la acción en arrendamiento | 2013 | `consignacion-renta-enervar-accion-arrendamiento-1247` |
| 1253 | Repercusión del IBI al arrendatario de vivienda anterior al 9-5-1985 | 2013 | `repercusion-ibi-arrendatario-vivienda-anterior-9-5-1985-1253` |
| 1263 | Subrogación en el arrendamiento de vivienda | 2013 | `subrogacion-arrendamiento-vivienda-1263` |
| 1265 | Consentimiento para ceder el arrendamiento de vivienda | 2013 | `consentimiento-ceder-arrendamiento-vivienda-1265` |
| 1268 | Consentir el subarriendo parcial de la vivienda | 2013 | `consentir-subarriendo-parcial-vivienda-1268` |
| 1271 | Subrogación en arrendamiento de local posterior al 9-5-1985 vigente con la LAU 1994 | 2013 | `subrogacion-arrendamiento-local-posterior-9-5-1985-1271` |
| 1272 | Subrogación en arrendamiento de vivienda posterior al 9-5-1985 vigente con la LAU 1994 | 2013 | `subrogacion-arrendamiento-vivienda-posterior-9-5-1985-1272` |
| 1273 | Repercusión de obras de reparación al arrendatario de vivienda posterior al 9-5-1985 | 2013 | `repercusion-obras-reparacion-arrendatario-vivienda-1273` |
| 1274 | Subrogación en arrendamiento de vivienda anterior al 9-5-1985 vigente con la LAU 1994 | 2013 | `subrogacion-arrendamiento-vivienda-anterior-9-5-1985-1274` |
| 1275 | Subrogación en arrendamiento de local anterior al 9-5-1985 vigente con la LAU 1994 | 2013 | `subrogacion-arrendamiento-local-anterior-9-5-1985-1275` |
| 1276 | Repercusión de obras de reparación al arrendatario de local posterior al 9-5-1985 | 2013 | `repercusion-obras-reparacion-arrendatario-local-1276` |
| 1297 | Aviso del arrendador de no renovar el arrendamiento para uso distinto de vivienda | 2013 | `aviso-arrendador-no-renovar-arrendamiento-uso-distinto-1297` |
| 1309 | Preaviso de desistimiento del arrendatario en vivienda de más de cinco años (LAU original) | 2013 | `preaviso-desistimiento-arrendatario-vivienda-mas-cinco-1309` |
| 1314 | Consentimiento del arrendador a obras en la vivienda | 2013 | `consentimiento-arrendador-obras-vivienda-1314` |
| 1364 | Apercibimiento al arrendatario para que cese en actividades molestas | 2013 | `apercibimiento-arrendatario-cese-actividades-molestas-1364` |
| 1426 | Apercibimiento al propietario para que su arrendatario cese en actividades molestas | 2013 | `apercibimiento-propietario-arrendatario-cese-actividades-1426` |
