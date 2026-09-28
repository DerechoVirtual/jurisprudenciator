---
name: finiquito-liquidacion
description: >-
  Liquidación de haberes y finiquito, para las dos partes. Para la empresa: calcula el salario pendiente,
  las vacaciones devengadas y no disfrutadas (art. 38 ET), las pagas extraordinarias no prorrateadas y
  los demás devengos del convenio, aplica el descuento por falta de preaviso solo si el convenio lo
  prevé, y redacta la propuesta de liquidación y el recibo de finiquito con cláusula de saldo, espacio
  para «no conforme» y la presencia del representante (art. 49.2 ET). Para el trabajador: revisa un
  finiquito recibido concepto a concepto, valora su valor liberatorio según la jurisprudencia y dice qué
  reclamar y hasta cuándo. Úsala con «haz el finiquito», «liquidación», «¿firmo el finiquito?» o «me han
  pagado mal el finiquito». La indemnización se calcula en calculo-indemnizacion-despido.
---

# Finiquito y liquidación de haberes

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Conceptos, pago y documento de liquidación** → `buscar_articulo` (`ley="ET"`, artículos `"26"`, `"29"`, `"31"`, `"38"`, `"49"` y `"64"`) y, para la compensación de las vacaciones al extinguirse el contrato, (`ley="Directiva 2003/88/CE"`, `articulo="7"`).
- **Preavisos y consecuencias de no darlos** → `buscar_articulo` (`ley="ET"`, artículos `"49"`, `"53"` y `"58"`, este por la prohibición de la multa de haber) y (`ley="Real Decreto 2720/1998"`, `articulo="8"`), comprobando en la cabecera el título y la vigencia.
- **Convenio: vacaciones, pagas, preaviso y otros devengos** → `buscar_convenio` + `leer_convenio` (`buscar_en="vacaciones"`, `"gratificaciones extraordinarias"` o `"pagas extraordinarias"`, `"preaviso"`, `"finiquito"` o `"liquidación"` e `"indemnización"`; en contratos temporales, además `"circunstancias de la producción"` o `"duración determinada"`, porque muchos convenios fijan una indemnización o un plus propios al terminar) + `vigencia_convenio`. Cuando la búsqueda por materia devuelva un fragmento cortado, pide el artículo completo con `articulo="N"`.
- **Valor liberatorio y retribución de las vacaciones** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión), con las consultas de «Estrategia y jurisprudencia».
- **Plazos y cauce para reclamar** → `buscar_articulo` (`ley="ET"`, artículos `"3"`, `"33"` y `"59"`) y (`ley="LRJS"`, artículos `"26"`, `"65"` y `"103"`). El calendario de fiestas de la sede (boletín de la comunidad autónoma y fiestas locales del municipio) no lo da el conector: búscalo en internet y cítalo con su enlace.
- **Empresa** → `buscar_empresa_mercantil` (denominación exacta para el documento; disolución o concurso para el FOGASA).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...). Lo que Jurisprudenciator no tenga se cita de la fuente oficial de internet, con su enlace y la fecha de consulta, como dice el punto 3 de la puerta.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Pregunta primero **a quién defiende el despacho**:

- **Empresa**: termina un contrato (dimisión, fin de temporal, despido, objetivo, mutuo acuerdo, fin de campaña de un fijo discontinuo) y hay que liquidar y documentar. Quiere un finiquito correcto, pagado a tiempo y que cierre lo que liquida.
- **Trabajador**: le han entregado una propuesta de liquidación o un finiquito, firmado o sin firmar. Quiere saber si está bien calculado, si puede firmarlo y qué le queda por reclamar.

| Si además hay que… | Skill |
|---|---|
| Calcular la indemnización por la extinción | `calculo-indemnizacion-despido` (su cifra entra aquí como línea separada) |
| Impugnar el despido que acompaña al finiquito | `laboral-empresa-intake` para el plazo; después `papeleta-conciliacion` y `redactar-demanda-despido` |
| Demandar las cantidades | `reclamacion-cantidad`; horas extraordinarias: `registro-jornada-horas-extra` |
| Saber qué convenio rige | `convenio-aplicable` |

## Datos que hay que reunir antes de redactar

Si falta un dato imprescindible (★), pídelo; si no se puede obtener, deja el concepto con su marcador y fuera del total.

**Para liquidar (empresa):**

1. ★ Causa y fecha de la extinción, y fecha en que se comunicó (la propuesta de liquidación acompaña a esa comunicación).
2. ★ Nómina ordinaria: conceptos e importes; si las pagas extraordinarias están prorrateadas; hasta qué día está pagado el salario.
3. ★ Vacaciones: días anuales (convenio o contrato; naturales o laborables), periodo de devengo que fije el convenio, días disfrutados en ese periodo y días pendientes de años anteriores con su causa (incapacidad temporal, suspensión por nacimiento).
4. ★ Pagas extraordinarias: número, importe y periodo de devengo de cada una según el convenio; cuáles se han cobrado ya.
5. ★ Preaviso: días exigidos (convenio o contrato), fecha del aviso y días realmente cumplidos, por quién.
6. Otros devengos: comisiones por negocios ya realizados y pagados, horas extraordinarias, pluses, dietas y gastos pendientes, anticipos, préstamos, embargos.
7. Indemnización, si procede (de `calculo-indemnizacion-despido`).
8. Representación legal en la empresa y forma y fecha de pago.

**Para revisar (trabajador):** el documento recibido completo, si lo ha firmado y con qué mención, en presencia de quién, qué ha cobrado y cuándo, la carta de extinción, contrato, nóminas del último año y convenio.

## Régimen jurídico y comprobaciones

Lee cada precepto con `buscar_articulo` y cada artículo del convenio con `leer_convenio` en esta conversación.

### 1. Conceptos de la liquidación

| Concepto | Cálculo | De dónde sale |
|---|---|---|
| Salario pendiente | días no pagados del último periodo × salario diario, con el divisor que use la nómina (mes de 30 días o días naturales del mes): decláralo | nóminas; art. 29.1 ET |
| Vacaciones devengadas y no disfrutadas | (días de vacaciones del año × días de servicio en el periodo de devengo ÷ días del periodo) − días disfrutados = días pendientes; × valor de un día de vacaciones | art. 38 ET y convenio; doctrina sobre su retribución |
| Pagas extraordinarias no prorrateadas | importe de cada paga × días devengados en su periodo ÷ días del periodo − lo ya cobrado | art. 31 ET y convenio (periodo de devengo) |
| Otros devengos salariales | comisiones de negocios realizados y pagados, horas extraordinarias, pluses devengados | art. 29.2 ET; convenio; registro de jornada |
| Conceptos no salariales | dietas y suplidos pendientes, en línea aparte | art. 26.2 ET |
| Indemnización | cifra de `calculo-indemnizacion-despido`, en línea aparte con su precepto | ET según la causa |
| Descuentos | anticipos (art. 29.1 ET), préstamos documentados, embargos con orden, falta de preaviso solo si el convenio o el contrato lo prevén | documento de cada uno; artículo del convenio |

- **Vacaciones**: el periodo es de treinta días naturales como mínimo y no puede sustituirse por dinero (art. 38.1 ET); la compensación solo cabe al concluir la relación laboral (art. 7.2 de la Directiva 2003/88/CE, leído con `buscar_articulo`; `verificar_escrito` no reconoce las directivas) y la doctrina de la Sala Cuarta la aplica: léela y cítala en la nota si se discute. Si el convenio cuenta las vacaciones en días laborables, calcula en laborables y dilo. Las pendientes por incapacidad temporal o por las suspensiones del art. 38.3 ET: aplica ese apartado (el plazo de dieciocho meses rige para la incapacidad temporal por contingencias distintas del embarazo, el parto o la lactancia natural) y la doctrina sobre su compensación al extinguirse el contrato.
- **Valor del día de vacaciones**: la retribución ordinaria o media, que incluye los complementos habituales del trabajador y excluye los ocasionales y los gastos: busca la doctrina y di en la hoja qué conceptos entran y por qué. Si el convenio fija cómo se retribuyen las vacaciones (media de un periodo, conceptos excluidos), aplica su regla y contrástala con esa doctrina: no puede dejar fuera conceptos salariales habituales. El valor del día no lleva la parte de las pagas, que se liquidan en su propia línea.
- **Pagas**: el convenio fija la cuantía y la fecha de la segunda paga (art. 31 ET); si no fija el periodo de devengo, pregúntaselo al abogado y marca el criterio como no contrastado. Si las devenga «por anualidades», las dos se ganan a lo largo del año natural: lo pendiente es lo devengado por ambas en el año menos lo ya cobrado (la paga de verano se cobra por adelantado). Si las devenga por semestres, cada una va con su semestre.
- **Vacaciones disfrutadas de más**: no descuentes el exceso sin una previsión expresa del convenio o del contrato; si la empresa quiere hacerlo, márcalo como riesgo en la nota.
- **Retenciones y cotizaciones**: las practica la nómina de liquidación (apartado 7 del formato); el documento muestra el bruto y remite a esa nómina.
- **Pago tardío**: interés por mora del diez por ciento de lo adeudado (art. 29.3 ET).

### 2. Preaviso

- **Dimisión**: el trabajador debe dar el preaviso que señalen los convenios o la costumbre del lugar (art. 49.1.d) ET). Lee en el convenio el plazo y la consecuencia de incumplirlo (`buscar_en="preaviso"`); aplica el descuento **solo** en los términos de ese artículo y cítalo con su número y código. Declara con qué salario de un día descuentas (el ordinario, sin la parte de pagas si estas se liquidan aparte). Sin previsión en el convenio ni en el contrato no hay descuento: detraer días de salario por decisión propia es una multa de haber (art. 58.3 ET).
- **Preaviso del contrato frente al del convenio**: la Sala Cuarta solo admite el preaviso pactado en el contrato **en defecto de regulación en el convenio**. Si el convenio lo regula, sus reglas son mínimas y solo pueden mejorarse a favor del trabajador: un plazo contractual más largo para la dimisión no se aplica en lo que exceda del convenio. Lee la doctrina (consulta abajo) antes de descontar por un plazo del contrato.
- **Cláusulas que quitan lo ya devengado**: si el convenio o el contrato añaden, por no preavisar, la pérdida de pagas, vacaciones u otros conceptos ya ganados, no la apliques sin advertir por escrito del riesgo: privar de salario devengado como castigo encaja en la multa de haber prohibida por el art. 58.3 ET, también cuando la prevé un convenio (consulta abajo). Muestra en la hoja la cifra con y sin esa pérdida.
- **Fin de contrato temporal de más de un año**: la parte que denuncia avisa con quince días (art. 49.1.c) ET); si la empresa no lo cumple, el art. 8.3 del Real Decreto 2720/1998 fija una indemnización equivalente al salario de los días incumplidos: léelo y comprueba su cabecera de vigencia antes de aplicarlo.
- **Despido objetivo**: quince días de preaviso o sus salarios (art. 53.1.c) ET y art. 53.4 ET, último párrafo).

### 3. Propuesta, firma y representación

- La empresa acompaña a la comunicación de la denuncia o del preaviso **una propuesta del documento de liquidación** (art. 49.2 ET, primer párrafo). Entrega la propuesta con la carta, no el día del pago.
- El trabajador puede pedir que un representante legal esté presente al firmar el recibo del finiquito; el recibo hace constar si firmó en su presencia o si no usó esa posibilidad, y el trabajador puede dejar constancia de que la empresa lo impidió (art. 49.2 ET, segundo párrafo).
- **El art. 49.2 ET regula la presencia del representante, no una copia del finiquito.** Lo que el ET exige respecto de la representación es: que conozca los modelos de los documentos de terminación de la relación (art. 64.4.b) ET), que reciba la notificación de las denuncias de los contratos en los diez días siguientes (art. 64.4 ET, último párrafo) y, en el despido objetivo del art. 52.c), copia del escrito de preaviso (art. 53.1.c) ET). Lee además si el convenio exige algo más (`buscar_en="finiquito"`).
- Fijos discontinuos: la liquidación al terminar cada periodo de actividad sigue los trámites y garantías del art. 49.2 ET (art. 29.1 ET, último párrafo).
- Si el trabajador se niega a firmar: dos testigos dejan constancia de la entrega y de la negativa, y la empresa paga por transferencia con el concepto detallado.

### 4. Valor liberatorio: lo que la jurisprudencia exige

Lee la doctrina antes de redactar o de aconsejar (consultas abajo). Las líneas que debes contrastar en el caso:

- El finiquito libera cuando expresa una voluntad clara e inequívoca de extinguir la relación y saldar las cuentas, y alcanza a los conceptos que liquida.
- La Sala Cuarta le ha negado ese efecto, entre otros supuestos, cuando contiene una renuncia genérica de futuro, cuando la liquidación es inferior a lo que legalmente correspondía, cuando se firma al término de cada contrato temporal encadenado, cuando no expresa el efecto extintivo y respecto de conceptos que no figuran en él.
- Un finiquito que no menciona el despido ni contiene una transacción sobre él no impide impugnar el despido.
- Los derechos de derecho necesario y los declarados indisponibles por convenio no se pueden renunciar (art. 3.5 ET).

## Estrategia y jurisprudencia

**Si defiendes a la empresa**: liquida cada concepto con su cálculo, paga todo lo debido y redacta la cláusula de saldo sobre los conceptos liquidados, sin renuncias genéricas de futuro ni a derechos indisponibles: una renuncia de más no añade protección y puede restársela al documento. Si se quiere cerrar también la discusión sobre el despido, no lo metas en el finiquito: la vía es la conciliación ante el servicio administrativo (y allí juega además la fiscalidad de la indemnización, que calcula `calculo-indemnizacion-despido`).

**Si defiendes al trabajador**:

1. Si hay despido, el plazo de veinte días hábiles corre igual (art. 103.1 LRJS): calcula la fecha en la nota antes que nada, sin sábados, domingos ni festivos de la sede (calendario de fiestas buscado en internet).
2. Si no está conforme, que firme como recibí con la mención «no conforme» (y, si quiere, pida la presencia del representante del art. 49.2 ET); busca la doctrina sobre el efecto de esa mención y cítala en la nota.
3. Compara concepto a concepto lo pagado con lo debido y cuantifica la diferencia.
4. Reclamación: un año de prescripción desde que la acción pudo ejercitarse (art. 59.2 ET), interrumpida por la papeleta (art. 65.1 LRJS); puede acumularse a la demanda de despido la reclamación de cantidades en los términos del art. 26.3 LRJS; interés por mora del art. 29.3 ET; si la empresa es insolvente, FOGASA con los límites del art. 33 ET.

**Consultas** (reformula como máximo dos veces):

- `consulta="finiquito valor liberatorio voluntad inequívoca extinguir relación laboral"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- `consulta="finiquito firmado no conforme reserva de acciones carece de valor liberatorio"`, `base="AN"`, `jurisdiccion="SOCIAL"`, `tipo_organo="TSJ"` y `provincia` con la sede de la Sala del territorio.
- `consulta="compensación económica vacaciones no disfrutadas extinción contrato incapacidad temporal"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- `consulta="retribución de las vacaciones retribución ordinaria complementos variables promedio"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- `consulta="falta de preaviso dimisión descuento liquidación convenio"`, `base="TS"`, `jurisdiccion="SOCIAL"` (la del preaviso superior pactado en contrato aparece como «establecimiento de preaviso superior al que fija el Convenio Colectivo»); y en el TSJ del territorio, `consulta="descuento falta de preaviso dimisión finiquito convenio colectivo"`.
- Pérdida de conceptos devengados como castigo: `consulta="multa de haber sanción encubierta artículo 58.3 nulidad cláusula"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
- Finiquito preparado por la empresa y entregado con la carta de despido: `consulta="finiquito puesto a la firma al tiempo que se entrega la carta de despido valor liberatorio"`, `base="TS"`, `jurisdiccion="SOCIAL"`.

La jurisprudencia es **imprescindible** (apartado 8 del formato) en la revisión del trabajador y siempre que se discuta el valor liberatorio, el valor del día de vacaciones o el descuento por preaviso. Sobre la mención «no conforme» no siempre hay una resolución específica en la base: si tras dos reformulaciones y la búsqueda en internet no aparece, apóyate en la doctrina general del valor liberatorio (su alcance depende de la declaración de voluntad del trabajador), dilo en el resumen y no atribuyas a ninguna sentencia lo que no dice. En el documento de la empresa no va jurisprudencia (el recibo es un documento al trabajador); va en la nota. Lee con `leer_sentencias` solo lo que vayas a citar, transcribe fundamentos y no hechos ni datos de aquel pleito, y comprueba que el párrafo es razonamiento de la Sala.

## Documentos que se entregan

Según `references/formato-y-organos-laboral.md`.

**Empresa:**

1. **Hoja de liquidación**: `calculo-finiquito-<apellido-trabajador>-<AAAAMMDD>.docx`.
   - Datos de partida con su fuente; salario diario y divisor declarado.
   - Una tabla por concepto con la operación completa (por ejemplo: «[días anuales] × [días de servicio] ÷ [días del periodo] = [días devengados]; [días devengados] − [días disfrutados] = [días pendientes]; [días pendientes] × [valor del día] = [importe]»), redondeo a céntimos.
   - Descuentos, cada uno con su soporte (artículo del convenio con su código, documento del anticipo).
   - Total bruto, indemnización en línea separada y nota de que las retenciones y cotizaciones las aplica la nómina de liquidación.
   - **Notas para el abogado**: artículos del ET y del convenio leídos, criterios adoptados, riesgos y, cuando se discuta algo, doctrina literal con su ECLI.
2. **Propuesta de liquidación y recibo de finiquito**: `carta-finiquito-<apellido-trabajador>-<AAAAMMDD>.docx`.
   - Membrete (`[DENOMINACIÓN SOCIAL]`, `[CIF]`), destinatario (`[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`), lugar y fecha.
   - Causa y fecha de la extinción; si se entrega con la comunicación, «propuesta del documento de liquidación» (art. 49.2 ET). En la dimisión no hay denuncia ni preaviso del empresario al que acompañar la propuesta: se entrega la liquidación y el recibo, antes de pedir la firma.
   - Si el convenio fija una indemnización propia para el fin del contrato, compárala con la legal y aplica la que corresponda según el propio artículo, con las dos cifras a la vista.
   - Tabla de conceptos con importes brutos, la indemnización aparte con su precepto, total, forma y fecha de pago.
   - Cláusula de saldo limitada a los conceptos detallados, con la voluntad de dar por extinguida la relación en la fecha indicada; sin renuncias genéricas de futuro ni a derechos indisponibles.
   - Casillas del art. 49.2 ET: «firmo en presencia del representante legal [nombre]» / «no he hecho uso de la posibilidad de solicitar su presencia» / espacio para que el trabajador haga constar que se le impidió.
   - Espacio para la conformidad o para «recibí, no conforme» y las observaciones del trabajador.
   - Firma de la empresa, firma y fecha del trabajador (recibí) o constancia de la negativa ante dos testigos.

**Trabajador:**

- **Nota de revisión**: `nota-revision-finiquito-<empresa>-<AAAAMMDD>.docx`: plazo del despido si lo hay (fecha final y precepto) en primera línea; tabla concepto · pagado · debido · diferencia · fundamento; valoración del valor liberatorio con la doctrina literal y su ECLI; qué hacer (firmar o no y con qué mención, qué reclamar, cauce, plazo con fecha y precepto); documentos que faltan. Adjunta la hoja `calculo-finiquito-<apellido-trabajador>-<AAAAMMDD>.docx` con lo debido.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los arts. 3, 26, 29, 31, 38, 49, 53, 59 y 64 ET que se citan, y el 26, 65 y 103 LRJS si se aconseja reclamar; anotada su vigencia.
- [ ] Convenio identificado, `vigencia_convenio` contrastada con la fecha de la extinción y leídos con `leer_convenio` sus artículos de vacaciones, pagas y preaviso.
- [ ] Ningún descuento por falta de preaviso sin artículo del convenio o cláusula del contrato leídos; un plazo del contrato superior al del convenio no se aplica en el exceso; la pérdida de conceptos ya devengados, solo con advertencia de riesgo de multa de haber.
- [ ] Buscado en el convenio si fija indemnización o plus propios al terminar un contrato temporal, y si regula la retribución de las vacaciones.
- [ ] Cada concepto con su operación visible, divisor declarado y redondeo a céntimos; la indemnización separada del salario.
- [ ] Documento sin renuncias genéricas de futuro, con las casillas del art. 49.2 ET y espacio para «no conforme».
- [ ] Sin afirmar que el art. 49.2 ET obliga a dar copia del finiquito a la representación; las comunicaciones a la representación citadas por su artículo (64.4 y 53.1.c).
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre la nota y el documento; sus veredictos sobre artículos de convenio ignorados y esos artículos comprobados con `leer_convenio`.
- [ ] Marcadores en lugar de datos no facilitados; ningún importe inventado.
- [ ] Todo dato que no salga de Jurisprudenciator citado con enlace y fecha de consulta y señalado en el resumen.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado y para quién, plazo con fecha y precepto si lo hay, importes y de dónde sale cada uno, documentos que faltan, riesgos, jurisprudencia citada y próximo paso.
