---
name: indice
description: "Índice de los 183 formularios de contratos, consumo y responsabilidad civil (reclamación de cantidad, cláusulas abusivas, seguros, daños). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Contratos, consumo y responsabilidad civil: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/contratos-y-responsabilidad-civil:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Demandas, interposiciones y peticiones iniciales (66)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 26 | Demanda genérica de cantidad en juicio verbal | 2024 | `demanda-generica-cantidad-juicio-verbal-26` |
| 30 | Demanda de cantidad entre obligados a comunicarse electrónicamente con el tribunal | 2024 | `demanda-cantidad-entre-obligados-comunicarse-30` |
| 44 | Demanda de resolución de compraventa de vehículo por falta de conformidad | 2024 | `demanda-resolucion-compraventa-vehiculo-falta-44` |
| 52 | Demanda contra el dictamen pericial del art. 38 de la Ley de Contrato de Seguro | 2023 | `demanda-contra-dictamen-pericial-art-38-ley-contrato-52` |
| 72 | Demanda ordinaria por vicios de la construcción | 2023 | `demanda-ordinaria-vicios-construccion-72` |
| 81 | Demanda de nulidad por objeto ilícito y, subsidiariamente, vicio del consentimiento | 2023 | `demanda-nulidad-objeto-ilicito-subsidiariamente-vicio-81` |
| 87 | Demanda de nulidad de contrato de opción de compra | 2023 | `demanda-nulidad-contrato-opcion-compra-87` |
| 98 | Demanda de resolución de compraventa por vicios ocultos | 2022 | `demanda-resolucion-compraventa-vicios-ocultos-98` |
| 125 | Demanda de honorarios impagados a un abogado | 2022 | `demanda-honorarios-impagados-abogado-125` |
| 131 | Demanda contra la aseguradora por impago de cobertura sanitaria | 2022 | `demanda-contra-aseguradora-impago-cobertura-sanitaria-131` |
| 132 | Demanda de honorarios impagados a una inmobiliaria | 2022 | `demanda-honorarios-impagados-inmobiliaria-132` |
| 151 | Demanda verbal contra aseguradora por pérdidas del cierre del negocio por COVID | 2021 | `demanda-verbal-contra-aseguradora-perdidas-cierre-151` |
| 153 | Demanda de cantidad por desistimiento del comitente en contrato de obra | 2021 | `demanda-cantidad-desistimiento-comitente-contrato-obra-153` |
| 166 | Demanda de nulidad de compraventa de negocio por vicios del consentimiento | 2021 | `demanda-nulidad-compraventa-negocio-vicios-166` |
| 189 | Demanda verbal para recuperar el depósito de reserva de un restaurante cerrado en estado de alarma | 2021 | `demanda-verbal-recuperar-deposito-reserva-restaurante-189` |
| 198 | Demanda de resolución de aparcería por incumplimiento del aparcero e indemnización | 2021 | `demanda-resolucion-aparceria-incumplimiento-aparcero-e-198` |
| 199 | Demanda de cantidad contra el banco por phishing | 2021 | `demanda-cantidad-contra-banco-phishing-199` |
| 202 | Demanda contra la aseguradora para cobrar el importe mínimo por incumplimiento del seguro | 2020 | `demanda-contra-aseguradora-cobrar-importe-minimo-202` |
| 217 | Demanda de resolución de compraventa por la cláusula rebus sic stantibus | 2020 | `demanda-resolucion-compraventa-clausula-rebus-sic-217` |
| 237 | Demanda verbal por vicios ocultos en compraventa de vehículo | 2020 | `demanda-verbal-vicios-ocultos-compraventa-vehiculo-237` |
| 240 | Demanda contra el contratista para resolver el contrato de obra por incumplimiento | 2020 | `demanda-contra-contratista-resolver-contrato-obra-240` |
| 270 | Demanda por gran invalidez derivada de accidente de circulación | 2020 | `demanda-gran-invalidez-derivada-accidente-circulacion-270` |
| 273 | Demanda de cumplimiento de contrato por venta de cosa ajena | 2020 | `demanda-cumplimiento-contrato-venta-cosa-ajena-273` |
| 274 | Demanda de cumplimiento de contrato por doble venta | 2020 | `demanda-cumplimiento-contrato-doble-venta-274` |
| 296 | Demanda de modificación del contrato por la cláusula rebus sic stantibus | 2020 | `demanda-modificacion-contrato-clausula-rebus-sic-296` |
| 301 | Demanda ordinaria de cantidad por contrato de obra | 2020 | `demanda-ordinaria-cantidad-contrato-obra-301` |
| 321 | Demanda verbal de resolución de comodato | 2020 | `demanda-verbal-resolucion-comodato-321` |
| 335 | Demanda ordinaria de cantidad por incumplimiento del seguro de asistencia sanitaria | 2019 | `demanda-ordinaria-cantidad-incumplimiento-seguro-335` |
| 354 | Demanda por accidente de circulación con elemento extranjero | 2019 | `demanda-accidente-circulacion-elemento-extranjero-354` |
| 358 | Demanda verbal de cantidad por cobro de lo indebido: acción | 2019 | `demanda-verbal-cantidad-cobro-lo-indebido-accion-358` |
| 361 | Demanda de daños por incumplimiento del contrato de depósito | 2019 | `demanda-danos-incumplimiento-contrato-deposito-361` |
| 366 | Demanda de resolución de compraventa de inmueble por incumplimiento del comprador | 2019 | `demanda-resolucion-compraventa-inmueble-incumplimiento-366` |
| 381 | Demanda verbal de cantidad por enriquecimiento injusto | 2019 | `demanda-verbal-cantidad-enriquecimiento-injusto-381` |
| 388 | Demanda verbal de cobro de lo indebido | 2019 | `demanda-verbal-cobro-lo-indebido-388` |
| 389 | Demanda ordinaria de cobro de lo indebido | 2019 | `demanda-ordinaria-cobro-lo-indebido-389` |
| 396 | Demanda verbal de repetición del asegurado contra la aseguradora | 2019 | `demanda-verbal-repeticion-asegurado-contra-aseguradora-396` |
| 414 | Demanda ordinaria de nulidad de compraventa por vicio del consentimiento | 2018 | `demanda-ordinaria-nulidad-compraventa-vicio-414` |
| 417 | Demanda de saneamiento por vicios ocultos en la venta de animales | 2018 | `demanda-saneamiento-vicios-ocultos-venta-animales-417` |
| 436 | Demanda ordinaria de resolución de comodato | 2018 | `demanda-ordinaria-resolucion-comodato-436` |
| 456 | Demanda ordinaria de acción directa en contratación de obra | 2018 | `demanda-ordinaria-accion-directa-contratacion-obra-456` |
| 458 | Demanda de nulidad de depósito estructurado | 2018 | `demanda-nulidad-deposito-estructurado-458` |
| 465 | Demanda de acción redhibitoria por vicios ocultos | 2017 | `demanda-accion-redhibitoria-vicios-ocultos-465` |
| 466 | Demanda redhibitoria por vicios ocultos con gastos y daños y perjuicios | 2017 | `demanda-redhibitoria-vicios-ocultos-gastos-danos-466` |
| 467 | Vicios en la construcción: demanda | 2017 | `vicios-construccion-demanda-467` |
| 469 | Demanda del comprador de vivienda en construcción contra el banco avalista por cantidades entregadas | 2017 | `demanda-comprador-vivienda-construccion-contra-banco-469` |
| 517 | Demanda de cantidad por dolo incidental | 2016 | `demanda-cantidad-dolo-incidental-517` |
| 592 | Demanda verbal por accidente de circulación contra conductor, propietario y aseguradora | 2016 | `demanda-verbal-accidente-circulacion-contra-conductor-592` |
| 594 | Demanda ordinaria de cantidad por enriquecimiento injusto | 2016 | `demanda-ordinaria-cantidad-enriquecimiento-injusto-594` |
| 597 | Demanda ordinaria por accidente de circulación con daños personales y materiales | 2016 | `demanda-ordinaria-accidente-circulacion-danos-personales-597` |
| 599 | Demanda ordinaria de cantidad por incumplimiento del seguro contra robo | 2016 | `demanda-ordinaria-cantidad-incumplimiento-seguro-contra-599` |
| 602 | Demanda de daños tras resolver un contrato de franquicia | 2016 | `demanda-danos-tras-resolver-contrato-franquicia-602` |
| 608 | Demanda de impugnación de acuerdos de la junta por grave perjuicio o abuso de derecho | 2016 | `demanda-impugnacion-acuerdos-junta-grave-perjuicio-abuso-608` |
| 827 | Demanda de resolución de contrato de servicios con préstamo vinculado | 2015 | `demanda-resolucion-contrato-servicios-prestamo-vinculado-827` |
| 828 | Demanda de lucro cesante por privación de vehículo de uso profesional | 2015 | `demanda-lucro-cesante-privacion-vehiculo-uso-profesional-828` |
| 867 | Demanda de cantidad por compraventa mercantil | 2013 | `demanda-cantidad-compraventa-mercantil-867` |
| 874 | Demanda de resolución de contrato con devolución de lo cobrado | 2013 | `demanda-resolucion-contrato-devolucion-lo-cobrado-874` |
| 960 | Demanda de demolición de obra (general) | 2013 | `demanda-demolicion-obra-general-960` |
| 1034 | Acción declarativa sobre condiciones generales de la contratación (general) | 2013 | `accion-declarativa-sobre-condiciones-generales-1034` |
| 1142 | Demanda de la comunidad contra un particular para eliminar obra en elemento común | 2013 | `demanda-comunidad-contra-particular-eliminar-obra-1142` |
| 1152 | Demanda verbal de cantidad por compraventa con precio aplazado | 2013 | `demanda-verbal-cantidad-compraventa-precio-aplazado-1152` |
| 1184 | Demanda verbal de cantidad por incumplimiento de compraventa de vehículo | 2014 | `demanda-verbal-cantidad-incumplimiento-compraventa-1184` |
| 1189 | Demanda de cantidad por incumplimiento de seguro de vida | 2014 | `demanda-cantidad-incumplimiento-seguro-vida-1189` |
| 1198 | Demanda de cantidad por incumplimiento de seguro de accidentes | 2014 | `demanda-cantidad-incumplimiento-seguro-accidentes-1198` |
| 1490 | Demanda arbitral de indemnización por incumplimiento contractual | 2014 | `demanda-arbitral-indemnizacion-incumplimiento-1490` |
| 1497 | Demanda de honorarios profesionales de arquitecto | 2014 | `demanda-honorarios-profesionales-arquitecto-1497` |
| 90 (Procesal) | Acción de regreso del socio contra la sociedad (art. 331 LSC): demanda | 2023 | `accion-regreso-socio-contra-sociedad-art-331-lsc-demanda-p90` |

## Recursos e impugnaciones (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 944 | Impugnar la oposición por defectos procesales: modelo general | 2013 | `impugnar-oposicion-defectos-procesales-modelo-general-944` |

## Contestaciones, oposiciones y alegaciones (22)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 21 | Contestación a la demanda de cantidad por consumos domésticos de energía | 2024 | `contestacion-demanda-cantidad-consumos-domesticos-21` |
| 139 | Contestación a demanda de resolución de compraventa (excepción de contrato incumplido) | 2021 | `contestacion-demanda-resolucion-compraventa-excepcion-139` |
| 322 | Contestación a demanda de cumplimiento alegando non adimpleti contractus | 2020 | `contestacion-demanda-cumplimiento-alegando-non-adimpleti-322` |
| 382 | Contestación a la demanda verbal de cantidad por enriquecimiento injusto | 2019 | `contestacion-demanda-verbal-cantidad-enriquecimiento-382` |
| 384 | Contestación a la demanda verbal de cantidad por cobro de lo indebido | 2019 | `contestacion-demanda-verbal-cantidad-cobro-lo-indebido-384` |
| 390 | Contestación y reconvención en demanda ordinaria por cobro de lo indebido | 2019 | `contestacion-reconvencion-demanda-ordinaria-cobro-lo-390` |
| 486 | Contestación a la demanda por vulneración del derecho al honor | 2017 | `contestacion-demanda-vulneracion-derecho-honor-486` |
| 531 | Contestación a la demanda por vicios constructivos | 2016 | `contestacion-demanda-vicios-constructivos-531` |
| 591 | Oposición por crédito compensable en juicio verbal | 2016 | `oposicion-credito-compensable-juicio-verbal-591` |
| 617 | Alegaciones del demandante sobre el posible carácter abusivo de una cláusula | 2015 | `alegaciones-demandante-sobre-posible-caracter-abusivo-617` |
| 629 | Contestación a la demanda de indemnización compensatoria entre convivientes | 2016 | `contestacion-demanda-indemnizacion-compensatoria-entre-629` |
| 718 | Contestación escrita a la demanda verbal de cantidad | 2015 | `contestacion-escrita-demanda-verbal-cantidad-718` |
| 840 | Reconvención de daños y perjuicios en juicio verbal | 2013 | `reconvencion-danos-perjuicios-juicio-verbal-840` |
| 862 | Contestación a la oposición de crédito compensable en juicio verbal | 2013 | `contestacion-oposicion-credito-compensable-juicio-verbal-862` |
| 882 | Oposición a la concesión de justicia gratuita | 2013 | `oposicion-concesion-justicia-gratuita-882` |
| 1051 | Oposición del deudor a la determinación de daños y perjuicios | 2013 | `oposicion-deudor-determinacion-danos-perjuicios-1051` |
| 1090 | Contestar a la impugnación de honorarios del perito | 2013 | `contestar-impugnacion-honorarios-perito-1090` |
| 1101 | Alegaciones sobre el carácter abusivo de una cláusula | 2013 | `alegaciones-sobre-caracter-abusivo-clausula-1101` |
| 1136 | Contestar a la impugnación de honorarios de letrado | 2013 | `contestar-impugnacion-honorarios-letrado-1136` |
| 1149 | Contestación a demanda de cantidad por contrato de obra | 2013 | `contestacion-demanda-cantidad-contrato-obra-1149` |
| 1220 | Contestación a reclamación de cuotas manteniendo la deuda | 2013 | `contestacion-reclamacion-cuotas-manteniendo-deuda-1220` |
| 1311 | Contestación del propietario al requerimiento de depositar la fianza | 2013 | `contestacion-propietario-requerimiento-depositar-fianza-1311` |

## Solicitudes y expedientes (12)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 4 | Pedir la exoneración de costas o la moderación de su cuantía | 2025 | `pedir-exoneracion-costas-moderacion-cuantia-4` |
| 92 | Consignación judicial por reclamación del subcontratista | 2023 | `consignacion-judicial-reclamacion-subcontratista-92` |
| 333 | Conciliación previa para reclamar daños de un accidente de circulación | 2019 | `conciliacion-previa-reclamar-danos-accidente-circulacion-333` |
| 385 | Conciliación previa por cobro de lo indebido | 2019 | `conciliacion-previa-cobro-lo-indebido-385` |
| 618 | Contestación a la alegación de crédito compensable en juicio verbal | 2015 | `contestacion-alegacion-credito-compensable-juicio-verbal-618` |
| 633 | Expediente notarial de nombramiento de perito en contrato de seguro | 2015 | `expediente-notarial-nombramiento-perito-contrato-seguro-633` |
| 665 | Expediente notarial de deudas dinerarias no contradichas | 2015 | `expediente-notarial-deudas-dinerarias-no-contradichas-665` |
| 692 | Inicio de expediente de título de depósito | 2015 | `inicio-expediente-titulo-deposito-692` |
| 698 | Comunicación al emisor para pagar rendimientos tras seis meses sin controversia | 2015 | `comunicacion-emisor-pagar-rendimientos-tras-seis-meses-698` |
| 1367 | Resarcimiento del propietario por daños causados por la comunidad | 2013 | `resarcimiento-propietario-danos-causados-comunidad-1367` |
| 1414 | Comunero pide beneficiarse de obra ya hecha por la comunidad | 2013 | `comunero-pide-beneficiarse-obra-ya-hecha-comunidad-1414` |
| 1424 | Resarcimiento solicitado por la comunidad por daños de un propietario | 2013 | `resarcimiento-solicitado-comunidad-danos-propietario-1424` |

## Escritos de trámite (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 679 | Subsanación de defectos de la solicitud por el promotor | 2015 | `subsanacion-defectos-solicitud-promotor-679` |
| 694 | Fianza del perceptor de rendimientos para garantizar su devolución | 2015 | `fianza-perceptor-rendimientos-garantizar-devolucion-694` |
| 706 | Daños y perjuicios reclamados por el requerido por no comparecer el solicitante a la conciliación | 2015 | `danos-perjuicios-reclamados-requerido-no-comparecer-706` |
| 792 | Subsanación de defectos u omisiones de la solicitud | 2015 | `subsanacion-defectos-u-omisiones-solicitud-792` |
| 800 | Justificante de pago de la tasa judicial presentado tras la demanda | 2013 | `justificante-pago-tasa-judicial-presentado-tras-demanda-800` |
| 839 | Subsanar la falta de depósito para recurrir | 2013 | `subsanar-falta-deposito-recurrir-839` |
| 1084 | Renuncia de profesionales de libre elección a honorarios o derechos | 2013 | `renuncia-profesionales-libre-eleccion-honorarios-1084` |
| 1111 | Otrosí: ofrecimiento de liberar el bien mediante pago | 2013 | `otrosi-ofrecimiento-liberar-bien-mediante-pago-1111` |
| 1115 | Encabezamiento de demanda del procurador de un grupo de consumidores afectados | 2013 | `encabezamiento-demanda-procurador-grupo-consumidores-1115` |
| 1192 | Oposición del demandante a la enervación por requerimiento previo de pago | 2014 | `oposicion-demandante-enervacion-requerimiento-previo-1192` |
| 1357 | Justificante de pago de tasa judicial presentado con posterioridad | 2013 | `justificante-pago-tasa-judicial-presentado-posterioridad-1357` |

## Actos y resoluciones de la Administración o del órgano judicial (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 99 | Autorización para domiciliar pagos en banco | 2022 | `autorizacion-domiciliar-pagos-banco-99` |
| 230 | Informes temporales emitidos por la aseguradora | 2020 | `informes-temporales-emitidos-aseguradora-230` |
| 1161 | Resolución por mutuo acuerdo del contrato de prestación de servicios | 2015 | `resolucion-mutuo-acuerdo-contrato-prestacion-servicios-1161` |
| 1207 | Certificar la liquidación de deudas | 2013 | `certificar-liquidacion-deudas-1207` |
| 1363 | Acta de rehabilitación del edificio con cesión de propiedad al contratista | 2013 | `acta-rehabilitacion-edificio-cesion-propiedad-1363` |

## Contratos, escrituras y documentos (32)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 53 | Rehabilitación de inmueble: contrato de obras | 2023 | `rehabilitacion-inmueble-contrato-obras-53` |
| 63 | Cláusula antiinquiokupación | 2023 | `clausula-antiinquiokupacion-63` |
| 118 | Pacto que declara cumplido un contrato de mandato | 2022 | `pacto-declara-cumplido-contrato-mandato-118` |
| 136 | Contrato de cubrición o venta de semen equino | 2021 | `contrato-cubricion-venta-semen-equino-136` |
| 191 | Fiducia cum amico entre particulares: contrato | 2021 | `fiducia-cum-amico-entre-particulares-contrato-191` |
| 203 | Contrato de transacción para terminar un proceso civil | 2020 | `contrato-transaccion-terminar-proceso-civil-203` |
| 206 | Registro de actividades de tratamiento del encargado del tratamiento | 2020 | `registro-actividades-tratamiento-encargado-tratamiento-206` |
| 207 | Comunicación a la APDCAT de la designación del DPD | 2020 | `comunicacion-apdcat-designacion-dpd-207` |
| 208 | Comunicación a la AVPD de la designación del DPD | 2020 | `comunicacion-avpd-designacion-dpd-208` |
| 220 | Respuesta al ejercicio del derecho de portabilidad de datos | 2020 | `respuesta-ejercicio-derecho-portabilidad-datos-220` |
| 221 | Respuesta al ejercicio del derecho de limitación del tratamiento de datos | 2020 | `respuesta-ejercicio-derecho-limitacion-tratamiento-datos-221` |
| 337 | Contrato de uso de espacios de coworking | 2019 | `contrato-uso-espacios-coworking-337` |
| 346 | Comodato de vivienda: contrato | 2019 | `comodato-vivienda-contrato-346` |
| 369 | Corresponsabilidad en el tratamiento de datos personales: contrato | 2019 | `corresponsabilidad-tratamiento-datos-personales-contrato-369` |
| 378 | Cesión de secreto empresarial: contrato | 2019 | `cesion-secreto-empresarial-contrato-378` |
| 460 | Exoneración de responsabilidad del suministrador: cláusula | 2017 | `exoneracion-responsabilidad-suministrador-clausula-460` |
| 490 | Dación en pago: contrato privado | 2017 | `dacion-pago-contrato-privado-490` |
| 491 | Mandato: contrato | 2017 | `mandato-contrato-491` |
| 501 | Préstamo de la empresa al trabajador | 2017 | `prestamo-empresa-trabajador-501` |
| 548 | Escritura de contrato de vitalicio | 2016 | `escritura-contrato-vitalicio-548` |
| 584 | Compraventa de bien tronquero con llamamiento previo (País Vasco) | 2016 | `compraventa-bien-tronquero-llamamiento-previo-pais-vasco-584` |
| 1166 | Contrato de aprovechamiento por turno de inmuebles turísticos | 2015 | `contrato-aprovechamiento-turno-inmuebles-turisticos-1166` |
| 1169 | Mediación inmobiliaria: contrato | 2015 | `mediacion-inmobiliaria-contrato-1169` |
| 1172 | Contrato de aprovechamiento por turno de inmuebles turísticos en construcción | 2015 | `contrato-aprovechamiento-turno-inmuebles-turisticos-1172` |
| 1178 | Ampliación de arras: contrato | 2015 | `ampliacion-arras-contrato-1178` |
| 1179 | Cuenta en participación en la construcción de edificio para la venta | 2015 | `cuenta-participacion-construccion-edificio-venta-1179` |
| 1181 | Mediación en disputas: contrato | 2015 | `mediacion-disputas-contrato-1181` |
| 1260 | Cláusula de improcedencia de prórroga por necesidad propia | 2013 | `clausula-improcedencia-prorroga-necesidad-propia-1260` |
| 1368 | Contrato de sustitución de la instalación de TDT | 2013 | `contrato-sustitucion-instalacion-tdt-1368` |
| 1458 | Venta de licencia de taxi y vehículo | 2014 | `venta-licencia-taxi-vehiculo-1458` |
| 1469 | Sumisión a arbitraje internacional: cláusula | 2014 | `sumision-arbitraje-internacional-clausula-1469` |
| 1507 | Cláusula contractual de sumisión a mediación | 2014 | `clausula-contractual-sumision-mediacion-1507` |

## Comunicaciones, requerimientos y reclamaciones (23)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 120 | Reclamación previa por cláusula abusiva en un crédito al consumo | 2022 | `reclamacion-previa-clausula-abusiva-credito-consumo-120` |
| 172 | Reclamación a la aseguradora del hermano perjudicado | 2021 | `reclamacion-aseguradora-hermano-perjudicado-172` |
| 173 | Reclamación a la aseguradora del nieto perjudicado | 2021 | `reclamacion-aseguradora-nieto-perjudicado-173` |
| 174 | Reclamación a la aseguradora del padre o la madre perjudicados | 2021 | `reclamacion-aseguradora-padre-madre-perjudicados-174` |
| 175 | Reclamación a la aseguradora del hijo perjudicado | 2021 | `reclamacion-aseguradora-hijo-perjudicado-175` |
| 176 | Reclamación a la aseguradora del abuelo perjudicado | 2021 | `reclamacion-aseguradora-abuelo-perjudicado-176` |
| 222 | Reclamación a la aseguradora por lesiones temporales | 2020 | `reclamacion-aseguradora-lesiones-temporales-222` |
| 223 | Reclamación a la aseguradora por muerte | 2020 | `reclamacion-aseguradora-muerte-223` |
| 224 | Reclamación a la aseguradora por secuelas | 2020 | `reclamacion-aseguradora-secuelas-224` |
| 225 | Reclamación a la aseguradora por perjuicio estético | 2020 | `reclamacion-aseguradora-perjuicio-estetico-225` |
| 226 | Reclamación a la aseguradora por necesidad de ayuda de tercera persona | 2020 | `reclamacion-aseguradora-necesidad-ayuda-tercera-persona-226` |
| 227 | Reclamación a la aseguradora por pérdida de calidad de vida | 2020 | `reclamacion-aseguradora-perdida-calidad-vida-227` |
| 228 | Reclamación a la aseguradora por lucro cesante por muerte | 2020 | `reclamacion-aseguradora-lucro-cesante-muerte-228` |
| 233 | Reclamación a la aseguradora por lucro cesante por lesiones permanentes | 2020 | `reclamacion-aseguradora-lucro-cesante-lesiones-233` |
| 239 | Reclamación a la aseguradora del perjudicado no conductor | 2020 | `reclamacion-aseguradora-perjudicado-no-conductor-239` |
| 251 | Reclamación al banco del importe garantizado por aval a primer requerimiento | 2020 | `reclamacion-banco-importe-garantizado-aval-primer-251` |
| 595 | Reclamación extrajudicial al asegurador por siniestro de circulación | 2016 | `reclamacion-extrajudicial-asegurador-siniestro-595` |
| 1103 | Reclamación de honorarios del abogado a su propio cliente | 2013 | `reclamacion-honorarios-abogado-propio-cliente-1103` |
| 1177 | Reclamación entre propietarios por daños en la vivienda | 2015 | `reclamacion-entre-propietarios-danos-vivienda-1177` |
| 1310 | Fianza: actualización | 2013 | `fianza-actualizacion-1310` |
| 1312 | Requerir al propietario que deposite la fianza | 2013 | `requerir-propietario-deposite-fianza-1312` |
| 1429 | Incumplimiento de condena de hacer no personalísimo: opción por resarcimiento | 2013 | `incumplimiento-condena-hacer-no-personalisimo-opcion-1429` |
| 1430 | Incumplimiento de condena de hacer no personalísimo: opción por encargo a tercero | 2013 | `incumplimiento-condena-hacer-no-personalisimo-opcion-1430` |

## Otros (11)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 229 | Respuesta motivada de la aseguradora que deniega la indemnización | 2020 | `respuesta-motivada-aseguradora-deniega-indemnizacion-229` |
| 234 | Respuesta motivada de la aseguradora que suspende la indemnización | 2020 | `respuesta-motivada-aseguradora-suspende-indemnizacion-234` |
| 235 | Pago de la aseguradora del perjudicado por daños causados por un tercero | 2020 | `pago-aseguradora-perjudicado-danos-causados-tercero-235` |
| 243 | Cesión del derecho de uso y habitación | 2020 | `cesion-derecho-uso-habitacion-243` |
| 516 | Demanda de nulidad de venta de participaciones de SL sin cumplir estatutos y ley | 2016 | `demanda-nulidad-venta-participaciones-sl-sin-cumplir-516` |
| 577 | Promesa de venta (Navarra) | 2016 | `promesa-venta-navarra-577` |
| 909 | Consumidores y usuarios: intervención en el proceso | 2013 | `consumidores-usuarios-intervencion-proceso-909` |
| 1117 | Conceder la venia a otro letrado | 2013 | `conceder-venia-otro-letrado-1117` |
| 1205 | Acreditación de impugnación judicial de deudas con la comunidad para votar | 2013 | `acreditacion-impugnacion-judicial-deudas-comunidad-votar-1205` |
| 1225 | Acreditación de pago de cuotas adeudadas | 2013 | `acreditacion-pago-cuotas-adeudadas-1225` |
| 1407 | Acreditación de pago o consignación de cuotas atrasadas para votar | 2013 | `acreditacion-pago-consignacion-cuotas-atrasadas-votar-1407` |
