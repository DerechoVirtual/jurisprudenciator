---
name: requerimiento-judicial-triage
description: Triage de resoluciones y citaciones penales. Identifica si el cliente es investigado o testigo, que plazo arranca y que hay que hacer. Cubre citacion como investigado art 118 LECrim, citacion de testigo, detencion, auto de incoacion, transformacion en abreviado, traslado para escrito de defensa, apertura de juicio oral, audiencia preliminar art 785, notificacion de sentencia y ejecutoria. Usar con hemos recibido una citacion, nos citan del juzgado, han detenido a un cliente o requerimiento judicial.
---

# Triage de resolución o citación penal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo que arranca** (arts. 118, 410, 420, 505, 784.1, 211, 212, 766, 790 y 856 LECrim) → `buscar_articulo` (`ley="LECrim"`).
- **Delito imputado y su pena** (decide el procedimiento y la prescripción) → `buscar_articulo` (`ley="CP"`).
- **Resoluciones citadas en el auto o la sentencia recibidos** → `buscar_por_cita` y, si hay que rebatirlas, `leer_sentencias` con `parrafos=3`.
- **Citación o notificación publicada por edicto** → `novedades_boe` (por número de procedimiento u órgano, no por el nombre del cliente) → `leer_boe`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

> 📐 **Cifras: `references/anclas-normativas-penal.md`**; lo que no esté ahí se verifica con `buscar_articulo` **antes** de afirmarlo.

**En penal, un "requerimiento" no es una demanda civil.** No hay emplazamiento para contestar, ni monitorio, ni oposición a la ejecución civil. Lo que llega es una **citación**, una **notificación** o un **auto**, y todo el triage se reduce a dos preguntas:

> ## ⭐ 1. ¿El cliente es INVESTIGADO o TESTIGO?
> ## ⭐ 2. ¿Qué plazo arranca, y desde cuándo?

**La diferencia entre investigado y testigo lo es todo.** No es un matiz de forma:

| | **Investigado / encausado** | **Testigo** |
|---|---|---|
| Derecho a **guardar silencio** | **Sí** — art. 118.1.g) LECrim y art. 24.2 CE | **No.** Obligación de declarar (art. 410 LECrim) |
| **No declarar contra sí mismo** | **Sí** — art. 118.1.h) LECrim y art. 24.2 CE | Solo la dispensa del art. 416 LECrim, si concurre |
| **Abogado** | **Sí** — designación libre o de oficio (art. 118.1.d y 118.2) | No preceptivo |
| **Acceso a las actuaciones** | **Sí**, con la debida antelación y **en todo caso antes de declarar** (art. 118.1.b) | No |
| **Si no comparece** | Requisitoria, busca, rebeldía; posible orden de detención | **Multa de 200 a 5.000 €** y posible delito de **obstrucción a la justicia del art. 463.1 CP** (art. 420 LECrim) |
| **Mentir** | No es delito (no está sujeto a juramento) | **Falso testimonio** |

> ⚠️ **Si hay la más mínima duda sobre la condición en que se cita al cliente, tratarlo como investigado hasta aclararlo con el juzgado.** Un cliente que declara como testigo cuando materialmente es investigado declara bajo obligación de decir verdad, sin abogado y sin acceso a las actuaciones. Es un daño que no se repara después.
>
> ⚠️ **Un testigo que puede autoincriminarse necesita abogado igualmente.** Si de la declaración puede resultar su propia imputación, plantear al juzgado su condición antes de la comparecencia.

## Cuándo activar

- "Nos ha llegado una citación del juzgado"
- "Citan a mi cliente como investigado / como testigo"
- "Han detenido a un cliente"
- "Nos han notificado un auto / una sentencia"
- "Nos dan traslado para escrito de defensa"
- "Requerimiento de la ejecutoria"
- Cualquier resolución penal entrante cuyo plazo o alcance no esté claro

## Flujo

### 1. Clasificar el documento

Tabla de resoluciones penales entrantes. **Verificar el artículo y el plazo con `buscar_articulo` antes de comunicárselo al cliente.**

| Documento | Plazo crítico | Acción típica |
|---|---|---|
| ⭐ **Citación como INVESTIGADO** (art. 118 LECrim) | Fecha de la comparecencia | **Activa el derecho de defensa.** Designar abogado, **examinar las actuaciones ANTES de la declaración** (art. 118.1.b), preparar al cliente |
| **Citación como TESTIGO** (art. 410 LECrim) | Fecha de la comparecencia | Comparecer. Valorar **dispensa del art. 416** y riesgo de autoincriminación |
| ⭐ **DETENCIÓN** (art. 520 LECrim) | **72 h** máximo para libertad o puesta a disposición judicial. **3 h** para que el abogado acuda (art. 520.5) | **Máxima urgencia.** Ver § 2 bis |
| **Auto de incoación** de Diligencias Previas / Urgentes | — (arranca el cómputo del art. 324) | **Anotar la fecha de incoación**: de ahí cuentan los 12 meses de instrucción |
| ⭐ **Auto de transformación en abreviado** (art. 779.1.4ª LECrim) | Recurso de reforma / apelación *(verificar plazo)* | Fija **hechos punibles y persona imputada**. Valorar recurso. **Requiere declaración previa del art. 775** — si no la hubo, es motivo de impugnación |
| **Auto de sobreseimiento** (art. 779.1.1ª) | **20 días** para que la **víctima** recurra, aunque no esté personada | Si defendemos: vigilar el recurso. Si acusamos: plazo para recurrir |
| **Auto de apertura de juicio oral** (art. 783 LECrim) | **No cabe recurso**, salvo en lo relativo a la **situación personal** (art. 783.3) | Reproducir ante el órgano de enjuiciamiento las peticiones no atendidas |
| **Emplazamiento tras apertura** (art. 784.1) | **3 días** para comparecer con abogado y procurador | Designar postulación |
| ⭐ **Traslado para ESCRITO DE DEFENSA** (art. 784.1) | **10 días comunes** desde el traslado | **Plazo de preclusión probatoria.** Ver § 2 ter |
| **Citación a la AUDIENCIA PRELIMINAR** (art. 785 LECrim) | Fecha de la comparecencia | **Asistencia preceptiva de acusado y defensor** (785.2). Sede de cuestiones previas, nulidades y **conformidad** |
| **Señalamiento del juicio oral** (art. 786) | Fecha del juicio | Asistencia preceptiva (art. 787.1). Ver § 2 quater |
| ⭐ **Notificación de SENTENCIA** | **10 días** apelación desde la notificación (art. 790.1, **Sección de lo Penal**). Casación: preparación en **5 días** (art. 856) | Ver § 2 quinquies |
| **Requerimiento de la EJECUTORIA** | Plazo del requerimiento | Liquidación de condena, **suspensión art. 80 CP**, responsabilidad civil |
| **Oficio al despacho** pidiendo documentación | Plazo del oficio | ⚠️ **Secreto profesional** — ver § 4 |
| **Citación a juicio de delito leve** | Fecha | Comparecer; valorar prueba |

### 2. Extraer datos

- **Órgano** emisor — **transcribe la denominación EXACTA que figure en la resolución**, sin
  «corregirla»: es la que después se copia en el encabezamiento de la respuesta. Denominaciones
  vigentes (art. 14 LECrim, desde el 3-10-2025): **Sección de Instrucción nº X del Tribunal de
  Instancia de [LUGAR]**, **Sección de Violencia sobre la Mujer**, ⭐ **Sección de Violencia contra
  la Infancia y la Adolescencia** (órgano nuevo, art. 14.6), **Sección de lo Penal**, AP Sección X,
  TSJ, AN, TS Sala Segunda, Juzgado Central de Instrucción, **Sección de Vigilancia Penitenciaria**
  y **Sección de Menores** (art. 84.2.g y f LOPJ: **también son Secciones**, no Juzgados aparte).
  > **Art. 14.7:** si concurren violencia contra la infancia **y** violencia sobre la mujer, la
  > competencia es **en todo caso** de la **Sección de Violencia sobre la Mujer**.
  > Si la resolución aún se rotula «Juzgado de …», **anótalo tal cual**: no es un defecto (la
  > **DA 1.ª de la LO 1/2025** manda entender esa mención hecha a la Sección correspondiente).
- **Procedimiento** y número (Diligencias Previas / Urgentes / Procedimiento Abreviado / Sumario / Ejecutoria)
- ⭐ **Condición en que se dirige al cliente**: investigado / encausado / acusado / testigo / perjudicado / responsable civil / tercero
- **Delito** que se atribuye y **fecha de los hechos** (→ ley aplicable, art. 2 CP)
- **Fecha del documento** y **fecha de notificación** (el cómputo va desde la **notificación**)
- **Plazo concedido**
- **Documentos adjuntos** y si se acompaña copia de las actuaciones

### 2 bis. Si hay DETENCIÓN — protocolo urgente

**Verificado 2026-07-17 (`references/anclas-normativas-penal.md` § 8):**

- **Plazo del abogado: 3 horas.** El designado debe acudir al centro de detención con la máxima premura y **siempre dentro de un máximo de 3 horas** desde la recepción del encargo (art. 520.5). Si no comparece, el Colegio designa otro, sin perjuicio de responsabilidad disciplinaria.
- **Duración de la detención:** no más del **tiempo estrictamente necesario**; **máximo 72 horas** para poner en libertad o a disposición judicial (art. 520.1).
- ⭐ **Entrevista reservada con el detenido INCLUSO ANTES de que se le reciba declaración** (art. 520.6.d), salvo art. 527. **Ejercerla siempre.**
- **Contenido de la asistencia** (art. 520.6): pedir información de derechos y **reconocimiento médico**; **intervenir** en la declaración, reconocimientos y reconstrucción de hechos; pedir, una vez terminada la diligencia, la **ampliación** de extremos y la **consignación en acta de cualquier incidencia**; informar sobre el consentimiento a las diligencias.
- **Derechos del detenido** (art. 520.2), informados **por escrito** y de forma inmediata: silencio; no declarar contra sí mismo; abogado; **acceso a los elementos esenciales para impugnar la legalidad de la detención**; comunicación a un familiar; llamada a un tercero; consulado; intérprete; médico forense; justicia gratuita. **Conserva en su poder la declaración escrita de derechos** durante toda la detención.
- **Confidencialidad** de las comunicaciones abogado-detenido: art. 520.7, con remisión al art. 118.4.
- **Renuncia a la asistencia letrada:** **solo** cabe si la detención lo es por hechos tipificables **exclusivamente como delitos contra la seguridad del tráfico**, y es **revocable en cualquier momento** (art. 520.8).
- **Menor:** a disposición de la Sección de Menores de la Fiscalía; comunicación a los titulares de la patria potestad; **defensor judicial** si hay conflicto de intereses (art. 520.4).
- Valorar **habeas corpus** (LO 6/1984) si la detención es ilegal o se prolonga indebidamente.

### 2 ter. Si es traslado para ESCRITO DE DEFENSA — art. 784.1

**Verificado 2026-07-17.**

- **10 días comunes** desde el traslado de las actuaciones.
- ⚠️ **Si no se presenta en plazo, se entiende que la defensa se OPONE** a las acusaciones y el procedimiento sigue su curso — pero con **responsabilidad disciplinaria** del letrado (Título V del Libro V LOPJ).
- ⭐ **Preclusión probatoria — el riesgo real:** precluido el trámite, la defensa **solo podrá proponer la prueba que aporte en el acto del juicio oral** para su práctica en el mismo, sin perjuicio de interesar previamente las comunicaciones necesarias con antelación suficiente, y de lo previsto en el art. 785.1 párr. 2. **Perder este plazo no es un defecto formal: es perder la prueba.**
- En el escrito puede pedirse que se recabe la remisión de documentos o se cite a peritos y testigos (art. 784.2).
- El escrito de defensa lo firma **también el acusado** (art. 784.3).

### 2 quater. Si es citación a la AUDIENCIA PRELIMINAR o al JUICIO ORAL

- **Audiencia preliminar (art. 785):** requiere asistencia del **acusado y del abogado defensor** (785.2). **No se suspende** por inasistencia injustificada del acusado debidamente citado; se celebra para lo que pueda resolverse en ausencia. Es la sede de: conformidad, competencia, **vulneración de derechos fundamentales**, artículos de previo pronunciamiento, **nulidad de actuaciones** y **nulidad de las pruebas**.
  > ⚠️ **Las cuestiones previas ya NO se plantean al inicio del juicio.** Su sede es la audiencia preliminar (LO 1/2025). Al inicio del juicio solo cabe pedir la incorporación de informes, certificaciones y documentos, y la prueba de la que no se tuvo conocimiento en la audiencia preliminar (art. 787.3).
- **Juicio oral (art. 787.1):** asistencia **preceptiva** del acusado y del defensor. La **ausencia injustificada** del acusado citado en forma solo permite celebrar si concurren **acumulativamente**: a) que la pena más grave solicitada no exceda de **2 años** de privación de libertad (o **6 años** si es de distinta naturaleza, o multa cualquiera que sea su cuantía); **y** b) tratándose de penas privativas de libertad, que **la suma total de las solicitadas no exceda de 5 años**.

### 2 quinquies. Si es NOTIFICACIÓN DE SENTENCIA

- **Apelación contra sentencia de la Sección de lo Penal: 10 días** desde la notificación (art. 790.1). La petición de copia de las grabaciones dentro de los **3 días** suspende el plazo, que **se reanuda** al entregarse las copias.
- **Casación: preparación en 5 días** desde la última notificación (art. 856), por escrito autorizado por abogado y procurador.
- ⚠️ **Casación — el motivo depende de la resolución recurrida** (art. 847, `anclas` § 4). Contra sentencias dictadas **en apelación por las Audiencias Provinciales**: **SOLO infracción de ley del art. 849.1º**. Plantear otro motivo → inadmisión.
- **Si la sentencia es de conformidad:** solo recurrible si **no se respetaron los requisitos o términos** de la conformidad; **el acusado no puede impugnar por razones de fondo** su conformidad libremente prestada (art. 785.10).

### 3. Cross-check de cartera

Buscar en `_log.yaml`:
- ¿Asunto abierto coincidente?
- ¿Procedimiento ya conocido o nuevo?
- ⭐ **¿Hay conflicto?** ¿Defendemos ya a otro investigado en esta misma causa? ¿A la persona jurídica y ahora citan a la física? Si es así, **parar** (art. 467.1 CP).
- ¿Coincide con la **fecha de incoación** anotada? Recalcular el plazo del art. 324.

### 4. Análisis de respuesta

**Si el cliente es investigado:**
- **Examinar las actuaciones antes de la declaración** — derecho del art. 118.1.b). Si no se da acceso, hacerlo constar y no declarar.
- ¿Declara o guarda silencio? Decisión estratégica, **informada y del cliente**.
- ¿Procede recurso (reforma / apelación) contra el auto? *(verificar plazos: reforma 3 días art. 211; apelación 5 días art. 766 — **verificar antes de citar**)*
- ¿Procede pedir diligencias de descargo antes del vencimiento del plazo de instrucción?
- ⭐ **Control del art. 324:** ¿se dictó auto de prórroga **antes** del vencimiento? Si no, **las diligencias acordadas a partir de esa fecha no son válidas** (art. 324.3). Es el argumento de nulidad más rentable y más desatendido.

**Si el cliente es testigo:**
- ¿Concurre la **dispensa del art. 416 LECrim**? (pariente en línea directa, cónyuge o pareja de hecho análoga, hermanos y colaterales consanguíneos hasta 2º grado). ⚠️ **Verificar las excepciones del art. 416.1**: representación legal o guarda de hecho de la víctima menor o con discapacidad; delito grave con víctima menor o con discapacidad; testigo que no comprende el sentido de la dispensa; **testigo que esté o haya estado personado como acusación particular**; **testigo que ya aceptó declarar tras ser informado de su derecho a no hacerlo**.
- ¿Riesgo de **autoincriminación**? → plantear su condición al juzgado antes de comparecer.
- Si no comparece: **multa de 200 a 5.000 €** y posible **art. 463.1 CP** (art. 420 LECrim).

**Si el oficio se dirige al despacho pidiendo documentación:**
- ⚠️ **Secreto profesional — art. 542.3 LOPJ**: el abogado debe guardar secreto de todos los hechos o noticias que conozca por razón de su actuación profesional, **no pudiendo ser obligado a declarar sobre los mismos**.
- **Art. 416.2 LECrim**: el abogado del procesado está **dispensado de declarar** respecto de los hechos que este le hubiese confiado en su calidad de defensor.
- **Art. 118.4 LECrim**: las comunicaciones entre investigado y abogado son **confidenciales**.
- → **Oposición motivada antes de entregar nada.** Pasar por `/revision-secreto-profesional`.

### 5. Output

`inbound/<slug>/triage.md`:

```markdown
# Triage — [tipo de resolución] [slug]

**Tipo:** [...]
**Órgano:** [Sección de Instrucción nº X del Tribunal de Instancia de (LUGAR) / .. — *tal y como se rotule en la resolución*]
**Procedimiento:** [Diligencias Previas nº X / ...]
**Delito atribuido:** [...]
**Fecha de los hechos:** [...] → ley aplicable: [art. 2 CP]
**Fecha de notificación:** [...]

## ⭐ Condición del cliente
[INVESTIGADO / TESTIGO / acusado / perjudicado / responsable civil / tercero]
[Si hay duda: "SIN ACLARAR — tratar como investigado hasta confirmar con el juzgado"]

## ⭐ Plazo que arranca
[Plazo] — vence el [fecha] — [artículo, verificado / marcado [verificar]]
[Margen de seguridad de la casa: presentar el (fecha − 2 días hábiles)]

## Qué hay que hacer antes de esa fecha
[Pasos concretos]

## Análisis
- ¿Asunto abierto en cartera? [sí: slug / no]
- ¿Conflicto de interés? [no / SÍ — parar]
- ¿Acceso a las actuaciones solicitado? [sí/no]
- ¿Plazo de instrucción (art. 324) bajo control? [fecha de incoación / prórrogas / vencimiento]
- ¿Procede recurso? [sí: cuál y plazo / no: por qué]

## Plan de actuación
[Pasos con responsable y fecha]
```

### 6. Decision tree

> **¿Qué hago ahora?**
> 1. **Solicitar acceso a las actuaciones** — si el cliente es investigado y aún no se ha pedido (art. 118.1.b)
> 2. **Preparar la comparecencia** — declaración o silencio, con el cliente
> 3. **Recurrir** — reforma / apelación, si procede y está en plazo
> 4. **Escrito de defensa** — si el traslado del art. 784.1 está corriendo
> 5. **Comunicar al cliente** — borrador con el plazo y la decisión que le corresponde
> 6. **Vigilancia de plazo** — anotar vencimiento y control del art. 324

## Reglas

1. ⭐ **Identificar SIEMPRE si el cliente es investigado o testigo.** Es la primera línea del output. Ante la duda, tratarlo como **investigado**.
2. ⭐ **Identificar SIEMPRE qué plazo arranca y desde cuándo.** El cómputo va desde la **notificación**, no desde la fecha del auto.
3. **Verificar cada artículo y cada plazo con `buscar_articulo`** antes de comunicárselo al cliente. Si no se puede verificar, marcar `[verificar]` y decirlo.
4. **Si la notificación llega al procurador**, el plazo arranca ahí — confirmar el día.
5. **Agosto**: inhábil con carácter general, **pero las actuaciones de instrucción y las urgentes son hábiles** (art. 183 LOPJ — *verificar antes de aplicar*). **Los plazos de un detenido no conocen agosto.**
6. **Secreto profesional como límite** (art. 542.3 LOPJ; arts. 118.4 y 416.2 LECrim): si el oficio pide documentación cubierta, **oposición motivada antes de entregar**.
7. **Prioridad absoluta a la detención.** El plazo de 3 horas del art. 520.5 se antepone a cualquier otra tarea de esta skill.
8. ⛔ **No aplicar plazos ni instituciones civiles.** No hay emplazamiento de 20 días para contestar, ni monitorio, ni oposición a la ejecución de la LEC, ni diligencias preliminares del art. 256 LEC, ni cómputo del art. 133 LEC.
9. ⛔ **No existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. La reforma está en tramitación (prevista 1-1-2028): no citarla como Derecho vigente.
10. ⛔ **Prohibido citar jurisprudencia concreta** (ECLI/ROJ/fecha) sin verificarla con `jurisprudenciator`.
11. **Cero datos reales** en los outputs de ejemplo: `[CLIENTE]`, `[LUGAR]`, `[X]`.
