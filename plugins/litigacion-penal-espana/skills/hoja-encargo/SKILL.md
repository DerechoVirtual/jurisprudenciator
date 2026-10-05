---
name: hoja-encargo
description: Hoja de encargo profesional del despacho penal conforme a EGA, Ley 10/2010 PBC y RGPD. Genera Word maquetado con objeto del encargo en clave penal, extension por fases (instruccion, intermedia, juicio oral, recursos, ejecutoria), regimen propio de costas penales, advertencia de conformidad y firmas. Usar con redactar hoja de encargo, contrato de servicios juridicos, aceptar nuevo asunto penal o documentar el encargo del cliente.
---

# Hoja de encargo profesional — penal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen propio de costas penales** (arts. 123-126 CP y 239-241 LECrim) → `buscar_articulo`.
- **Cliente persona jurídica: denominación, CIF, domicilio y quién puede firmar** → `buscar_empresa_mercantil` (administradores y apoderados vigentes; sirve también para la identificación de la Ley 10/2010).
- **Cláusulas de secreto profesional y protección de datos** → `buscar_articulo` (`ley="LOPJ"`, `articulo="542"`; `ley="RGPD"`, `articulo="10"`).
- **Ley 10/2010 y LO 3/2018** → `buscar_boe` para su ID BOE y `buscar_articulo` con él.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Documento contractual entre letrado y cliente que formaliza el encargo de **defensa o acusación en un procedimiento penal** y blinda al despacho frente a impagos, expectativas mal fijadas y discusiones sobre la extensión del encargo.

> 📐 **Cifras: `references/anclas-normativas-penal.md`**; lo que no esté ahí, se verifica con `buscar_articulo` antes de afirmarlo.

## Marco legal

- **Estatuto General de la Abogacía (RD 135/2021)** — relación con el cliente; hoja de encargo por escrito
- **Código Deontológico de la Abogacía** — información previa, honorarios, cuota litis
- **Arts. 123-126 CP y 239-241 LECrim** — **régimen propio de costas del orden penal** (ver § 5)
- **Art. 785 LECrim** (redacción LO 1/2025) — audiencia preliminar y **conformidad**
- **Art. 542.3 LOPJ** — secreto profesional
- **Ley 10/2010** de prevención del blanqueo de capitales — sujeción del abogado en determinadas actividades
- **RGPD (UE) 2016/679 + LO 3/2018** — con mención expresa al **art. 10 RGPD** (datos relativos a infracciones y condenas penales)
- **LEC 35** (jura de cuentas) — **supletorio**: habilita la reclamación de honorarios al cliente. Sin hoja de encargo firmada, la reclamación se debilita.

> ⛔ **Aquí NO hay MASC.** El MASC de la LO 1/2025 es requisito de procedibilidad del orden **civil**. En penal no existe intento previo de MASC ni burofax como requisito, y **no se informa al cliente de ninguna obligación de MASC**. Lo más próximo, y solo en supuestos tasados, son la **querella** o la **denuncia del ofendido** en delitos privados y semipúblicos, y el **acto de conciliación del art. 804 LECrim** en injurias y calumnias.
>
> ⛔ **No trasladar el art. 394 LEC ni el criterio civil del vencimiento.** En penal el régimen es otro y es más favorable al defendido (§ 5).

## Cuándo activar

- "Redacta una hoja de encargo para [CLIENTE]"
- "Contrato de servicios para el asunto [X]"
- "Documento de aceptación del encargo"
- Al aceptar un nuevo asunto penal, antes de iniciar trabajo facturable
- Tras una asistencia al detenido en turno de oficio que el cliente quiera continuar con designación particular

## Flujo — siete fases

Las fases son el contenido que debe tener la hoja, no una cadena de pasos: los datos se cierran antes de redactar (pasos 2-3 de `redaccion-rapida`) y la redacción la hace el equipo.

### 1. Datos del despacho (auto-rellenar desde el perfil)

Leer de `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md`:

- `[LETRADO]` — nombre del letrado
- Colegio profesional + nº de colegiado
- Domicilio profesional
- Email y teléfono
- Logo: `[logo del despacho, si se aporta]`

Si algún campo aparece como `[PLACEHOLDER]`, déjalo como `[PENDIENTE: dato]` y lístalo en la entrega; pregunta **solo ese dato** si bloquea.

### 2. Datos del cliente — mínimos

Sácalos de la documentación aportada; los que falten se piden en la única ronda de preguntas del paso 2 de `redaccion-rapida` (datos que NO se inventan). **Todos van al documento como marcadores hasta que el usuario los aporte:**

- `[CLIENTE]` — nombre completo o razón social
- `[DNI]` — DNI / NIE / CIF
- `[DOMICILIO]`
- `[TELEFONO]` y `[EMAIL]`
- Si es persona jurídica: representante legal y cargo — y **representante especialmente designado con poder especial** para el proceso penal (art. 785.11 LECrim)
- **Posición procesal del cliente**: investigado / encausado / acusado / penado / víctima o perjudicado / responsable civil subsidiario

> ⚠️ **Comprobación de conflicto antes de firmar.** Si el despacho ya defiende a otro investigado en la misma causa, o a la persona jurídica y se pretende asumir también a la persona física (o viceversa), **parar**. El **art. 467.1 CP** *(verificado 2026-07-17)* castiga con **multa de 6 a 12 meses e inhabilitación especial de 2 a 4 años** al abogado que, habiendo asesorado o tomado la defensa de una persona, **sin su consentimiento** defienda o represente en el mismo asunto a quien tenga intereses contrarios.

### 3. Objeto del encargo — en clave penal

Redactar el objeto con la fórmula del orden penal, no con la civil:

> «**Defensa de [CLIENTE] en las Diligencias Previas nº [X] seguidas ante la Sección de Instrucción nº [X] del Tribunal de Instancia de [LUGAR] por un presunto delito de [TIPO].**»

Variantes según el caso, ajustando el procedimiento y el órgano realmente existentes:

> ⭐ **Identifica el órgano copiando la denominación EXACTA de la resolución o de la carátula del
> procedimiento.** La hoja de encargo delimita el objeto contractual: debe identificar el
> procedimiento tal y como existe, no como debería llamarse. La nomenclatura vigente (art. 14
> LECrim, desde el 3-10-2025) es la de **Sección del Tribunal de Instancia**.

| Situación | Fórmula |
|---|---|
| Instrucción en curso | Diligencias Previas nº [X] ante la Sección de Instrucción nº [X] del Tribunal de Instancia de [LUGAR] |
| Juicio rápido | Diligencias Urgentes nº [X] ante la Sección de Instrucción nº [X] del Tribunal de Instancia de [LUGAR], en funciones de guardia |
| Enjuiciamiento abreviado | Procedimiento Abreviado nº [X] ante la Sección de lo Penal nº [X] del Tribunal de Instancia de [LUGAR] |
| Violencia de género | ante la Sección de Violencia sobre la Mujer nº [X] del Tribunal de Instancia de [LUGAR] |
| ⭐ Violencia contra la infancia y la adolescencia | ante la Sección de Violencia contra la Infancia y la Adolescencia nº [X] del Tribunal de Instancia de [LUGAR] (art. 14.6; **si concurre con violencia sobre la mujer, art. 14.7: competencia de esta última en todo caso**) |
| Sumario / jurado | ante la Audiencia Provincial de [PROVINCIA], Sección [X] |
| Acusación particular | Ejercicio de la acusación particular en [procedimiento] en nombre de [CLIENTE] como perjudicado por un presunto delito de [TIPO] |
| Ejecutoria | Ejecutoria nº [X] dimanante de [procedimiento] |
| Asistencia al detenido | Asistencia letrada a [CLIENTE] en situación de detención en [dependencias], y en su caso continuación del encargo |

**Capturar además:** órgano, número de procedimiento (si ya existe), delito imputado, fecha de los hechos y de la incoación.

> ⚠️ **Fecha de los hechos — anotarla siempre.** Determina la **ley penal aplicable** (art. 2 CP) y si procede la retroactividad de la norma más favorable (art. 2.2 CP). Con las reformas de 2025 y 2026 no es un dato accesorio.

### 4. ⭐ Extensión del encargo POR FASES — apartado crítico

**El cliente suele creer que la sentencia cierra el asunto. No es así.** Este apartado existe para impedir esa confusión y la discusión de honorarios que la sigue. Marcar expresamente **qué fases cubre** el encargo y cuáles no:

| Fase | Qué comprende | ¿Incluida? |
|---|---|---|
| **1. Instrucción** | Asistencia a declaración como investigado (art. 118 LECrim), proposición de diligencias, recursos de reforma y apelación contra autos, control del plazo de instrucción (art. 324 LECrim), medidas cautelares | [Sí/No] |
| **2. Fase intermedia** | Escrito de defensa (plazo de **10 días** comunes desde el traslado, art. 784.1 LECrim), petición de sobreseimiento, oposición a la apertura de juicio oral | [Sí/No] |
| **3. Juicio oral** | **Audiencia preliminar del art. 785 LECrim** (cuestiones previas, nulidades, prueba, conformidad), señalamiento (art. 786) y celebración del juicio (art. 787) | [Sí/No] |
| **4. Recursos** | Apelación (**10 días** desde la notificación de la sentencia de la **Sección de lo Penal**, art. 790.1), casación (preparación en **5 días**, art. 856), amparo | [Sí/No — pactar honorarios aparte por cada instancia] |
| **5. ⭐ Ejecutoria** | **Liquidación de condena**, **suspensión de la ejecución (art. 80 CP)**, sustitución, **responsabilidad civil** y su fraccionamiento (art. 125 CP), cancelación de antecedentes, incidencias ante la **Sección de Vigilancia Penitenciaria** (art. 84.2.g y 92 LOPJ) | [Sí/No] |

> **Texto que debe aparecer en el documento, destacado:**
>
> «**La sentencia no agota el procedimiento.** Aun después de dictada —incluso si es de conformidad— resta la fase de **ejecutoria**, en la que se practica la **liquidación de condena**, se resuelve sobre la **suspensión de la ejecución de la pena privativa de libertad** conforme al art. 80 CP, y se exige el pago de la **responsabilidad civil**. Estas actuaciones [están / **no están**] comprendidas en el presente encargo y, en su caso, se minutarán conforme a [modalidad].»

Si el alcance **no** incluye una fase, dejarlo explícito. Es la fuente número uno de conflicto con el cliente en penal.

### 5. ⭐ Advertencia sobre COSTAS PENALES — régimen propio

**Verificado con `buscar_articulo` el 2026-07-17.** No trasladar el vencimiento objetivo del art. 394 LEC: en penal **no existe**.

**Lo que dice la ley (literal verificado):**

- **Art. 123 CP** — «Las costas procesales se entienden impuestas por la ley a los **criminalmente responsables** de todo delito.» → las costas siguen a la **condena penal**, no al vencimiento.
- **⭐ Art. 240.2º LECrim** — «**No se impondrán nunca las costas a los procesados que fueren absueltos.**» → **el absuelto nunca paga costas.** Ni las suyas por condena, ni las de la acusación.
- **Art. 240.3º LECrim** — el **querellante particular o actor civil** solo es condenado en costas «cuando resultare de las actuaciones que han obrado con **temeridad o mala fe**». → Quien ejerce la acusación particular y pierde **no** paga costas por el mero hecho de perder.
- **Art. 240.1º LECrim** — cabe declarar las costas **de oficio**.
- **Art. 239 LECrim** — en los autos o sentencias que pongan término a la causa o a cualquier incidente **debe resolverse** sobre las costas.
- **Art. 124 CP** — las costas comprenden los derechos e indemnizaciones ocasionados en las actuaciones judiciales, e incluyen **siempre** los honorarios de la acusación particular en los **delitos solo perseguibles a instancia de parte**.
- **Art. 241 LECrim** — contenido de las costas: reintegro del papel sellado, derechos de arancel, **honorarios de abogados y peritos**, indemnizaciones a testigos y demás gastos de la instrucción.
- **Art. 126 CP** — **orden de imputación de pagos** del penado: 1.º reparación del daño e indemnización de perjuicios; 2.º indemnización al Estado; 3.º costas del acusador particular o privado; 4.º demás costas procesales, **incluidas las de la defensa del procesado**; 5.º multa.
- **Art. 125 CP** — si los bienes no bastan, el juez, **previa audiencia del perjudicado**, puede **fraccionar** el pago según las necesidades del perjudicado y las posibilidades económicas del responsable.

**Cómo explicárselo al cliente en el documento:**

1. **Si el cliente es defendido y resulta absuelto:** no se le impondrán costas (art. 240.2º LECrim). **Pero los honorarios pactados con este despacho se devengan igualmente** — la absolución no los hace gratuitos, y no existe en penal un mecanismo por el que la acusación se los reembolse salvo condena en costas a un querellante temerario.
2. **Si el cliente es defendido y resulta condenado:** las costas se le imponen por ley (art. 123 CP) y comprenden los honorarios de abogado y perito (art. 241 LECrim) y, en delitos privados, los de la acusación particular (art. 124 CP).
3. **Si el cliente ejerce la acusación particular y la causa termina en absolución o sobreseimiento:** por regla general **no** se le imponen costas; solo si actuó con **temeridad o mala fe** (art. 240.3º LECrim). Advertirlo sin dramatizar, pero advertirlo.
4. **Prioridad de pagos:** si el cliente es condenado y su patrimonio no alcanza, la ley cobra primero a la víctima y al Estado; **los honorarios de su propia defensa van en cuarto lugar** (art. 126.1.4º CP). Esto explica por qué el despacho pide provisión.

### 6. ⭐ Advertencia sobre la CONFORMIDAD

Bloque destacado, obligatorio en toda hoja de encargo de defensa:

1. **Quién decide: el cliente.** La conformidad es una decisión **del defendido**, no del letrado. El abogado informa, aconseja y calcula; **no consiente por él**. El art. 785.5 LECrim prevé que el órgano judicial oiga al acusado sobre si prestó su conformidad **libremente** y si conoce sus consecuencias.
2. **⭐ Deber del art. 785.7 in fine LECrim** *(redacción LO 1/2025)*: «**El letrado o la letrada facilitará por escrito a la persona a quien defiende la información sobre el acuerdo alcanzado.**» → **Documentarlo siempre.** La hoja de encargo debe recoger que el despacho entregará esa información por escrito, y el despacho debe conservar acuse.
3. **⭐ Irrecurribilidad de fondo — art. 785.10 LECrim:** las sentencias de conformidad solo son recurribles cuando **no se hayan respetado los requisitos o términos** de la conformidad. **El acusado NO puede impugnar por razones de fondo su conformidad libremente prestada.** Decírselo al cliente antes, por escrito, y no después: es irreversible.
4. **Límites de la conformidad** (art. 785.4): no puede referirse a **hecho distinto** ni contener **calificación más grave** que la del escrito de acusación anterior.
5. **La víctima será oída** (art. 785.4 párr. 2): el Ministerio Fiscal oirá previamente a la víctima o perjudicado cuando sea posible y se estime necesario, y **en todo caso** si la gravedad o la cuantía son especialmente significativas, y **siempre** si la víctima está en situación de **especial vulnerabilidad**.
6. **Persona jurídica** (art. 785.11): la conformidad la presta su **representante especialmente designado con poder especial**; es independiente de la de los demás acusados y **no les vincula**.
7. **Juicio rápido** (art. 801): si concurren los requisitos, la conformidad ante el juzgado de guardia da lugar a sentencia con la pena **reducida en un tercio**. Explicar el incentivo sin prometer resultado.

> ⚠️ **Defecto de coordinación legislativa.** El **art. 784.3** LECrim sigue remitiendo al **art. 787** para la conformidad, y el 801 también, pero el régimen sustantivo está hoy en el **art. 785** (LO 1/2025). Al redactar, citar el art. 785 como sede de la conformidad. Ver `references/anclas-normativas-penal.md` § 2.2.

### 7. Honorarios — modalidad

Cuatro modalidades. Si el abogado no ha dicho cuál, inclúyela en la única ronda de preguntas del paso 2 de `redaccion-rapida`; si sigue sin decirse, redacta con presupuesto cerrado por fase (la recomendada) y deja las cifras como `[PENDIENTE: importe]`:

1. **Presupuesto cerrado** — cantidad fija acordada, **por fase** (recomendado en penal, dada la estructura del § 4)
2. **Por hora** — tarifa horaria con estimación
3. **Criterios orientadores del Colegio** — minuta según baremo
4. **Cuota litis pura: prohibida.** En penal carece además de sentido en la defensa: no hay "éxito" cuantificable. Solo cabría pacto sobre resultado con parte fija mínima en el ejercicio de la **acusación particular** con reclamación de responsabilidad civil.

Para cada modalidad, capturar:

- Cantidad o tarifa **por fase** (instrucción / intermedia / juicio oral / recursos / ejecutoria)
- IVA (21% salvo exención aplicable)
- **Provisión de fondos**: cuantía, momento, justificación
- Forma de pago: transferencia bancaria a **`[IBAN]`** del despacho *(no inventar; tomarlo del perfil o dejar el marcador)*
- **Devengos parciales**: qué se cobra si el cliente revoca, si hay **conformidad temprana** (que reduce el trabajo pero no lo elimina — la negociación y el cálculo de pena son el trabajo), o si la causa se **sobresee** en instrucción
- **Honorarios del procurador** — no incluidos en los del abogado
- **Periciales de parte** (forense, calígrafo, informático forense, tasador), **gastos de desplazamiento**, testimonios y copias: a cargo del cliente
- **Turno de oficio:** si el cliente venía de una designación de oficio y pasa a designación particular, dejar constancia de la fecha del cambio y de la renuncia al beneficio de justicia gratuita si la hubiere

### 8. Advertencias obligatorias

Bloque destacado. NO se elimina ni se suaviza:

1. **Costas penales** — según § 5, con el régimen propio ya explicado.
2. **Resultado incierto** — la defensa puede resultar infructuosa por razones ajenas a la diligencia del letrado (prueba practicada, valoración judicial, criterio del órgano). **Prohibido garantizar absolución, sobreseimiento, conformidad concreta o suspensión de la pena.**
3. **La sentencia no cierra el asunto** — remisión al § 4 (ejecutoria).
4. **Conformidad** — según § 6.
5. **Ley 10/2010 PBC** — obligación del letrado de comunicar al SEPBLAC operaciones sospechosas en los supuestos sujetos; información al cliente. Advertir de que el asesoramiento en el marco de la **defensa en un proceso penal** goza de la protección del secreto profesional en los términos legalmente previstos.
6. **Delegación en colaboradores** — posibilidad de apoyarse en otros profesionales del despacho o colaboradores externos, sin incremento de honorarios. En **guardia y turno de oficio**, indicar quién cubre si el letrado no está disponible (recordar el plazo de **3 horas** del art. 520.5 LECrim).
7. **Renuncia y revocación** — el cliente puede revocar el encargo en cualquier momento; los honorarios devengados hasta la revocación siguen siendo exigibles. El letrado puede renunciar conforme al EGA, **sin causar indefensión** y respetando los plazos en curso.
8. **Deber de veracidad del cliente** — la defensa se construye sobre lo que el cliente cuenta; la información incompleta o falsa compromete la estrategia. **El abogado no puede en ningún caso aconsejar destruir, alterar u ocultar prueba** (ver `/conservacion-documental`).

### 9. Protección de datos — cláusula RGPD + LO 3/2018

Bloque obligatorio, con la especialidad penal:

- **Responsable:** `[LETRADO]` / `[DESPACHO]`
- **Finalidad:** prestación de los servicios jurídicos de defensa o acusación contratados
- **Base jurídica:** ejecución del contrato (art. 6.1.b RGPD) + obligación legal (art. 6.1.c) + interés legítimo en la defensa (art. 6.1.f)
- **⭐ Art. 10 RGPD — datos relativos a infracciones y condenas penales.** Mención expresa: el tratamiento de datos personales relativos a **condenas e infracciones penales** o medidas de seguridad conexas está sometido al régimen reforzado del art. 10 RGPD y del art. 10 LO 3/2018. El expediente penal contiene datos de esta naturaleza **del propio cliente y de terceros** (víctimas, testigos, otros investigados).
- **⭐ Secreto profesional — art. 542.3 LOPJ** *(literal verificado)*: los abogados «deberán guardar secreto de todos los hechos o noticias de que conozcan por razón de cualquiera de las modalidades de su actuación profesional, **no pudiendo ser obligados a declarar sobre los mismos**». Complementar con la **confidencialidad de las comunicaciones abogado-cliente del art. 118.4 LECrim**.
- **Plazo de conservación:** durante la relación + plazos legales aplicables. Advertir de que en penal el plazo relevante puede extenderse por la **prescripción de la pena** (art. 133 CP) y la **cancelación de antecedentes** (art. 136 CP).
- **Cesiones:** a procurador, peritos de parte, órgano judicial y demás partes en el marco del procedimiento. **No se cederán a terceros ajenos al proceso.**
- **Derechos:** acceso, rectificación, supresión, oposición, limitación y portabilidad, ante el despacho y, en su caso, ante la **AEPD**.

### 10. Jurisdicción y firma

- Sometimiento a los tribunales del domicilio del despacho para las controversias derivadas **del contrato** (cláusula válida entre empresarios; si el cliente es **consumidor** —persona física no profesional— prevalece su fuero: el domicilio del consumidor). En la práctica, el cliente penal persona física será casi siempre consumidor a estos efectos.
- **Doble firma:** `[LETRADO]` + `[CLIENTE]`, con DNI debajo
- Lugar y fecha

**Reparto para la redacción rápida:** las cláusulas llevan el rótulo `### [ESTIPULACION]`, que el ensamblador numera en femenino (PRIMERA.-, SEGUNDA.-…). 01 comparecencia con los datos de las partes (§ 1-2), objeto del encargo y extensión por fases con su tabla (§ 3-4) · 02 costas penales y conformidad (§ 5-6) · 03 honorarios y advertencias obligatorias (§ 7-8) · 04 protección de datos, jurisdicción, lugar, fecha y doble firma (§ 9-10). Si la hoja no pasa de cuatro páginas, redáctala sin equipo.

## Maquetación del Word

**Diseño corporativo del despacho:**

- Logo: `[logo del despacho]` (cabecera, columna izquierda) — opcional
- Paleta (DEFAULT — ajustar a los colores de marca cuando se definan):
  - Color de títulos `#B8860B`
  - Fondo suave `#F5EBD7`
  - Gris oscuro texto `#333333`
  - Gris medio secundario `#666666`
- Fuente: Arial 11 cuerpo, 12 títulos
- Página: A4, márgenes 2 cm
- Cabecera: tabla de 2 columnas sin bordes (logo + título "HOJA DE ENCARGO PROFESIONAL")
- Campos: tablas con borde gris claro 1 pt
- **Tabla de extensión por fases** (§ 4): destacada, con casillas marcables
- Bloques de **advertencias**, **costas** y **conformidad**: cuadro con fondo dorado claro y borde dorado a la izquierda de 3 pt
- Firmas: tabla de 2 columnas, altura fija 5 cm para firma manuscrita
- Pie: nº de página + dominio del despacho

**Generación:**

- El Word lo genera el ensamblado de `redaccion-rapida`, que ya incluye tablas con bordes, rótulos y firmas en dos columnas; la paleta, el logo y los cuadros de color de arriba se aplican solo si el abogado los pide o el perfil del despacho los define
- Logo desde `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/brand/logo-despacho.jpg` si se aporta
- Si no existe, cabecera de texto plano y aviso en el resumen de la entrega

## Salida

- `matters/<slug-asunto>/hoja-encargo/hoja-encargo-v1.docx` cuando el workspace de asunto esté habilitado
- En su defecto, `outputs/hoja-encargo-[slug-asunto]-[YYYY-MM-DD].docx`

> ⚠️ **Slug: `descriptor-delito-año`. Nunca el nombre del cliente** en la ruta ni en el nombre del archivo. Un directorio que revele quién está investigado es una brecha de datos de categoría especial (art. 10 RGPD).

- La cabecera interna RESERVADO Y CONFIDENCIAL **no** se aplica: la hoja de encargo es un documento que sale al cliente
- El checklist pre-firma y los datos pendientes van en el resumen de la entrega, no en un mensaje aparte

## Reglas

1. **Sin hoja de encargo firmada no se inicia trabajo facturable** — salvo **asistencia urgente al detenido o comparecencia inaplazable**, que se atienden primero y se documentan por email en el acto, avanzando la firma en paralelo. **El plazo del art. 520.5 LECrim (3 horas) no se negocia esperando una firma.**
2. **Cero datos reales inventados.** Todo va como `[CLIENTE]`, `[DNI]`, `[DOMICILIO]`, `[IBAN]`, `[LETRADO]` hasta que el usuario los aporte. Nunca inventar un IBAN, un DNI, un domicilio ni un número de procedimiento.
3. **Conflicto de interés antes que nada.** Si hay coinvestigados o persona jurídica + persona física, parar y advertir (art. 467.1 CP).
4. **Prohibido garantizar resultados.** Ni absolución, ni sobreseimiento, ni suspensión de la pena, ni una conformidad concreta.
5. **La conformidad la decide el cliente**, y se le informa **por escrito** (art. 785.7 in fine LECrim).
6. **Costas: régimen penal, nunca el civil.** Verificar con `buscar_articulo` antes de afirmar cualquier extremo. El absuelto **nunca** paga costas (art. 240.2º LECrim).
7. **Cuota litis pura prohibida.**
8. **Aplicar estilo de la casa.** Los redactores aplican el estilo del abogado y el lenguaje de `estilo-escritos-judiciales` al escribir (no para la estructura); no hay una pasada final aparte.
9. ⛔ **No mencionar MASC, burofax previo, ni la Ley 1/2025 como requisito de procedibilidad.** No existen en penal.
10. ⛔ **No existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. No mencionar la reforma en tramitación (prevista 1-1-2028) como Derecho vigente.
11. ⛔ **Prohibido citar jurisprudencia concreta** (ECLI/ROJ/fecha) en el documento.

## Handoffs

- Si el cliente ha sido citado o detenido y aún no se ha triado la resolución: `/requerimiento-judicial-triage`
- Antes de aconsejar al cliente sobre qué guardar: `/conservacion-documental` — **incluye la advertencia de que el abogado no puede aconsejar destruir nada** (arts. 451, 464, 465 CP)
- Si el cliente impaga: la hoja firmada es la base de la reclamación de honorarios (**LEC 35, supletorio**)
- Si el encargo alcanza una fase nueva no cubierta (recurso, ejecutoria): **confirmar por escrito la extensión y minutar aparte antes de actuar**
