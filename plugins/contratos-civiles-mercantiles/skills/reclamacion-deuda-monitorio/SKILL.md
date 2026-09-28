---
name: reclamacion-deuda-monitorio
description: >-
  Reclama una deuda contractual de dinero: liquida principal e intereses (pactados, legales o de la Ley
  3/2004, con los 40 euros y costes de cobro) en una tabla, prepara el requerimiento previo que sirve de
  intento de negociación y redacta en Word la petición de proceso monitorio (arts. 812-818 LEC) con nota para
  el abogado. Úsala cuando el abogado diga «monitorio», «me deben facturas», «reclamar una deuda», «intereses
  de demora de la Ley de morosidad», «liquidación de intereses» o «el deudor no paga». Cubre competencia,
  MASC previo, oposición y deudores consumidores. Si la deuda consta en letra, pagaré o cheque, o en título
  ejecutivo, dilo y no uses el monitorio; si hay que resolver el contrato, usa resolucion-por-incumplimiento;
  solo el burofax, requerimiento-cumplimiento; la propuesta u oferta vinculante, masc-propuesta-acuerdo.
---

# Reclamación de deuda y proceso monitorio

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Mora, intereses e imputación de pagos** → `buscar_articulo` (`ley="CC"`, artículos `"1100"`, `"1108"`, `"1109"`, `"1172"`, `"1173"` y `"1174"`); mercantil, (`ley="CCom"`, artículos `"63"`, `"316"`, `"317"` y `"341"`).
- **Morosidad entre empresas** → `buscar_articulo` (`ley="BOE-A-2004-21830"`, artículos `"2"` a `"9"`); **tipo legal de cada semestre** → `novedades_boe` (`contiene="tipo legal de interés de demora"`, ventanas de hasta 31 días alrededor del 1 de enero y del 1 de julio) + `leer_boe` (identificador de la resolución); si `novedades_boe` no la devuelve (le ha pasado con la del primer semestre de 2026, publicada el 31/12/2025), `sumario_boe` (`fecha` de cada día entre el 28 y el 31 de diciembre o de junio y el 1 y 2 de enero o julio, `contiene="interés de demora"`).
- **Prescripción** → `buscar_articulo` (`ley="CC"`, artículos `"1964"`, `"1966"`, `"1967"`, `"1969"` y `"1973"`).
- **Monitorio, cuantía y órgano** → `buscar_articulo` (`ley="LEC"`, artículos `"812"` a `"818"`, `"23"`, `"31"`, `"249"`, `"250"` y `"576"`) y (`ley="LOPJ"`, artículos `"84"`, `"85"` y, si el deudor está en concurso, `"87"`).
- **Intento de negociación previo** → `buscar_articulo` (`ley="LO 1/2025"`, artículos `"5"`, `"6"`, `"7"`, `"9"`, `"10"` y `"17"`) y (`ley="LEC"`, artículos `"264"`, `"399"` y `"403"`).
- **Deudor consumidor** → `buscar_articulo` (`ley="TRLGDCU"`, artículos `"3"`, `"82"`, `"83"` y `"85"`); si es un préstamo, (`ley="Ley de 23 de julio de 1908"`, `articulo="1"`).
- **Doctrina** (MASC antes del monitorio en la Audiencia de la plaza, control de oficio con consumidores, interés de demora abusivo, Ley 3/2004) → `buscar_sentencias` (`base="AN"`, `jurisdiccion="CIVIL"`, `tipo_organo="AP"`, `provincia`; `base="TS"`; `base="TJUE"`) + `leer_sentencias` (`parrafos=3`).
- **Deudor que es sociedad** → `buscar_empresa_mercantil` (domicilio social vigente, que fija la competencia; disolución o concurso).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Si `buscar_articulo` devuelve una nota «Téngase en cuenta…» seguida de un texto entre comillas, ese texto es la redacción anterior (así ocurre en los arts. 250, 814 y 815 LEC): aplica la que encabeza la respuesta.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Deuda de dinero nacida de un contrato (facturas de suministro o servicios, precio aplazado, préstamo, cuotas, reconocimiento de deuda), **líquida, determinada, vencida y exigible**, de cualquier importe, acreditada con documentos del art. 812 LEC.
- Liquidar intereses de una deuda aunque no se vaya a pedir un monitorio (reclamación extrajudicial, demanda ordinaria o verbal, comunicación de créditos).

| Situación | Vía o skill |
|---|---|
| La deuda consta en letra de cambio, pagaré o cheque | Juicio cambiario (excluido del requisito de negociación previa, art. 5.2 LO 1/2025): esta skill no lo redacta; dilo al abogado |
| Hay título ejecutivo (escritura, póliza intervenida, laudo, acuerdo elevado a escritura) | Demanda ejecutiva (art. 517 LEC), sin negociación previa (art. 5.3 LO 1/2025) |
| Deudor domiciliado en otro Estado de la UE | Proceso monitorio europeo (Reglamento (CE) 1896/2006), exceptuado del MASC (art. 5.3): esta skill no lo redacta |
| Deudor en concurso | La jurisdicción del juez del concurso es exclusiva para las acciones civiles con trascendencia patrimonial contra el concursado (art. 87.7 LOPJ): comunica el crédito en el concurso; esta skill no lo redacta |
| Rentas de arrendamiento con desahucio | Juicio verbal de desahucio; con monitorio, la oposición va siempre a verbal (art. 818.3 LEC) |
| La deuda depende de resolver el contrato o de valorar daños | `resolucion-por-incumplimiento` |
| Solo hace falta el burofax de reclamación | `requerimiento-cumplimiento` |
| Hay que formular una propuesta de acuerdo u oferta vinculante confidencial | `masc-propuesta-acuerdo` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ Acreedor y deudor: nombre o denominación, DNI/NIE o CIF y **domicilio o residencia actual del deudor** (fija la competencia, art. 813 LEC); si el deudor es consumidor (art. 3 TRLGDCU) o empresa.
2. ★ Origen de la deuda: contrato (pídelo completo, con condiciones generales si las hay), pedidos, albaranes firmados, facturas, certificaciones, reconocimientos de deuda, extractos, correos.
3. ★ Cada partida: número, fecha de emisión, fecha de entrega o prestación, vencimiento pactado, importe, pagos parciales con fecha. Si la factura lleva retención del IRPF, el principal es el total a pagar al acreedor (la retención la ingresa el deudor en Hacienda al pagar): dilo en la nota.
4. ★ Pactos sobre plazo de pago, intereses ordinarios y de demora, penalidades, gastos de cobro.
5. ★ Reclamaciones previas, respuestas, reconocimientos y cualquier negociación o intento de acuerdo (con fechas y prueba de recepción).
6. ★ Si el deudor discute la deuda y por qué (calidad, cantidad, compensación): anticipa la oposición.
7. Si hay fiadores o codeudores solidarios.
8. Si hay un cálculo de intereses que el cliente ya haya enviado al deudor (para no contradecirlo; si reclamaba conceptos que ahora se excluyen, la petición lo dice expresamente).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

### 1. Antes de liquidar: exigibilidad y prescripción

- La deuda debe estar vencida y ser exigible. Si el contrato no fija plazo de pago entre empresas, la Ley 3/2004 da treinta días naturales desde la recepción de mercancías o servicios, ampliables por pacto sin superar sesenta (art. 4); las cláusulas que excedan esos plazos o excluyan intereses o costes de cobro pueden ser nulas (art. 9).
- Prescripción de cada partida (apartado 9 del formato): regla general de cinco años (arts. 1964.2 y 1969 CC); pagos por años o plazos más breves, cinco (art. 1966); tres años para los honorarios de los profesionales que enumera, los servicios de menestrales y jornaleros y el precio de géneros vendidos a quien no es comerciante o se dedica a distinto tráfico; en los servicios, desde que dejaron de prestarse (art. 1967). Si dudas entre el de tres y el de cinco años (compras de un empresario para su propia actividad), calcula los dos y trabaja con el más corto. Descarta o señala lo prescrito y lo interrumpido (art. 1973).

### 2. Liquidación en tabla

Presenta dos tablas y explica cada columna en la nota:

- **Principal**: `Partida | Documento | Fecha | Vencimiento | Importe | Pagos imputados | Pendiente`. Imputa cada pago a la deuda que designó el deudor al pagar (art. 1172 CC) o, en su defecto, a la más onerosa de las vencidas y, si todas lo son por igual, a todas a prorrata (art. 1174). Dentro de la deuda a la que se imputa, el pago cubre primero sus intereses devengados hasta ese día y solo el resto va a capital (art. 1173), también cuando el deudor designó la deuda. Explica en la nota cuánto cambiaría el total con otra imputación.
- **Intereses**: `Partida | Desde | Hasta | Días | Base | Tipo anual | Fuente del tipo | Interés`. Fórmula por defecto: base × tipo × días / 365 (usa 360 solo si está pactado). Un tramo por cada cambio de tipo.

Qué interés corresponde, por este orden:

1. **Pactado**: el del contrato. Si es un préstamo, comprueba que no sea usurario (art. 1 de la Ley de 23 de julio de 1908); si el deudor es consumidor, que no sea abusivo (apartado 5); entre empresas, que no sea abusivo en perjuicio del acreedor (art. 9 Ley 3/2004).
2. **Ley 3/2004** (operaciones comerciales entre empresas o con la Administración; nunca con consumidores, art. 3.2): mora automática al vencer el plazo, sin intimación (art. 5), si el acreedor cumplió (art. 6); tipo del BCE más ocho puntos, fijado por semestres (art. 7.2) y publicado en el BOE (art. 7.3). Obtén el tipo de cada semestre del cálculo con `novedades_boe` (`contiene="tipo legal de interés de demora"`, `desde` y `hasta` de no más de 31 días que abarquen el cambio de semestre anterior: finales de diciembre y primeros de enero, o finales de junio y primeros de julio) y léelo con `leer_boe`: cita la resolución en la tabla. Si `novedades_boe` no la encuentra, prueba `sumario_boe` en los días del cambio de semestre y, si tampoco, búscala en internet en el BOE y cítala con enlace (con su identificador, `leer_boe` suele devolverla). Añade 40 euros fijos por los costes de cobro y los costes acreditados que los superen (art. 8): la cantidad fija total (40 euros por factura, si la doctrina lo admite) se compara con los costes acreditados y se reclama además solo el exceso, sin el IVA que el acreedor pueda deducir; busca la doctrina sobre si los 40 euros se deben por cada factura.
3. **Legal del dinero** (art. 1108 CC) desde la constitución en mora (art. 1100; en obligaciones mercantiles con día señalado, desde el día siguiente al vencimiento, art. 63 CCom; en compraventa mercantil, art. 341 CCom). El tipo lo fija cada año la Ley de Presupuestos Generales del Estado o su prórroga, y Jurisprudenciator no lo devuelve: búscalo en internet en el BOE (la disposición de la ley de presupuestos que lo fija para cada año del cálculo) y cita en la tabla el enlace y la fecha de consulta. Si los presupuestos están prorrogados (art. 134.4 CE), la disposición de la última ley aprobada dirá «hasta el 31 de diciembre» de su año: cítala junto con la tabla oficial de tipos de interés legal del Banco de España para el año del cálculo. No escribas una cifra de memoria.
4. **Anatocismo**: los intereses vencidos devengan interés legal desde que se reclaman judicialmente (art. 1109 CC), también los de la Ley 3/2004 (busca la doctrina); en el préstamo mercantil, los intereses no pagados no devengan intereses salvo capitalización pactada (art. 317 CCom).
5. **Mora procesal**: desde el auto que despacha ejecución en el monitorio (art. 816.2 LEC) o la sentencia (art. 576 LEC). No la incluyas en la petición.

Hay Audiencias que inadmiten o reducen la petición cuando la deuda no viene desglosada por partidas con su liquidación: busca la doctrina de la plaza y no reclames intereses que no resulten del documento o de la ley con su cálculo. Pedir más de lo debido expone a la pluspetición (art. 818.1 LEC).

### 3. Intento de negociación previo (LO 1/2025)

- El art. 5.2 LO 1/2025 exige actividad negociadora previa en los procesos declarativos del libro II y en los especiales del libro IV de la LEC, donde está el monitorio; el monitorio no figura entre las excepciones de sus letras a) a h) (sí el juicio cambiario, letra h), y el art. 5.3 solo excluye el monitorio europeo. Varias Audiencias lo exigen para la petición monitoria e inadmiten sin él: **haz siempre el intento antes** y busca el criterio de la Audiencia de la plaza.
- Un requerimiento de pago que invite expresamente a negociar, con el objeto idéntico al de la reclamación y remitido al domicilio del deudor con prueba de recepción, fecha y contenido, ha sido considerado intento suficiente (arts. 2, 5.1 y 10.2 LO 1/2025). Redáctalo con `requerimiento-cumplimiento` o dentro de esta skill (Documentos, 2) y espera treinta días naturales desde la recepción sin reunión ni respuesta (art. 10.4.a) antes de presentar. Si el deudor contestó o hubo reuniones, la negociación termina por las otras letras del art. 10.4: treinta días sin respuesta a una propuesta concreta (b), tres meses desde la primera reunión (c) o escrito que la da por terminada (d). Si se usa oferta vinculante confidencial, el plazo es de un mes (art. 17.4): deriva a `masc-propuesta-acuerdo`.
- Una reclamación de pago sin invitación a negociar (correos, mensajes o burofax que solo exigen pagar, aunque anuncien acciones) no cumple el requisito: si es lo único que hay, redacta la invitación y no prepares la presentación inmediata de la petición.
- La solicitud interrumpe la prescripción desde el intento de comunicación (art. 7.1) y hay un año para presentar (art. 7.3). Si una partida está a punto de prescribir, envía la solicitud de inmediato: presentar la petición sin el intento no es la alternativa, porque se inadmite.
- Con la petición: documento que acredite el intento o, si no se conoce el domicilio ni el medio para requerir al deudor, declaración responsable de esa imposibilidad (art. 264.4 LEC), y descripción del proceso negociador (art. 399.3 LEC); sin ello, inadmisión (art. 403.2). Describe fechas, medio, objeto y resultado, pero no el contenido de las propuestas ni de las respuestas, y no aportes los correos o cartas con cifras cruzadas durante la negociación: son confidenciales y el tribunal los inadmite (art. 9 LO 1/2025). El documento que acredita el intento es la invitación a negociar recibida. Busca si la Audiencia de la plaza ha fijado criterios sobre intentos de contacto fallidos.

### 4. Petición de monitorio (arts. 812-818 LEC)

- **Documentos** (art. 812): firmados por el deudor o con su señal, o facturas, albaranes, certificaciones y documentos que habitualmente documentan créditos en esa relación, aunque los cree el acreedor; también documentos comerciales que acrediten una relación anterior duradera (art. 812.2).
- **Competencia exclusiva** (art. 813): el domicilio o residencia del deudor o, si no se conocen, el lugar donde pueda ser hallado; no vale la sumisión. Si el deudor aparece en otro partido, se archiva y hay que empezar de nuevo: comprueba el domicilio (sociedades: `buscar_empresa_mercantil`).
- **Órgano**: el art. 813 conserva la mención al Juzgado de Primera Instancia; tras la LO 1/2025 el órgano es el Tribunal de Instancia del partido, en su Sección Civil o en la Sección Única de Civil y de Instrucción (arts. 84 y 85 LOPJ). Pregunta al abogado cuál existe en ese partido o, si no lo sabe, compruébalo en internet en la sede judicial electrónica y cita el enlace; encabeza: «AL TRIBUNAL DE INSTANCIA DE [SEDE], SECCIÓN CIVIL» (o «SECCIÓN ÚNICA DE CIVIL Y DE INSTRUCCIÓN»).
- **Postulación**: la petición inicial no necesita abogado ni procurador, sea cual sea la cuantía (arts. 814.2, 23.2 y 31.2 LEC). La oposición sí los requiere cuando la cuantía lo exige según las reglas generales (art. 818.1): juicios verbales por cuantía de más de 2.000 euros (arts. 23.2 y 31.2).
- **Contenido** (art. 814.1): identidad del deudor, domicilios de acreedor y deudor, origen y cuantía de la deuda, con los documentos. Puede usarse el impreso o formulario oficial (art. 814.1): si el abogado lo prefiere, búscalo en internet en la sede judicial electrónica, cita el enlace y adapta el contenido a él.

### 5. Deudor consumidor

- Antes de requerir de pago, el juez examina de oficio si alguna cláusula que fundamenta la petición o determina la cantidad es abusiva y puede proponer un requerimiento por importe inferior; el acreedor acepta o rechaza en diez días; si calla, se entiende aceptada, y si rechaza se le tiene por desistido y solo puede reclamar en el declarativo que corresponda (art. 815.3 LEC). Explica al abogado esa decisión y su plazo en la nota. Aporta el contrato completo con sus condiciones generales y la liquidación separada por conceptos.
- Revisa antes las cláusulas de intereses de demora, comisiones, penalidades y vencimiento anticipado (arts. 82, 83, 85 y 87 TRLGDCU; doctrina de la Sala Primera y del Tribunal de Justicia). Si una es dudosa, reclama sin ella o avisa al abogado del riesgo. Si la cláusula de interés de demora es abusiva, se suprime sin moderarla ni sustituirla por el interés legal supletorio (busca la doctrina de la Sala Primera: `consulta="interés de demora abusivo supresión no aplicación norma supletoria interés legal"`, `base="TS"`): no pidas en su lugar el interés legal del art. 1108 CC, y di en la petición qué conceptos del contrato no se reclaman.

### 6. Qué pasa después

- **Paga**: archivo (art. 817). **No paga ni se opone**: decreto y ejecución con la mera solicitud; ni acreedor ni deudor pueden después reclamar en proceso ordinario la cantidad (art. 816).
- **Se opone** (art. 818): hasta la cuantía del juicio verbal (15.000 euros, art. 250.2), se sigue por el verbal y el acreedor puede impugnar la oposición en diez días; por encima, el acreedor debe presentar demanda de juicio ordinario en un mes desde el traslado de la oposición o se sobresee con costas. Calcula y da esas fechas en la nota. Si se opone por pluspetición, se actúa sobre la cantidad reconocida (art. 818.1).

## Jurisprudencia: qué buscar

Imprescindible para la nota (apartado 8 del formato). Reformula como máximo dos veces:

- MASC y monitorio en la plaza: `consulta="proceso monitorio requisito de procedibilidad medio adecuado de solución de controversias"`, `base="AN"`, `jurisdiccion="CIVIL"`, `tipo_organo="AP"`, `fecha_desde="03/04/2025"`, `provincia="<provincia>"`; y `consulta="requerimiento de pago solicitud de negociación intento suficiente monitorio"`.
- Liquidación y desglose: `consulta="monitorio desglose partidas liquidación de la deuda intereses"`, `base="AN"`, `tipo_organo="AP"`, `anios=3`.
- Ley 3/2004: `consulta="Ley 3/2004 morosidad interés de demora costes de cobro 40 euros"`, `base="TS"`, `jurisdiccion="CIVIL"`; y `consulta="indemnización costes de cobro 40 euros por cada factura Ley 3/2004"`, `base="AN"`, `tipo_organo="AP"`.
- Consumidores: `consulta="monitorio consumidor control de oficio cláusulas abusivas interés de demora"`, `base="TS"`; `consulta="procedimiento monitorio control de oficio cláusulas abusivas consumidor"`, `base="TJUE"`; y `consulta="interés de demora préstamo personal consumidor dos puntos porcentuales abusivo"`, `base="TS"`.
- Mora de deuda discutida: `consulta="in illiquidis non fit mora canon de razonabilidad intereses moratorios"`, `base="TS"`.

Lee con `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión) solo lo que vayas a citar en la nota; la petición monitoria no lleva jurisprudencia salvo que el criterio de la plaza sobre el MASC lo aconseje, y entonces con párrafo literal y ECLI.

## Documentos que se entregan

En todos los documentos, nombra las normas como pide el apartado 6 del formato («artículo 814 de la Ley de Enjuiciamiento Civil», «artículo 85 de la Ley Orgánica del Poder Judicial», «artículo 7 de la Ley 3/2004, de 29 de diciembre», «artículo 1108 del Código Civil», «artículo 5 de la Ley Orgánica 1/2025, de 2 de enero»), cada artículo con su norma: así los reconoce `verificar_escrito`.

1. **Liquidación de la deuda** (`liquidacion-deuda-<deudor>-<AAAAMMDD>.docx`): las dos tablas del apartado 2, con la fuente de cada tipo (resolución semestral leída con `leer_boe` o disposición del BOE en internet con enlace y fecha de consulta) y la fecha de cálculo. Se adjunta a la petición como documento.
2. **Requerimiento previo con invitación a negociar**, si no existe (`requerimiento-<deudor>-<AAAAMMDD>.docx`, apartado 5 del formato): deuda desglosada, plazo para pagar, constitución en mora, invitación expresa a negociar que defina el objeto (las mismas partidas que irán en la petición), con cauce y plazo no inferior a treinta días naturales, sin cifras de transacción; si el acreedor actuará con abogado, dilo en el escrito (art. 6.3 LO 1/2025). Envíalo al domicilio del deudor y, si lo hay, también al medio electrónico usado en las relaciones previas (art. 7.1), con prueba de recepción y contenido.
3. **Petición de proceso monitorio** (`peticion-monitorio-<acreedor>-<AAAAMMDD>.docx`, apartado 5 del formato): encabezamiento al órgano; comparecencia del acreedor; identificación y domicilio del deudor; hechos numerados (relación contractual, partidas, vencimientos, pagos, reclamaciones, intento de negociación y su resultado, condición de consumidor o empresa); fundamentos breves (arts. 812, 813, 814 y 815 LEC; art. 5 LO 1/2025; preceptos de los intereses); **SUPLICO** que se requiera de pago al deudor por la cantidad, con apercibimiento; otrosíes (medios de notificación, domicilios alternativos); lugar, fecha, firma y relación numerada de documentos.
4. **Nota para el abogado** (`nota-monitorio-<deudor>-<AAAAMMDD>.docx`, 2-4 páginas): vía elegida y descartadas; liquidación explicada; prescripción de cada partida; estado del intento de negociación con sus fechas (recepción, treinta días o un mes, un año); competencia y órgano; control de abusividad si el deudor es consumidor; escenarios tras el requerimiento judicial con plazos (arts. 816-818); jurisprudencia con párrafo literal, órgano, fecha y ECLI; datos pendientes; riesgos.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió; ninguna consulta imprescindible quedó sin resultado, y lo que Jurisprudenciator no tenía se obtuvo de una fuente oficial en internet, con enlace y fecha de consulta, y se señala en el resumen.
- [ ] Leídos con `buscar_articulo` en esta conversación LEC 812-818, 23, 31, 250 y 576; LOPJ 84 y 85; LO 1/2025 arts. 5, 7, 9 y 10; LEC 264, 399 y 403; CC 1100, 1108, 1109, 1172, 1173, 1174 y los de prescripción aplicados; Ley 3/2004 arts. 3 a 9 si se aplica; TRLGDCU si el deudor es consumidor.
- [ ] Cada tipo de interés con su fuente: pacto del contrato, resolución semestral leída con `leer_boe` o BOE en internet con enlace y fecha de consulta (y señalado en el resumen); ninguna cifra escrita de memoria.
- [ ] Deuda líquida, vencida y exigible; partidas prescritas excluidas o señaladas; pagos imputados.
- [ ] Intento de negociación acreditado (o declaración responsable) y plazo de treinta días o de un mes vencido antes de presentar; criterio de la Audiencia de la plaza buscado.
- [ ] Domicilio del deudor comprobado; órgano y denominación de la sección confirmados.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el requerimiento, la petición y la nota; avisos de «posible disonancia» contrastados con el texto leído.
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[DOMICILIO]`, `[IMPORTE]`, `[IBAN]`) en lugar de datos inventados; importes idénticos en tabla, requerimiento y petición.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado, cuantía y su composición, intento de negociación y fechas, datos que faltan, tabla de jurisprudencia, plazos con precepto y próximo paso.
