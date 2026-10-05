---
name: confidencialidad-nda
description: >-
  Redacta en Word un acuerdo de confidencialidad (NDA) unilateral o mutuo, con su nota para el abogado:
  definición de la información confidencial y exclusiones, finalidad permitida, destinatarios, duración,
  devolución y destrucción, cláusula penal (moderación del art. 1154 CC), protección de secretos
  empresariales (Ley 1/2019), no captación de personal, ley, fuero y medidas cautelares. Úsala con «NDA»,
  «acuerdo de confidencialidad», «vamos a enseñar la información a un inversor, comprador o
  proveedor», «pacto de secreto». Si la otra parte manda su NDA, revísalo con la lista de esta skill en
  negociacion-contrapropuesta. Con empleados, usa el plugin laboral; si se ceden datos personales,
  encargo-tratamiento-datos.
---

# Acuerdo de confidencialidad (NDA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Secreto empresarial: concepto, usos lícitos, violación, acciones, prescripción y tribunal** → `buscar_articulo` (`ley="BOE-A-2019-2364"`, artículos `"1"`, `"2"`, `"3"`, `"9"`, `"10"`, `"11"`, `"14"`, `"20"` y `"21"`) y (`ley="LOPJ"`, `articulo="87"`).
- **Obligación, incumplimiento y cláusula penal** → `buscar_articulo` (`ley="CC"`, artículos `"1255"`, `"1101"`, `"1106"`, `"1107"`, `"1124"`, del `"1152"` al `"1155"`, uno por uno, `"1257"` y `"1964"`) y, si el receptor es consumidor, (`ley="TRLGDCU"`, `articulo="85"`).
- **Competencia desleal y no captación** → `buscar_articulo` (`ley="BOE-A-1991-628"`, artículos `"13"`, `"14"` y `"35"`) y (`ley="Ley 15/2007"`, `articulo="1"`) si las partes son competidoras.
- **Límites que el contrato no puede saltar** → `buscar_articulo` (`ley="BOE-A-2023-4513"`, artículos `"35"` y `"38"`; `ley="LSC"`, `articulo="228"`; `ley="ET"`, `articulo="21"` solo para derivar lo laboral; `ley="CP"`, artículos `"278"` y `"279"` para la nota).
- **Fuero, arbitraje y negociación previa** → `buscar_articulo` (`ley="LEC"`, artículos `"52"`, `"54"` y `"55"`; `ley="Ley 60/2003"`, artículos `"9"` y `"11"`; `ley="LO 1/2025"`, `articulo="5"`).
- **Doctrina** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CIVIL"`; `base="AN"`, `jurisdiccion="CIVIL"`, `tipo_organo="AP"` si el Supremo no ha tratado el punto) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (existencia, estado, administradores y apoderados vigentes de cada firmante; grupo al que pertenece).
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Nombra las leyes con su fecha: «artículo 1 de la Ley 1/2019, de 20 de febrero, de Secretos Empresariales», «artículo 14 de la Ley 3/1991, de 10 de enero, de Competencia Desleal», «artículo 38 de la Ley 2/2023, de 20 de febrero». Si un párrafo de la nota mezcla cláusula penal y secretos, `verificar_escrito` puede avisar de una disonancia en el art. 1154 CC: contrástalo con el texto leído.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Antes de compartir información en una negociación: venta de la empresa o de participaciones (revisión legal y contable), entrada de un inversor, empresa conjunta, alianza, licencia, desarrollo de un producto con un proveedor o un cliente.
- Como acuerdo autónomo o como cláusula de confidencialidad que se inserta en otro contrato (las cláusulas de esta skill sirven para ambos casos).
- **Unilateral**: solo una parte revela. **Mutuo**: las dos revelan; redacta obligaciones simétricas.

| Situación | Qué procede |
|---|---|
| Confidencialidad o no competencia de un trabajador | Plugin laboral, skill `pactos-contrato-trabajo` (el art. 21 ET exige interés efectivo y compensación en la no competencia; la Ley 1/2019 no puede limitar la movilidad del trabajador, art. 1.3) |
| Deber de secreto de un administrador | Nace de la ley (art. 228.b LSC); el NDA solo lo complementa |
| Se comparten datos personales | Además del NDA, `encargo-tratamiento-datos` (el NDA no sustituye al contrato del art. 28 RGPD) |
| Se licencia el know-how o se ceden resultados | `licencia-cesion-propiedad-intelectual` |
| Exclusiva o no competencia en una red comercial | `agencia-distribucion-franquicia` |
| El NDA forma parte de la compra de una sociedad o de un pacto entre socios | `compraventa-participaciones` o `pacto-de-socios` |
| NDA de la otra parte que hay que revisar | `negociacion-contrapropuesta`, con la tabla de cláusulas de esta skill |
| Ya se ha revelado la información | `requerimiento-cumplimiento` o `resolucion-por-incumplimiento`; la demanda de secretos, plugin de litigación civil |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ A quién defiende el abogado: parte que revela, parte que recibe o ambas (mutuo).
2. ★ Partes: denominación, CIF, domicilio y firmante con su cargo o poder; si la información se compartirá con sociedades del grupo, asesores o financiadores.
3. ★ Finalidad concreta para la que se comparte (evaluar la compra de X, desarrollar el producto Y): define el uso permitido.
4. ★ Qué información se entrega y cómo: categorías (técnica, comercial, financiera, clientes, código fuente), soporte (sala de datos, correos, visitas a instalaciones, muestras) y si hay auténticos secretos empresariales que exijan reglas especiales (acceso restringido, equipo limpio, registro de accesos).
5. ★ Duración: periodo en que se intercambia información y años que dura la obligación después.
6. Si hay datos personales o información de terceros sujeta a su propia confidencialidad.
7. Si las partes son competidoras (riesgo de intercambio de información sensible: precios, costes, estrategia).
8. Cláusula penal: si se quiere, importe y si sustituye a la indemnización o se suma a ella.
9. No captación de personal o de clientes, prohibición de ingeniería inversa, compromiso de no adquirir acciones: si se quieren y durante cuánto.
10. Ley, tribunales o arbitraje; idioma; si alguna parte es extranjera. Si rige un Derecho civil foral, busca la norma con `buscar_boe`; si el conector no devuelve el precepto, léelo en internet en el texto consolidado oficial y cítalo con enlace (punto 3 de la puerta).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de aplicarlo.

**1. Naturaleza del acuerdo.** Es un contrato atípico basado en la autonomía de la voluntad (art. 1255 CC): obligaciones de no hacer (no revelar, no usar fuera de la finalidad) y de hacer (proteger, devolver, destruir). El incumplimiento da derecho a indemnización (art. 1101 CC), que comprende daño emergente y lucro cesante (art. 1106), con el límite de lo previsible salvo dolo (art. 1107); en un contrato con obligaciones recíprocas, a resolver (art. 1124). La acción contractual prescribe a los cinco años y, en las obligaciones continuadas de no hacer, el plazo empieza cada vez que se incumplan (art. 1964.2). Solo obliga a quien firma (art. 1257): para que obligue a sociedades del grupo o a asesores, que firmen o que la receptora responda por ellos.

**2. Secretos empresariales (Ley 1/2019).**
- Es secreto empresarial la información que no es generalmente conocida ni fácilmente accesible en su círculo, tiene valor empresarial por ser secreta y ha sido objeto de medidas razonables de su titular para mantenerla en secreto (art. 1.1). El NDA es una de esas medidas, pero no la única: los tribunales han negado protección cuando las medidas eran las estándar de cualquier empresa y no ponían de manifiesto que el titular tratara esa información como secreta (consulta 2; al leer la resolución, comprueba si ese razonamiento es de la Sala o de la sentencia recurrida y atribúyelo a quien corresponda). Añade en la nota las medidas prácticas: marcado, accesos limitados y registro.
- Es ilícito usar o revelar un secreto incumpliendo un acuerdo de confidencialidad o una obligación que limite su uso (art. 3.2). Acciones: declaración, cesación, remoción, indemnización y publicación (art. 9); indemnización con lucro cesante, enriquecimiento injusto del infractor o una regalía hipotética (art. 10); prescripción de tres años desde que se conoce al infractor (art. 11); tribunal: la Sección de lo Mercantil del domicilio del demandado o del lugar de la infracción o sus efectos (art. 14 Ley 1/2019, que aún dice «Juzgado de lo Mercantil», y art. 87 LOPJ tras la LO 1/2025); medidas cautelares de cese, retención y embargo (arts. 20 y 21).
- Son lícitos la creación independiente y la observación, estudio, desmontaje o ensayo de un producto disponible, salvo que una obligación válida lo impida (art. 2.1.b): si defiendes a quien revela y entrega muestras o prototipos, prohíbe expresamente la ingeniería inversa.
- Ninguna cláusula impide la revelación en ejercicio de la libertad de expresión, para descubrir una actividad ilegal en defensa del interés general, a los representantes de los trabajadores o para proteger un interés legítimo reconocido (art. 2.3), ni la comunicación de infracciones protegida por la Ley 2/2023: quien informa conforme a esa ley no infringe ninguna restricción de revelación (art. 38.1, con las condiciones del art. 35). Incluye esa salvedad en el contrato.
- La violación de secretos es también competencia desleal (art. 13 Ley 3/1991), y la inducción a infringir deberes contractuales básicos, o aprovechar una infracción ajena conocida para explotar un secreto, también lo es (art. 14); esas acciones prescriben en un año desde que pudieron ejercitarse y se conoció al autor, y en todo caso en tres desde que acabó la conducta (art. 35). En la nota, advierte de que revelar un secreto de empresa estando obligado a reserva puede ser delito (art. 279 CP).

**3. Cláusula penal.** La pena sustituye a la indemnización de daños y al abono de intereses si no se pacta otra cosa (art. 1152 CC); no se puede exigir a la vez el cumplimiento y la pena si no se ha otorgado claramente esa facultad (art. 1153); el juez modera la pena cuando la obligación se ha cumplido en parte o irregularmente (art. 1154); la nulidad de la pena no arrastra la de la obligación principal (art. 1155). La Sala Primera no modera cuando el incumplimiento es precisamente el que las partes previeron al fijar la pena, ni porque la pena supere el daño real; solo admite moderar por analogía si la diferencia es extraordinaria y se debe a un cambio de circunstancias imprevisible al contratar (consulta 1). Por eso, describe con precisión el incumplimiento que activa la pena. Si el receptor es una persona física que actúa fuera de su actividad empresarial, es consumidor y la pena desproporcionada puede ser abusiva (art. 85.6 TRLGDCU): léelo antes.

**4. No captación y competencia.** El pacto de no contratar al personal de la otra parte es una obligación de no hacer entre las partes que no vincula a los trabajadores; la Sala Primera ha admitido una prohibición de contratar al personal de la otra parte limitada a un año tras el contrato, con cláusula penal (consulta 3). Limítala en tiempo, en personas (quienes intervinieron en el proyecto) y a la captación activa, con excepción de las ofertas públicas de empleo. Si las partes son competidoras, un acuerdo de no captación o un intercambio de información sensible no ligado a la operación puede ser una conducta colusoria nula (art. 1 Ley 15/2007): vincúlalo a la operación, limítalo y, para información sensible, prevé un equipo limpio.

**5. Fuero, arbitraje y urgencia.** La sumisión expresa vale si designa con precisión la circunscripción (art. 55 LEC), pero no en contratos de adhesión ni con consumidores, ni frente a las reglas imperativas del art. 52.1 (art. 54 LEC), entre ellas la de competencia desleal (art. 52.1.12.º): el fuero pactado cubre la acción contractual; la de secretos sigue el art. 14 Ley 1/2019. El convenio arbitral debe constar por escrito (art. 9 Ley 60/2003). Antes de demandar hay que intentar la negociación previa, pero no para pedir medidas cautelares antes de la demanda (art. 5.3 LO 1/2025): deja claro en el contrato que las medidas cautelares pueden pedirse al tribunal aunque se pacte arbitraje o mediación (el convenio arbitral no lo impide: art. 11.3 Ley 60/2003).

**6. Contraparte extranjera.** Si se elige una ley o unos tribunales extranjeros, o se aplican reglamentos de la Unión sobre ley aplicable o competencia, búscalos con `buscar_boe` y lee cada artículo con `buscar_articulo` por su CELEX; `verificar_escrito` no identifica esas normas. Si la norma no se obtiene del conector, léela en internet en EUR-Lex o en la fuente oficial y cítala con enlace y fecha de consulta, nunca de memoria.

## Cláusulas clave y jurisprudencia

| Cláusula | Si defiendes a quien revela | Si defiendes a quien recibe |
|---|---|---|
| Información confidencial | Toda la entregada por cualquier medio, marcada o no, más la existencia de la negociación | Solo la marcada como confidencial o confirmada por escrito en `[N]` días si fue oral |
| Exclusiones | Carga de la prueba de la exclusión en el receptor, con documentos de fecha anterior | Dominio público, posesión previa, desarrollo independiente, recibida lícitamente de tercero, exigida por ley o autoridad |
| Finalidad y destinatarios | Solo la finalidad descrita; destinatarios con necesidad de conocerla, por escrito, y responsabilidad por ellos | Grupo, asesores y financiadores sujetos a secreto profesional o a obligaciones equivalentes |
| Duración | La obligación dura `[N]` años y, para los secretos empresariales, mientras sigan siéndolo | Plazo cerrado, sin obligación indefinida |
| Devolución y destrucción | A requerimiento, con certificado firmado | Excepción para copias de seguridad automáticas y conservación legal, que siguen siendo confidenciales |
| Requerimiento de autoridad | Aviso previo, colaboración para limitar lo revelado | Revelación mínima exigida, sin responsabilidad |
| Cláusula penal | Importe fijo por cada incumplimiento, sin perjuicio del daño mayor (art. 1152 CC, pactado expresamente) | Pena sustitutiva, con tope y solo por incumplimiento doloso o culpa grave |
| Sin licencia ni garantía | La información se entrega «tal cual», sin licencia ni obligación de contratar | Igual; nada impide desarrollar productos propios con información no confidencial |
| No captación | `[N]` meses tras la negociación, personal que intervino, con pena | Plazo breve, solo captación activa, excepción de ofertas públicas |

Consultas (reformula como máximo dos veces; lee con `leer_sentencias`, `parrafos=3`, solo lo que vayas a citar):

1. Moderación de la pena: `consulta="cláusula penal moderación artículo 1154 incumplimiento previsto por las partes no procede moderar"`, `base="TS"`, `jurisdiccion="CIVIL"`.
2. Medidas razonables y concepto de secreto: `consulta="secreto empresarial medidas razonables información confidencial conocimiento generalmente"`, `base="TS"`, y `consulta="secretos empresariales medidas razonables acuerdo de confidencialidad Ley 1/2019"`, `base="AN"`, `tipo_organo="AP"`.
3. No captación de personal: `consulta="cláusula de no contratar trabajadores de la otra parte contratante indemnización"`, `base="TS"`.
4. Incumplimiento de un NDA: `consulta="incumplimiento del pacto de confidencialidad revelación de información confidencial indemnización cláusula penal"`, `base="AN"`, `tipo_organo="AP"`, `anios=6`.

La cláusula penal y la no captación son cláusulas cuya validez discute la jurisprudencia (apartado 8 del formato): la nota cita al menos una resolución literal para cada una. Si no aparece ninguna aplicable tras dos reformulaciones, aplica el punto 3 de la puerta (internet para localizarla, `buscar_por_cita` y `leer_sentencias` para citarla); si tampoco así aparece, detén la tarea.

## Documentos que se entregan

1. `contrato-confidencialidad-<parte-principal>-<AAAAMMDD>.docx`, maquetado según el apartado 2 del formato. Título «ACUERDO DE CONFIDENCIALIDAD» (añade «RECÍPROCO» si es mutuo). REUNIDOS, INTERVIENEN (con poder o cargo de cada firmante) y EXPONEN (la operación que se estudia y la necesidad de compartir información). ESTIPULACIONES:
   1. Definiciones: «Información Confidencial», «Parte Reveladora», «Parte Receptora», «Finalidad», «Representantes».
   2. Objeto y finalidad permitida.
   3. Obligaciones de la Parte Receptora: secreto, uso limitado, medidas de protección al menos iguales a las propias, prohibición de copias no necesarias y, si procede, de ingeniería inversa.
   4. Exclusiones y carga de la prueba.
   5. Destinatarios autorizados y responsabilidad por ellos.
   6. Revelación exigida por ley o autoridad, y salvedad de la Ley 1/2019 (art. 2.3) y de la Ley 2/2023.
   7. Ausencia de licencia, de garantía y de obligación de contratar.
   8. Devolución y destrucción, con certificado.
   9. Duración del intercambio y de la obligación.
   10. No captación (y otras obligaciones accesorias pactadas).
   11. Datos personales: remisión al acuerdo de tratamiento, si se comparten.
   12. Incumplimiento, cláusula penal y medidas cautelares.
   13. Cesión del acuerdo, solo con consentimiento.
   14. Notificaciones.
   15. Ley aplicable y fuero o arbitraje.
   16. Acuerdo íntegro y modificaciones por escrito.
   Cierre y firmas según el formato. Cita en el contrato solo los artículos cuyo efecto dependa de nombrarlos (arts. 1152 y 1153 CC si la pena es cumulativa).

   **Reparto para la redacción rápida:** una sección por bloque de estipulaciones (`### [ESTIPULACION]`): comparecencia, expositivos, definiciones, objeto y obligaciones de la Parte Receptora / exclusiones, destinatarios, revelación exigida, ausencia de licencia, devolución y duración / no captación, datos, incumplimiento y cláusula penal, cesión, notificaciones, ley, fuero y firmas. La nota: apartado 11 del formato.
2. `nota-confidencialidad-<parte-principal>-<AAAAMMDD>.docx` (apartado 3 del formato): régimen aplicable; cada cláusula crítica con su porqué y su base (pena, no captación, exclusiones, duración, fuero); medidas prácticas de protección que deben acompañar al acuerdo para que la información sea secreto empresarial; riesgos de competencia si las partes compiten; relevancia penal de la revelación; datos pendientes.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los arts. 1, 2, 3, 9, 10, 11 y 14 de la Ley 1/2019, CC 1152 a 1155 y 1964, y los demás citados.
- [ ] Posición del cliente reflejada en cada cláusula de la tabla; en el mutuo, obligaciones simétricas.
- [ ] Exclusiones, finalidad y duración coherentes con las definiciones; un término por concepto.
- [ ] Salvedad de la Ley 1/2019 (art. 2.3) y de la Ley 2/2023 incluida; nada que restrinja la movilidad de trabajadores; lo laboral, derivado.
- [ ] Pena descrita con el incumplimiento concreto que la activa y su naturaleza (sustitutiva o cumulativa) expresa.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`.
- [ ] Lo que no dio Jurisprudenciator y se obtuvo en internet, citado con enlace y fecha de consulta desde fuente oficial y señalado en el resumen; ninguna sentencia citada sin `buscar_por_cita` y `leer_sentencias`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); los avisos de «posible disonancia» contrastados con el apartado leído.
- [ ] Marcadores (`[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[IMPORTE]`, `[N]`) en lugar de datos inventados.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas, datos pendientes y riesgos, tabla de jurisprudencia, plazos (prescripción de tres años de la Ley 1/2019 y de un año de la Ley 3/1991) y próximo paso.
