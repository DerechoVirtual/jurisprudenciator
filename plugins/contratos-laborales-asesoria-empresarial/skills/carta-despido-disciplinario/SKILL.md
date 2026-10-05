---
name: carta-despido-disciplinario
description: >-
  Prepara para la empresa la carta de despido disciplinario (art. 55 ET), la comunicación de audiencia previa al
  trabajador que exige la doctrina de la Sala Cuarta sobre el artículo 7 del Convenio 158 de la OIT, el expediente
  contradictorio o la audiencia a delegados sindicales cuando procedan, y, si la pides, una nota de riesgo con el cálculo de la
  indemnización si el despido se declarase improcedente. Úsala con «despedir a un trabajador por…», «carta de
  despido disciplinario», «transgresión de la buena fe», «faltas de asistencia», «audiencia previa al despido».
  También revisa, para el trabajador, una carta recibida y señala por qué no aguanta. Para sancionar sin despedir,
  sanciones-disciplinarias; para la demanda, redactar-demanda-despido; si la causa es objetiva, carta-despido-objetivo.
---

# Carta de despido disciplinario con audiencia previa

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Causas, forma, calificación y efectos del despido** → `buscar_articulo` (`ley="ET"`, artículos `"54"`, `"55"` y `"56"`) y (`ley="LRJS"`, artículos `"105"`, `"108"` y `"110"`).
- **Audiencia previa al despido disciplinario** → `buscar_sentencias` (`consulta="audiencia previa despido disciplinario artículo 7 Convenio 158 OIT"`, `base="TS"`, `jurisdiccion="SOCIAL"`): localiza la del Pleno de noviembre de 2024 (con `fecha_desde="15/11/2024"` y `fecha_hasta="30/11/2024"` si no sale) y la más reciente que la aplique; + `leer_sentencias` (`parrafos=4`, `terminos="audiencia previa posibilidad de defenderse cargos razonablemente"`). Cómo se da en la práctica: la misma consulta con `base="AN"`, `tipo_organo="TSJ"`, `fecha_desde="01/01/2025"`.
- **Suficiencia de los hechos de la carta** → `buscar_sentencias` (`consulta="carta de despido contenido hechos imputados conocimiento claro suficiente e inequívoco defensa"`, `base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`).
- **Garantías de representantes y afiliados** → `buscar_articulo` (`ley="ET"`, `articulo="68"`) y (`ley="LOLS"`, `articulo="10"`).
- **Prescripción de la falta** → `buscar_articulo` (`ley="ET"`, `articulo="60"`) + `buscar_sentencias` (`consulta="prescripción faltas laborales dies a quo conocimiento cabal faltas continuadas ocultación"`, `base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias`.
- **Plazo del trabajador y tramitación** → `buscar_articulo` (`ley="ET"`, `articulo="59"`) y (`ley="LRJS"`, artículos `"103"` y `"43"`).
- **Convenio aplicable y sus artículos** → `buscar_convenio` (`consulta` con el nombre del sector tal como lo usa el registro y `territorio` = provincia del centro) + `leer_convenio` (`buscar_en="faltas"`, `buscar_en="despido"` y `buscar_en="audiencia"` para localizar los artículos; después `articulo="N"` para leerlos enteros; si el provincial remite el régimen disciplinario a un acuerdo o convenio estatal, léelo en el estatal). Después, `vigencia_convenio` de cada convenio que uses: **`leer_convenio` devuelve el texto publicado originalmente, no las modificaciones posteriores**. Si `vigencia_convenio` registra una modificación, un acuerdo parcial o un pronunciamiento de tribunal posterior a esa publicación y anterior a la decisión, búscalo en internet en el boletín oficial (BOE, boletín autonómico o BOP) y comprueba si cambia los artículos que aplicas; cítalo con su enlace (punto 3 de la puerta). Si no lo localizas, dilo en la nota.
- **Empresa** → `buscar_empresa_mercantil` (denominación exacta y CIF para el membrete, si el abogado no los da).
- **Revisión del documento antes de entregarlo** → cada redactor pasa `verificar_escrito` sobre las frases de su sección que citan normas (no sobre el documento entero) y el ensamblado de `redaccion-rapida` comprueba que cada ECLI o ROJ citado figure entre las fuentes leídas; `buscar_por_cita` solo para una sentencia que aporte el abogado y no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...). El conector no devuelve el texto del Convenio 158 de la OIT: cítalo a través del párrafo literal de la sentencia del Supremo que lo transcribe o, si necesitas el texto del artículo, léelo en internet (instrumento de ratificación publicado en el BOE o la base oficial de la OIT) y cítalo con su enlace; nunca de memoria.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Primera pregunta: **¿a quién defiende el abogado?**

- **Empresa** (uso principal): quiere despedir por un incumplimiento grave y culpable con una carta que aguante. Entregas la comunicación de audiencia previa y la carta, con el riesgo en el resumen (y la nota de riesgo, si la pides).
- **Trabajador**: ha recibido una carta y quiere saber por qué no aguanta. Entregas una nota de revisión con los defectos (forma, audiencia, garantías, prescripción, nulidad) y el plazo de caducidad calculado; la papeleta y la demanda se hacen con `papeleta-conciliacion` y `redactar-demanda-despido`.

| Situación | Skill que procede |
|---|---|
| La conducta no justifica el despido o la empresa prefiere una sanción menor | `sanciones-disciplinarias` |
| El motivo es ineptitud, falta de adaptación o causa económica, técnica, organizativa o de producción | `carta-despido-objetivo` |
| El cálculo exige tramos anteriores al 12/02/2012, salarios de tramitación o casos complejos | `calculo-indemnizacion-despido` |
| Hay que preparar el finiquito que acompaña a la carta | `finiquito-liquidacion` |
| No se sabe qué convenio se aplica | primero `convenio-aplicable` |
| El trabajador es alto directivo (RD 1382/1985) | `alta-direccion` |

## Datos que hay que reunir antes de redactar

Obtén estos datos de la documentación aportada y pregunta solo lo que bloquee la estructura del escrito y no se deduzca de ella (los marcados con ★, si faltan), en una única ronda (paso 2 de `redaccion-rapida`); lo demás se redacta con su marcador. Cierra los datos del caso y el plan antes de que el equipo redacte (pasos 2 y 3 de `redaccion-rapida`).

1. ★ A quién defiende el abogado.
2. ★ Hechos que se imputan: qué, cuándo (día y, si importa, hora), dónde, con qué consecuencias, y cómo se prueban (testigos, documentos, registros, informes de detective, cámaras). Si es una conducta repetida, el listado de episodios con fecha.
3. ★ Fecha en que la empresa conoció los hechos, quién los conoció y si hubo investigación (fechas de inicio y cierre).
4. ★ Fecha prevista de entrega de la carta y fecha de efectos del despido.
5. ★ Convenio colectivo (o actividad real y provincia del centro) y régimen de faltas que tipifica esos hechos.
6. ★ Condición del trabajador: representante legal o delegado sindical (o lo fue en el último año), afiliado a un sindicato con constancia de la empresa, y si hay delegados sindicales de su sección.
7. ★ Situaciones que abren la nulidad: embarazo o suspensión por nacimiento, adopción, riesgo durante el embarazo o la lactancia; permisos del art. 37 ET o adaptación del art. 34.8 ET solicitados o en disfrute; excedencia del art. 46.3; reincorporación tras nacimiento en los últimos doce meses; víctima de violencia de género o sexual; reclamaciones, denuncias o quejas previas; baja médica; actividad sindical.
8. ★ Para la nota de riesgo: fecha de antigüedad (y si hubo contratos anteriores encadenados o sucesión de empresa), nóminas de los últimos doce meses (salario bruto con prorrata de pagas y complementos salariales), tipo de contrato y jornada.
9. Sanciones previas relacionadas y su firmeza.
10. **Solo trabajador**: la carta, la fecha de entrega y la de efectos, si hubo audiencia previa y qué se le comunicó, y si la empresa tramitó la baja en la Seguridad Social.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

**1. Causa (art. 54 ET).** Incumplimiento grave y culpable. Encaja cada hecho en una letra del art. 54.2 ET y en el tipo de falta muy grave del convenio que prevé el despido como sanción. Si el convenio no permite el despido para ese tipo o el hecho es aislado y de poca entidad, advierte del riesgo de improcedencia por falta de gravedad y valora `sanciones-disciplinarias`: el juez puede declarar improcedente el despido y autorizar una sanción menor (art. 108.1 LRJS).

**2. La carta (art. 55.1 ET).** Escrita, con los hechos que motivan el despido y la fecha en que tendrá efectos. La doctrina exige que los hechos permitan al trabajador un conocimiento claro, suficiente e inequívoco para defenderse: conducta, fecha y circunstancias; en conductas continuadas, la determinación temporal en la medida de lo posible. Solo los hechos de la carta podrán justificar el despido en juicio (art. 105.2 LRJS): no dejes nada fuera. Lee además qué otras exigencias formales añade el convenio (art. 55.1, párrafo segundo).

**3. Audiencia previa al trabajador.** El Pleno de la Sala Cuarta declaró en noviembre de 2024 que el artículo 7 del Convenio 158 de la OIT es de aplicación directa: antes de despedir por motivos de conducta o rendimiento hay que ofrecer al trabajador la posibilidad de defenderse de los cargos, salvo que no pueda pedirse razonablemente al empleador. Lee esa sentencia y la más reciente que la aplique y comprueba en ellas:
- desde qué despidos es exigible (la doctrina posterior la excluye para los despidos anteriores al cambio);
- que no se confunde con la impugnación judicial ni se cumple con la sola entrega de la carta;
- qué ocurre si se omite (lee cómo califican el despido las sentencias que la aplican; no lo afirmes sin ese párrafo).

Cómo darla y documentarla (es lo que entregas):
- Comunicación escrita de los cargos al trabajador, con los mismos hechos que llevará la carta, entregada con recibí.
- Plazo para alegar por escrito o en reunión con acta. La ley no fija el plazo: el del convenio si lo prevé; si no, uno que permita defenderse de verdad según la complejidad de los hechos. Busca en los TSJ cómo se han valorado plazos concretos (la consulta práctica de la lista) y dilo en la nota.
- Constancia de las alegaciones presentadas o de que no se presentaron, y valoración de las alegaciones antes de decidir.
- Mención de la audiencia y de lo alegado en la carta de despido.
- La prescripción sigue corriendo mientras dura la audiencia: planifica las fechas para que la carta se entregue dentro del plazo del art. 60.2 ET.
- Excepción de razonabilidad: solo en circunstancias concretas que impidan objetivamente dar audiencia; si la empresa la invoca, documenta por qué y adviértele del riesgo.

**4. Representantes, delegados sindicales y afiliados.**
- Representante legal o delegado sindical: expediente contradictorio en el que se oye al interesado y a los restantes miembros de la representación (art. 55.1, párrafo tercero, y art. 68.a ET; art. 10.3 LOLS). Si deja de serlo hace menos de un año, ábrelo igualmente. En caso de improcedencia, la opción entre readmisión e indemnización es suya (art. 56.4 ET).
- Afiliado con constancia empresarial: audiencia previa a los delegados sindicales de su sección (art. 55.1, párrafo cuarto, ET; art. 10.3.3.º LOLS). Es distinta de la audiencia al trabajador: hay que dar las dos.

**5. Consecuencias de los defectos de forma.** El despido sin los requisitos del art. 55.1 ET es improcedente (art. 55.4 ET; art. 108.1 LRJS). La empresa puede efectuar un nuevo despido que cumpla lo omitido en los veinte días siguientes al primero, pagando los salarios intermedios y manteniendo el alta (art. 55.2 ET). Tras una sentencia de improcedencia por forma y readmisión, cabe un nuevo despido en siete días (art. 110.4 LRJS).

**6. Nulidad (art. 55.5 ET y art. 108.2 LRJS).** Nulo si el móvil es discriminatorio o lesiona derechos fundamentales, y en los supuestos objetivos que lista el art. 55.5 (dato 7), salvo que se declare la procedencia por motivos no relacionados. Si en el art. 55.5 aparece una nota «Téngase en cuenta» con otra redacción de la letra b), compara las dos y, para la empresa, trata como protegidos los supuestos que figuren en cualquiera de ellas. Efecto: readmisión inmediata con salarios dejados de percibir (art. 55.6 ET).

**7. Prescripción (art. 60.2 ET).** Faltas muy graves: sesenta días desde que la empresa tuvo conocimiento y, en todo caso, seis meses desde la comisión. Aplica la doctrina del conocimiento cabal y de la ocultación que devuelve la consulta de la lista y fija las dos fechas límite antes de calendarizar la audiencia.

**8. Fecha de efectos, entrega y recibí.** Fecha de efectos igual o posterior a la entrega. Entrega en mano con copia y recibí fechado; si el trabajador se niega a firmar, lectura ante dos testigos que firman la constancia; si no está, burofax con certificación de texto y acuse. La fecha de efectos abre al trabajador el plazo de caducidad de veinte días hábiles (art. 59.3 ET y art. 103.1 LRJS; agosto y Navidad cuentan, art. 43.4 LRJS). Advierte a la empresa de que tramite la baja en la Seguridad Social: si no lo hace, el proceso será urgente (art. 103.4 LRJS). El finiquito, con `finiquito-liquidacion`.

## Estrategia y jurisprudencia

**Empresa.** Antes de redactar, decide si los hechos probados sostienen el despido: gravedad, culpabilidad, prueba disponible y proporción con el tipo del convenio. Después calendariza: prescripción → audiencia (y expediente o audiencia sindical) → valoración → carta dentro de plazo. En la nota, califica el riesgo (procedencia, improcedencia, nulidad) y cuantifica la improcedencia.

**Trabajador (revisión de una carta recibida).** Revisa por este orden: audiencia previa omitida o meramente formal; carta genérica o sin fechas; expediente o audiencia sindical omitidos; requisito del convenio incumplido; prescripción; hechos no probados o sin gravedad; supuesto de nulidad del dato 7 o móvil lesivo. Calcula la caducidad y pasa a `papeleta-conciliacion`.

**Consultas en Jurisprudenciator** (reformula como máximo dos veces):

- Audiencia previa: las dos de la lista (TS y TSJ). Añade `consulta="omisión audiencia previa despido disciplinario Convenio 158 improcedencia consecuencia"`, `base="AN"`, `tipo_organo="TSJ"`, `fecha_desde="01/01/2025"` para las consecuencias.
- Carta: la consulta de suficiencia de la lista y, si la conducta es continuada, `consulta="carta de despido conducta continuada determinación temporal hechos"`.
- Gravedad y gradualismo: `consulta="despido disciplinario teoría gradualista proporcionalidad gravedad culpabilidad"`, `base="TS"`, `anios=5`.
- La causa concreta: `consulta="despido disciplinario <causa> procedencia"` (transgresión de la buena fe, faltas de asistencia, disminución del rendimiento, ofensas) con `base="AN"`, `tipo_organo="TSJ"` y la `provincia` de la sede de la Sala del lugar de trabajo.
- Nulidad: `consulta="despido nulo indicios discriminación carga de la prueba"`, `base="TC"` y `base="TS"`.

Lee con `leer_sentencias` (`parrafos=3` o `4`, `terminos` de la cuestión) solo lo que vayas a citar. Transcribe párrafos de fundamentos, nunca el relato de hechos ni datos de las partes de aquel pleito. La jurisprudencia va en la nota, nunca en la carta ni en la comunicación de audiencia.

## Cálculo de la indemnización si fuera improcedente

Muéstralo en tabla (en la nota si se entrega; si no, en el resumen; apartado 7 del formato), con cada operación visible:

| Concepto | Dato | Fuente |
|---|---|---|
| Salario bruto anual (12 meses, con prorrata de pagas y complementos salariales) | `[importe]` | nóminas |
| Salario diario (anual / 365) | | |
| Antigüedad (desde / hasta la fecha de efectos) en años y meses | | contrato, vida laboral |
| Días por año y tope | 33 días por año, prorrateo por meses, máximo 24 mensualidades | art. 56.1 ET leído |
| Indemnización | días × salario diario, con el tope | |

- Antigüedad anterior al 12/02/2012: hacen falta los dos tramos de la disposición transitoria undécima del ET. Pídela con `buscar_articulo` (`ley="ET"`, `articulo="disposición transitoria undécima"`); es un límite conocido del conector que no la devuelva (anclas, apartado 7). En ese caso léela en internet en el texto consolidado del BOE (https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430, disposición transitoria undécima) y cítala con el enlace y la fecha de consulta. Puedes apoyar el método de cálculo en la sentencia de la Sala Cuarta que aplica esas reglas (`consulta="cálculo indemnización despido improcedente antigüedad anterior 12 febrero 2012 disposición transitoria 720 días"`, `base="TS"`, `jurisdiccion="SOCIAL"`) si la lees. Calcula cada tramo por separado, con su prorrateo por meses, y aplica el tope de 720 días o, si el primer tramo lo supera, el de ese tramo con el máximo de 42 mensualidades. Solo si tampoco en internet aparece el texto, aplica la puerta y deriva el cálculo a `calculo-indemnizacion-despido`.
- Reducción de jornada por cuidado de menor o familiar (apartados 4 in fine, 5, 6 y 8 del art. 37 ET) o ejercicio a tiempo parcial de los permisos de nacimiento o parental: la indemnización se calcula con el salario que correspondería **sin la reducción**, mientras no haya vencido su plazo máximo (disposición adicional decimonovena del ET). El conector no devuelve las disposiciones adicionales: léela en internet en el texto consolidado del BOE y cítala con enlace. Pide el salario a jornada completa (o calcúlalo con el porcentaje de reducción).
- Añade la alternativa de readmisión con salarios de tramitación (art. 56.2 ET) y, si es representante o delegado, que la opción es del trabajador (art. 56.4 ET).
- En caso de nulidad: readmisión y salarios dejados de percibir (art. 55.6 ET), más la posible indemnización por lesión de derechos fundamentales: dilo sin cuantificarla.

## Documentos que se entregan

Todo en Word según `references/formato-y-organos-laboral.md`.

1. **Comunicación de audiencia previa** — `carta-audiencia-previa-<apellido-trabajador>-<AAAAMMDD>.docx`: membrete; destinatario; lugar y fecha; asunto «Comunicación de cargos y apertura de trámite de audiencia»; relación numerada de los hechos (los mismos de la carta futura); calificación provisional que la empresa baraja; plazo concreto (fecha y hora límite), forma de presentar alegaciones (escrito o reunión con acta, lugar y persona) y posibilidad de aportar documentos; advertencia de que la empresa decidirá tras valorarlas; firma y recibí.
2. **Constancia de la audiencia** — acta de la reunión o diligencia de recepción de las alegaciones (o de que no se presentaron), con fecha y firmas.
3. **Si procede**: comunicaciones del expediente contradictorio (interesado y representación) y de la audiencia a los delegados sindicales, con sus plazos.
4. **Carta de despido** — `carta-despido-disciplinario-<apellido-trabajador>-<AAAAMMDD>.docx`: membrete (`[DENOMINACIÓN SOCIAL]`, `[CIF]`); destinatario (`[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`); lugar y fecha; asunto; hechos numerados con fecha, lugar y conducta; referencia a la audiencia y a las alegaciones y por qué no desvirtúan los hechos; calificación (letra del art. 54.2 ET y artículo del convenio con su denominación y código); decisión de despido y **fecha de efectos**; puesta a disposición de la liquidación; firma; recibí o constancia ante testigos; copia a la representación si el convenio lo exige.
5. **Nota de riesgo para el abogado**, solo si el abogado la pide (si no, lo que esta skill manda «a la nota» —calendario, riesgos, cálculos y jurisprudencia con su ECLI— va en el resumen de la entrega) — `nota-despido-disciplinario-<empresa>-<AAAAMMDD>.docx`: calendario (conocimiento, fechas límite de prescripción, audiencia, entrega, efectos); comprobación de cada requisito formal con su artículo; garantías; riesgo de nulidad; valoración de la prueba; cálculo de la improcedencia en tabla; jurisprudencia literal (audiencia previa, suficiencia de la carta y la que sostenga la causa); plazo de caducidad del trabajador con fechas.

**Reparto para la redacción rápida:** la comunicación de audiencia previa, la constancia y la carta de despido son documentos cortos (1-3 páginas): cada uno en una sola sección, sin equipo. Si la carta lleva muchos hechos, dos secciones: encabezamiento y hechos / calificación, audiencia, efectos y firma.

Para el trabajador, en lugar de 1-5: **nota de revisión** — `nota-revision-carta-despido-<apellido-trabajador>-<AAAAMMDD>.docx` con los defectos, su efecto (improcedencia o nulidad), la jurisprudencia literal, el cálculo y el plazo.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: ET 54, 55, 56, 59, 60 y 68; LOLS 10; LRJS 43, 103, 105, 108 y 110; revisada la nota «Téngase en cuenta» del art. 55.5.
- [ ] Sentencia del Pleno sobre audiencia previa y una posterior que la aplique leídas con párrafo literal; comprobado que el despido es posterior al cambio de doctrina.
- [ ] Audiencia calendarizada y documentada antes de la carta, dentro del plazo de prescripción calculado con fechas.
- [ ] Expediente contradictorio y audiencia a delegados sindicales, si proceden.
- [ ] Convenio identificado, tipo de falta y requisitos formales leídos con `leer_convenio`, vigencia comprobada y modificaciones posteriores al texto leído localizadas en el boletín oficial (o señaladas como pendientes en la nota).
- [ ] Carta con hechos concretos y fechados, calificación, fecha de efectos y recibí; sin jurisprudencia.
- [ ] Cálculo de la improcedencia en tabla con salario real y antigüedad; tramo anterior al 12/02/2012 con la disposición transitoria undécima leída (BOE en internet, con enlace) y, si hay reducción de jornada por cuidado, salario sin reducir (disposición adicional decimonovena).
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; `verificar_escrito` pasado por cada redactor sobre las frases de su sección que citan normas (no sobre el documento entero) y los artículos del convenio contrastados con `leer_convenio`.
- [ ] Marcadores en vez de datos inventados.
- [ ] Resumen para el abogado según el apartado 9 del formato, con el calendario y el riesgo.
