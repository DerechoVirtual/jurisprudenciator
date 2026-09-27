---
name: asunto-intake
description: Intake de un nuevo asunto penal. Recoge posicion procesal, fase, procedimiento, organo, delitos y fecha de los hechos, plazo de instruccion del art. 324 LECrim, prescripcion del art. 131 CP, situacion personal y medidas cautelares, detenido, conformidad y responsabilidad civil. Usar con nuevo asunto o intake este asunto.
---

# Intake de asunto — Litigación penal España

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Tipo penal y pena a la fecha de los hechos** → `buscar_articulo` (`ley="CP"`, `articulo` del delito): la respuesta indica desde cuándo rige la redacción y qué norma la dio; con esa pena se calcula la prescripción (arts. 131 y 132 CP).
- **Plazo de instrucción** → `buscar_articulo` (`ley="LECrim"`, `articulo="324"`) al fijar incoación, vencimiento y prórrogas.
- **Persona jurídica implicada** (cliente, perjudicada, responsable civil o coinvestigada) → `buscar_empresa_mercantil` por denominación o CIF: estado, administradores y apoderados; sirve también para el control de conflictos del bloque 2.
- **Norma especial fuera de las grandes siglas** (Estatuto de la víctima, LO 1/2004, LORPM) → `buscar_boe` para localizarla y `buscar_articulo` con su ID BOE (el Estatuto de la víctima es `BOE-A-2015-4606`).
- **Resoluciones citadas en la denuncia, la querella o el atestado recibidos** → `buscar_por_cita` con su ECLI o ROJ.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- "Nuevo asunto", "intake", "abrir asunto", "vamos a empezar con este caso"
- Tras `/requerimiento-judicial-triage` cuando el triage escala a asunto
- Cuando llega una citación como investigado, un traslado para escrito de defensa, una denuncia o
  atestado contra el cliente, o un encargo de acusación particular
- Tras una asistencia al detenido que continúa como encargo

## Prerrequisito

`~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md` debe estar configurado.
Si no, parar y derivar a `/cold-start-interview`.

> **Anclas normativas.** Todo plazo, pena o artículo que cite esta skill sale de
> `references/anclas-normativas-penal.md` o se verifica en el momento con `buscar_articulo`
> (conector `jurisprudenciator`). Lo que no se pueda verificar se marca `[verificar]`.

---

## Flujo

### Bloque 1: Identificación y slug

> ⚠️ **Regla de oro del penal.** El **slug NUNCA lleva el nombre del cliente**. La condición de
> investigado es un dato de **infracciones y condenas penales — art. 10 RGPD**, altamente lesivo.
> Un listado de carpetas que revele quién está investigado es una brecha grave. Ver
> `PROTECCION-DATOS.md`.

Vía `AskUserQuestion`:
- **Slug**: patrón `descriptor-delito-año` (p. ej. `estafa-inversion-2026`, `lesiones-riña-2026`,
  `seguridad-vial-tasa-2026`). Sin nombres, sin iniciales, sin nº de DNI.
- **Nombre del asunto**: `<Delito> — <posición>` (p. ej. `Estafa — defensa`). Tampoco lleva nombres.
- **Cliente**: nombre a efectos internos. Se escribe **solo** en `matter.md`, bajo cabecera de
  secreto profesional. **Nunca** en `_log.yaml`.
- Marcadores en cualquier plantilla o borrador: `[CLIENTE]`, `[INVESTIGADO]`, `[PERJUDICADO]`,
  `[ÓRGANO]`.

> **DNI, domicilio y antecedentes reales no se escriben en los archivos del plugin.** Se toman del
> expediente documental del despacho (carpeta local, OneDrive, Google Drive o Dropbox, según lo que
> use) en el momento de redactar el escrito y solo para ese escrito.

### Bloque 2: Conflictos de interés

Comprobar contra el método configurado en CLAUDE.md:
- ¿Es el cliente actual o de los últimos 5 años?
- ¿Es el perjudicado / denunciante cliente actual o ex-cliente?
- ⚠️ **Codefensa de coinvestigados:** ¿se pide defender a más de un investigado por los mismos
  hechos? Conflicto potencial en cuanto uno pueda conformarse, delatar o alegar coacción del otro.
  Advertir por escrito antes de aceptar.
- ⚠️ **Persona jurídica + persona física:** defender a la PJ (art. 31 bis CP) y a la persona física
  investigada por los mismos hechos es **conflicto estructural**. Comprobar siempre.
- ¿Hay parte adversa coincidente en otro asunto activo?
- Conflicto duro → **parar el intake** y avisar. Blando → registrar y seguir.

### Bloque 3: Fuente y encargo

- ¿Cómo llega el cliente? (recomendación / web / **turno de oficio o guardia** / despacho /
  colaborador / continuación de asistencia al detenido)
- ¿Hoja de encargo firmada? Si no, recordar firmar antes de actos procesales (`/hoja-encargo`).
- ¿Provisión de fondos? Cuantía + cobrada o pendiente.
- ¿Designa procurador? Y si es de oficio, ¿venia del compañero anterior?

### Bloque 4: Posición procesal — `posicion`

Una de: `defensa` / `acusacion-particular` / `acusacion-popular` / `actor-civil` /
`responsable-civil-subsidiario`.

- Si `acusacion-popular`: ojo a la **fianza del art. 280 LECrim** (excepciones del art. 281)
  — *verificar antes de afirmar el régimen*.
- Si `acusacion-particular` o `actor-civil`: comprobar plazo para personarse antes del trámite de
  calificación.
- Si `responsable-civil-subsidiario`: identificar el título de imputación civil y la aseguradora.

### Bloque 5: Fase, procedimiento y órgano

- **`fase`**: `diligencias-previas` / `instruccion` / `intermedia` / `juicio-oral` / `recurso` /
  `ejecucion`.
- **`procedimiento`**: `abreviado` / `sumario` / `juicio-rapido` / `delito-leve` / `jurado` /
  `menores`.
- **`organo`**: `Sección de Instrucción nº [X] del Tribunal de Instancia de [PARTIDO JUDICIAL]` /
  `Sección de Violencia sobre la Mujer nº [X]` / `Sección de Violencia contra la Infancia y la
  Adolescencia nº [X]` / `Sección de lo Penal nº [X]` / `AP de [PROVINCIA], Sección [X]` /
  `TSJ de [CCAA]` / `AN` / `TS` / `Juzgado Central de Instrucción nº [X]` /
  `Sección de Vigilancia Penitenciaria nº [X]` / `Sección de Menores nº [X]`.
  Capturar también el **nº de procedimiento** (DP / PA / Sumario / Ejecutoria).

  > ⭐ **Regla práctica: transcribe la denominación EXACTA que figure en la resolución o en la
  > carátula del procedimiento**, sin «corregirla». Es el dato que después se copia en cada
  > encabezamiento. La LO 1/2025 sustituyó los Juzgados por **Secciones de los Tribunales de
  > Instancia** (art. 14 LECrim, desde el 3-10-2025) y el calendario de implantación concluyó el
  > **31-12-2025**; aun así, muchas carátulas, sellos y asientos de LexNET conservan el rótulo
  > antiguo. **Manda lo que diga el órgano**, no lo que debería decir.

  > **Art. 14.7:** si concurren violencia contra la infancia **y** violencia sobre la mujer, la
  > competencia es **en todo caso** de la **Sección de Violencia sobre la Mujer**.

> ⛔ **Instruye el Juez de Instrucción.** No existe el «fiscal instructor». La reforma que
> atribuiría la instrucción al Ministerio Fiscal está **en tramitación**, prevista para **1-1-2028**.
> No describirla nunca como Derecho vigente.

### Bloque 6: Hechos, delitos y ley aplicable en el tiempo

- **`fecha_hechos`** — ⚠️ **campo crítico**. Determina la **redacción del CP aplicable (art. 2 CP)**.
  En delito continuado, permanente o de habitualidad, el cómputo del art. 132.1 CP arranca,
  respectivamente, de la **última infracción**, de la **eliminación de la situación ilícita** o del
  **cese de la conducta**: preguntarlo expresamente, no asumir una fecha única.
- **`delitos_imputados`**: lista de `tipo` + `artículo CP` (+ subtipo agravado si se invoca). Tomar
  la calificación **de la acusación / del auto**, no la propia; la calificación propia va en la tesis.
- **`ley_aplicable_hechos`**: comparar la redacción vigente a la fecha de los hechos con la actual y
  **pedir la más favorable (art. 2.2 CP)**. Con **LO 1/2025** (3-4-2025) y **LO 1/2026**
  (10-4-2026) esto ya no es teórico: hechos anteriores al **10-4-2026** en hurto, estafa,
  multirreincidencia o suspensión exigen **comparación de penas** explícita. Ver
  `references/anclas-normativas-penal.md` § 7.
- Resumen de hechos en 3-5 frases, en versión del atestado/denuncia y, aparte, versión del cliente.
- Estado de la prueba de cargo conocida (atestado, pericial, testifical, digital).

### Bloque 7: ⚠️ Plazo de instrucción — art. 324 LECrim

**El control más rentable de la defensa.** Capturar siempre, aunque el asunto entre en fase avanzada:

- **`fecha_incoacion`** — fecha del auto de incoación de la causa.
- **`fecha_vencimiento_instruccion`** — incoación **+ 12 meses**, de fecha a fecha.
- **`prorrogas`** — lista; cada una con `fecha_auto`, `periodo_meses` (**≤ 6**) y `nuevo_vencimiento`.
  Las prórrogas son sucesivas, de oficio o a instancia de parte, **oídas las partes**, y exigen
  **auto motivado** con las causas, las **concretas diligencias** que faltan y su relevancia.
- **Comprobación del art. 324.3:** ¿el auto de prórroga se dictó **ANTES** del vencimiento?
  - Si **no** se dictó antes, o fue **revocado en recurso** → **las diligencias acordadas a partir de
    esa fecha NO son válidas**. Anotarlo en `matter.md` como línea de ataque y en `history.md`.
- Recordar el **art. 324.2**: las diligencias **acordadas antes** del vencimiento son válidas aunque
  se **reciban** después. No confundir fecha de acuerdo con fecha de recepción.
- Si la instrucción ya venció: identificar qué diligencias se acordaron después y si sostienen la
  acusación.

> Si el asunto entra en el despacho con la instrucción avanzada, **reconstruir el historial de
> prórrogas del expediente antes de nada**. Es el primer trabajo útil del intake.

### Bloque 8: Prescripción del delito — arts. 131 y 132 CP

- **`prescripcion_delito.plazo`** según el art. 131 CP, por la **pena máxima** señalada al delito:
  **20 / 15 / 10 / 5 años**, y **1 año** para **delitos leves** y para **injurias y calumnias**.
  Pena compuesta → la que exija **mayor** tiempo (131.2). Concurso o conexos → plazo del **delito más
  grave** (131.4). Imprescriptibles: los supuestos del art. 131.3.
- **`prescripcion_delito.fecha_estimada`**: desde `fecha_hechos` conforme al art. 132.1 (con las
  reglas especiales de víctimas menores de edad, si aplican).
- **Interrupción (art. 132.2):** solo interrumpe la **resolución judicial motivada** que atribuya al
  investigado su presunta participación. La **querella o denuncia** ante órgano judicial **suspende**
  el cómputo **6 meses**; si en ese plazo recae la resolución, la interrupción se retrotrae a la
  fecha de presentación; si no, el cómputo **continúa** desde esa fecha.
- Anotar también si hay riesgo de **paralización** del procedimiento (reinicia el cómputo).

### Bloque 9: Situación personal y medidas cautelares

- **`situacion_personal`**: `libertad` / `libertad-provisional` / `prision-provisional` /
  `con-medidas-544-bis`.
- **`medidas_cautelares`**: `ninguna` / `544-bis` / `544-ter` (orden de protección) / `prision` /
  `fianza-embargo`.
- Si **`prision-provisional`**: capturar **fecha de ingreso** y **límite máximo** del art. 504
  LECrim, y anotarlos como plazo vigilado:
  - Fines del art. 503.1.3.º a) o c) o del 503.2 → **1 año** si la pena señalada es **≤ 3 años**;
    **2 años** si es **> 3 años**. Prórroga **única** por auto: hasta **2 años** más (pena > 3 años) o
    hasta **6 meses** más (pena ≤ 3 años).
  - Condenado y sentencia recurrida → prórroga hasta **la mitad de la pena impuesta**.
  - Fin del art. 503.1.3.º b) (ocultación/alteración de prueba) → **máximo 6 meses**.
  - Cómputo: se **suma** el tiempo de detención y prisión provisional por la misma causa; se
    **excluyen** las dilaciones no imputables a la Administración de Justicia (504.5).
  - Superadas las **2/3 partes** del máximo → comunicación al presidente de la sala de gobierno y al
    fiscal jefe, y **tramitación preferente** (504.6). Argumento útil.
- Si **`544-bis`**: son medidas de los delitos del **art. 57 CP**, motivadas y estrictamente
  necesarias (prohibición de residir, de acudir, de aproximarse o comunicarse), ponderando situación
  económica, salud, situación familiar y **continuidad de la actividad laboral** del inculpado. El
  **incumplimiento** abre la comparecencia del **art. 505** (prisión, 544 ter u otra más limitativa).
- Si **`544-ter`** (orden de protección): capturar contenido penal y civil y su plazo de vigencia.

### Bloque 10: Detenido

- **`detenido.hubo`**: sí / no. Si sí, **`detenido.fecha`** y **hora**.
- Plazo máximo: **72 horas** para poner en libertad o a disposición judicial (art. 520.1). El
  **atestado** debe reflejar lugar y hora de detención y de puesta a disposición o en libertad:
  **comprobarlo**, es el primer punto de impugnación de la legalidad de la detención.
- Comprobar en el atestado: información de derechos **por escrito** y de forma inmediata (520.2);
  entrevista **reservada previa** a la declaración (520.6.d); reconocimiento por médico forense;
  intérprete. Si falló algo → anotarlo como línea de nulidad.
- Recordar el plazo del **art. 520.5**: el abogado designado acude en un **máximo de 3 horas**.
- Si la detención sigue viva y es ilegal → valorar **habeas corpus** (LO 6/1984) `[verificar cauce]`.

### Bloque 11: Conformidad

- **`conformidad`**: `no-planteada` / `negociando` / `prestada`.
- Sede vigente de la conformidad en el **abreviado**: **audiencia preliminar del art. 785**
  (apdos. 4 a 11), tras la **LO 1/2025**. El art. 787 ya **no** es la conformidad: hoy regula la
  celebración del juicio oral. Ver anclas § 2.
  > ⚠️ Defecto de coordinación: el art. 784.3 y el art. 801.1-2 siguen remitiendo al art. 787.
  > Citar el 785 como sede sustantiva y ser consciente del desajuste.
- **Juicio rápido**: conformidad ante el juzgado de guardia, **art. 801** — pena **≤ 3 años** de
  prisión, multa de cualquier cuantía, u otra pena **≤ 10 años**; y que la pena privativa de
  libertad, **reducida en un tercio, no supere 2 años**. No debe haber acusación particular personada.
- Si se negocia: recordar el deber del **art. 785.7 in fine** — «el letrado o la letrada facilitará
  **por escrito** a la persona a quien defiende la información sobre el acuerdo alcanzado».
  Documentarlo siempre.
- Si el asunto es de los perseguibles previa denuncia o querella y se prevé suspensión: **audiencia
  al ofendido** (art. 80.6 CP).

### Bloque 12: Responsabilidad civil

- **`responsabilidad_civil.cuantia_reclamada`** (€) y **`responsabilidad_civil.aseguradora`**
  (nombre o `no`).
- La acción civil derivada del delito se ejercita en el proceso penal (arts. 100, 108-117 LECrim;
  109-126 CP). ¿Se **reserva** la acción civil? Registrarlo.
- ⚠️ Impacto en defensa: la **reparación del daño** condiciona la **suspensión** (art. 80.2.3.ª CP
  — basta el **compromiso** conforme a la capacidad económica) y pesa como **esfuerzo reparador**
  (art. 80.1 y 80.3). Plantearlo desde el intake, no en ejecución.

### Bloque 13: Triage de riesgo

Aplicar la matriz severidad × probabilidad del CLAUDE.md. En penal la **severidad** se mide por:
- **Pena solicitada / señalada** y si supera los 2 años (frontera de la suspensión, art. 80 CP).
- **Situación personal** (prisión provisional pesa siempre alto).
- **Antecedentes** y riesgo de **reincidencia / multirreincidencia** (art. 22.8.ª CP y tipos
  agravados de la LO 1/2026).
- Consecuencias colaterales: **art. 89 CP** (extranjería), inhabilitación profesional, privación del
  permiso de conducir, responsabilidad civil desproporcionada.

Etiqueta resultante → mapping a `_log.yaml`: `critico` / `alto` / `medio` / `bajo`.

### Bloque 14: Colaboradores y representación

- Procurador (default del CLAUDE.md o preguntar). En penal la postulación con procurador es la regla
  en abreviado y sumario; en **juicio por delito leve** no es preceptiva `[verificar el supuesto]`.
- Perito necesario: médico forense de parte, calígrafo, informático forense, tasador, criminólogo.
- ¿Abogado colaborador por especialidad cruzada (extranjería, penitenciario, compliance)?
- Si hay **persona jurídica**: representante especialmente designado, con **poder especial** para
  prestar conformidad (art. 785.11).

### Bloque 15: Conservación documental

- ¿Riesgo de pérdida de prueba de descargo? (mensajería, geolocalización, cámaras con borrado
  automático, correos, registros bancarios, tacógrafo).
- ⚠️ En penal la prueba **exculpatoria** de terceros caduca rápido: las grabaciones de
  videovigilancia se sobrescriben en días. Si hay algo así, **no esperar**: preparar solicitud de
  diligencia urgente al instructor (`/solicitud-diligencias-instruccion-catalogo`).
- Marcar `conservacion_documental: pending` para que `/conservacion-documental --emitir` genere la
  comunicación al cliente.
- ⛔ Nunca sugerir al cliente conductas de ocultación o alteración de prueba: además de ser ilícito,
  activa el art. 503.1.3.º b) (prisión provisional).

### Bloque 16: Fechas críticas y próximo plazo

Capturar y calcular, con fecha absoluta:
- `fecha_vencimiento_instruccion` y la de cada prórroga (Bloque 7).
- `prescripcion_delito.fecha_estimada` (Bloque 8).
- Límite de la prisión provisional, si la hay (Bloque 9).
- Plazo de recurso abierto, si acaba de haber notificación.
- **Escrito de defensa**: **10 días** comunes desde el traslado (art. 784.1).
- **Víctima**: recurso contra el auto de sobreseimiento en **20 días**, aunque no se haya mostrado
  parte (art. 779.1.1.ª).
- Señalamiento de juicio o de comparecencia, si lo hay.
- **`next_deadline`** = la más próxima, con su **`next_deadline_concepto`**.

> **Cómputo en penal — no es el del civil.**
> - **Todos los días y horas del año son hábiles para la INSTRUCCIÓN**, sin habilitación especial
>   (art. 201 LECrim).
> - Son **inhábiles agosto** y **del 24 de diciembre al 6 de enero**, ambos inclusive, salvo las
>   actuaciones **declaradas urgentes** por las leyes procesales (art. 183 LOPJ).
> - Los términos judiciales son **improrrogables** salvo disposición expresa (art. 202 LECrim).
> - El plazo del art. 324 es de **meses**: de fecha a fecha desde la incoación.

### Bloque 17: Tesis inicial

- Tesis en 2-3 frases (la historia que vamos a sostener).
- **Línea de defensa dominante**: atipicidad / autoría no acreditada / prueba ilícita (art. 11.1
  LOPJ) / presunción de inocencia / eximente o atenuante / prescripción / nulidad por art. 324.3 /
  error de tipo o prohibición / conformidad negociada. En acusación: elementos del tipo que hay que
  acreditar y cómo.
- Puntos débiles ya identificados.
- Cuestión jurídica central (p. ej. «suficiencia del engaño bastante del art. 248.1 CP»,
  «validez del cotejo de ADN sin consentimiento», «cadena de custodia»).
- Diligencias de descargo a pedir **ya** (mientras la instrucción esté viva y en plazo).

---

## Salida

1. Crear carpeta
   `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/matters/<slug>/`
2. Escribir `matter.md` con:
   - Cabecera `RESERVADO Y CONFIDENCIAL — SECRETO PROFESIONAL DEL ABOGADO`
   - Aviso: `Datos de infracciones y condenas penales — art. 10 RGPD. No difundir.`
   - Identificación mínima (cliente y posición; **sin DNI ni domicilio**)
   - Delitos imputados + **fecha de los hechos** + redacción del CP aplicable (art. 2 CP)
   - Fase, procedimiento, órgano y nº de procedimiento
   - **Control del art. 324**: incoación, vencimiento, prórrogas con fecha de auto, veredicto 324.3
   - Prescripción del delito (art. 131) con fecha estimada
   - Situación personal y medidas cautelares
   - Hechos (versión atestado / versión cliente)
   - Tesis y línea de defensa
   - Triage de riesgo
   - Responsabilidad civil y conformidad
   - Fechas críticas
   - Colaboradores
   - Próximos pasos
3. Crear `history.md` con primera entrada `[AAAA-MM-DD] INTAKE — asunto creado.`
4. Crear subcarpetas `escritos/`, `jurisprudencia/`
5. Añadir fila a `matters/_log.yaml`:

```yaml
- slug: estafa-inversion-2026
  name: Estafa — defensa
  status: open
  posicion: defensa
  fase: instruccion
  procedimiento: abreviado
  organo: Sección de Instrucción nº [X] del Tribunal de Instancia de [PARTIDO JUDICIAL]
  num_procedimiento: DP [XXXX]/2026
  delitos_imputados:
    - tipo: estafa
      articulo: 248 CP
      agravante_invocada: 250.1.5º CP (valor > 50.000 €)
  fecha_hechos: 2025-11-04
  ley_aplicable_hechos: redacción anterior a LO 1/2026 — comparar con la vigente (art. 2.2 CP)
  fecha_incoacion: 2026-02-10
  fecha_vencimiento_instruccion: 2027-02-10   # incoación + 12 meses (art. 324.1 LECrim)
  prorrogas: []                               # cada una: {fecha_auto, periodo_meses, nuevo_vencimiento}
  art_324_3_alerta: no                        # sí = hubo diligencias tras vencer sin auto previo
  prescripcion_delito:
    plazo: 5 años (art. 131 CP)
    fecha_estimada: 2030-11-04
  situacion_personal: libertad-provisional
  medidas_cautelares: fianza-embargo
  detenido:
    hubo: no
    fecha: null
  conformidad: no-planteada
  responsabilidad_civil:
    cuantia_reclamada: 42000
    aseguradora: no
  risk: alto
  materiality: alta
  procurador: [PROCURADOR]
  conservacion_documental: pending
  next_deadline: 2026-08-28
  next_deadline_concepto: comparecencia de prórroga de instrucción (art. 324.1)
  related_matters: []
  opened: 2026-07-17
  last_updated: 2026-07-17
  notas: "Instrucción viva. Pericial informática de descargo pendiente de solicitar."
```

> ⚠️ **`_log.yaml` no lleva nombres.** Ni cliente, ni investigado, ni perjudicado, ni testigos, ni
> DNI, ni domicilios, ni antecedentes. El log debe poder abrirse sin que nadie reconstruya **quién**
> está investigado. Las identidades viven solo en `matter.md`.

6. Si los workspaces de asunto están habilitados (default sí), preguntar: "¿Hacer este asunto el
   activo?" Si sí, escribir en CLAUDE.md → `## Workspaces de asuntos` → `Asunto activo: <slug>`.

---

## Reglas

1. **NUNCA crear asunto sin chequeo de conflictos.** Conflicto duro → parar. La codefensa de
   coinvestigados y la defensa simultánea de PJ y persona física exigen advertencia expresa.
2. **⚠️ El art. 324 se captura SIEMPRE.** Sin `fecha_incoacion` no hay intake completo: es el plazo
   que manda y el que nadie vigila. Si no consta en el expediente, marcarlo como primera diligencia
   a averiguar y dejar `art_324_3_alerta: [verificar]`.
3. **`fecha_hechos` es obligatoria.** Determina la redacción del CP aplicable (art. 2 CP) y el
   arranque de la prescripción (art. 132.1). Sin ella no se califica nada.
4. **Calcular la prescripción del delito al intake** (art. 131 CP), no después.
5. **El slug nunca lleva el nombre del cliente.** Art. 10 RGPD. Sin excepciones.
6. **Fechas en formato AAAA-MM-DD.** Convertir relativas ("la semana que viene") a absolutas. Si hay
   detención, capturar también la **hora**.
7. **Prohibido inventar penas, plazos o artículos.** Lo que no esté en
   `references/anclas-normativas-penal.md` se verifica con `buscar_articulo` o se marca `[verificar]`.
8. **No hay MASC en penal.** Es requisito de procedibilidad del orden **civil**. Aquí el proceso se
   inicia por **denuncia**, **querella** o **de oficio** (atestado). Lo más próximo, y solo en
   supuestos tasados, son la querella o denuncia del ofendido en delitos privados y semipúblicos, y
   el **acto de conciliación del art. 804 LECrim** en injurias y calumnias.
