---
name: compraventa-mercantil
description: >-
  Redacta el contrato de compraventa de mercaderías o de suministro entre empresas (venta puntual,
  contrato marco con pedidos, suministro periódico, condiciones generales de venta o de compra B2B) y
  su nota para el abogado, en Word. Úsala cuando el abogado diga «contrato de suministro»,
  «compraventa mercantil», «condiciones de venta a clientes profesionales», «plazo de pago a
  proveedores», «reserva de dominio» o «Incoterm». Ajusta entrega, riesgo, examen y denuncia de
  defectos, precio y revisión, pago y morosidad, fuerza mayor y limitación de responsabilidad según
  defienda al vendedor o al comprador. Si el comprador es consumidor, usa
  condiciones-generales-consumidores; si hay reventa con exclusiva o red de distribuidores,
  agencia-distribucion-franquicia; para reclamar defectos ya aparecidos, vicios-ocultos-saneamiento.
---

# Compraventa mercantil y suministro

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Mercantilidad y régimen supletorio** → `buscar_articulo` (`ley="CCom"`, artículos `"2"`, `"50"`, `"325"` y `"326"`) y (`ley="CC"`, artículos `"1445"`, `"1447"`, `"1449"`, `"1450"`, `"1255"` y `"1256"`); consumidor o no (`ley="TRLGDCU"`, `articulo="3"`); condiciones generales impuestas (`ley="BOE-A-1998-8789"`, artículos `"5"`, `"7"` y `"8"`).
- **Entrega, riesgo, examen de la mercancía, denuncia de defectos, señal y saneamiento** → `buscar_articulo` (`ley="CCom"`, artículos `"327"` a `"345"`, uno por uno) y (`ley="CC"`, artículos `"1096"`, `"1182"`, `"1452"`, `"1462"`, `"1466"`, `"1484"`, `"1485"`, `"1486"` y `"1490"`).
- **Plazo de pago, interés de demora, costes de cobro, pactos nulos y reserva de dominio** → `buscar_articulo` (`ley="BOE-A-2004-21830"`, artículos `"2"` a `"10"`, uno por uno); mora fuera de esa ley (`ley="CCom"`, artículos `"63"` y `"341"`); reserva frente a terceros (`ley="BOE-A-1998-16717"`, artículos `"1"`, `"3"`, `"7"` y `"15"`); pagos en efectivo (`ley="BOE-A-2012-13416"`, `articulo="7"`).
- **Incumplimiento, fuerza mayor, cláusula penal y prescripción** → `buscar_articulo` (`ley="CC"`, artículos `"1101"` a `"1107"`, `"1124"`, `"1152"`, `"1154"`, `"1964"` y `"1967"`; `ley="CCom"`, `articulo="943"`).
- **Fuero, arbitraje, negociación previa y compraventa internacional** → `buscar_articulo` (`ley="LEC"`, artículos `"54"` y `"55"`; `ley="Ley 60/2003"`, `articulo="9"`; `ley="LO 1/2025"`, `articulo="5"`) y, si las partes están establecidas en Estados distintos, (`ley="BOE-A-1991-2552"`, artículos `"1"`, `"4"`, `"6"`, `"38"`, `"39"`, `"40"`, `"78"` y los demás que se vayan a usar; `ley="32008R0593"`, artículos `"3"`, `"4"` y `"12"`; `ley="32012R1215"`, artículos `"7"` y `"25"`; `ley="CC"`, `articulo="10"` para la ley que rige la propiedad de los bienes).
- **Doctrina sobre las cláusulas críticas** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; `base="AN"` + `tipo_organo="AP"` si no hay doctrina del Supremo o el asunto se litigará en esa plaza) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (existencia, estado, administradores y apoderados vigentes, concurso o disolución).
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Comprueba el texto de cada respuesta: con `ley="CCom"` y `articulo="2"` el conector devuelve a veces el artículo 2 del Real Decreto de promulgación («Un ejemplar de la edición oficial…») en lugar del artículo 2 del Código («Los actos de comercio…»); si ocurre, repite la consulta o apóyate en el artículo 50. Cita la morosidad como «artículo N de la Ley 3/2004, de 29 de diciembre» (con la fecha: sin ella el verificador puede tomar otra ley del mismo número). `verificar_escrito` no identifica la Convención de Viena (atribuye su artículo al Código Civil) ni los reglamentos de la Unión: comprueba cada uno de esos artículos con `buscar_articulo` e ignora el veredicto del verificador sobre ellos.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Venta de mercaderías entre empresarios o profesionales: venta puntual, contrato marco de suministro con pedidos sucesivos, suministro periódico con calendario, condiciones generales de venta (defiendes al proveedor) o de compra (defiendes al cliente).
- Revisión de un borrador propio antes de enviarlo a la otra parte.

Antes de redactar, pasa este detector y, si encaja otra skill, dilo al abogado y deriva:

| Situación | Skill que procede |
|---|---|
| El comprador actúa fuera de su actividad empresarial o profesional (art. 3 TRLGDCU), o las condiciones se dirigen a consumidores | `condiciones-generales-consumidores` |
| El comprador revende en un territorio con exclusiva, forma parte de una red, o quien «vende» solo promueve operaciones por cuenta del fabricante | `agencia-distribucion-franquicia` |
| El proveedor fabrica a medida o instala y esa actividad pesa más que la entrega del bien | `contrato-obra` o `prestacion-servicios` (y esta skill para la parte de suministro, si la hay) |
| Software, licencias o contenidos | `licencia-cesion-propiedad-intelectual` |
| Inmuebles, participaciones sociales o una empresa | `compraventa-inmueble` o `compraventa-participaciones` |
| Se entrega una señal y se quiere arrepentimiento con pérdida o devolución doblada | `contrato-arras` (en la venta mercantil, la señal es a cuenta del precio salvo pacto: art. 343 CCom) |
| Hay que revisar o contestar el borrador de la otra parte | `revision-contrato-semaforo` o `negociacion-contrapropuesta` |
| La mercancía ya se entregó con defectos, o el precio está impagado | `vicios-ocultos-saneamiento`, `requerimiento-cumplimiento`, `reclamacion-deuda-monitorio` o `resolucion-por-incumplimiento` |
| Se va a compartir información técnica o comercial antes de firmar | `confidencialidad-nda` |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ A quién defiende el abogado (vendedor/proveedor o comprador/cliente) y si el texto serán condiciones propias que la otra parte aceptará sin negociar o un contrato negociado.
2. ★ Partes: denominación, CIF, domicilio, firmante y cargo o poder. Si alguna actúa fuera de su actividad, para y aplica el detector.
3. ★ Mercancía: descripción, especificaciones técnicas o muestras, normas de calidad, embalaje, marcado y documentación que debe acompañarla.
4. ★ Destino que le dará el comprador (reventa, incorporación a su producción, uso en su negocio): decide si la venta es mercantil y el plazo de prescripción de la acción de precio.
5. ★ Modalidad: venta única o suministro; cómo se cursan y aceptan los pedidos (plazo de aceptación, silencio), previsiones de consumo (vinculantes o no), compras mínimas y exclusividad de compra o de suministro.
6. ★ Entrega: lugar, plazo o calendario, quién transporta y asegura, si se pacta un Incoterm (término, lugar y versión) y qué documentos se entregan.
7. ★ Precio: importe o tarifa, moneda, impuestos, descuentos y *rappels*, y si se revisará (índice oficial, fórmula, periodicidad, tope).
8. ★ Pago: plazo, forma de cómputo, facturación (agrupación de facturas), medio de pago, anticipos y garantías (aval, seguro de crédito, reserva de dominio).
9. Recepción e inspección: quién examina, cuándo y cómo; garantía comercial y plazo que quiere cada parte para reclamar defectos.
10. Responsabilidad: tope deseado, exclusión de lucro cesante o daños indirectos, seguros de responsabilidad civil y de producto.
11. Duración, prórroga, preaviso de salida y causas de resolución (en suministro).
12. Establecimiento de cada parte (si están en Estados distintos, la compraventa puede ser internacional), ley aplicable, fuero o arbitraje.
13. Si el contrato puede regirse supletoriamente por un Derecho civil propio (por ejemplo, Cataluña): pregunta y, si aplica, busca la norma con `buscar_boe` (título de la norma); si no aparece, aplica la puerta.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota su línea «vigente desde… redacción dada por…».

**Calificación.** Es mercantil la compra de muebles para revenderlos con ánimo de lucro (art. 325 CCom); el art. 326 excluye la compra para consumo del comprador, la venta de la propia cosecha o ganado y la del artesano en su taller. Lo no regulado en el Código de Comercio se rige por el Derecho común (arts. 2 y 50 CCom). Consecuencias que debes explicar en la nota según la calificación:

- Plazos de denuncia de defectos muy breves (arts. 336 y 342 CCom) frente a los seis meses del art. 1490 CC.
- No hay rescisión por lesión (art. 344 CCom); la señal se entiende a cuenta del precio salvo pacto (art. 343 CCom); el vendedor responde de evicción salvo pacto (art. 345 CCom).
- Prescripción de la acción de precio: el art. 943 CCom remite al Derecho común; el art. 1967 CC (regla 4.ª) fija tres años para el precio de los géneros vendidos por mercaderes a quien no lo es o se dedica a distinto tráfico, y el art. 1964.2 CC, cinco años para lo demás. La Sala Primera ha aplicado los tres años aunque el comprador destine la mercancía a su negocio: búscalo antes de afirmar el plazo en la nota (consulta abajo).

**Ley 3/2004, de 29 de diciembre (morosidad).** Se aplica a los pagos entre empresas, incluidos profesionales, por entrega de bienes o prestación de servicios (arts. 2.a y 3.1), y no a las operaciones con consumidores (art. 3.2.a). Comprueba y aplica:

- Plazo legal supletorio de treinta días naturales desde la recepción de la mercancía; la factura debe llegar antes de quince días; el procedimiento de aceptación o comprobación no puede exceder de treinta días, y el pacto no puede fijar un plazo superior a sesenta días naturales (art. 4.1 a 4.3). La agrupación de facturas tiene sus propios límites (art. 4.4). Son nulos los pactos que excluyan del cómputo los periodos vacacionales (art. 2.d).
- Cómputo: cuenta los sesenta días desde la recepción de la mercancía y deja el procedimiento de aceptación dentro de ellos. La lectura que los cuenta desde la aceptación (art. 4.2) o desde la recepción de la factura electrónica (art. 4.1, párrafo tercero) alarga el pago hasta unos noventa días desde la entrega y choca con la doctrina que declara imperativo el límite: si el abogado la quiere, preséntala en la nota como alternativa de riesgo, nunca como redacción por defecto.
- **Si el abogado o el cliente piden un plazo superior, excluir agosto o las vacaciones, un interés de demora rebajado o suprimir los costes de cobro, no lo redactes aunque defiendas al comprador**: el contrato recoge el máximo lícito y la nota abre con una tabla «Lo que se pidió | Lo que dice la ley | Cómo queda» con cada artículo leído, y avisa de que la cláusula ilícita sería nula y el juez integraría el contrato (art. 9.2). Un interés pactado un 70 % inferior al legal de demora se presume abusivo (art. 9.1): calcula el umbral con el tipo del semestre leído en el BOE.
- Interés de demora automático, sin intimación (art. 5), con los requisitos del art. 6; tipo pactado o, en su defecto, el legal del art. 7.2, que se publica cada semestre en el BOE (art. 7.3). No escribas la cifra de memoria: localiza la resolución del semestre con `novedades_boe` (`contiene="tipo legal de interés de demora"`, ventana de hasta 31 días alrededor del 1 de enero o del 1 de julio) y léela con `leer_boe`; si no aparece, búscala en internet en el BOE y cítala con enlace y fecha de consulta. En el contrato basta la remisión al art. 7.
- Indemnización fija por costes de cobro y costes acreditados que la superen (art. 8).
- Nulidad de las cláusulas y prácticas manifiestamente abusivas sobre plazo, interés o costes de cobro, y en todo caso de las que excluyan el interés de demora o la indemnización del art. 8 (art. 9.1); el juez integra el contrato (art. 9.2). La Sala Primera ha declarado imperativo el límite de sesenta días: localiza esa doctrina antes de justificarlo en la nota.
- Reserva de dominio: eficaz entre las partes si se pacta expresamente antes de la entrega (art. 10). Para oponerla a terceros, el art. 15 de la Ley 28/1998 exige su inscripción, y esa ley solo alcanza a bienes muebles corporales no consumibles e identificables (art. 1) con precio aplazado más de tres meses (art. 3). Si la mercancía se revende o se transforma, advierte en la nota de que la reserva protege poco y propone otras garantías.
- Si la Ley 3/2004 no se aplica, la mora mercantil se rige por los arts. 63 y 341 CCom.
- Pagos en efectivo: comprueba el límite del art. 7 de la Ley 7/2012 (`ley="BOE-A-2012-13416"`) y fija en el contrato un medio de pago trazable.

**Entrega y riesgo (Código de Comercio, con el Código Civil como supletorio).**

- Sin plazo pactado, la mercancía debe estar a disposición en veinticuatro horas (art. 337); los gastos de entrega son del vendedor hasta ponerla a disposición, pesada o medida, salvo pacto (art. 338).
- Retraso del vendedor: cumplimiento o rescisión con indemnización (art. 329); entregas parciales (art. 330); rechazo injustificado del comprador y depósito judicial (art. 332); obligación de pagar desde la puesta a disposición (art. 339); preferencia del vendedor sobre la mercancía que conserva (art. 340).
- Riesgo: pérdida antes de la entrega sin culpa del vendedor (art. 331); a cargo del comprador desde que la mercancía está a su disposición en lugar y tiempo convenidos, salvo dolo o negligencia del vendedor (art. 333); sigue a cargo del vendedor en los casos del art. 334 (venta por número, peso o medida, derecho de examen previo, entrega condicionada) con devolución del precio (art. 335). En la venta civil, arts. 1452, 1096 y 1182 CC.
- Pacta siempre el momento exacto de transmisión del riesgo. Un Incoterm solo vale como reglas privadas incorporadas por remisión y el conector no las contiene: identifica término, lugar y versión; si la nota debe explicar el reparto de gastos y riesgos, consúltalo en internet en la fuente oficial de la Cámara de Comercio Internacional y cítalo con enlace y fecha de consulta, nunca de memoria.

**Conformidad y defectos.**

- Venta sobre muestras o calidad conocida (art. 327) y géneros no vistos o con reserva de ensayo (art. 328).
- Si el comprador examina la mercancía a su contento al recibirla, pierde la acción por defectos de cantidad o calidad (art. 336, párrafo primero); en mercancía embalada, cuatro días desde el recibo (art. 336, párrafo segundo), y el vendedor puede exigir el reconocimiento en el acto de la entrega (art. 336, último párrafo). Vicios internos: treinta días desde la entrega (art. 342).
- Cuando lo entregado es inhábil para su fin o distinto de lo pactado, la Sala Primera aplica el régimen general del incumplimiento (arts. 1101 y 1124 CC) y no esos plazos: busca la doctrina y explica la distinción en la nota.
- Saneamiento civil supletorio: arts. 1484 a 1486 y 1490 CC.

**Precio.** Debe ser cierto o determinable por referencia a otra cosa cierta o por tercero (arts. 1445, 1447 y 1448 CC) y nunca queda al arbitrio de un contratante (arts. 1449 y 1256 CC): cualquier revisión se ata a un índice oficial o a una fórmula objetiva, con fecha de cálculo y derecho de salida si el aumento supera un umbral.

**Incumplimiento, fuerza mayor y limitación de responsabilidad.**

- Resolución por incumplimiento recíproco (art. 1124 CC); daños previsibles salvo dolo (art. 1107 CC).
- Fuerza mayor: nadie responde de sucesos imprevisibles o inevitables «fuera de los casos… en que así lo declare la obligación» (art. 1105 CC): define los hechos, la notificación, la suspensión y el plazo tras el cual cualquiera puede resolver.
- Es nula la renuncia a la responsabilidad por dolo (art. 1102 CC); la procedente de negligencia puede moderarse (art. 1103 CC). Entre empresas, la Sala Primera admite limitar la responsabilidad si no cubre el dolo ni vacía la obligación esencial y no genera un desequilibrio manifiesto: busca y lee la doctrina reciente antes de redactar el tope.
- Cláusula penal: sustituye a la indemnización salvo pacto (art. 1152 CC) y el juez la modera si hubo cumplimiento parcial o irregular (art. 1154 CC), pero no cuando la pena se pactó precisamente para ese incumplimiento; las penas extraordinariamente desproporcionadas pueden reducirse por el art. 1255 CC. Lee la doctrina antes de fijar importes.

**Condiciones generales B2B.** Si el texto lo impondrá una parte, cumple los requisitos de incorporación (`ley="BOE-A-1998-8789"`, artículos `"5"` y `"7"`) y evita contradecir normas imperativas (art. 8.1). La sumisión expresa a un fuero no vale en contratos de adhesión o con condiciones generales impuestas (art. 54.2 LEC): en ese caso, prevé arbitraje (art. 9 de la Ley 60/2003) o deja el fuero legal. Incluye una cláusula de negociación previa coherente con el requisito de procedibilidad del art. 5 de la LO 1/2025 y remite su ejecución a `masc-propuesta-acuerdo`.

**Compraventa internacional.** Las referencias del plugin (anclas, apartado 7) advierten de que el conector puede no traer la Convención de Viena. Pide primero su articulado con `buscar_articulo` (`ley="BOE-A-1991-2552"`, el instrumento de adhesión publicado en el BOE); si no lo devuelve, léela en internet en esa publicación del BOE y cítala con enlace y fecha de consulta, nunca de memoria. Con el texto obtenido:

- Ámbito (art. 1): se aplica si los establecimientos están en Estados contratantes. La lista de Estados contratantes no está en el BOE ni en el conector: compruébala en internet en el estado oficial de la Convención que publica la CNUDMI (uncitral.un.org) y cítala con enlace y fecha de consulta; nunca afirmes de memoria que un Estado es parte.
- Exclusión (art. 6): si la documentación no lo dice, incluye en la única ronda de preguntas si el cliente quiere excluirla. Elegir «la ley española» no la excluye, porque forma parte del Derecho español: si se mantiene, la cláusula dice «la Convención y, en lo que no regule, el Derecho español»; si se excluye, dilo expresamente y aplica entonces el Código de Comercio.
- Lo que la Convención no regula (art. 4): la validez del contrato y de sus cláusulas (limitación de responsabilidad, cláusula penal) y los efectos sobre la propiedad. La validez se examina con la ley aplicable al contrato; la reserva de dominio frente a terceros depende de la ley del lugar donde estén los bienes (art. 10 CC): si van a otro Estado, di en la nota que su eficacia depende de ese Derecho, que el conector no cubre, y refuerza el cobro con aval o seguro de crédito. Tampoco fija el tipo de interés (art. 78): sale de la ley aplicable (con ley española, art. 7 de la Ley 3/2004). La prescripción la rige la ley del contrato (art. 12 del Reglamento Roma I).
- Examen y denuncia de defectos: con la Convención no rigen los plazos de los arts. 336 y 342 CCom, sino el examen en el plazo más breve posible (art. 38), la comunicación en plazo razonable especificando la naturaleza del defecto, con el máximo de dos años (art. 39), y la pérdida de ese beneficio para el vendedor que conocía el defecto (art. 40). La cláusula concreta esos plazos (art. 6).
- Redacta la cláusula de ley aplicable y de fuero con los reglamentos de la Unión leídos (`32008R0593` y `32012R1215`).

**Tributación.** Avisa de que el abogado debe comprobar el IVA de la operación y, en operaciones intracomunitarias o de exportación, su régimen específico; no des tipos. Para doctrina, `buscar_consultas_hacienda`.

## Cláusulas clave y jurisprudencia

Para cada cláusula, aplica la posición del cliente (dato 1) y usa la opción correspondiente. Todas las consultas van con `jurisdiccion="CIVIL"` y `base="TS"` salvo que se indique otra cosa; lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar en la nota.

| Cláusula | Si defiendes al vendedor o proveedor | Si defiendes al comprador o cliente | Qué buscar |
|---|---|---|---|
| Recepción y denuncia de defectos | Reconocimiento a la entrega con acta (art. 336 CCom); reclamación escrita y motivada en plazo breve; garantía comercial limitada a reparar o sustituir | Plazo contractual de inspección y denuncia más amplio que el legal; definición de «defecto oculto»; derecho a rechazar lotes y a reponer a costa del vendedor | `consulta="compraventa mercantil vicios internos plazo treinta días artículo 342 Código de Comercio aliud pro alio"`; con la Convención de Viena, `consulta="Convención de Viena compraventa internacional de mercaderías artículo 39 plazo razonable comunicación falta de conformidad"` |
| Plazo de pago e intereses | Plazo corto con cómputo desde la entrega; interés y costes de cobro por remisión a la Ley 3/2004 | Plazo hasta el máximo legal, cómputo desde la aceptación (máximo treinta días de comprobación) | `consulta="Ley 3/2004 morosidad plazo de pago superior a sesenta días nulidad cláusula abusiva"` |
| Reserva de dominio y garantías | Reserva pactada antes de la entrega; inscripción si procede; aval o seguro de crédito; facultad expresa de suspender las entregas pendientes mientras haya facturas vencidas (el art. 1466 CC solo la da cuando no hay plazo de pago) | Reserva limitada al lote impagado; liberación automática al pago | `consulta="cláusula de reserva de dominio Ley 3/2004 compraventa de mercaderías impago"`, `base="AN"`, `tipo_organo="AP"` |
| Limitación de responsabilidad | Tope por importe del pedido o anual, exclusión de lucro cesante y daños indirectos; nunca por dolo | Excluir del tope el dolo, la culpa grave, los daños a personas y la infracción de derechos de terceros | `consulta="cláusula limitación de responsabilidad contrato entre empresas validez dolo culpa grave"`, `anios=10` |
| Penalización por retraso | Tope global; única consecuencia del retraso | Pena por día o semana acumulable a los daños («si otra cosa no se hubiere pactado», art. 1152 CC) y resolución tras un umbral | `consulta="cláusula penal moderación artículo 1154 incumplimiento previsto por las partes"` |
| Revisión de precios | Índice y fórmula con periodicidad; traslado de costes de materias primas | Tope anual y derecho a resolver si se supera | Solo arts. 1447 a 1449 y 1256 CC; si hay doctrina aplicable a su caso, cítala |
| Duración y salida (suministro) | Preaviso largo; indemnización pactada por salida anticipada | Preaviso corto; sin compras mínimas tras el preaviso | `consulta="contrato de suministro resolución unilateral preaviso duración indefinida"` |
| Prescripción de la acción de precio | Documenta la condición de comerciante del comprador y su tráfico | — | `consulta="prescripción acción de reclamación del precio compraventa artículo 1967 distinto tráfico"` |

Reglas para la nota:

- La cláusula de defectos, el plazo de pago, la limitación de responsabilidad y la cláusula penal son de validez discutida por la jurisprudencia (apartado 8 del formato): cita en la nota el párrafo literal de la resolución leída, con órgano, fecha y ECLI. Si tras dos reformulaciones no hay resolución aplicable, aplica la puerta.
- Si la resolución interpreta una redacción anterior de la Ley 3/2004, dilo y compárala con el texto vigente leído.
- Cita una Audiencia Provincial solo si no hay doctrina del Supremo o si el asunto se litigará en esa plaza, y di que es doctrina de Audiencia.

## Documentos que se entregan

Dos documentos Word maquetados según `references/formato-y-entrega-contratos.md`:

1. `contrato-suministro-<parte-principal>-<AAAAMMDD>.docx` o `contrato-compraventa-mercantil-<parte-principal>-<AAAAMMDD>.docx`.
2. `nota-suministro-<parte-principal>-<AAAAMMDD>.docx` (o `nota-compraventa-mercantil-…`).

Estructura del contrato (orden de estipulaciones):

1. REUNIDOS e INTERVIENEN (datos societarios y poder de cada firmante); EXPONEN (actividad de cada parte y destino de la mercancía, que sostiene la calificación).
2. PRIMERA.- Definiciones (Productos, Pedido, Especificaciones, Entrega, Defecto) y prelación de documentos: contrato, anexos, pedidos aceptados; exclusión expresa de las condiciones generales de la otra parte.
3. SEGUNDA.- Objeto y, en suministro, pedidos: emisión, plazo de aceptación, efectos del silencio, previsiones y compras mínimas.
4. TERCERA.- Precio, impuestos y revisión (fórmula en anexo).
5. CUARTA.- Facturación y pago: plazo con su cómputo, medio de pago, interés de demora e indemnización por costes de cobro por remisión a los arts. 7 y 8 de la Ley 3/2004, de 29 de diciembre.
6. QUINTA.- Entrega, transporte, transmisión del riesgo (Incoterm si se pacta) y documentación.
7. SEXTA.- Recepción, inspección y reclamación de defectos: procedimiento, plazos, remedios y garantía comercial.
8. SÉPTIMA.- Reserva de dominio y otras garantías de pago.
9. OCTAVA.- Responsabilidad, límite y seguros.
10. NOVENA.- Fuerza mayor.
11. DÉCIMA.- Penalizaciones, si las hay.
12. UNDÉCIMA.- Duración, prórroga y resolución (incumplimiento, concurso, cambio de control si se pacta).
13. DUODÉCIMA.- Confidencialidad y protección de datos (remite a `confidencialidad-nda` o `encargo-tratamiento-datos` si hace falta un contrato propio).
14. DECIMOTERCERA.- Cesión y subcontratación.
15. DECIMOCUARTA.- Notificaciones (direcciones y medios).
16. DECIMOQUINTA.- Negociación previa, ley aplicable y fuero o arbitraje.
17. DECIMOSEXTA.- Integridad y modificaciones por escrito.
18. Cierre, firmas y ANEXOS: especificaciones, tarifa y fórmula de revisión, calendario de entregas, modelo de pedido, protocolo de inspección, garantías.

**Reparto para la redacción rápida:** una sección por bloque de estipulaciones (`### [ESTIPULACION]`): comparecencia, expositivos, definiciones y objeto (pedidos) / precio, facturación y pago (Ley 3/2004) / entrega y riesgo, recepción y defectos, reserva de dominio / responsabilidad, fuerza mayor, penalizaciones, duración y resolución / confidencialidad, cesión, notificaciones, negociación previa, ley y fuero, integridad, firmas y anexos. La nota: apartado 11 del formato.

La nota sigue el apartado 3 del formato: calificación (mercantil o civil) y sus consecuencias, régimen de la Ley 3/2004 aplicado al plazo pactado, cláusulas críticas con su artículo y, cuando proceda, el párrafo literal de la jurisprudencia, datos pendientes (`[…]`), riesgos de redacción y fiscalidad que debe comprobarse.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Detector pasado: ninguna parte es consumidora, no es distribución ni obra; si lo era, se derivó.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos citados del CCom, del CC y de la Ley 3/2004 (`ley="BOE-A-2004-21830"`, comprobado el título que encabeza la respuesta), y los de la Ley 28/1998, la Ley 7/2012, la LEC, la Ley 60/2003 y la LO 1/2025 que se usen.
- [ ] Plazo de pago pactado no superior al máximo del art. 4.3 y cómputo coherente con el procedimiento de aceptación; interés y costes de cobro no excluidos ni rebajados de forma abusiva (art. 9).
- [ ] Momento de transmisión del riesgo, lugar de entrega e Incoterm (término, lugar y versión) coherentes entre sí.
- [ ] Precio o fórmula de revisión objetivos, sin dejar el precio al arbitrio de una parte.
- [ ] Limitación de responsabilidad sin exclusión del dolo; cláusula penal proporcionada y con su relación con los daños resuelta.
- [ ] Compraventa internacional: Convención y reglamentos leídos con `buscar_articulo` o, si el conector no los devolvió, en internet en su fuente oficial (BOE, EUR-Lex) con enlace y fecha de consulta; Estados contratantes comprobados en la CNUDMI (internet, con enlace); decidido y escrito si se excluye o no; validez de cláusulas, reserva de dominio, intereses y denuncia de defectos resueltos con los arts. 4, 38 a 40 y 78 de la Convención.
- [ ] Si se pidió un plazo de pago, un cómputo, un interés o una exclusión de costes de cobro contrarios a la Ley 3/2004, el contrato no los recoge y la nota explica la corrección con su tabla.
- [ ] Lo que no dio Jurisprudenciator y se obtuvo en internet, citado con enlace y fecha de consulta desde fuente oficial y señalado en el resumen; ninguna sentencia citada sin `buscar_por_cita` y `leer_sentencias`.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos, no hechos ni alegaciones) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); los avisos sobre la Convención y los reglamentos se han resuelto con `buscar_articulo`, y cada «posible disonancia» se ha contrastado con el apartado leído.
- [ ] Sociedades comprobadas con `buscar_empresa_mercantil`; si firma quien no consta como administrador o apoderado, dicho en la nota.
- [ ] Marcadores (`[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[IMPORTE]`, `[IBAN]`…) en lugar de datos inventados; definiciones, importes y fechas coherentes en todo el texto.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas, datos que faltan, tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene), plazos con su precepto (denuncia de defectos, pago, prescripción) y próximo paso.
