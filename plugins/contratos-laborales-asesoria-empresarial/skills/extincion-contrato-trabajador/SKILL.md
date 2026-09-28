---
name: extincion-contrato-trabajador
description: >-
  Prepara la demanda de extinción del contrato a instancia del trabajador por incumplimiento grave del
  empresario (art. 50 ET): modificaciones sin respetar el art. 41 que menoscaban la dignidad, impago o
  retrasos continuados del salario (definición legal vigente y doctrina sobre gravedad), acoso y otros
  incumplimientos graves; indemnización de despido improcedente, mantenimiento del contrato y cautelares
  del art. 79.7 LRJS, acumulación con un despido posterior (art. 32 LRJS). Para el trabajador, la demanda;
  para la empresa demandada, la nota de riesgo. Úsala con «quiero irme con indemnización», «artículo 50»,
  «no me pagan a tiempo», «nos piden la extinción». Si solo quiere cobrar, reclamacion-cantidad; si quiere
  seguir y que cese la conducta, tutela-derechos-fundamentales; si ya le despidieron,
  redactar-demanda-despido.
---

# Extinción del contrato a instancia del trabajador (art. 50 ET)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Causas y efectos de la extinción** → `buscar_articulo` (`ley="ET"`, artículos `"50"`, `"49"` y `"56"`; según la causa, `"4"` y `"29"` para el salario, `"41"` para la modificación sustancial y `"40"` para el traslado).
- **Proceso: urgencia, calendario, cautelares, acumulación y recurso** → `buscar_articulo` (`ley="LRJS"`, artículos `"26"`, `"32"`, `"43"`, `"79"`, `"103"`, `"180"` y `"191"`; si la empresa ha despedido después de la demanda, también `"29"`, `"65"` y `"83"`).
- **Si hay vulneración de derechos fundamentales** → `buscar_articulo` (`ley="LRJS"`, artículos `"178"`, `"179"`, `"181"`, `"183"` y `"184"`) y la norma del derecho afectado (`ley="CE"`; `ley="BOE-A-2022-11589"` o `ley="BOE-A-2007-6115"` si el acoso es discriminatorio).
- **Desempleo tras la extinción** → `buscar_articulo` (`ley="LGSS"`, `articulo="267"`).
- **Doctrina sobre gravedad del impago o del retraso, mantenimiento de la relación, despido posterior y acoso** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`; y `base="AN"`, `tipo_organo="TSJ"`, `provincia` = sede de la Sala) + `leer_sentencias` (`parrafos=3`, `terminos` del incumplimiento concreto).
- **Convenio aplicable y sus artículos** (fecha y forma de pago del salario, estructura salarial, jornada, clasificación) → `buscar_convenio` + `leer_convenio` + `vigencia_convenio` en el periodo de los incumplimientos.
- **Empresa** → `buscar_empresa_mercantil` (situación, concurso, grupo, administradores).
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

Esta skill también está en el plugin de litigación laboral. En este plugin la usa el despacho que asesora a la empresa y además lleva sus despidos y reclamaciones, o que defiende al trabajador. **Pregunta primero a quién defiende el abogado**:

- **Trabajador**: quiere salir de la empresa con la indemnización del despido improcedente porque el empresario incumple gravemente (salario, dignidad, acoso, ocupación efectiva, seguridad, reincorporación tras un traslado o una modificación anulados).
- **Empresa demandada o amenazada con la demanda**: nota que mide la exposición, dice qué hacer ya (regularizar pagos, cortar la conducta, no represaliar), qué no hacer (un despido precipitado) y qué ofrecer en conciliación.

| Situación | Skill |
|---|---|
| Solo quiere cobrar lo debido y seguir | `reclamacion-cantidad` |
| Quiere seguir trabajando y que cese el acoso o la discriminación | `tutela-derechos-fundamentales` |
| La relación ya se extinguió (despido expreso o tácito) antes de demandar | `redactar-demanda-despido`: la acción es la de despido |
| Modificación sustancial hecha por el cauce del art. 41 ET que le perjudica | `modificacion-sustancial-condiciones` (rescisión con la indemnización del art. 41.3 o impugnación); el art. 50.1.a exige que no se respetara el art. 41 y que se menoscabe la dignidad |
| Traslado que implica cambio de residencia | `movilidad-geografica-funcional` (opción del art. 40.1 ET) |
| Instruir internamente una denuncia de acoso | `protocolo-acoso-laboral` |
| Falta la papeleta | `papeleta-conciliacion` |
| Cuantificar la indemnización | `calculo-indemnizacion-despido` |

## Datos que hay que reunir antes de redactar

No redactes al primer disparo: si falta un dato imprescindible (★), pregúntalo.

1. ★ A quién defiende el abogado y qué causa del art. 50.1 se invoca (una o varias).
2. ★ Si el trabajador sigue prestando servicios y si quiere o necesita dejar de hacerlo (salud, riesgo, acoso): condiciona la estrategia de mantenimiento o cautelares.
3. ★ Impago o retraso: **calendario completo** de los últimos doce meses como mínimo, con la fecha de pago fijada (contrato, convenio o usos), la fecha real de cada abono, el importe y lo que sigue pendiente. Pide las nóminas y los extractos bancarios.
4. ★ Otros incumplimientos: cada episodio con fecha, autor, testigos y soporte (correos, mensajes, partes médicos, denuncias internas o ante la Inspección, sentencias previas sobre traslado o modificación).
5. ★ Antigüedad con todos los periodos, salario real con sus conceptos (nóminas de doce meses), categoría y convenio.
6. ★ Fecha de la papeleta y del acto; otros procesos en curso entre las partes (despido, cantidad, tutela).
7. ★ Empresa exacta; situación económica, concurso, acuerdos con la representación para aplazar pagos.
8. Daños adicionales si hay vulneración de derechos fundamentales: duración, gravedad, consecuencias en la salud (sin reproducir diagnósticos de terceros).
9. Si defiende a la empresa: explicación de cada retraso o conducta, pagos posteriores, medidas adoptadas, protocolo de acoso y su aplicación.
10. Si el trabajador está de baja médica, embarazada, disfruta permisos o ha denunciado la situación: anótalo, porque un despido posterior tendría riesgo de nulidad y la empresa debe saberlo.
11. Si es o fue representante legal o sindical: la indemnización no cambia, pero sí el riesgo de que la conducta empresarial lesione la libertad sindical.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su «vigente desde»; el art. 50 ET fue modificado por la LO 1/2025.

**Causas (art. 50.1 ET).**
- **a)** Modificaciones sustanciales llevadas a cabo **sin respetar el art. 41** y que redunden en **menoscabo de la dignidad**. Redacciones antiguas mencionaban también el perjuicio a la formación profesional: no lo alegues como causa. Si se respetó el art. 41, la vía es otra (art. 41.3 ET).
- **b)** Falta de pago o retrasos continuados en el abono del salario pactado. El texto vigente precisa, sin excluir otros supuestos que aprecie el juez, que hay retraso cuando se supera en quince días la fecha fijada para el pago, y que la causa concurre si en un año se adeudan tres mensualidades completas, aunque no sean consecutivas, o si hay retraso durante seis meses, aunque no sean consecutivos. Aplica esta regla con el calendario y, fuera de ella, la doctrina de la Sala Cuarta sobre gravedad (criterio objetivo, sin exigir culpabilidad, valorando la persistencia en el tiempo y la cuantía): léela antes de afirmarla.
- **c)** Cualquier otro incumplimiento grave, salvo fuerza mayor, y la negativa a reintegrar al trabajador en sus condiciones anteriores cuando una sentencia ha declarado injustificados un traslado o una modificación (arts. 40 y 41 ET). Aquí entran el acoso, la falta de ocupación efectiva o de seguridad y las lesiones de la dignidad (art. 4.2 ET).
- Efectos: la indemnización del despido improcedente (art. 50.2 ET, en relación con el art. 56.1). Es causa de extinción del contrato (art. 49.1.j ET).

**Indemnización y antigüedad anterior al 12/02/2012.** Calcula con la tabla del apartado 7 del formato o con `calculo-indemnizacion-despido`. `buscar_articulo` no devuelve la disposición transitoria undécima del ET: si hay antigüedad anterior a esa fecha, léela en internet en el texto consolidado del ET en el BOE (BOE-A-2015-11430) y cítala con su enlace y la fecha de consulta, o remite el cálculo a esa skill. La página completa del ET es demasiado larga para leerla de una vez: pide solo el bloque de la disposición en la API de datos abiertos del BOE (`https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2015-11430/texto/bloque/dtundecima`, cabecera `Accept: application/xml`).

**Proceso.**
- Conciliación previa obligatoria (la materia no figura en el art. 64.1 LRJS). En esta modalidad agosto y del 24 de diciembre al 6 de enero son hábiles (art. 43.4 LRJS).
- Plazo: el ET no fija uno especial para esta acción; comprueba con la doctrina cómo se aplica la prescripción del art. 59.1 ET y si el incumplimiento debe persistir al demandar, y deja en la nota la fecha límite prudente. Las sentencias de la Sala Cuarta sobre gravedad del retraso suelen fijar también hasta qué fecha se valoran los incumplimientos (en ocasiones, hasta el juicio). Si no aparece doctrina específica sobre el plazo, no detengas la tarea por ese dato: toma como referencia prudente un año desde el último incumplimiento (art. 59.1 ET), dilo así en la nota y recomienda presentar sin demora.
- Si la causa es la del art. 50.1.b, tramitación urgente y preferente, con vista y sentencia en cinco días (art. 103.4 y 103.5 LRJS): pídela en un otrosí.
- Acumulación en una sola demanda: despido y extinción, si la acción de despido está en plazo; con el art. 50.1.b, la reclamación salarial, ampliable a lo que se siga debiendo (art. 26.3 LRJS). Si se presentan por separado la de extinción y la de despido, se acumulan y la sentencia sigue el orden del art. 32.1 LRJS (primero la que está en la base del conflicto; si son independientes, la nacida antes). La segunda demanda debe indicar la pendencia de la primera y el juzgado.
- La sentencia es siempre recurrible en suplicación (art. 191.3.a LRJS).

**Mantenimiento de la relación durante el pleito.** La extinción la declara la sentencia, que tiene carácter constitutivo: por regla general el contrato debe estar vivo cuando el juez resuelve. La doctrina admite que el trabajador cese al demandar cuando seguir le causaría un grave perjuicio, pero a su riesgo: si no se aprecia incumplimiento grave, pierde el empleo sin indemnización. Alternativa segura: pedir **medidas cautelares** del art. 79.7 LRJS cuando la conducta perjudica la dignidad o la integridad, puede vulnerar derechos fundamentales o hace inexigible seguir en las condiciones anteriores; las medidas son las del art. 180.4 (suspensión o exoneración de prestar servicios, traslado de puesto o centro, reordenación del tiempo de trabajo…), con mantenimiento del salario y de la cotización. Lee la doctrina vigente antes de aconsejar el cese.

**Despido posterior.** Si la empresa despide mientras se tramita, hay que impugnar el despido en su plazo: si no, el contrato queda extinguido por el despido y la acción del art. 50 decae. Adviértelo al cliente por escrito desde el primer día. Si el despido ya se ha producido, esta skill prepara:
- el **plazo de caducidad** del despido con fecha límite: veinte días hábiles (art. 103.1 LRJS), con la suspensión de la papeleta (art. 65.1 LRJS); cuenta como consumido, por prudencia, el día de la papeleta;
- un **escrito a la Sección que conoce de la extinción** que comunica el despido, pide la acumulación de la demanda de despido (art. 32.1 LRJS; la petición se dirige a la Sección de la demanda más antigua, art. 29 LRJS), la suspensión del juicio si está señalado antes de que pueda acumularse (art. 83.1 LRJS) y, con la causa del art. 50.1.b, la ampliación de las cantidades adeudadas después de la demanda (art. 26.3 LRJS);
- en la nota, el orden en que el juez examinará las acciones (art. 32.1 LRJS, párrafo segundo), los escenarios (extinción estimada, con la doctrina sobre salarios de tramitación; despido improcedente; despido nulo por represalia) y la situación legal de desempleo desde el despido (art. 267.1.a LGSS).
La **demanda de despido** se redacta con `redactar-demanda-despido`, que debe hacer constar la pendencia del primer proceso y el juzgado; la nota le pasa los indicios de represalia y lo que no debe duplicarse (las cantidades ya reclamadas por ampliación).

**Derechos fundamentales.** Si se invoca su lesión (acoso, discriminación, represalia), la extinción sigue su modalidad con las garantías de la tutela (arts. 178.2 y 184 LRJS): citación del Ministerio Fiscal, indicios y carga de la prueba (art. 181.2), indemnización pretendida con sus bases (art. 179.3), compatible con la de extinción (art. 183.3), y posibilidad de demandar también al causante directo.

**Desempleo.** La resolución voluntaria en los supuestos del art. 50 ET es situación legal de desempleo; el cese voluntario sin resolución favorable no lo es (art. 267.1.a.5.º y 267.2.a LGSS). Si se negocia una salida en conciliación, comprueba sus efectos en ese artículo antes de firmar.

## Estrategia y jurisprudencia

**Si defiende al trabajador.**
1. Encaja primero en la regla objetiva del art. 50.1.b (tres mensualidades completas en un año o seis meses con retraso superior a quince días) y, si no llega, construye la gravedad con la doctrina y con el calendario.
2. En el art. 50.1.c, cada episodio es un hecho con fecha y prueba; evita valoraciones sin soporte. Si hay acoso, valora pedir cautelares y la indemnización del art. 183 LRJS.
3. No aconsejes dejar de trabajar sin haber leído la doctrina de mantenimiento y sin haber valorado las cautelares.

**Si defiende a la empresa.**
1. Mide la exposición: indemnización, salarios pendientes con el interés del art. 29.3 ET, daño moral si hay derechos fundamentales. Con la causa del art. 50.1.a, calcula también como referencia de negociación la rescisión del art. 41.3 ET (veinte días por año, máximo nueve meses).
2. Corta ya el incumplimiento (paga, regulariza, activa el protocolo de acoso) y documenta cada medida; busca la doctrina sobre el efecto de la regularización posterior antes de prometer que enerva la acción.
3. No despidas como reacción a la demanda: el art. 32.1 LRJS obliga a examinar ambas acciones y la represalia puede fundar la nulidad por vulneración de la garantía de indemnidad.

**Consultas** (reformula dos veces como máximo; lee solo lo que vayas a citar, `parrafos=3`, y transcribe fundamentos, nunca hechos ni datos de las partes):
- Gravedad (y fecha límite de los incumplimientos, efecto de la crisis de la empresa): `consulta="retraso continuado pago salario extinción artículo 50 gravedad objetiva situación económica"`, `base="TS"`, `fecha_desde="01/01/2005"`; aplicación de la definición de la LO 1/2025: la misma consulta con `base="AN"`, `tipo_organo="TSJ"`, `fecha_desde="03/04/2025"`.
- Mantenimiento: `consulta="extinción artículo 50 mantenimiento de la relación laboral hasta sentencia cese voluntario grave perjuicio"`, `base="TS"`.
- Despido posterior: `consulta="acumulación despido y extinción artículo 50 orden de resolución artículo 32"`, `base="TS"`.
- Acoso y dignidad: `consulta="extinción artículo 50.1.c acoso laboral dignidad integridad moral"`, `base="AN"`, `tipo_organo="TSJ"`.
- Regularización posterior: `consulta="extinción artículo 50 pago de los salarios adeudados antes del juicio"`, `base="TS"`.
- Plazo: `consulta="plazo ejercicio acción extinción artículo 50 incumplimiento persistente"`, `base="TS"` (si no hay resultado útil, regla prudente del apartado «Proceso»).
- Interés por mora del salario: `consulta="interes por mora 10 por ciento anual salario"`, `base="TS"`. El «diez por ciento de lo adeudado» del art. 29.3 ET se aplica de forma automática y se calcula como tipo anual, en proporción a los días de demora desde cada vencimiento hasta el pago o la sentencia: léelo antes de cuantificarlo y no lo sumes como un 10 % fijo.

## Documentos que se entregan

**1. Demanda** (`demanda-extincion-art50-<apellido-cliente>-<AAAAMMDD>.docx`), si defiende al trabajador, maquetada según el apartado 2 del formato:
1. Encabezamiento al Tribunal de Instancia de `[SEDE]`, Sección de lo Social; demandante con marcadores; `[DENOMINACIÓN SOCIAL]` y `[CIF]` comprobados; persona física causante si se la demanda; Ministerio Fiscal si se invocan derechos fundamentales; FOGASA si procede. Acción: extinción del contrato por voluntad del trabajador (art. 50 ET), por el procedimiento ordinario, con la tramitación urgente del art. 103.5 LRJS si la causa es la letra b.
2. HECHOS: relación laboral (antigüedad con periodos, categoría, salario con conceptos, convenio con su código, fecha de pago fijada); incumplimientos en orden cronológico, con el **calendario de pagos** en tabla (mes · fecha debida · fecha de pago · días de retraso · importe · pendiente) o los episodios con su soporte; afectación a la dignidad o a la salud; si sigue prestando servicios; conciliación previa.
3. FUNDAMENTOS: competencia (art. 2.a y art. 10.1 LRJS); conciliación previa; causa del art. 50.1 con su texto vigente y la doctrina leída sobre gravedad; efectos (art. 50.2 y art. 56.1 ET); acumulación de la cantidad (art. 26.3 LRJS) y su interés (art. 29.3 ET); si hay derechos fundamentales, arts. 178.2, 181.2 y 183 LRJS con las bases de la indemnización; convenio.
4. SUPLICO: que se declare extinguida la relación por incumplimiento grave del empresario, con condena a la indemnización de `[IMPORTE]` €, a las cantidades adeudadas con el interés del art. 29.3 ET (diez por ciento anual desde cada vencimiento) y, en su caso, a `[IMPORTE]` € por daño moral.
5. OTROSÍES: tramitación urgente (art. 103.5 LRJS) si la causa es la letra b; medidas cautelares del art. 79.7 en relación con el art. 180.4 LRJS, con su justificación; prueba (interrogatorio con el apercibimiento del art. 91.2, documental en poder de la empresa, testifical, pericial médica si procede).

**2. Hoja de cálculo** (`calculo-indemnizacion-<apellido-trabajador>-<AAAAMMDD>.docx`) con la tabla del apartado 7 del formato.

**3. Escrito de acumulación** (`escrito-acumulacion-<apellido-cliente>-<AAAAMMDD>.docx`), solo si la empresa despide después de presentada la demanda: al órgano y autos de la extinción; alegaciones (estado del proceso, despido y papeleta, acumulación obligatoria con la doctrina leída, orden de examen, suspensión del señalamiento, ampliación de cantidades en tabla con su interés); suplico; documentos.

**4. Nota** (`nota-extincion-<empresa>-<AAAAMMDD>.docx`): encaje en la regla del art. 50.1.b o en la doctrina; riesgos de mantenimiento y de despido posterior; desempleo; para la empresa, exposición por escenarios, medidas inmediatas y propuesta para la conciliación; jurisprudencia literal usada.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos en esta conversación ET 50 (redacción de la LO 1/2025), 49 y 56, y los que se citen (4, 29, 40, 41); LRJS 26, 32, 43, 79, 103, 180 y 191; y LGSS 267 si se habla de desempleo.
- [ ] Convenio con su código y vigencia; fecha de pago del salario obtenida del convenio, del contrato o de los usos.
- [ ] Empresa comprobada con `buscar_empresa_mercantil`.
- [ ] Calendario de pagos completo y regla objetiva del art. 50.1.b aplicada mes a mes, o gravedad sostenida con doctrina leída.
- [ ] Advertencias escritas al cliente sobre el mantenimiento de la relación y sobre la impugnación de un despido posterior.
- [ ] Si ya hubo despido posterior: plazo de caducidad con fecha límite, escrito de acumulación (y de suspensión y ampliación, si procede) y derivación de la demanda de despido a `redactar-demanda-despido`.
- [ ] Si se piden cautelares, el otrosí justifica los presupuestos del art. 79.7 LRJS y concreta las medidas del art. 180.4 que se solicitan.
- [ ] Si se invocan derechos fundamentales, Ministerio Fiscal citado e indemnización del art. 183 LRJS con sus bases.
- [ ] Interés del art. 29.3 ET calculado por días de demora desde cada vencimiento (tipo anual), con la doctrina leída.
- [ ] Cálculo en tabla con cada operación; antigüedad anterior al 12/02/2012 calculada con la disposición transitoria undécima leída en el BOE consolidado (enlace y fecha) o remitida a `calculo-indemnizacion-despido`.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre cada documento; avisos de «posible disonancia» contrastados con el apartado leído.
- [ ] Marcadores en lugar de datos no facilitados; plazo con su fecha y precepto.
- [ ] Los datos obtenidos en internet figuran con su enlace en el documento y en el resumen.
- [ ] Resumen para el abogado según el apartado 9 del formato.
