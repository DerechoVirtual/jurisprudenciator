---
name: requerimiento-cumplimiento
description: >-
  Redacta en Word el requerimiento o burofax que exige cumplir o pagar, con nota para el abogado, o la
  contestación de quien lo recibe. Úsala cuando el abogado diga «burofax de reclamación», «requerimiento de
  pago», «constituir en mora», «intimación resolutoria del 1504», «interrumpir la prescripción» o «reclamar antes
  de demandar». Fija qué se exige, en qué plazo y con qué consecuencias, y ajusta mora (art. 1100 CC, art. 63
  CCom), prescripción (art. 1973 CC), costas (art. 395 LEC), desahucio (art. 22.4 LEC) e intento de negociación
  (LO 1/2025). Si el cliente ya quiere resolver, usa resolucion-por-incumplimiento; para acreditar el MASC con
  propuesta u oferta vinculante, masc-propuesta-acuerdo; para liquidar y pedir monitorio,
  reclamacion-deuda-monitorio; defectos de la cosa, vicios-ocultos-saneamiento.
---

# Requerimiento de cumplimiento, pago o constitución en mora

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Mora, intereses y plazo de la obligación** → `buscar_articulo` (`ley="CC"`, artículos `"1096"`, `"1100"`, `"1101"`, `"1108"` y `"1128"`); si la obligación es mercantil, (`ley="CCom"`, `articulo="63"`); si es una operación comercial entre empresas, (`ley="BOE-A-2004-21830"`, artículos `"3"`, `"4"`, `"5"`, `"7"` y `"8"`).
- **Tipo de interés de demora de la Ley 3/2004 de cada semestre** → `novedades_boe` (`contiene="interés de demora"`, con `desde` y `hasta` obligatorios y una ventana de 31 días como máximo: del 15/12 al 14/01 para el primer semestre, del 15/06 al 15/07 para el segundo) y `leer_boe` con el identificador de la resolución de la Secretaría General del Tesoro que aparezca.
- **Prescripción y su interrupción** → `buscar_articulo` (`ley="CC"`, artículos `"1964"`, `"1966"`, `"1967"`, `"1969"`, `"1973"`, `"1974"` y `"1975"`); obligaciones mercantiles, (`ley="CCom"`, `articulo="943"`).
- **Intimación resolutoria y arrendamientos** → `buscar_articulo` (`ley="CC"`, artículos `"1124"` y `"1504"`); condición resolutoria inscrita, (`ley="BOE-A-1946-2453"`, artículos `"11"` y `"37"`) y Reglamento Hipotecario (`ley="BOE-A-1947-3843"`, `articulo="175"`); rentas: (`ley="LEC"`, `articulo="22"`) y (`ley="LAU"`, artículos `"27"` y `"35"`).
- **Costas e intento de negociación previo** → `buscar_articulo` (`ley="LEC"`, artículos `"394"` y `"395"`) y (`ley="LO 1/2025"`, artículos `"2"`, `"5"`, `"7"`, `"9"` y `"10"`).
- **Doctrina de la Sala Primera** (requerimiento del art. 1504, carácter recepticio de la reclamación, comunicación frustrada por el destinatario, mora) → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CIVIL"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Requerimiento como intento de negociación** → `buscar_sentencias` (`base="AN"`, `jurisdiccion="CIVIL"`, `tipo_organo="AP"`, `fecha_desde="03/04/2025"` y, si se sabe dónde se demandará, `provincia`).
- **Destinatario que es sociedad** → `buscar_empresa_mercantil` (denominación o CIF: domicilio social vigente, administradores, disolución o concurso).
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Si `buscar_articulo` devuelve una nota «Téngase en cuenta…» seguida de un texto entre comillas, ese texto entrecomillado es la redacción anterior: aplica la que encabeza la respuesta.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- El acreedor quiere exigir el cumplimiento de una obligación (pagar, entregar, hacer o dejar de hacer) antes de acudir al juzgado, o constituir en mora al deudor para que corran intereses y riesgos.
- Hay que interrumpir una prescripción que se acerca, dejar preparada la condena en costas si el demandado se allana o impedir que el arrendatario enerve el desahucio.
- Compraventa de inmueble con precio aplazado impagado y el vendedor quiere cerrar la puerta al pago tardío (intimación del art. 1504 CC).
- El cliente **ha recibido** un requerimiento y hay que contestarlo sin reconocer la deuda ni perder defensas.

| Situación | Skill |
|---|---|
| Aún no está claro qué quiere el cliente ni qué vía conviene | `contratos-intake` |
| El cliente decide dar el contrato por resuelto, reclamar la cláusula penal o los daños | `resolucion-por-incumplimiento` |
| La cosa entregada tiene defectos o no es la pactada | `vicios-ocultos-saneamiento` |
| Deuda dineraria documentada: liquidación con intereses y petición de monitorio | `reclamacion-deuda-monitorio` |
| Hay que acreditar el requisito de procedibilidad con una propuesta de acuerdo u oferta vinculante confidencial | `masc-propuesta-acuerdo` |
| El contrato requerido está mal redactado o su sentido es dudoso | `dictamen-interpretacion-contrato` |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ A quién defiende el abogado: al que requiere o al requerido.
2. ★ Partes: nombre o denominación, DNI/NIE o CIF y **domicilio donde se enviará** (el designado en el contrato para notificaciones, el domicilio social vigente o el lugar de trabajo); medio electrónico que usan habitualmente en sus relaciones. Si hay fiadores o codeudores solidarios, los suyos también.
3. ★ Contrato: fecha, tipo, cláusulas de la obligación incumplida, plazo o fecha de cumplimiento pactados, cláusula de notificaciones, cláusula penal o de intereses, cláusula resolutoria, sumisión a mediación o arbitraje. Pide el documento.
4. ★ Incumplimiento: qué falta, desde cuándo, importe exacto y cómo se calcula (facturas, vencimientos, entregas parciales), y si el cliente ha cumplido lo suyo.
5. ★ Fechas de exigibilidad de cada obligación y de cualquier reclamación, reconocimiento o pago parcial anterior (para calcular la prescripción).
6. ★ Efecto que busca el cliente: pago o cumplimiento, mora e intereses, interrumpir la prescripción, preparar la resolución, costas, desahucio o intento de negociación previo a la demanda.
7. Si el deudor es consumidor y el contrato tiene condiciones generales (condiciona qué intereses o penalidades se pueden exigir).
8. Si aplica Derecho civil foral o autonómico (Cataluña, Aragón, Navarra, País Vasco, Galicia, Baleares): busca la norma con `buscar_boe` y, si el conector no devuelve el precepto (no resuelve, por ejemplo, la numeración con guion del Código civil de Cataluña), léelo en internet en el texto consolidado oficial y cítalo con enlace.
9. Medio de envío que prefiere el despacho (burofax con certificación de texto y acuse de recibo, acta notarial, comunicación electrónica certificada).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo, y anota la línea «vigente desde… redacción vigente dada por…».

### 1. Qué efecto produce el requerimiento y qué forma exige

| Efecto buscado | Precepto | Requisito y trampa |
|---|---|---|
| Constituir en mora | art. 1100 CC | Exigencia judicial o extrajudicial. No hace falta si la obligación o la ley lo declaran o si el plazo fue determinante (art. 1100, párrafo segundo). En obligaciones recíprocas no hay mora si el requirente no cumple o no se allana a cumplir lo suyo (último párrafo): comprueba antes qué ha cumplido el cliente. Efectos: intereses (art. 1108), daños (art. 1101) y caso fortuito a cargo del moroso (art. 1096). |
| Mora en obligación mercantil | art. 63 CCom | Con día señalado, la mora empieza al día siguiente del vencimiento sin requerimiento. Sin día señalado exige interpelación judicial o protesta ante juez, notario u otro oficial público: un burofax no basta; propón acta notarial. |
| Mora en operación comercial entre empresas | arts. 3, 5, 7 y 8 Ley 3/2004 | Mora automática al vencer el plazo pactado o legal (art. 4, con un máximo pactable de sesenta días naturales), sin intimación. Tipo legal (art. 7): el del BCE más ocho puntos, publicado cada semestre en el BOE; liquida factura por factura y semestre por semestre con el tipo leído en esta conversación. 40 euros fijos de costes de cobro **por cada factura** impagada (busca la doctrina del TJUE) y los costes acreditados que los superen (art. 8). No se aplica si interviene un consumidor ni a deudas en concurso (art. 3.2). El requerimiento sigue siendo útil para prescripción, costas y negociación. |
| Interrumpir la prescripción | arts. 1973-1975 CC | Basta la reclamación extrajudicial, pero es recepticia: surte efecto cuando llega al deudor (busca la doctrina). El plazo se reinicia entero. Solidarios: aprovecha a todos (art. 1974); mancomunados: solo respecto de la parte reclamada. **Fiador**: la reclamación extrajudicial al deudor no le perjudica (art. 1975): requiérele por separado. Un plazo de **caducidad** (p. ej., art. 1490 CC) no se interrumpe con un burofax: deriva a `vicios-ocultos-saneamiento` o `masc-propuesta-acuerdo`. |
| Intimación resolutoria en venta de inmuebles | art. 1504 CC | Solo «judicialmente o por acta notarial»: el burofax no vale aunque el abogado lo pida así; díselo antes de redactar y entrega el texto para el acta. Debe hacerse vencido el plazo de pago y expresar de forma inequívoca la voluntad de resolver (una reserva de acciones no basta); puede conceder un último plazo breve con resolución automática si no se paga en él (busca la doctrina). Hecho el requerimiento, el juez no puede conceder nuevo término y el pago posterior no rehabilita el contrato; si el comprador paga antes de recibirlo, no cabe resolver por ese impago: urge practicarlo. Con condición resolutoria inscrita, cancelar la inscripción del comprador exige además consignar lo que haya de devolverse (art. 175 del Reglamento Hipotecario, regla sexta). |
| Impedir la enervación del desahucio | art. 22.4 LEC | Requerimiento de pago por medio fehaciente con al menos treinta días de antelación a la demanda, y pago no efectuado al presentarla. Arrendamiento inscrito con pacto resolutorio: requerimiento judicial o notarial del art. 27.4 LAU. |
| Costas si el demandado se allana | art. 395.1 LEC | Hay mala fe si antes de la demanda se le requirió «de forma fehaciente y justificada» o rechazó el acuerdo o el medio adecuado: el requerimiento debe ser concreto, cuantificado y documentado. |
| Intento de negociación previo a la demanda | arts. 2, 5.1, 7, 9 y 10 LO 1/2025 | Ver apartado 3. |

### 2. Prescripción: calcula antes de redactar

- Acciones personales sin plazo especial: cinco años desde que pudo exigirse el cumplimiento (art. 1964.2 CC, y art. 1969); las mercantiles sin plazo propio se rigen por el Derecho común (art. 943 CCom). Pagos por años o plazos más breves y rentas: cinco años (art. 1966). Honorarios de profesionales, servicios de menestrales y precio de géneros vendidos por comerciantes a quien no lo es **o, siéndolo, se dedica a distinto tráfico**: tres años desde que dejaron de prestarse los servicios (art. 1967): encaja cada deuda en su supuesto con el texto leído. Si el comprador es una empresa que no revende lo comprado (instalador, constructor, fabricante que lo consume), no descartes los tres años: da las dos fechas y trabaja con la más prudente.
- Da al abogado, por cada crédito, la fecha de exigibilidad, el precepto, la fecha final del plazo y la nueva fecha final si el requerimiento se recibe en la fecha prevista (apartado 9 del formato). Si no consta la fecha de exigibilidad, pídela: sin ella no se da plazo.
- Si la obligación nació antes del 7 de octubre de 2015 (redacción del art. 1964 por la Ley 42/2015), avisa de que hay régimen transitorio y comprueba con `buscar_boe` la disposición transitoria de esa ley; si el conector no la devuelve, léela en internet en el BOE (texto de la Ley 42/2015) y cítala con enlace y fecha de consulta; nunca calcules ese tramo de memoria.
- Si el plazo vence antes de que el requerimiento pueda llegar, no confíes en él: recomienda al abogado presentar la demanda o la solicitud que interrumpa con fecha cierta.

### 3. El requerimiento como intento de negociación (LO 1/2025)

La demanda civil exige haber acudido antes a un medio adecuado de solución de controversias (art. 5.1 LO 1/2025) y la negociación directa entre las partes o sus abogados vale como tal. Si lo que busca el abogado es acreditar el requisito con más garantías (documento firmado por ambas partes, oferta vinculante confidencial, mediador o conciliador), deriva a `masc-propuesta-acuerdo`. Para que el requerimiento sirva también de solicitud de negociación:

- Define el objeto de la controversia con la misma extensión que tendrá la demanda (identidad de objeto, art. 5.1) y **invita expresamente a negociar de buena fe** (art. 2), con un cauce concreto (reunión, videoconferencia, respuesta escrita) y un plazo.
- Envíalo al domicilio personal o lugar de trabajo del destinatario o por el medio electrónico usado en sus relaciones previas (art. 7.1), por un medio que acredite recepción, fecha y acceso al contenido íntegro (art. 10.2).
- Calcula y da al abogado: la interrupción de la prescripción o suspensión de la caducidad desde el intento de comunicación (art. 7.1); la terminación sin acuerdo a los treinta días naturales desde la recepción sin reunión ni respuesta escrita (art. 10.4.a), antes de la cual no conviene demandar; y el año para presentar la demanda (art. 7.3).
- Confidencialidad (art. 9): las propuestas concretas de acuerdo y las cifras de transacción no van en el requerimiento, que se aportará con la demanda; van en documento aparte con `masc-propuesta-acuerdo`.
- Materias excluidas: laboral, penal, concursal y conflictos con una entidad del sector público (art. 3.2); procesos exceptuados en el art. 5.2 y 5.3 (entre ellos, el juicio cambiario y la demanda ejecutiva). El monitorio **sí** lo exige: es un proceso especial del libro IV de la LEC, incluido en el art. 5.2.
- Busca cómo lo aplica la Audiencia de la plaza (consultas en la sección siguiente): hay Audiencias con acuerdos de unificación de criterios sobre qué comunicación basta.

### 4. Plazo y consecuencias

- **Plazo**: la ley no fija uno general. Usa el pactado; si no hay, fija uno proporcionado a la prestación (pagar dinero exige menos que ejecutar una obra) y exprésalo como fecha cierta o días naturales desde la recepción. Si el requerimiento sirve de intento de negociación, no uses menos de treinta días naturales antes de anunciar la demanda (art. 10.4.a LO 1/2025). Si el contrato no señala plazo pero de su naturaleza resulta que se concedió al deudor, recuerda que lo fijan los tribunales (art. 1128 CC).
- **Consecuencias**: anuncia solo las que el cliente está dispuesto a ejercer y que la ley o el contrato permiten: acciones de cumplimiento o de reclamación de cantidad, resolución (si la obligación es recíproca, art. 1124 CC), intereses, cláusula penal pactada, costas. No incluyas amenazas de denuncia penal, de difusión pública o de inclusión en ficheros sin base legal comprobada: además de ineficaces, exponen al cliente.
- **Consumidor destinatario**: antes de exigir intereses de demora o penalidades pactadas en condiciones generales, comprueba su posible abusividad (deriva a `condiciones-generales-consumidores` si hay duda); lo que se reclame en el requerimiento condiciona la demanda.

### 5. Envío

El medio lo decide el abogado; tú explicas qué exige cada efecto: acta notarial o requerimiento judicial para el art. 1504 CC, el art. 63.2 CCom y el art. 27.4 LAU; para lo demás, un medio fehaciente con certificación de contenido y acuse. No des precios, tarifas ni límites de páginas de ningún servicio. Si el destinatario no recoge la comunicación, busca la doctrina sobre comunicaciones frustradas por su conducta y deja constancia de cada intento.

## Contenido crítico y jurisprudencia

**Si defiendes al que requiere:**

- Identifica la obligación con cláusula y fecha, cuantifica al céntimo (principal, intereses y su cálculo, costes) y adjunta o describe los documentos: un requerimiento genérico no es «justificado» a efectos del art. 395 LEC.
- Declara que el cliente ha cumplido lo suyo o se allana a cumplir (art. 1100, último párrafo) y ofrece la contraprestación si es simultánea.
- Si hay fiador o varios deudores, un requerimiento a cada uno.
- No confundas la intimación del art. 1504 con un simple requerimiento de pago. Si la documentación no lo aclara, incluye en la única ronda de preguntas si el cliente quiere resolver o cobrar: si quiere resolver, el acta declara la resolución de forma inequívoca (o la condiciona a que no pague en un último plazo breve); si todavía quiere cobrar, basta un requerimiento de pago ordinario. Hasta que se notifique el acta, el cliente no debe aceptar pagos parciales ni conceder aplazamientos. La liquidación (restitución, cláusula penal, daños) se prepara con `resolucion-por-incumplimiento`.

**Si defiendes al requerido (contestación):**

- No reconozcas la deuda ni pidas aplazamientos que la reconozcan: cualquier acto de reconocimiento interrumpe la prescripción (art. 1973 CC). Si conviene negociar, hazlo con reserva expresa y sin admitir hechos.
- Alega, si procede, el incumplimiento previo del requirente (art. 1100, último párrafo) o la excepción de contrato no cumplido (busca la doctrina), la falta de vencimiento, la pluspetición o la prescripción ya consumada.
- Muestra disposición a acudir a un medio adecuado: rehusarlo sin causa pesa en costas (arts. 394.1 y 395.3 LEC).

**Consultas en Jurisprudenciator** (reformula como máximo dos veces si no hay resultados útiles; la jurisprudencia es imprescindible en esta skill según el apartado 8 del formato):

- Intimación del 1504: `consulta="requerimiento resolutorio artículo 1504 requerimiento notarial burofax pago posterior"` y `consulta="requerimiento artículo 1504 no es requerimiento de pago sino notificación de la voluntad de resolver"`, ambas con `base="TS"`, `jurisdiccion="CIVIL"`.
- Costes de cobro por factura: `consulta="morosidad operaciones comerciales importe mínimo de 40 euros por cada factura costes de cobro"`, `base="TJUE"` (o `buscar_por_cita` con `"C-585/20"`).
- Carácter recepticio y fecha de efectos: `consulta="reclamación extrajudicial interrupción de la prescripción carácter recepticio conocimiento del deudor"`, `base="TS"`.
- Comunicación no recogida: `consulta="requerimiento de pago no entregado dejado aviso eficacia conducta del destinatario"`, `base="TS"`, y la misma con `base="AN"`, `tipo_organo="AP"`.
- Mora y deuda ilíquida: `consulta="in illiquidis non fit mora canon de razonabilidad intereses moratorios"`, `base="TS"`.
- Mora mercantil: `consulta="artículo 63 Código de Comercio mora interpelación obligaciones mercantiles sin día señalado"`, `base="TS"`.
- Costas por allanamiento tras requerimiento: `consulta="allanamiento mala fe requerimiento fehaciente y justificado costas artículo 395"`, `base="AN"`, `tipo_organo="AP"`, `anios=3`.
- Requerimiento como MASC: `consulta="requerimiento de pago solicitud de negociación intento suficiente requisito de procedibilidad"`, `base="AN"`, `tipo_organo="AP"`, `fecha_desde="03/04/2025"` (añade `provincia`).

Lee con `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión) solo lo que vayas a citar en la nota; comprueba que el párrafo es razonamiento de la Sala y no alegación de parte ni transcripción de un precepto. El requerimiento no lleva jurisprudencia.

## Documentos que se entregan

En el requerimiento y en la nota, nombra las normas como pide el apartado 6 del formato («artículo 1100 del Código Civil», «artículo 63 del Código de Comercio», «artículo 5 de la Ley 3/2004, de 29 de diciembre», «artículo 22 de la Ley de Enjuiciamiento Civil», «artículo 5 de la Ley Orgánica 1/2025, de 2 de enero»): así las reconoce `verificar_escrito`.

**1. Requerimiento** (`requerimiento-<destinatario>-<AAAAMMDD>.docx`), maquetado según el apartado 5 del formato:

1. Remitente y destinatario con domicilio; lugar y fecha; medio de envío.
2. Asunto: «Requerimiento de [pago / cumplimiento] del contrato de [tipo] de fecha [FECHA]».
3. Hechos numerados: contrato, obligación incumplida (cláusula), cumplimiento propio, incumplimiento con fechas e importes, reclamaciones previas.
4. Requerimiento concreto: qué, cuánto (desglose) y en qué plazo, forma de pago o de cumplimiento (cuenta `[IBAN]`, lugar de entrega).
5. Mención expresa de los efectos: constitución en mora (art. 1100 CC o art. 63 CCom), interrupción de la prescripción (art. 1973 CC), intimación del art. 1504 CC si procede.
6. Invitación a negociar, si sirve de intento del MASC (apartado 3): objeto, cauce y plazo, sin cifras de transacción.
7. Consecuencias del incumplimiento (apartado 4).
8. Firma del cliente o del abogado con su representación.

Si el efecto exige acta notarial o requerimiento judicial (art. 1504 CC, art. 63.2 CCom, art. 27.4 LAU), el documento es el texto que se incorporará al acta, con el mismo nombre de archivo: requirente y requerido, medio («acta notarial de requerimiento»), hechos, declaración o requerimiento y firma del requirente.

Para el requerido: **contestación** (`contestacion-requerimiento-<remitente>-<AAAAMMDD>.docx`) con la misma estructura de hechos, las defensas y la reserva de acciones.

**Reparto para la redacción rápida:** el requerimiento, el texto para el acta notarial y la contestación (1-2 páginas) no necesitan equipo: los redactas tú en un único archivo, con las consultas en paralelo. La nota (2-4 páginas), en equipo (apartado 11 del formato): efectos buscados y prescripción / intento de negociación y fechas / jurisprudencia y riesgos.

**2. Nota para el abogado** (`nota-requerimiento-<destinatario>-<AAAAMMDD>.docx`, 2-4 páginas, apartado 3 del formato): efectos buscados y precepto de cada uno; forma de envío recomendada y por qué; cálculo de prescripción con fechas; fechas del MASC (recepción prevista, treinta días, un año); jurisprudencia con párrafo literal, órgano, fecha y ECLI; datos pendientes; riesgos; próximo paso (demanda, monitorio, resolución o propuesta de acuerdo).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió; ninguna consulta imprescindible quedó sin resultado, y lo que Jurisprudenciator no tenía se obtuvo de una fuente oficial en internet, con enlace y fecha de consulta, y se señala en el resumen.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos que se citan (CC 1100, 1101, 1108, 1973 y los de prescripción aplicables; CCom 63 o Ley 3/2004 si es mercantil; CC 1504, LEC 22 o LAU 27 si se usan; LEC 394 y 395; LO 1/2025 arts. 2, 5, 7, 9 y 10 si sirve de MASC), con su línea de vigencia.
- [ ] El efecto buscado casa con la forma de envío (acta notarial o requerimiento judicial donde la ley lo exige).
- [ ] Prescripción calculada por crédito, con fecha inicial, precepto y fecha final; fiadores y codeudores requeridos por separado si procede.
- [ ] Si sirve de intento de negociación: objeto idéntico al de la futura demanda, invitación expresa, sin propuestas confidenciales, y fechas de treinta días y un año en la nota.
- [ ] Cada ECLI citado en la nota se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); cada aviso de «posible disonancia» contrastado con el texto leído.
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[CIF]`, `[DOMICILIO]`, `[IMPORTE]`, `[IBAN]`) en lugar de datos inventados; importes, fechas y definiciones coherentes entre documentos.
- [ ] Sin precios de burofax o notaría; cualquier tipo de interés, con su fuente (Jurisprudenciator o el BOE en internet, con enlace y fecha de consulta).
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, efectos y cómo se aseguran, datos que faltan, tabla de jurisprudencia, plazos con su precepto y próximo paso.
