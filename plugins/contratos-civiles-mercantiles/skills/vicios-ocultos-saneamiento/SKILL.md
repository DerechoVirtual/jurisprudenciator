---
name: vicios-ocultos-saneamiento
description: >-
  Decide la vía correcta cuando la cosa vendida tiene defectos (saneamiento del Código Civil, compraventa
  mercantil, garantía de conformidad de consumo, aliud pro alio o daños de edificación de la LOE), calcula
  los plazos con su precepto y entrega en Word la reclamación extrajudicial y una nota de viabilidad. Úsala
  cuando el abogado diga «vicios ocultos», «humedades en el piso comprado», «el coche salió averiado»,
  «acción redhibitoria», «rebaja del precio», «quanti minoris», «garantía de tres años», «aliud pro alio»,
  «defectos de construcción» o «se nos pasa el plazo de seis meses». También para el vendedor que recibe la
  reclamación. Si solo hay retraso o impago, usa requerimiento-cumplimiento; para dar el contrato por resuelto
  con daños, resolucion-por-incumplimiento; para redactar un contrato de obra, contrato-obra.
---

# Vicios ocultos, aliud pro alio y garantías

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Saneamiento civil** → `buscar_articulo` (`ley="CC"`, artículos `"1461"`, `"1462"`, `"1468"`, `"1474"` y `"1484"` a `"1490"`; animales, `"1491"` a `"1499"`) y cómputo de plazos (`ley="CC"`, `articulo="5"`) y (`ley="LEC"`, `articulo="135"`).
- **Compraventa mercantil** → `buscar_articulo` (`ley="CCom"`, artículos `"325"`, `"336"`, `"342"` y `"345"`).
- **Consumo** → `buscar_articulo` (`ley="TRLGDCU"`, artículos `"3"`, `"6"`, `"10"`, `"114"`, `"115"`, `"115 bis"`, `"115 ter"`, `"116"`, `"117"`, `"118"`, `"119"`, `"119 bis"`, `"119 ter"`, `"120"`, `"121"`, `"122"`, `"124"`, `"125"` y `"127"`).
- **Edificación** → `buscar_articulo` (`ley="BOE-A-1999-21567"`, artículos `"3"`, `"17"`, `"18"` y `"19"`) y, para edificios anteriores a esa ley, (`ley="CC"`, `articulo="1591"`).
- **Aliud pro alio, error, dolo y plazo general** → `buscar_articulo` (`ley="CC"`, artículos `"1101"`, `"1124"`, `"1266"`, `"1269"`, `"1270"`, `"1301"`, `"1964"` y `"1969"`; mercantil, `ley="CCom"`, `articulo="943"`); suspensión de la caducidad por solicitud de negociación, (`ley="LO 1/2025"`, artículos `"5"`, `"7"` y `"10"`), e inadmisión de la demanda sin ese intento, (`ley="LEC"`, artículos `"264"` y `"403"`); tipo de juicio por la cuantía, (`ley="LEC"`, artículos `"249"` y `"250"`).
- **Doctrina** (naturaleza del plazo del art. 1490, aliud pro alio, plazos mercantiles, cláusulas de exoneración, conformidad de consumo, LOE) → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CIVIL"`; Audiencias: `base="AN"`, `tipo_organo="AP"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (vendedor, promotora, constructora: existencia, disolución, concurso); **inmuebles** → `consultar_catastro` (año de construcción, superficie) y nota simple del Registro de la Propiedad.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). En varios artículos del TRLGDCU (116, 120, 121, 122, 124…), `buscar_articulo` devuelve primero la redacción vigente desde el 1 de enero de 2022 y, tras la nota «Téngase en cuenta…», un texto entre comillas que es la redacción anterior: usa la primera salvo que el contrato sea anterior y la anterior le resulte aplicable (detector). Lo mismo vale para cualquier otra norma que devuelva ese formato.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Comprador de vivienda, local, vehículo, maquinaria, mercancía o animal que descubre defectos tras la entrega.
- Comprador que recibe algo distinto de lo pactado o inservible para el fin del contrato.
- Propietario de un edificio nuevo o reformado con daños por vicios de construcción.
- Vendedor, promotor o proveedor que recibe la reclamación y quiere saber si está en plazo y qué debe.

| Situación | Skill |
|---|---|
| No hay defecto: retraso en la entrega o impago | `requerimiento-cumplimiento` |
| El cliente quiere resolver el contrato con daños y cláusula penal por un incumplimiento que no es de saneamiento | `resolucion-por-incumplimiento` |
| El defecto está en condiciones generales abusivas de un contrato con consumidor | `condiciones-generales-consumidores` |
| Hay que acreditar el intento de negociación con una propuesta u oferta vinculante antes de demandar | `masc-propuesta-acuerdo` |
| Redactar o revisar el contrato de obra o de reforma | `contrato-obra` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende el abogado: comprador o vendedor (o agente de la edificación).
2. ★ Quién vende y quién compra: particular, empresario o profesional, consumidor (art. 3 TRLGDCU); si el comprador compró para revender (art. 325 CCom).
3. ★ Objeto: bien mueble (nuevo o de segunda mano, con elementos digitales), inmueble (usado o de nueva construcción), animal, contenido o servicio digital.
4. ★ Fechas: contrato, **entrega** (puesta en posesión o escritura pública, art. 1462 CC), recepción de la obra si es edificación, aparición o conocimiento del defecto, primera reclamación y su forma.
5. ★ Defecto: descripción, cómo se detectó, informe técnico o pericial, fotografías, acta notarial; si era visible o detectable por un perito al comprar; si el comprador es profesional del ramo.
6. ★ Contrato: cláusulas de saneamiento, de exoneración («en el estado en que se encuentra», «como cuerpo cierto»), de garantía comercial, de inspección o aceptación; precio y forma de pago.
7. ★ Qué quiere el cliente: devolver la cosa y recuperar el precio, rebaja del precio, reparación o sustitución, daños.
8. Si el vendedor conocía el defecto y lo ocultó (condiciona daños, exoneración y error).
9. Si aplica Derecho civil foral o autonómico (en Cataluña, la compraventa tiene regulación propia en su Código civil): búscalo con `buscar_boe`; `buscar_articulo` no resuelve la numeración con guion, así que lee esos preceptos en internet en el texto consolidado oficial y cítalos con enlace.

## Detector de la vía correcta

Pasa el caso por esta tabla antes de redactar. Lee cada precepto con `buscar_articulo` y di al abogado qué vías caben y cuál recomiendas. Si caben varias, la nota propone ejercitarlas de forma principal y subsidiaria.

| Supuesto | Régimen | Plazo que decide | Desde |
|---|---|---|---|
| Consumidor compra un bien mueble a un empresario, contrato desde el 1 de enero de 2022 | Garantía de conformidad: TRLGDCU arts. 114-127 (incompatible con el saneamiento civil, art. 116) | El empresario responde de las faltas que se manifiesten en tres años (bienes) o dos (contenidos y servicios digitales); segunda mano: pacto no inferior a un año (art. 120). Presunción de preexistencia: dos años o uno (art. 121). La acción prescribe a los cinco años (art. 124) | Entrega (arts. 120 y 121); manifestación de la falta (art. 124) |
| Consumo, contrato anterior al 1 de enero de 2022 | Redacción anterior de esos artículos (texto entre comillas tras «Téngase en cuenta…») | La que diga esa redacción | Busca el régimen transitorio del Real Decreto-ley 7/2021 con `buscar_boe`; si el conector no lo devuelve, léelo en internet en el BOE y cítalo con enlace; no lo supongas |
| Compraventa civil (particulares; consumidor que compra vivienda: la garantía de consumo se refiere a bienes muebles, arts. 6 y 114 TRLGDCU) | Saneamiento, CC arts. 1484-1490 | Seis meses (art. 1490), plazo que la jurisprudencia trata como de caducidad: búscalo | Entrega |
| Compraventa mercantil (art. 325 CCom) | CCom arts. 336, 342 y 345, con el CC | Faltas de cantidad o calidad en mercancías enfardadas o embaladas: cuatro días desde el recibo (art. 336); vicios internos: reclamación en treinta días desde la entrega (art. 342) y acción judicial en el plazo del art. 1490 CC según la doctrina: búscala | Recibo o entrega |
| Animales | CC arts. 1491-1499 | Acción redhibitoria en cuarenta días, salvo usos locales (art. 1496) | Entrega |
| Cosa distinta de la pactada o inhábil para su fin (aliud pro alio) | Incumplimiento: CC arts. 1124 y 1101 | Acción personal, cinco años (art. 1964.2); no le alcanza la caducidad del saneamiento (doctrina) | Desde que pudo exigirse |
| Daños materiales en un edificio por vicios de construcción | LOE arts. 17-19, frente a los agentes (promotor, constructor, técnicos), compatible con las acciones contractuales frente al vendedor (art. 17.1 y 17.9) | Garantía: diez años (estructura), tres (habitabilidad, art. 3.1.c) y uno (acabados, constructor), desde la recepción de la obra; acción: dos años desde que se producen los daños (art. 18) | Recepción de la obra y aparición del daño |
| Edificio sujeto al régimen anterior a la LOE | CC art. 1591 | Diez años (ruina) y quince por incumplimiento del contrato (art. 1591) | Conclusión de la construcción; confirma con `buscar_boe` (o, si no la devuelve, en internet en el BOE, con enlace) la disposición transitoria de la Ley 38/1999 |
| Error sustancial sobre la cosa | Nulidad por error: CC arts. 1266 y 1301 | Cuatro años (art. 1301) | Consumación del contrato |
| Vendedor que conocía el vicio y lo ocultó | Además del saneamiento (sin que le valga la cláusula de exoneración, art. 1485), dolo: CC arts. 1269 y 1270 (anulación si es grave; daños si es incidental) | Cuatro años para la anulación (art. 1301) | Consumación del contrato. Busca la doctrina antes de usar el dolo para eludir los seis meses del art. 1490: si no la hay, plantéalo solo como subsidiario y no dejes caducar el saneamiento |

## Régimen jurídico y comprobaciones

### 1. Saneamiento civil (CC arts. 1484-1490)

- **Requisitos** (art. 1484): defecto oculto (no manifiesto ni a la vista, y no fácilmente cognoscible para un comprador perito por su oficio), grave (hace la cosa impropia para su uso o disminuye este de modo que no se habría comprado o se habría pagado menos) y existente al vender (busca la doctrina sobre la prueba de la preexistencia). En vivienda usada, la entrega se refiere al estado del inmueble al perfeccionarse el contrato (art. 1468): busca cómo tratan las Audiencias el desgaste propio de la antigüedad, que no suele considerarse vicio.
- **Responsabilidad** aunque el vendedor ignorase el defecto (art. 1485). El pacto de exclusión solo vale si el vendedor ignoraba el vicio (art. 1485, párrafo segundo): la cláusula «en el estado en que se encuentra» no cubre lo que el vendedor conocía y calló. Busca la doctrina de Audiencias sobre estas cláusulas.
- **Opciones** (art. 1486): desistir del contrato con abono de gastos (redhibitoria) o rebaja proporcional del precio a juicio de peritos (quanti minoris). La rebaja no equivale sin más al coste de dejar la cosa como nueva: pide al perito el desglose por capítulos y la valoración de la rebaja proporcional, y busca cómo la cuantifican las Audiencias. Daños solo si el vendedor conocía el defecto y no lo manifestó y el comprador opta por la rescisión (art. 1486, párrafo segundo). Pérdida de la cosa: arts. 1487 y 1488.
- **Plazo**: seis meses desde la entrega (art. 1490). Cómputo de fecha a fecha (art. 5.1 CC), sin excluir inhábiles (art. 5.2). Un burofax no interrumpe un plazo de caducidad. La presentación hasta las quince horas del día hábil siguiente (art. 135.5 LEC) se ha admitido para este plazo: busca la doctrina reciente antes de apoyarte en ella y, en todo caso, no apures.
- **Suspensión por solicitud de negociación**: la solicitud a la otra parte para negociar un medio adecuado, con el objeto bien definido, suspende la caducidad desde que consta el intento de comunicación (art. 7.1 LO 1/2025), pero el cómputo se reanuda si en treinta días naturales no hay reunión ni respuesta escrita. Redacta la reclamación como solicitud de negociación (apartado 5), pero calcula la fecha final en el supuesto más desfavorable, sin contar la suspensión, y da aparte la que resultaría con ella. Busca doctrina de Audiencias sobre este precepto y la caducidad.
- **Plazo a punto de vencer sin intento de negociación.** La demanda no se admite sin el documento que acredite el intento (arts. 264.4 y 403.2 LEC): presentarla antes de que el intento termine la expone a la inadmisión, que no salva la caducidad. Recomienda enviar la solicitud de negociación el mismo día, por el domicilio del vendedor y por el medio electrónico usado entre las partes; calcula los días de caducidad que quedaban al enviarla (cuenta como consumido el día del envío) y la fecha de reanudación: treinta días naturales desde la recepción sin reunión ni respuesta escrita (si la envías por dos medios, desde la recepción **más temprana**, que suele ser la del medio electrónico el mismo día; si no llega a recibirse, desde el intento de comunicación, art. 7.1 LO 1/2025), o la fecha del escrito que dé por terminada la negociación (art. 10.4 LO 1/2025); y la fecha final resultante, que es la del supuesto más desfavorable; y deja la demanda preparada para presentarla el día en que termine el intento. Da también la fecha final sin suspensión y el margen del art. 135.5 LEC, como rescate y no como plan.

### 2. Consumo (TRLGDCU arts. 114-127, redacción vigente desde el 1 de enero de 2022)

- Ámbito (art. 114): compraventa de bienes y suministro de contenidos o servicios digitales entre empresario y consumidor (art. 3); no animales vivos ni servicios no digitales (art. 114.2). Los derechos son irrenunciables (art. 10).
- Conformidad (arts. 115 a 115 quater) y derechos (art. 117): por simple declaración, subsanación, reducción del precio o resolución, más daños si proceden, y derecho a suspender el pago pendiente. Primero reparación o sustitución a elección del consumidor salvo imposibilidad o coste desproporcionado (art. 118); rebaja o resolución en los casos del art. 119; la resolución no procede si la falta es de escasa importancia (art. 119 ter).
- Plazos: arts. 120 (tres años, dos en digital; segunda mano, pacto de al menos un año), 121 (presunción), 122 (suspensión durante la puesta en conformidad y un año más de responsabilidad por la misma falta) y 124 (prescripción de cinco años desde la manifestación). Acción directa contra el productor si dirigirse al vendedor es imposible o excesivamente gravoso (art. 125). Garantía comercial adicional (art. 127).
- El ejercicio de estas acciones es incompatible con el saneamiento civil (art. 116): elige y dilo en la nota.

### 3. Compraventa mercantil

- Es mercantil la compra de muebles para revenderlos con ánimo de lucro (art. 325 CCom); si no lo es, rige el CC.
- Si el comprador examinó la mercancía a su contento al recibirla, pierde la acción por vicios o faltas de cantidad o calidad (art. 336, párrafo primero); el vendedor puede exigir ese reconocimiento en la entrega (último párrafo).
- Mercancías enfardadas o embaladas: cuatro días desde el recibo (art. 336). Vicios internos: reclamación dentro de los treinta días siguientes a la entrega, o se pierde toda acción (art. 342). Busca la doctrina sobre la relación entre ese plazo de denuncia y el de ejercicio de la acción.
- El vendedor queda obligado al saneamiento salvo pacto (art. 345).

### 4. Aliud pro alio

Cuando la cosa es distinta o tan inhábil que el comprador no obtiene lo que compró, la Sala Primera admite la acción de incumplimiento (arts. 1124 y 1101 CC) con el plazo general, no el de seis meses. En la compraventa mercantil tampoco le alcanzan los plazos de los arts. 336 y 342 CCom: la inhabilidad total no es vicio interno (busca la doctrina). Las sentencias anteriores a la Ley 42/2015 hablan de quince años: para obligaciones nacidas desde el 7 de octubre de 2015 el plazo del art. 1964.2 CC es de cinco años. Cosa distinta: el modelo o las especificaciones esenciales del contrato no coinciden con lo entregado; inhabilidad: la cosa no sirve para el uso pactado o no puede comercializarse legalmente (falta de marcado CE o de la documentación exigida: busca la norma sectorial con `buscar_boe` y lee su artículo). Busca la doctrina y compara el caso con los supuestos que ha admitido; si hay duda, plantea el aliud pro alio como acción principal y el saneamiento como subsidiaria (o al revés si el plazo de saneamiento sigue abierto y el defecto es claramente un vicio).

### 5. Edificación (LOE)

- Responsables frente a propietarios y terceros adquirentes (art. 17.1): responsabilidad individual (art. 17.2), solidaria si no puede individualizarse (art. 17.3), promotor siempre solidario frente a los adquirentes. Exoneración por caso fortuito, fuerza mayor, acto de tercero o del perjudicado (art. 17.8).
- Distingue plazo de garantía (el daño debe aparecer dentro de él) y plazo de ejercicio de la acción (dos años desde que se produce el daño, art. 18.1). Busca la doctrina sobre esa distinción y sobre los daños continuados.
- Seguros y garantías del art. 19: pide la póliza decenal y la de la promotora; recomienda dirigir la reclamación también a la aseguradora cuando exista.
- Consulta el año de construcción con `consultar_catastro` para decidir si rige la LOE o el art. 1591 CC (en País Vasco y Navarra, en su catastro foral en internet, con enlace).

## Jurisprudencia: qué buscar

Imprescindible para la nota de viabilidad (apartado 8 del formato). Reformula como máximo dos veces:

- Plazo del art. 1490: `consulta="vicios ocultos plazo seis meses artículo 1490 caducidad"`, `base="TS"`, `jurisdiccion="CIVIL"`; y `consulta="caducidad acción saneamiento presentación día hábil siguiente artículo 135.5"`, `base="TS"`.
- Aliud pro alio: `consulta="aliud pro alio inhabilidad del objeto incumplimiento artículo 1124 vicios ocultos plazo"`, `base="TS"`.
- Mercantil: `consulta="compraventa mercantil vicios internos artículo 342 Código de Comercio treinta días"`, `base="TS"`; y `consulta="compraventa mercantil maquinaria aliud pro alio no aplicables plazos artículos 336 y 342"`, `base="TS"`.
- Requisitos y vivienda usada: `consulta="vicios ocultos requisitos preexistentes graves ocultos compraventa vivienda usada"`, `base="AN"`, `tipo_organo="AP"`, `anios=4` (añade `provincia` si se litiga allí; si no hay resultados en la provincia, el conector devuelve doctrina del Supremo o usa otra Audiencia diciendo cuál). Para cuantificar la rebaja, lee la que la calcule por capítulos de reparación.
- Exoneración: `consulta="vicios ocultos cláusula exoneración estado en que se encuentra vendedor conocía"`, `base="AN"`, `tipo_organo="AP"`.
- Consumo: `consulta="falta de conformidad garantía tres años presunción texto refundido consumidores"`, `base="AN"`, `tipo_organo="AP"`, `anios=3`.
- LOE: `consulta="Ley de Ordenación de la Edificación plazo de garantía y plazo de ejercicio de la acción daños"`, `base="TS"`.
- Solicitud de negociación y caducidad: `consulta="medio adecuado de solución de controversias suspensión de la caducidad solicitud de negociación"`, `base="AN"`, `tipo_organo="AP"`, `fecha_desde="03/04/2025"`.

Lee con `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión) solo lo que vayas a citar; transcribe fundamentos, nunca los hechos ni los nombres de aquel pleito.

## Documentos que se entregan

En la reclamación y en la nota, nombra las normas como pide el apartado 6 del formato («artículo 1490 del Código Civil», «artículo 342 del Código de Comercio», «artículo 120 del Real Decreto Legislativo 1/2007», «artículo 17 de la Ley 38/1999, de 5 de noviembre, de Ordenación de la Edificación», «artículo 7 de la Ley Orgánica 1/2025, de 2 de enero»), cada artículo con su norma: así los reconoce `verificar_escrito`.

**1. Reclamación extrajudicial** (`requerimiento-<destinatario>-<AAAAMMDD>.docx`, apartado 5 del formato), sin jurisprudencia:

1. Remitente y destinatario con domicilio; lugar, fecha y medio de envío con prueba de recepción y contenido.
2. Hechos numerados: contrato, entrega (fecha), defecto con su descripción técnica y documento que lo acredita, fecha de conocimiento.
3. Declaración de la opción que ejercita el cliente con su precepto: desistimiento o rebaja (art. 1486 CC), puesta en conformidad, rebaja o resolución (arts. 117-119 ter TRLGDCU), denuncia del vicio interno (art. 342 CCom), cumplimiento por aliud pro alio (art. 1124 CC) o reparación de daños (art. 17 LOE).
4. Petición concreta con importe o actuación y plazo.
5. Solicitud expresa de negociación con objeto definido y cauce (reunión, respuesta escrita), para suspender la caducidad y cumplir el intento previo a la demanda (arts. 5 y 7 LO 1/2025); sin cifras de transacción, que van con `masc-propuesta-acuerdo`.
6. Reserva de acciones y firma.

Para el vendedor: **contestación** (`contestacion-requerimiento-<remitente>-<AAAAMMDD>.docx`) con la excepción de caducidad o prescripción calculada, el carácter aparente o perito del comprador, la cláusula de exoneración y la causa del defecto, sin reconocer hechos.

**2. Nota de viabilidad** (`nota-viabilidad-vicios-<parte-principal>-<AAAAMMDD>.docx`, 2-5 páginas): resultado del detector y vía recomendada; requisitos y prueba de cada uno (informe pericial, acta notarial, conservación de la cosa); **tabla de plazos** (vía · precepto · fecha inicial · fecha final calculada · estado); jurisprudencia con párrafo literal, órgano, fecha y ECLI; riesgos (caducidad, exoneración, carga de la prueba, compatibilidad de acciones); estrategia procesal (acciones principales y subsidiarias, legitimados pasivos, aseguradoras) y próximo paso.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió; ninguna consulta imprescindible quedó sin resultado, y lo que Jurisprudenciator no tenía se obtuvo de una fuente oficial en internet, con enlace y fecha de consulta, y se señala en el resumen.
- [ ] Detector pasado: posición de cada parte (consumidor, empresario, particular), objeto y fechas; vías compatibles e incompatibles (art. 116 TRLGDCU) señaladas.
- [ ] Leídos con `buscar_articulo` en esta conversación los preceptos de la vía elegida (CC 1484-1490, 5 y LEC 135; CCom 336, 342 y 345; TRLGDCU 114-127; LOE 17 y 18; CC 1124, 1964 o 1301), con su línea de vigencia y, en consumo, la redacción aplicable por fecha del contrato.
- [ ] Cada plazo con fecha inicial, precepto y fecha final; el de caducidad calculado sin interrupciones ni suspensión (y, aparte, con la suspensión del art. 7.1 LO 1/2025 si se envió solicitud de negociación).
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre la reclamación y la nota; avisos de «posible disonancia» contrastados con el texto leído.
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[DOMICILIO]`, `[REFERENCIA CATASTRAL]`, `[IMPORTE]`) en lugar de datos inventados; fechas e importes coherentes entre documentos.
- [ ] Resumen para el abogado según el apartado 10 del formato: vía y por qué, plazos con precepto y fecha final, documentos y pruebas que faltan, riesgos, tabla de jurisprudencia y próximo paso.
