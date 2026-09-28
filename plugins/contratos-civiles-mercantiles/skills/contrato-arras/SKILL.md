---
name: contrato-arras
description: >-
  Redacta el contrato de arras o señal previo a la compraventa de un inmueble (arras penitenciales del
  artículo 1454 del Código Civil, confirmatorias o penales) y su nota para el abogado, en Word. Úsala
  cuando el abogado diga «contrato de arras», «señal», «reserva del piso», «arras penitenciales»,
  «contrato privado antes de la escritura» o «devolver las arras dobladas». Califica las arras con la
  doctrina de la Sala Primera, fija plazo para escriturar, cargas, condición de financiación, gastos,
  llaves y desistimiento según defienda al comprador o al vendedor, con Catastro y nota simple. Si se
  firma ya la compraventa o la minuta de escritura, usa compraventa-inmueble; si la otra parte ya no
  quiere escriturar, requerimiento-cumplimiento o resolucion-por-incumplimiento.
---

# Contrato de arras o señal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Arras, cláusula penal, resolución y mora** → `buscar_articulo` (`ley="CC"`, artículos `"1454"`, `"1152"`, `"1153"`, `"1154"`, `"1124"`, `"1100"`, `"1101"` y `"1504"`).
- **Condición de financiación, validez y consignación** → `buscar_articulo` (`ley="CC"`, artículos `"1113"`, `"1114"`, `"1115"`, `"1119"`, `"1255"`, `"1256"` y `"1176"`).
- **Compraventa, entrega, llaves, gastos, forma y vivienda familiar** → `buscar_articulo` (`ley="CC"`, artículos `"1445"`, `"1450"`, `"1455"`, `"1462"`, `"1466"`, `"1473"`, `"1279"`, `"1280"`, `"1320"` y `"1377"`); pagos en efectivo (`ley="BOE-A-2012-13416"`, `articulo="7"`).
- **Información previa, comunidad, arrendatario, Registro y certificado energético** → `buscar_articulo` (`ley="Ley 12/2023"`, `articulo="31"`), (`ley="Ley 49/1960"`, `articulo="9"`), (`ley="LAU"`, artículos `"14"` y `"25"` si hay arrendatario de vivienda; `"29"` y `"31"` si es local), (`ley="BOE-A-1946-2453"`, `articulo="34"`) y (`ley="BOE-A-2021-9176"`, artículos `"13"` y `"17"`).
- **Consumidores (vendedor promotor o empresario)** → `buscar_articulo` (`ley="TRLGDCU"`, artículos `"3"`, `"4"`, `"82"`, `"83"`, `"87"` y `"89"`). Los arts. 3 y 4 bastan para decidir si hay relación de consumo: entre particulares no la hay.
- **Plusvalía y tributos pactados** → `buscar_articulo` (`ley="BOE-A-2004-4214"`, `articulo="106"`, sujeto pasivo) y (`ley="LGT"`, `articulo="17"`).
- **Doctrina sobre calificación de las arras, desistimiento, moderación y abusividad** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; `base="AN"` + `tipo_organo="AP"` si no hay doctrina del Supremo o el asunto se litigará en esa plaza) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil`; **inmueble** → `consultar_catastro` (referencia catastral, o dirección y municipio) y `buscar_articulo` (`ley="Real Decreto Legislativo 1/2004"`, artículos `"38"` y `"40"`); **tributación de las arras** → `buscar_consultas_hacienda` (`consulta="arras penitenciales"`) + `leer_consulta_hacienda`.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Formas que reconoce `verificar_escrito`: «artículo 1454 del Código Civil», «artículo 31 de la Ley 12/2023, de 24 de mayo, por el derecho a la vivienda», «artículo 9 de la Ley 49/1960, de 21 de julio, sobre propiedad horizontal», «artículo 7 de la Ley 7/2012, de 29 de octubre», «artículo 17 del Real Decreto 390/2021, de 1 de junio», «artículo 38 del Real Decreto Legislativo 1/2004, de 5 de marzo» y «artículo 25 de la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos».

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Compraventa de un inmueble (vivienda, local, garaje, trastero, solar o finca rústica) en la que el comprador entrega una cantidad antes de la escritura y hay que decidir qué ocurre si una de las partes no sigue adelante.
- Revisión de un borrador de arras propio, o del modelo de la inmobiliaria que el cliente todavía no ha firmado y que el abogado quiere rehacer.

Pasa este detector antes de redactar. Si encaja otra skill, díselo al abogado y deriva:

| Situación | Skill que procede |
|---|---|
| Se firma ya la compraventa (precio pagado o aplazado, entrega) o se prepara la minuta para el notario | `compraventa-inmueble` |
| Vivienda sobre plano o en construcción con entregas a cuenta al promotor | `compraventa-inmueble` (garantía de las cantidades anticipadas) y, para las condiciones generales, `condiciones-generales-consumidores` |
| Hay que comprobar a fondo quién firma: poderes, sociedad en concurso, menores o personas con apoyos | `verificacion-partes-contrato` antes de esta skill |
| El borrador es de la otra parte y hay que contestarlo | `revision-contrato-semaforo` o `negociacion-contrapropuesta` |
| Plazo vencido, la otra parte no comparece o se niega a escriturar | `requerimiento-cumplimiento` o `resolucion-por-incumplimiento` |
| Señal en una venta de mercaderías entre empresas | `compraventa-mercantil` |
| Se quiere un derecho a decidir si se compra, con prima por ese derecho | No son arras: es una opción de compra. Díselo al abogado; esta skill no la redacta |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende el abogado (comprador o vendedor) y si alguna parte actúa como empresario o profesional: con vendedor empresario y comprador consumidor (art. 3 TRLGDCU) cambian las cláusulas admisibles.
2. ★ Qué quiere el cliente de las arras: poder apartarse pagando un precio cierto (penitenciales), asegurar el cumplimiento y poder exigirlo (confirmatorias) o fijar de antemano la indemnización por incumplir (penales). Si el cliente no lo sabe, explica las tres con sus consecuencias y deja que el abogado elija.
3. ★ Partes: nombre, DNI/NIE y domicilio; si es persona casada, régimen económico y si el inmueble es su vivienda habitual (arts. 1320 y 1377 CC: puede hacer falta el consentimiento del cónyuge). Si es sociedad, denominación y CIF para `buscar_empresa_mercantil`.
4. ★ Inmueble: dirección o referencia catastral y **nota simple** reciente del Registro de la Propiedad (titular, cargas, arrendamientos inscritos, prohibiciones de disponer, afecciones). El conector no consulta el Registro: si el abogado aún no la tiene, prepara el borrador con `[DATOS REGISTRALES]` y di en la nota y en el resumen que no debe firmarse sin contrastarla.
5. ★ Precio total, importe de las arras, cuenta de destino y forma de pago del resto; si hay financiación, importe, plazo para obtenerla y cuántas entidades se consultarán.
6. ★ Fecha límite para otorgar la escritura y quién elige notario; fecha prevista de entrega de la posesión.
7. ★ Ocupación: libre, arrendada (tipo de arrendamiento, fecha y si hubo renuncia al derecho de adquisición preferente) u ocupada sin título.
8. Cargas que hay que cancelar y cómo (hipoteca con saldo pendiente, embargos), deudas con la comunidad, derramas acordadas y quién las paga.
9. Intermediario: agencia, honorarios, quién paga y si retiene las arras como depositaria.
10. Si el inmueble o las partes se rigen por un Derecho civil propio (Cataluña, Navarra, Aragón, País Vasco, Galicia, Baleares).
11. Documentos disponibles: certificado de eficiencia energética registrado y etiqueta, cédula o certificado de habitabilidad si la comunidad autónoma lo exige, último recibo del IBI, certificado de deudas con la comunidad, inspección técnica del edificio.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota la línea «vigente desde».

**Las tres clases de arras.**

- **Penitenciales** (art. 1454 CC): permiten a cada parte desistir sin causa; el comprador pierde lo entregado y el vendedor lo devuelve duplicado. No admiten más indemnización ni moderación judicial. La jurisprudencia de la Sala Primera las considera excepcionales y exige interpretación restrictiva: sin voluntad inequívoca de pactar el desistimiento, las arras se tienen por confirmatorias. Por eso el contrato debe decir «arras penitenciales», citar el artículo 1454 del Código Civil y describir la facultad de desistir y su precio.
- **Confirmatorias**: son parte del precio y prueba de que el contrato está perfeccionado (art. 1450 CC). Ante el incumplimiento, la parte cumplidora elige entre exigir el cumplimiento o resolver con indemnización de daños (arts. 1124 y 1101 CC), que tendrá que probar. El contrato debe excluir de forma expresa el desistimiento.
- **Penales**: cláusula penal (arts. 1152 y 1153 CC). La pena sustituye a la indemnización salvo pacto; el deudor no se libera pagándola salvo que se le haya reservado ese derecho. El juez solo la modera si hubo cumplimiento parcial o irregular (art. 1154 CC); la Sala Primera no modera la pena pactada precisamente para el incumplimiento que se produjo.

**Comprobaciones de validez y de riesgo.**

- **Libertad de pactos y su límite** (arts. 1255 y 1256 CC): el cumplimiento no puede quedar al arbitrio de una parte. Una condición de financiación que dependa solo de la voluntad del comprador («si le conviene») es nula (art. 1115 CC); si depende de la decisión de un banco, es válida, y se tiene por cumplida si el comprador impide su cumplimiento (art. 1119 CC). Redáctala con hechos comprobables: importe, número mínimo de entidades, plazo y acreditación escrita de la denegación.
- **Duración de la facultad de desistir**: sin plazo pactado, la jurisprudencia la extiende hasta la consumación del contrato. Fija siempre una fecha límite y di qué pasa al vencer (las arras se imputan al precio y pierden el carácter penitencial, o el contrato queda resuelto).
- **Desistimiento frente a incumplimiento**: son acciones distintas. Sin pacto, que el vendedor no comparezca a la firma o venda a otro es un incumplimiento (arts. 1124 y 1101 CC: el comprador tendría que probar sus daños), no un desistimiento. Si defiendes al comprador, pacta expresamente que esas conductas equivalen al desistimiento y dan derecho a las arras duplicadas (art. 1255 CC), con opción de exigir el cumplimiento. Busca doctrina que respalde la equiparación (búsqueda 3 del apartado siguiente) y cítala solo si la encuentras y la lees; si no aparece, di en la nota que la cláusula descansa en el pacto y no atribuyas esa doctrina a la Sala Primera; si defiendes al vendedor, regula cómo se ejerce el desistimiento y cómo se devuelve el doble (transferencia en un plazo fijo y, si el comprador no la acepta, consignación conforme al art. 1176 CC).
- **Consumidores**: si vende un empresario a un consumidor, comprueba los arts. 82, 87 y 89 TRLGDCU. Es abusiva la retención de lo pagado por el consumidor si no se prevé una indemnización equivalente cuando renuncia el empresario (art. 87, apartado 2) y la imposición al consumidor de gastos o tributos que corresponden al empresario (art. 89, apartado 3). La cláusula abusiva es nula y se tiene por no puesta (art. 83): no se modera, se pierde entera. Unas arras penitenciales asimétricas (el consumidor pierde si no firma; el promotor se aparta con solo no convocar) pueden ser abusivas: haz la búsqueda de abusividad del apartado siguiente.
- **Vivienda familiar**: si el inmueble es la vivienda habitual de la familia, el vendedor necesita el consentimiento del cónyuge aunque sea privativa (art. 1320 CC); si es ganancial, el de ambos (art. 1377 CC). Haz que firmen los dos o deja constancia en EXPONEN.
- **Doble venta** (art. 1473 CC): el comprador que no inscribe primero puede perder frente a otro comprador de buena fe que inscriba (art. 34 de la Ley Hipotecaria). Si defiendes al comprador, prohíbe al vendedor gravar, arrendar o comprometer el inmueble durante la vigencia de las arras y pide nota simple actualizada antes de la escritura.
- **Arrendatario**: si la vivienda está arrendada, el arrendatario tiene tanteo durante 30 días naturales desde la notificación fehaciente de la decisión de vender, el precio y las condiciones, y retracto si no se le notifica (art. 25 LAU); para inscribir la venta hay que justificar las notificaciones (art. 25.5 LAU). El comprador se subroga en el arrendamiento en los términos del art. 14 LAU. Si el arrendatario renunció a la adquisición preferente, el vendedor debe comunicarle su intención de vender con 30 días de antelación a la formalización (art. 25.8 LAU). Unas arras confirmatorias o penales ya perfeccionan la compraventa (art. 1450 CC), de modo que podría sostenerse que la «formalización» es su firma: recomienda enviar la comunicación antes de firmar las arras, declara en el contrato que la fecha de formalización es la de la escritura y no fijes la escritura antes de que pasen treinta días desde la recepción. Condiciona las arras a que el arrendatario no ejerza el tanteo y regula la devolución (simple, no duplicada) si lo ejerce. Si es un local, aplica los arts. 29 y 31 LAU.
- **Información previa** (art. 31 de la Ley 12/2023): el comprador puede pedir, antes de entregar cualquier cantidad, identificación registral y cargas, cuota, superficie útil y construida, certificado de eficiencia energética, estado de ocupación, régimen de protección, entre otros datos. Si defiendes al comprador, exígela como anexo; si defiendes al vendedor, entrégala y haz constar la recepción.
- **Comunidad de propietarios** (art. 9.1.e LPH): el inmueble responde de las deudas de la anualidad en curso y de los tres años anteriores; en la escritura el vendedor debe aportar la certificación de deudas. Pacta que la aporte y que las deudas y derramas acordadas antes de la firma sean suyas, con retención del precio si no se acredita el pago.
- **Pagos en efectivo** (art. 7 de la Ley 7/2012): si alguna parte actúa como empresario o profesional, no puede pagarse en efectivo una operación de importe igual o superior al umbral que devuelva la consulta. Pacta transferencia o cheque bancario y conserva los justificantes.
- **Llaves y posesión** (art. 1462 CC): la escritura equivale a la entrega salvo que resulte lo contrario. Evita entregar llaves antes de la escritura; si se entregan, regula el título (precario con fecha de desalojo si no se escritura) y el reparto de riesgos y suministros.
- **Gastos** (art. 1455 CC): salvo pacto, el otorgamiento de la escritura es del vendedor y la primera copia y lo posterior, del comprador. Con consumidor, respeta el art. 89 TRLGDCU.
- **Catastro**: la referencia catastral debe constar en los documentos de negocios con trascendencia real y las partes la consignan (arts. 38 y 40 del Real Decreto Legislativo 1/2004). Consulta el inmueble con `consultar_catastro` y compara uso y superficie con la nota simple y lo que se anuncia; toda discrepancia va a la nota. En País Vasco y Navarra el conector no cubre el catastro foral: búscalo en internet en la sede electrónica del catastro foral (o toma la referencia de la certificación foral que aporte el abogado), cítalo con enlace y fecha de consulta y dilo en la nota.
- **Derecho civil propio**: si aplica, busca la norma con `buscar_boe` (en Cataluña, `consulta="libro sexto del Código civil de Cataluña"`). `buscar_articulo` no devuelve los artículos con guion del Código civil catalán: léelos en internet en el texto consolidado oficial (BOE o diario oficial de la comunidad) y cítalos con enlace y fecha de consulta.
- **Tributación**: no des tipos ni importes. Avisa de que las arras perdidas o cobradas duplicadas tienen tratamiento en el IRPF: búscalo con `buscar_consultas_hacienda` (`consulta="arras penitenciales"`) y cita la consulta leída; si la herramienta no responde, busca la consulta en internet en la base oficial de la Dirección General de Tributos y cítala con enlace y fecha. La compraventa tributará por ITP o por IVA según el vendedor y el inmueble: remite a `compraventa-inmueble`. Un pacto sobre quién paga un tributo no altera al sujeto pasivo frente a la Administración (art. 17.5 LGT: léelo con `ley="LGT"`).

## Cláusulas clave y jurisprudencia

Haz estas búsquedas con `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`, salvo que se indique otra cosa), lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y comprueba que el párrafo es razonamiento de la Sala. La calificación de las arras, su moderación y la abusividad son jurisprudencia imprescindible (apartado 8 del formato): si tras dos reformulaciones no hay resolución aplicable, sigue el punto 3 de la puerta.

1. **Calificación de las arras.** `consulta="arras penitenciales interpretación restrictiva voluntad inequívoca artículo 1454"`, `terminos="arras penitenciales interpretación restrictiva"`. En la nota, el párrafo que exige pacto claro justifica el título del contrato, la cita del artículo 1454 y la exclusión expresa de las otras modalidades.
   - Comprador que quiere salida barata: penitenciales con importe moderado y plazo de desistimiento hasta la víspera de la escritura.
   - Comprador que quiere asegurar la compra: confirmatorias, con acción de cumplimiento y pena para el vendedor que no escritura.
   - Vendedor que quiere retirar el inmueble del mercado con seguridad: confirmatorias o penales con pena suficiente y plazo corto para escriturar; si acepta penitenciales, que el importe compense el tiempo de inmovilización.
2. **Plazo del desistimiento y de la escritura.** `consulta="arras penitenciales vigencia hasta la consumación facultad de desistir"`. Redacta: fecha límite, convocatoria a la notaría por medio fehaciente con antelación mínima, y consecuencia del vencimiento sin escritura.
3. **Vendedor que no comparece o vende a otro.** `consulta="arras penitenciales devolución duplicada vendedor incumple sin desistir"` y, como reformulación, `consulta="arras penitenciales vendedor no comparece notaría otorgamiento escritura"` (`base="AN"`, `tipo_organo="AP"`). Es jurisprudencia que se cita si existe (apartado 8 del formato): si no aparece, la cláusula se apoya en el pacto. Pro comprador: la incomparecencia o la venta a tercero equivalen a desistimiento y dan derecho al doble, sin perjuicio de optar por el cumplimiento. Pro vendedor: el desistimiento se comunica por escrito y se paga en el plazo pactado; cumplido eso, no hay más responsabilidad.
4. **Moderación de la pena.** `consulta="arras penales moderación cláusula penal incumplimiento previsto"`. Describe en la cláusula penal el incumplimiento exacto que la activa (no escriturar en plazo, no pagar el resto): así la pena no se modera. Si defiendes a quien la sufriría, limita su importe y pacta que sustituye a la indemnización. Con arras confirmatorias o penales, la resolución por falta de pago del resto del precio exige requerimiento judicial o notarial: hasta entonces el comprador puede pagar aunque haya vencido el plazo (art. 1504 CC). Prevé ese requerimiento en la estipulación QUINTA.
5. **Condición de financiación.** `consulta="arras condición suspensiva concesión préstamo hipotecario devolución"`, `base="AN"`, `tipo_organo="AP"`, `anios=5`. Redacta como condición suspensiva objetiva: importe y plazo del préstamo, número de entidades, fecha límite, denegación por escrito y devolución simple de las arras si no se obtiene pese a la diligencia del comprador. Pro vendedor: prueba documental de las solicitudes, plazo corto y renuncia expresa si el comprador no aporta la denegación en fecha.
6. **Consumidor y vendedor empresario.** `consulta="arras consumidor promotor cláusula abusiva falta de reciprocidad"` y `consulta="cláusula penal abusiva consumidor nulidad no moderación"`. Si defiendes al empresario, redacta arras recíprocas (quien desiste pierde o devuelve el doble) y penas proporcionadas; si defiendes al consumidor, identifica en la nota cada cláusula expuesta a nulidad.
7. **Cargas y cancelación.** Cláusula de venta libre de cargas: cancelación en el acto de la escritura con retención del precio necesario (cheque bancario a favor del acreedor) y compromiso del vendedor de obtener el certificado de saldo. Pro comprador: si aparece una carga no declarada, el comprador puede resolver con devolución duplicada o retener su importe.
8. **Depósito de las arras.** Si las recibe la inmobiliaria, pacta que las tiene como depositaria y a disposición de quien resulte con derecho, no como pago al vendedor ni a cuenta de sus honorarios.

## Documentos que se entregan

Dos documentos en Word, según `references/formato-y-entrega-contratos.md`:

1. `contrato-arras-<apellido-o-denominación-del-cliente>-<AAAAMMDD>.docx`
2. `nota-arras-<apellido-o-denominación-del-cliente>-<AAAAMMDD>.docx`

**Estructura del contrato** (una definición por término: «el Inmueble», «las Arras», «la Escritura»):

- Título que ya califica: «CONTRATO DE COMPRAVENTA CON ARRAS PENITENCIALES», «CONTRATO DE ARRAS CONFIRMATORIAS» o «CONTRATO DE ARRAS PENALES». Lugar y fecha.
- **REUNIDOS** e **INTERVIENEN** (con el consentimiento del cónyuge si procede y el poder o cargo de quien firma por una sociedad).
- **EXPONEN**: I. Titularidad, descripción, datos registrales `[DATOS REGISTRALES]` y referencia catastral `[REFERENCIA CATASTRAL]`. II. Cargas según nota simple de `[FECHA]`. III. Situación de ocupación y, si hay arrendatario, estado del derecho de adquisición preferente. IV. Situación con la comunidad. V. Información entregada al comprador (art. 31 de la Ley 12/2023). VI. Voluntad de comprar y vender.
- **ESTIPULACIONES**:
  - PRIMERA.- Objeto: compromiso de compraventa del Inmueble como cuerpo cierto, libre de cargas, ocupantes y deudas.
  - SEGUNDA.- Precio y forma de pago: total, Arras, resto en la Escritura; medios de pago distintos del efectivo; retención para cancelar cargas.
  - TERCERA.- Naturaleza de las Arras: la modalidad elegida, con la cita del artículo 1454 del Código Civil si son penitenciales, y exclusión expresa de las otras.
  - CUARTA.- Plazo y otorgamiento de la Escritura: fecha límite, notario, convocatoria fehaciente, documentos que aporta cada parte.
  - QUINTA.- Desistimiento o incumplimiento: cómo se ejerce, plazo, devolución o pérdida, equiparaciones pactadas y, si son confirmatorias, remisión al artículo 1124 del Código Civil.
  - SEXTA.- Condición de financiación (si la hay).
  - SÉPTIMA.- Declaraciones del vendedor: cargas, arrendamientos, situación urbanística, ausencia de expedientes, de litigios y de deudas.
  - OCTAVA.- Entrega de la posesión y de las llaves; estado del Inmueble; suministros.
  - NOVENA.- Gastos y tributos: notaría, Registro, cancelación de cargas, IBI del año, derramas, cuotas de comunidad; plusvalía según quién sea el sujeto pasivo y, con consumidor, sin trasladarle lo que corresponda al empresario.
  - DÉCIMA.- Documentación que entrega el vendedor antes de la Escritura: certificado de eficiencia energética registrado y etiqueta, certificado de deudas con la comunidad, último recibo del IBI, cédula de habitabilidad si procede.
  - UNDÉCIMA.- Intermediación y depósito de las Arras (si interviene agencia; si no, suprímela y renumera las siguientes).
  - DUODÉCIMA.- Notificaciones (domicilios y correos electrónicos), protección de datos, ley aplicable y fuero.
- Cierre, firmas en dos columnas y **ANEXOS**: nota simple, resultado de la consulta al Catastro, información del artículo 31 de la Ley 12/2023, certificado energético y etiqueta.

**Nota para el abogado** (2-5 páginas): modalidad elegida y por qué, con el párrafo literal de la Sala Primera sobre la interpretación restrictiva (órgano, fecha, ECLI); cláusulas críticas con su artículo; comparación entre Catastro, nota simple y lo anunciado; pendientes (nota simple, notificación al arrendatario, certificado de deudas, consentimiento del cónyuge); riesgos y alternativas; tributación y formalidades que hay que comprobar, sin importes no leídos en una norma.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos de la lista (CC, Ley 12/2023, LPH, LAU si hay arrendatario, Ley Hipotecaria, Ley 7/2012, Real Decreto 390/2021, Real Decreto Legislativo 1/2004, texto refundido de Haciendas Locales si se pacta la plusvalía, y TRLGDCU si una parte es empresario y la otra consumidor), con su fecha de vigencia.
- [ ] La modalidad de arras figura en el título, en la estipulación TERCERA y en QUINTA sin contradicciones; si son penitenciales, se cita el artículo 1454 del Código Civil; si no lo son, se excluye el desistimiento.
- [ ] Fecha límite de desistimiento y de escritura fijadas; plazo de tanteo del arrendatario calculado desde la notificación, si procede.
- [ ] Inmueble consultado con `consultar_catastro` (o catastro foral consultado en internet con enlace) y contrastado con la nota simple; `[DATOS REGISTRALES]` pendiente señalado si no hay nota simple.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`; ninguno en el contrato.
- [ ] `verificar_escrito` pasado sobre el contrato y sobre la nota; cada aviso de «posible disonancia» contrastado con el artículo leído.
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[IMPORTE]`, `[IBAN]`, `[FECHA]`) en lugar de datos inventados; importes, fechas y definiciones coherentes en todo el documento.
- [ ] Si vende un empresario a un consumidor: arras recíprocas y ningún gasto o tributo del art. 89 TRLGDCU trasladado.
- [ ] Plusvalía y demás tributos pactados de acuerdo con el sujeto pasivo leído (art. 106 del texto refundido de Haciendas Locales), sin tipos ni importes.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, modalidad y cláusulas críticas, datos y documentos pendientes, tabla de jurisprudencia y plazos con su precepto.
