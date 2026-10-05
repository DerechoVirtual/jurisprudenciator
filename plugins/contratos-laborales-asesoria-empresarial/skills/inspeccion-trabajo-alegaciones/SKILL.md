---
name: inspeccion-trabajo-alegaciones
description: >-
  Prepara la respuesta de la empresa a la Inspección de Trabajo: comparecencia y aportación de documentos ante
  un requerimiento, alegaciones contra un acta de infracción o de liquidación de cuotas, decisión de pagar con
  reducción y recurso de alzada contra la resolución sancionadora, con los plazos del Real Decreto 928/1998,
  la Ley 23/2015 y la LISOS. Úsala cuando digan «nos ha llegado un acta», «requerimiento de la Inspección»,
  «citación para comparecer», «alegaciones al acta», «acta de liquidación», «¿pagamos con el 40 %?» o
  «recurso de alzada contra la sanción». Sirve a la empresa y, para valorar su posición de interesados, al
  trabajador o a la representación. Entrega escrito en Word (y nota, si la pides). Si el acta es sobre plan de igualdad o
  registro retributivo, lee también plan-igualdad-registro-retributivo; si es por cesión ilegal o contratas,
  sucesion-empresa-contratas.
---

# Inspección de Trabajo: comparecencia, alegaciones y alzada

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Facultades, deber de colaboración, modalidades y plazo de las actuaciones, medidas y presunción de certeza** → `buscar_articulo` (`ley="BOE-A-2015-8168"`, artículos `"13"`, `"18"`, `"20"`, `"21"`, `"22"` y `"23"`).
- **Contenido del acta, valor probatorio, notificación, alegaciones, instrucción, resolución, caducidad y alzada** → `buscar_articulo` (`ley="Real Decreto 928/1998"`, artículos `"14"`, `"15"`, `"16"`, `"17"`, `"18"`, `"18 bis"`, `"20"`, `"21"`, `"22"` y `"23"`); **actas de liquidación** → artículos `"31"` a `"34"` y (`ley="LGSS"`, artículos `"24"` y `"34"`).
- **Tipo infractor, prescripción, graduación, responsables, concurrencia penal, tramitación y contenido del acta** → `buscar_articulo` (`ley="BOE-A-2000-15060"`, el artículo del tipo que cite el acta y los artículos `"3"`, `"4"`, `"39"`, `"42"`, `"50"`, `"52"` y `"53"`); cuantías, del artículo `"40"` en el momento.
- **Cómputo de plazos y alzada** → `buscar_articulo` (`ley="LPAC"`, artículos `"30"`, `"121"` y `"122"`); vía judicial posterior → (`ley="LRJS"`, artículos `"2"`, `"3"`, `"69"` y `"151"`).
- **La norma sustantiva que el acta dice infringida** (ET, LPRL, LGSS, convenio) → `buscar_articulo` con el valor de `ley` de las anclas y, si es un convenio, `buscar_convenio` + `leer_convenio` + `vigencia_convenio`.
- **Doctrina sobre presunción de certeza, caducidad, plazo de las actuaciones, graduación y non bis in idem** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`; actas de liquidación, `jurisdiccion="CONTENCIOSO"`; TSJ con `base="AN"`, `jurisdiccion="SOCIAL"`, `tipo_organo="TSJ"`) + `leer_sentencias` (`parrafos=3`); estructura del recurso de alzada → `guia_escrito` (`escrito="recurso-alzada-reposicion-ca"`, `jurisdiccion="contencioso"`).
- **Empresa y responsables solidarios** → `buscar_empresa_mercantil`.
- **Revisión del documento antes de entregarlo** → cada redactor pasa `verificar_escrito` sobre las frases de su sección que citan normas (no sobre el documento entero) y el ensamblado de `redaccion-rapida` comprueba que cada ECLI o ROJ citado figure entre las fuentes leídas; `buscar_por_cita` solo para una sentencia que aporte el abogado y no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Identifica primero el documento recibido: cada uno tiene su respuesta y su plazo.

| Documento | Respuesta | Norma |
|---|---|---|
| Diligencia de visita o requerimiento de comparecencia y documentos | Escrito de comparecencia y aportación | Arts. 13.3, 18 y 21 de la Ley 23/2015 |
| Requerimiento de subsanación | Cumplimiento justificado, o escrito que explique por qué no procede | Art. 22.2 de la Ley 23/2015 |
| Acta de infracción | Alegaciones o pago con reducción | Arts. 14 y 17 del Real Decreto 928/1998; art. 52 LISOS |
| Acta de liquidación de cuotas (con o sin acta de infracción por los mismos hechos) | Alegaciones o ingreso | Arts. 31 a 34 del Real Decreto 928/1998; art. 34 LGSS |
| Acta de obstrucción | Alegaciones | Art. 50 LISOS |
| Resolución sancionadora o liquidatoria | Recurso de alzada | Arts. 23 y 33.3 del Real Decreto 928/1998; arts. 121 y 122 LPAC |

Si defiende al trabajador o a la representación: el denunciante no es interesado en la fase de investigación, pero tiene derecho a ser informado del estado de su denuncia cuando afecta a sus derechos; si la denuncia da lugar a procedimiento sancionador puede serlo, y en ese procedimiento lo son los representantes sindicales o de los trabajadores (art. 20.4 de la Ley 23/2015). Las denuncias anónimas no se tramitan (art. 20.5).

Tras agotar la vía administrativa, la impugnación judicial va al orden social si la sanción es laboral o de Seguridad Social (letras n) y s) del art. 2 LRJS; art. 151 LRJS; dos meses del art. 69.2 LRJS) y al contencioso-administrativo si se trata de actas de liquidación y actas de infracción vinculadas a ellas (letra f) del art. 3 LRJS; art. 33.3 del Real Decreto 928/1998). Esta skill deja indicado el plazo y el orden en la nota; la demanda no la redacta.

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ El documento completo (acta, diligencia, requerimiento o resolución) con sus anexos, y **fecha de notificación**; si fue electrónica, la fecha de acceso o de puesta a disposición.
2. ★ Fecha de la primera visita o de la comparecencia con la documentación completa, y fechas de cada actuación posterior (para el plazo de las actuaciones).
3. ★ Fecha del acta y órgano instructor y resolutor que indica (letra f) del art. 14.1 del Real Decreto 928/1998).
4. ★ Tipo infractor citado (artículo y apartado de la LISOS), calificación, grado propuesto, criterios de graduación que dice aplicar, número de trabajadores afectados y sanciones accesorias.
5. ★ Versión de la empresa sobre cada hecho del acta y prueba de que dispone (nóminas, registros de jornada, contratos, comunicaciones, testigos).
6. Si hay acta de liquidación: periodo, trabajadores, bases y conceptos, y si coincide con un acta de infracción.
7. Si hay responsables solidarios o subsidiarios (contratas, grupo, sucesión) y si les han notificado.
8. Actuaciones penales abiertas por los mismos hechos, sanciones previas por los mismos hechos y requerimientos anteriores.
9. Si la empresa quiere pagar para obtener la reducción o prefiere discutir.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y comprueba la redacción que regía en la fecha del acta: el Real Decreto 928/1998 se reformó con efectos de 1 de enero de 2022 y la respuesta de `buscar_articulo` trae la redacción anterior bajo «Téngase en cuenta».

**A. Actuaciones inspectoras (Ley 23/2015)**

- Facultades de los inspectores: entrada, requerimiento de información, comparecencia y examen de documentación, también en soporte electrónico y formato tratable (art. 13). Deber de colaborar, declarar y aportar documentación; quien represente a la empresa acredita su condición (art. 18.1.d). La obstrucción se califica en el art. 50 LISOS: el mero retraso en comparecer o informar es leve salvo que se refiera a documentos que deban estar en el centro durante una visita.
- Modalidades: visita sin aviso, requerimiento de comparecencia o expediente administrativo; diligencia escrita de cada actuación (art. 21.1 y 21.6).
- **Plazo de las actuaciones comprobatorias:** nueve meses, ampliables otros nueve en los supuestos tasados, y sin interrupciones de más de cinco meses, salvo causa imputable a la empresa; se cuenta desde la primera visita o desde la comparecencia con toda la documentación, y no computa el aplazamiento concedido para subsanar (art. 21.4). Busca la doctrina sobre el efecto de superarlo y sobre el día inicial cuando hay orden de servicio.
- Medidas que puede adoptar el inspector: advertencia, requerimiento, acta de infracción o de liquidación, propuestas de recargo, paralización, entre otras (art. 22).
- Criterios técnicos: la Inspección actúa con instrucciones y criterios técnicos vinculantes que se publican (art. 20.2). Si el acta o la materia se apoya en uno, Jurisprudenciator no lo devuelve: búscalo en internet en la web oficial del Organismo Estatal Inspección de Trabajo y Seguridad Social, léelo y cítalo con enlace y fecha de consulta. Igual con la vía de presentación electrónica del escrito: sede electrónica oficial, con enlace.
- **Presunción de certeza** de los hechos constatados que se formalizan en las actas de infracción y liquidación con los requisitos legales, sin perjuicio de la prueba en contrario (art. 23; art. 53.2 LISOS; art. 15 del Real Decreto 928/1998). Busca y lee la doctrina sobre su alcance: hechos percibidos directamente o inmediatamente deducibles, y no juicios de valor, apreciaciones globales ni calificaciones jurídicas.

**B. El acta de infracción y el procedimiento sancionador**

- Contenido obligatorio del acta (art. 14.1 del Real Decreto 928/1998; art. 53.1 LISOS): identificación del sujeto y, en su caso, del responsable solidario o subsidiario con su fundamento; hechos comprobados, medios de comprobación y criterios de graduación; precepto infringido y calificación; trabajadores de la empresa y afectados cuando gradúan o califican; propuesta de sanción y accesorias; órganos y plazo de alegaciones; funcionario y visado; fecha. La resolución **anula el acta** que carezca de los requisitos imprescindibles o cause indefensión no subsanada (art. 20.1).
- Acumulación de infracciones de una misma materia en una sola acta, con excepciones (art. 16).
- Notificación del acta en diez días hábiles desde el término de la actuación (art. 17.1). **Alegaciones en quince días hábiles** desde el siguiente a la notificación, con la prueba, ante el órgano instructor; sin alegaciones, el acta puede ser propuesta de resolución (art. 17.1; art. 52.1.b LISOS). Vista del expediente, salvo la confidencialidad del origen de la denuncia (art. 17.4).
- Instrucción: informe ampliatorio del inspector, **preceptivo** si las alegaciones invocan hechos distintos, insuficiencia del relato fáctico o indefensión; periodo de prueba; audiencia de ocho días y tres más si aparecen hechos distintos (arts. 18 y 18 bis).
- Resolución motivada; **caducidad** si pasan seis meses desde la fecha del acta hasta la notificación de la resolución, descontadas las interrupciones imputables a la empresa y las suspensiones (art. 20.3 en su redacción vigente desde el 1 de enero de 2022; para actas anteriores, lee la redacción previa que muestra `buscar_articulo` y la doctrina sobre el día final).
- **Pago con reducción:** si la sanción propuesta es solo pecuniaria y sin accesorias, pagar antes de la resolución con renuncia a alegaciones y recursos reduce la sanción un cuarenta por ciento e implica reconocer la responsabilidad (arts. 14.1.e, 14.6 y 17.1); el pago se hace y acredita en diez días hábiles desde que se notifican los documentos de pago (art. 18 bis.7); después no cabe alzada (art. 23.1). Con varios responsables, la reducción exige que ninguno alegue (art. 14.6). No se aplica a actas de infracción concurrentes con liquidación, que tienen su propia reducción (art. 34.2).
- **Prescripción** de las infracciones: tres años con carácter general, cuatro en Seguridad Social, y en prevención de riesgos laborales uno, tres o cinco años según su gravedad, desde la fecha de la infracción (art. 4 LISOS); la acción para imponer sanciones de Seguridad Social y liquidar cuotas, cuatro años (art. 24 LGSS).
- **Graduación:** criterios del art. 39.2 LISOS; no pueden usarse los que ya forman parte del tipo (art. 39.5); el acta y la resolución deben explicitar los criterios aplicados y, si ninguno es relevante, la sanción va en grado mínimo y tramo inferior (art. 39.6); la persistencia continuada se sanciona en el máximo (art. 39.7). Cuantías de cada grado: léelas del art. 40 LISOS en el momento.
- **Concurrencia penal:** no se sanciona lo ya sancionado con identidad de sujeto, hecho y fundamento; si hay indicios de delito, se pasa el tanto de culpa y se suspende el procedimiento (art. 3 LISOS; art. 5 del Real Decreto 928/1998; art. 52.3 LISOS).

**C. Actas de liquidación**

- Proceden por falta de alta, diferencias de cotización y derivación de responsabilidad (art. 34.1 LGSS; art. 31 del Real Decreto 928/1998); contenido en el art. 32 (bases, periodos, trabajadores, criterios de imputación en contratas); los hechos consignados gozan de presunción de certeza (art. 32.1.c).
- Alegaciones en quince días desde la notificación ante la Unidad Especializada de Seguridad Social; ingreso antes de vencer ese plazo, que convierte la liquidación en definitiva; audiencia de diez días tras el informe ampliatorio; resolución de la Tesorería con el mismo plazo de seis meses (art. 33.1 y 33.2). Días hábiles por remisión a la LPAC (art. 22 del Real Decreto 928/1998; art. 30.2 LPAC).
- Con acta de infracción por los mismos hechos: tramitación conjunta, y si se ingresa la liquidación en plazo la sanción se reduce automáticamente al cincuenta por ciento cuando la liquidación supera la sanción propuesta (art. 34 del Real Decreto 928/1998; art. 34.4 LGSS). Las alegaciones o recurso contra una se entienden contra la otra salvo manifestación en contrario (art. 18.5).
- Alzada ante el superior jerárquico; el importe debe ingresarse hasta el último día del mes siguiente a la notificación salvo aval o consignación (art. 33.3).

**D. Recurso de alzada**

- Un mes desde la notificación de la resolución; tres meses sin resolver equivalen a desestimación (art. 23 del Real Decreto 928/1998; art. 122 LPAC). Puede presentarse ante el órgano que dictó el acto o ante el que resuelve (art. 121.2 LPAC).

## Estrategia y jurisprudencia

1. **Decide primero pagar o alegar.** Calcula, con el art. 40 LISOS leído, el importe con la reducción del cuarenta por ciento y compáralo con la probabilidad de anulación o de rebaja de grado. Advierte de que pagar reconoce la responsabilidad (puede pesar en recargos, reincidencia del art. 14.5 del Real Decreto 928/1998 o reclamaciones de trabajadores) y cierra la alzada.
2. **Ordena las alegaciones de mayor a menor efecto:** caducidad del expediente o de las actuaciones y prescripción; defectos del acta que causan indefensión (hechos genéricos, sin medios de comprobación, sin trabajadores identificados, sin criterios de graduación); falta de tipicidad (el hecho probado no encaja en el apartado de la LISOS citado); hechos desvirtuados con prueba concreta, separando lo que el inspector percibió de lo que valora o califica; número de infracciones (en contratación temporal, una por trabajador: apartado 2 del artículo 7 LISOS); graduación sin motivar; subsidiariamente, grado mínimo.
3. **No confundas hechos con juicios:** discute cada afirmación del acta por su naturaleza y aporta el documento que la contradice; pide el informe ampliatorio cuando invoques hechos distintos o indefensión (art. 18.3) y la vista del expediente (art. 17.4).
4. **Comparecencia:** aporta exactamente lo requerido, indexado y en el formato pedido; no hagas manifestaciones de reconocimiento; si falta algo, explica por qué y cuándo se aportará para evitar la obstrucción; pide copia de la diligencia.
5. Consultas en Jurisprudenciator (reformula como máximo dos veces):
   - Presunción de certeza: `consulta="presunción de certeza acta Inspección de Trabajo hechos constatados directamente juicios de valor"`, `base="TS"`, `jurisdiccion="SOCIAL"`; y `consulta="presunción de certeza actas inspección de trabajo hechos percibidos directamente"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`.
   - Caducidad del expediente: `consulta="caducidad procedimiento sancionador orden social seis meses fecha del acta"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
   - Plazo de las actuaciones: `consulta="caducidad actuaciones inspectoras plazo máximo nueve meses artículo 21.4"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
   - Graduación: `consulta="graduación sanción grado mínimo criterios acta inspección motivación"`, `base="AN"`, `jurisdiccion="SOCIAL"`, `tipo_organo="TSJ"`, `provincia` con la sede de la Sala.
   - Una sola conducta continuada: `consulta="sanción orden social non bis in idem conducta continuada"`, `base="TS"`, `jurisdiccion="SOCIAL"`.
   - Fondo: la doctrina de la materia del acta (registro de jornada, fraude en la contratación temporal, cesión ilegal, falso autónomo) con consultas cortas y `anios=5`.
6. Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y transcribe fundamentos, nunca los hechos ni el nombre de aquella empresa. Las alegaciones que discuten la validez de la actuación o la calificación llevan jurisprudencia leída (apartado 8 del formato).

## Documentos que se entregan

Word maquetado según `references/formato-y-organos-laboral.md`, con prosa forense y cada artículo citado con su norma («artículo 17 del Real Decreto 928/1998, de 14 de mayo», «artículo 21 de la Ley 23/2015, de 21 de julio», «apartado 5 del artículo 7 del Real Decreto Legislativo 5/2000»).

**1. Escrito de alegaciones** — `alegaciones-acta-infraccion-<empresa>-<AAAAMMDD>.docx` (o `alegaciones-acta-liquidacion-…`):

1. Encabezamiento al órgano instructor que indique el acta (sin él, `[ÓRGANO INSTRUCTOR SEGÚN EL ACTA]`), con número y fecha del acta.
2. Comparecencia: `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[CÓDIGO DE CUENTA DE COTIZACIÓN]`, representante y título; domicilio o medio para notificaciones.
3. Fecha de notificación y cómputo del plazo de quince días hábiles.
4. ALEGACIONES en ordinales (PRIMERA.-, SEGUNDA.-), en el orden de la estrategia; en cada una, premisa normativa, doctrina leída, hecho del expediente y conclusión.
5. SOLICITO: archivo o anulación del acta; subsidiariamente, recalificación o grado mínimo en su tramo inferior; informe ampliatorio y vista del expediente; práctica de la prueba propuesta.
6. OTROSÍ: prueba documental y testifical; si hay acta de liquidación conexa, alcance de las alegaciones (art. 18.5).
7. Lugar, fecha, firma y relación numerada de documentos.

**2. Escrito de comparecencia y aportación** — `comparecencia-inspeccion-<empresa>-<AAAAMMDD>.docx`: identificación del requerimiento y del inspector actuante, comparecencia y acreditación de la representación, índice de documentos con lo que acredita cada uno, aclaraciones sin reconocimiento de hechos, documentos pendientes con fecha de entrega, solicitud de copia de la diligencia.

**3. Recurso de alzada** — `recurso-alzada-sancion-<empresa>-<AAAAMMDD>.docx`: con la estructura de la guía `recurso-alzada-reposicion-ca`, dirigido al órgano que indique el pie de recursos de la resolución; reitera y desarrolla lo no resuelto y combate la motivación de la resolución.

**Reparto para la redacción rápida:** alegaciones: encabezamiento, comparecencia y plazo en una sección; una por alegación de fondo o grupo de ellas, en el orden de la estrategia (caducidad y prescripción / defectos del acta / tipicidad y hechos desvirtuados / graduación); solicito, otrosí, firma y documentos en la de cierre. La comparecencia, sin equipo; el recurso de alzada, una sección por motivo.

**4. Nota para el abogado**, solo si el abogado la pide o si es el único entregable, porque se defiende a la parte para la que esta skill no redacta documento (si no se entrega aparte, lo que esta skill manda «a la nota» va en el resumen de la entrega) — `nota-abogado-inspeccion-<empresa>-<AAAAMMDD>.docx`: calendario en tabla (hito · fecha · precepto: alegaciones, caducidad del expediente, plazo de las actuaciones, prescripción, pago con reducción, alzada, vía judicial y orden competente); cálculo de la sanción propuesta y de la reducida con el art. 40 LISOS leído; valoración de cada motivo; doctrina con párrafo literal.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos de la Ley 23/2015, del Real Decreto 928/1998 (con la redacción que regía en la fecha del acta), de la LISOS (incluido el tipo concreto del acta y el art. 40 si se calcula algo), de la LGSS y de la LPAC que se citan, y la norma sustantiva que el acta dice infringida.
- [ ] Plazos con fecha inicial, precepto y fecha final: alegaciones, caducidad del expediente, nueve meses de actuaciones, prescripción y alzada.
- [ ] Cálculos de la sanción y de la reducción visibles y con el artículo del que salen.
- [ ] Convenio, si el acta lo invoca, con código, artículo leído y vigencia en la fecha de los hechos.
- [ ] Cada ECLI citado leído con `leer_sentencias` (fundamentos) o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero) y corregido lo que señale.
- [ ] Marcadores en vez de datos inventados; ningún importe sin artículo leído.
- [ ] Lo obtenido en internet (criterios técnicos, sede de presentación) citado con enlace y fecha de consulta y señalado en el resumen.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado y ante qué órgano, plazo y fecha límite con su precepto, cálculos, documentos que faltan y riesgos, tabla de jurisprudencia y próximo paso (pagar, alegar o recurrir).
