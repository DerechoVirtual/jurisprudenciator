---
name: indice
description: "Índice de los 343 formularios de escritos procesales civiles (demanda, contestación, prueba, vista, recusación, encabezamientos). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Escritos procesales civiles: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Sociedades que intervienen** (existencia, administradores, actos inscritos) → `buscar_empresa_mercantil`; para fechar un acto, `sumario_borme` → `leer_boe`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/escritos-procesales-civiles:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (23)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 34 | Demanda en procedimiento testigo | 2024 | `demanda-procedimiento-testigo-34` |
| 65 | Demanda de condena a una obligación de hacer | 2023 | `demanda-condena-obligacion-hacer-65` |
| 84 | Demanda para reconocer la condición de beneficiario de un plan de pensiones y reclamar prestaciones | 2023 | `demanda-reconocer-condicion-beneficiario-plan-pensiones-84` |
| 167 | Demanda de reclamación de premio de lotería | 2021 | `demanda-reclamacion-premio-loteria-167` |
| 190 | Demanda de cumplimiento de un compromiso de hacer | 2021 | `demanda-cumplimiento-compromiso-hacer-190` |
| 277 | Demanda verbal de repetición de cuotas comunitarias (art. 9.1.i LPH) | 2020 | `demanda-verbal-repeticion-cuotas-comunitarias-art-9-1-i-277` |
| 295 | Demanda verbal de reembolso del billete por vuelo cancelado en estado de alarma | 2020 | `demanda-verbal-reembolso-billete-vuelo-cancelado-estado-295` |
| 324 | Demanda ordinaria por gestión de negocios ajenos | 2020 | `demanda-ordinaria-gestion-negocios-ajenos-324` |
| 412 | Demanda de saneamiento por gravámenes ocultos | 2018 | `demanda-saneamiento-gravamenes-ocultos-412` |
| 415 | Saneamiento por evicción: demanda | 2018 | `saneamiento-eviccion-demanda-415` |
| 457 | Demanda con prueba electrónica (WhatsApp) | 2018 | `demanda-prueba-electronica-whatsapp-457` |
| 523 | Demanda de reclamación de hacer | 2016 | `demanda-reclamacion-hacer-523` |
| 525 | Demanda de nulidad por simulación y, subsidiariamente, fraude de acreedores | 2016 | `demanda-nulidad-simulacion-subsidiariamente-fraude-525` |
| 611 | Demanda sucinta en juicio verbal | 2016 | `demanda-sucinta-juicio-verbal-611` |
| 639 | Exequatur: demanda | 2015 | `exequatur-demanda-639` |
| 843 | Reconvención en juicio verbal: demanda reconvencional | 2015 | `reconvencion-juicio-verbal-demanda-reconvencional-843` |
| 1030 | Acción de cesación: modelo general | 2013 | `accion-cesacion-modelo-general-1030` |
| 1033 | Acción de cesación con devolución de cantidades cobradas (general) | 2013 | `accion-cesacion-devolucion-cantidades-cobradas-general-1033` |
| 1036 | Acción de retractación: modelo general | 2013 | `accion-retractacion-modelo-general-1036` |
| 1164 | Demanda ordinaria por acción derivada de relaciones de vecindad | 2015 | `demanda-ordinaria-accion-derivada-relaciones-vecindad-1164` |
| 1237 | Demanda posesoria para paralizar obras | 2013 | `demanda-posesoria-paralizar-obras-1237` |
| 1455 | Demanda de nulidad matrimonial por exclusión total | 2014 | `demanda-nulidad-matrimonial-exclusion-total-1455` |
| 1457 | Demanda de nulidad matrimonial por defecto de forma | 2014 | `demanda-nulidad-matrimonial-defecto-forma-1457` |

## Recursos e impugnaciones (10)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 404 | Impugnación por el solicitante de la denegación de justicia gratuita | 2019 | `impugnacion-solicitante-denegacion-justicia-gratuita-404` |
| 851 | Impugnar un documento privado aportado por vía telemática | 2013 | `impugnar-documento-privado-aportado-via-telematica-851` |
| 894 | Impugnación del valor probatorio de documento público presentado por vía telemática | 2013 | `impugnacion-valor-probatorio-documento-publico-894` |
| 896 | Impugnación de la resolución que reconoce la justicia gratuita, ante el órgano judicial | 2013 | `impugnacion-resolucion-reconoce-justicia-gratuita-ante-896` |
| 968 | Impugnar el valor probatorio de un documento público | 2013 | `impugnar-valor-probatorio-documento-publico-968` |
| 979 | Impugnación de documentos presentados fuera del momento inicial | 2013 | `impugnacion-documentos-presentados-fuera-momento-inicial-979` |
| 983 | Oponerse a preguntas del interrogatorio | 2013 | `oponerse-preguntas-interrogatorio-983` |
| 1001 | Impugnar copias reprográficas | 2013 | `impugnar-copias-reprograficas-1001` |
| 1009 | Impugnación de documento privado | 2013 | `impugnacion-documento-privado-1009` |
| 1118 | Impugnar una traducción privada | 2013 | `impugnar-traduccion-privada-1118` |

## Contestaciones, oposiciones y alegaciones (49)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1 | Alegaciones del demandante a las excepciones procesales de la contestación (juicio verbal) | 2026 | `alegaciones-demandante-excepciones-procesales-1` |
| 3 | Alegaciones sobre la prueba propuesta e impugnación de la cuantía (juicio verbal) | 2026 | `alegaciones-sobre-prueba-propuesta-e-impugnacion-cuantia-3` |
| 96 | Contestación y reconvención alegando compensación judicial | 2022 | `contestacion-reconvencion-alegando-compensacion-judicial-96` |
| 169 | Contestación a demanda verbal con allanamiento parcial | 2021 | `contestacion-demanda-verbal-allanamiento-parcial-169` |
| 341 | Oposición del deudor con reconvención | 2019 | `oposicion-deudor-reconvencion-341` |
| 403 | Alegaciones ante el Tribunal de Instancia contra la denegación de justicia gratuita | 2019 | `alegaciones-ante-tribunal-instancia-contra-denegacion-403` |
| 481 | Contestación a la demanda de nulidad por simulación | 2017 | `contestacion-demanda-nulidad-simulacion-481` |
| 496 | Oposición de los interesados | 2017 | `oposicion-interesados-496` |
| 524 | Contestación oponiendo prescripción de la acción | 2016 | `contestacion-oponiendo-prescripcion-accion-524` |
| 527 | Contestación oponiendo litispendencia | 2016 | `contestacion-oponiendo-litispendencia-527` |
| 575 | Oposición a la apreciación de oficio de falta de competencia objetiva | 2016 | `oposicion-apreciacion-oficio-falta-competencia-objetiva-575` |
| 616 | Alegaciones del demandante frente a la objeción de que la cantidad reclamada es incorrecta | 2015 | `alegaciones-demandante-frente-objecion-cantidad-616` |
| 703 | Alegaciones del solicitante: su incomparecencia obedeció a justa causa | 2015 | `alegaciones-solicitante-incomparecencia-obedecio-justa-703` |
| 710 | Alegaciones de los interesados | 2015 | `alegaciones-interesados-710` |
| 715 | Contestar la reconvención en juicio verbal | 2015 | `contestar-reconvencion-juicio-verbal-715` |
| 721 | Contestación a la demanda verbal con solicitud de vista | 2015 | `contestacion-demanda-verbal-solicitud-vista-721` |
| 740 | Alegaciones del solicitante frente a la posible falta de competencia objetiva del Juez | 2015 | `alegaciones-solicitante-frente-posible-falta-competencia-740` |
| 761 | Alegaciones del solicitante sobre la falta de competencia territorial del juez | 2015 | `alegaciones-solicitante-sobre-falta-competencia-761` |
| 764 | Oposición de los interesados con paso a contencioso (plazo para cumplir una obligación) | 2015 | `oposicion-interesados-paso-contencioso-plazo-cumplir-764` |
| 765 | Alegaciones del solicitante sobre la falta de competencia territorial del LAJ | 2015 | `alegaciones-solicitante-sobre-falta-competencia-765` |
| 770 | Alegaciones del solicitante sobre la falta de competencia objetiva del LAJ | 2015 | `alegaciones-solicitante-sobre-falta-competencia-objetiva-770` |
| 784 | Alegaciones del interesado sobre actuaciones posteriores a la comparecencia | 2015 | `alegaciones-interesado-sobre-actuaciones-posteriores-784` |
| 834 | Oposición del interesado a las operaciones divisorias | 2013 | `oposicion-interesado-operaciones-divisorias-834` |
| 929 | Oposición del demandante en la audiencia previa a la excepción de inadecuación de procedimiento | 2013 | `oposicion-demandante-audiencia-previa-excepcion-929` |
| 956 | Contestación a la impugnación de sentencia | 2013 | `contestacion-impugnacion-sentencia-956` |
| 958 | Contestar a la demanda en juicio verbal | 2013 | `contestar-demanda-juicio-verbal-958` |
| 985 | Contestar a la reconvención implícita por compensación o nulidad: modelo general | 2013 | `contestar-reconvencion-implicita-compensacion-nulidad-985` |
| 988 | Reconvención por otrosí | 2013 | `reconvencion-otrosi-988` |
| 989 | Alegaciones sobre acumulación de acciones en la audiencia previa | 2013 | `alegaciones-sobre-acumulacion-acciones-audiencia-previa-989` |
| 993 | Alegaciones complementarias y de aclaración | 2013 | `alegaciones-complementarias-aclaracion-993` |
| 995 | Alegar demanda o contestación defectuosa en la audiencia previa | 2013 | `alegar-demanda-contestacion-defectuosa-audiencia-previa-995` |
| 996 | Excepciones procesales alegadas en la audiencia previa del ordinario | 2013 | `excepciones-procesales-alegadas-audiencia-previa-996` |
| 1043 | Alegaciones del demandante sobre cuestiones procesales | 2013 | `alegaciones-demandante-sobre-cuestiones-procesales-1043` |
| 1046 | Alegaciones a la oposición: modelo general | 2013 | `alegaciones-oposicion-modelo-general-1046` |
| 1069 | Alegaciones sobre la competencia del Tribunal Supremo en la admisión | 2013 | `alegaciones-sobre-competencia-tribunal-supremo-admision-1069` |
| 1085 | Oposición a la impugnación del reconocimiento de justicia gratuita | 2013 | `oposicion-impugnacion-reconocimiento-justicia-gratuita-1085` |
| 1092 | Alegaciones sobre la acumulación de procesos | 2013 | `alegaciones-sobre-acumulacion-procesos-1092` |
| 1124 | Oponerse a la recusación de jueces y magistrados: modelo general | 2013 | `oponerse-recusacion-jueces-magistrados-modelo-general-1124` |
| 1143 | Contestación del propietario a la comunidad: abuso de derecho | 2013 | `contestacion-propietario-comunidad-abuso-derecho-1143` |
| 1204 | Alegaciones a la solicitud de suspensión | 2013 | `alegaciones-solicitud-suspension-1204` |
| 1261 | Contestar a la denegación de prórroga | 2013 | `contestar-denegacion-prorroga-1261` |
| 1283 | Contestación al requerimiento para liquidar impuestos | 2013 | `contestacion-requerimiento-liquidar-impuestos-1283` |
| 1333 | Contestación a demanda de impugnación de acuerdo lesivo o perjudicial | 2013 | `contestacion-demanda-impugnacion-acuerdo-lesivo-1333` |
| 1343 | Contestación a demanda de impugnación de acuerdo contrario a la ley o los estatutos | 2013 | `contestacion-demanda-impugnacion-acuerdo-contrario-ley-1343` |
| 1397 | Contestación del propietario que construyó en zona común | 2013 | `contestacion-propietario-construyo-zona-comun-1397` |
| 1461 | Contestación a la demanda con excepción de cosa juzgada | 2014 | `contestacion-demanda-excepcion-cosa-juzgada-1461` |
| 1479 | Contestación a demanda arbitral por falta de validez del convenio | 2014 | `contestacion-demanda-arbitral-falta-validez-convenio-1479` |
| 1481 | Contestación a demanda arbitral sobre el fondo | 2014 | `contestacion-demanda-arbitral-sobre-fondo-1481` |
| 1491 | Contestación a la reconvención en arbitraje de consumo | 2014 | `contestacion-reconvencion-arbitraje-consumo-1491` |

## Solicitudes y expedientes (85)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 2 | Proposición de prueba y citación de testigos o peritos a la vista del juicio verbal | 2026 | `proposicion-prueba-citacion-testigos-peritos-vista-2` |
| 45 | Solicitar la celebración de la vista por videoconferencia | 2024 | `solicitar-celebracion-vista-videoconferencia-45` |
| 54 | Solicitud de amparo al colegio de la abogacía por un letrado | 2023 | `solicitud-amparo-colegio-abogacia-letrado-54` |
| 134 | Determinación de la cantidad líquida de una sentencia con reserva de liquidación | 2022 | `determinacion-cantidad-liquida-sentencia-reserva-134` |
| 162 | Deducción de testimonios en un procedimiento civil | 2021 | `deduccion-testimonios-procedimiento-civil-162` |
| 265 | Averiguación de domicilio | 2020 | `averiguacion-domicilio-265` |
| 267 | Solicitud del certificado de eficiencia energética del edificio | 2020 | `solicitud-certificado-eficiencia-energetica-edificio-267` |
| 308 | Solicitud de actuación civil urgente durante el estado de alarma por coronavirus | 2020 | `solicitud-actuacion-civil-urgente-durante-estado-alarma-308` |
| 319 | Citación del demandado por edictos | 2020 | `citacion-demandado-edictos-319` |
| 401 | Suspensión del procedimiento por solicitud de justicia gratuita ante el LAJ | 2019 | `suspension-procedimiento-solicitud-justicia-gratuita-401` |
| 411 | Solicitud de declaración de mejor fortuna a la Comisión de Asistencia Jurídica Gratuita | 2018 | `solicitud-declaracion-mejor-fortuna-comision-asistencia-411` |
| 413 | Notificación al vendedor de la demanda de evicción | 2018 | `notificacion-vendedor-demanda-eviccion-413` |
| 476 | Nombramiento de traductor | 2017 | `nombramiento-traductor-476` |
| 494 | Impulso procesal en el proceso declarativo | 2017 | `impulso-procesal-proceso-declarativo-494` |
| 628 | Reconocimiento en España de sentencia rusa (Convenio España-URSS de 1990) | 2016 | `reconocimiento-espana-sentencia-rusa-convenio-espana-628` |
| 643 | Certificación del art. 15 del Convenio de La Haya de 1980 | 2015 | `certificacion-art-15-convenio-haya-1980-643` |
| 680 | Citación judicial de testigos a la comparecencia | 2015 | `citacion-judicial-testigos-comparecencia-680` |
| 686 | Nombramiento de tercer perito | 2015 | `nombramiento-tercer-perito-686` |
| 689 | Revocación o cese de nombramientos | 2015 | `revocacion-cese-nombramientos-689` |
| 690 | Exhibición de libros de quienes deben llevar contabilidad | 2015 | `exhibicion-libros-quienes-deben-llevar-contabilidad-690` |
| 696 | Convocatoria de la asamblea general de obligacionistas | 2015 | `convocatoria-asamblea-general-obligacionistas-696` |
| 731 | Fijación judicial del plazo para cumplir una obligación | 2015 | `fijacion-judicial-plazo-cumplir-obligacion-731` |
| 737 | Habilitación para comparecer en juicio por imposibilidad de hecho | 2015 | `habilitacion-comparecer-juicio-imposibilidad-hecho-737` |
| 746 | Extracción de órganos de donantes vivos | 2015 | `extraccion-organos-donantes-vivos-746` |
| 752 | Defensor del desaparecido | 2015 | `defensor-desaparecido-752` |
| 763 | Caducidad del expediente: solicitud | 2015 | `caducidad-expediente-solicitud-763` |
| 767 | Acumulación de expedientes ante el mismo órgano judicial | 2015 | `acumulacion-expedientes-ante-mismo-organo-judicial-767` |
| 771 | Acumulación de expedientes ante órganos judiciales distintos | 2015 | `acumulacion-expedientes-ante-organos-judiciales-771` |
| 774 | Beneficio de mayoría de edad: solicitud | 2015 | `beneficio-mayoria-edad-solicitud-774` |
| 786 | Suspender al representante del ausente hasta la comparecencia | 2015 | `suspender-representante-ausente-hasta-comparecencia-786` |
| 790 | Nombramiento inmediato de defensor del desaparecido antes de la comparecencia | 2015 | `nombramiento-inmediato-defensor-desaparecido-antes-790` |
| 797 | Habilitación para comparecer en juicio por negativa a representar: inicio del expediente | 2015 | `habilitacion-comparecer-juicio-negativa-representar-797` |
| 798 | Testimonio de la resolución final del expediente para el Registro Civil | 2015 | `testimonio-resolucion-final-expediente-registro-civil-798` |
| 841 | Remisión al tribunal competente de la prueba anticipada practicada | 2015 | `remision-tribunal-competente-prueba-anticipada-841` |
| 853 | Medidas civiles junto con la orden de protección | 2013 | `medidas-civiles-junto-orden-proteccion-853` |
| 859 | Declaración judicial del derecho a justicia gratuita por inactividad del Colegio | 2013 | `declaracion-judicial-derecho-justicia-gratuita-859` |
| 871 | Copia del acta y de la grabación de la vista | 2013 | `copia-acta-grabacion-vista-871` |
| 872 | Presencia en el reconocimiento pericial | 2013 | `presencia-reconocimiento-pericial-872` |
| 877 | Nombramiento de perito tasador | 2013 | `nombramiento-perito-tasador-877` |
| 884 | Aprobación de transacción (general) | 2013 | `aprobacion-transaccion-general-884` |
| 886 | Suspensión del curso del procedimiento principal | 2013 | `suspension-curso-procedimiento-principal-886` |
| 889 | Interrogatorio domiciliario: solicitud | 2013 | `interrogatorio-domiciliario-solicitud-889` |
| 891 | Autorización de entrada en lugar cerrado con auxilio de la fuerza pública | 2013 | `autorizacion-entrada-lugar-cerrado-auxilio-fuerza-891` |
| 902 | Proposición de prueba testifical | 2013 | `proposicion-prueba-testifical-902` |
| 906 | Requerimiento al ocupante para que presente sus títulos | 2013 | `requerimiento-ocupante-presente-titulos-906` |
| 910 | Alzamiento de la suspensión por renuncia al documento controvertido | 2013 | `alzamiento-suspension-renuncia-documento-controvertido-910` |
| 912 | Acumulación a proceso universal: solicitud | 2013 | `acumulacion-proceso-universal-solicitud-912` |
| 928 | Prueba anticipada solicitada por el demandado con el proceso ya iniciado | 2013 | `prueba-anticipada-solicitada-demandado-proceso-ya-928` |
| 940 | Reparación del quebranto en condena de no hacer | 2013 | `reparacion-quebranto-condena-no-hacer-940` |
| 951 | Testimonio de la sentencia: solicitud | 2013 | `testimonio-sentencia-solicitud-951` |
| 954 | Intervención de las partes en el reconocimiento de personas | 2013 | `intervencion-partes-reconocimiento-personas-954` |
| 964 | Cambio de fecha del juicio por enfermedad de parte o coincidencia de señalamientos | 2013 | `cambio-fecha-juicio-enfermedad-parte-coincidencia-964` |
| 966 | Adición a un documento público | 2013 | `adicion-documento-publico-966` |
| 982 | Prueba anticipada solicitada por el demandante con el proceso ya iniciado | 2013 | `prueba-anticipada-solicitada-demandante-proceso-ya-982` |
| 994 | Citación a juicio de personas que aclaren la testifical de personas jurídicas o entidades públicas | 2013 | `citacion-juicio-personas-aclaren-testifical-personas-994` |
| 1006 | Comparecencia del perito en el juicio o vista | 2013 | `comparecencia-perito-juicio-vista-1006` |
| 1007 | Testimonio de documentos públicos no escritos exhibidos ante el LAJ | 2013 | `testimonio-documentos-publicos-no-escritos-exhibidos-1007` |
| 1010 | Concurrencia con la prueba de testigos | 2013 | `concurrencia-prueba-testigos-1010` |
| 1011 | Concurrencia con el reconocimiento pericial | 2013 | `concurrencia-reconocimiento-pericial-1011` |
| 1012 | Concurrencia con el interrogatorio de parte | 2013 | `concurrencia-interrogatorio-parte-1012` |
| 1013 | Designación de perito por el tribunal: solicitud | 2013 | `designacion-perito-tribunal-solicitud-1013` |
| 1021 | Citación a comparecencia para constituir la administración | 2013 | `citacion-comparecencia-constituir-administracion-1021` |
| 1028 | Suspensión del plazo para valorar la pretensión | 2013 | `suspension-plazo-valorar-pretension-1028` |
| 1039 | Exhibición de cosa mueble: petición | 2013 | `exhibicion-cosa-mueble-peticion-1039` |
| 1049 | Comunicación de la pendencia del proceso al rebelde | 2013 | `comunicacion-pendencia-proceso-rebelde-1049` |
| 1066 | Diligencia preliminar: exhibición de cuentas sociales | 2013 | `diligencia-preliminar-exhibicion-cuentas-sociales-1066` |
| 1068 | Diligencia preliminar para concretar los miembros de un grupo de afectados determinables | 2013 | `diligencia-preliminar-concretar-miembros-grupo-afectados-1068` |
| 1070 | Contestación por escrito de preguntas por persona jurídica o entidad pública | 2013 | `contestacion-escrito-preguntas-persona-juridica-entidad-1070` |
| 1081 | Certificación de procedimiento penal en tramitación | 2013 | `certificacion-procedimiento-penal-tramitacion-1081` |
| 1082 | Alzamiento de la suspensión acordada por prejudicialidad civil | 2013 | `alzamiento-suspension-acordada-prejudicialidad-civil-1082` |
| 1091 | Información sobre el estado de las actuaciones | 2013 | `informacion-sobre-estado-actuaciones-1091` |
| 1109 | Venia a otro letrado: solicitud | 2013 | `venia-otro-letrado-solicitud-1109` |
| 1132 | Justicia gratuita solicitada ante el Tribunal | 2013 | `justicia-gratuita-solicitada-ante-tribunal-1132` |
| 1133 | Uso de la lengua castellana: solicitud | 2013 | `uso-lengua-castellana-solicitud-1133` |
| 1182 | Declaración de firmeza de la sentencia: solicitud | 2014 | `declaracion-firmeza-sentencia-solicitud-1182` |
| 1243 | Notificación de sentencia por edictos: solicitud | 2013 | `notificacion-sentencia-edictos-solicitud-1243` |
| 1341 | Relevo de la presidencia: solicitud | 2013 | `relevo-presidencia-solicitud-1341` |
| 1378 | Corrección de errores del acta: solicitud | 2013 | `correccion-errores-acta-solicitud-1378` |
| 1396 | Orden del día: obras comunes de eficiencia energética | 2013 | `orden-dia-obras-comunes-eficiencia-energetica-1396` |
| 1398 | Orden del día: obras de aprovechamiento privativo de eficiencia energética | 2013 | `orden-dia-obras-aprovechamiento-privativo-eficiencia-1398` |
| 1415 | Solicitud de obras urgentes en el inmueble | 2013 | `solicitud-obras-urgentes-inmueble-1415` |
| 1421 | Obras necesarias de accesibilidad del inmueble | 2013 | `obras-necesarias-accesibilidad-inmueble-1421` |
| 1422 | Obras necesarias de conservación del inmueble | 2013 | `obras-necesarias-conservacion-inmueble-1422` |
| 1438 | Autorización de segregación: solicitud | 2013 | `autorizacion-segregacion-solicitud-1438` |
| 1439 | Aprobación de agregación: solicitud | 2013 | `aprobacion-agregacion-solicitud-1439` |

## Escritos de trámite (101)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 32 | Desistimiento del actor y anuncio de extensión de efectos de la sentencia del procedimiento testigo | 2024 | `desistimiento-actor-anuncio-extension-efectos-sentencia-32` |
| 33 | Solicitud del actor de extensión de efectos de la sentencia del procedimiento testigo | 2024 | `solicitud-actor-extension-efectos-sentencia-33` |
| 100 | Propuesta comercial de servicios de administración de fincas | 2022 | `propuesta-comercial-servicios-administracion-fincas-100` |
| 128 | Otrosí de contestación anunciando dictamen pericial (art. 337 LEC) | 2022 | `otrosi-contestacion-anunciando-dictamen-pericial-art-337-128` |
| 326 | Otrosí de la demanda con justicia gratuita: designación judicial de perito | 2020 | `otrosi-demanda-justicia-gratuita-designacion-judicial-326` |
| 394 | Impugnación de la resolución apelada | 2019 | `impugnacion-resolucion-apelada-394` |
| 576 | Declinatoria por competencia objetiva | 2016 | `declinatoria-competencia-objetiva-576` |
| 582 | Escrito del deudor: pasó un mes sin demanda ordinaria del peticionario | 2016 | `escrito-deudor-paso-mes-sin-demanda-ordinaria-582` |
| 587 | Solicitud del demandante para que no se celebre vista en juicio verbal | 2016 | `solicitud-demandante-no-celebre-vista-juicio-verbal-587` |
| 589 | Oposición o conformidad a que una parte renuncie a la vista en juicio verbal | 2016 | `oposicion-conformidad-parte-renuncie-vista-juicio-verbal-589` |
| 590 | Renuncia a la solicitud de vista antes de celebrarse | 2016 | `renuncia-solicitud-vista-antes-celebrarse-590` |
| 624 | Otrosí de la demanda: designación judicial de perito | 2016 | `otrosi-demanda-designacion-judicial-perito-624` |
| 625 | Solicitud del demandante para celebrar vista en juicio verbal | 2016 | `solicitud-demandante-celebrar-vista-juicio-verbal-625` |
| 676 | Citación de interesados u oyentes a la comparecencia | 2015 | `citacion-interesados-u-oyentes-comparecencia-676` |
| 684 | Dictamen del perito nombrado | 2015 | `dictamen-perito-nombrado-684` |
| 685 | Rechazo del cargo por el perito designado con justa causa | 2015 | `rechazo-cargo-perito-designado-justa-causa-685` |
| 687 | Aceptación del cargo por el perito designado | 2015 | `aceptacion-cargo-perito-designado-687` |
| 688 | Requerimiento del LAJ a la persona obligada a exhibir | 2015 | `requerimiento-laj-persona-obligada-exhibir-688` |
| 700 | Autorización del acreedor para retirar lo consignado si el deudor pide su devolución | 2015 | `autorizacion-acreedor-retirar-lo-consignado-si-deudor-700` |
| 720 | Preparación de informe pericial pedida por el demandado | 2015 | `preparacion-informe-pericial-pedida-demandado-720` |
| 756 | Comunicación al Juez de la intención de revocar el consentimiento otorgado judicialmente | 2015 | `comunicacion-juez-intencion-revocar-consentimiento-756` |
| 760 | Alegación de cosa juzgada | 2015 | `alegacion-cosa-juzgada-760` |
| 795 | Presentación del inventario de bienes | 2015 | `presentacion-inventario-bienes-795` |
| 833 | Proposición de prueba en juicio verbal | 2013 | `proposicion-prueba-juicio-verbal-833` |
| 849 | Encabezamiento de escritos posteriores del procurador de una persona física | 2013 | `encabezamiento-escritos-posteriores-procurador-persona-849` |
| 854 | Otrosí: emplazamiento del demandado por auxilio judicial | 2013 | `otrosi-emplazamiento-demandado-auxilio-judicial-854` |
| 857 | Prueba pericial del demandado con justicia gratuita en juicio verbal | 2013 | `prueba-pericial-demandado-justicia-gratuita-juicio-857` |
| 858 | Renuncia a la dirección del asunto, dirigida al cliente | 2013 | `renuncia-direccion-asunto-dirigida-cliente-858` |
| 863 | Documentos del demandado en juicio verbal | 2013 | `documentos-demandado-juicio-verbal-863` |
| 864 | Sustitución en el interrogatorio: propuesta | 2013 | `sustitucion-interrogatorio-propuesta-864` |
| 865 | Admisión de la prueba documental en el juicio o vista | 2013 | `admision-prueba-documental-juicio-vista-865` |
| 868 | Recusar a peritos: modelo general | 2013 | `recusar-peritos-modelo-general-868` |
| 875 | Prueba por filmación, grabación e instrumentos semejantes | 2013 | `prueba-filmacion-grabacion-e-instrumentos-semejantes-875` |
| 887 | Demanda sin procurador: encabezamiento | 2013 | `demanda-sin-procurador-encabezamiento-887` |
| 888 | Personación del deudor alegando falsedad de firma | 2013 | `personacion-deudor-alegando-falsedad-firma-888` |
| 913 | Recusar a jueces y magistrados: modelo general | 2013 | `recusar-jueces-magistrados-modelo-general-913` |
| 926 | Escrito de conclusiones: modelo general | 2013 | `escrito-conclusiones-modelo-general-926` |
| 953 | Reconocimiento judicial: proposición en la comparecencia previa o la vista | 2013 | `reconocimiento-judicial-proposicion-comparecencia-previa-953` |
| 969 | Documentos presentados después de la vista o juicio | 2013 | `documentos-presentados-despues-vista-juicio-969` |
| 970 | Documentos presentados hasta la vista o juicio | 2013 | `documentos-presentados-hasta-vista-juicio-970` |
| 971 | Propuesta de interrogatorio domiciliario | 2013 | `propuesta-interrogatorio-domiciliario-971` |
| 972 | Propuesta de interrogatorio domiciliario por auxilio judicial | 2013 | `propuesta-interrogatorio-domiciliario-auxilio-judicial-972` |
| 973 | Propuesta de interrogatorio de colitigante | 2013 | `propuesta-interrogatorio-colitigante-973` |
| 974 | Propuesta de interrogatorio de la parte contraria | 2013 | `propuesta-interrogatorio-parte-contraria-974` |
| 975 | Propuesta de interrogatorio del titular de la relación jurídica | 2013 | `propuesta-interrogatorio-titular-relacion-juridica-975` |
| 976 | Preguntas para el interrogatorio de la propia parte | 2013 | `preguntas-interrogatorio-propia-parte-976` |
| 977 | Preguntas para el interrogatorio de la parte contraria | 2013 | `preguntas-interrogatorio-parte-contraria-977` |
| 978 | Impugnación de preguntas: propuesta | 2013 | `impugnacion-preguntas-propuesta-978` |
| 980 | Documentos del actor en la audiencia previa | 2013 | `documentos-actor-audiencia-previa-980` |
| 997 | Ampliar la demanda, objetiva y subjetivamente | 2013 | `ampliar-demanda-objetiva-subjetivamente-997` |
| 998 | Dictamen pericial sobre otras pruebas: proposición | 2013 | `dictamen-pericial-sobre-otras-pruebas-proposicion-998` |
| 1002 | Encabezamiento del dictamen pericial escrito | 2013 | `encabezamiento-dictamen-pericial-escrito-1002` |
| 1005 | Aportación de dictamen pericial posterior a la demanda o contestación | 2013 | `aportacion-dictamen-pericial-posterior-demanda-1005` |
| 1014 | Dictamen pericial por actuaciones procesales posteriores a la demanda | 2013 | `dictamen-pericial-actuaciones-procesales-posteriores-1014` |
| 1016 | Ampliación del reconocimiento judicial propuesta por la otra parte | 2013 | `ampliacion-reconocimiento-judicial-propuesta-otra-parte-1016` |
| 1017 | Encabezamiento del primer escrito del demandado, con procurador de persona física | 2013 | `encabezamiento-primer-escrito-demandado-procurador-1017` |
| 1018 | Sustitución en el interrogatorio del representante de la persona jurídica | 2013 | `sustitucion-interrogatorio-representante-persona-1018` |
| 1019 | Propuesta de interrogatorio de organismos públicos | 2013 | `propuesta-interrogatorio-organismos-publicos-1019` |
| 1024 | Otrosí: vista en la oposición o en su impugnación | 2013 | `otrosi-vista-oposicion-impugnacion-1024` |
| 1026 | Comparecer ante la Sala | 2013 | `comparecer-ante-sala-1026` |
| 1029 | Otrosí sobre tasas judiciales | 2013 | `otrosi-sobre-tasas-judiciales-1029` |
| 1031 | Otrosí: liquidación de tasas por persona jurídica obligada (general) | 2013 | `otrosi-liquidacion-tasas-persona-juridica-obligada-1031` |
| 1045 | Otrosí: dictamen pericial en la oposición por pluspetición | 2013 | `otrosi-dictamen-pericial-oposicion-pluspeticion-1045` |
| 1056 | Habilitación de fondos pedida por el procurador | 2013 | `habilitacion-fondos-pedida-procurador-1056` |
| 1064 | Resumen de la prueba practicada, por el demandado | 2013 | `resumen-prueba-practicada-demandado-1064` |
| 1065 | Resumen de la prueba practicada, por el demandante | 2013 | `resumen-prueba-practicada-demandante-1065` |
| 1093 | Ampliación objetiva de la demanda | 2013 | `ampliacion-objetiva-demanda-1093` |
| 1094 | Recusar después de la vista | 2013 | `recusar-despues-vista-1094` |
| 1095 | Otrosí: prueba pericial de beneficiario de justicia gratuita en juicio ordinario | 2013 | `otrosi-prueba-pericial-beneficiario-justicia-gratuita-1095` |
| 1096 | Otrosí: designación de archivos | 2013 | `otrosi-designacion-archivos-1096` |
| 1099 | Encabezamiento del procurador que representa una masa patrimonial | 2013 | `encabezamiento-procurador-representa-masa-patrimonial-1099` |
| 1105 | Otrosí: averiguación del domicilio del demandado | 2013 | `otrosi-averiguacion-domicilio-demandado-1105` |
| 1108 | Renuncia a la dirección del asunto, dirigida al Tribunal | 2013 | `renuncia-direccion-asunto-dirigida-tribunal-1108` |
| 1112 | Encabezamiento de demanda del procurador de turno de oficio | 2013 | `encabezamiento-demanda-procurador-turno-oficio-1112` |
| 1113 | Renuncia conjunta de abogado y procurador | 2013 | `renuncia-conjunta-abogado-procurador-1113` |
| 1116 | Encabezamiento de demanda del procurador de sociedad en concurso | 2013 | `encabezamiento-demanda-procurador-sociedad-concurso-1116` |
| 1119 | Encabezamiento del primer escrito del actor, con procurador de persona física | 2013 | `encabezamiento-primer-escrito-actor-procurador-persona-1119` |
| 1120 | Encabezamiento del procurador de persona física que representa a una persona con discapacidad | 2013 | `encabezamiento-procurador-persona-fisica-representa-1120` |
| 1121 | Subsanación de deficiencias en la solicitud de justicia gratuita | 2013 | `subsanacion-deficiencias-solicitud-justicia-gratuita-1121` |
| 1122 | Encabezamiento de contestación con representación apud acta | 2013 | `encabezamiento-contestacion-representacion-apud-acta-1122` |
| 1125 | Recusar al LAJ: modelo general | 2013 | `recusar-laj-modelo-general-1125` |
| 1129 | Falta de jurisdicción: declinatoria | 2013 | `falta-jurisdiccion-declinatoria-1129` |
| 1131 | Otrosí: designación de despacho de letrado para notificaciones | 2013 | `otrosi-designacion-despacho-letrado-notificaciones-1131` |
| 1134 | Comparecer el demandado declarado rebelde | 2013 | `comparecer-demandado-declarado-rebelde-1134` |
| 1135 | Encabezamiento del procurador de una entidad sin personalidad jurídica | 2013 | `encabezamiento-procurador-entidad-sin-personalidad-1135` |
| 1137 | Encabezamiento del procurador de una persona jurídica | 2013 | `encabezamiento-procurador-persona-juridica-1137` |
| 1138 | Encabezamiento del procurador de quienes representan al concebido y no nacido | 2013 | `encabezamiento-procurador-quienes-representan-concebido-1138` |
| 1139 | Encabezamiento del procurador de entidad sin personalidad por falta de requisitos constitutivos | 2013 | `encabezamiento-procurador-entidad-sin-personalidad-falta-1139` |
| 1140 | Encabezamiento de demanda apud acta con varios tribunales de instancia en la localidad | 2013 | `encabezamiento-demanda-apud-acta-varios-tribunales-1140` |
| 1141 | Encabezamiento de demanda con varios domicilios del demandado | 2013 | `encabezamiento-demanda-varios-domicilios-demandado-1141` |
| 1196 | Falta de competencia territorial del Tribunal: planteamiento | 2014 | `falta-competencia-territorial-tribunal-planteamiento-1196` |
| 1241 | Presentar el acto de comunicación ya diligenciado | 2013 | `presentar-acto-comunicacion-ya-diligenciado-1241` |
| 1331 | Personación del demandado sin postulación preceptiva | 2013 | `personacion-demandado-sin-postulacion-preceptiva-1331` |
| 1353 | Comparecer ante la Audiencia Provincial | 2013 | `comparecer-ante-audiencia-provincial-1353` |
| 1356 | El demandado se persona (escrito básico) | 2013 | `demandado-persona-escrito-basico-1356` |
| 1362 | Requerimiento a la Administración para incluir el edificio en un plan de rehabilitación | 2013 | `requerimiento-administracion-incluir-edificio-plan-1362` |
| 1386 | Comunero pide incluir en el orden del día obras de accesibilidad | 2013 | `comunero-pide-incluir-orden-dia-obras-accesibilidad-1386` |
| 1389 | Comunero pide incluir un punto en el orden del día | 2013 | `comunero-pide-incluir-punto-orden-dia-1389` |
| 1425 | Comunicación de la comunidad a la Administración | 2013 | `comunicacion-comunidad-administracion-1425` |
| 1477 | Impugnación de la inadmisión de una prueba en el arbitraje | 2014 | `impugnacion-inadmision-prueba-arbitraje-1477` |
| 1492 | Conclusiones de una parte en el procedimiento arbitral | 2014 | `conclusiones-parte-procedimiento-arbitral-1492` |

## Actos y resoluciones de la Administración o del órgano judicial (18)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 68 | Autorización al inquilino para hacer obras en la vivienda alquilada | 2023 | `autorizacion-inquilino-hacer-obras-vivienda-alquilada-68` |
| 211 | Acta de inventario | 2020 | `acta-inventario-211` |
| 311 | Diligencia de ordenación que suspende un señalamiento civil por el estado de alarma COVID-19 | 2020 | `diligencia-ordenacion-suspende-senalamiento-civil-estado-311` |
| 822 | Certificación de obras y aportaciones individuales en obras comunes | 2015 | `certificacion-obras-aportaciones-individuales-obras-822` |
| 987 | Acuerdo alcanzado en la audiencia previa | 2013 | `acuerdo-alcanzado-audiencia-previa-987` |
| 1004 | Anuncio de dictamen pericial posterior a la demanda o contestación | 2013 | `anuncio-dictamen-pericial-posterior-demanda-contestacion-1004` |
| 1197 | Notificación al Tribunal del cambio de domicilio de la empresa demandada | 2014 | `notificacion-tribunal-cambio-domicilio-empresa-demandada-1197` |
| 1230 | Certificado de que el vicepresidente actúa por la comunidad en acciones judiciales | 2013 | `certificado-vicepresidente-actua-comunidad-acciones-1230` |
| 1301 | Aviso de cambio de cerradura | 2013 | `aviso-cambio-cerradura-1301` |
| 1372 | Certificado de que el presidente obliga a la comunidad | 2013 | `certificado-presidente-obliga-comunidad-1372` |
| 1374 | Certificado de que el presidente actúa por la comunidad en acciones judiciales | 2013 | `certificado-presidente-actua-comunidad-acciones-1374` |
| 1381 | Notificación al comunero por tablón de anuncios | 2013 | `notificacion-comunero-tablon-anuncios-1381` |
| 1383 | Notificar la corrección de errores del acta | 2013 | `notificar-correccion-errores-acta-1383` |
| 1385 | Acta de alteración de la estructura del edificio | 2013 | `acta-alteracion-estructura-edificio-1385` |
| 1395 | Requerimiento del presidente para derribar construcción en zona común | 2013 | `requerimiento-presidente-derribar-construccion-zona-1395` |
| 1427 | Traslado de sanción administrativa al propietario | 2013 | `traslado-sancion-administrativa-propietario-1427` |
| 1428 | Autorización para usar instalación común de aprovechamiento privativo | 2013 | `autorizacion-usar-instalacion-comun-aprovechamiento-1428` |
| 1435 | Aviso de la comunidad: fin del plazo contractual y no prórroga | 2013 | `aviso-comunidad-fin-plazo-contractual-no-prorroga-1435` |

## Contratos, escrituras y documentos (9)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 102 | Estatutos de sociedad limitada unipersonal de administración de fincas | 2022 | `estatutos-sociedad-limitada-unipersonal-administracion-102` |
| 177 | Estatutos de la comunidad de plazas de garaje | 2021 | `estatutos-comunidad-plazas-garaje-177` |
| 209 | Certificado de destrucción de documentación | 2020 | `certificado-destruccion-documentacion-209` |
| 216 | Comunicación a los trabajadores de la instalación del control horario | 2020 | `comunicacion-trabajadores-instalacion-control-horario-216` |
| 547 | Escritura de constitución de compañía familiar gallega | 2016 | `escritura-constitucion-compania-familiar-gallega-547` |
| 615 | Modelo normalizado de contestación a la demanda verbal | 2016 | `modelo-normalizado-contestacion-demanda-verbal-615` |
| 717 | Minuta de proposición de prueba en la audiencia previa del juicio ordinario | 2015 | `minuta-proposicion-prueba-audiencia-previa-juicio-717` |
| 1251 | Recibo de cantidades complementarias del alquiler | 2013 | `recibo-cantidades-complementarias-alquiler-1251` |
| 1478 | Proposición de prueba en procedimiento arbitral (modelo) | 2014 | `proposicion-prueba-procedimiento-arbitral-modelo-1478` |

## Comunicaciones, requerimientos y reclamaciones (8)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 305 | Comunicación del propietario discrepante de un acuerdo de la junta | 2020 | `comunicacion-propietario-discrepante-acuerdo-junta-305` |
| 556 | Aviso del propietario de plaza de garaje de instalar un punto de recarga eléctrica | 2016 | `aviso-propietario-plaza-garaje-instalar-punto-recarga-556` |
| 826 | Entrega al titular de la vivienda del certificado energético del edificio | 2015 | `entrega-titular-vivienda-certificado-energetico-edificio-826` |
| 895 | Reclamar a tribunal distinto el envío de todas las actuaciones del proceso | 2013 | `reclamar-tribunal-distinto-envio-todas-actuaciones-895` |
| 1003 | Denunciar que una copia es inexacta | 2013 | `denunciar-copia-es-inexacta-1003` |
| 1258 | Denegación de prórroga por necesidad del arrendador o de un familiar | 2013 | `denegacion-prorroga-necesidad-arrendador-familiar-1258` |
| 1280 | Requerimiento para liquidar impuestos | 2013 | `requerimiento-liquidar-impuestos-1280` |
| 1423 | Requerimiento al comunero para facilitar obras exigidas por la Administración | 2013 | `requerimiento-comunero-facilitar-obras-exigidas-1423` |

## Otros (40)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 231 | No aceptar la oferta motivada de la aseguradora | 2020 | `no-aceptar-oferta-motivada-aseguradora-231` |
| 232 | Aceptar la oferta de la aseguradora | 2020 | `aceptar-oferta-aseguradora-232` |
| 440 | Planteamiento de cuestión prejudicial ante el TJUE | 2018 | `planteamiento-cuestion-prejudicial-ante-tjue-440` |
| 485 | Condiciones particulares del contrato (pliego) | 2017 | `condiciones-particulares-contrato-pliego-485` |
| 856 | Reiterar la asistencia jurídica gratuita ante la Comisión | 2013 | `reiterar-asistencia-juridica-gratuita-ante-comision-856` |
| 869 | Actos de comunicación tramitados por el procurador | 2013 | `actos-comunicacion-tramitados-procurador-869` |
| 873 | Alegación de vulneración de derecho fundamental en la obtención de la prueba | 2013 | `alegacion-vulneracion-derecho-fundamental-obtencion-873` |
| 941 | Información sobre cargas aminoradas o extinguidas | 2013 | `informacion-sobre-cargas-aminoradas-extinguidas-941` |
| 949 | Corregir errores aritméticos | 2013 | `corregir-errores-aritmeticos-949` |
| 950 | Demanda de revisión de sentencia firme | 2013 | `demanda-revision-sentencia-firme-950` |
| 952 | Contestación a la demanda tras sentencia estimatoria: sustanciación del proceso | 2013 | `contestacion-demanda-tras-sentencia-estimatoria-952` |
| 961 | Incomparecencia del demandante: efectos | 2013 | `incomparecencia-demandante-efectos-961` |
| 967 | Acreditar la validez del documento público impugnado | 2013 | `acreditar-validez-documento-publico-impugnado-967` |
| 984 | Preguntas de la parte que no propuso al testigo | 2013 | `preguntas-parte-no-propuso-testigo-984` |
| 991 | Pronunciamiento sobre documentos y dictámenes aportados de contrario | 2013 | `pronunciamiento-sobre-documentos-dictamenes-aportados-991` |
| 992 | Fijación de hechos con conformidad | 2013 | `fijacion-hechos-conformidad-992` |
| 1000 | Parcialidad del testigo: manifestaciones | 2013 | `parcialidad-testigo-manifestaciones-1000` |
| 1008 | Acreditar la validez del documento privado impugnado | 2013 | `acreditar-validez-documento-privado-impugnado-1008` |
| 1015 | Observaciones del reconocimiento judicial | 2013 | `observaciones-reconocimiento-judicial-1015` |
| 1023 | Participación de las partes en la tasación | 2013 | `participacion-partes-tasacion-1023` |
| 1027 | Declarar insostenible la pretensión | 2013 | `declarar-insostenible-pretension-1027` |
| 1032 | Personas que las partes piden que cite el tribunal | 2013 | `personas-partes-piden-cite-tribunal-1032` |
| 1042 | Exposición del demandante en la vista | 2013 | `exposicion-demandante-vista-1042` |
| 1077 | Acumulación subjetiva de acciones contra varios demandados (general) | 2013 | `acumulacion-subjetiva-acciones-contra-varios-demandados-1077` |
| 1078 | Litisconsorcio necesario: modelo general | 2013 | `litisconsorcio-necesario-modelo-general-1078` |
| 1086 | Litisconsorcio voluntario y acumulación subjetiva de acciones de varios demandantes (general) | 2013 | `litisconsorcio-voluntario-acumulacion-subjetiva-acciones-1086` |
| 1087 | Audiencia al perito | 2013 | `audiencia-perito-1087` |
| 1089 | Audiencia de parte ante la apreciación de oficio de falta de competencia objetiva | 2013 | `audiencia-parte-ante-apreciacion-oficio-falta-1089` |
| 1123 | Adherirse a la recusación de jueces y magistrados: modelo general | 2013 | `adherirse-recusacion-jueces-magistrados-modelo-general-1123` |
| 1186 | Agrupar fincas | 2014 | `agrupar-fincas-1186` |
| 1242 | Devolución de tasas judiciales por acumulación de procesos | 2013 | `devolucion-tasas-judiciales-acumulacion-procesos-1242` |
| 1259 | Muebles y enseres del inmueble: inventario | 2013 | `muebles-enseres-inmueble-inventario-1259` |
| 1270 | Ingreso de retenciones fiscales: declaración | 2013 | `ingreso-retenciones-fiscales-declaracion-1270` |
| 1336 | Devolución de tasa judicial a persona jurídica por solución extrajudicial | 2013 | `devolucion-tasa-judicial-persona-juridica-solucion-1336` |
| 1384 | Aviso de zona sin humo | 2013 | `aviso-zona-sin-humo-1384` |
| 1390 | Nudo propietario prohíbe que lo represente el usufructuario | 2013 | `nudo-propietario-prohibe-lo-represente-usufructuario-1390` |
| 1391 | Delegación expresa del nudo propietario en el usufructuario | 2013 | `delegacion-expresa-nudo-propietario-usufructuario-1391` |
| 1392 | Régimen interior: reglamento | 2013 | `regimen-interior-reglamento-1392` |
| 1393 | Estatuto privativo del título constitutivo | 2013 | `estatuto-privativo-titulo-constitutivo-1393` |
| 1418 | Consentimiento del propietario a obras que le priven de una facultad | 2013 | `consentimiento-propietario-obras-le-priven-facultad-1418` |
