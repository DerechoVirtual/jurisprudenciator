---
name: prestamo-reconocimiento-deuda
description: >-
  Redacta contratos de préstamo de dinero (entre particulares o familiares, de socio a sociedad, de
  sociedad a socio, entre empresas) y reconocimientos de deuda con plan de pagos, con su nota para el
  abogado en Word. Úsala cuando el abogado diga «préstamo entre familiares», «préstamo privado»,
  «préstamo del socio a la empresa», «contrato de préstamo con intereses», «reconocimiento de deuda»,
  «plan de pagos», «aplazamiento de la deuda», «avalista» o «¿es usurario este interés?». Ajusta
  entrega, intereses, usura, amortización, vencimiento anticipado, fianza, forma y título ejecutivo
  según defienda al prestamista o al prestatario, y avisa de la normativa de consumo y de la
  fiscalidad que hay que comprobar. Si el préstamo lleva hipoteca sobre vivienda de una persona
  física, remite al notario; para reclamar una deuda ya impagada, usa reclamacion-deuda-monitorio.
---

# Préstamo y reconocimiento de deuda

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Préstamo, intereses, plazo, pagos y usura** → `buscar_articulo` (`ley="CC"`, artículos `"1740"`, `"1753"`, `"1754"`, `"1755"`, `"1756"`, `"1170"`, `"1100"`, `"1108"`, `"1109"`, `"1125"`, `"1127"`, `"1129"`, `"1172"`, `"1173"` y `"1174"`; `ley="CCom"`, artículos `"311"` a `"319"`, uno por uno) y (`ley="Ley de 23 de julio de 1908"`, artículos `"1"`, `"3"` y `"9"`).
- **Fianza y garantías personales** → `buscar_articulo` (`ley="CC"`, artículos `"1822"`, `"1827"`, `"1830"`, `"1831"`, `"1837"`, `"1838"`, `"1844"`, `"1847"` y `"1851"`; `ley="CCom"`, artículos `"439"` y `"440"`).
- **Reconocimiento de deuda, novación, forma, prescripción y título ejecutivo** → `buscar_articulo` (`ley="CC"`, artículos `"1203"`, `"1204"`, `"1207"`, `"1216"`, `"1218"`, `"1225"`, `"1227"`, `"1277"`, `"1935"`, `"1937"`, `"1964"`, `"1966"`, `"1967"`, `"1969"`, `"1973"` y `"1974"`; fiador y gananciales: `"1853"`, `"1365"` y `"1367"`; `ley="LEC"`, artículos `"517"`, `"572"`, `"573"` y `"812"`; `ley="LO 1/2025"`, `articulo="5"`) y, si la deuda nace de una operación comercial entre empresas, el interés de demora y los costes de cobro (`ley="BOE-A-2004-21830"`, artículos `"7"` y `"8"`).
- **Prestamista profesional, prestatario consumidor, garantía sobre vivienda, sociedades y efectivo** → `buscar_articulo` (`ley="BOE-A-2009-5391"`, artículos `"1"` a `"4"`; `ley="BOE-A-2011-10970"`, artículos `"1"` a `"4"`; `ley="BOE-A-2019-3814"`, artículos `"1"`, `"2"`, `"24"` y `"25"`; `ley="TRLGDCU"`, artículos `"3"`, `"85"` y `"86"`; `ley="LSC"`, artículos `"143"` y `"150"`; `ley="TRLC"`, artículos `"281"` y `"283"`; `ley="BOE-A-2012-13416"`, `articulo="7"`).
- **Fiscalidad que debe comprobarse** → `buscar_articulo` (`ley="BOE-A-1993-25359"`, artículos `"7"` y `"45"`; `ley="BOE-A-2006-20764"`, artículos `"6"` y `"40"`) y doctrina con `buscar_consultas_hacienda` (préstamo entre particulares, gratuidad, garantías) y, si hace falta, `buscar_doctrina_teac`.
- **Doctrina sobre usura, intereses de demora, vencimiento anticipado, fianza y reconocimiento de deuda** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; `base="AN"` + `tipo_organo="AP"` si no hay doctrina del Supremo o se litigará en esa plaza) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil` (existencia, estado, administradores, concurso; en préstamos socio-sociedad, cargos del socio).
- **Revisión de las citas** → `verificar_escrito`, que pasa cada redactor sobre las frases de su sección que citan normas (y tú sobre lo que redactes sin equipo), y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación; el ensamblado rechaza el ECLI que ningún redactor leyó.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Cita con fecha las leyes con número repetido: «Ley 2/2009, de 31 de marzo», «Ley 16/2011, de 24 de junio», «Ley 5/2019, de 15 de marzo», «Ley 7/2012, de 29 de octubre». `verificar_escrito` no identifica la Ley de 23 de julio de 1908 (con cualquier denominación la da por no localizada o atribuye su artículo al Código Civil o al de Comercio): comprueba sus artículos con `buscar_articulo` (`ley="Ley de 23 de julio de 1908"`), cítala como «artículo N de la Ley de 23 de julio de 1908, sobre nulidad de los contratos de préstamos usurarios» e ignora el veredicto del verificador sobre ella; explícalo en el resumen.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Préstamo de dinero entre particulares o familiares, de un socio a su sociedad, de una sociedad a un socio o administrador, o entre empresas.
- Reconocimiento de una deuda previa (precio impagado, préstamo verbal, facturas, liquidación entre socios) con plan de pagos, espera o quita.

Antes de redactar, pasa este detector:

| Situación | Qué hacer |
|---|---|
| El prestamista concede préstamos o créditos de forma profesional y el prestatario actúa como consumidor | Aplica la Ley 16/2011 (crédito al consumo, arts. 1 a 4) o la Ley 2/2009 (préstamos hipotecarios de empresas que no son entidades de crédito, art. 1), su carácter irrenunciable (art. 2 de la Ley 2/2009) y los arts. 85 y 86 TRLGDCU; si hay condiciones generales, usa también `condiciones-generales-consumidores` |
| Garantía hipotecaria o real sobre un inmueble de uso residencial, o préstamo para adquirir un inmueble, con prestatario, fiador o garante persona física y prestamista profesional (también el ocasional con finalidad exclusivamente inversora, art. 2.1 de la Ley 5/2019) | Rige la Ley 5/2019 (vencimiento anticipado y demora imperativos, arts. 24 y 25): no redactes la hipoteca; prepara solo las condiciones económicas y remite al notario |
| La sociedad presta a un tercero o a un socio para que adquiera participaciones o acciones de la propia sociedad o de su grupo | Prohibido (arts. 143.2 y 150 LSC): detén la tarea y explícalo |
| Deuda vencida sin acuerdo con el deudor | `requerimiento-cumplimiento` o `reclamacion-deuda-monitorio` |
| Se negocia con el deudor antes de demandar | `masc-propuesta-acuerdo` (y esta skill para el documento final del acuerdo) |
| Modificar un préstamo existente, cambiar de deudor o de acreedor | `modificacion-novacion-cesion` |
| Revisar un préstamo que ha redactado la otra parte | `revision-contrato-semaforo` |

## Datos que hay que reunir antes de redactar

Comprueba estos datos con la documentación que aporte el abogado antes de redactar. Pregunta solo los marcados con ★ que falten y no se deduzcan de lo aportado, todos en una única ronda de como máximo cuatro preguntas; lo demás que falte se redacta con el marcador del apartado 7 del formato y se lista en la entrega.

1. ★ A quién defiende el abogado: prestamista o acreedor, prestatario o deudor, o fiador.
2. ★ Partes: identificación; si son personas físicas casadas, régimen económico matrimonial (pregunta si el cónyuge debe intervenir: lee los arts. 1365 y 1367 CC, que deciden si responden los bienes gananciales); si son sociedades, cargo del firmante y relación entre ellas (socio con qué porcentaje, administrador, grupo).
3. ★ Condición del prestamista (presta habitualmente o como negocio, o de forma aislada) y del prestatario (consumidor o empresario), y finalidad del préstamo.
4. ★ Importe, moneda, fecha y forma de entrega (transferencia a una cuenta identificada; si ya se entregó, justificante).
5. ★ Interés remuneratorio (gratuito, fijo o variable con índice oficial), interés de demora y comisiones o gastos.
6. ★ Plazo y amortización: cuotas, fechas, carencia, amortización anticipada (y si tiene compensación).
7. ★ Garantías: fiadores (solidarios o no, con qué límite), pagarés, prenda; si se pide hipoteca, aplica el detector.
8. ★ En el reconocimiento de deuda: origen de la deuda y documentos que la acreditan, desglose (principal, intereses, gastos), pagos ya hechos, si hay fiadores o garantías de la deuda original, y si se concede espera o quita (y si esta queda condicionada al cumplimiento del plan).
9. Forma: documento privado, póliza intervenida o escritura pública, según si se quiere ejecución directa.
10. Si puede aplicarse un Derecho civil propio (por ejemplo, Navarra o Cataluña): pregunta y, si aplica, busca la norma con `buscar_boe`; si no aparece, aplica la puerta.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota su línea de vigencia.

**Préstamo civil.** Se entrega dinero con obligación de devolver otro tanto (art. 1740 CC); el prestatario adquiere su propiedad (art. 1753) y la deuda se paga en la especie pactada (arts. 1754 y 1170). No hay intereses sin pacto expreso (art. 1755) y los pagados sin pacto no se reclaman ni se imputan al capital (art. 1756). El contrato debe dejar constancia de la entrega: sin ella solo hay promesa de préstamo, así que redacta la cláusula de entrega con referencia a la transferencia y su fecha.

**Préstamo mercantil.** Es mercantil si concurren las dos circunstancias del art. 311 CCom. Consecuencias: sin plazo, solo es exigible treinta días después del requerimiento notarial (art. 313); los intereses solo se deben si se pactan por escrito (art. 314); el art. 315 permite pactar interés «sin tasa ni limitación», pero la Ley de 1908 alcanza a toda operación equivalente a un préstamo (su art. 9): busca doctrina antes de sostener lo contrario; demora desde el día siguiente al vencimiento (art. 316); los intereses vencidos no devengan intereses salvo capitalización pactada (art. 317); el recibo del capital sin reserva extingue los intereses y las entregas se imputan primero a intereses (art. 318).

**Intereses y mora.** Mora desde la intimación salvo pacto o ley (art. 1100 CC): pacta la mora automática al vencimiento de cada cuota. Demora: la pactada o, en su defecto, el interés legal (art. 1108 CC); si la deuda viene de una operación comercial entre empresas, el tipo legal de la Ley 3/2004 (art. 7, publicado cada semestre) y la indemnización por costes de cobro (art. 8); los intereses vencidos devengan el legal desde su reclamación judicial (art. 1109 CC). No escribas el interés legal del dinero de memoria: se fija cada año por ley; búscalo en internet en el BOE (norma que lo fija para ese año) o en el Banco de España y cítalo con enlace y fecha de consulta, o deja en el contrato la remisión al interés legal.

**Usura (Ley de 23 de julio de 1908).** Es nulo el préstamo con interés notablemente superior al normal del dinero y manifiestamente desproporcionado con las circunstancias, o en condiciones leoninas aceptadas por situación angustiosa, inexperiencia o limitación mental, y siempre el que supone recibida mayor cantidad que la entregada (art. 1); el prestatario solo devuelve lo recibido (art. 3); alcanza a toda operación sustancialmente equivalente a un préstamo (art. 9). Para préstamos entre particulares o de prestamistas que no son entidades de crédito, la Sala Primera compara con operaciones homogéneas de ese mercado y no con las estadísticas de las entidades de crédito: lee la doctrina y obtén el dato de referencia en internet, en la fuente oficial que indique la sentencia (estadísticas oficiales del Banco de España o del ministerio competente), y cítalo con enlace y fecha de consulta; no escribas porcentajes de memoria. Nunca recojas en el documento una cantidad entregada distinta de la real.

**Plazo, vencimiento anticipado y pagos.** El plazo se presume a favor de ambas partes (art. 1127 CC): la amortización anticipada necesita pacto. El deudor pierde el plazo si resulta insolvente o no da o disminuye las garantías (art. 1129 CC). El vencimiento anticipado por impago es pactable entre particulares y empresas, pero debe responder a un incumplimiento relevante: fija número de cuotas o importe y requerimiento previo con plazo; en préstamos con consumidores o sobre vivienda, busca y aplica la doctrina de abusividad y, si rige la Ley 5/2019, su art. 24 sin pacto en contrario. Imputación de pagos: arts. 1172 a 1174 CC y art. 318 CCom; pacta el orden (gastos, intereses de demora, ordinarios, capital).

**Fianza.** No se presume y no se extiende a más de lo pactado; la indefinida comprende los accesorios (art. 1827 CC). El fiador tiene beneficio de excusión salvo renuncia expresa, obligación solidaria o concurso del deudor (arts. 1830 y 1831) y, si son varios, de división salvo solidaridad pactada (art. 1837); el que paga se reembolsa (art. 1838) y reclama a los cofiadores (art. 1844). La prórroga concedida al deudor sin consentimiento del fiador extingue la fianza (art. 1851): todo plan de pagos o espera sobre una deuda afianzada debe firmarlo el fiador. En préstamo mercantil, la fianza debe constar por escrito (arts. 439 y 440 CCom). Si el prestamista es profesional y el fiador consumidor, busca la doctrina sobre transparencia y desproporción de las fianzas.

**Reconocimiento de deuda.** Aunque no se exprese la causa, se presume que existe y es lícita mientras el deudor no pruebe lo contrario (art. 1277 CC); la Sala Primera le atribuye el efecto de dispensar al acreedor de probar la relación anterior. Aun así, identifica la causa (origen, documentos, liquidación), porque su falsedad o inexistencia es la defensa típica del deudor. Decide y di expresamente si hay novación extintiva: solo existe si se declara terminantemente o las obligaciones son incompatibles (art. 1204 CC), y extinguida la obligación original solo subsisten las garantías accesorias que aprovechen a terceros que no consintieron (art. 1207 CC). Si defiendes al acreedor, declara que el reconocimiento no nova la deuda original y que sus garantías subsisten; si hay quita, condiciónala al cumplimiento íntegro del plan. El reconocimiento interrumpe la prescripción (art. 1973 CC); los plazos corren desde que la acción pudo ejercitarse (art. 1969), son de cinco años para las acciones personales sin plazo especial (art. 1964.2) y para los pagos por años o plazos más breves (art. 1966.3), y la interrupción frente a un deudor solidario alcanza a los demás (art. 1974). **Antes de dar un plazo, comprueba si hay uno especial**: el precio de géneros vendidos por un comerciante a quien no lo es o se dedica a distinto tráfico (una empresa que compra para su propio uso, no para revender) prescribe a los tres años (art. 1967, regla 4.ª); busca la doctrina actual (`consulta="prescripción tres años artículo 1967.4 distinto tráfico uso empresarial"`). Calcula el plazo de cada factura o partida por separado: si alguna ya había prescrito cuando se reclamó, el reconocimiento no la resucita por sí solo; para incluirla hace falta una renuncia expresa a la prescripción ganada (art. 1935) del deudor **y del fiador**, porque el fiador puede oponer las excepciones inherentes a la deuda (art. 1853) y cualquier interesado puede hacer valer la prescripción pese a la renuncia del deudor (art. 1937). Dilo en la nota con las fechas.

**Forma y ejecución.** El documento privado firmado por el deudor permite el monitorio (art. 812 LEC), que exige intentar antes un medio adecuado de solución de controversias; la demanda ejecutiva no lo exige (art. 5.3 de la Ley Orgánica 1/2025). Solo la escritura pública o la póliza intervenida llevan aparejada ejecución (art. 517.2.4.º y 5.º LEC), y la ejecución por saldo exige pactar la liquidación en el título y notificarla antes al deudor y al fiador (arts. 572.2 y 573). El documento público prueba su fecha frente a terceros (art. 1218 CC); la fecha del privado no, salvo los supuestos del art. 1227. Si el abogado necesita el coste notarial, búscalo en internet en el arancel publicado en el BOE y cítalo con enlace y fecha de consulta; no lo estimes.

**Sociedades.** Si el prestamista es socio con la participación que fija el art. 283.1 TRLC, administrador o sociedad del grupo, su crédito será subordinado si la prestataria entra en concurso (art. 281.1.5.º TRLC; la excepción del art. 281.2.3.º no alcanza a los préstamos): dilo en la nota y valora garantías o capitalización. Comprueba siempre la prohibición de asistencia financiera (arts. 143.2 y 150 LSC).

**Pagos en efectivo.** Si alguna parte actúa como empresario o profesional, comprueba el límite del art. 7 de la Ley 7/2012, de 29 de octubre; en todo caso, pacta entrega y pagos por transferencia para poder probarlos.

**Fiscalidad (avisar, no calcular).** Los préstamos están sujetos a la modalidad de transmisiones patrimoniales onerosas (art. 7.1.B del Real Decreto Legislativo 1/1993) y el art. 45 recoge su exención (apartado I.B.15); las garantías y la forma pública pueden tener otro tratamiento. En el IRPF se presumen retribuidas las prestaciones que generan rendimientos del capital (art. 6.5 de la Ley 35/2006) y se valoran al interés legal del dinero (art. 40.2): si el préstamo es gratuito, documéntalo y avisa del riesgo. Una quita puede tener consecuencias fiscales. Lee esos artículos, consulta `buscar_consultas_hacienda` sobre el caso (préstamo entre particulares, modelo de declaración, gratuidad, condonación) y no des tipos ni importes.

## Cláusulas clave y jurisprudencia

Consultas con `jurisdiccion="CIVIL"` y `base="TS"` salvo indicación; lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar.

| Cláusula | Si defiendes al prestamista o acreedor | Si defiendes al prestatario, deudor o fiador | Qué buscar |
|---|---|---|---|
| Entrega del capital | Transferencia identificada y carta de pago en el propio contrato o documento posterior | Entrega efectiva antes de que nazca cualquier obligación; nada de «recibido» anticipado | Arts. 1740 y 1753 CC |
| Interés remuneratorio | Tipo pactado por escrito, justificado por el riesgo y comparado con el mercado homogéneo | Interés dentro del mercado de referencia; si no, nulidad por usura | `consulta="usura interés notablemente superior al normal del dinero préstamo entre particulares"`; `consulta="usura préstamo empresa sujeta a la Ley 2/2009 canon de comparación"`; `consulta="préstamo usurario se supone recibida mayor cantidad que la entregada"` |
| Interés de demora | Pactado sobre el importe vencido, mora automática | Moderado y solo sobre lo vencido; con consumidor, criterio de la Sala Primera | `consulta="intereses moratorios préstamo personal consumidores abusividad dos puntos porcentuales"`, `fecha_hasta="31/12/2018"` (y la misma sin fecha para doctrina posterior) |
| Vencimiento anticipado | Por impago de un número de cuotas, concurso, falsedad o pérdida de garantías, con requerimiento previo | Umbral relevante, requerimiento con plazo para ponerse al día | `consulta="vencimiento anticipado préstamo entre particulares cláusula resolutoria impago cuotas"` |
| Fianza | Fianza solidaria con renuncia expresa a excusión y división; consentimiento anticipado a prórrogas | Fianza simple, limitada en importe y tiempo; sin extensión a prórrogas no consentidas | `consulta="fianza solidaria renuncia a los beneficios de excusión orden y división"`; `consulta="prórroga concedida al deudor sin consentimiento del fiador extingue la fianza artículo 1851"` |
| Reconocimiento de deuda | Causa identificada, no novación, subsistencia de garantías, quita condicionada, vencimiento de todo el plan por impago | Liquidación detallada y documentos; reserva de excepciones sobre partidas discutidas; quita firme | `consulta="reconocimiento de deuda efectos dispensa de prueba de la relación obligatoria preexistente"`; `consulta="reconocimiento de deuda interrupción de la prescripción"` |
| Forma y título | Escritura o póliza con pacto de liquidación (arts. 517 y 572 LEC) | Documento privado; notificación previa de la liquidación | `consulta="póliza intervenida título ejecutivo préstamo liquidación saldo notificación previa"` |
| Préstamo de socio | Garantías y advertencia de subordinación concursal | — | `consulta="préstamo de socio a la sociedad concursada crédito subordinado persona especialmente relacionada"` |

Reglas para la nota:

- La usura, el vencimiento anticipado y el interés de demora con consumidores están en el apartado 8 del formato: cita en la nota el párrafo literal de la resolución leída, con órgano, fecha y ECLI; si tras dos reformulaciones no hay resolución aplicable, aplica la puerta.
- Distingue en la nota la doctrina dictada para préstamos con consumidores o sobre vivienda de la que se aplica entre particulares o empresas: no traslades la primera sin decirlo.
- Si la usura se analiza para un préstamo concreto, indica qué término de comparación usa la sentencia leída y el dato oficial obtenido, con su enlace y fecha de consulta.

## Documentos que se entregan

Dos documentos Word maquetados según `references/formato-y-entrega-contratos.md`:

1. `contrato-prestamo-<parte-principal>-<AAAAMMDD>.docx` o `reconocimiento-deuda-<deudor>-<AAAAMMDD>.docx`.
2. `nota-prestamo-<parte-principal>-<AAAAMMDD>.docx` o `nota-reconocimiento-deuda-<deudor>-<AAAAMMDD>.docx`.

Estructura del contrato de préstamo:

1. REUNIDOS e INTERVIENEN (con la relación entre las partes si son socio y sociedad); EXPONEN: finalidad, condición de las partes y, si se trata de prestamista no profesional, que presta de forma aislada.
2. PRIMERA.- Objeto e importe; entrega por transferencia y carta de pago.
3. SEGUNDA.- Intereses remuneratorios (o gratuidad expresa).
4. TERCERA.- Plazo, calendario de amortización (cuadro en anexo) y amortización anticipada.
5. CUARTA.- Pagos: cuenta, imputación, gastos.
6. QUINTA.- Mora e interés de demora.
7. SEXTA.- Vencimiento anticipado y requerimiento previo.
8. SÉPTIMA.- Garantías: fianza (con su régimen de excusión, división y prórrogas) u otras.
9. OCTAVA.- Liquidación de la deuda y certificación del saldo (si se va a formalizar en póliza o escritura).
10. NOVENA.- Gastos e impuestos a cargo de cada parte.
11. DÉCIMA.- Notificaciones.
12. UNDÉCIMA.- Ley aplicable y fuero (sin sumisión si el prestatario es consumidor, art. 54.2 LEC).
13. Cierre, firmas (y del fiador) y ANEXOS: cuadro de amortización, justificante de la transferencia.

Estructura del reconocimiento de deuda: comparecencia; EXPONEN (origen de la deuda y documentos); PRIMERA.- Reconocimiento del importe con desglose; SEGUNDA.- Carácter no novatorio (o novatorio, si se pacta) y subsistencia de garantías; TERCERA.- Plan de pagos; CUARTA.- Quita condicionada, si la hay; QUINTA.- Intereses; SEXTA.- Vencimiento anticipado; SÉPTIMA.- Consentimiento del fiador a la espera; OCTAVA.- Efecto interruptivo de la prescripción; NOVENA.- Gastos, notificaciones y fuero; firmas.

**Reparto para la redacción rápida:** contratos cortos, una sección por bloque de estipulaciones (`### [ESTIPULACION]`). Préstamo: comparecencia, expositivos, objeto, entrega, intereses y plazo / pagos, mora, vencimiento anticipado, garantías y liquidación / gastos, notificaciones, ley, fuero, firmas y anexos. Reconocimiento de deuda: comparecencia y expositivos (origen y documentos) / reconocimiento con desglose, carácter no novatorio, plan de pagos, quita e intereses / vencimiento anticipado, consentimiento del fiador, efecto interruptivo, gastos, fuero y firmas. La nota: apartado 11 del formato.

La nota sigue el apartado 3 del formato e incluye siempre: régimen aplicable (civil o mercantil, consumo o no, Ley 5/2019 o no), análisis de usura con el término de comparación, valor probatorio y ejecutivo del documento elegido, riesgos concursales si hay socios y fiscalidad que debe comprobarse.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Detector pasado: prestamista profesional con consumidor, garantía sobre vivienda, asistencia financiera prohibida; si encajaba alguno, se aplicó o se detuvo la tarea.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos citados del CC, del CCom, de la Ley de 1908, de la LEC, y los de las Leyes 2/2009, 16/2011, 5/2019, 7/2012, la LSC, el TRLC, el TRLGDCU y las normas fiscales que se mencionen (título de cada respuesta comprobado).
- [ ] Entrega del capital acreditada; ninguna cantidad reconocida distinta de la entregada.
- [ ] Interés remuneratorio contrastado con la doctrina de usura y con el dato de referencia de la fuente oficial (internet, con enlace y fecha); interés de demora solo sobre lo vencido.
- [ ] Lo que no dio Jurisprudenciator y se obtuvo en internet, citado con enlace y fecha de consulta desde fuente oficial y señalado en el resumen; ninguna sentencia citada sin `buscar_por_cita` y `leer_sentencias`.
- [ ] Vencimiento anticipado con umbral y requerimiento; en préstamos sobre vivienda de persona física, sin contradecir el art. 24 de la Ley 5/2019.
- [ ] Fiador firmante de cualquier espera o plan de pagos (art. 1851 CC); renuncias a excusión y división expresas si se pactan.
- [ ] Reconocimiento con causa identificada, decisión expresa sobre la novación y quita condicionada, si la hay.
- [ ] Forma elegida coherente con la ejecución que se quiere (monitorio o ejecución directa) y pacto de liquidación si hay saldo.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (y por ti sobre lo que redactes sin equipo); la Ley de 1908 comprobada con `buscar_articulo` al margen del veredicto; cada «posible disonancia» contrastada con el apartado leído.
- [ ] Sociedades comprobadas con `buscar_empresa_mercantil`.
- [ ] Marcadores (`[IMPORTE]`, `[IBAN]`, `[FECHA DE ENTREGA]`, `[TIPO DE INTERÉS]`…) en lugar de datos inventados; cuadro de amortización cuadrado con importe, tipo y plazo.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas, datos y documentos que faltan, tabla de jurisprudencia, plazos con su precepto (vencimientos, prescripción desde cada cuota, art. 313 CCom si no hay plazo) y próximo paso, incluida la fiscalidad que debe comprobar.
