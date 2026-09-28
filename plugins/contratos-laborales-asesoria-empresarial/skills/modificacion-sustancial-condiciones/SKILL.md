---
name: modificacion-sustancial-condiciones
description: >-
  Modificación sustancial de condiciones de trabajo (art. 41 ET) para las dos partes. Para la empresa:
  causa, carácter individual o colectivo según los umbrales de noventa días, preaviso de quince días,
  periodo de consultas y carta de comunicación que aguante. Para el trabajador: aceptar, impugnar en
  20 días hábiles por el art. 138 LRJS, rescindir con 20 días por año (art. 41.3 ET) o extinguir por
  el art. 50.1.a) ET si hay menoscabo de la dignidad. Distingue la modificación sustancial del ius
  variandi y de la inaplicación del convenio (art. 82.3 ET). Úsala con «cambio de horario», «bajan el
  sueldo», «quitan el plus», «nuevo sistema de turnos», «me cambian las condiciones». Para traslados
  y cambios de funciones, movilidad-geografica-funcional; para ERTE, erte-suspension-reduccion.
---

# Modificación sustancial de condiciones de trabajo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Concepto, causas, umbrales, preaviso, periodo de consultas y opción de rescindir** → `buscar_articulo` (`ley="ET"`, artículos `"41"`, `"39"` y `"40"` para deslindar la movilidad, y `"64"` para los derechos de información de la representación).
- **Inaplicación del convenio** → `buscar_articulo` (`ley="ET"`, artículos `"82"` —apartado 3— y `"87"`, legitimación para negociarla).
- **Acción del trabajador, plazo y recursos** → `buscar_articulo` (`ley="ET"`, artículos `"50"` y `"59"`) y (`ley="LRJS"`, artículos `"43"`, `"64"`, `"108"`, `"138"`, `"153"`, `"184"` y `"191"`).
- **Infracción administrativa por imponer la modificación sin procedimiento** → `buscar_articulo` (`ley="BOE-A-2000-15060"`, artículos `"7"` —apartado 6—, `"39"` y `"40"`).
- **Convenio aplicable, la condición que se quiere cambiar y los procedimientos que añada** → `buscar_convenio` + `leer_convenio` (`buscar_en="modificación sustancial"`, `"jornada"`, `"horario"`, `"turnos"` o el concepto salarial afectado; `articulo` concreto cuando lo conozcas) + `vigencia_convenio`.
- **Doctrina sobre carácter sustancial, caducidad, modalidad procesal, rescisión y consultas** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; los TSJ con `base="AN"`, `tipo_organo="TSJ"` y `provincia` con la sede de la Sala) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Método para la demanda o el conflicto colectivo** → `guia_escrito` (`escrito="demanda de modificación sustancial de condiciones de trabajo"` o `escrito="conflicto-colectivo"`, `jurisdiccion="laboral"`).
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

Pregunta primero **a quién defiende el abogado**. La empresa quiere una decisión y una carta que resistan la impugnación; el trabajador quiere saber si la medida es sustancial, si se ha seguido el procedimiento, si hay causa y qué opción le conviene antes de que caduque el plazo.

- Cambios de jornada, horario, distribución del tiempo de trabajo, turnos, sistema de remuneración o cuantía salarial, sistema de trabajo y rendimiento, o funciones fuera de los límites del art. 39 ET.
- Supresión de una condición más beneficiosa o de un pacto de empresa no estatutario.
- Revisión de una comunicación ya recibida o de un periodo de consultas en marcha.

| Situación | Skill que procede |
|---|---|
| Cambio de centro que exige cambio de residencia, o desplazamiento temporal | `movilidad-geografica-funcional` |
| Cambio de funciones dentro del grupo profesional o funciones superiores o inferiores temporales | `movilidad-geografica-funcional` (art. 39 ET); solo si excede sus límites, esta skill |
| Suspensión de contratos o reducción de jornada por causas ETOP o fuerza mayor | `erte-suspension-reduccion` |
| La condición está en un convenio estatutario (sectorial o de empresa) | Esta skill, pero por el procedimiento del art. 82.3 ET (inaplicación), no del art. 41 |
| Cambio de convenio o de condiciones tras una sucesión de empresa | `sucesion-empresa-contratas` |
| El trabajador quiere irse con la indemnización del despido improcedente (art. 50 ET) | `extincion-contrato-trabajador` |
| La medida esconde una represalia o discriminación y la relación sigue | Esta skill por el art. 138 LRJS acumulando la tutela (art. 184 LRJS); `tutela-derechos-fundamentales` solo si no hay decisión modificativa |
| Hay que determinar el convenio aplicable | `convenio-aplicable` |
| Hay que cuantificar la indemnización del art. 41.3 ET con hoja de cálculo | `calculo-indemnizacion-despido` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende y qué necesita (carta individual, procedimiento colectivo, estrategia, demanda, carta de rescisión).
2. ★ Condición actual y condición nueva, con cifras: horario de entrada y salida, jornada, turnos, conceptos salariales y su importe, sistema de rendimiento. Origen de la condición actual: contrato, convenio estatutario (con su artículo), pacto colectivo no estatutario, decisión unilateral de efectos colectivos o práctica consolidada.
3. ★ Causa económica, técnica, organizativa o productiva y los documentos que la prueban (cuentas, pérdidas, cambios en la demanda, nuevos sistemas, pérdida de clientes).
4. ★ Plantilla de la **empresa** (no del centro) y número de personas afectadas en los últimos noventa días, contando modificaciones anteriores del mismo periodo; centros afectados y representación legal de cada uno.
5. ★ Fechas: notificación (o fecha prevista), efectividad, inicio y fin del periodo de consultas y forma de notificación (escrita, individual, a la representación). Sin fecha de notificación escrita no se da plazo.
6. ★ Circunstancias protegidas de las personas afectadas: reducción de jornada o adaptación por conciliación, embarazo, representantes, víctimas de violencia, discapacidad.
7. ★ Convenio aplicable (actividad y territorio del centro) y antigüedad y salario real de quien valore rescindir (nóminas de los doce últimos meses).
8. Para el trabajador: perjuicio concreto que le causa (económico, familiar, de salud) y si ya ha actuado (firma «no conforme», reclamación, papeleta).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

**¿Es sustancial?**

- La lista del art. 41.1 ET es abierta («entre otras»): jornada, horario y distribución del tiempo, turnos, sistema de remuneración y cuantía salarial, sistema de trabajo y rendimiento, y funciones que excedan el art. 39 ET.
- La Sala Cuarta distingue la modificación sustancial, que altera y transforma aspectos fundamentales de la relación de modo notorio, de la accidental, que es ius variandi. Valora la importancia cualitativa del cambio, su alcance temporal y las compensaciones. Deja escrito el juicio en la nota con la doctrina leída.
- Consecuencia procesal: si la medida es discutiblemente no sustancial, o si lo que se reclama es la existencia de un derecho (condición más beneficiosa, lo que dice el convenio, un imperativo legal), la vía es el **procedimiento ordinario**, no la modalidad del art. 138 LRJS. Elige la modalidad antes de redactar: un error de modalidad cierra el recurso o obliga a reconducir.

**¿Individual o colectiva? (art. 41.2 ET)**

- Colectiva si en noventa días afecta al menos a diez trabajadores (empresas de menos de cien), al diez por ciento (entre cien y trescientos) o a treinta (más de trescientos). Por debajo, individual.
- Encadenar modificaciones en periodos sucesivos de noventa días por debajo del umbral, sin causas nuevas, para eludir las consultas: fraude de ley con nulidad (art. 41.3 ET, último párrafo).
- La condición contenida en un convenio estatutario no se modifica por el art. 41: se inaplica por el art. 82.3 ET (art. 41.6 ET).

**Procedimiento individual:** notificación escrita al trabajador **y** a sus representantes legales con quince días de antelación a la efectividad (art. 41.3 ET). La medida es ejecutiva en esa fecha aunque se impugne.

**Procedimiento colectivo (art. 41.4 y 41.5 ET):**

- Comunicación fehaciente de la intención de iniciar el procedimiento para que se constituya la comisión representativa (siete días, o quince si algún centro afectado no tiene representación); después, comunicación de inicio del periodo de consultas.
- Interlocutores en el orden del art. 41.4: secciones sindicales con mayoría en los órganos unitarios si así lo acuerdan; si no, comité o delegados del centro; sin representación, comisión de hasta tres trabajadores elegida democráticamente o comisión sindical; varios centros, comité intercentros con esa función o comisión representativa. Máximo trece miembros por parte.
- Consultas de hasta quince días sobre causas, posibilidad de evitar o reducir efectos y medidas para atenuarlos, negociando de buena fe; acuerdo por mayoría de los representantes que represente a la mayoría de la plantilla afectada. Con acuerdo se presume la causa y solo cabe impugnar por fraude, dolo, coacción o abuso de derecho. Cabe sustituir las consultas por mediación o arbitraje dentro del mismo plazo.
- Sin acuerdo: la empresa notifica la decisión a los trabajadores y surte efecto a los siete días (art. 41.5 ET). Impugnación por conflicto colectivo (art. 153 LRJS), que paraliza las acciones individuales.
- Lee en el convenio (`leer_convenio`, `buscar_en="modificación sustancial"`) si establece un procedimiento específico o preavisos mayores (art. 41.4 ET, inciso inicial).

**Inaplicación del convenio (art. 82.3 ET):** causas definidas en el propio artículo (económicas con la regla de los dos trimestres; técnicas, organizativas, productivas); materias de las letras a) a g), que incluyen las mejoras voluntarias de Seguridad Social; acuerdo con los representantes legitimados para negociar un convenio (art. 87.1 ET) tras consultas del art. 41.4; el acuerdo fija las nuevas condiciones y su duración, que no puede ir más allá del nuevo convenio, no puede incumplir las obligaciones de igualdad y se notifica a la comisión paritaria; sin acuerdo, comisión paritaria (siete días), procedimientos de los acuerdos interprofesionales y, en su defecto, Comisión Consultiva Nacional de Convenios Colectivos u órgano autonómico (veinticinco días; el nombre del órgano autonómico, búscalo en internet en la sede oficial de la comunidad y cita el enlace); resultado comunicado a la autoridad laboral a efectos de depósito.

**Opciones del trabajador:**

| Opción | Requisito y plazo | Precepto |
|---|---|---|
| Aceptar | Conviene firmar «recibí, no conforme» si se reserva impugnar | — |
| Impugnar | 20 días hábiles de caducidad desde el día siguiente a la notificación escrita de la decisión, tras las consultas si las hubo; no corre sin notificación escrita; sin conciliación previa; agosto hábil | arts. 59.4 ET, 138.1, 64.1 y 43.4 LRJS |
| Rescindir con indemnización | Modificación de las letras a), b), c), d) o f) del art. 41.1 y perjuicio; 20 días de salario por año, prorrateo por meses, máximo nueve mensualidades; tras sentencia que declare justificada la medida, 15 días para optar | arts. 41.3 ET y 138.7 LRJS |
| Extinguir por el art. 50.1.a) | Modificación sin respetar el art. 41 **y** con menoscabo de la dignidad; indemnización del despido improcedente | art. 50 ET → `extincion-contrato-trabajador` |
| Extinguir por el art. 50.1.c) | La empresa no repone tras sentencia que declaró injustificada la medida | arts. 50.1.c ET y 138.8 LRJS |

- La letra e) del art. 41.1 (sistema de trabajo y rendimiento) no da derecho a rescindir con indemnización.
- La rescisión del art. 41.3 no necesita resolución judicial; si la empresa la discute, se reclama la indemnización en el procedimiento ordinario. Busca la doctrina sobre qué ocurre si la empresa deja sin efecto la medida antes de su efectividad (ver «Estrategia») antes de aconsejar rescindir.
- Sentencia (art. 138.7 LRJS): justificada; injustificada con reposición y daños y perjuicios; nula si se eludieron las consultas en fraude de ley, si hay móvil discriminatorio, vulneración de derechos fundamentales o alguno de los supuestos del art. 108.2 LRJS. Recurso solo en las colectivas (arts. 138.6 y 191.2.e LRJS): advierte al cliente de que en la individual la instancia es única.
- Imponer la modificación sin acudir a los arts. 41 u 82.3 ET es infracción grave (apartado 6 del artículo 7 del Real Decreto Legislativo 5/2000); cuantía en su art. 40, leída en el momento.

**Riesgos de nulidad que la empresa debe descartar y el trabajador debe buscar:** afectados con reducción de jornada o adaptación por conciliación (el cambio de horario puede ser discriminación indirecta), embarazo o maternidad reciente, representantes, represalia tras una reclamación (garantía de indemnidad), umbral colectivo eludido.

## Estrategia y jurisprudencia

1. **Empresa**: prueba primero que la causa existe y conecta con la medida (documentos, no afirmaciones); calcula el umbral con la plantilla de la empresa y todas las medidas de los noventa días; elige el procedimiento (individual, colectivo, art. 82.3); prepara la carta con la condición anterior y la nueva en cifras, la causa concreta y la fecha de efectos; entrega la notificación por escrito a cada afectado y a la representación, con acuse. Si hay afectados en situación protegida, justifica por qué la medida les alcanza o exclúyelos.
2. **Trabajador**: calcula el plazo el primer día; comprueba si la medida es sustancial, si el procedimiento se siguió (preaviso, representación, umbral), si la causa está probada y si hay vulneración de derechos fundamentales; decide entre impugnar y rescindir con el cliente según su perjuicio y su interés en seguir.
3. Consultas en Jurisprudenciator (reformula como máximo dos veces si no hay resultados útiles):
   - Sustancial o accidental: `buscar_sentencias` (`consulta="modificación sustancial ius variandi alteración aspectos fundamentales de la relación laboral"`, `base="TS"`, `jurisdiccion="SOCIAL"`) y la misma con la materia del caso (`"modificación sustancial horario"`, `"modificación sustancial supresión plus"`).
   - Caducidad y notificación: `consulta="caducidad modificación sustancial notificación escrita expresa dies a quo"`, `base="TS"`.
   - Modalidad procesal: `consulta="modificación no sustancial procedimiento ordinario modalidad procesal artículo 138"`, `base="TS"`.
   - Condición más beneficiosa: `consulta="condición más beneficiosa supresión modificación sustancial artículo 41"`, `base="TS"`.
   - Rescisión: `consulta="rescisión del contrato artículo 41.3 perjuicio modificación sustancial"`, `base="TS"`.
   - Colectiva y consultas: `consulta="modificación sustancial colectiva periodo de consultas buena fe nulidad"` y `consulta="inaplicación convenio colectivo artículo 82.3 causas periodo de consultas"`, `base="TS"`.
   - Conciliación y discriminación: `consulta="modificación sustancial horario reducción de jornada guarda legal discriminación"`, `base="AN"`, `tipo_organo="TSJ"`, `anios=3`.
4. Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que vayas a citar y transcribe fundamentos, nunca los hechos ni los datos de aquel pleito. En la carta de la empresa no va jurisprudencia: va en la nota.

## Documentos que se entregan

Todos en Word según `references/formato-y-organos-laboral.md`.

**Posición de la empresa:**

1. Carta individual (`carta-modificacion-sustancial-<apellido-trabajador>-<AAAAMMDD>.docx`): membrete con `[DENOMINACIÓN SOCIAL]` y `[CIF]`; destinatario; asunto; condición actual y nueva en cifras; causa concreta con los datos y documentos que la acreditan y su conexión con la medida; carácter individual (y por qué no se alcanza el umbral); fecha de efectividad con al menos quince días de antelación; información en términos condicionales de las opciones legales («si considera que la modificación le perjudica…»), sin reconocer perjuicio ni ofrecer indemnización pactada salvo que la empresa lo decida; firma; recibí con fecha o constancia de la negativa ante testigos; copia a la representación legal.
2. Procedimiento colectivo: comunicación de la intención de iniciar el procedimiento; comunicación de inicio del periodo de consultas con memoria de las causas y documentación; modelo de acta de cada reunión; notificación final a cada trabajador (con o sin acuerdo) con la fecha de efectos.
3. Nota para el abogado (`nota-modificacion-sustancial-<empresa>-<AAAAMMDD>.docx`): calificación (sustancial, individual o colectiva, art. 41 u 82.3), cómputo del umbral en tabla, causa y prueba, calendario con fechas, riesgos de nulidad detectados, artículos del ET y del convenio leídos y doctrina literal si existe.

**Posición del trabajador:**

1. Nota de estrategia (`nota-modificacion-sustancial-<apellido-trabajador>-<AAAAMMDD>.docx`): calificación, defectos de procedimiento, causa, opciones en tabla con su plazo (fecha inicial, precepto, fecha final) y recomendación.
2. Demanda por el art. 138 LRJS (`demanda-modificacion-sustancial-<apellido-trabajador>-<AAAAMMDD>.docx`), dirigida al Tribunal de Instancia, Sección de lo Social (apartado 3 del formato; competencia territorial del art. 10 LRJS): hechos (relación laboral, condición anterior, notificación y su fecha, medida, perjuicio, circunstancias protegidas); fundamentos (plazo; carácter sustancial; individual o colectiva y procedimiento incumplido; falta de causa; nulidad si procede, acumulando la tutela con el art. 184 LRJS y citando al Ministerio Fiscal); súplica (nulidad o, subsidiariamente, injustificación con reposición en las condiciones anteriores y daños y perjuicios); otrosíes de prueba, incluida la petición de informe de la Inspección del art. 138.3 LRJS si conviene. Sin papeleta previa (art. 64.1 LRJS). Si la vía es el procedimiento ordinario, dilo y usa `papeleta-conciliacion`.
3. Carta de rescisión del art. 41.3 ET y hoja de cálculo de la indemnización: salario anual real, salario diario (anual / 365), antigüedad en años y meses (prorrateo por meses), 20 días por año, tope de nueve mensualidades y resultado, con cada operación visible (apartado 7 del formato).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado, ni en Jurisprudenciator ni en internet.
- [ ] Todo dato que no sale de Jurisprudenciator (orden de cotización, tabla salarial, criterio técnico, nombre de un órgano, sede electrónica) lleva su enlace oficial y la fecha de consulta, y el resumen lo identifica.
- [ ] Leídos con `buscar_articulo` en esta conversación: ET 39, 40, 41, 50, 59, 64, 82 y 87 (los usados); LRJS 43, 64, 108, 138, 153, 184 y 191; Real Decreto Legislativo 5/2000 arts. 7 y 40 si se menciona la infracción.
- [ ] Calificada la medida (sustancial o accidental, individual o colectiva, art. 41 o art. 82.3) con doctrina leída; modalidad procesal elegida y justificada.
- [ ] Umbral de noventa días calculado con la plantilla de la empresa y las medidas anteriores.
- [ ] Convenio leído con `leer_convenio` y vigencia comprobada con `vigencia_convenio` si la condición o el procedimiento dependen de él.
- [ ] Plazo con fecha de notificación escrita, precepto y fecha final; agosto contado como hábil conforme al art. 43.4 LRJS.
- [ ] Cálculo de la indemnización del art. 41.3 visible y con el tope de nueve mensualidades.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`; ninguna jurisprudencia en la carta.
- [ ] `verificar_escrito` pasado sobre cada documento; los avisos de «posible disonancia» contrastados con el apartado exacto leído.
- [ ] Marcadores en lugar de datos no facilitados.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado, para quién y ante qué órgano; plazo; cálculos; riesgos y documentos que faltan; tabla de jurisprudencia; próximo paso.
