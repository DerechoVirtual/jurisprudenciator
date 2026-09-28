---
name: papeleta-conciliacion
description: >-
  Redacta la papeleta de conciliación o la solicitud de mediación previa ante el servicio autonómico de
  mediación, arbitraje y conciliación (arts. 63-68 LRJS) para demandar por despido, cantidad, extinción
  del art. 50 ET o sanción, con hechos, cuantías desglosadas y petición que protejan la demanda
  posterior frente a la variación sustancial (art. 80.1.c LRJS). Sirve al trabajador (redactarla) y a la
  empresa que la recibe o que reclama a un trabajador (postura para el acto, oferta, riesgo de costas por
  no comparecer). Úsala con «papeleta», «SMAC», «conciliación previa», «me citan a conciliación»,
  «presentar la conciliación antes de la demanda». Si la materia está exenta (tutela sin despido,
  vacaciones, modificación sustancial, movilidad, ERTE, monitorio), ve directamente a la demanda o a su
  skill.
---

# Papeleta de conciliación o solicitud de mediación previa

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Requisito, exenciones, efectos, incomparecencia, impugnación y ejecutividad** → `buscar_articulo` (`ley="LRJS"`, artículos `"63"`, `"64"`, `"65"`, `"66"`, `"67"`, `"68"`), y **congruencia con la demanda y aportación de la certificación** → (`ley="LRJS"`, artículos `"80"` y `"81"`).
- **Plazo de la acción que se va a conciliar** → `buscar_articulo` (`ley="ET"`, `articulo="59"`), (`ley="LRJS"`, artículos `"103"`, `"121"` si es despido objetivo, `"114"` si es sanción, y `"43"` para agosto y Navidad); **acumulación en una sola papeleta** → (`ley="LRJS"`, artículos `"25"` y `"26"`); **despido con lesión de derechos fundamentales** (no exento: va por la modalidad de despido) → (`ley="LRJS"`, artículos `"184"`, `"179"` y `"183"`).
- **Contenido mínimo de la papeleta y lugar de presentación** → `buscar_articulo` (`ley="Real Decreto 2756/1979"`, artículos `"5"`, `"6"` y `"9"`), norma estatal supletoria; **nombre, modelo y forma de presentación del servicio autonómico**, que el conector no tiene → en internet, en la sede oficial de la comunidad (punto 3 de la puerta).
- **Garantía del FOGASA sobre lo que se pacte** → `buscar_articulo` (`ley="ET"`, `articulo="33"`).
- **Festivos de la sede del órgano** (para contar los días hábiles), que el conector no tiene → en internet: decreto de fiestas laborales del año en el diario oficial de la comunidad y fiestas locales en la web del ayuntamiento de la sede o en el diario oficial, con enlace.
- **Doctrina sobre la correspondencia entre papeleta y demanda** → `buscar_sentencias` (`consulta="papeleta de conciliación variación sustancial demanda hechos distintos"`, `base="TS"`, `jurisdiccion="SOCIAL"`, `anios=3`) + `leer_sentencias` (`parrafos=3`, `terminos="variación sustancial conciliación previa"`); en despidos disciplinarios, además, la doctrina de audiencia previa (apartado 4 de las anclas).
- **Convenio aplicable** (categoría, salario, graduación de faltas, órgano propio de solución de conflictos) → `buscar_convenio` + `leer_convenio` (`buscar_en="comisión paritaria"`, `buscar_en="solución extrajudicial"` o el artículo que toque) + `vigencia_convenio`.
- **Empresa** → `buscar_empresa_mercantil` (denominación exacta, domicilio social, administradores, concurso o disolución).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Esta skill también está en el plugin Contratos Laborales y Asesoría Empresarial, que añade la asesoría de empresa (convenio aplicable, cálculo de indemnizaciones, cartas de despido, finiquitos…). Si una derivación de esta skill nombra una skill que no está en este plugin, está en aquel. **Pregunta primero a quién defiende el abogado** y bifurca:

- **Trabajador (solicitante)**: redacta la papeleta para despido, extinción del art. 50 ET, reclamación de cantidad, impugnación de sanción u otra acción ordinaria frente a la empresa. Objetivo: que suspenda la caducidad o interrumpa la prescripción a tiempo y que la demanda posterior no pueda tacharse de variación sustancial.
- **Empresa que ha recibido la papeleta**: prepara la postura para el acto (avenencia posible, oferta y su cálculo, reconocimiento o no de la improcedencia, riesgo de costas si no comparece). La empresa no redacta papeleta en respuesta.
- **Empresa solicitante**: cuando reclama al trabajador en el orden social (por ejemplo, incumplimiento de un pacto de permanencia o de no competencia, o daños). Mismo método que el trabajador.

No es esta skill:

| Situación | Qué procede |
|---|---|
| Materia exenta del art. 64.1 LRJS (tutela de derechos fundamentales sin despido, vacaciones, movilidad geográfica, modificación sustancial, ERTE, conciliación de la vida familiar del art. 139, trabajo a distancia del art. 138 bis, monitorio…) | Demanda directa: `tutela-derechos-fundamentales`, `modificacion-sustancial-condiciones`, `movilidad-geografica-funcional`, `permisos-conciliacion-adaptacion`, `erte-suspension-reduccion` o `reclamacion-cantidad` (monitorio) |
| Demandada una Administración pública empleadora | Agotamiento de la vía administrativa (arts. 69 y 70 LRJS), no papeleta |
| Prestaciones de Seguridad Social | Reclamación previa del art. 71 LRJS: fuera de este plugin |
| Aún no está claro qué acción ni qué plazo corre | `laboral-empresa-intake` |
| Papeleta presentada y acto celebrado o vencido el plazo | `redactar-demanda-despido`, `reclamacion-cantidad`, `extincion-contrato-trabajador`, `sanciones-disciplinarias` |
| Hay que cuantificar indemnización o liquidación para la papeleta o la oferta | `calculo-indemnizacion-despido` o `finiquito-liquidacion`, y vuelve con la cifra |

## Datos que hay que reunir antes de redactar

No redactes al primer disparo: si falta un dato imprescindible (★), pregúntalo.

1. ★ A quién defiende el abogado y quién es solicitante y quién citado.
2. ★ Acción o acciones que se van a ejercitar y, para cada una, su **fecha inicial**: efectos del despido o de la extinción, notificación de la sanción, fecha en que cada cantidad fue exigible. Sin ella no se calcula el plazo (formato, apartado 6).
3. ★ Fecha prevista de presentación y forma (sede electrónica o registro del servicio autonómico): búscala en internet en la sede oficial de la comunidad y cita el enlace; no des modelos, códigos ni tasas que no salgan de esa fuente.
4. ★ Datos del trabajador: categoría o grupo, antigüedad (periodos), salario real con sus conceptos (nóminas), lugar y clase de trabajo, jornada, convenio aplicable.
5. ★ Empresa exacta y, si hay grupo, contrata, cesión o sucesión, todas las posibles demandadas: después no se podrá conciliar con quien no figuró, salvo el supuesto del art. 64.2.b LRJS.
6. ★ En despido: fecha, forma, motivos alegados en la carta (adjúntala), si hubo audiencia previa al trabajador, si es o fue representante en el último año o afiliado conocido, y cualquier indicio de nulidad (embarazo, permisos, adaptación de jornada, baja médica, reclamación previa, denuncia, afiliación).
7. ★ En cantidad: cada concepto, periodo, devengado, percibido y diferencia; si son diferencias de convenio, la tabla salarial del año: búscala en internet (revisión salarial publicada en el BOE, el boletín autonómico o el BOP; `vigencia_convenio` dice qué publicaciones hay) y, si no aparece, pídela al abogado. Sin tabla no se calculan (anclas, apartado 3).
8. Quién comparecerá y con qué representación (art. 9 del Real Decreto 2756/1979); teléfono y correo del solicitante sin profesional (art. 66.1 LRJS).
9. Si defiende a la empresa: papeleta recibida, fecha del acto, margen económico autorizado y documentación del expediente (carta, nóminas, registro de jornada, expediente disciplinario).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su «vigente desde».

**Requisito y destinatario.**
- El intento de conciliación o mediación previa es requisito para tramitar el proceso, ante el servicio administrativo o ante el órgano creado por acuerdos interprofesionales o convenios colectivos (art. 63 LRJS). Comprueba en el convenio si prevé un órgano o sistema propio de solución de conflictos y dilo al abogado.
- Lugar: el del lugar de prestación de servicios o del domicilio de los interesados, a elección del solicitante (art. 5 del Real Decreto 2756/1979). La denominación del servicio cambia en cada comunidad: búscala en internet en la sede oficial de la comunidad (con enlace y fecha de consulta) o pregúntala al abogado; si no aparece, encabeza como indica el apartado 3 del formato y avísalo.

**Exenciones (art. 64 LRJS).** Lee la lista vigente del apartado 1 antes de decidir: incluye, entre otros, Seguridad Social, vacaciones, materia electoral, movilidad geográfica, modificación sustancial, suspensión y reducción de jornada del art. 47 ET, procesos monitorios, derechos de conciliación del art. 139, tutela de derechos fundamentales, impugnación de convenios, trabajo a distancia del art. 138 bis y acciones de protección frente a la violencia de género. El apartado 2 exceptúa además la ampliación posterior a personas distintas. El apartado 3 permite acudir voluntariamente y de común acuerdo en materias exentas, con efecto suspensivo o interruptivo. **El despido en que se alega vulneración de derechos fundamentales no está exento**: se tramita inexcusablemente por la modalidad de despido, acumulando la tutela (art. 184 LRJS), y exige papeleta; dilo en la nota.

**Plazos y efectos de la presentación.**
- Despido y extinción impugnable como despido: veinte días hábiles de caducidad (art. 59.3 ET y art. 103.1 LRJS, que excluye sábados, domingos y festivos de la sede del órgano); en el despido objetivo se cuentan desde el día siguiente a la fecha de extinción, no desde la entrega de la carta (art. 121.1 LRJS). Impugnación de sanción: el mismo plazo (art. 114.1 LRJS). Cantidades y acciones sin plazo especial: un año de prescripción desde que cada una pudo ejercitarse (art. 59.1 y 59.2 ET). En despido y extinción de los arts. 50, 51 y 52 ET, agosto y del 24 de diciembre al 6 de enero cuentan (art. 43.4 LRJS).
- La presentación **suspende la caducidad e interrumpe la prescripción** desde esa fecha; el cómputo se reanuda (caducidad) o se reinicia (prescripción) al día siguiente de intentado el acto o a los quince días hábiles de la presentación sin celebrarse (art. 65.1 LRJS). A los treinta días hábiles sin acto se tiene por cumplido el trámite (art. 65.2 LRJS). El art. 59.3 ET habla de «interrupción»: calcula con el art. 65.1 LRJS y dilo en la nota.
- Cálculo obligatorio, visible en la nota: días hábiles consumidos hasta la presentación, fecha de reanudación, días restantes y **fecha límite de la demanda** con cada precepto. **Cuenta como consumido el propio día de presentación** (cómputo prudente: da la fecha límite más temprana) y dilo. Calcula siempre dos hipótesis: acto celebrado en una fecha concreta (reanudación al día siguiente) y acto **no celebrado en los quince días hábiles** (reanudación al día siguiente del decimoquinto), porque los servicios suelen citar más tarde; en esa segunda hipótesis la demanda se presenta sin esperar al acto y el intento se acredita después (art. 81.3 LRJS). Da también la fecha de los treinta días hábiles del art. 65.2 LRJS.

**Asistencia (art. 66 LRJS).**
- Si el solicitante citado no comparece sin justa causa, la papeleta se tiene por no presentada y se archiva (art. 66.2): se pierde el efecto suspensivo y la acción puede haber caducado. Adviértelo por escrito al cliente trabajador.
- Si no comparece el citado, la conciliación se tiene por intentada sin efecto y, si la sentencia coincide esencialmente con la papeleta, el juez impondrá las costas, con honorarios hasta el límite del art. 66.3. Por eso la papeleta debe llevar la pretensión completa y cuantificada; y la empresa debe comparecer siempre, aunque no ofrezca nada.

**Contenido (art. 6 del Real Decreto 2756/1979).** Datos personales y domicilios de todos los interesados; lugar y clase de trabajo, categoría, antigüedad, salario y demás remuneraciones; enumeración clara y concreta de los hechos y cuantía económica; en despido, fecha y motivos alegados por la empresa; fecha y firma. Añade las copias que exija el servicio.

**Congruencia con la demanda (art. 80.1.c LRJS).** La demanda no podrá alegar hechos distintos de los aducidos en conciliación, salvo los nuevos o desconocidos. Reglas de redacción que de ello resultan:
- Incluye **todos** los hechos conocidos, también los que fundan una posible nulidad (indicios, fechas de la reclamación o del embarazo, afiliación), aunque sean solo sospechas razonables.
- Pide siempre la calificación más amplia defendible: «nulidad y, subsidiariamente, improcedencia»; en cantidad, cada concepto con su importe y el interés del art. 29.3 ET si es salarial.
- En despidos disciplinarios posteriores a la doctrina del Pleno de noviembre de 2024, si no hubo audiencia previa, dilo ya en la papeleta.
- La doctrina de la Sala Cuarta modula el rigor de la correspondencia según haya hecho imposible la conciliación o causado indefensión: léela antes de afirmarlo y úsala solo en la nota.
- Si el servicio exige su **formulario oficial** y este solo ofrece casillas de improcedencia o de cantidad, traslada la petición de nulidad, la indemnización y sus hechos al campo de texto libre o adjunta la papeleta como escrito de hechos y pretensión; avísalo en la nota.

**Una papeleta o varias.** Acumula en una sola solo lo que después pueda ir en la misma demanda (arts. 25 y 26 LRJS): por ejemplo, despido con extinción del contrato y con las cantidades vencidas, exigibles y de cuantía determinada (art. 26.3), o extinción del art. 50.1.b con la reclamación salarial. Lo que irá en demanda separada (una sanción y una reclamación de horas, por ejemplo), en papeletas separadas: cada una con su plazo y su certificación.

**Después del acto.** Lo acordado es título ejecutivo (art. 68 LRJS) y se impugna por nulidad en treinta días hábiles (art. 67). La certificación del acto o la papeleta sellada se acompaña a la demanda; si falta, hay quince días para acreditarla con apercibimiento de archivo (arts. 80.2 y 81.3 LRJS).

**FOGASA.** El Fondo abona salarios reconocidos en acto de conciliación o resolución judicial (art. 33.1 ET), pero las **indemnizaciones** solo si se reconocen en sentencia, auto, acto de conciliación judicial o resolución administrativa (art. 33.2 ET). Si la empresa puede ser insolvente o está en concurso, advierte al trabajador de que una avenencia sobre la indemnización en el servicio administrativo no queda cubierta por el Fondo y valora conciliar en sede judicial.

## Estrategia y jurisprudencia

**Si defiende al trabajador.**
1. Presenta cuanto antes: cada día hábil que pasa se descuenta del plazo que quedará tras el acto.
2. Redacta los hechos como si fueran los de la demanda, en ordinales breves; la papeleta no necesita fundamentos extensos, pero sí la petición completa.
3. En despido, anota en la nota si la empresa no ha tramitado la baja en la Seguridad Social: la demanda será urgente (art. 103.4 LRJS).
4. En despido disciplinario con defectos de forma (incluida la falta de audiencia previa), advierte de que la empresa puede hacer un nuevo despido que los subsane en los veinte días siguientes al primero (art. 55.2 ET, léelo): sería un despido distinto, con su propio plazo y su propia papeleta.
5. Si se pide la nulidad por lesión de derechos fundamentales, cuantifica ya en la papeleta la indemnización por daño moral del art. 183 LRJS con sus bases (art. 179.3 LRJS). Si tomas como referencia orientativa la escala del artículo 40 del Real Decreto Legislativo 5/2000, léela con `buscar_articulo` (`ley="BOE-A-2000-15060"`) y di en la nota que la demanda justificará la cifra con la doctrina que se lea entonces.

**Si defiende a la empresa.**
1. Comprueba con los documentos si la carta, el procedimiento (audiencia previa, expediente contradictorio, audiencia a delegados sindicales) o la causa aguantan; si no, calcula con `calculo-indemnizacion-despido` la oferta: indemnización por improcedencia (art. 56.1 ET, y la disposición transitoria undécima del ET si el contrato es anterior al 12/02/2012, leída en el texto consolidado del BOE: formato, apartado 7) y, si la readmisión es probable, el trabajador es representante (art. 56.4 ET) o hay riesgo de nulidad, los salarios de tramitación que seguirían devengándose hasta la sentencia.
2. En despido objetivo, recalcula la indemnización puesta a disposición (salario real con todos los conceptos salariales y antigüedad con todos los contratos): si fue inferior a la debida, solo el **error excusable** evita la improcedencia (art. 53.4 ET y art. 122.3 LRJS). Busca la doctrina (`consulta="error excusable indemnización despido objetivo puesta a disposición cantidad inferior improcedencia"`, `base="TS"`) y advierte de que pagar después la diferencia no subsana la puesta a disposición, que debe ser simultánea a la entrega de la carta. Presenta en una tabla el coste de cada escenario (procedente con la diferencia, improcedente, readmisión), descontando lo ya pagado (art. 53.5.b ET).
3. Si se reconoce la improcedencia, déjalo expreso en el acta. Si no hay acuerdo, comparece igualmente y deja constancia de la postura (art. 66.3).
4. Nunca pactes en el acta un concepto salarial como indemnizatorio ni al revés sin avisar de sus efectos fiscales y de cotización: remite al asesor fiscal y a la nómina de liquidación.

**Jurisprudencia.** Es imprescindible solo si la papeleta lleva fundamentación o si la nota valora un riesgo que discute la doctrina (formato, apartado 8):
- Correspondencia papeleta-demanda: la consulta de la lista de arriba; si no devuelve nada útil, `consulta="hechos distintos aducidos en conciliación nulidad del despido no alegada en la papeleta"`.
- Costas por incomparecencia: `consulta="incomparecencia injustificada acto de conciliación costas honorarios artículo 66.3"`, `base="TS"`.
- Audiencia previa en despido disciplinario: consulta del apartado 4 de las anclas.
- Lee solo lo que vayas a citar (`parrafos=3`, `terminos` de la cuestión) y transcribe fundamentos, nunca los hechos ni los datos de las partes de aquel pleito.

## Documentos que se entregan

Maquetación según el apartado 2 del formato (escrito procesal, con «SOLICITO»).

**1. Papeleta** (`papeleta-conciliacion-<apellido-cliente>-<AAAAMMDD>.docx`), si el cliente es solicitante:
1. Encabezamiento al servicio autonómico (formato, apartado 3).
2. Solicitante: `[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[DOMICILIO]`, teléfono y correo; representación, si la hay.
3. Citados: `[DENOMINACIÓN SOCIAL]`, `[CIF]`, domicilio social comprobado con `buscar_empresa_mercantil`; demás empresas del grupo o contrata; FOGASA si procede.
4. HECHOS en ordinales: relación laboral (antigüedad con periodos, categoría, salario con conceptos, lugar, jornada, convenio con su código); hecho litigioso (despido con fecha y motivos, sanción, impago…); indicios de nulidad; falta de audiencia previa, si procede; cantidades en tabla (concepto · periodo · importe) con total.
5. Fundamento breve: arts. 63 y 65 LRJS y precepto sustantivo de la acción.
6. SOLICITO: que se tenga por presentada, se cite a las partes y, en el acto, se reconozca [pretensión completa: nulidad y readmisión con los salarios dejados de percibir (con su importe diario) y, si se alega lesión de derechos fundamentales, la indemnización por daño moral del art. 183 LRJS por `[IMPORTE]`; subsidiariamente, improcedencia con la opción e indemnización de `[IMPORTE]`; o pago de `[TOTAL]` más el interés del art. 29.3 ET].
7. Lugar, fecha y firma; relación de documentos (carta, nóminas, contrato, cuadro de cantidades).

**2. Nota para el abogado** (`nota-conciliacion-<empresa>-<AAAAMMDD>.docx`), siempre:
- Tabla de plazo: fecha inicial · precepto · días hábiles consumidos (incluido el de presentación) · fecha de presentación · reanudación (art. 65.1) · fecha límite de la demanda, en las dos hipótesis (acto en fecha concreta y sin acto en quince días hábiles) · festivos aplicados con su fuente.
- Riesgos: incomparecencia (art. 66), congruencia (art. 80.1.c), garantía del FOGASA (art. 33 ET), materias que no admiten acumulación.
- Si defiende a la empresa: valoración de la carta y del procedimiento, cálculo de la oferta en tabla con su origen, propuesta de redacción del acta.
- Jurisprudencia leída, con párrafo literal y ECLI, solo si se ha usado.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos en esta conversación LRJS 63, 64, 65, 66, 80 y 81, ET 59 y el precepto de plazo de la acción (LRJS 103, 121 o 114), y Real Decreto 2756/1979 arts. 5 y 6; el art. 64.1 comprobado para confirmar que la materia no está exenta (y el 184 si se alega lesión de derechos fundamentales en un despido).
- [ ] Convenio identificado con su código y vigencia en la fecha de los hechos, si se ha usado.
- [ ] Empresa comprobada con `buscar_empresa_mercantil`; todas las posibles demandadas en la papeleta.
- [ ] Plazo con fecha inicial, precepto, fecha de presentación (contada como consumida), festivos de la sede con su fuente y fecha límite de la demanda en las dos hipótesis (acto celebrado o sin acto en quince días hábiles); si falta la fecha inicial, no se ha dado plazo.
- [ ] Hechos completos (incluidos indicios de nulidad y falta de audiencia previa) y pretensión cuantificada, para no exponerse al art. 80.1.c LRJS.
- [ ] Cantidades en tabla, con cada operación visible; diferencias de convenio solo con la tabla salarial citada con su enlace o aportada por el abogado.
- [ ] Cada ECLI citado leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre la papeleta y la nota; los avisos de «posible disonancia» sobre los arts. 65, 66 u 80 contrastados con el apartado leído (el verificador compara con el título del artículo).
- [ ] Marcadores en lugar de datos no facilitados; denominación y forma de presentación del servicio autonómico con enlace a la sede oficial y fecha de consulta, o marcadas como no confirmadas; nada inventado.
- [ ] Los datos obtenidos en internet (y no de Jurisprudenciator) figuran con su enlace en el documento y en el resumen.
- [ ] Resumen para el abogado según el apartado 9 del formato.
