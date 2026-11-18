---
name: indice
description: "Índice de los 128 formularios de ejecución civil (demanda ejecutiva, ejecución hipotecaria, oposición, embargo, subasta, costas). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Ejecución civil: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Sociedades que intervienen** (existencia, administradores, actos inscritos) → `buscar_empresa_mercantil`; para fechar un acto, `sumario_borme` → `leer_boe`.
- **Inmuebles** (referencia catastral, superficie, uso) → `consultar_catastro` (y `callejero_catastro` para localizar la dirección).

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/ejecucion-civil:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (37)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 35 | Demanda de gastos no incluidos en la tasación de costas (juicio verbal) | 2024 | `demanda-gastos-no-incluidos-tasacion-costas-juicio-35` |
| 48 | Demanda del propietario para exigir a la comunidad obras de mantenimiento de elementos comunes | 2023 | `demanda-propietario-exigir-comunidad-obras-mantenimiento-48` |
| 97 | Ejecución de sentencia por crédito revolving: demanda | 2022 | `ejecucion-sentencia-credito-revolving-demanda-97` |
| 105 | Demanda verbal por defectos en obras de una vivienda | 2022 | `demanda-verbal-defectos-obras-vivienda-105` |
| 121 | Demanda ejecutiva del decreto que aprueba la tasación de costas | 2022 | `demanda-ejecutiva-decreto-aprueba-tasacion-costas-121` |
| 154 | Demanda ejecutiva de la sentencia de desahucio por precario | 2021 | `demanda-ejecutiva-sentencia-desahucio-precario-154` |
| 159 | Demanda ejecutiva basada en escritura de reconocimiento de deuda | 2021 | `demanda-ejecutiva-basada-escritura-reconocimiento-deuda-159` |
| 160 | Demanda de resolución de contrato de obra por cumplimiento defectuoso | 2021 | `demanda-resolucion-contrato-obra-cumplimiento-defectuoso-160` |
| 164 | Reconocimiento y ejecución de resolución extranjera sin convenio internacional: modelo general | 2021 | `reconocimiento-ejecucion-resolucion-extranjera-sin-164` |
| 252 | Demanda ejecutiva por aval a primer requerimiento (título no judicial) | 2020 | `demanda-ejecutiva-aval-primer-requerimiento-titulo-no-252` |
| 340 | Demanda de ejecución de acuerdos de la junta de propietarios | 2019 | `demanda-ejecucion-acuerdos-junta-propietarios-340` |
| 397 | Ejecución de título judicial extranjero conforme al Reglamento (UE) 1215/2012 | 2019 | `ejecucion-titulo-judicial-extranjero-conforme-reglamento-397` |
| 408 | Ejecución de concesión administrativa: demanda | 2018 | `ejecucion-concesion-administrativa-demanda-408` |
| 473 | Demanda ejecutiva de sentencia de condena con bases de liquidación | 2017 | `demanda-ejecutiva-sentencia-condena-bases-liquidacion-473` |
| 526 | Demanda de ejecución hipotecaria parcial de crédito sindicado | 2016 | `demanda-ejecucion-hipotecaria-parcial-credito-sindicado-526` |
| 593 | Demanda ejecutiva de sentencia firme que anula la cláusula suelo y ordena devolver cantidades | 2016 | `demanda-ejecutiva-sentencia-firme-anula-clausula-suelo-593` |
| 601 | Ejecución contra el sucesor mortis causa del ejecutado: demanda | 2016 | `ejecucion-contra-sucesor-mortis-causa-ejecutado-demanda-601` |
| 620 | Demanda de exequátur para ejecutar resoluciones extranjeras en España | 2016 | `demanda-exequatur-ejecutar-resoluciones-extranjeras-620` |
| 667 | Ejecución del acta notarial de deuda dineraria no contradicha | 2015 | `ejecucion-acta-notarial-deuda-dineraria-no-contradicha-667` |
| 668 | Ejecución de acto de conciliación con avenencia | 2015 | `ejecucion-acto-conciliacion-avenencia-668` |
| 870 | Demanda ejecutiva con ampliación por nuevos plazos (general) | 2013 | `demanda-ejecutiva-ampliacion-nuevos-plazos-general-870` |
| 885 | Demanda ejecutiva con ejecución provisional de sentencia de apelación | 2013 | `demanda-ejecutiva-ejecucion-provisional-sentencia-885` |
| 908 | Demanda ejecutiva ordinaria sin habilitación de fondos | 2013 | `demanda-ejecutiva-ordinaria-sin-habilitacion-fondos-908` |
| 920 | Ejecución de sentencia por impago de pensiones | 2013 | `ejecucion-sentencia-impago-pensiones-920` |
| 937 | Demanda ejecutiva por el saldo de una cuenta | 2013 | `demanda-ejecutiva-saldo-cuenta-937` |
| 945 | Demanda ejecutiva de condena dineraria hasta 2.000 euros | 2013 | `demanda-ejecutiva-condena-dineraria-hasta-2-000-euros-945` |
| 1165 | Demanda ejecutiva hipotecaria contra el deudor y el tercer poseedor | 2015 | `demanda-ejecutiva-hipotecaria-contra-deudor-tercer-1165` |
| 1191 | Apelación contra el auto que desestima la oposición a ejecución hipotecaria por abusividad | 2014 | `apelacion-contra-auto-desestima-oposicion-ejecucion-1191` |
| 1195 | Demanda ejecutiva sobre auto que aprueba una transacción judicial | 2014 | `demanda-ejecutiva-sobre-auto-aprueba-transaccion-1195` |
| 1246 | Ejecución de acuerdo de mediación en propiedad horizontal | 2013 | `ejecucion-acuerdo-mediacion-propiedad-horizontal-1246` |
| 1346 | Demanda ejecutiva derivada de monitorio | 2013 | `demanda-ejecutiva-derivada-monitorio-1346` |
| 1350 | Ejecución de sentencia: demanda | 2013 | `ejecucion-sentencia-demanda-1350` |
| 1358 | Demanda ejecutiva por condena en acción de cesación | 2013 | `demanda-ejecutiva-condena-accion-cesacion-1358` |
| 1359 | Demanda ejecutiva contra la comunidad por condena de hacer no personalísimo | 2013 | `demanda-ejecutiva-contra-comunidad-condena-hacer-no-1359` |
| 1449 | Demanda ordinaria por incumplimiento de contrato de obra (comunidad de propietarios) | 2014 | `demanda-ordinaria-incumplimiento-contrato-obra-comunidad-1449` |
| 1462 | Apelación contra el auto que deniega el despacho de ejecución hipotecaria | 2014 | `apelacion-contra-auto-deniega-despacho-ejecucion-1462` |
| 1465 | Apelación contra el auto que deniega el despacho de ejecución | 2014 | `apelacion-contra-auto-deniega-despacho-ejecucion-1465` |

## Recursos e impugnaciones (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 107 | Reposición contra el decreto que aplaza un lanzamiento | 2022 | `reposicion-contra-decreto-aplaza-lanzamiento-107` |
| 194 | Recurso de revisión directo contra el decreto que resuelve la impugnación de tasación de costas | 2021 | `recurso-revision-directo-contra-decreto-resuelve-194` |
| 832 | Apelación contra el auto de sobreseimiento de la ejecución por cláusula abusiva | 2013 | `apelacion-contra-auto-sobreseimiento-ejecucion-clausula-832` |
| 914 | Impugnación de la tasación de costas por partidas excesivas o superfluas | 2013 | `impugnacion-tasacion-costas-partidas-excesivas-914` |
| 1057 | Impugnar la tasación de costas como parte solicitante | 2013 | `impugnar-tasacion-costas-como-parte-solicitante-1057` |
| 1464 | Recurso de revisión directo contra decreto del LAJ con medidas ejecutivas | 2014 | `recurso-revision-directo-contra-decreto-laj-medidas-1464` |

## Contestaciones, oposiciones y alegaciones (14)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 24 | Alegaciones a la propuesta de requerimiento de pago por cláusulas abusivas | 2024 | `alegaciones-propuesta-requerimiento-pago-clausulas-24` |
| 57 | Alegaciones sobre suspensión del lanzamiento de vivienda habitual de colectivos vulnerables | 2023 | `alegaciones-sobre-suspension-lanzamiento-vivienda-57` |
| 119 | Oposición del arrendador a suspender el desahucio y lanzamiento (art. 1 RDL 11/2020) | 2022 | `oposicion-arrendador-suspender-desahucio-lanzamiento-art-119` |
| 244 | Oposición a la demanda de reconocimiento y ejecución de resolución extranjera | 2020 | `oposicion-demanda-reconocimiento-ejecucion-resolucion-244` |
| 268 | Oposición a la ejecución hipotecaria por abusividad del interés IRPH | 2020 | `oposicion-ejecucion-hipotecaria-abusividad-interes-irph-268` |
| 515 | Oposición a la ejecución del fiador solidario o avalista | 2016 | `oposicion-ejecucion-fiador-solidario-avalista-515` |
| 652 | Oposición a ejecutar un acta notarial de deudas dinerarias no contradichas | 2015 | `oposicion-ejecutar-acta-notarial-deudas-dinerarias-no-652` |
| 938 | Oposición a la suspensión por prejudicialidad penal en la ejecución de sentencia | 2013 | `oposicion-suspension-prejudicialidad-penal-ejecucion-938` |
| 946 | Oposición a la ejecución provisional de sentencia (general) | 2013 | `oposicion-ejecucion-provisional-sentencia-general-946` |
| 947 | Oposición a la ejecución de título no judicial | 2013 | `oposicion-ejecucion-titulo-no-judicial-947` |
| 948 | Oposición a ejecutar resoluciones procesales o arbitrales | 2013 | `oposicion-ejecutar-resoluciones-procesales-arbitrales-948` |
| 1044 | Oponerse a actuaciones ejecutivas concretas en condena dineraria: modelo general | 2013 | `oponerse-actuaciones-ejecutivas-concretas-condena-1044` |
| 1510 | Oposición a la ejecución de auto que homologa un acuerdo de mediación | 2014 | `oposicion-ejecucion-auto-homologa-acuerdo-mediacion-1510` |
| 1511 | Oposición a la ejecución de un acuerdo de mediación | 2014 | `oposicion-ejecucion-acuerdo-mediacion-1511` |

## Solicitudes y expedientes (37)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 58 | Suspensión del lanzamiento de vivienda habitual (Ley 12/2023, derecho a la vivienda) | 2023 | `suspension-lanzamiento-vivienda-habitual-ley-12-2023-58` |
| 123 | Inmovilización y subasta de un vehículo embargado | 2022 | `inmovilizacion-subasta-vehiculo-embargado-123` |
| 165 | Enervar el embargo con aval bancario en el declarativo tras oposición a monitorio | 2021 | `enervar-embargo-aval-bancario-declarativo-tras-oposicion-165` |
| 195 | Suspensión del lanzamiento arrendaticio de vulnerables sin alternativa (art. 1 RDL 11/2020) | 2021 | `suspension-lanzamiento-arrendaticio-vulnerables-sin-195` |
| 197 | Suspensión de lanzamiento (precario, tutela sumaria, derechos reales): art. 1 bis RDL 11/2020 | 2021 | `suspension-lanzamiento-precario-tutela-sumaria-derechos-197` |
| 204 | Homologación judicial de transacción en ejecución de sentencia | 2020 | `homologacion-judicial-transaccion-ejecucion-sentencia-204` |
| 246 | Administración judicial de empresa embargada | 2020 | `administracion-judicial-empresa-embargada-246` |
| 256 | Homologación judicial de acuerdo de mediación en ejecución | 2020 | `homologacion-judicial-acuerdo-mediacion-ejecucion-256` |
| 355 | Alzamiento de la suspensión del lanzamiento tras un mes del aviso de servicios sociales | 2019 | `alzamiento-suspension-lanzamiento-tras-mes-aviso-355` |
| 357 | Sobreseimiento de ejecución hipotecaria por vencimiento anticipado abusivo (STJUE 26-3-2019) | 2019 | `sobreseimiento-ejecucion-hipotecaria-vencimiento-357` |
| 386 | Nulidad de embargo indeterminado | 2019 | `nulidad-embargo-indeterminado-386` |
| 418 | Nulidad de actuaciones en proceso de ejecución | 2018 | `nulidad-actuaciones-proceso-ejecucion-418` |
| 437 | Embargo de intereses, rentas o frutos | 2018 | `embargo-intereses-rentas-frutos-437` |
| 483 | Subasta voluntaria de bien en proindiviso | 2017 | `subasta-voluntaria-bien-proindiviso-483` |
| 493 | Impulso procesal en el proceso ejecutivo | 2017 | `impulso-procesal-proceso-ejecutivo-493` |
| 622 | Subasta voluntaria: solicitud | 2016 | `subasta-voluntaria-solicitud-622` |
| 780 | Ejecución de la resolución firme que cierra el expediente de jurisdicción voluntaria | 2015 | `ejecucion-resolucion-firme-cierra-expediente-780` |
| 796 | Mandamiento a registro público para inscribir la resolución final del expediente | 2015 | `mandamiento-registro-publico-inscribir-resolucion-final-796` |
| 904 | Modificación del embargo a instancia del ejecutante | 2013 | `modificacion-embargo-instancia-ejecutante-904` |
| 907 | Requerimiento al ejecutado para que presente sus títulos | 2013 | `requerimiento-ejecutado-presente-titulos-907` |
| 911 | Tasación de costas: solicitud | 2013 | `tasacion-costas-solicitud-911` |
| 924 | Testimonio de haber instado la ejecución y certificado de imposibilidad de llevarla a cabo | 2013 | `testimonio-haber-instado-ejecucion-certificado-924` |
| 936 | Conversión de la ejecución provisional en definitiva | 2013 | `conversion-ejecucion-provisional-definitiva-936` |
| 939 | Suspensión por prejudicialidad penal en ejecución de sentencia (falsedad del título) | 2013 | `suspension-prejudicialidad-penal-ejecucion-sentencia-939` |
| 943 | Apremios para garantizar la entrega de cosa determinada | 2013 | `apremios-garantizar-entrega-cosa-determinada-943` |
| 963 | Suspensión de la ejecución del acuerdo impugnado | 2013 | `suspension-ejecucion-acuerdo-impugnado-963` |
| 1050 | Liquidación de daños y perjuicios por obras prohibidas en sentencia | 2013 | `liquidacion-danos-perjuicios-obras-prohibidas-sentencia-1050` |
| 1055 | Interrogatorio del ejecutado condenado a entregar cosa determinada | 2013 | `interrogatorio-ejecutado-condenado-entregar-cosa-1055` |
| 1059 | Mandamiento de cancelación de embargo | 2013 | `mandamiento-cancelacion-embargo-1059` |
| 1060 | Medidas de garantía en ejecución no dineraria | 2013 | `medidas-garantia-ejecucion-no-dineraria-1060` |
| 1199 | Embargo preventivo de buque (convenio de 12 de marzo de 1999) | 2014 | `embargo-preventivo-buque-convenio-12-marzo-1999-1199` |
| 1338 | Otrosí: suspensión de la ejecución del acuerdo impugnado | 2013 | `otrosi-suspension-ejecucion-acuerdo-impugnado-1338` |
| 1351 | Embargo preventivo: solicitud | 2013 | `embargo-preventivo-solicitud-1351` |
| 1431 | Comunero pide acceder a instalación de mejora energética ya ejecutada | 2013 | `comunero-pide-acceder-instalacion-mejora-energetica-ya-1431` |
| 1488 | Alzamiento de suspensión de ejecución tras desestimar la anulación del laudo, con indemnización | 2014 | `alzamiento-suspension-ejecucion-tras-desestimar-1488` |
| 1493 | Suspensión del lanzamiento de vivienda habitual de colectivos vulnerables | 2014 | `suspension-lanzamiento-vivienda-habitual-colectivos-1493` |
| 1496 | Prórroga de anotación preventiva de embargo | 2014 | `prorroga-anotacion-preventiva-embargo-1496` |

## Escritos de trámite (19)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 124 | Impugnación por el ejecutante de la oposición a la ejecución de título judicial | 2022 | `impugnacion-ejecutante-oposicion-ejecucion-titulo-124` |
| 158 | Impugnación de la oposición a la ejecución en familia por motivos de fondo | 2021 | `impugnacion-oposicion-ejecucion-familia-motivos-fondo-158` |
| 260 | Comunicar nuevo domicilio del deudor y pedir requerimiento de pago por auxilio judicial | 2020 | `comunicar-nuevo-domicilio-deudor-pedir-requerimiento-260` |
| 334 | Impago tras el requerimiento y petición de decreto que ponga fin al desahucio | 2019 | `impago-tras-requerimiento-peticion-decreto-ponga-fin-334` |
| 362 | Oposición extraordinaria a la ejecución hipotecaria: cláusula abusiva sobre la cantidad exigible | 2019 | `oposicion-extraordinaria-ejecucion-hipotecaria-clausula-362` |
| 363 | Oposición extraordinaria a la ejecución hipotecaria: cláusula abusiva que fundamenta la ejecución | 2019 | `oposicion-extraordinaria-ejecucion-hipotecaria-clausula-363` |
| 419 | Denuncia por el ejecutado de infracciones en los actos de la ejecución | 2018 | `denuncia-ejecutado-infracciones-actos-ejecucion-419` |
| 482 | Aprobación del remate pedida por el solicitante de la subasta | 2017 | `aprobacion-remate-pedida-solicitante-subasta-482` |
| 484 | Sobreseimiento del expediente pedido por el solicitante de la subasta | 2017 | `sobreseimiento-expediente-pedido-solicitante-subasta-484` |
| 683 | Personación del tercer poseedor de inmueble en la ejecución | 2015 | `personacion-tercer-poseedor-inmueble-ejecucion-683` |
| 713 | Notificar la ejecución al ocupante del inmueble embargado por el procurador | 2015 | `notificar-ejecucion-ocupante-inmueble-embargado-713` |
| 714 | Inspección del inmueble subastado pedida por un licitador | 2015 | `inspeccion-inmueble-subastado-pedida-licitador-714` |
| 923 | Otrosí: acreditación de pago en arrendamientos con lanzamiento | 2013 | `otrosi-acreditacion-pago-arrendamientos-lanzamiento-923` |
| 935 | Otrosí: suspensión de la ejecución de sentencia | 2013 | `otrosi-suspension-ejecucion-sentencia-935` |
| 957 | Otrosí: suspensión de la ejecución en el incidente de nulidad | 2013 | `otrosi-suspension-ejecucion-incidente-nulidad-957` |
| 1047 | Otrosí: caución del ejecutante en condena no dineraria | 2013 | `otrosi-caucion-ejecutante-condena-no-dineraria-1047` |
| 1130 | Desistimiento del ejecutante en la ejecución provisional | 2013 | `desistimiento-ejecutante-ejecucion-provisional-1130` |
| 1157 | Otrosí: ampliación de la ejecución | 2013 | `otrosi-ampliacion-ejecucion-1157` |
| 1159 | Mandamiento al Registro de la Propiedad por extinción de la hipoteca (pago) | 2015 | `mandamiento-registro-propiedad-extincion-hipoteca-pago-1159` |

## Actos y resoluciones de la Administración o del órgano judicial (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 67 | Requerimiento al inquilino para pagar el IBI | 2023 | `requerimiento-inquilino-pagar-ibi-67` |
| 241 | Resolución de contrato de obra por mutuo acuerdo | 2020 | `resolucion-contrato-obra-mutuo-acuerdo-241` |
| 551 | Requerimiento de pago de gastos generales en propiedad horizontal | 2016 | `requerimiento-pago-gastos-generales-propiedad-horizontal-551` |
| 552 | Requerimiento para pagar servicios individuales | 2016 | `requerimiento-pagar-servicios-individuales-552` |
| 1509 | Acuerdo de mediación alcanzado en ejecución de sentencia | 2014 | `acuerdo-mediacion-alcanzado-ejecucion-sentencia-1509` |

## Contratos, escrituras y documentos (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 116 | Pacto de ejecución y cumplimiento de un contrato de mandato | 2022 | `pacto-ejecucion-cumplimiento-contrato-mandato-116` |
| 257 | Burofax de requerimiento de pago en arrendamiento de industria | 2020 | `burofax-requerimiento-pago-arrendamiento-industria-257` |

## Comunicaciones, requerimientos y reclamaciones (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1355 | Aviso al tribunal de entrega de la finca antes del lanzamiento, con la sentencia cumplida | 2013 | `aviso-tribunal-entrega-finca-antes-lanzamiento-sentencia-1355` |

## Otros (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 299 | Vulnerabilidad del arrendador frente a la suspensión del lanzamiento (art. 1.4 RDL 11/2020) | 2020 | `vulnerabilidad-arrendador-frente-suspension-lanzamiento-299` |
| 638 | Testimonio del decreto de aprobación de remate para constituir hipoteca | 2015 | `testimonio-decreto-aprobacion-remate-constituir-hipoteca-638` |
| 664 | Oposición del deudor al requerimiento en reclamación notarial de deudas dinerarias | 2015 | `oposicion-deudor-requerimiento-reclamacion-notarial-664` |
| 850 | Declaración responsable de especial vulnerabilidad contra el lanzamiento | 2013 | `declaracion-responsable-especial-vulnerabilidad-contra-850` |
| 905 | Postura por escrito en subasta | 2013 | `postura-escrito-subasta-905` |
| 942 | Caución ofrecida en sustitución del embargo | 2013 | `caucion-ofrecida-sustitucion-embargo-942` |
| 1330 | Enervar el embargo preventivo | 2013 | `enervar-embargo-preventivo-1330` |
