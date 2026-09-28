---
name: movilidad-geografica-funcional
description: >-
  Traslados y desplazamientos (art. 40 ET: causa, cambio de residencia, preaviso, compensación de
  gastos, dietas, opción de extinguir con 20 días por año y umbrales colectivos) y movilidad funcional
  (art. 39 ET: dentro del grupo profesional, funciones superiores o inferiores, retribución y
  reclamación de ascenso), con su impugnación (art. 138 LRJS o proceso de clasificación del art. 137
  LRJS). Sirve a la empresa (carta de traslado, desplazamiento o cambio de funciones que aguante) y al
  trabajador (opción, impugnación, ascenso y diferencias). Úsala con «me trasladan a otra ciudad»,
  «desplazamiento», «dietas», «cambio de centro», «hago funciones de superior categoría», «me ponen a
  hacer tareas inferiores». Si el cambio de funciones excede el art. 39, usa
  modificacion-sustancial-condiciones.
---

# Movilidad geográfica y funcional

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Traslado, desplazamiento, traslado colectivo, preferencias y prioridad de permanencia** → `buscar_articulo` (`ley="ET"`, `articulo="40"`, y `"41"` para los interlocutores del periodo de consultas a los que remite).
- **Movilidad funcional, grupo profesional y ascensos** → `buscar_articulo` (`ley="ET"`, artículos `"39"`, `"22"` y `"24"`).
- **Acciones, plazos y recursos** → `buscar_articulo` (`ley="ET"`, artículos `"50"` y `"59"`) y (`ley="LRJS"`, artículos `"43"`, `"63"`, `"64"`, `"137"`, `"138"`, `"153"` y `"191"`).
- **Convenio: compensación por traslado, dietas, kilometraje, plus de distancia, grupos profesionales, periodos para reclamar la vacante y procedimiento de ascensos** → `buscar_convenio` + `leer_convenio` (`buscar_en="traslados"`, `"dietas"`, `"desplazamientos"`, `"clasificación profesional"`, `"ascensos"`) + `vigencia_convenio`.
- **Doctrina sobre cambio de residencia, ius variandi, centros itinerantes, carácter colectivo del traslado (umbral y cómputo), dietas, funciones inferiores y ascenso** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; los TSJ con `base="AN"`, `tipo_organo="TSJ"` y `provincia` con la sede de la Sala) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Método para la demanda** → `guia_escrito` (`escrito="demanda de movilidad geográfica"` o `escrito="demanda de reclamación de categoría o grupo profesional"`, `jurisdiccion="laboral"`). No hay guía específica de movilidad geográfica: la herramienta devuelve las reglas comunes del orden social, que dicen que hay que conciliar antes y que agosto es inhábil. En la demanda del art. 138 LRJS no rige ninguna de las dos (arts. 64.1 y 43.4 LRJS, leídos): prevalece esta skill, y también el formato del plugin (márgenes de 3 cm, hechos en ordinales «PRIMERO.-») y la puerta (nada de marcadores «[VERIFICAR]»).
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

Pregunta primero **a quién defiende el abogado**. La empresa quiere una decisión con causa, preaviso y compensación correctos; el trabajador quiere saber si puede negarse, irse con indemnización, impugnar o reclamar la categoría superior.

Clasifica el caso antes de seguir, porque cada figura tiene su régimen y su plazo:

| Situación | Figura | Régimen |
|---|---|---|
| Cambio a otro centro que **exige cambio de residencia**, definitivo | Traslado | art. 40.1 ET (individual) o 40.2 (colectivo) |
| Estancia temporal en otra población que exige residir fuera | Desplazamiento | art. 40.6 ET |
| Desplazamientos que superan doce meses en tres años | Traslado | art. 40.6 ET, último párrafo |
| Cambio de centro **sin** cambio de residencia | No es art. 40: ius variandi o, si es sustancial, `modificacion-sustancial-condiciones` | procedimiento ordinario salvo modificación sustancial |
| Trabajador contratado para centros móviles o itinerantes | No es traslado del art. 40.1 | contrato y convenio |
| Víctima de violencia de género, sexual o terrorismo, o persona con discapacidad que necesita tratamiento en otra localidad | Traslado preferente a instancia del trabajador | art. 40.4 y 40.5 ET |
| Funciones del mismo grupo profesional | Movilidad funcional ordinaria | art. 39.1 ET y art. 22 ET |
| Funciones superiores o inferiores fuera del grupo, temporales, con razones técnicas u organizativas | Movilidad funcional extraordinaria | art. 39.2 y 39.3 ET |
| Cambio de funciones fuera de esos supuestos | Modificación sustancial | art. 39.4 ET → `modificacion-sustancial-condiciones` |
| Funciones superiores desde el inicio de la relación | Clasificación profesional | art. 137 LRJS y diferencias (`reclamacion-cantidad`) |

Otras derivaciones: si el trabajador quiere irse con la indemnización del despido porque la empresa no le repone tras una sentencia, `extincion-contrato-trabajador`; si hay que fijar el convenio, `convenio-aplicable`; si la medida esconde represalia o discriminación, se acumula la tutela en la demanda de esta skill (art. 184 LRJS) o, sin decisión de movilidad, `tutela-derechos-fundamentales`.

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende y qué necesita (carta, procedimiento colectivo, estrategia, demanda, carta de opción, reclamación de ascenso).
2. ★ Centro de origen y de destino (localidad y distancia), domicilio del trabajador y si el cambio le obliga a mudarse; duración prevista; si el contrato preveía centros móviles o itinerantes.
3. ★ Causa económica, técnica, organizativa o productiva, o contratación referida a la actividad (traslado y desplazamiento), o razones técnicas u organizativas (movilidad funcional), con documentos.
4. ★ Plantilla de la empresa y del centro, personas trasladadas en los noventa días anteriores y si el traslado afecta al centro entero; representación legal.
5. ★ Fechas: notificación escrita, efectividad y, en desplazamientos, fechas de ida, vuelta y desplazamientos anteriores de los tres últimos años.
6. ★ Convenio aplicable y lo que dice sobre compensación, dietas, kilometraje, grupos profesionales y ascensos.
7. ★ Para la movilidad funcional: grupo profesional del contrato, funciones que realiza de verdad y desde cuándo (días por año, con prueba), retribución de las funciones superiores según convenio, titulación exigida.
8. ★ Situaciones protegidas: representante legal (prioridad de permanencia), cónyuge en la misma empresa, víctima, discapacidad, conciliación, embarazo.
9. Salario real y antigüedad (nóminas de doce meses) si se valora extinguir.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

**Traslado individual (art. 40.1 ET):**

- Requiere razones económicas, técnicas, organizativas o de producción, o contrataciones referidas a la actividad empresarial, y notificación al trabajador **y** a sus representantes con treinta días de antelación a la efectividad.
- El trabajador opta: trasladarse con compensación por gastos propios y de los familiares a su cargo (lo pactado, nunca por debajo del convenio) o extinguir con veinte días de salario por año, prorrateo por meses y máximo de doce mensualidades. Si el convenio no regula la compensación por traslado, dilo así (no hay mínimo convencional y la cifra se negocia) y no la confundas con las dietas o el kilometraje de los desplazamientos puntuales. Puede además impugnar sin optar por extinguir; la decisión es ejecutiva en el plazo de incorporación.
- Traslados en periodos sucesivos de noventa días por debajo del umbral colectivo, sin causas nuevas, para eludir las consultas: fraude de ley y nulidad.

**Traslado colectivo (art. 40.2 ET):** periodo de consultas de hasta quince días si afecta a la totalidad de un centro de más de cinco trabajadores, o si en noventa días alcanza diez trabajadores (menos de cien), el diez por ciento (entre cien y trescientos) o treinta (más de trescientos). Interlocutores y comisión representativa como en el art. 41.4 ET (siete días para constituirla, quince si algún centro no tiene representación). La apertura y las posiciones finales se notifican a la autoridad laboral para su conocimiento. Acuerdo por mayoría; aun con acuerdo, cada trabajador conserva la opción de extinguir. Impugnación por conflicto colectivo, que paraliza las individuales. Cabe sustituir las consultas por mediación o arbitraje.

**Preferencias (art. 40.3, 40.4, 40.5 y 40.7 ET):** derecho del cónyuge que trabaje en la misma empresa a ser trasladado a la misma localidad si hay puesto; traslado preferente de víctimas y de personas con discapacidad (reserva de seis a doce meses y opción final, incluida la extinción con veinte días por año y máximo de doce mensualidades); prioridad de permanencia de los representantes legales y de los colectivos que fije el convenio o el acuerdo.

**Desplazamiento (art. 40.6 ET):** mismas causas; salarios más gastos de viaje y dietas; información con antelación suficiente, no inferior a cinco días laborables si dura más de tres meses; en ese caso, cuatro días laborables de permiso en el domicilio de origen por cada tres meses, sin contar los de viaje, a cargo de la empresa. Se impugna como el traslado. Más de doce meses en tres años: se trata como traslado a todos los efectos. Lee en el convenio las dietas y el kilometraje: la Sala Cuarta ha limitado su devengo a desplazamientos temporales cuando el nuevo lugar se ha convertido en habitual.

**Cambio de centro sin cambio de residencia:** fuera del art. 40. La Sala Cuarta lo ha tratado como ius variandi en distancias que no obligan a mudarse; si el cambio es de entidad (tiempos de desplazamiento, horario, costes), valora la modificación sustancial. Lee en el convenio los pluses de distancia o transporte y las compensaciones. La impugnación de una medida no sustancial va por el procedimiento ordinario.

**Movilidad funcional (art. 39 ET):**

- Dentro del grupo profesional: poder de dirección, con respeto a la titulación exigida y a la dignidad (art. 39.1 ET; el grupo, art. 22 ET y convenio).
- Fuera del grupo (superiores o inferiores): solo con razones técnicas u organizativas y por el tiempo imprescindible; la empresa comunica la decisión y sus razones a los representantes (art. 39.2 ET).
- Retribución: la de las funciones que efectivamente se realizan; en las inferiores se mantiene la de origen. No cabe despido objetivo por ineptitud sobrevenida o falta de adaptación derivadas de funciones distintas asignadas por movilidad (art. 39.3 ET).
- Funciones superiores más de seis meses en un año u ocho en dos: el trabajador puede reclamar el ascenso si el convenio no lo impide, o la cobertura de la vacante según las reglas de ascenso (art. 24 ET y convenio), además de las diferencias salariales; acciones acumulables, previo informe del comité o de los delegados; el convenio puede fijar otros periodos (art. 39.2 ET). La Sala Cuarta ha precisado cómo se computa ese tiempo (días efectivos de funciones superiores sobre los de actividad): búscalo antes de afirmar que se alcanza el periodo.
- Si las funciones superiores se ejercen desde el inicio, la vía es la reclamación de categoría o grupo (art. 137 LRJS: informe del comité, o prueba de haberlo pedido, e informe de la Inspección; acumulable la diferencia salarial). En el sector público, la Sala Cuarta niega la consolidación de la categoría cuando el convenio exige proceso selectivo, aunque se deban las diferencias.
- Cambio de funciones no incluido en estos supuestos: acuerdo o reglas de la modificación sustancial (art. 39.4 ET).

**Plazos y proceso:**

| Acción | Plazo | Proceso | Recurso |
|---|---|---|---|
| Impugnar traslado o desplazamiento | 20 días hábiles de caducidad desde el día siguiente a la notificación escrita, tras las consultas si las hubo; agosto hábil; excluye las fiestas nacionales y autonómicas (relación anual de fiestas laborales publicada en el BOE) y las locales del lugar del órgano (diario oficial de la comunidad), comprobadas en internet con su enlace | art. 138 LRJS, sin conciliación previa (arts. 59.4 ET, 64.1 y 43.4 LRJS) | solo en el traslado colectivo del art. 40.2 (arts. 138.6 y 191.2.e LRJS); si la empresa presentó como individuales traslados que superan el umbral, el carácter colectivo que se alega decide también si hay recurso |
| Extinguir por traslado | Tras la notificación; si una sentencia declara justificado el traslado, quince días | arts. 40.1 ET y 138.7 LRJS | — |
| Movilidad funcional (orden, funciones inferiores) | Prescripción de un año | ordinario con conciliación previa (arts. 59.1 ET y 63 LRJS) | no, salvo acumulación de otra acción recurrible (art. 191.2.e LRJS) |
| Ascenso o categoría y diferencias | Prescripción de un año de cada diferencia | art. 137 LRJS con conciliación previa | solo si las diferencias alcanzan la cuantía de suplicación (art. 137.3 LRJS) |

La sentencia del art. 138 declara la medida justificada, injustificada (reincorporación al centro de origen y daños y perjuicios) o nula (fraude eludiendo las consultas, discriminación, vulneración de derechos fundamentales o supuestos del art. 108.2 LRJS). Si la empresa no repone, ejecución y extinción por la letra c) del art. 50.1 ET (art. 138.8 LRJS).

## Estrategia y jurisprudencia

1. **Empresa**: acredita la causa con documentos y su conexión con la persona elegida (criterios de selección objetivos); respeta preavisos y prioridades; ofrece una compensación de gastos que cubra al menos el convenio; en desplazamientos, fija duración, dietas y regreso; en movilidad funcional, limita el tiempo y deja constancia de las razones y de la comunicación a los representantes.
2. **Trabajador**: calcula el plazo el primer día; comprueba cambio de residencia, preaviso, causa, umbral colectivo y compensación (si hay indicios de que el umbral se supera, reúne las cartas de los demás trasladados y pide en la demanda que la empresa aporte todas las decisiones de traslado de los noventa días y la relación nominal de su plantilla, con el apercibimiento del art. 94.2 LRJS; valora con los representantes si impugnan por conflicto colectivo, que suspende el proceso individual, art. 138.4 LRJS); compara extinguir (20 días por año, tope de doce mensualidades) con impugnar; en funciones superiores, reúne prueba de días y funciones y pide el informe del comité antes de demandar.
3. Consultas en Jurisprudenciator (reformula como máximo dos veces si no hay resultados útiles):
   - Cambio de residencia e ius variandi: `buscar_sentencias` (`consulta="cambio de centro de trabajo sin cambio de residencia ius variandi"`, `base="TS"`, `jurisdiccion="SOCIAL"`) y `consulta="movilidad geográfica traslado cambio de residencia distancia"`.
   - Centros itinerantes: `consulta="centros de trabajo móviles o itinerantes traslado artículo 40"`, `base="TS"`.
   - Carácter colectivo del traslado y cómputo del umbral: `consulta="carácter colectivo o individual número de trabajadores afectados umbrales ámbito de cómputo empresa o centro de trabajo movilidad geográfica modificación sustancial"`, `base="TS"`, y `consulta="movilidad geográfica traslado colectivo sin periodo de consultas nulidad artículo 40.2 trabajadores afectados"`. Los traslados individuales no llegan casi nunca a la Sala Cuarta (no hay recurso), así que la doctrina sobre umbrales suele estar en sentencias de modificación sustancial, que comparte la misma escala: léela y comprueba que el fundamento se refiere también a la movilidad geográfica antes de citarlo para un traslado.
   - Dietas y desplazamiento: `consulta="dietas kilometraje desplazamiento temporal lugar habitual"`, `base="TS"`.
   - Funciones inferiores y dignidad: `consulta="movilidad funcional funciones inferiores grupo profesional dignidad"`, `base="TS"`.
   - Ascenso: `consulta="ascenso funciones superiores artículo 39.2 cómputo tiempo"` y `consulta="clasificación profesional funciones superiores desde el inicio diferencias retributivas"`, `base="TS"`; sector público: `consulta="personal laboral administración funciones superiores no consolida categoría proceso selectivo"`.
   - Doctrina reciente de la Sala del territorio: las mismas consultas con `base="AN"`, `tipo_organo="TSJ"`, `provincia` de la sede, `anios=3`.
4. Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que vayas a citar; transcribe fundamentos, nunca hechos ni datos de aquel pleito. En las cartas no va jurisprudencia: va en la nota.

## Documentos que se entregan

Todos en Word según `references/formato-y-organos-laboral.md`.

**Posición de la empresa:**

1. Carta de traslado (`carta-traslado-<apellido-trabajador>-<AAAAMMDD>.docx`): membrete; destinatario; asunto; centro de origen y de destino; causa concreta con datos y conexión con la persona; fecha de efectividad con al menos treinta días de antelación; compensación de gastos con sus conceptos e importes (mínimo del convenio con su artículo); información de las opciones legales; firma, recibí o constancia de la negativa, copia a la representación.
2. Carta de desplazamiento (`carta-desplazamiento-<apellido-trabajador>-<AAAAMMDD>.docx`): destino, causa, duración y fechas, salarios, gastos de viaje y dietas (convenio), antelación, permisos de cuatro días laborables por cada tres meses si supera ese plazo, y cómputo de desplazamientos de los tres últimos años.
3. Comunicación de movilidad funcional (`carta-movilidad-funcional-<apellido-trabajador>-<AAAAMMDD>.docx`): funciones nuevas y grupo, razones técnicas u organizativas, duración imprescindible, retribución aplicable, y comunicación a los representantes.
4. Traslado colectivo: comunicación de intención, inicio de consultas con memoria causal, actas, notificación a la autoridad laboral de la apertura y de las posiciones finales, y notificaciones individuales.
5. Nota para el abogado (`nota-movilidad-<empresa>-<AAAAMMDD>.docx`): calificación de la medida, umbral en tabla, calendario, riesgos (nulidad, prioridad de permanencia, víctimas, conciliación), artículos del ET y del convenio leídos, doctrina literal si existe.

**Posición del trabajador:**

1. Nota de estrategia (`nota-movilidad-<apellido-trabajador>-<AAAAMMDD>.docx`) con opciones, plazos (fecha inicial, precepto, fecha final) y recomendación.
2. Demanda por el art. 138 LRJS contra traslado o desplazamiento (`demanda-movilidad-geografica-<apellido-trabajador>-<AAAAMMDD>.docx`), al Tribunal de Instancia, Sección de lo Social: hechos, fundamentos (plazo, calificación, procedimiento, causa, nulidad acumulando la tutela si procede y citando al Ministerio Fiscal), súplica de nulidad o injustificación con reincorporación y daños, otrosíes de prueba. Sin papeleta previa.
3. Carta de opción por la extinción del art. 40.1 ET y cálculo: salario anual real, salario diario (anual / 365), antigüedad con prorrateo por meses, 20 días por año, tope de doce mensualidades y resultado, cada operación visible.
4. Reclamación de ascenso o de categoría: solicitud del informe al comité o a los delegados; papeleta con `papeleta-conciliacion`; demanda del art. 137 LRJS (`demanda-categoria-<apellido-trabajador>-<AAAAMMDD>.docx`) con cuadro de días de funciones superiores y diferencias por mes (tabla salarial del año buscada en internet en el boletín oficial que indique `vigencia_convenio` y citada con su enlace, o aportada por el abogado; sin tabla no se calculan diferencias, apartado 3 de las anclas).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado, ni en Jurisprudenciator ni en internet.
- [ ] Todo dato que no sale de Jurisprudenciator (orden de cotización, tabla salarial, criterio técnico, nombre de un órgano, sede electrónica) lleva su enlace oficial y la fecha de consulta, y el resumen lo identifica.
- [ ] Leídos con `buscar_articulo` en esta conversación: ET 22, 24, 39, 40, 41, 50 y 59 (los usados); LRJS 43, 63, 64, 137, 138, 153 y 191, y en la demanda 10 (competencia territorial) y 94 (aportación de documentos por la empresa).
- [ ] Medida clasificada con la tabla de «Cuándo usarla» (traslado, desplazamiento, cambio sin residencia, funcional ordinaria o extraordinaria, clasificación) y modalidad procesal justificada.
- [ ] Umbral colectivo calculado con la plantilla y los traslados de los noventa días.
- [ ] Convenio leído con `leer_convenio` y vigencia comprobada (compensación, dietas, grupos, ascensos).
- [ ] Plazo con fecha de notificación escrita, precepto y fecha final; agosto hábil en la impugnación del art. 138; fiestas nacionales, autonómicas y locales del año comprobadas en fuente oficial con su enlace.
- [ ] Cálculo de la indemnización visible con el tope de doce mensualidades.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`; ninguna jurisprudencia en las cartas.
- [ ] `verificar_escrito` pasado sobre cada documento; los avisos de «posible disonancia» contrastados con el apartado exacto leído.
- [ ] Marcadores en lugar de datos no facilitados (`[CENTRO DE TRABAJO]`, `[CATEGORÍA/GRUPO PROFESIONAL]`, `[SALARIO BRUTO ANUAL]`).
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado y ante qué órgano; plazo; cálculos; riesgos y documentos que faltan; tabla de jurisprudencia; próximo paso.
