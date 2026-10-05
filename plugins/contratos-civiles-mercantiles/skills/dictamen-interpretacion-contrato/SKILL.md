---
name: dictamen-interpretacion-contrato
description: >-
  Emite un dictamen en Word sobre qué significa una cláusula o un contrato, cómo se integra una laguna o
  si cabe adaptarlo por alteración sobrevenida de las circunstancias (cláusula rebus sic stantibus), con
  antecedentes, cuestión, análisis, conclusiones y recomendación. Aplica las reglas de interpretación del
  Código Civil (arts. 1281-1289), la integración por buena fe (art. 1258), la regla contra proferentem
  (art. 1288 CC y art. 6 Ley 7/1998) y los actos propios. Úsala con «¿qué significa esta cláusula?», «el
  contrato no dice nada de…», «¿puedo pedir que me bajen el precio por…?», «dictamen». Para exigir el
  cumplimiento, requerimiento-cumplimiento; para resolver, resolucion-por-incumplimiento; para pactar el
  cambio, modificacion-novacion-cesion.
---

# Dictamen sobre interpretación, integración y alteración de un contrato

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Reglas de interpretación, integración y buena fe** → `buscar_articulo` (`ley="CC"`, del `"1281"` al `"1289"`, uno por uno, y `"1258"`, `"1255"`, `"1256"`, `"1115"` y `"7"`).
- **Contratos mercantiles** → `buscar_articulo` (`ley="CCom"`, artículos `"50"`, `"57"` y `"59"`); el art. 2, con `ley="Código de Comercio de 1885"`: con `"CCom"`, `"Código de Comercio"`, `"BOE-A-1885-6627"` o `articulo="2º"` sale el artículo 2 del real decreto de promulgación («Un ejemplar de la edición oficial…»). Comprueba que el texto empieza por «Los actos de comercio».
- **Condiciones generales y consumidores** → `buscar_articulo` (`ley="BOE-A-1998-8789"`, artículos `"6"` y `"10"`) y (`ley="TRLGDCU"`, artículos `"65"` y `"80"`).
- **Alteración de circunstancias, imposibilidad y resolución** → `buscar_articulo` (`ley="CC"`, artículos `"1091"`, `"1105"`, `"1182"`, `"1184"`, `"1101"` y `"1124"`), `buscar_boe` para descartar una norma posterior o de emergencia que regule el caso (`desde` = fecha del contrato y `consulta` de una a tres palabras del título que tendría la norma: «revisión de precios», el nombre de la materia prima o del sector; con frases largas no devuelve nada), y (`ley="LO 1/2025"`, `articulo="5"`) para la negociación previa a la demanda.
- **Plazos de la recomendación** → `buscar_articulo` (`ley="CC"`, artículos `"5"` —cómputo de plazos por días, meses y años— y `"1964"` —prescripción de las acciones personales—) y el precepto especial del contrato si lo hay.
- **Norma propia del contrato** (arrendamiento, agencia, sociedades…) → `buscar_articulo` con el valor de `ley` de las anclas.
- **Doctrina de la Sala Primera** (interpretación, actos propios, rebus) → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CIVIL"`; Audiencias con `base="AN"`, `tipo_organo="AP"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (cuando el análisis dependa de quién firmó o de los actos de sus administradores).
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Si citas el art. 2 del Código de Comercio, `verificar_escrito` lo compara con el real decreto de promulgación y puede avisar de una disonancia falsa: compruébalo con `ley="Código de Comercio de 1885"` y explícalo en el resumen.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Una cláusula admite dos lecturas, contradice a otra o a un anexo, o hay versiones distintas del documento.
- Hay que saber si un supuesto está cubierto (qué comprende una garantía, un precio «cerrado», una exclusividad) o qué rige en lo que el contrato no previó.
- La conducta posterior de las partes (pagos, tolerancias, comunicaciones) cambia o confirma el sentido de lo pactado.
- Un cambio sobrevenido (costes, normativa, crisis sanitaria o de suministro) lleva a una parte a pedir la revisión o la salida del contrato, o el cliente quiere resistirse a esa petición.

Esta skill dictamina; no reclama ni modifica. Si el objetivo es otro, deriva:

| Objetivo del cliente | Skill |
|---|---|
| Exigir el pago o el cumplimiento | `requerimiento-cumplimiento` o `reclamacion-deuda-monitorio` |
| Salir del contrato por incumplimiento | `resolucion-por-incumplimiento` |
| Pactar el cambio (adenda, novación, prórroga) | `modificacion-novacion-cesion` |
| Saber si una condición general es nula o abusiva | `condiciones-generales-consumidores` |
| Revisar un contrato entero antes de firmar | `revision-contrato-semaforo` |
| Negociar antes de demandar (requisito de la LO 1/2025) | `masc-propuesta-acuerdo` |
| Defectos de la cosa entregada | `vicios-ocultos-saneamiento` |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega. No se dictamina sobre un contrato que no se ha leído entero.

1. ★ Texto íntegro del contrato firmado, con anexos, adendas y condiciones generales; si hay versiones, cuál se firmó y cuándo.
2. ★ Cliente, su posición en el contrato y qué quiere conseguir con el dictamen.
3. ★ La cuestión, formulada como una o varias preguntas cerradas, y la lectura que sostiene cada parte.
4. ★ Quién redactó la cláusula; si es condición general o contrato de adhesión; si alguna parte es consumidor.
5. ★ Conducta de las partes, con fecha y documento: correos y borradores de la negociación, ejecución, facturas, pagos, reclamaciones, silencios y tolerancias.
6. Carácter civil o mercantil, sector y usos (arts. 1287 CC y 2 del Código de Comercio). Si se invoca un uso, pide cómo se prueba.
7. Ley aplicable: la pactada y si rige un Derecho civil foral o autonómico (Cataluña, Aragón, Navarra, País Vasco, Galicia, Baleares). Si aplica, busca su norma con `buscar_boe`; si el conector no devuelve el precepto (el Código civil de Cataluña, por su numeración con guion, no lo resuelve `buscar_articulo`), léelo en internet en el texto consolidado oficial y cítalo con enlace (punto 3 de la puerta).
8. ★ Si se plantea la alteración de circunstancias: fecha y duración del contrato y fase de ejecución; qué ocurrió y cuándo; datos económicos antes y después (contabilidad, informe pericial); cláusulas de reparto de riesgos (fuerza mayor, revisión de precios, desistimiento, seguros); si se pidió renegociar y qué se contestó; normas dictadas por el hecho.
9. Si hay un plazo en curso (preaviso, prescripción, caducidad), su fecha inicial.

## Régimen jurídico y método de análisis

Lee cada artículo con `buscar_articulo` en esta conversación antes de aplicarlo. Sigue este orden y deja escrito en el dictamen cada paso.

**1. Califica la cuestión.** Separa en el dictamen tres preguntas distintas: interpretación (qué quisieron las partes), integración (qué rige en lo que no previeron, art. 1258 CC) y validez (si la cláusula es nula o abusiva, que es otra skill). Decide si el contrato es mercantil: se rige por el derecho común en interpretación salvo lo especial del Código de Comercio (art. 50 CCom).

**2. Literalidad e intención (art. 1281 CC).** Si los términos son claros y no dejan duda sobre la intención, se está a su sentido literal; si las palabras parecen contrarias a la intención evidente, prevalece la intención. Para la Sala Primera, la literalidad es el punto de partida y el fin es la voluntad real común, sobre el contrato entendido como un todo (consulta 1). Transcribe la cláusula literal; nunca la parafrasees antes de analizarla.

**3. Conducta de las partes (art. 1282 CC).** Atiende principalmente a los actos coetáneos y posteriores al contrato, con fecha y prueba de cada uno. El precepto no nombra los tratos preliminares: si usas borradores o correos previos, preséntalos como indicio de la intención común y busca doctrina antes de darles más peso (consulta 8). Comprueba si el contrato tiene una cláusula de acuerdo íntegro («sustituye a cualesquiera acuerdos o comunicaciones anteriores»): la otra parte la opondrá a esos correos. Si no encuentras doctrina aplicable, no apoyes la conclusión en los tratos preliminares y dilo; lo mismo con cualquier regla que solo uses como refuerzo.

**4. Reglas complementarias.** Alcance: los términos generales no comprenden cosas ni casos distintos de los que se propusieron contratar (art. 1283). Conservación: el sentido más adecuado para que la cláusula produzca efecto (art. 1284). Sistemática: unas cláusulas por otras (art. 1285). Naturaleza y objeto del contrato (art. 1286). Usos del país, que además suplen omisiones (art. 1287). En contratos mercantiles, buena fe y sentido recto, propio y usual de las palabras, sin restringir los efectos que naturalmente se derivan (art. 57 CCom) y usos del comercio (art. 2 CCom).

**5. Oscuridad imputable (contra proferentem).** La interpretación de las cláusulas oscuras no favorece a quien causó la oscuridad (art. 1288 CC). Aplícala después de las reglas anteriores y di quién redactó y por qué la cláusula es oscura; si el texto se negoció y cada parte redactó una frase, identifica quién escribió precisamente la que causa la duda: la regla puede volverse contra el cliente. En condiciones generales: prevalecen las particulares salvo que las generales sean más beneficiosas, y las dudas se resuelven a favor del adherente (art. 6 Ley 7/1998); con consumidores, en acciones individuales, la interpretación más favorable (art. 80.2 TRLGDCU).

**6. Última regla (art. 1289 CC).** Si la duda recae sobre circunstancias accidentales: en los gratuitos, menor transmisión; en los onerosos, mayor reciprocidad de intereses. Si recae sobre el objeto principal y no puede conocerse la voluntad, el contrato es nulo: dilo como riesgo. En mercantil, la duda que no se resuelva por el art. 2 CCom se decide a favor del deudor (art. 59 CCom).

**7. Integración.** El contrato obliga también a las consecuencias que, según su naturaleza, sean conformes a la buena fe, al uso y a la ley (art. 1258 CC). Si la laguna nace de una condición general no incorporada o nula, se integra por el art. 1258 (art. 10.2 Ley 7/1998); con consumidores, a su favor (art. 65 TRLGDCU). Integrar no es añadir lo que las partes excluyeron: si el contrato reguló la materia, es interpretación.

**8. Buena fe y actos propios.** Los derechos se ejercitan conforme a la buena fe y no se ampara el abuso del derecho (art. 7 CC). Para oponer los actos propios, el acto previo tiene que ser concluyente e inequívoco y definir la situación jurídica de su autor (consulta 3); una tolerancia aislada no basta. Si una cláusula deja la validez o el cumplimiento al arbitrio de una parte, analiza los arts. 1256 y 1115 CC.

**9. Alteración sobrevenida de las circunstancias (rebus sic stantibus).** No está regulada con carácter general en ninguna ley: compruébalo con `buscar_boe` para la materia y la fecha del contrato y di en el dictamen qué normas especiales existen y cómo se relacionan con la doctrina según la Sala Primera (en alquileres de local durante la pandemia, lee cómo ha tratado las medidas de los reales decretos-leyes de 2020 antes de invocar la rebus). Requisitos que exige hoy la Sala Primera; léelos en la resolución que cites (consulta 4):
- una alteración de tal magnitud que incremente de modo significativo el riesgo de frustración de la finalidad del contrato o haga excesivamente onerosa la prestación;
- totalmente imprevisible al contratar: no lo es la que está dentro de los riesgos normales del contrato;
- riesgo no asumido expresa ni implícitamente por quien la invoca, ni asignado por el contrato (cláusulas de riesgo, revisión, desistimiento) o por su naturaleza (en el alquiler de local, la caída de ingresos del negocio es, en principio, riesgo del arrendatario);
- prueba del desequilibrio concreto: la notoriedad del hecho no basta; hace falta prueba contable o pericial;
- efecto: sobre todo, modificar el contrato para reequilibrarlo; la resolución, solo en último término;
- buena fe: valora si quien pide la adaptación propuso renegociar y cómo respondió la otra parte.
Distingue la rebus de la imposibilidad sobrevenida (arts. 1182, 1184 y 1105 CC: libera al deudor), de la frustración del fin del contrato (consulta 5) y del incumplimiento (art. 1124 CC). Antes de una demanda de adaptación hay que intentar la negociación previa (art. 5 de la LO 1/2025): recomiéndala y deriva a `masc-propuesta-acuerdo`.

**10. Según a quién defiendas.** Construye el análisis desde la posición del cliente, pero expón en el dictamen los argumentos contrarios y su peso.
- Quien sostiene la lectura literal: claridad de los términos (art. 1281, párrafo primero), coherencia de la conducta posterior con esa lectura y ausencia de oscuridad imputable a su cliente.
- Quien sostiene otra lectura: contradicción entre las palabras y la intención evidente (art. 1281, párrafo segundo), probada con actos coetáneos y posteriores (art. 1282) y con el conjunto del contrato (art. 1285); si la otra parte redactó, art. 1288.
- Quien pide la adaptación por alteración de circunstancias: prueba contable o pericial del desequilibrio, cláusulas que no asignan ese riesgo, propuesta de renegociación documentada y un remedio proporcionado y temporal antes que la resolución.
- Quien la resiste: cláusulas de reparto de riesgos, previsibilidad del hecho al contratar, riesgo propio de la actividad de la otra parte, falta de prueba del impacto y ofertas razonables ya hechas.

## Jurisprudencia: consultas y uso

El dictamen es un documento en el que la jurisprudencia es imprescindible (apartado 8 del formato): cada conclusión discutible lleva al menos una resolución leída. Consultas (`base="TS"`, `jurisdiccion="CIVIL"`; reformula como máximo dos veces y, si el Supremo no ha tratado el punto, pasa a `base="AN"`, `tipo_organo="AP"`, diciendo que es doctrina de Audiencia):

1. Método: `consulta="interpretación del contrato voluntad real común sentido literal punto de partida interpretación sistemática"`.
2. Oscuridad imputable al redactor: `consulta="cláusula oscura interpretación contra quien la redactó artículo 1288"`.
3. Actos propios: `consulta="actos propios acto concluyente e indubitado que defina la situación jurídica"` (la doctrina es antigua y estable: puedes citar un hito si no hay resolución reciente).
4. Rebus: `consulta="rebus sic stantibus requisitos alteración extraordinaria imprevisible excesiva onerosidad riesgo"`; para arrendamientos de local tras la pandemia, añade `fecha_desde="01/01/2024"`.
5. Frustración del fin: `consulta="frustración del fin del contrato desaparición de la base del negocio resolución"`.
6. Integración: `consulta="integración del contrato artículo 1258 buena fe obligaciones no pactadas expresamente"`.
7. Para la cláusula concreta, añade a la consulta el tipo de contrato y la palabra clave de la cláusula («opción de compra», «exclusividad», «revisión de precios»); por ejemplo, `consulta="interpretación contrato de distribución exclusiva territorio venta directa del fabricante"`.
8. Tratos preliminares y acuerdo íntegro: `consulta="negociaciones previas al contrato valor interpretativo actos anteriores intención común de las partes artículo 1282"` y `consulta="cláusula de acuerdo íntegro interpretación tratos preliminares"`.

Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que vayas a citar. Comprueba que el párrafo es razonamiento de la Sala y no alegación de parte, resumen de lo que dijo la sentencia de instancia ni voto particular (si los tres párrafos devueltos son de ese tipo, repite la lectura con otros `terminos`), y no traslades hechos ni nombres de aquel pleito: si el párrafo útil nombra a las partes, sustituye cada nombre por su posición entre corchetes («[el concesionario]») y dilo. Si la resolución inadmite un recurso o solo confirma la interpretación de instancia por no ser ilógica, úsala por su razonamiento y dilo.

## Documento que se entrega

`dictamen-interpretacion-<parte-principal>-<AAAAMMDD>.docx`, maquetado como el apartado 2 del formato (Times New Roman 12, A4, márgenes de 3 cm, justificado, interlineado 1,5). No se entrega nota aparte: la justificación va dentro.

1. **Encabezamiento**: «DICTAMEN», destinatario (`[CLIENTE]`), abogado firmante, fecha, asunto y la mención de confidencialidad y secreto profesional.
2. **I. Antecedentes**: contrato (partes, fecha, objeto), cláusulas en cuestión transcritas literalmente y hechos relevantes numerados con su documento.
3. **II. Cuestiones planteadas**: preguntas cerradas y numeradas.
4. **III. Normas aplicables**: artículos leídos, con su texto vigente cuando la conclusión dependa de la letra.
5. **IV. Análisis**, una sección por cuestión: sentido literal; contexto del contrato; conducta de las partes; finalidad; usos; regla de oscuridad si procede; integración si hay laguna; argumentos de la otra parte y por qué pesan menos o más. En la alteración de circunstancias, un subapartado por requisito con su prueba.
6. **V. Jurisprudencia**: párrafo literal entre comillas con órgano, fecha, número y ECLI, y una línea sobre por qué es aplicable.
7. **VI. Conclusiones**: numeradas, una por cuestión, con su grado de solidez (alto, medio o bajo) y el motivo; sin porcentajes.
8. **VII. Recomendación**: qué hacer (requerir, negociar, pactar una adenda, resistir, demandar), qué prueba conservar o reunir, y plazos con su precepto y fecha calculada (apartado 9 del formato).

**Reparto para la redacción rápida:** sin rótulos que se numeren solos (escribe `## I. Antecedentes` y siguientes): cabecera, antecedentes, cuestiones y normas aplicables (I a III) / una sección por cuestión planteada, con su análisis (IV) y, al final, las resoluciones que lo sostienen con su párrafo literal (V, repartido así entre las cuestiones) / conclusiones y recomendación con sus plazos (VI y VII). La alteración de circunstancias, si se plantea, lleva sección propia con un subapartado por requisito.

En el texto, nombra cada norma junto a cada artículo («artículo 1281 del Código Civil», «artículo 57 del Código de Comercio», «artículo 6 de la Ley 7/1998, de 13 de abril, sobre condiciones generales de la contratación»), para que `verificar_escrito` los enlace.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Contrato leído entero; cláusulas transcritas literalmente, sin paráfrasis.
- [ ] Leídos con `buscar_articulo` en esta conversación los arts. 1281 a 1289 y 1258 CC y los demás citados (también los de los plazos: arts. 5 y 1964 CC); el art. 2 del Código de Comercio, con `ley="Código de Comercio de 1885"`.
- [ ] Separadas interpretación, integración y validez; las cuestiones de validez, derivadas.
- [ ] Cada hecho usado para la intención o los actos propios tiene fecha y documento.
- [ ] En la rebus, cada requisito tratado con su prueba y comprobado con `buscar_boe` que no hay norma específica.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; ninguna conclusión discutible sin jurisprudencia.
- [ ] Lo que no dio Jurisprudenciator y se obtuvo en internet, citado con enlace y fecha de consulta desde fuente oficial y señalado en el resumen; ninguna sentencia citada sin `buscar_por_cita` y `leer_sentencias`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); los avisos de «posible disonancia» contrastados con el apartado leído.
- [ ] Marcadores en lugar de datos no facilitados; sin nombres ni datos de las partes en las consultas.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha dictaminado, conclusiones y su solidez, riesgos, tabla de jurisprudencia, plazos y próximo paso.
