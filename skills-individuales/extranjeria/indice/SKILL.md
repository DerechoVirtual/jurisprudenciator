---
name: indice
description: "Índice de los 96 formularios de extranjería (residencia, arraigo, renovación, reagrupación, visados, autorizaciones de trabajo, expulsión, nacionalidad, asilo). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Extranjería: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/extranjeria:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (26)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1 | Contencioso contra la denegación del certificado de insuficiencia de demandantes de empleo | 2025 | `contencioso-contra-denegacion-certificado-insuficiencia-1` |
| 3 | Contencioso por denegar renovar residencia y trabajo por cuenta ajena (antecedentes policiales) | 2025 | `contencioso-denegar-renovar-residencia-trabajo-cuenta-3` |
| 4 | Contencioso contra el silencio en el certificado de insuficiencia de demandantes de empleo | 2025 | `contencioso-contra-silencio-certificado-insuficiencia-4` |
| 43 | Demanda contra denegar la tarjeta de residencia permanente de familiar de ciudadano UE | 2021 | `demanda-contra-denegar-tarjeta-residencia-permanente-43` |
| 79 | Contencioso ante la Audiencia Nacional por silencio negativo en nacionalidad | 2019 | `contencioso-ante-audiencia-nacional-silencio-negativo-79` |
| 80 | Demanda contra la expulsión del art. 57.2 LO 4/2000 | 2019 | `demanda-contra-expulsion-art-57-2-lo-4-2000-80` |
| 191 | Demanda contra denegar visados en régimen comunitario | 2016 | `demanda-contra-denegar-visados-regimen-comunitario-191` |
| 279 | Demanda contra la denegación de visado | 2016 | `demanda-contra-denegacion-visado-279` |
| 283 | Demanda en un expediente de expulsión | 2015 | `demanda-expediente-expulsion-283` |
| 294 | Demanda contra denegar la nacionalidad por falta de integración | 2014 | `demanda-contra-denegar-nacionalidad-falta-integracion-294` |
| 301 | Demanda contra visado de reagrupación familiar denegado (modelo 1) | 2014 | `demanda-contra-visado-reagrupacion-familiar-denegado-301` |
| 327 | Interponer contencioso contra la denegación de nacionalidad | 2013 | `interponer-contencioso-contra-denegacion-nacionalidad-327` |
| 340 | Demanda para obtener la nacionalidad por opción | 2013 | `demanda-obtener-nacionalidad-opcion-340` |
| 341 | Contencioso para obtener la nacionalidad por opción | 2013 | `contencioso-obtener-nacionalidad-opcion-341` |
| 363 | Demanda abreviada contra la denegación de autorización de trabajo y residencia | 2013 | `demanda-abreviada-contra-denegacion-autorizacion-trabajo-363` |
| 364 | Contencioso abreviado contra resolución de expulsión | 2013 | `contencioso-abreviado-contra-resolucion-expulsion-364` |
| 365 | Contencioso ante la Audiencia Nacional en nacionalidad (procedimiento ordinario) | 2013 | `contencioso-ante-audiencia-nacional-nacionalidad-365` |
| 366 | Demanda contra decreto de expulsión | 2013 | `demanda-contra-decreto-expulsion-366` |
| 377 | Demanda contra visado de reagrupación familiar denegado (modelo 2) | 2013 | `demanda-contra-visado-reagrupacion-familiar-denegado-377` |
| 385 | Contencioso con medida cautelarísima por internamiento | 2013 | `contencioso-medida-cautelarisima-internamiento-385` |
| 387 | Demanda de nacionalidad: acreditar buena conducta cívica | 2013 | `demanda-nacionalidad-acreditar-buena-conducta-civica-387` |
| 389 | Contencioso contra la denegación de entrada | 2013 | `contencioso-contra-denegacion-entrada-389` |
| 710 | Alzada contra la denegación de entrada y retorno del servicio fronterizo | 2009 | `alzada-contra-denegacion-entrada-retorno-servicio-710` |
| 713 | Demanda abreviada en extranjería: autorización de residencia y trabajo | 2009 | `demanda-abreviada-extranjeria-autorizacion-residencia-713` |
| 963 | Contencioso contra la inadmisión de residencia y trabajo en la regularización extraordinaria | 2008 | `contencioso-contra-inadmision-residencia-trabajo-963` |
| 226 (Laboral) | Residencia de larga duración denegada por antecedentes penales: demanda | 2019 | `residencia-larga-duracion-denegada-antecedentes-penales-l226` |

## Recursos e impugnaciones (19)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 58 | Alzada contra denegar la tarjeta de residencia temporal de familiar de ciudadano UE | 2020 | `alzada-contra-denegar-tarjeta-residencia-temporal-58` |
| 247 | Reposición contra denegación de residencia permanente (silencio positivo) | 2016 | `reposicion-contra-denegacion-residencia-permanente-247` |
| 261 | Alzada contra denegación de entrada en España con carta de invitación | 2016 | `alzada-contra-denegacion-entrada-espana-carta-invitacion-261` |
| 284 | Apelación en procedimiento de expulsión | 2015 | `apelacion-procedimiento-expulsion-284` |
| 300 | Reposición contra visado de reagrupación familiar denegado | 2014 | `reposicion-contra-visado-reagrupacion-familiar-denegado-300` |
| 342 | Reposición en nacionalidad española por residencia | 2013 | `reposicion-nacionalidad-espanola-residencia-342` |
| 360 | Reposición en residencia de larga duración por antecedentes penales | 2013 | `reposicion-residencia-larga-duracion-antecedentes-360` |
| 370 | Apelación en materia de asilo | 2013 | `apelacion-materia-asilo-370` |
| 371 | Reposición contra denegar renovar residencia y trabajo por cuenta propia | 2013 | `reposicion-contra-denegar-renovar-residencia-trabajo-371` |
| 373 | Reposición contra visado de reagrupación denegado por no acreditar edad o parentesco | 2013 | `reposicion-contra-visado-reagrupacion-denegado-no-373` |
| 374 | Reposición ante la Subdelegación en expulsión preferente | 2013 | `reposicion-ante-subdelegacion-expulsion-preferente-374` |
| 382 | Alzada contra denegación de entrada a un extranjero con carta de invitación | 2013 | `alzada-contra-denegacion-entrada-extranjero-carta-382` |
| 383 | Reposición contra multa por estancia irregular | 2013 | `reposicion-contra-multa-estancia-irregular-383` |
| 537 | Reposición contra denegación de permiso de trabajo a un extranjero | 2011 | `reposicion-contra-denegacion-permiso-trabajo-extranjero-537` |
| 584 | Reposición contra denegación de residencia temporal por arraigo | 2011 | `reposicion-contra-denegacion-residencia-temporal-arraigo-584` |
| 709 | Alzada contra denegar renovar residencia y trabajo por informe gubernativo desfavorable | 2009 | `alzada-contra-denegar-renovar-residencia-trabajo-informe-709` |
| 717 | Reposición contra sanción de expulsión por estancia ilegal (art. 53.a Ley de Extranjería) | 2009 | `reposicion-contra-sancion-expulsion-estancia-ilegal-art-717` |
| 957 | Reposición contra inadmisión por falta de empadronamiento | 2008 | `reposicion-contra-inadmision-falta-empadronamiento-957` |
| 966 | Recurso contra la expulsión del procedimiento preferente | 2008 | `recurso-contra-expulsion-procedimiento-preferente-966` |

## Contestaciones, oposiciones y alegaciones (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 359 | Alegaciones en expulsión de extranjero condenado a pena de prisión | 2013 | `alegaciones-expulsion-extranjero-condenado-pena-prision-359` |
| 388 | Alegaciones en expulsión por procedimiento preferente | 2013 | `alegaciones-expulsion-procedimiento-preferente-388` |
| 536 | Alegaciones en expulsión por arraigo familiar | 2011 | `alegaciones-expulsion-arraigo-familiar-536` |
| 715 | Alegaciones de defensa en expulsión preferente por infracción de la Ley de Extranjería | 2009 | `alegaciones-defensa-expulsion-preferente-infraccion-ley-715` |
| 716 | Alegaciones en expulsión por estancia ilegal (art. 53.a Ley de Extranjería) | 2009 | `alegaciones-expulsion-estancia-ilegal-art-53-ley-716` |
| 959 | Alegaciones en actuaciones complementarias de extranjería | 2008 | `alegaciones-actuaciones-complementarias-extranjeria-959` |

## Solicitudes y expedientes (16)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 51 | Medida cautelarísima para suspender la orden de expulsión de un extranjero | 2021 | `medida-cautelarisima-suspender-orden-expulsion-51` |
| 69 | Pedir certificado escolar para obtener la residencia legal | 2019 | `pedir-certificado-escolar-obtener-residencia-legal-69` |
| 369 | Pedir informe de escolarización para renovar residencia y trabajo | 2013 | `pedir-informe-escolarizacion-renovar-residencia-trabajo-369` |
| 375 | Pedir que se declare prescrita la sanción de expulsión | 2013 | `pedir-declare-prescrita-sancion-expulsion-375` |
| 386 | Pedir la caducidad del expediente de expulsión | 2013 | `pedir-caducidad-expediente-expulsion-386` |
| 390 | Pedir revocar la devolución por arraigo | 2013 | `pedir-revocar-devolucion-arraigo-390` |
| 391 | Pedir modificar la autorización de residencia y trabajo | 2013 | `pedir-modificar-autorizacion-residencia-trabajo-391` |
| 587 | Pedir cédula de inscripción o título de viaje (EX16) | 2011 | `pedir-cedula-inscripcion-titulo-viaje-ex16-587` |
| 588 | Pedir tarjeta de residencia de familiar de ciudadano comunitario (EX19) | 2011 | `pedir-tarjeta-residencia-familiar-ciudadano-comunitario-588` |
| 589 | Pedir certificado de registro de residencia comunitaria (EX18) | 2011 | `pedir-certificado-registro-residencia-comunitaria-ex18-589` |
| 878 | Pedir ejecución provisional de sentencia en extranjería | 2009 | `pedir-ejecucion-provisional-sentencia-extranjeria-878` |
| 955 | Reexamen de la denegación de asilo | 2008 | `reexamen-denegacion-asilo-955` |
| 956 | Reexamen de la inadmisión a trámite de asilo | 2008 | `reexamen-inadmision-tramite-asilo-956` |
| 960 | Archivo por colaborar con la justicia: alegaciones a propuesta de expulsión (ordinario) | 2008 | `archivo-colaborar-justicia-alegaciones-propuesta-960` |
| 962 | Archivo por colaborar con la justicia: alegaciones a propuesta de expulsión (preferente) | 2008 | `archivo-colaborar-justicia-alegaciones-propuesta-962` |
| 227 (Laboral) | Revocar la resolución de expulsión: solicitud | 2019 | `revocar-resolucion-expulsion-solicitud-l227` |

## Escritos de trámite (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 295 | Conclusiones: nacionalidad denegada por falta de integración | 2014 | `conclusiones-nacionalidad-denegada-falta-integracion-295` |
| 392 | Solicitar el retorno voluntario | 2013 | `solicitar-retorno-voluntario-392` |
| 711 | Otrosí de demanda pidiendo suspender la expulsión | 2009 | `otrosi-demanda-pidiendo-suspender-expulsion-711` |
| 712 | Apelación contra auto que deniega suspender la expulsión (extranjería) | 2009 | `apelacion-contra-auto-deniega-suspender-expulsion-712` |
| 714 | Apelación contra sentencia que confirma una expulsión (extranjería) | 2009 | `apelacion-contra-sentencia-confirma-expulsion-714` |

## Actos y resoluciones de la Administración o del órgano judicial (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 68 | Certificado de silencio positivo en la renovación de residencia y trabajo | 2019 | `certificado-silencio-positivo-renovacion-residencia-68` |
| 362 | Solicitar autorización de residencia comunitaria | 2013 | `solicitar-autorizacion-residencia-comunitaria-362` |
| 376 | Acta de manifestaciones para reagrupación familiar comunitaria | 2013 | `acta-manifestaciones-reagrupacion-familiar-comunitaria-376` |
| 224 (Laboral) | Silencio positivo en la modificación de autorización: certificado | 2019 | `silencio-positivo-modificacion-autorizacion-certificado-l224` |

## Contratos, escrituras y documentos (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 262 | Mandato con poder de representación para tramitar la nacionalidad española | 2016 | `mandato-poder-representacion-tramitar-nacionalidad-262` |
| 282 | Convenio de colaboración para estancia en España por voluntariado | 2015 | `convenio-colaboracion-estancia-espana-voluntariado-282` |
| 357 | Recurso contra la denegación de asilo | 2013 | `recurso-contra-denegacion-asilo-357` |
| 358 | Demanda contra la denegación de asilo | 2013 | `demanda-contra-denegacion-asilo-358` |
| 493 | Solicitud oficial del Estatuto de Apátrida | 2012 | `solicitud-oficial-estatuto-apatrida-493` |
| 586 | Modelos oficiales para iniciar trámites de documentación de extranjeros | 2011 | `modelos-oficiales-iniciar-tramites-documentacion-586` |
| 238 (Laboral) | Designar representante para tramitar visados | 2019 | `designar-representante-tramitar-visados-l238` |

## Comunicaciones, requerimientos y reclamaciones (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 280 | Frente a la denegación de visado de reagrupación familiar comunitaria | 2015 | `frente-denegacion-visado-reagrupacion-familiar-280` |
| 958 | Denuncia de un hecho relevante en extranjería | 2008 | `denuncia-hecho-relevante-extranjeria-958` |

## Otros (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 71 | Revocar la expulsión por matrimonio con español | 2019 | `revocar-expulsion-matrimonio-espanol-71` |
| 94 | Declaración de empresas extranjeras de someterse a los tribunales españoles (contratos públicos) | 2018 | `declaracion-empresas-extranjeras-someterse-tribunales-94` |
| 361 | Residencia comunitaria de familiar de ciudadano de la Unión | 2013 | `residencia-comunitaria-familiar-ciudadano-union-361` |
| 372 | Revocar la expulsión por circunstancias excepcionales | 2013 | `revocar-expulsion-circunstancias-excepcionales-372` |
| 378 | Certificado de solicitante de asilo para pedir la nacionalidad | 2013 | `certificado-solicitante-asilo-pedir-nacionalidad-378` |
| 379 | Certificado de solicitante de asilo para casarse | 2013 | `certificado-solicitante-asilo-casarse-379` |
| 380 | Matrimonio de un solicitante de asilo | 2013 | `matrimonio-solicitante-asilo-380` |
| 381 | Periodo de reflexión en casos de trata de seres humanos | 2013 | `periodo-reflexion-casos-trata-seres-humanos-381` |
| 393 | Internamiento de extranjeros: reforma y apelación contra el auto | 2013 | `internamiento-extranjeros-reforma-apelacion-contra-auto-393` |
| 191 (Laboral) | Memoria de actividad de la empresa y perfil del puesto para desplazar y contratar extranjeros | 2020 | `memoria-actividad-empresa-perfil-puesto-desplazar-l191` |
| 225 (Laboral) | Silencio positivo en la residencia de larga duración: certificado | 2019 | `silencio-positivo-residencia-larga-duracion-certificado-l225` |
