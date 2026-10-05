---
name: falso-autonomo-trade
description: >-
  Analiza si un autónomo es en realidad un trabajador por cuenta ajena (falso autónomo: dependencia y
  ajenidad de los arts. 1.1 y 8.1 ET, indicios de la Sala Cuarta, repartidores de plataformas y
  disposición adicional vigesimotercera ET) y redacta el contrato de trabajador autónomo
  económicamente dependiente (TRADE: arts. 11-18 LETA y Real Decreto 197/2009). Sirve a la empresa
  (informe de riesgo con cotizaciones, recargos e infracciones de la LISOS, o un contrato TRADE que
  aguante) y al trabajador (estrategia para que se declare la laboralidad). Úsala con «falso
  autónomo», «trabaja con factura», «rider», «freelance que ficha», «TRADE», «el 75 % de sus
  ingresos». Si ya hubo cese y se impugna, usa papeleta-conciliacion y redactar-demanda-despido; si
  hay acta de la Inspección, inspeccion-trabajo-alegaciones.
---

# Falso autónomo y contrato TRADE

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Concepto de trabajador, presunción de contrato y poder de dirección** → `buscar_articulo` (`ley="ET"`, artículos `"1"`, `"8"` y `"20"`); **presunción de laboralidad del reparto por plataforma** → `leer_boe` (`identificador="BOE-A-2021-15767"`, Ley 12/2021, que introdujo la disposición adicional vigesimotercera del ET; `buscar_articulo` no devuelve las disposiciones adicionales del ET) y `buscar_articulo` (`ley="ET"`, `articulo="64"`, letra d) del apartado 4, algoritmos).
- **Trabajo en plataformas (derecho de la Unión)** → `buscar_articulo` (`ley="Directiva (UE) 2024/2831"`, artículos `"5"` y `"29"`) y `buscar_boe` (`consulta="trabajo en plataformas digitales"`, `desde="01/01/2026"`) para saber si ya hay norma española de transposición.
- **TRADE: concepto, contrato, jornada, extinción, interrupciones, jurisdicción y conciliación** → `buscar_articulo` (`ley="LETA"`, artículos `"1"`, `"11"`, `"12"`, `"13"`, `"14"`, `"15"`, `"16"`, `"17"` y `"18"`) y (`ley="BOE-A-2009-3673"`, Real Decreto 197/2009, artículos `"2"`, `"3"`, `"4"`, `"5"` y `"6"`).
- **Riesgo de Seguridad Social y sanciones** → `buscar_articulo` (`ley="LGSS"`, artículos `"16"`, `"24"`, `"30"`, `"136"`, `"142"`, `"167"` y `"305"`), (`ley="Real Decreto 1415/2004"`, artículos `"42"` y `"56"`: desde cuándo corre la prescripción de cuotas y cuál es el plazo reglamentario de ingreso), (`ley="BOE-A-2000-15060"`, artículos `"22"`, `"23"`, `"39"` y `"40"`) y (`ley="BOE-A-2015-8168"`, `articulo="22"`, medidas de la Inspección). Órdenes anuales de cotización → `buscar_boe` (`consulta="normas legales de cotización a la Seguridad Social desempleo"`, `desde` con el primer año del periodo); la que no aparezca (la de 2022 no sale), en internet en el BOE.
- **Acción del trabajador y plazos** → `buscar_articulo` (`ley="LRJS"`, artículos `"2"`, `"26"`, `"63"`, `"64"`, `"65"`, `"103"`, `"148"` y `"150"`) y (`ley="ET"`, artículos `"55"` y `"59"`).
- **Doctrina sobre laboralidad, plataformas, TRADE y procedimiento de oficio** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"` para la Sala Cuarta; `base="AN"` + `tipo_organo="TSJ"` + `provincia` con la sede de la Sala para los TSJ) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Convenio que se aplicaría si la relación es laboral y empresa real** → `buscar_convenio` + `leer_convenio` (+ `vigencia_convenio`) con la actividad real del cliente, y `buscar_empresa_mercantil` (denominación, CIF, administradores, grupo, intermediarios).
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

Pregunta primero **a quién defiende el abogado** y bifurca: la empresa (o el cliente del autónomo) quiere saber cuánto riesgo tiene y cómo corregirlo, o un contrato TRADE que resista una inspección; el trabajador quiere que se declare que es laboral y cobrar lo que le corresponde.

- Autónomo que presta servicios de forma continuada para un único cliente o casi único, con horario, instrucciones o herramientas del cliente.
- Repartidores y otros prestadores que trabajan a través de una aplicación que asigna tareas, fija precios o puntúa.
- Profesional que factura a un cliente del que obtiene la mayor parte de sus ingresos y quiere (o al que el cliente propone) un contrato TRADE.
- Auditoría preventiva de una empresa con colaboradores externos, antes o durante una actuación de la Inspección.

| Situación | Skill o herramienta que procede |
|---|---|
| El cliente ya ha puesto fin a la relación y el trabajador quiere impugnarlo como despido | `papeleta-conciliacion` y `redactar-demanda-despido` (caducidad de 20 días hábiles: calcúlala antes de nada) |
| El trabajador reclama salarios, diferencias de convenio o vacaciones como laboral | `reclamacion-cantidad` |
| El TRADE reclama al cliente la indemnización del art. 15 LETA o facturas | `guia_escrito` (`escrito="reclamacion-trade"`, `jurisdiccion="laboral"`) |
| Hay una cooperativa, una contrata o una ETT entre el trabajador y quien dirige el trabajo | `sucesion-empresa-contratas` (cesión ilegal, art. 43 ET) |
| Ya hay acta de infracción o de liquidación, o requerimiento de la Inspección | `inspeccion-trabajo-alegaciones` |
| La empresa decide regularizar con contrato laboral | `contrato-trabajo-modalidad` (y `convenio-aplicable`) |
| Consejero o administrador de la sociedad, o socio con control | no es esta skill: encuadramiento de los arts. 136 y 305 LGSS; si es directivo, `alta-direccion` |
| Hay que cuantificar la indemnización si se declara despido | `calculo-indemnizacion-despido` |

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ A quién defiende y qué quiere: informe de riesgo, contrato TRADE, estrategia para reclamar o revisión de un contrato ya firmado.
2. ★ Estado de la relación: viva, cesada (fecha exacta y forma en que se comunicó el cese) o en inspección (fecha de la visita, requerimientos, actas). Con cese, el plazo de 20 días hábiles corre desde el día siguiente: da la fecha límite antes que cualquier otra cosa.
3. ★ Cómo se presta el servicio, hecho a hecho: actividad, fecha de inicio, lugar, horario o turnos, quién los fija, vacaciones y ausencias (si pide permiso), instrucciones y controles (geolocalización, aplicación, informes, valoraciones, sanciones o desconexiones), si puede rechazar encargos o sustituirse por otra persona, con qué medios trabaja y quién los paga, uniforme o marca del cliente, trato con los clientes finales y quién fija los precios.
4. ★ Retribución: forma de cálculo (por hora, por día, fija mensual, por resultado), facturas de los últimos 12-24 meses, otros clientes y porcentaje de ingresos que procede de este cliente; última declaración del IRPF o certificado de rendimientos (art. 2.4 del Real Decreto 197/2009).
5. ★ Documentos: contrato mercantil o de arrendamiento de servicios, correos y mensajes con órdenes, cuadrantes, registros de la aplicación, alta en el régimen de autónomos (fecha), comunicaciones de la condición de TRADE y registro del contrato si lo hay.
6. ★ Cliente: denominación exacta (`buscar_empresa_mercantil`), actividad real, plantilla, si hay trabajadores por cuenta ajena que hacen lo mismo, representación legal y convenio que aplica a su plantilla.
7. Para el contrato TRADE: objeto y resultado que se encarga, precio y forma de pago, duración, régimen de descanso y jornada máxima, preaviso, indemnización pactada, acuerdo de interés profesional si existe, y quién registrará el contrato.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota su «vigente desde» y «redacción vigente dada por».

**Laboralidad (arts. 1.1, 8.1 y 20 ET):**

- El art. 1.1 ET exige servicios voluntarios, retribuidos, por cuenta ajena y dentro del ámbito de organización y dirección de otro; el art. 8.1 ET presume el contrato de trabajo entre quien presta un servicio así y quien lo recibe a cambio de retribución. El nombre que las partes dieron al contrato y el alta como autónomo no deciden: la calificación sale de cómo se presta el servicio.
- Revisa las exclusiones del art. 1.3 ET, en particular la letra f) (operaciones mercantiles en las que el agente responde del buen fin y asume el riesgo) y el párrafo final de la letra g) (transportistas con autorización administrativa y vehículo propio). Si el caso encaja literalmente, dilo; si solo se parece, compáralo con la doctrina.
- La Sala Cuarta trabaja con la técnica indiciaria. Busca en el caso, uno por uno, los indicios comunes de **dependencia** (asistencia al centro o lugar designado por el cliente y sometimiento a horario; desempeño personal sin sustitución; inserción en la organización del cliente, que programa la actividad; ausencia de organización empresarial propia) y de **ajenidad** (el cliente recibe directamente los frutos o servicios; el cliente decide precios, clientela y personas a atender; retribución fija o periódica; cálculo de la retribución con proporción a la actividad, sin riesgo ni lucro especial; falta de inversión relevante propia). Léelos en la resolución que cites con `leer_sentencias` (`terminos="indicios comunes de dependencia"` y `"indicios comunes de ajenidad"`), no de memoria.
- **Reparto por plataforma**: la disposición adicional vigesimotercera del ET presume incluida en el ámbito del ET la actividad de reparto o distribución de productos o mercancías cuando la empleadora ejerce la organización, dirección y control, de forma directa, indirecta o implícita, mediante gestión algorítmica a través de una plataforma digital. Léela en `leer_boe` (Ley 12/2021) y dilo en el documento; `verificar_escrito` no la comprueba. La representación legal tiene derecho a conocer los parámetros de los algoritmos (letra d) del apartado 4 del artículo 64 del ET).
- **Otras plataformas**: la Directiva (UE) 2024/2831 establece una presunción de laboralidad refutable cuando hay hechos que indican dirección y control, con plazo de transposición hasta el 2 de diciembre de 2026 y aplicación a las relaciones vigentes solo desde esa fecha (arts. 5.6 y 29, léelos). Comprueba con `buscar_boe` si ya hay ley española de transposición y, si el resultado no es concluyente, búscala en internet en el BOE y cítala con su enlace y la fecha de consulta; si no la hay, di que la presunción de la directiva aún no es derecho aplicable en España y apóyate en el art. 8.1 ET y la doctrina.

**Consecuencias para la empresa (informe de riesgo):**

- Seguridad Social: alta de oficio y encuadramiento en el Régimen General (arts. 16.4 y 136 LGSS; art. 22.7 de la Ley 23/2015), liquidación de las cuotas no prescritas y recargos del art. 30 LGSS (letra b) del apartado 1 si no se transmitieron las liquidaciones). **Prescripción con fechas**: cuatro años (art. 24 LGSS, con sus causas de interrupción) contados desde que termina el plazo reglamentario de ingreso (art. 42 del Real Decreto 1415/2004), que en el Régimen General es el mes siguiente al del devengo (art. 56 del mismo real decreto): di desde qué mes siguen siendo exigibles las cuotas a la fecha del informe y cuándo prescribe el siguiente. La empresa ingresa **también la aportación del trabajador**, porque no la descontó al pagar (art. 142.2 LGSS). Para cuantificar, busca la orden de cotización de cada año del periodo (bases y tipos) con `buscar_boe` o, si no aparece, en internet en el BOE, y cítala con su enlace y la fecha de consulta; sin el salario acreditado (nóminas, facturas que el abogado acepte como retribución o tabla salarial del año, apartado 3 de las anclas) no calcules cuotas: di qué dato falta.
- Responsabilidad en prestaciones por falta de alta y cotización (art. 167 LGSS): si el trabajador ha tenido un accidente o una baja, destácalo como riesgo principal.
- Infracciones de la LISOS: no solicitar el alta (apartado 2 del artículo 22 del Real Decreto Legislativo 5/2000); dar de baja en el Régimen General y servirse de un alta indebida como autónomo (apartado 16 del artículo 22), **solo si el trabajador estuvo antes de alta en el Régimen General con esa empresa y pasó a autónomo con la misma prestación** (si nunca estuvo, dilo: no aplica); no ingresar cuotas (apartado 3 del artículo 22 o letra b) del apartado 1 del artículo 23, según se hayan transmitido o no las liquidaciones). Una infracción por trabajador afectado. Si la empresa regulariza por su cuenta y pide el alta fuera de plazo sin actuación inspectora, el tipo es el apartado 10 del artículo 22 (grave, cuantía general del art. 40): inclúyelo al valorar la opción de regularizar. **Cuantías y graduación**: léelas en los artículos 39 y 40 del Real Decreto Legislativo 5/2000 en el momento; no las escribas de memoria.
- Laborales: antigüedad desde el inicio real de la prestación, convenio aplicable, vacaciones y diferencias salariales (prescripción de un año, art. 59 ET) y, si se extingue, despido con esa antigüedad.
- Consecuencias fiscales (IVA facturado, retenciones): fuera de esta skill; avisa de que existen y de que las valore un asesor fiscal.
- Si entre el trabajador y quien dirige el trabajo hay una cooperativa, contrata o empresa interpuesta, la laboralidad puede declararse respecto de la empresa principal: valora la cesión ilegal con `sucesion-empresa-contratas`.

**Acción del trabajador:**

- Orden social (art. 2 LRJS). Relación viva: demanda declarativa de la existencia de relación laboral por el procedimiento ordinario, con conciliación previa (arts. 63-65 LRJS), acumulable a la reclamación de cantidades (art. 26 LRJS). Alternativa: denuncia ante la Inspección, que puede promover el alta de oficio (art. 22.7 de la Ley 23/2015).
- Cese: se impugna como despido en **20 días hábiles de caducidad** (art. 59.3 ET y art. 103 LRJS), suspendidos por la papeleta (art. 65 LRJS). La antigüedad y el salario del módulo son los de la relación laboral que se pide declarar.
- Procedimiento de oficio (arts. 148-150 LRJS): lee el art. 148 vigente antes de invocarlo; la versión que devuelve el conector enumera las letras a) a c), y es la correcta: la antigua letra d) (actas impugnadas alegando que la relación no es laboral) la suprimió la disposición final novena de la Ley 3/2023 (compruébalo en el texto consolidado del BOE si lo necesitas y cítalo con enlace). En el proceso de oficio los hechos de la resolución o comunicación base hacen fe salvo prueba en contrario (art. 150.2.d LRJS).

**Contrato TRADE (LETA y Real Decreto 197/2009):**

- Requisitos acumulativos: actividad habitual, personal, directa y predominante para un cliente del que percibe al menos el 75 % de sus ingresos por rendimientos del trabajo y de actividades económicas (art. 11.1 LETA; cómputo del art. 2.1 del Real Decreto 197/2009), más todas las condiciones del art. 11.2 LETA: sin trabajadores a su cargo ni subcontratación (con las excepciones tasadas de la letra a), actividad diferenciada de la plantilla del cliente, infraestructura y material propios cuando sean relevantes, criterios organizativos propios y retribución por resultado con riesgo y ventura. Excluidos los titulares de establecimientos abiertos al público y quienes ejercen en sociedad (art. 11.3 LETA).
- La condición de TRADE solo puede ostentarse respecto de un cliente (art. 12.2 LETA) y exige que el autónomo **comunique** su condición al cliente (art. 2.2 del Real Decreto 197/2009); el cliente puede pedirle acreditación al firmar y cada seis meses (art. 2.3), con la declaración del IRPF o el certificado de la Agencia Tributaria (art. 2.4).
- Forma y contenido: siempre por escrito (art. 12.1 LETA; art. 4.1 del Real Decreto 197/2009), con los extremos obligatorios del art. 4.2 y las declaraciones del art. 5 de ese real decreto. Sin duración ni servicio determinado se presume indefinido (art. 12.4 LETA; art. 3 del real decreto).
- Registro: lo hace el TRADE en los diez días hábiles siguientes a la firma y lo comunica al cliente en cinco días hábiles; si a los quince días hábiles no hay comunicación, registra el cliente en los diez días hábiles siguientes, ante el Servicio Público de Empleo Estatal; también las modificaciones y la terminación (art. 6 del real decreto). El canal vigente para registrarlo búscalo en internet en la sede electrónica del SEPE (servicio «Registro de contratos de trabajadores autónomos económicamente dependientes (TAED)») y cítalo con su enlace; no des códigos ni rutas de memoria. Da las fechas límite de registro con la fecha de firma prevista: días hábiles del art. 30.2 de la Ley 39/2015 (`buscar_articulo`, `ley="LPAC"`), con las fiestas nacionales y autonómicas de la resolución anual de fiestas laborales del BOE y las locales del municipio (búscalas en internet y di cuáles no has podido confirmar).
- Jornada y descansos: interrupción anual de 18 días hábiles como mínimo; descanso semanal, festivos y jornada máxima fijados por contrato o acuerdo de interés profesional; exceso voluntario con el límite del art. 14.3 LETA; adaptación de horario para víctimas (art. 14.5).
- Interrupciones justificadas (art. 16 LETA) y extinción (art. 15 LETA): la extinción por el cliente sin causa justificada da derecho a indemnización de daños y perjuicios, fijada en el contrato o el acuerdo de interés profesional o, en su defecto, con los factores del art. 15.4. **No la excluyas ni la fijes en cero** aunque lo pida el cliente: el art. 15.3 LETA reconoce el derecho y el art. 3.1.c) LETA declara nulas las cláusulas contrarias a derecho necesario; propón una cuantía o fórmula (la certidumbre es lo que protege al cliente). Las interrupciones del art. 16.1 no justifican la extinción, salvo el perjuicio importante del art. 16.3 en los supuestos que allí se indican.
- **Exclusividad y disponibilidad**: no pactes exclusividad (el TRADE puede tener otros clientes y la exclusividad refuerza la dependencia) ni horarios de disponibilidad o presencia periódica en la sede del cliente (art. 11.2.d LETA y art. 5.1.b del Real Decreto 197/2009): si el borrador del cliente los trae, suprímelos y explica por qué en la nota.
- **Obras protegidas** (traducción, diseño, fotografía, textos, software): el contrato marco no puede ceder en bloque los derechos de explotación de las obras futuras ni prohibir al autor crear otras (apartados 3 y 4 del artículo 43 del Real Decreto Legislativo 1/1996, de 12 de abril, texto refundido de la Ley de Propiedad Intelectual; `buscar_articulo`, `ley="LPI"`); remite la cesión a un documento por encargo y revisa si la tarifa puede ser a tanto alzado (art. 46 de ese real decreto legislativo). Cítalo como «Real Decreto Legislativo 1/1996»: con «texto refundido de la Ley de Propiedad Intelectual» a secas, `verificar_escrito` atribuye el artículo a otra ley.
- Conciliación o mediación previa obligatoria (art. 18.1 LETA) y competencia social (art. 17 LETA; letra d) del art. 2 LRJS). El órgano autonómico que concilia a los TRADE búscalo en internet en la sede de la comunidad (en Aragón, por ejemplo, es un trámite propio de la Dirección General de Trabajo) y nómbralo en el contrato; si no aparece, usa una denominación genérica y avísalo en la nota.
- Plazo para reclamar la indemnización del art. 15: la LETA no lo fija en los artículos 11-18. Busca doctrina (ver «Estrategia») y, si Jurisprudenciator no la tiene, búscala en internet: cita solo las resoluciones que Jurisprudenciator localice con `buscar_por_cita` y leas con `leer_sentencias`. Si no aparece, dilo en la nota y recomienda actuar dentro del plazo más corto defendible.
- **Advertencia que va siempre al abogado (en la nota o, si no se entrega, en el resumen)**: un contrato TRADE no impide que se declare la laboralidad si en la práctica hay dependencia y ajenidad. Las cláusulas cosméticas (declarar «autonomía» mientras se fijan horarios, turnos o precios) empeoran el riesgo: redacta el contrato solo si los hechos del apartado «Datos» encajan en el art. 11 LETA; si no encajan, dilo y propón regularizar.

## Estrategia y jurisprudencia

1. **Empresa**: construye una matriz indicio por indicio (hecho, prueba que lo acredita, sentido a favor o en contra) y clasifica el riesgo con un criterio visible: alto si concurren horario o lugar fijados por el cliente, sustitución prohibida y precios fijados por el cliente; medio si hay dependencia económica pero organización propia real; bajo si hay varios clientes, medios propios relevantes y riesgo empresarial acreditado. Ofrece tres salidas con su coste: regularizar con contrato laboral, reconfigurar de verdad la relación (quitando lo que genera dependencia, no solo cambiando el papel) o formalizar un TRADE si encaja.
2. **Trabajador**: ordena la prueba por indicios (mensajes con órdenes, cuadrantes, capturas de la aplicación, facturas homogéneas, testigos de la plantilla), decide si conviene pedir la declaración con la relación viva o esperar al cese, y calcula plazos. Si hay cese, la prioridad es la papeleta dentro de la caducidad.
3. Consultas en Jurisprudenciator (reformula como máximo dos veces si no hay resultados útiles):
   - Doctrina general: `buscar_sentencias` (`consulta="existencia de relación laboral técnica indiciaria notas de dependencia y ajenidad"`, `base="TS"`, `jurisdiccion="SOCIAL"`) y la misma con la actividad del caso (`"<actividad> relación laboral arrendamiento de servicios dependencia"`).
   - Plataformas: `consulta="plataforma digital reparto repartidores relación laboral"`, `base="TS"`; para otras plataformas, `base="AN"`, `tipo_organo="TSJ"`, `anios=3`.
   - TRADE: `consulta="reconocimiento condición trabajador autónomo económicamente dependiente comunicación al cliente"` y `consulta="validez contrato TRADE riesgo fijación de precios dependencia"`, `base="TS"`; plazo de la acción: `consulta="TRADE extinción contrato plazo ejercicio acción prescripción caducidad"`.
   - Procedimiento de oficio y actas: `consulta="procedimiento de oficio acta Inspección de Trabajo naturaleza laboral de la relación"`, `base="TS"`.
   - Falsos cooperativistas o empresas interpuestas: `consulta="socios cooperativistas verdadera empleadora relación laboral"`, `base="TS"`.
   - Criterios técnicos de la Inspección sobre falsos autónomos o plataformas: no están en Jurisprudenciator; búscalos en internet en la web oficial de la Inspección de Trabajo y cítalos con su enlace y la fecha de consulta, como criterio de actuación (no son norma).
4. Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que vayas a citar y transcribe **fundamentos**, nunca el relato de hechos ni los datos de aquel pleito. La Sala Cuarta advierte a menudo que la calificación depende de las circunstancias de cada caso: cuando una resolución niegue la laboralidad en un sector (o la afirme), compara sus hechos con los del cliente antes de usarla.
5. Prefiere la doctrina posterior a la entrada en vigor de la Ley 12/2021 para plataformas (`fecha_desde="30/09/2021"`) y la reciente para el resto (`anios=5`); amplía solo si no hay nada.

## Documentos que se entregan

Todos en Word según `references/formato-y-organos-laboral.md`.

**Posición de la empresa — informe de riesgo** (`nota-riesgo-laboralidad-<empresa>-<AAAAMMDD>.docx`):

1. Resumen: riesgo (alto, medio o bajo) y por qué, en cinco líneas.
2. Hechos relevantes, con el documento que prueba cada uno.
3. Marco normativo leído (arts. 1, 8 y 20 ET; disposición adicional vigesimotercera si hay plataforma; LETA si se plantea TRADE).
4. Matriz de indicios en tabla: indicio · hecho del caso · prueba · a favor o en contra de la laboralidad · doctrina (ECLI y párrafo literal).
5. Consecuencias: Seguridad Social (periodo no prescrito con fechas, conceptos que se liquidarían y qué datos faltan para cuantificar), responsabilidad en prestaciones, infracciones de la LISOS con su artículo y la remisión a sus artículos 39 y 40 para la cuantía, consecuencias laborales.
6. Opciones con coste y riesgo residual, y recomendación.
7. Jurisprudencia literal (apartado 8 del formato: aquí es imprescindible).

**Reparto para la redacción rápida (informe de riesgo):** resumen, hechos y marco normativo / matriz de indicios con su doctrina / consecuencias (Seguridad Social con fechas, prestaciones, LISOS y laborales) / opciones, recomendación y jurisprudencia literal.

**Posición de la empresa — contrato TRADE** (`contrato-trade-<apellido-trabajador>-<AAAAMMDD>.docx`), solo si los hechos encajan:

- REUNIDOS e INTERVIENEN (cliente con denominación exacta y CIF; nombre y DNI del TRADE, con los marcadores `[NOMBRE Y APELLIDOS]` y `[DNI/NIE]` si no se han facilitado).
- EXPONEN: actividad del TRADE, comunicación de su condición de económicamente dependiente y declaraciones del art. 5.1 del Real Decreto 197/2009.
- CLÁUSULAS en ordinales con título: objeto y resultado encargado (no tiempo de trabajo); contraprestación por resultado, periodicidad y forma de pago; organización propia e indicaciones solo técnicas; medios propios; interrupción anual (mínimo del art. 14.1 LETA), descanso semanal, festivos y jornada máxima con su distribución; actividad adicional voluntaria con su límite; interrupciones justificadas; duración y fecha de inicio; preaviso de desistimiento y de extinción; indemnización por extinción; acuerdo de interés profesional aplicable, si el TRADE da su conformidad expresa; prevención de riesgos; comunicación por escrito de las variaciones de la dependencia y consecuencias si deja de cumplirla; registro en el SEPE (quién lo hace y plazos del art. 6); conciliación previa y orden social.
- Anexo: declaración del TRADE del art. 5.2 del Real Decreto 197/2009 (ingresos del 75 %, sin trabajadores, sin subcontratación, infraestructura propia, sin establecimiento abierto al público ni ejercicio en sociedad) y documentación acreditativa del art. 2.4.
- Firmas en dos columnas. Sin jurisprudencia en el contrato.
- **Reparto para la redacción rápida (contrato TRADE):** comparecencia, EXPONEN, objeto, contraprestación, organización y medios / interrupción anual, descanso, jornada, actividad adicional, interrupciones, duración, preaviso e indemnización / acuerdo de interés profesional, prevención, registro en el SEPE, conciliación, firmas y anexo.
- Nota para el abogado, solo si el abogado la pide (si no, lo que esta skill manda «a la nota» —calendario, riesgos, cálculos y jurisprudencia con su ECLI— va en el resumen de la entrega) — `nota-contrato-trade-<empresa>-<AAAAMMDD>.docx`: por qué encaja cada requisito del art. 11 LETA, riesgos de laboralidad que subsisten, artículos leídos y doctrina (si existe).

**Posición del trabajador** (`nota-laboralidad-<apellido-trabajador>-<AAAAMMDD>.docx`): hechos y prueba por indicio, calificación razonada con doctrina literal, acciones posibles (declarativa, despido, cantidad, denuncia), plazos con fecha inicial, precepto y fecha final, documentos que faltan y riesgos (por ejemplo, que una resolución considere acreditada la autonomía). Si el abogado pide el escrito, deriva a la skill del cuadro o, para la demanda declarativa, usa `guia_escrito` (`escrito="demanda declarativa de existencia de relación laboral"`, `jurisdiccion="laboral"`).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado, ni en Jurisprudenciator ni en internet.
- [ ] Todo dato que no sale de Jurisprudenciator (orden de cotización, tabla salarial, criterio técnico, nombre de un órgano, sede electrónica) lleva su enlace oficial y la fecha de consulta, y el resumen lo identifica.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos usados (ET 1, 8, 20, 55, 59 y 64; LETA 1 y 11-18; Real Decreto 197/2009 arts. 2-6; LGSS 16, 24, 30, 136, 167 y 305; Real Decreto Legislativo 5/2000 arts. 22, 23, 39 y 40; LRJS 2, 26, 63-65, 103, 148 y 150), con su fecha de vigencia; la disposición adicional vigesimotercera del ET leída con `leer_boe` si hay plataforma.
- [ ] Comprobado con `buscar_boe` si existe ley española de transposición de la Directiva (UE) 2024/2831 antes de mencionarla.
- [ ] Cada indicio de la matriz tiene hecho y prueba; lo no acreditado está marcado.
- [ ] Ninguna cuantía de sanción, base de cotización ni recargo escrita de memoria: remisión al artículo leído o cálculo con datos aportados.
- [ ] Informe de riesgo: periodo no prescrito con fechas (arts. 42 y 56 del Real Decreto 1415/2004), aportación del trabajador a cargo de la empresa (art. 142.2 LGSS) y apartado 16 del art. 22 LISOS descartado si no hubo alta previa en el Régimen General.
- [ ] Contrato TRADE: sin exclusividad ni horario de disponibilidad, indemnización del art. 15 cuantificada (nunca cero) y, si la actividad crea obras protegidas, cesión de derechos remitida a documentos por encargo (art. 43 del Real Decreto Legislativo 1/1996).
- [ ] Convenio y vigencia comprobados si se ha usado para cuantificar.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero); los avisos de «posible disonancia» contrastados con el apartado exacto leído (el verificador compara con el título del artículo).
- [ ] Marcadores en lugar de datos no facilitados (`[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[FECHA DE ANTIGÜEDAD]`).
- [ ] Plazo con fecha inicial, precepto y fecha final (despido, conciliación, registro del contrato TRADE).
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha preparado y para quién; plazos; riesgo y de dónde sale; documentos que faltan; tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene); próximo paso.
