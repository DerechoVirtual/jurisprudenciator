---
name: indice
description: "Índice de los 277 formularios de procedimiento administrativo común (solicitudes, alegaciones, audiencia, acceso al expediente, silencio, notificaciones). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Procedimiento administrativo común: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Ordenanzas municipales** (tráfico, urbanismo, tributos locales, convivencia) → `buscar_ordenanzas` → `leer_ordenanza`.
- **Criterio de Hacienda y del TEAC** → `buscar_consultas_hacienda` → `leer_consulta_hacienda`; `buscar_doctrina_teac` → `leer_resolucion_teac`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/procedimiento-administrativo-comun:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Contestaciones, oposiciones y alegaciones (20)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 36 | Alegaciones en procedimiento administrativo simplificado | 2022 | `alegaciones-procedimiento-administrativo-simplificado-36` |
| 66 | Alegaciones en expediente de contrabando por importar una pieza de fauna | 2020 | `alegaciones-expediente-contrabando-importar-pieza-fauna-66` |
| 146 | Alegaciones del interesado en actuaciones complementarias ordenadas por el órgano resolutor | 2017 | `alegaciones-interesado-actuaciones-complementarias-146` |
| 975 | Alegaciones y prueba tras el acuerdo de iniciación | 2008 | `alegaciones-prueba-tras-acuerdo-iniciacion-975` |
| 976 | Alegaciones en las actuaciones previas | 2008 | `alegaciones-actuaciones-previas-976` |
| 980 | Alegaciones a la propuesta de resolución | 2008 | `alegaciones-propuesta-resolucion-980` |
| 981 | Alegaciones y prueba en la iniciación por denuncia | 2008 | `alegaciones-prueba-iniciacion-denuncia-981` |
| 982 | Alegaciones y prueba al inicio del procedimiento | 2008 | `alegaciones-prueba-inicio-procedimiento-982` |
| 983 | Alegaciones en la audiencia previa, sin propuesta de resolución | 2008 | `alegaciones-audiencia-previa-sin-propuesta-resolucion-983` |
| 994 | Alegaciones ante la conversión del procedimiento | 2008 | `alegaciones-ante-conversion-procedimiento-994` |
| 996 | Alegaciones y prueba en la propuesta de resolución | 2008 | `alegaciones-prueba-propuesta-resolucion-996` |
| 1104 | Descargos | 2008 | `descargos-1104` |
| 1323 | Alegaciones del interesado antes del trámite de audiencia | 2004 | `alegaciones-interesado-antes-tramite-audiencia-1323` |
| 1335 | Oposición a la acumulación de expedientes | 2004 | `oposicion-acumulacion-expedientes-1335` |
| 1339 | Alegaciones en audiencia para evitar las medidas provisionales | 2004 | `alegaciones-audiencia-evitar-medidas-provisionales-1339` |
| 1375 | Alegaciones de terceros en información pública | 2004 | `alegaciones-terceros-informacion-publica-1375` |
| 1381 | Alegaciones en audiencia y vista del expediente | 2004 | `alegaciones-audiencia-vista-expediente-1381` |
| 1401 | Respuesta a la petición de información y orientación del ciudadano | 2004 | `respuesta-peticion-informacion-orientacion-ciudadano-1401` |
| 1911 | Alegaciones por no evacuar en plazo un informe administrativo | 2012 | `alegaciones-no-evacuar-plazo-informe-administrativo-1911` |
| 1914 | Alegaciones por incumplir el plazo máximo para resolver | 2012 | `alegaciones-incumplir-plazo-maximo-resolver-1914` |

## Solicitudes y expedientes (56)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 73 | Pedir garantías al encargado del tratamiento de datos | 2019 | `pedir-garantias-encargado-tratamiento-datos-73` |
| 126 | Pedir certificado de denegación por silencio administrativo | 2017 | `pedir-certificado-denegacion-silencio-administrativo-126` |
| 132 | Pedir tramitación ordinaria por necesitar trámites adicionales | 2017 | `pedir-tramitacion-ordinaria-necesitar-tramites-132` |
| 136 | Pedir la tramitación simplificada del procedimiento | 2017 | `pedir-tramitacion-simplificada-procedimiento-136` |
| 155 | Pedir certificado de silencio administrativo | 2017 | `pedir-certificado-silencio-administrativo-155` |
| 251 | Pedir a la Administración la traducción al castellano de la documentación | 2016 | `pedir-administracion-traduccion-castellano-documentacion-251` |
| 252 | Pedir que el procedimiento se instruya en castellano | 2016 | `pedir-procedimiento-instruya-castellano-252` |
| 330 | Pedir certificado de acto presunto por doble silencio | 2013 | `pedir-certificado-acto-presunto-doble-silencio-330` |
| 349 | Pedir requerimiento por incumplir la estimación (información y participación) (en catalán) | 2013 | `pedir-requerimiento-incumplir-estimacion-informacion-349` |
| 394 | Pedir requerimiento por incumplir la estimación (información y participación) | 2013 | `pedir-requerimiento-incumplir-estimacion-informacion-394` |
| 550 | Pedir acceso a documentos que afectan a la intimidad | 2011 | `pedir-acceso-documentos-afectan-intimidad-550` |
| 569 | Pedir medidas provisionales antes de iniciar el procedimiento | 2011 | `pedir-medidas-provisionales-antes-iniciar-procedimiento-569` |
| 573 | Pedir acceso directo a consultar expedientes | 2011 | `pedir-acceso-directo-consultar-expedientes-573` |
| 574 | Pedir copia de documentos | 2011 | `pedir-copia-documentos-574` |
| 575 | Acceso individualizado a documentos de un archivo | 2011 | `acceso-individualizado-documentos-archivo-575` |
| 695 | Pedir abrir el periodo de prueba | 2010 | `pedir-abrir-periodo-prueba-695` |
| 722 | Reclamación previa por no ejecutar un acto firme (Castilla-La Mancha) | 2009 | `reclamacion-previa-no-ejecutar-acto-firme-castilla-722` |
| 723 | Reclamación previa por no ejecutar una prestación (Castilla-La Mancha) | 2009 | `reclamacion-previa-no-ejecutar-prestacion-castilla-723` |
| 735 | Reclamación previa por no ejecutar una prestación (Castilla y León) | 2009 | `reclamacion-previa-no-ejecutar-prestacion-castilla-leon-735` |
| 757 | Pedir la terminación del procedimiento por falta de objeto (Galicia) | 2009 | `pedir-terminacion-procedimiento-falta-objeto-galicia-757` |
| 758 | Reclamación previa por no ejecutar un acto firme (Galicia) | 2009 | `reclamacion-previa-no-ejecutar-acto-firme-galicia-758` |
| 759 | Reclamación previa por no ejecutar una prestación (Comunidad Valenciana) | 2009 | `reclamacion-previa-no-ejecutar-prestacion-comunidad-759` |
| 772 | Pedir la terminación del procedimiento por falta de objeto (Comunidad Valenciana) | 2009 | `pedir-terminacion-procedimiento-falta-objeto-comunidad-772` |
| 773 | Reclamación previa por no ejecutar un acto firme (Comunidad Valenciana) | 2009 | `reclamacion-previa-no-ejecutar-acto-firme-comunidad-773` |
| 774 | Reclamación previa por no ejecutar una prestación (Galicia) | 2009 | `reclamacion-previa-no-ejecutar-prestacion-galicia-774` |
| 785 | Pedir la terminación del procedimiento por falta de objeto (Andalucía) | 2009 | `pedir-terminacion-procedimiento-falta-objeto-andalucia-785` |
| 786 | Reclamación previa por no ejecutar un acto firme (Andalucía) | 2009 | `reclamacion-previa-no-ejecutar-acto-firme-andalucia-786` |
| 787 | Reclamación previa por no ejecutar una prestación (Andalucía) | 2009 | `reclamacion-previa-no-ejecutar-prestacion-andalucia-787` |
| 798 | Reclamación previa por no ejecutar una prestación (Navarra) | 2009 | `reclamacion-previa-no-ejecutar-prestacion-navarra-798` |
| 799 | Reclamación previa por no ejecutar un acto firme (Navarra) | 2009 | `reclamacion-previa-no-ejecutar-acto-firme-navarra-799` |
| 852 | Reclamación previa por no ejecutar una prestación (Cataluña, en catalán) | 2009 | `reclamacion-previa-no-ejecutar-prestacion-cataluna-852` |
| 863 | Reclamación previa por no ejecutar una prestación (Comunidad de Madrid) | 2009 | `reclamacion-previa-no-ejecutar-prestacion-comunidad-863` |
| 903 | Pedir a la Administración ejecutar un acto firme | 2009 | `pedir-administracion-ejecutar-acto-firme-903` |
| 973 | Pedir el archivo del expediente por colaborar con la justicia | 2008 | `pedir-archivo-expediente-colaborar-justicia-973` |
| 978 | Pedir que cese la aprehensión de bienes por ser de un tercero | 2008 | `pedir-cese-aprehension-bienes-ser-tercero-978` |
| 979 | Pedir copias de documentos del expediente | 2008 | `pedir-copias-documentos-expediente-979` |
| 997 | Pedir actuaciones complementarias | 2008 | `pedir-actuaciones-complementarias-997` |
| 1183 | Solicitud vecinal de antecedentes antes de actuar por sustitución | 2008 | `solicitud-vecinal-antecedentes-antes-actuar-sustitucion-1183` |
| 1188 | Solicitud vecinal de antecedentes antes de ejercitar acciones (Cataluña) | 2008 | `solicitud-vecinal-antecedentes-antes-ejercitar-acciones-1188` |
| 1202 | Solicitud de iniciación de expediente a instancia del interesado | 2008 | `solicitud-iniciacion-expediente-instancia-interesado-1202` |
| 1203 | Petición razonada de un órgano a otro para iniciar expediente | 2008 | `peticion-razonada-organo-otro-iniciar-expediente-1203` |
| 1317 | Solicitud del interesado de tramitación urgente | 2004 | `solicitud-interesado-tramitacion-urgente-1317` |
| 1318 | Solicitud de ampliación de plazo para cumplir trámites | 2004 | `solicitud-ampliacion-plazo-cumplir-tramites-1318` |
| 1319 | Solicitud de acumulación de expedientes | 2004 | `solicitud-acumulacion-expedientes-1319` |
| 1324 | Pedir que se admita la subsanación requerida por la Administración | 2004 | `pedir-admita-subsanacion-requerida-administracion-1324` |
| 1330 | Pedir certificado del silencio producido | 2004 | `pedir-certificado-silencio-producido-1330` |
| 1331 | Pedir copias de documentos del expediente como interesado | 2004 | `pedir-copias-documentos-expediente-como-interesado-1331` |
| 1359 | Pedir eficacia retroactiva de actos administrativos | 2004 | `pedir-eficacia-retroactiva-actos-administrativos-1359` |
| 1361 | Petición de terceros para que se adopten medidas provisionales | 2004 | `peticion-terceros-adopten-medidas-provisionales-1361` |
| 1384 | Pedir la identificación de las autoridades y el personal que tramitan el procedimiento | 2004 | `pedir-identificacion-autoridades-personal-tramitan-1384` |
| 1387 | Pedir información sobre el estado de tramitación como interesado | 2004 | `pedir-informacion-sobre-estado-tramitacion-como-1387` |
| 1397 | Pedir acceso a expedientes | 2004 | `pedir-acceso-expedientes-1397` |
| 1724 | Solicitud de autorización para actividades de transporte terrestre | 2004 | `solicitud-autorizacion-actividades-transporte-terrestre-1724` |
| 1727 | Solicitud de medalla o placa al mérito del transporte terrestre | 2004 | `solicitud-medalla-placa-merito-transporte-terrestre-1727` |
| 1909 | Pedir ampliación del plazo del trámite de audiencia | 2012 | `pedir-ampliacion-plazo-tramite-audiencia-1909` |
| 1910 | Pedir ampliación del plazo de subsanación para aportar documentación | 2012 | `pedir-ampliacion-plazo-subsanacion-aportar-documentacion-1910` |

## Escritos de trámite (44)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 133 | Subsanar la solicitud de tramitación simplificada | 2017 | `subsanar-solicitud-tramitacion-simplificada-133` |
| 134 | Oposición del particular a la tramitación simplificada acordada de oficio | 2017 | `oposicion-particular-tramitacion-simplificada-acordada-134` |
| 143 | Comunicar el cambio del medio de notificación | 2017 | `comunicar-cambio-medio-notificacion-143` |
| 207 | Contestación a la petición de información sobre el estado del expediente | 2016 | `contestacion-peticion-informacion-sobre-estado-207` |
| 214 | Pedir potestativamente certificado de actos presuntos | 2016 | `pedir-potestativamente-certificado-actos-presuntos-214` |
| 250 | Queja por defectos de tramitación | 2016 | `queja-defectos-tramitacion-250` |
| 254 | Renunciar al trámite de audiencia | 2016 | `renunciar-tramite-audiencia-254` |
| 326 | Revocar la representación dada a otro | 2013 | `revocar-representacion-dada-otro-326` |
| 384 | Certificación de acto presunto por silencio negativo | 2013 | `certificacion-acto-presunto-silencio-negativo-384` |
| 567 | Cumplimentar el trámite de audiencia | 2011 | `cumplimentar-tramite-audiencia-567` |
| 628 | Pedir el archivo por caducidad | 2010 | `pedir-archivo-caducidad-628` |
| 630 | Aportar documentos antes del trámite de audiencia | 2010 | `aportar-documentos-antes-tramite-audiencia-630` |
| 694 | Proponer medios de prueba en el procedimiento administrativo | 2010 | `proponer-medios-prueba-procedimiento-administrativo-694` |
| 696 | Propuesta del interesado de terminación convencional | 2010 | `propuesta-interesado-terminacion-convencional-696` |
| 995 | Aportar documentos como prueba en el expediente | 2008 | `aportar-documentos-como-prueba-expediente-995` |
| 1071 | Subsanación de defectos por el interesado | 2008 | `subsanacion-defectos-interesado-1071` |
| 1075 | Contestación al requerimiento de información previa | 2008 | `contestacion-requerimiento-informacion-previa-1075` |
| 1165 | Mejora de la solicitud de iniciación del expediente (escrito) | 2008 | `mejora-solicitud-iniciacion-expediente-escrito-1165` |
| 1180 | Vecino pide antecedentes y documentos a la entidad local antes de actuar por sustitución (Navarra) | 2008 | `vecino-pide-antecedentes-documentos-entidad-local-antes-1180` |
| 1205 | Otros interesados se personan en el procedimiento | 2008 | `otros-interesados-personan-procedimiento-1205` |
| 1209 | Denegación de la información solicitada | 2008 | `denegacion-informacion-solicitada-1209` |
| 1247 | Prueba de documentos públicos | 2008 | `prueba-documentos-publicos-1247` |
| 1325 | Renuncia a derechos en el procedimiento administrativo | 2004 | `renuncia-derechos-procedimiento-administrativo-1325` |
| 1326 | Formalización del desistimiento en el procedimiento administrativo | 2004 | `formalizacion-desistimiento-procedimiento-administrativo-1326` |
| 1332 | Pedir que se tengan por subsanados los defectos de representación | 2004 | `pedir-tengan-subsanados-defectos-representacion-1332` |
| 1333 | Queja por anormalidades en la tramitación y exigencia de responsabilidad a la Administración | 2004 | `queja-anormalidades-tramitacion-exigencia-1333` |
| 1341 | Queja por defectos de tramitación con petición de subsanación y responsabilidad disciplinaria | 2004 | `queja-defectos-tramitacion-peticion-subsanacion-1341` |
| 1344 | Contestación que identifica a los interesados no personados o aporta la información requerida | 2004 | `contestacion-identifica-interesados-no-personados-aporta-1344` |
| 1345 | Comunicación de decisión favorable al acceso a archivos y registros | 2004 | `comunicacion-decision-favorable-acceso-archivos-1345` |
| 1350 | Contestación a la puesta de manifiesto sobre cuestiones conexas | 2004 | `contestacion-puesta-manifiesto-sobre-cuestiones-conexas-1350` |
| 1376 | Respuesta razonada a los alegantes en información pública | 2004 | `respuesta-razonada-alegantes-informacion-publica-1376` |
| 1382 | Manifestar que no se formularán alegaciones en audiencia | 2004 | `manifestar-no-formularan-alegaciones-audiencia-1382` |
| 1385 | Comunicar a la Administración el cese del representante | 2004 | `comunicar-administracion-cese-representante-1385` |
| 1390 | Personación de los interesados en el procedimiento | 2004 | `personacion-interesados-procedimiento-1390` |
| 1391 | Personación por acción popular en un expediente | 2004 | `personacion-accion-popular-expediente-1391` |
| 1392 | Personación de interesados por relación jurídica transmisible | 2004 | `personacion-interesados-relacion-juridica-transmisible-1392` |
| 1393 | Personación de asociaciones y organizaciones de intereses colectivos | 2004 | `personacion-asociaciones-organizaciones-intereses-1393` |
| 1394 | Informe al interesado sobre el estado de tramitación del expediente | 2004 | `informe-interesado-sobre-estado-tramitacion-expediente-1394` |
| 1395 | Peticiones sobre la lengua oficial del procedimiento | 2004 | `peticiones-sobre-lengua-oficial-procedimiento-1395` |
| 1396 | Pedir información y orientación previas a un procedimiento | 2004 | `pedir-informacion-orientacion-previas-procedimiento-1396` |
| 1399 | Hacer valer el derecho a no presentar documentos que ya obran en la Administración | 2004 | `hacer-valer-derecho-no-presentar-documentos-ya-obran-1399` |
| 1405 | Personación para continuar el procedimiento tras desistimiento o renuncia | 2004 | `personacion-continuar-procedimiento-tras-desistimiento-1405` |
| 1418 | Pedir la admisión y práctica de medios de prueba | 2004 | `pedir-admision-practica-medios-prueba-1418` |
| 1821 | Ratificación de la denuncia por el agente cuando el denunciado niega los hechos | 2004 | `ratificacion-denuncia-agente-cuando-denunciado-niega-1821` |

## Actos y resoluciones de la Administración o del órgano judicial (99)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 35 | Resolución final en el procedimiento simplificado | 2022 | `resolucion-final-procedimiento-simplificado-35` |
| 125 | Dictamen del Consejo de Estado u órgano autonómico equivalente sobre nulidad de actos | 2017 | `dictamen-consejo-estado-u-organo-autonomico-equivalente-125` |
| 131 | Notificar al interesado la tramitación simplificada del procedimiento | 2017 | `notificar-interesado-tramitacion-simplificada-131` |
| 135 | Resolución que pasa el procedimiento a tramitación ordinaria | 2017 | `resolucion-pasa-procedimiento-tramitacion-ordinaria-135` |
| 147 | Acta de las alegaciones del interesado en instrucción complementaria | 2017 | `acta-alegaciones-interesado-instruccion-complementaria-147` |
| 149 | Acuerdo del órgano resolutor que ordena actuaciones complementarias | 2017 | `acuerdo-organo-resolutor-ordena-actuaciones-149` |
| 153 | Traslado a los interesados del acuerdo de actuaciones complementarias | 2017 | `traslado-interesados-acuerdo-actuaciones-complementarias-153` |
| 206 | Acta del intento de notificar la denuncia rechazado por el destinatario | 2016 | `acta-intento-notificar-denuncia-rechazado-destinatario-206` |
| 226 | Acta de manifestaciones del requerido en información previa | 2016 | `acta-manifestaciones-requerido-informacion-previa-226` |
| 257 | Notificar la ejecución subsidiaria de una resolución administrativa | 2016 | `notificar-ejecucion-subsidiaria-resolucion-257` |
| 258 | Notificar multa coercitiva en procedimiento administrativo | 2016 | `notificar-multa-coercitiva-procedimiento-administrativo-258` |
| 345 | Estimar reclamación de información y participación (en catalán, modelo 1) | 2013 | `estimar-reclamacion-informacion-participacion-catalan-345` |
| 346 | Multa coercitiva por incumplir requerimiento sobre información y participación (en catalán) | 2013 | `multa-coercitiva-incumplir-requerimiento-sobre-346` |
| 350 | Desestimar reclamación de información y participación (C. Valenciana, en valenciano) | 2013 | `desestimar-reclamacion-informacion-participacion-c-350` |
| 351 | Estimar reclamación de información y participación (en catalán, modelo 2) | 2013 | `estimar-reclamacion-informacion-participacion-catalan-351` |
| 353 | Desestimar reclamación de información y participación (Cataluña, en catalán) | 2013 | `desestimar-reclamacion-informacion-participacion-353` |
| 368 | Comunicar el cambio de domicilio | 2013 | `comunicar-cambio-domicilio-368` |
| 396 | Multa coercitiva por incumplir requerimiento sobre información y participación | 2013 | `multa-coercitiva-incumplir-requerimiento-sobre-396` |
| 398 | Resolución que estima la reclamación de información y participación | 2013 | `resolucion-estima-reclamacion-informacion-participacion-398` |
| 399 | Resolución que desestima la reclamación de información y participación | 2013 | `resolucion-desestima-reclamacion-informacion-399` |
| 427 | Resolver sobre la ejecución provisional | 2012 | `resolver-sobre-ejecucion-provisional-427` |
| 697 | Resolución de terminación convencional del procedimiento | 2010 | `resolucion-terminacion-convencional-procedimiento-697` |
| 700 | Notificación municipal de multa coercitiva por incumplir una orden de ejecución | 2010 | `notificacion-municipal-multa-coercitiva-incumplir-orden-700` |
| 953 | Acta de apertura del sobre de criterios de juicio de valor (suministro) | 2008 | `acta-apertura-sobre-criterios-juicio-valor-suministro-953` |
| 1030 | Denegación total o parcial de la prueba propuesta por los interesados | 2008 | `denegacion-total-parcial-prueba-propuesta-interesados-1030` |
| 1032 | Respuesta del pleno municipal al requerimiento: inadecuación de acciones (Andalucía) | 2008 | `respuesta-pleno-municipal-requerimiento-inadecuacion-1032` |
| 1033 | Respuesta del pleno municipal al requerimiento: inadecuación de acciones (Aragón) | 2008 | `respuesta-pleno-municipal-requerimiento-inadecuacion-1033` |
| 1034 | Respuesta del pleno municipal al requerimiento: inadecuación de acciones (Navarra) | 2008 | `respuesta-pleno-municipal-requerimiento-inadecuacion-1034` |
| 1035 | Respuesta del pleno de la Diputación al requerimiento de la entidad local: inadecuación de acciones | 2008 | `respuesta-pleno-diputacion-requerimiento-entidad-local-1035` |
| 1051 | Respuesta del ayuntamiento al requerimiento: no cabe impugnar actos propios (Andalucía) | 2008 | `respuesta-ayuntamiento-requerimiento-no-cabe-impugnar-1051` |
| 1052 | Respuesta del ayuntamiento al requerimiento: no cabe impugnar actos propios (Aragón) | 2008 | `respuesta-ayuntamiento-requerimiento-no-cabe-impugnar-1052` |
| 1053 | Respuesta del ayuntamiento al requerimiento: no cabe impugnar actos propios (Galicia) | 2008 | `respuesta-ayuntamiento-requerimiento-no-cabe-impugnar-1053` |
| 1054 | Respuesta de la Diputación al requerimiento: no cabe impugnar actos propios (Cataluña) | 2008 | `respuesta-diputacion-requerimiento-no-cabe-impugnar-1054` |
| 1055 | Respuesta de la Diputación Provincial al requerimiento: no cabe impugnar actos propios | 2008 | `respuesta-diputacion-provincial-requerimiento-no-cabe-1055` |
| 1056 | Respuesta del Ayuntamiento al requerimiento: no cabe impugnar actos propios (Cataluña) | 2008 | `respuesta-ayuntamiento-requerimiento-no-cabe-impugnar-1056` |
| 1057 | Respuesta del ayuntamiento al requerimiento: acciones sin posibilidad de prosperar (Andalucía) | 2008 | `respuesta-ayuntamiento-requerimiento-acciones-sin-1057` |
| 1058 | Respuesta del ayuntamiento al requerimiento: no cabe impugnar actos propios (Navarra) | 2008 | `respuesta-ayuntamiento-requerimiento-no-cabe-impugnar-1058` |
| 1059 | Respuesta del ayuntamiento al requerimiento: vía procesal inadecuada para impugnar actos propios | 2008 | `respuesta-ayuntamiento-requerimiento-via-procesal-1059` |
| 1060 | Respuesta del ayuntamiento al requerimiento: acciones sin posibilidad de prosperar (Aragón) | 2008 | `respuesta-ayuntamiento-requerimiento-acciones-sin-1060` |
| 1061 | Respuesta del pleno de la diputación al requerimiento: inadecuación de acciones (Galicia) | 2008 | `respuesta-pleno-diputacion-requerimiento-inadecuacion-1061` |
| 1062 | Respuesta del Ayuntamiento al requerimiento: acciones sin posibilidad de prosperar (Galicia) | 2008 | `respuesta-ayuntamiento-requerimiento-acciones-sin-1062` |
| 1063 | Respuesta del ayuntamiento al requerimiento: acciones sin posibilidad de prosperar (Navarra) | 2008 | `respuesta-ayuntamiento-requerimiento-acciones-sin-1063` |
| 1064 | Respuesta del ayuntamiento al requerimiento: acciones solicitadas sin posibilidad de prosperar | 2008 | `respuesta-ayuntamiento-requerimiento-acciones-1064` |
| 1065 | Respuesta del pleno de la diputación: acciones sin posibilidad de prosperar (Galicia) | 2008 | `respuesta-pleno-diputacion-acciones-sin-posibilidad-1065` |
| 1164 | Informe de un órgano administrativo a petición de otro | 2008 | `informe-organo-administrativo-peticion-otro-1164` |
| 1166 | Mejora de la solicitud de iniciación del expediente (acta) | 2008 | `mejora-solicitud-iniciacion-expediente-acta-1166` |
| 1167 | Decreto de alcaldía que ejercita acciones y encomienda la defensa a la diputación | 2008 | `decreto-alcaldia-ejercita-acciones-encomienda-defensa-1167` |
| 1171 | Respuesta del Pleno municipal al requerimiento: inadecuación de las acciones (Cataluña) | 2008 | `respuesta-pleno-municipal-requerimiento-inadecuacion-1171` |
| 1172 | Respuesta del Pleno de la Diputación al requerimiento: inadecuación de las acciones (Cataluña) | 2008 | `respuesta-pleno-diputacion-requerimiento-inadecuacion-1172` |
| 1174 | Respuesta del pleno municipal al requerimiento: inadecuación de acciones (Galicia) | 2008 | `respuesta-pleno-municipal-requerimiento-inadecuacion-1174` |
| 1197 | Respuesta del pleno de la diputación al requerimiento: no cabe impugnar actos propios (Galicia) | 2008 | `respuesta-pleno-diputacion-requerimiento-no-cabe-1197` |
| 1198 | Respuesta de la diputación al requerimiento: acciones sin posibilidad de prosperar (Andalucía) | 2008 | `respuesta-diputacion-requerimiento-acciones-sin-1198` |
| 1199 | Respuesta de la Diputación Provincial al requerimiento: acciones sin posibilidad de prosperar | 2008 | `respuesta-diputacion-provincial-requerimiento-acciones-1199` |
| 1200 | Respuesta de la diputación al requerimiento: acciones solicitadas sin prosperar (Cataluña) | 2008 | `respuesta-diputacion-requerimiento-acciones-solicitadas-1200` |
| 1201 | Respuesta del Ayuntamiento al requerimiento: acciones solicitadas sin prosperar (Cataluña) | 2008 | `respuesta-ayuntamiento-requerimiento-acciones-1201` |
| 1204 | Emplazamiento a titulares de derechos no comparecidos | 2008 | `emplazamiento-titulares-derechos-no-comparecidos-1204` |
| 1210 | Iniciación del expediente por petición razonada de otros órganos | 2008 | `iniciacion-expediente-peticion-razonada-otros-organos-1210` |
| 1211 | Informe del órgano autor de la resolución sobre el recurso interpuesto | 2008 | `informe-organo-autor-resolucion-sobre-recurso-1211` |
| 1214 | Requerir información previa al presunto responsable | 2008 | `requerir-informacion-previa-presunto-responsable-1214` |
| 1218 | Acuerdo que estima las alegaciones y rechaza las medidas provisionales | 2008 | `acuerdo-estima-alegaciones-rechaza-medidas-provisionales-1218` |
| 1219 | Acuerdo de terminación convencional del procedimiento | 2008 | `acuerdo-terminacion-convencional-procedimiento-1219` |
| 1220 | Acuerdo que deniega la acumulación | 2008 | `acuerdo-deniega-acumulacion-1220` |
| 1311 | Notificar determinados actos de otros órganos administrativos | 2005 | `notificar-determinados-actos-otros-organos-1311` |
| 1320 | Acuerdo de acumulación de expedientes incoados de oficio | 2004 | `acuerdo-acumulacion-expedientes-incoados-oficio-1320` |
| 1327 | Resolución que pone fin al procedimiento administrativo | 2004 | `resolucion-pone-fin-procedimiento-administrativo-1327` |
| 1328 | Resolución que declara la caducidad de un procedimiento iniciado a instancia de parte | 2004 | `resolucion-declara-caducidad-procedimiento-iniciado-1328` |
| 1334 | Traslado a los demás interesados de la petición de acumular expedientes | 2004 | `traslado-demas-interesados-peticion-acumular-expedientes-1334` |
| 1336 | Acuerdo de acumulación de expedientes a petición del interesado | 2004 | `acuerdo-acumulacion-expedientes-peticion-interesado-1336` |
| 1337 | Acuerdo de alteración del orden de tramitación de expedientes | 2004 | `acuerdo-alteracion-orden-tramitacion-expedientes-1337` |
| 1338 | Apertura de pieza separada de medidas provisionales | 2004 | `apertura-pieza-separada-medidas-provisionales-1338` |
| 1340 | Acuerdo que resuelve el incidente adoptando las medidas provisionales | 2004 | `acuerdo-resuelve-incidente-adoptando-medidas-1340` |
| 1342 | Acuerdo que deniega certificar el acto producido por silencio | 2004 | `acuerdo-deniega-certificar-acto-producido-silencio-1342` |
| 1346 | Requerimiento de identificación de otros interesados | 2004 | `requerimiento-identificacion-otros-interesados-1346` |
| 1347 | Resolución de multas coercitivas sucesivas para ejecutar un acto administrativo | 2004 | `resolucion-multas-coercitivas-sucesivas-ejecutar-acto-1347` |
| 1349 | Resolución de ejecución subsidiaria de un acto administrativo | 2004 | `resolucion-ejecucion-subsidiaria-acto-administrativo-1349` |
| 1351 | Acuerdo de inadmisión de pretensiones de derechos no previstos o manifiestamente infundados | 2004 | `acuerdo-inadmision-pretensiones-derechos-no-previstos-1351` |
| 1355 | Acuerdo de anulación de actuaciones y conservación de trámites | 2004 | `acuerdo-anulacion-actuaciones-conservacion-tramites-1355` |
| 1357 | Acuerdo que convierte partes de actos nulos y anulables | 2004 | `acuerdo-convierte-partes-actos-nulos-anulables-1357` |
| 1370 | Acuerdo de oficio de apertura del período de prueba | 2004 | `acuerdo-oficio-apertura-periodo-prueba-1370` |
| 1371 | Requerimiento de anticipo de gastos de la prueba propuesta | 2004 | `requerimiento-anticipo-gastos-prueba-propuesta-1371` |
| 1372 | Acuerdo de iniciación de oficio de la revisión de actos nulos | 2004 | `acuerdo-iniciacion-oficio-revision-actos-nulos-1372` |
| 1374 | Diligencia de comparecencia en información pública | 2004 | `diligencia-comparecencia-informacion-publica-1374` |
| 1377 | Acuerdo de medidas provisionales en el procedimiento administrativo | 2004 | `acuerdo-medidas-provisionales-procedimiento-1377` |
| 1380 | Acuerdo de medidas provisionales urgentes | 2004 | `acuerdo-medidas-provisionales-urgentes-1380` |
| 1400 | Resolución motivada que deniega el acceso a archivos y registros | 2004 | `resolucion-motivada-deniega-acceso-archivos-registros-1400` |
| 1404 | Resolución que termina el procedimiento por desistimiento del interesado | 2004 | `resolucion-termina-procedimiento-desistimiento-1404` |
| 1406 | Notificación del desistimiento a los demás interesados | 2004 | `notificacion-desistimiento-demas-interesados-1406` |
| 1407 | Diligencia de desistimiento por comparecencia personal | 2004 | `diligencia-desistimiento-comparecencia-personal-1407` |
| 1408 | Acuerdo de suspensión de la ejecución en la revisión de actos nulos | 2004 | `acuerdo-suspension-ejecucion-revision-actos-nulos-1408` |
| 1409 | Resolución que termina el procedimiento por renuncia del interesado | 2004 | `resolucion-termina-procedimiento-renuncia-interesado-1409` |
| 1419 | Requerimiento de pago anticipado de los gastos de la ejecución subsidiaria | 2004 | `requerimiento-pago-anticipado-gastos-ejecucion-1419` |
| 1420 | Requerimiento de subsanación de defectos en un trámite | 2004 | `requerimiento-subsanacion-defectos-tramite-1420` |
| 1422 | Emplazamiento al trámite de audiencia previo a la propuesta de resolución | 2004 | `emplazamiento-tramite-audiencia-previo-propuesta-1422` |
| 1423 | Diligencia de alegaciones por comparecencia personal en la audiencia | 2004 | `diligencia-alegaciones-comparecencia-personal-audiencia-1423` |
| 1426 | Iniciación del procedimiento por petición razonada de otros órganos (acuerdo) | 2004 | `iniciacion-procedimiento-peticion-razonada-otros-organos-1426` |
| 1427 | Acuerdo que deniega iniciar el procedimiento | 2004 | `acuerdo-deniega-iniciar-procedimiento-1427` |
| 1428 | Requerimiento de información en la información previa | 2004 | `requerimiento-informacion-informacion-previa-1428` |
| 1429 | Acuerdo de iniciación del procedimiento | 2004 | `acuerdo-iniciacion-procedimiento-1429` |
| 1906 | Notificar la denegación de prórroga por necesidad de traslado | 2004 | `notificar-denegacion-prorroga-necesidad-traslado-1906` |

## Contratos, escrituras y documentos (9)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 86 | Modelo genérico de alegaciones | 2018 | `modelo-generico-alegaciones-86` |
| 140 | Pedir la notificación telemática en un expediente administrativo | 2017 | `pedir-notificacion-telematica-expediente-administrativo-140` |
| 285 | Otorgar representación ante la Administración | 2015 | `otorgar-representacion-ante-administracion-285` |
| 604 | Declaración responsable general | 2010 | `declaracion-responsable-general-604` |
| 605 | Comunicación a la Administración del ejercicio de actividades | 2010 | `comunicacion-administracion-ejercicio-actividades-605` |
| 1329 | Modelo de certificado de silencio administrativo del órgano competente | 2004 | `modelo-certificado-silencio-administrativo-organo-1329` |
| 1379 | Acuerdo de medidas provisionales con trámite de audiencia | 2004 | `acuerdo-medidas-provisionales-tramite-audiencia-1379` |
| 1388 | Solicitud general del ciudadano para hacer valer sus derechos ante la Administración | 2004 | `solicitud-general-ciudadano-hacer-valer-derechos-ante-1388` |
| 1876 | Convenio con la Administración como alternativa al contencioso | 2004 | `convenio-administracion-como-alternativa-contencioso-1876` |

## Comunicaciones, requerimientos y reclamaciones (27)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 113 | Denuncia de un particular para que se inicie un procedimiento administrativo | 2018 | `denuncia-particular-inicie-procedimiento-administrativo-113` |
| 290 | Requerimiento al inquilino sobre causas de posposición ante la prórroga por necesidad | 2015 | `requerimiento-inquilino-sobre-causas-posposicion-ante-290` |
| 291 | Reclamación entre propietarios por daños en una vivienda | 2015 | `reclamacion-entre-propietarios-danos-vivienda-291` |
| 347 | Reclamación específica de información y participación (en catalán, modelo 1) | 2013 | `reclamacion-especifica-informacion-participacion-catalan-347` |
| 348 | Requerimiento por incumplir la estimación (información y participación) (en catalán) | 2013 | `requerimiento-incumplir-estimacion-informacion-348` |
| 352 | Reclamación específica de información y participación (en catalán, modelo 2) | 2013 | `reclamacion-especifica-informacion-participacion-catalan-352` |
| 395 | Requerimiento por incumplir la estimación (información y participación) | 2013 | `requerimiento-incumplir-estimacion-informacion-395` |
| 397 | Reclamación específica por derechos de información y participación | 2013 | `reclamacion-especifica-derechos-informacion-397` |
| 721 | Requerimiento para que cese una vía de hecho (Castilla-La Mancha) | 2009 | `requerimiento-cese-via-hecho-castilla-mancha-721` |
| 733 | Requerimiento para que cese una vía de hecho (Castilla y León) | 2009 | `requerimiento-cese-via-hecho-castilla-leon-733` |
| 754 | Requerimiento para que cese una vía de hecho (Galicia) | 2009 | `requerimiento-cese-via-hecho-galicia-754` |
| 768 | Requerimiento para que cese una vía de hecho (Comunidad Valenciana) | 2009 | `requerimiento-cese-via-hecho-comunidad-valenciana-768` |
| 804 | Requerimiento para que cese una vía de hecho (Navarra) | 2009 | `requerimiento-cese-via-hecho-navarra-804` |
| 861 | Requerimiento para que cese una vía de hecho (Comunidad de Madrid) | 2009 | `requerimiento-cese-via-hecho-comunidad-madrid-861` |
| 1037 | Requerimiento vecinal a la entidad local antes de actuar por sustitución (Aragón) | 2008 | `requerimiento-vecinal-entidad-local-antes-actuar-1037` |
| 1038 | Requerimiento vecinal a la entidad local antes de acudir a los tribunales por sustitución (Galicia) | 2008 | `requerimiento-vecinal-entidad-local-antes-acudir-1038` |
| 1170 | Requerimiento vecinal a la entidad local antes de actuar por sustitución (Navarra) | 2008 | `requerimiento-vecinal-entidad-local-antes-actuar-1170` |
| 1173 | Requerimiento vecinal previo a acudir a tribunales por sustitución (Andalucía) | 2008 | `requerimiento-vecinal-previo-acudir-tribunales-1173` |
| 1175 | Requerimiento vecinal a la entidad local antes de actuar por sustitución (Cataluña) | 2008 | `requerimiento-vecinal-entidad-local-antes-actuar-1175` |
| 1176 | Requerimiento vecinal a la entidad local antes de acudir a los tribunales por sustitución | 2008 | `requerimiento-vecinal-entidad-local-antes-acudir-1176` |
| 1207 | Requerimiento de subsanación de defectos | 2008 | `requerimiento-subsanacion-defectos-1207` |
| 1352 | Requerimiento de subsanación o mejora de la solicitud | 2004 | `requerimiento-subsanacion-mejora-solicitud-1352` |
| 1369 | Designación por el interesado de técnicos que le asistan en la prueba | 2004 | `designacion-interesado-tecnicos-le-asistan-prueba-1369` |
| 1386 | Comunicación a los interesados que puedan resultar afectados | 2004 | `comunicacion-interesados-puedan-resultar-afectados-1386` |
| 1389 | Requerimiento de subsanación de la representación | 2004 | `requerimiento-subsanacion-representacion-1389` |
| 1416 | Requerimiento previo a multas coercitivas | 2004 | `requerimiento-previo-multas-coercitivas-1416` |
| 1417 | Requerir antes de la ejecución subsidiaria | 2004 | `requerir-antes-ejecucion-subsidiaria-1417` |

## Otros (22)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 40 | Actuaciones previas al procedimiento administrativo | 2021 | `actuaciones-previas-procedimiento-administrativo-40` |
| 84 | Declarar qué datos de la oferta son confidenciales | 2018 | `declarar-datos-oferta-son-confidenciales-84` |
| 180 | Convenio de un Ayuntamiento: contenido mínimo | 2017 | `convenio-ayuntamiento-contenido-minimo-180` |
| 451 | Asistencia jurídica gratuita: impugnar la denegación ante la Comisión | 2012 | `asistencia-juridica-gratuita-impugnar-denegacion-ante-451` |
| 595 | Defecto de tramitación: denegación de la prueba solicitada | 2011 | `defecto-tramitacion-denegacion-prueba-solicitada-595` |
| 631 | Identificar el órgano que resuelve el procedimiento | 2010 | `identificar-organo-resuelve-procedimiento-631` |
| 679 | Levantar la suspensión tras resolverse el expediente comunitario | 2010 | `levantar-suspension-tras-resolverse-expediente-679` |
| 699 | Edicto de ejecución subsidiaria para desalojar personas y enseres de un inmueble | 2010 | `edicto-ejecucion-subsidiaria-desalojar-personas-enseres-699` |
| 811 | Pedir la terminación del procedimiento por falta de objeto (País Vasco, en euskera) | 2009 | `pedir-terminacion-procedimiento-falta-objeto-pais-vasco-811` |
| 828 | Requerimiento para que cese una vía de hecho (País Vasco, en euskera) | 2009 | `requerimiento-cese-via-hecho-pais-vasco-euskera-828` |
| 830 | Reclamación previa por no ejecutar una prestación (País Vasco, en euskera) | 2009 | `reclamacion-previa-no-ejecutar-prestacion-pais-vasco-830` |
| 850 | Requerimiento para que cese una vía de hecho (Cataluña, en catalán) | 2009 | `requerimiento-cese-via-hecho-cataluna-catalan-850` |
| 1105 | Remisión de información por el órgano requerido | 2008 | `remision-informacion-organo-requerido-1105` |
| 1160 | Respuesta a las alegaciones de información pública del expediente | 2008 | `respuesta-alegaciones-informacion-publica-expediente-1160` |
| 1316 | Declaración de oficio de tramitación urgente del procedimiento | 2004 | `declaracion-oficio-tramitacion-urgente-procedimiento-1316` |
| 1353 | Acuse de recibo de solicitudes y escritos de los interesados | 2004 | `acuse-recibo-solicitudes-escritos-interesados-1353` |
| 1366 | Declaración de pérdida del trámite por transcurso del plazo sin actuar | 2004 | `declaracion-perdida-tramite-transcurso-plazo-sin-actuar-1366` |
| 1368 | Puesta de manifiesto del expediente para resolver cuestiones conexas no planteadas | 2004 | `puesta-manifiesto-expediente-resolver-cuestiones-conexas-1368` |
| 1373 | Remisión a los demás interesados del escrito de renuncia | 2004 | `remision-demas-interesados-escrito-renuncia-1373` |
| 1383 | Orden superior de iniciar un expediente | 2004 | `orden-superior-iniciar-expediente-1383` |
| 1402 | Advertir de la caducidad por causa del interesado | 2004 | `advertir-caducidad-causa-interesado-1402` |
| 1424 | Anuncio de información pública del expediente | 2004 | `anuncio-informacion-publica-expediente-1424` |
