---
name: pacto-de-socios
description: >-
  Redacta o adapta un pacto de socios (pacto parasocial) de una sociedad limitada o anónima española, con las
  cláusulas que hay que llevar a estatutos y la nota para el abogado: gobierno y materias reforzadas, consejo y
  vetos, transmisión (lock-up, adquisición preferente, arrastre, acompañamiento), bloqueo y salida, valoración,
  no competencia y dedicación de socios trabajadores, cláusula penal, duración, confidencialidad, ley y
  arbitraje. Úsala cuando el abogado diga «pacto de socios», «pacto parasocial», «acuerdo de accionistas»,
  «drag along», «tag along», «entra un inversor», «socios trabajadores» o «los socios se bloquean». Si se firma
  la compra de participaciones o acciones, usa compraventa-participaciones; para revisar el pacto de la otra
  parte, revision-contrato-semaforo o negociacion-contrapropuesta; si solo es confidencialidad,
  confidencialidad-nda.
---

# Pacto de socios

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Validez del pacto y su eficacia frente a la sociedad** → `buscar_articulo` (`ley="LSC"`, artículos `"28"` y `"29"`) y (`ley="CC"`, artículos `"7"`, `"1091"`, `"1255"`, `"1256"` y `"1257"`).
- **Transmisión y su traslado a estatutos** → `buscar_articulo` (`ley="LSC"`, artículos `"104"`, `"106"`, `"107"`, `"108"`, `"109"`, `"110"`, `"111"`, `"112"` y `"346"` para la SL; `"123"`, `"124"` y `"125"` para la SA) y el Reglamento del Registro Mercantil (`ley="BOE-A-1996-17533"`, artículos `"188"` y `"175"` para la SL; `"123"` y `"114"` para la SA).
- **Gobierno, mayorías, consejo y vetos** → `buscar_articulo` (`ley="LSC"`, artículos `"160"`, `"161"`, `"188"`, `"190"`, `"198"`, `"199"`, `"200"`, `"201"`, `"204"`, `"205"`, `"223"`, `"234"`, `"242"` y `"243"`); si defiendes a un minoritario, además `"196"` (información en la SL) y `"265"` (auditor a petición del 5 %).
- **Salida, exclusión, valoración, dividendos y socios trabajadores** → `buscar_articulo` (`ley="LSC"`, artículos `"86"` a `"89"`, `"140"`, `"220"`, `"229"`, `"230"`, `"346"`, `"347"`, `"348 bis"`, `"350"`, `"351"`, `"353"`, `"356"` y `"363"`) y, si el socio es trabajador por cuenta ajena, (`ley="ET"`, `articulo="21"`).
- **Cláusula penal, duración y denuncia** → `buscar_articulo` (`ley="CC"`, artículos `"1152"`, `"1153"`, `"1154"`, `"1700"`, `"1705"`, `"1706"` y `"1707"`) y (`ley="CCom"`, `articulo="224"`); **arbitraje** → (`ley="Ley 60/2003"`, artículos `"2"`, `"9"`, `"11 bis"` y `"11 ter"`); **vetos que dan control conjunto** → (`ley="Ley 15/2007"`, artículos `"1"`, `"7"`, `"8"` y `"9"`).
- **Doctrina sobre pactos omnilaterales, duración indefinida, no competencia, valoración y cláusula penal** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; para Audiencias, `base="AN"` y `tipo_organo="AP"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **La sociedad y los socios que son sociedades** → `buscar_empresa_mercantil` (denominación o CIF): tipo social, estado, órgano de administración, cargos vigentes y actos inscritos (disolución, concurso, depósito de pactos parasociales).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...).

Cita el Reglamento del Registro Mercantil como «artículo 188 del Real Decreto 1784/1996, de 19 de julio, por el que se aprueba el Reglamento del Registro Mercantil»: con «Reglamento del Registro Mercantil» a secas, `verificar_escrito` atribuye el artículo a la Ley de Sociedades de Capital (comprobado).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Constitución de una SL o SA con varios socios que quieren reglas propias de gobierno, permanencia y salida.
- Entrada de un inversor mediante ampliación de capital o compra: el pacto regula la relación posterior; el acuerdo de inversión o la compraventa van aparte (o como anexo) y se redactan con la skill que corresponda.
- Socios trabajadores y socios capitalistas; empresa familiar que quiere ordenar la sucesión (si hay protocolo familiar, pregunta si se va a publicar conforme al Real Decreto 171/2007 y léelo con `buscar_boe`, identificador `BOE-A-2007-5587`).
- Adaptar un pacto antiguo (duración indefinida, reglas que ya no casan con los estatutos, socios nuevos que deben adherirse).

| Situación | Skill |
|---|---|
| Se compran o venden participaciones o acciones | `compraventa-participaciones` (el pacto puede ir como anexo) |
| Informe de riesgos sobre el pacto que envía la otra parte | `revision-contrato-semaforo` |
| Contrapropuesta al borrador del otro lado | `negociacion-contrapropuesta` |
| Adenda, adhesión de un socio nuevo o prórroga del pacto | `modificacion-novacion-cesion` |
| Qué significa una cláusula de un pacto ya firmado | `dictamen-interpretacion-contrato` |
| Un socio incumple: requerirle o resolver y reclamar la pena | `requerimiento-cumplimiento`, `resolucion-por-incumplimiento` |
| Préstamo de un socio a la sociedad | `prestamo-reconocimiento-deuda` |
| Quién firma por una sociedad socia, poderes, concurso | `verificacion-partes-contrato` |
| Impugnar acuerdos, excluir judicialmente, pedir la disolución | Litigación societaria, fuera de este plugin: díselo al abogado |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ **A quién defiende el abogado**: socio mayoritario o fundador gestor, minoritario o inversor financiero, socio trabajador, o encargo común de todos los socios (redacción equilibrada). Cambia cada cláusula de la sección siguiente.
2. ★ **Sociedad**: denominación, CIF, tipo (SL o SA), si está constituida o en constitución. Compruébala con `buscar_empresa_mercantil` y pide los **estatutos vigentes**: sin ellos no se puede detectar contradicción entre pacto y estatutos.
3. ★ **Socios**: identidad, porcentaje, clases de participaciones o acciones, si firman **todos** (pacto omnilateral) o solo algunos; los socios que son sociedades, con quién firma por ellas. Si un socio está casado, pregunta el régimen económico y si las participaciones son gananciales: si lo son, el arrastre y las opciones de compra son actos de disposición y conviene que el cónyuge consienta en el propio pacto (art. 1377 CC). Si algún socio tiene vecindad civil foral, pide el régimen y búscalo con `buscar_boe`; si no aparece, léelo en internet en el texto consolidado oficial (punto 3 de la puerta).
4. ★ **Operación y horizonte**: constitución, ronda, reorganización familiar; plazo previsto de salida del inversor.
5. ★ **Gobierno**: órgano de administración, quién nombra consejeros, materias que deben requerir mayoría reforzada o el voto de un socio concreto, derechos de información.
6. ★ **Transmisión**: plazo de permanencia, adquisición preferente (quién, plazo, precio), arrastre (umbral, precio mínimo), acompañamiento (total o proporcional), cambio de control de un socio sociedad, transmisiones libres (grupo, familia).
7. ★ **Socios trabajadores**: funciones, dedicación, retribución y si su relación es laboral o mercantil; si son administradores; qué pasa si dejan de trabajar (causa, momento, precio).
8. **Bloqueo y salida**: mecanismo preferido (escalado, mediación, opciones de compra y venta, oferta cruzada, venta conjunta), método de valoración y experto.
9. **Financiación y dividendos**: compromisos de aportación, préstamos de socios, garantías personales, política de reparto.
10. **Cláusula penal** (importe o fórmula), duración, confidencialidad, notificaciones, ley aplicable, tribunales o arbitraje (institución).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota la línea de vigencia. Distingue siempre dos planos: el **pacto** es un contrato entre quienes lo firman (arts. 1091, 1255 y 1257 CC); los **estatutos** vinculan a la sociedad y a los socios futuros, pero están sujetos a la LSC y a los principios configuradores del tipo (art. 28 LSC). Los pactos reservados no son oponibles a la sociedad (art. 29 LSC).

**1. Eficacia del pacto y doctrina de la Sala Primera.** Busca antes de redactar: `buscar_sentencias` (`consulta="pacto parasocial omnilateral impugnación acuerdo social buena fe"`, `base="TS"`, `jurisdiccion="CIVIL"`) y (`consulta="pactos parasociales validez límites artículo 1255 inoponibilidad sociedad"`). Lee con `leer_sentencias` las dos más recientes y comprueba lo que sostienen hoy, y que el párrafo que vas a citar es de la Sala y no de la sentencia recurrida que reproduce (con esos términos, el conector puede devolver párrafos de la Audiencia transcritos por el Supremo; si pasa, afina `terminos` o busca la sentencia de pleno de la Sala sobre el pacto omnilateral y la buena fe con `consulta="pacto omnilateral buena fe impugnación acuerdo pleno"`). La doctrina localizada al preparar esta skill mantiene que el pacto es válido con los límites del art. 1255 CC y no oponible a la sociedad, que su infracción no basta por sí sola para anular un acuerdo social, y que la buena fe (art. 7.1 CC) puede impedir que quien firmó un pacto omnilateral impugne el acuerdo que lo cumple. Consecuencias de redacción, que explicas en la nota:
- Lleva a estatutos lo que deba vincular a la sociedad o a los adquirentes (transmisión, mayorías, valoración, arbitraje), en un anexo con el texto exacto y la obligación de todos de votarlo.
- Añade la obligación de votar en junta y en el consejo conforme al pacto y de promover las modificaciones estatutarias necesarias, con cláusula penal.
- Si se quiere una sanción societaria, valora configurar el cumplimiento del pacto como prestación accesoria estatutaria (arts. 86 a 89 LSC) cuyo incumplimiento voluntario permite excluir en la SL (art. 350 LSC); incorporar causas de exclusión exige el consentimiento de todos (art. 351 LSC). Busca la doctrina que ha admitido esta vía antes de proponerla.
- Exige que todo adquirente de participaciones se adhiera al pacto como condición de la transmisión.

**2. Transmisión en la SL.**
- Libre entre socios, al cónyuge, ascendientes, descendientes y sociedades del grupo, salvo que los estatutos digan otra cosa; en los demás casos, lo que digan los estatutos y, en su defecto, el régimen supletorio del art. 107.2 (comunicación a los administradores, consentimiento de la junta, denegación solo presentando adquirentes de la totalidad por conducto notarial, libre transmisión si pasan tres meses sin respuesta). Si el pacto restringe las transmisiones entre socios o familiares, dilo también en estatutos.
- Nulas las cláusulas estatutarias que hagan prácticamente libre la transmisión y las que obliguen a transmitir un número distinto del ofrecido; la prohibición de transmitir solo vale si se reconoce el derecho de separación en cualquier momento y con el consentimiento de todos; los estatutos pueden impedir la transmisión o la separación durante un máximo de cinco años desde la constitución o desde la escritura de la ampliación (art. 108 LSC). Calcula la fecha límite con la fecha de constitución (o de la escritura de la ampliación, para las participaciones nuevas): si la permanencia pactada va más allá, el exceso solo vale entre las partes y la nota debe decirlo. El acompañamiento proporcional obliga al vendedor a transmitir menos de lo que ofreció para dar cabida al que acompaña, efecto próximo al que prohíbe el art. 108.2: déjalo en el pacto y lleva a estatutos solo el acompañamiento total.
- La transmisión consta en documento público (art. 106 LSC); la que no se ajuste a la ley o a los estatutos no produce efecto frente a la sociedad (art. 112 LSC); la sociedad solo reputa socio a quien figura en el libro registro (art. 104 LSC); rige el régimen vigente al comunicar el propósito de transmitir (art. 111 LSC).
- Transmisiones mortis causa y forzosas: arts. 110 y 109 LSC. Si el pacto quiere un derecho de adquisición al fallecimiento, llévalo a estatutos con el valor razonable al día del fallecimiento y el plazo de tres meses que fija el art. 110.2.
- Introducir o modificar después el régimen de transmisión da derecho de separación a quien no vote a favor (art. 346.2 LSC): avísalo si el pacto se firma con la sociedad ya en marcha.
- Registro: son inscribibles la adquisición preferente que expresa transmisiones, condiciones y plazo, y la obligación de transmitir cuando concurran circunstancias claras y precisas (art. 188.2 y 3 del Real Decreto 1784/1996); también las cláusulas penales en garantía de obligaciones pactadas e inscritas, los criterios de valoración pactados por unanimidad, el arbitraje y la venta conjunta en grupos consolidados (art. 175.2 del mismo real decreto). El arrastre y la salida del socio trabajador se llevan a estatutos por la vía del art. 188.3. **Criterio registral**: las resoluciones de la Dirección General de Seguridad Jurídica y Fe Pública no están en el conector (`buscar_boe` solo busca normas): búscalas en internet en el BOE y cítalas con enlace y fecha de consulta (punto 3 de la puerta). En las pruebas, la Resolución de 4 de diciembre de 2017 (BOE-A-2017-15582) admite el arrastre estatutario al amparo del art. 188.3, pero exige el consentimiento de todos los socios, sin que pueda suplirlo un derecho de separación (basta el acuerdo mayoritario si los demás consienten individualmente después). Por eso la modificación estatutaria que introduce el arrastre o la obligación de transmitir del socio trabajador debe contar con el voto o el consentimiento individual de todos los socios: prevelo en el pacto y en la escritura, y si defiendes a un minoritario, recuerda que sin su consentimiento esas cláusulas no entran en los estatutos.

**3. Transmisión en la SA.** Solo son válidas frente a la sociedad las restricciones sobre acciones nominativas impuestas en estatutos; si se introducen por modificación, quien no votó a favor no queda sometido durante tres meses desde la publicación en el BORME; son nulas las que hagan prácticamente intransmisible la acción; la autorización previa exige causas estatutarias y se entiende concedida a los dos meses (art. 123 LSC). Lee el art. 123 del Real Decreto 1784/1996: prohibición de transmitir inscribible solo hasta dos años desde la constitución y ninguna restricción que impida obtener el valor real. Mortis causa y ejecución: arts. 124 y 125 LSC. Lo que no quepa en estatutos queda en el pacto con remedio contractual.

**4. Valoración.** En la SL, a falta de acuerdo, el valor razonable lo fija un experto independiente distinto del auditor de la sociedad, y los estatutos no pueden encomendar la valoración al auditor de la sociedad (art. 107.2.d y 3 LSC); en separación y exclusión, el experto lo designa el registrador mercantil (art. 353 LSC) y el reembolso se rige por el art. 356. En estos artículos la respuesta del conector trae, además del texto vigente («experto independiente», vigente desde el 01/01/2016), una nota «Téngase en cuenta» que reproduce otra redacción («auditor de cuentas»): usa la del cuerpo del artículo. Si la sociedad compra las participaciones del que sale, solo puede hacerlo con cargo a beneficios o reservas libres y con autorización de la junta (art. 140 LSC).

**5. Gobierno.**
- Mayorías en la SL: ordinaria del art. 198 y reforzadas legales del art. 199; los estatutos pueden exigir un porcentaje mayor sin llegar a la unanimidad y el voto favorable de un número de socios (art. 200). En la SA: arts. 194 y 201 (los estatutos pueden elevar las mayorías).
- Si con el porcentaje elegido el acuerdo exige de hecho el voto de todos los socios, adviértelo en la nota como riesgo de calificación registral por el límite del art. 200.1 y mantén el veto también en el pacto.
- La junta puede dar instrucciones o reservarse la autorización de asuntos de gestión salvo que los estatutos lo excluyan (art. 161), pero las limitaciones de las facultades representativas de los administradores son ineficaces frente a terceros (art. 234): el veto es interno y su remedio es contractual.
- Consejo: mínimo tres miembros y máximo doce en la SL (art. 242); en la SA existe el sistema proporcional del art. 243; en la SL el reparto de consejeros se asegura con un compromiso de voto en el pacto. La junta puede separar a los administradores en cualquier momento y en la SL los estatutos solo pueden reforzar esa mayoría hasta dos tercios (art. 223): el puesto del minoritario es siempre una protección contractual, díselo.
- Información del minoritario: en la SL el órgano de administración puede denegar la información si perjudica el interés social, salvo que la pidan socios con el 25 % (art. 196); el socio con el 5 % puede pedir al registrador un auditor si la sociedad no está obligada, dentro de los tres meses siguientes al cierre (art. 265.2). Si el cliente no llega al 25 %, el pacto debe darle información periódica propia.
- Conflicto de intereses del socio (art. 190): no vota, entre otros, su exclusión ni la autorización para transmitir participaciones sujetas a restricción; tenlo en cuenta al diseñar mayorías para esos acuerdos.
- Impugnación de acuerdos y caducidad de un año: arts. 204 y 205.

**6. Separación, exclusión y bloqueo.** Causas legales y estatutarias de separación (arts. 346 y 347; estas últimas exigen el consentimiento de todos); separación por falta de dividendos salvo disposición contraria de los estatutos y con las exclusiones de su apartado 5 (art. 348 bis: si el pacto fija política de dividendos, coordínala con él); exclusión legal en la SL (art. 350) y estatutaria (art. 351). Un bloqueo que impida el funcionamiento de los órganos es causa de disolución (art. 363.1.d): el pacto debe traer un mecanismo de desbloqueo antes de llegar ahí.

**7. Socios trabajadores y no competencia.** La dedicación puede configurarse como prestación accesoria estatutaria, con retribución que no exceda el valor de la prestación, autorización para transmitir y consentimiento individual para crearla o modificarla (arts. 86 a 89 LSC). Si el socio es administrador de una SL, su relación de servicios requiere acuerdo de junta (arts. 220 y 230.2 LSC) y la dispensa de no competencia, acuerdo expreso y separado de la junta (art. 230.3). Si además es trabajador por cuenta ajena, el pacto de no competencia posterior al contrato de trabajo tiene los límites y requisitos del art. 21.2 del Estatuto de los Trabajadores (dos años para técnicos y seis meses para los demás, interés efectivo y compensación adecuada): coordina ambos pactos y remite lo laboral al abogado laboralista. Busca también la doctrina social: `buscar_sentencias` (`consulta="pacto de no competencia postcontractual compensación económica adecuada interés industrial efectivo"`, `base="TS"`, `jurisdiccion="SOCIAL"`). La Sala de lo Social ha considerado laboral, y de su competencia, la no competencia de trabajadores incluida en un documento societario, y nula la facultad del empresario de dejarla sin efecto unilateralmente: localiza esas sentencias con `buscar_sentencias` (`consulta="pacto no competencia documento societario competencia orden social"` y `consulta="pacto no competencia renuncia unilateral empresario nula"`, `base="TS"`, `jurisdiccion="SOCIAL"`) y léelas antes de citarlas. Entre empresas socias, comprueba el art. 1 de la Ley 15/2007.

**8. Control conjunto.** Si el pacto da a un socio vetos sobre decisiones estratégicas (presupuesto, plan de negocio, nombramiento de la dirección), puede atribuirle control conjunto: lee el art. 7 de la Ley 15/2007 y, si se superan los umbrales del art. 8, la obligación de notificar y de no ejecutar del art. 9. Díselo al abogado en la nota; no calcules cuotas de mercado.

**9. Cláusula penal, duración y arbitraje.**
- Pena sustitutiva de la indemnización salvo pacto (art. 1152 CC); el deudor no se libera pagándola salvo que se reservara ese derecho, y el acreedor solo exige a la vez pena y cumplimiento si se le concedió expresamente (art. 1153); moderación judicial si hubo cumplimiento parcial o irregular (art. 1154).
- Duración: arts. 1700, 1705 a 1707 CC y 224 CCom (ver cláusula 11).
- Arbitraje: materias de libre disposición (art. 2 de la Ley 60/2003) y convenio por escrito (art. 9); el estatutario exige dos tercios de los votos y permite someter la impugnación de acuerdos a árbitros con administración institucional (art. 11 bis); el laudo que anula un acuerdo inscribible se inscribe (art. 11 ter).

**10. Tributación.** No des tipos ni importes. Avisa de que las opciones de compra, el arrastre y la retribución del socio trabajador tienen efectos fiscales que el abogado debe comprobar; si necesita doctrina, `buscar_consultas_hacienda`.

## Cláusulas clave y jurisprudencia

Para cada cláusula: redacción según a quién defiendas, riesgo y búsqueda. La jurisprudencia es **imprescindible** (apartado 8 del formato) para la no competencia, la cláusula penal y la duración; para las demás se busca y se cita si existe.

1. **Materias reservadas y vetos.** Mayoritario: lista corta y cerrada, umbral económico alto, veto solo en junta. Minoritario o inversor: lista amplia (modificación de estatutos, aumentos sin preferencia, endeudamiento y garantías por encima de un umbral, operaciones con partes vinculadas, presupuesto, venta de activos esenciales, retribución de administradores), también en el consejo, y reflejo estatutario (art. 200 LSC). Siempre: plazo para responder, silencio y consecuencia del veto (desbloqueo).
2. **Consejo y derechos de información.** Número de consejeros que propone cada socio y compromiso de votarlos y de cesarlos a petición de quien los propuso; información periódica con fechas; en la SA, recuerda el art. 243.
3. **Permanencia (lock-up).** Inversor: permanencia del fundador y del socio trabajador. Fundador: plazo corto y excepciones (grupo, familia, sucesión). En estatutos, dentro del máximo del art. 108.4 LSC (SL) o del art. 123 del Real Decreto 1784/1996 (SA).
4. **Adquisición preferente.** Define si es tanteo sobre una oferta de tercero o derecho de primera oferta; plazo, prorrata, adquisición de la totalidad (art. 108.2 LSC), precio y condiciones iguales a las del tercero, y qué pasa si nadie la ejercita. Llévala a estatutos con el contenido del art. 188.2 del Real Decreto 1784/1996.
5. **Arrastre (drag along).** Quien quiere vender el 100 %: umbral bajo y poder para ejecutar. Minoritario: umbral alto, precio mínimo o múltiplo, mismo precio y condiciones por participación, pago en efectivo, garantías del minoritario limitadas a titularidad y capacidad, y plazo. En estatutos, como obligación de transmitir con circunstancias claras y precisas (art. 188.3). Busca doctrina: `consulta="pacto de socios cláusula de arrastre acompañamiento validez"`, `base="AN"`, `tipo_organo="AP"`.
6. **Acompañamiento (tag along).** Minoritario: total si cambia el control, proporcional en las demás ventas. Mayoritario: solo si se transmite el control. Si el comprador no acepta comprar a todos, el vendedor no puede vender.
7. **Cambio de control de un socio sociedad.** Se trata como transmisión indirecta y dispara la adquisición preferente o una opción de compra; define «control».
8. **Bloqueo.** Escalado a los socios, mediación con plazo, y después opción de compra y venta cruzada, oferta cruzada o venta conjunta; valoración por experto independiente con plazo y reparto de costes. Coordínalo con el art. 363.1.d LSC.
9. **Salida del socio trabajador (buen y mal saliente).** Inversor: opción de compra sobre sus participaciones si deja de prestar servicios, con precio reducido si sale por causa imputable. Socio trabajador: causas cerradas y objetivas, valor razonable si sale sin culpa, adquisición gradual de derechos. El descuento del «mal saliente» funciona como pena: lee la doctrina sobre moderación (`consulta="cláusula penal moderación improcedente cuando el incumplimiento es el previsto"`, `base="TS"`) y la de exclusión y valoración (`consulta="exclusión socio valoración participaciones valor razonable orden público"`, `base="TS"`); no fijes un precio que vacíe de contenido el valor razonable sin decírselo al abogado.
10. **No competencia, no captación y dedicación.** Ámbito material y territorial ligado a la actividad real, duración mientras sea socio y un plazo razonable después, y compensación si es socio trabajador. Imprescindible: `consulta="pacto de no competencia socio pacto parasocial validez duración ámbito"` con `base="AN"` y `tipo_organo="AP"` (en las pruebas, la misma consulta en `base="TS"` no devolvió nada aplicable; en el Supremo prueba `consulta="pacto de no concurrencia compraventa de acciones participaciones"`). Lee el fundamento que fija los límites (actividad efectiva, ámbito geográfico, duración) y redacta dentro de ellos. Si el socio es trabajador por cuenta ajena, respeta el art. 21.2 ET.
11. **Duración y denuncia.** Plazo determinado (con prórrogas) o vigencia mientras la sociedad exista y el firmante sea socio, con un máximo. Imprescindible: `consulta="pacto parasocial duración indefinida denuncia unilateral vinculaciones perpetuas"` en `base="TS"` y en `base="AN"` con `tipo_organo="AP"`. En las pruebas, las Audiencias aplican por analogía los arts. 1700, 1705 CC y 224 CCom para admitir la denuncia de los pactos indefinidos y la rechazan cuando hay plazo cierto; la Sala Primera ha considerado contrario al art. 1255 CC mantener indefinidamente restricciones a la transmisión. Si el cliente quiere estabilidad, fija un plazo; si quiere poder salir, prevé la denuncia con preaviso y efectos.
12. **Dividendos y financiación.** Política de reparto coordinada con el art. 348 bis LSC (suprimirlo exige el consentimiento de todos, art. 348 bis.2: si defiendes al minoritario, es una baza; busca además `consulta="acuerdo de no reparto de dividendos abuso de la mayoría impugnación socio minoritario"`, `base="TS"`); aportaciones o préstamos de socios y consecuencias de no atenderlos; preferencia en aumentos (art. 304 LSC) y, si hay inversor, antidilución.
13. **Cláusula penal.** Acreedor: pena cumulativa con la indemnización y exigible además del cumplimiento (dilo expresamente, art. 1153 CC). Deudor: pena sustitutiva, limitada a incumplimientos graves y con plazo de subsanación. Imprescindible: `consulta="cláusula penal moderación improcedente cuando el incumplimiento es el previsto"` y `consulta="interpretación artículo 1152 función de la cláusula penal sancionadora"` (`base="TS"`); lee la más reciente y di en la nota si la pena pactada es liquidatoria, cumulativa o puramente sancionadora.
14. **Confidencialidad, notificaciones, cesión y adhesión.** Remite la confidencialidad compleja a `confidencialidad-nda`. Adhesión obligatoria del adquirente mediante documento de adhesión anexo.
15. **Ley, tribunales o arbitraje.** Si hay arbitraje, que el del pacto y el estatutario remitan a la misma institución y reglas.

## Documentos que se entregan

Según `references/formato-y-entrega-contratos.md`, dos documentos:

1. `contrato-pacto-socios-<sociedad>-<AAAAMMDD>.docx`:
   - Título («PACTO DE SOCIOS DE [DENOMINACIÓN SOCIAL]»), lugar y fecha; REUNIDOS e INTERVIENEN (cada socio, y la sociedad si comparece para conocerlo y comprometerse a respetarlo).
   - EXPONEN: sociedad, capital y reparto, finalidad del pacto.
   - ESTIPULACIONES, en este orden: definiciones; objeto y prevalencia entre las partes; gobierno (junta, materias reservadas, consejo, información); compromisos de voto y de modificación estatutaria; transmisión (permanencia, transmisiones libres, adquisición preferente, arrastre, acompañamiento, cambio de control, adhesión); socios trabajadores (dedicación, retribución, salida); bloqueo; valoración; no competencia y no captación; dividendos y financiación; incumplimiento y cláusula penal; duración y denuncia; confidencialidad; notificaciones; ley y tribunales o arbitraje; integridad del acuerdo.
   - Anexos: I, texto de las cláusulas estatutarias que las partes se obligan a aprobar; II, documento de adhesión; III, método de valoración si es extenso. El pacto no lleva jurisprudencia.
2. `nota-pacto-socios-<sociedad>-<AAAAMMDD>.docx`:
   - Régimen aplicable con los artículos leídos: qué es imperativo en estatutos y qué pactable en el pacto.
   - Por cada cláusula crítica, qué dice, por qué, a quién protege y su base (artículo y, cuando proceda, párrafo literal con órgano, fecha y ECLI).
   - Qué se lleva a estatutos y qué queda solo en el pacto, con el riesgo de cada opción (oponibilidad, calificación registral, derecho de separación del art. 346.2).
   - Datos pendientes y comprobaciones registrales, de competencia y fiscales.

Marcadores para lo que falte: `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[DATOS REGISTRALES]`, `[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[DOMICILIO]`, `[PORCENTAJE]`, `[IMPORTE]`.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Sociedad y socios sociedad comprobados con `buscar_empresa_mercantil`; si firma quien no figura como administrador o apoderado, dicho en la nota.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos usados de la LSC, del CC, del Real Decreto 1784/1996 y, en su caso, del CCom, la Ley 60/2003, la Ley 15/2007 y el ET, con la línea de vigencia anotada.
- [ ] Cada cláusula estatutaria del anexo respeta los arts. 108 y 123 LSC y los arts. 188 y 123 del Real Decreto 1784/1996; la nota dice qué no es inscribible y queda solo en el pacto.
- [ ] Doctrina leída con `leer_sentencias` (párrafo de fundamentos) para no competencia, cláusula penal y duración; cada ECLI citado, leído o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el pacto y sobre la nota, corregido lo que señale; cada «posible disonancia» contrastada con el apartado leído.
- [ ] Definiciones únicas, porcentajes que suman el 100 %, plazos coherentes entre pacto y estatutos, marcadores en lugar de datos inventados.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas y cómo se resolvieron, qué va a estatutos, datos y documentos que faltan (estatutos, consentimiento del cónyuge, poderes), tabla de jurisprudencia y próximo paso (junta y escritura de modificación estatutaria).
