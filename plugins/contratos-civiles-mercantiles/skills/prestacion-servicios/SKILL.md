---
name: prestacion-servicios
description: >-
  Redacta el contrato de prestación de servicios (arrendamiento de servicios) entre empresas o con un
  profesional autónomo, con su nota para el abogado en Word: consultoría, asesoría, mantenimiento,
  informática, marketing, externalización. Úsala cuando el abogado diga «contrato de servicios»,
  «contrato con un autónomo», «contrato de consultoría», «acuerdo de nivel de servicio», «SLA» o
  «honorarios por hitos». Ajusta alcance y entregables, niveles de servicio, honorarios, resultados,
  confidencialidad, responsabilidad, duración y desistimiento según defienda al cliente o al
  prestador, y avisa del riesgo de falso autónomo. Si se promete un resultado material (obra,
  reforma), usa contrato-obra; si lo principal es ceder software o contenidos,
  licencia-cesion-propiedad-intelectual; si el cliente es consumidor,
  condiciones-generales-consumidores.
---

# Prestación de servicios

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Calificación, duración, cumplimiento y responsabilidad** → `buscar_articulo` (`ley="CC"`, artículos `"1544"`, `"1583"`, `"1255"`, `"1256"`, `"1258"`, `"1100"`, `"1101"` a `"1107"`, `"1124"`, `"1152"` y `"1154"`).
- **Honorarios, plazo de pago, intereses y prescripción** → `buscar_articulo` (`ley="BOE-A-2004-21830"`, artículos `"2"` a `"9"`, uno por uno) y (`ley="CC"`, artículos `"1964"` y `"1967"`).
- **Riesgo de laboralidad, autónomo económicamente dependiente y contratas** → `buscar_articulo` (`ley="ET"`, artículos `"1"`, `"8"`, `"21"`, `"42"` y `"43"`) y (`ley="LETA"`, artículos `"1"`, `"11"`, `"12"`, `"15"` y `"16"`).
- **Resultados, secretos y datos personales** → `buscar_articulo` (`ley="TRLPI"`, artículos `"43"`, `"45"`, `"51"` y `"97"`; `ley="BOE-A-2019-2364"`, artículos `"1"` y `"3"`; `ley="RGPD"`, `articulo="28"`; `ley="LOPDGDD"`, `articulo="33"`).
- **Fuero, arbitraje y negociación previa** → `buscar_articulo` (`ley="LEC"`, artículos `"54"` y `"55"`; `ley="Ley 60/2003"`, `articulo="9"`; `ley="LO 1/2025"`, `articulo="5"`).
- **Doctrina** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; `base="AN"` + `tipo_organo="AP"` si no hay doctrina del Supremo o se litigará en esa plaza; laboralidad con `jurisdiccion="SOCIAL"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (existencia, estado, administradores y apoderados vigentes; concurso o disolución).
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Cita la morosidad como «artículo N de la Ley 3/2004, de 29 de diciembre», el autónomo como «artículo N de la Ley 20/2007, de 11 de julio, del Estatuto del trabajo autónomo» y la propiedad intelectual como «artículo N del Real Decreto Legislativo 1/1996, de 12 de abril, texto refundido de la Ley de Propiedad Intelectual» (con «Texto Refundido de la Ley de Propiedad Intelectual» a secas, el verificador atribuye el artículo al Código Civil). `verificar_escrito` no identifica el Reglamento (UE) 2016/679 (atribuye su artículo a la última norma española nombrada): comprueba el art. 28 con `buscar_articulo` e ignora ese veredicto.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Servicios entre empresas: consultoría, asesoría, auditoría, mantenimiento, soporte y servicios informáticos, marketing, logística, limpieza, seguridad, externalización de procesos.
- Servicios de un profesional autónomo para una empresa (diseñador, programador, formador, técnico, abogado o asesor externo).
- Condiciones generales de servicios B2B y anexos de nivel de servicio (SLA).

| Situación | Skill que procede |
|---|---|
| El cliente actúa fuera de su actividad empresarial o profesional | `condiciones-generales-consumidores` |
| Se promete un resultado material (construir, reformar, fabricar, instalar) y se paga por él | `contrato-obra` |
| Lo principal es crear y ceder software, diseño o contenidos | `licencia-cesion-propiedad-intelectual` (y esta skill para el servicio) |
| El prestador tratará datos personales del cliente | Esta skill, más el anexo de `encargo-tratamiento-datos` |
| Solo se quiere proteger información antes de contratar | `confidencialidad-nda` |
| El «prestador» promueve ventas del cliente a cambio de comisión | `agencia-distribucion-franquicia` |
| Hay que revisar o contestar el borrador de la otra parte | `revision-contrato-semaforo` o `negociacion-contrapropuesta` |
| Ya hay incumplimiento: reclamar, resolver o cobrar | `requerimiento-cumplimiento`, `resolucion-por-incumplimiento` o `reclamacion-deuda-monitorio` |
| El prestador es persona física que trabaja con horario, medios y órdenes del cliente | Detén la redacción y aplica el apartado «Riesgo de laboralidad» |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ A quién defiende el abogado (cliente o prestador) y si el texto es un contrato negociado o condiciones que la otra parte aceptará sin negociar.
2. ★ Partes: denominación o nombre, CIF o NIF, domicilio, firmante y poder. Si el prestador es persona física, pregunta además los datos del apartado 6.
3. ★ Servicios: descripción funcional, entregables concretos (si los hay), lugar de prestación, horarios de soporte, recursos que aporta cada parte, dependencias del cliente (información, accesos, aprobaciones).
4. ★ Niveles de servicio: indicadores medibles (disponibilidad, tiempos de respuesta y resolución, calidad), cómo se miden y quién los mide, periodo de cálculo y consecuencias (créditos de servicio, penalizaciones, resolución).
5. ★ Honorarios: importe fijo, por horas o por hitos; gastos y suplidos; revisión; facturación, plazo y medio de pago; si hay aceptación de entregables antes de pagar.
6. ★ Si el prestador es persona física: ¿trabaja para otros clientes?, ¿qué parte de sus ingresos procede de este cliente?, ¿tiene trabajadores o subcontrata?, ¿usa medios propios?, ¿decide cómo y cuándo trabaja?, ¿está de alta como autónomo?
7. ★ Duración: inicio, plazo determinado o indefinido, prórrogas, preaviso y si alguna parte podrá desistir sin causa.
8. Resultados: qué crea el prestador (informes, código, diseños, bases de datos) y quién debe ser su titular o licenciatario.
9. Confidencialidad y datos personales: qué información se intercambia y si el prestador accede a datos personales de clientes o empleados del cliente.
10. Personal del prestador: si trabajará en instalaciones del cliente, si el servicio es de la propia actividad del cliente, si habrá subcontratación.
11. Responsabilidad: tope, exclusiones, seguros de responsabilidad civil profesional exigidos.
12. Fin del contrato: devolución de información, transición a otro proveedor, asistencia posterior.
13. Si el contrato puede regirse supletoriamente por un Derecho civil propio: pregunta y, si aplica, busca la norma con `buscar_boe`; si no aparece, aplica la puerta.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota su línea de vigencia.

**Calificación.** En el arrendamiento de servicios una parte se obliga a prestar un servicio por precio cierto (art. 1544 CC); puede pactarse sin tiempo fijo, por tiempo cierto o para una obra determinada, y es nulo el hecho por toda la vida (art. 1583 CC). El Código apenas lo regula: el contrato debe prever lo que la ley no dice. Si el prestador asume un resultado y cobra por él, el régimen es el de obra (arts. 1588 y siguientes): riesgo, pago a la entrega y desistimiento del comitente cambian; si conviven actividad y entregables, dilo en la cláusula de objeto y regula la aceptación de cada entregable.

**Cumplimiento y responsabilidad.**

- Diligencia exigible: la que exija la naturaleza de la obligación y, a falta de pacto, la de un buen padre de familia (art. 1104 CC). Pacta el estándar (normas técnicas, buenas prácticas del sector, certificaciones) y si la obligación es de medios o de resultado para cada servicio.
- Mora e incumplimiento: arts. 1100, 1101, 1106 y 1124 CC; daños previsibles salvo dolo (art. 1107 CC).
- Es nula la renuncia a la responsabilidad por dolo (art. 1102 CC); la de negligencia puede moderarse (art. 1103 CC). La Sala Primera ha examinado las cláusulas de exoneración o limitación temporal o cuantitativa en arrendamientos de servicios negociados: válidas si respetan la buena fe y no cubren el dolo ni vacían la obligación esencial. Lee esa doctrina antes de fijar el tope.
- Niveles de servicio con penalizaciones: son cláusulas penales (arts. 1152 y 1154 CC). Decide si sustituyen a la indemnización o se acumulan («si otra cosa no se hubiere pactado») y si los créditos de servicio son el único remedio. La moderación judicial no cabe cuando la pena se pactó para ese incumplimiento, pero las penas extraordinariamente desproporcionadas pueden reducirse (art. 1255 CC).

**Duración y desistimiento.** La validez y el cumplimiento del contrato no pueden dejarse al arbitrio de una parte (art. 1256 CC). En contratos por tiempo determinado, sin pacto de desistimiento, la salida anticipada es incumplimiento con daños; con pacto de desistimiento recíproco y preaviso, la Sala Primera lo ha aplicado sin indemnización. En contratos indefinidos, cabe la denuncia unilateral con preaviso razonable conforme a la buena fe (art. 1258 CC). Busca y lee la doctrina que aplique al caso antes de redactar la cláusula.

**Honorarios y pago.** Entre empresas o con profesionales rige la Ley 3/2004, de 29 de diciembre, también para servicios (arts. 1 y 3): plazo supletorio de treinta días desde la prestación, aceptación o comprobación no superior a treinta días y máximo pactado de sesenta días naturales (art. 4); interés de demora automático y costes de cobro (arts. 5 a 8); nulidad de los pactos abusivos (art. 9). Prescripción: tres años desde que dejaron de prestarse los servicios para los honorarios de los profesionales que enumera el art. 1967 CC (reglas 1.ª y 2.ª y párrafo final; comprueba si el prestador encaja en ellas); en otro caso, cinco años (art. 1964.2 CC).

**Riesgo de laboralidad (falso autónomo).** Si el prestador es persona física, compara los hechos del apartado 6 de los datos con el art. 1.1 del Estatuto de los Trabajadores (servicios retribuidos por cuenta ajena y dentro del ámbito de organización y dirección de otro), con la presunción de contrato de trabajo del art. 8.1 ET y con el art. 1.1 de la Ley 20/2007 (actividad habitual, personal, directa, por cuenta propia y fuera del ámbito de dirección y organización de otro). Reglas:

- Si el prestador percibe del cliente al menos el 75 % de sus ingresos y reúne las condiciones del art. 11 de la Ley 20/2007, es autónomo económicamente dependiente: el contrato debe formalizarse por escrito, registrarse y hacer constar esa condición (art. 12), y su extinción sigue el art. 15 y las interrupciones justificadas del art. 16. No lo redactes con esta skill: remite a la skill `falso-autonomo-trade` del plugin de contratos laborales, si está instalado, o avisa al abogado de que debe tratarse como contrato TRADE.
- Si concurren indicios de dependencia y ajenidad (horario y lugar fijados por el cliente, medios del cliente, retribución fija sin riesgo, integración en su plantilla, exclusividad, órdenes sobre cómo trabajar), no ocultes el riesgo con cláusulas de estilo: dilo en la nota y recomienda revisar la relación con el plugin laboral. Busca doctrina con `jurisdiccion="SOCIAL"`, `base="TS"`.
- No uses la denominación «contrato mercantil» como salvaguarda: la calificación depende de cómo se presta el servicio.
- Las condiciones del art. 11.2 de la Ley 20/2007 son simultáneas: quien trabaja indiferenciado con la plantilla del cliente, con sus medios, sin organización propia o sin riesgo no es autónomo económicamente dependiente aunque supere el 75 %; el riesgo es de relación laboral.
- **Qué se entrega en esta rama.** Si los hechos muestran dependencia y ajenidad, no redactes el contrato de servicios (y menos con exclusividad o no competencia, que añaden indicios): entrega solo la nota (`nota-prestacion-servicios-<parte-principal>-<AAAAMMDD>.docx`) con la tabla «Hecho | Indicio de | Valoración», la doctrina leída de la Sala de lo Social y dos opciones: (A) contrato de trabajo con el plugin de contratos laborales (skill `contrato-trabajo-modalidad`, si está instalado), con la plena dedicación y la no competencia del art. 21 ET si se quieren; o (B) colaboración autónoma real, cambiando los hechos, y si el prestador supera el 75 % de ingresos, contrato TRADE con la skill `falso-autonomo-trade`. Indica también si hay resultados ya creados sin cesión escrita (arts. 43, 45 y 51 TRLPI). Solo si el abogado confirma unos hechos de autonomía real (y el prestador no es TRADE) se redacta el contrato con esta skill.

**Personal del prestador y contratas.** Si el servicio corresponde a la propia actividad del cliente, el art. 42 ET le obliga a comprobar que el contratista está al corriente con la Seguridad Social (certificación) y le hace responsable solidario de cotizaciones y salarios en los plazos que fija: prevé certificados periódicos, retención de pagos y repetición. Si el objeto se limita a poner trabajadores a disposición del cliente, hay cesión ilegal (art. 43 ET): el prestador debe organizar y dirigir a su personal con medios propios; recógelo en el contrato y revisa que la realidad lo sostenga.

**Resultados, secretos y datos.**

- Derechos de autor sobre lo creado por un prestador externo: la cesión se limita a los derechos, modalidades, tiempo y territorio pactados; sin mención del tiempo, cinco años; sin territorio, el país de la cesión; es nula la cesión de obras futuras en conjunto (art. 43 TRLPI); debe constar por escrito (art. 45 TRLPI). Las presunciones a favor del empresario de los arts. 51 y 97.4 TRLPI son para asalariados: con un prestador externo, la titularidad del cliente solo nace del pacto. Si la cesión es relevante, remite a `licencia-cesion-propiedad-intelectual`.
- Secretos empresariales: la protección exige medidas razonables para mantener la información en secreto (art. 1 de la Ley 1/2019) y el incumplimiento de un acuerdo de confidencialidad hace ilícita su utilización (art. 3.2): la cláusula debe identificar la información y las medidas.
- Si el prestador accede a datos personales por cuenta del cliente, el contrato de encargo del art. 28 del Reglamento (UE) 2016/679 es obligatorio y por escrito (art. 28.3 y 28.9); el encargado que usa los datos para sus fines pasa a ser responsable (art. 33 LOPDGDD). Incorpóralo como anexo con `encargo-tratamiento-datos`.

**Fuero y controversias.** Sumisión expresa no válida en contratos de adhesión o con condiciones generales impuestas (art. 54.2 LEC); arbitraje por escrito (art. 9 de la Ley 60/2003); cláusula de negociación previa coherente con el art. 5 de la LO 1/2025, que se ejecuta con `masc-propuesta-acuerdo`.

**Tributación.** Avisa de que el abogado debe comprobar el IVA de los servicios y, si el prestador es persona física profesional, la retención a cuenta del IRPF sobre sus facturas; no des tipos. Doctrina: `buscar_consultas_hacienda`.

## Cláusulas clave y jurisprudencia

Consultas con `jurisdiccion="CIVIL"` y `base="TS"` salvo indicación; lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar.

| Cláusula | Si defiendes al cliente | Si defiendes al prestador | Qué buscar |
|---|---|---|---|
| Alcance y entregables | Descripción cerrada, entregables con criterios de aceptación, plazo de aceptación y efecto del silencio | Lista de exclusiones, supuestos del cliente y dependencias; cambios solo por orden escrita con presupuesto | Solo arts. 1544 y 1258 CC; doctrina si la calificación obra/servicios es dudosa: `consulta="distinción arrendamiento de obra y arrendamiento de servicios obligación de resultado"` |
| Niveles de servicio y penalizaciones | Indicadores medidos por el cliente o por herramienta auditable; penalizaciones acumulables a los daños; resolución por incumplimiento reiterado | Créditos de servicio como único remedio, con tope mensual; exclusiones (mantenimiento programado, causas del cliente, fuerza mayor) | `consulta="cláusula penal moderación artículo 1154 incumplimiento previsto por las partes"` y, si interesa una plaza, `consulta="penalizaciones por incumplimiento de niveles de servicio contrato de mantenimiento"`, `base="AN"`, `tipo_organo="AP"` |
| Honorarios e hitos | Pago tras aceptación; retención de una parte hasta el hito final; honorarios cerrados | Pagos anticipados o mensuales; interés y costes de cobro de la Ley 3/2004; suspensión del servicio por impago tras requerimiento | `consulta="Ley 3/2004 morosidad plazo de pago superior a sesenta días nulidad cláusula abusiva"` |
| Resultados | Cesión exclusiva de todos los derechos de explotación, con modalidades, plazo y territorio expresos, y entrega de fuentes | Licencia limitada o cesión solo tras el pago íntegro; reserva de herramientas y conocimientos previos | Solo arts. 43 y 45 TRLPI; deriva a `licencia-cesion-propiedad-intelectual` |
| Responsabilidad | Sin tope para dolo, culpa grave, confidencialidad, datos y derechos de terceros; seguro con capital mínimo | Tope por honorarios de un periodo, calculado sobre la cuota fija y las horas aceptadas por el cliente, nunca sobre lo que el prestador cuantifique por sí solo (art. 1256 CC); exclusión de lucro cesante y daños indirectos; plazo para reclamar | `consulta="arrendamiento de servicios cláusula de exoneración o limitación temporal o cuantitativa de la responsabilidad"` |
| Duración y desistimiento | Desistimiento del cliente con preaviso breve y sin indemnización | Plazo mínimo de permanencia o indemnización pactada por desistimiento; preaviso largo | `consulta="arrendamiento de servicios desistimiento unilateral contrato de duración determinada indemnización lucro cesante"` y `consulta="arrendamiento de servicios de duración indefinida desistimiento unilateral buena fe preaviso"` |
| Laboralidad (prestador persona física) | Autonomía real del prestador documentada; sin exclusividad salvo necesidad | Libertad de organización, medios propios, otros clientes | `consulta="relación laboral o arrendamiento de servicios notas de dependencia y ajenidad"`, `jurisdiccion="SOCIAL"`, `base="TS"`; TRADE: `consulta="trabajador autónomo económicamente dependiente extinción del contrato indemnización"`, `jurisdiccion="SOCIAL"` |
| Personal y subcontratación | Certificados del art. 42 ET, derecho a auditar, subcontratación solo con autorización | Libertad de sustituir a su personal y de subcontratar partes accesorias | `consulta="cesión ilegal de trabajadores contrata de servicios aportación de mano de obra"`, `jurisdiccion="SOCIAL"` |

Reglas para la nota:

- La limitación de responsabilidad, las penalizaciones, el desistimiento y el riesgo de laboralidad son cuestiones cuya validez o calificación discute la jurisprudencia (apartado 8 del formato): cita en la nota el párrafo literal con órgano, fecha y ECLI. Sin resolución aplicable tras dos reformulaciones, aplica la puerta.
- Si pactas no captación del personal de la otra parte, limítala en tiempo y alcance, justifícala por la relación y dilo en la nota como cláusula sin norma específica; cita doctrina solo si la encuentras.
- Una sentencia de la Sala de lo Social se cita para la calificación de la relación, nunca para interpretar las cláusulas civiles.

## Documentos que se entregan

Dos documentos Word maquetados según `references/formato-y-entrega-contratos.md`:

1. `contrato-prestacion-servicios-<parte-principal>-<AAAAMMDD>.docx`
2. `nota-prestacion-servicios-<parte-principal>-<AAAAMMDD>.docx`

Estructura del contrato:

1. REUNIDOS e INTERVIENEN; EXPONEN: actividad y medios propios del prestador, necesidad del cliente, que el prestador actúa con organización propia.
2. PRIMERA.- Definiciones y prelación de documentos (contrato, anexos, órdenes de cambio aceptadas).
3. SEGUNDA.- Objeto: servicios, entregables y exclusiones (Anexo I).
4. TERCERA.- Forma de prestación: organización y medios del prestador, interlocutores, obligaciones de colaboración del cliente.
5. CUARTA.- Niveles de servicio, medición, informes y penalizaciones o créditos (Anexo II).
6. QUINTA.- Honorarios, gastos, revisión, facturación y pago; intereses y costes de cobro por remisión a la Ley 3/2004, de 29 de diciembre (Anexo III).
7. SEXTA.- Aceptación de entregables.
8. SÉPTIMA.- Personal, cumplimiento laboral y de Seguridad Social, subcontratación.
9. OCTAVA.- Propiedad de los resultados y conocimientos previos.
10. NOVENA.- Confidencialidad y secretos empresariales.
11. DÉCIMA.- Protección de datos (Anexo IV, encargo de tratamiento, si procede).
12. UNDÉCIMA.- Responsabilidad, límite y seguros.
13. DUODÉCIMA.- Duración, prórroga, desistimiento con preaviso y resolución por incumplimiento.
14. DECIMOTERCERA.- Efectos de la terminación: devolución de información, transición y asistencia (Anexo V).
15. DECIMOCUARTA.- Fuerza mayor.
16. DECIMOQUINTA.- Cesión del contrato.
17. DECIMOSEXTA.- Notificaciones.
18. DECIMOSÉPTIMA.- Negociación previa, ley aplicable y fuero o arbitraje.
19. DECIMOCTAVA.- Integridad y modificaciones por escrito.
20. Cierre, firmas y ANEXOS: I Servicios y entregables; II Niveles de servicio; III Honorarios e hitos; IV Encargo de tratamiento; V Plan de transición.

**Reparto para la redacción rápida:** una sección por bloque de estipulaciones (`### [ESTIPULACION]`): comparecencia, expositivos, definiciones, objeto y forma de prestación / niveles de servicio, honorarios y aceptación de entregables / personal y subcontratación, resultados, confidencialidad, datos, responsabilidad y seguros / duración y desistimiento, efectos de la terminación, fuerza mayor, cesión, notificaciones, ley, fuero y firmas / anexos I a V. Si el prestador es persona física con indicios de dependencia y ajenidad (rama «Qué se entrega en esta rama»), no hay contrato ni equipo: la nota la redactas tú. La nota: apartado 11 del formato.

La nota sigue el apartado 3 del formato e incluye siempre un apartado «Calificación y riesgo de laboralidad» cuando el prestador sea persona física, con los hechos que lo sostienen o lo contradicen.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Detector pasado: no es obra, ni licencia principal, ni agencia, ni cliente consumidor; si lo era, se derivó.
- [ ] Prestador persona física: hechos del apartado 6 recogidos, comparados con los arts. 1 y 8 ET y 1 y 11 de la Ley 20/2007; si es TRADE o hay indicios de laboralidad, entregada solo la nota con la tabla de indicios y las dos opciones, sin contrato de servicios.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos citados del CC, de la Ley 3/2004 (`ley="BOE-A-2004-21830"`, título comprobado), del ET, de la Ley 20/2007, del TRLPI, de la Ley 1/2019, del RGPD y de la LOPDGDD.
- [ ] Plazo de pago no superior al máximo legal y aceptación no superior a treinta días; interés y costes de cobro no excluidos.
- [ ] Penalizaciones con su relación con la indemnización resuelta; limitación de responsabilidad sin exclusión del dolo.
- [ ] Cesión de resultados con derechos, modalidades, plazo y territorio expresos, o derivada a `licencia-cesion-propiedad-intelectual`; anexo de encargo si hay datos personales.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); el art. 28 del RGPD comprobado con `buscar_articulo` al margen del veredicto; cada «posible disonancia» contrastada con el apartado leído.
- [ ] Lo que no dio Jurisprudenciator y se obtuvo en internet, citado con enlace y fecha de consulta desde fuente oficial y señalado en el resumen; ninguna sentencia citada sin `buscar_por_cita` y `leer_sentencias`.
- [ ] Sociedades comprobadas con `buscar_empresa_mercantil`; firmantes con cargo o poder vigentes, o dicho en la nota.
- [ ] Marcadores en lugar de datos inventados; definiciones, importes, plazos y anexos coherentes.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas, riesgo de laboralidad, datos que faltan, tabla de jurisprudencia, plazos con su precepto (pago, preaviso, prescripción) y próximo paso.
