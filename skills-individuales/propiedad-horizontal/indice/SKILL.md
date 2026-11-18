---
name: indice
description: "Índice de los 78 formularios de propiedad horizontal (juntas, actas, impugnación de acuerdos, cuotas, obras, actividades molestas). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Propiedad horizontal: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/propiedad-horizontal:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (15)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 7 | Demanda contra la comunidad para obras de accesibilidad: instalación de ascensor | 2025 | `demanda-contra-comunidad-obras-accesibilidad-instalacion-7` |
| 71 | Demanda por obras no autorizadas en la comunidad de propietarios | 2023 | `demanda-obras-no-autorizadas-comunidad-propietarios-71` |
| 306 | Demanda verbal contra la comunidad por indemnización al cesar al administrador | 2020 | `demanda-verbal-contra-comunidad-indemnizacion-cesar-306` |
| 315 | Demanda ordinaria de constitución de edificio en propiedad horizontal | 2020 | `demanda-ordinaria-constitucion-edificio-propiedad-315` |
| 359 | Demanda contra el promotor por impugnación del título constitutivo de propiedad horizontal | 2019 | `demanda-contra-promotor-impugnacion-titulo-constitutivo-359` |
| 365 | Demanda verbal de división de cosa común y constitución en propiedad horizontal | 2019 | `demanda-verbal-division-cosa-comun-constitucion-365` |
| 395 | Demanda de la comunidad contra un propietario para acceder a su vivienda o local | 2019 | `demanda-comunidad-contra-propietario-acceder-vivienda-395` |
| 420 | Demanda de daños entre comunidades de propietarios en elementos comunes | 2018 | `demanda-danos-entre-comunidades-propietarios-elementos-420` |
| 503 | Demanda contra propietario por aire acondicionado no consentido en patio interior | 2017 | `demanda-contra-propietario-aire-acondicionado-no-503` |
| 609 | Demanda de impugnación de acuerdos de la junta lesivos para la comunidad | 2016 | `demanda-impugnacion-acuerdos-junta-lesivos-comunidad-609` |
| 842 | Demanda de la comunidad contra un comunero por alterar elementos comunes | 2015 | `demanda-comunidad-contra-comunero-alterar-elementos-842` |
| 1245 | Demanda de repetición del antiguo propietario | 2013 | `demanda-repeticion-antiguo-propietario-1245` |
| 1329 | Cesación de actividad e indemnización por perjuicios contra propietario | 2013 | `cesacion-actividad-e-indemnizacion-perjuicios-contra-1329` |
| 1339 | Cesación de actividad contra propietario (general) | 2013 | `cesacion-actividad-contra-propietario-general-1339` |
| 1440 | Demanda de cesación de actividades prohibidas con indemnización de daños | 2013 | `demanda-cesacion-actividades-prohibidas-indemnizacion-1440` |

## Recursos e impugnaciones (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1289 | Impugnación de acuerdo de junta lesivo o perjudicial | 2013 | `impugnacion-acuerdo-junta-lesivo-perjudicial-1289` |
| 1334 | Impugnación de acuerdo de junta contrario a la ley o a los estatutos | 2013 | `impugnacion-acuerdo-junta-contrario-ley-estatutos-1334` |

## Contestaciones, oposiciones y alegaciones (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 5 | Contestación a la demanda por alteración de elementos comunes en propiedad horizontal | 2025 | `contestacion-demanda-alteracion-elementos-comunes-5` |
| 603 | Oposición a la solicitud de cesación de actividades prohibidas, dañosas o ilícitas | 2016 | `oposicion-solicitud-cesacion-actividades-prohibidas-603` |
| 1221 | Contestación a reclamación de cuotas impagadas por el anterior propietario | 2013 | `contestacion-reclamacion-cuotas-impagadas-anterior-1221` |
| 1371 | Contestación del propietario no usuario a demanda de cesación de actividades prohibidas | 2013 | `contestacion-propietario-no-usuario-demanda-cesacion-1371` |
| 1403 | Contestación del usuario a demanda de cesación de actividades prohibidas | 2013 | `contestacion-usuario-demanda-cesacion-actividades-1403` |
| 1416 | Contestación al requerimiento de cesar actividades molestas | 2013 | `contestacion-requerimiento-cesar-actividades-molestas-1416` |

## Solicitudes y expedientes (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 104 | Prueba pericial anticipada en propiedad horizontal antes del proceso | 2022 | `prueba-pericial-anticipada-propiedad-horizontal-antes-104` |
| 1365 | Permiso para instalaciones provisionales en elementos comunes por obra privativa | 2013 | `permiso-instalaciones-provisionales-elementos-comunes-1365` |
| 1388 | Convocatoria de junta solicitada por comuneros al presidente | 2013 | `convocatoria-junta-solicitada-comuneros-presidente-1388` |
| 1406 | Solicitud de obras privadas en elementos comunes | 2013 | `solicitud-obras-privadas-elementos-comunes-1406` |
| 1412 | Solicitud de instalación individual de telecomunicaciones | 2013 | `solicitud-instalacion-individual-telecomunicaciones-1412` |
| 1413 | Solicitud de acceso a servicios comunes de telecomunicaciones | 2013 | `solicitud-acceso-servicios-comunes-telecomunicaciones-1413` |
| 1437 | Autorización de entrada en elemento privativo: solicitud | 2013 | `autorizacion-entrada-elemento-privativo-solicitud-1437` |

## Escritos de trámite (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 604 | Propietario pide al presidente que requiera a otro el cese de actividades prohibidas | 2016 | `propietario-pide-presidente-requiera-otro-cese-604` |
| 1104 | Otrosí: acreditación de pago de cantidades debidas por un comunero | 2013 | `otrosi-acreditacion-pago-cantidades-debidas-comunero-1104` |
| 1345 | Otrosí: cesación inmediata de la actividad | 2013 | `otrosi-cesacion-inmediata-actividad-1345` |
| 1347 | Declinatoria por mediación pactada entre comuneros y comunidad | 2013 | `declinatoria-mediacion-pactada-entre-comuneros-comunidad-1347` |
| 1394 | Comunero pide requerir a otro que derribe lo construido en elementos comunes | 2013 | `comunero-pide-requerir-otro-derribe-lo-construido-1394` |

## Actos y resoluciones de la Administración o del órgano judicial (22)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 101 | Certificado de estar al corriente de pago en la comunidad de propietarios | 2022 | `certificado-estar-corriente-pago-comunidad-propietarios-101` |
| 307 | Certificado del acuerdo de la junta de ejercitar la acción de cesación | 2020 | `certificado-acuerdo-junta-ejercitar-accion-cesacion-307` |
| 557 | Acta que acuerda desafectar elementos comunes para venderlos | 2016 | `acta-acuerda-desafectar-elementos-comunes-venderlos-557` |
| 605 | Requerimiento al presidente para convocar junta extraordinaria y acordar acciones judiciales | 2016 | `requerimiento-presidente-convocar-junta-extraordinaria-605` |
| 606 | Acta de la junta que aprueba la acción de cesación por actividades prohibidas | 2016 | `acta-junta-aprueba-accion-cesacion-actividades-606` |
| 823 | Permiso para entrar en un elemento privativo | 2015 | `permiso-entrar-elemento-privativo-823` |
| 1173 | Acta de constitución de comunidad de propietarios con subcomunidades | 2015 | `acta-constitucion-comunidad-propietarios-subcomunidades-1173` |
| 1174 | Citación de los comuneros a la reunión de la comunidad | 2015 | `citacion-comuneros-reunion-comunidad-1174` |
| 1175 | Acta de junta ordinaria o extraordinaria de propietarios | 2015 | `acta-junta-ordinaria-extraordinaria-propietarios-1175` |
| 1206 | Acta de junta constituida sin convocatoria previa | 2013 | `acta-junta-constituida-sin-convocatoria-previa-1206` |
| 1214 | Acta de aprobación de ascensor | 2013 | `acta-aprobacion-ascensor-1214` |
| 1219 | Acuerdo de junta autorizando al presidente a integrarse en un complejo inmobiliario privado | 2013 | `acuerdo-junta-autorizando-presidente-integrarse-complejo-1219` |
| 1223 | Acta de junta de comunidad agrupada con acuerdos de mayoría cualificada | 2013 | `acta-junta-comunidad-agrupada-acuerdos-mayoria-1223` |
| 1234 | Certificar el acta de la junta de propietarios | 2013 | `certificar-acta-junta-propietarios-1234` |
| 1379 | Notificación del acta a los propietarios presentes | 2013 | `notificacion-acta-propietarios-presentes-1379` |
| 1380 | Notificación de convocatoria de junta a un comunero | 2013 | `notificacion-convocatoria-junta-comunero-1380` |
| 1382 | Notificación del acta a los propietarios ausentes | 2013 | `notificacion-acta-propietarios-ausentes-1382` |
| 1387 | Acta de la junta constituyente | 2013 | `acta-junta-constituyente-1387` |
| 1408 | Autorización de acceso a servicios comunes de telecomunicaciones | 2013 | `autorizacion-acceso-servicios-comunes-telecomunicaciones-1408` |
| 1410 | Autorización de instalación individual de telecomunicaciones | 2013 | `autorizacion-instalacion-individual-telecomunicaciones-1410` |
| 1436 | Junta de comunidad agrupada: acta | 2013 | `junta-comunidad-agrupada-acta-1436` |
| 1441 | Acta de aprobación de obras y derrama extraordinaria | 2013 | `acta-aprobacion-obras-derrama-extraordinaria-1441` |

## Contratos, escrituras y documentos (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 56 | Contrato de la comunidad con instaladora de paneles solares y gestión de la subvención | 2023 | `contrato-comunidad-instaladora-paneles-solares-gestion-56` |
| 69 | Cláusula informativa de videovigilancia en comunidades de propietarios | 2023 | `clausula-informativa-videovigilancia-comunidades-69` |
| 70 | Respuesta de la comunidad al derecho de acceso sobre su videovigilancia | 2023 | `respuesta-comunidad-derecho-acceso-sobre-videovigilancia-70` |
| 137 | Contrato de acceso a datos entre la comunidad y el administrador de fincas | 2021 | `contrato-acceso-datos-entre-comunidad-administrador-137` |
| 558 | Estatutos de la comunidad de monte vecinal en mano común | 2016 | `estatutos-comunidad-monte-vecinal-mano-comun-558` |
| 1376 | Estatutos de la comunidad (documento) | 2013 | `estatutos-comunidad-documento-1376` |

## Comunicaciones, requerimientos y reclamaciones (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 89 | Convocatoria de la junta general ordinaria de propietarios (Cataluña) | 2023 | `convocatoria-junta-general-ordinaria-propietarios-89` |
| 1176 | Aviso a la comunidad de obra en vivienda o local | 2015 | `aviso-comunidad-obra-vivienda-local-1176` |
| 1211 | Convocatoria de junta extraordinaria para instalar ascensor | 2013 | `convocatoria-junta-extraordinaria-instalar-ascensor-1211` |
| 1212 | Convocatoria de junta extraordinaria para reclamar cuotas atrasadas | 2013 | `convocatoria-junta-extraordinaria-reclamar-cuotas-1212` |
| 1215 | Convocatoria de junta extraordinaria sobre telecomunicaciones | 2013 | `convocatoria-junta-extraordinaria-sobre-1215` |
| 1229 | Convocatoria de junta extraordinaria para ejercitar la acción de cesación | 2013 | `convocatoria-junta-extraordinaria-ejercitar-accion-1229` |
| 1232 | Convocatoria de nueva junta por falta de quórum | 2013 | `convocatoria-nueva-junta-falta-quorum-1232` |
| 1375 | Convocar la junta constituyente por los propietarios | 2013 | `convocar-junta-constituyente-propietarios-1375` |
| 1377 | Convocatoria de la junta constituyente por el promotor | 2013 | `convocatoria-junta-constituyente-promotor-1377` |
| 1402 | Aviso de obras privadas en elementos comunes | 2013 | `aviso-obras-privadas-elementos-comunes-1402` |
| 1409 | Denegación de instalación individual de telecomunicaciones | 2013 | `denegacion-instalacion-individual-telecomunicaciones-1409` |

## Otros (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 825 | Constitución en comunidad de propietarios de un complejo inmobiliario privado | 2015 | `constitucion-comunidad-propietarios-complejo-825` |
| 1235 | Comunidad agrupada: estatutos | 2013 | `comunidad-agrupada-estatutos-1235` |
| 1433 | Constitución en agrupación de comunidades de propietarios | 2013 | `constitucion-agrupacion-comunidades-propietarios-1433` |
| 1434 | Constituirse en comunidad de propietarios | 2013 | `constituirse-comunidad-propietarios-1434` |
