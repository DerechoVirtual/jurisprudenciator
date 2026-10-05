---
name: recurso-reforma-apelacion-auto-apertura-jo
description: >-
  Analiza la recurribilidad del auto de apertura de juicio oral (art. 783.3 LECrim — IRRECURRIBLE salvo en lo relativo a la situación personal del acusado) y redacta el recurso procedente o redirige a la vía útil. Cubre la excusa absolutoria del art. 268 CP entre parientes. Actívala ante "recurrir la situación personal acordada en el auto de apertura", "¿es recurrible el auto de apertura de juicio oral?", "solicitar sobreseimiento pese a la apertura", "excusa absolutoria entre parientes", "art. 268 CP", "acusación infundada". Aviso: en la inmensa mayoría de los casos el auto NO es recurrible, de modo que si lo que se quiere es combatir la acusación de fondo, el cauce correcto es el escrito de defensa → /escrito-defensa-calificacion.
---

# Auto de apertura de juicio oral — recurribilidad y vía útil

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Recurribilidad y vía útil** (arts. 783, 784 y 785 LECrim) → `buscar_articulo` (`ley="LECrim"`).
- **Apropiación indebida y excusa absolutoria entre parientes** → `buscar_articulo` (`ley="CP"`, arts. 253 y 268).
- **Doctrina sobre la excusa del art. 268 y la irrecurribilidad del auto de apertura** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`; `base="AN"` con `tipo_organo="AP"` para la Audiencia) + `leer_sentencias` con `parrafos=3`.
- **Situación personal acordada en el auto (único extremo recurrible)** → `buscar_sentencias` (`base="TC"`, motivación de las medidas cautelares).
- **Comprobar las citas de normas** → `verificar_escrito`: cada redactor lo pasa solo con las frases de su sección que citan artículos o leyes; el ensamblado comprueba que cada ECLI o ROJ procede de una fuente leída.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

**⚠️ Antes de redactar nada: comprueba si el auto es recurrible. Casi siempre NO lo es.** Esta es la
pregunta que más se falla en la práctica del abreviado, y la que más recursos inadmitidos genera.

---

## 🚨 REGLA CAPITAL — art. 783.3 LECrim, verificado literalmente

> «**Contra el auto que acuerde la apertura del juicio oral no se dará recurso alguno, excepto en lo
> relativo a la situación personal, pudiendo el acusado reproducir ante el órgano de enjuiciamiento las
> peticiones no atendidas.**»

Redacción vigente desde el **4-5-2010** (Ley 13/2009). **No modificada por la LO 1/2025.**

**Descomposición de la regla:**

| Contenido del auto | ¿Recurrible? |
|---|---|
| **La apertura del juicio oral en sí** | **NO.** «No se dará recurso alguno» |
| Existencia de indicios / calificación / atipicidad | **NO.** Va dentro de la apertura |
| **La situación personal** (prisión provisional, libertad con fianza, medidas cautelares personales) | **SÍ.** Es la **única** excepción legal |
| **Pronunciamientos sobre responsabilidad civil y fianza** (art. 783.2) | **[verificar]** — no están literalmente en la excepción de la «situación personal». Comprueba el criterio de la Sección con `buscar_sentencias` antes de recurrir |

- **Vía de reacción que la ley SÍ da:** «pudiendo el acusado **reproducir ante el órgano de
  enjuiciamiento las peticiones no atendidas**». Es una **remisión**, no una denegación de tutela: el
  debate no se cierra, **se aplaza**.
- **Asimetría que debes conocer:** el 783.3 blinda el auto que **acuerda** la apertura. El auto que
  acuerda el **sobreseimiento** sí es recurrible por la acusación (ver skill
  `recurso-reforma-apelacion-auto-archivo`). **La irrecurribilidad juega solo contra la defensa.**

### ⛔ Consecuencia práctica: no redactes un recurso condenado a la inadmisión

Si el cliente pide «recurrir la apertura» por **falta de indicios o atipicidad**, **explícale que la ley
lo impide** y redirígelo. Presentar ese recurso no es celo defensivo: es **consumir el plazo, revelar la
estrategia a la acusación y obtener una inadmisión** que refuerza la posición contraria.

**Redacta el recurso SOLO si:**

1. El auto contiene un pronunciamiento sobre **situación personal** que se combate — **y limita el
   recurso a ese extremo**; o
2. Concurre un **defecto formal grave** ajeno al juicio de apertura [verificar caso a caso, y ser
   honesto sobre el riesgo de inadmisión].

**Si recurres la situación personal** (art. 766, verificado): **reforma en 3 días** (art. 211);
**apelación en 5 días** (art. 766.3); la reforma previa **nunca es necesaria** (art. 766.2). ⭐ **Art.
766.5:** si el auto acordó **prisión provisional**, el apelante **puede solicitar la celebración de
vista** en el escrito de interposición, **que la Audiencia acordará** — señalada en los **10 días**
siguientes a la recepción de la causa. **Pídela siempre**: es oralidad e inmediatez ante la Audiencia.

---

## ✅ LA VÍA ÚTIL — dónde se combate de verdad la acusación infundada

### 1. Antes de la apertura: oponerse al escrito de acusación

El momento natural. **Art. 783.1** (verificado): solicitada la apertura por el Fiscal o la acusación
particular, el juez **la acordará, salvo** que estime que concurre el supuesto del **art. 637.2.º** (el
hecho **no es constitutivo de delito**) o que **no existen indicios racionales de criminalidad** contra
el acusado, en cuyo caso acordará el **sobreseimiento** conforme a los arts. 637 y 641.

> **Ahí está el debate real.** El estándar del 783.1 es doble y estrecho: atipicidad o ausencia de
> indicios racionales. **Si tienes argumentos, hazlos valer ANTES** — en el trámite del art. 780 o
> mediante escrito de oposición a la apertura. Una vez dictado el auto, el 783.3 cierra la puerta.

**Art. 782** (verificado): si el Fiscal y el acusador particular piden el sobreseimiento, **el juez lo
acuerda** (salvo eximentes del art. 20.1.º, 2.º, 3.º, 5.º y 6.º CP, en que devuelve para calificación a
efectos de medidas de seguridad y acción civil).

### 2. Después de la apertura: la AUDIENCIA PRELIMINAR del art. 785 — sede nueva

**⚠️ Cambio estructural de la LO 1/2025 (vigente 3-4-2025).** Los arts. 785-787 fueron reordenados:
el **785** es hoy la **audiencia preliminar** (y la conformidad, 785.4-11); el **786**, el
**señalamiento**; el **787**, la **celebración del juicio oral**.

**Art. 785.1 — objeto de la audiencia preliminar** (verificado): conformidad; **competencia**;
**vulneración de algún derecho fundamental**; **artículos de previo pronunciamiento**; causas de
suspensión; **nulidad de actuaciones**; y **contenido, finalidad o nulidad de las pruebas** propuestas.
Además, incorporación de informes, certificaciones y documentos, y prueba desconocida al calificar.

- **785.2:** requiere asistencia del **acusado y del abogado defensor**; no se suspende por inasistencia
  injustificada del acusado citado en forma.
- **785.3:** resolución **oral** (o auto en **10 días** si hay complejidad). **No cabe recurso alguno**,
  sin perjuicio de la **protesta** y de reproducir la cuestión en el recurso contra la sentencia —
  **salvo** que la resolución **ponga fin al procedimiento**, en cuyo caso cabe **apelación** (arts. 790
  y ss.).
  > ⭐ **La puerta que sí existe:** si en la audiencia preliminar consigues una resolución que **pone fin
  > al procedimiento**, **esa sí es apelable**. Es el objetivo a perseguir, y es exactamente lo que el
  > recurso contra el auto de apertura **nunca** te habría dado.
- **⚠️ Las cuestiones previas YA NO se plantean al inicio del juicio oral.** **Art. 787.3** (verificado):
  al inicio de las sesiones **únicamente** puede solicitarse la incorporación de **informes,
  certificaciones y documentos**, y la prueba **de la que no se tuvo conocimiento al celebrar la
  comparecencia del art. 785**. **Quien reserve las cuestiones previas para el juicio llega tarde.**
- **La «reproducción ante el órgano de enjuiciamiento» del art. 783.3 se materializa hoy en la audiencia
  preliminar del art. 785**, no en el turno de intervenciones del antiguo 786.2 (derogado). **Cítalo
  así.**

### 3. En el escrito de defensa

Anuncia por otrosí las cuestiones que sostendrás en la audiencia preliminar. Ver la skill
`escrito-defensa-calificacion` (plazo de **10 días** comunes, art. 784.1, **preclusivo para la prueba**).

---

## Comprobaciones previas

Se responden con la documentación aportada (paso 2 de `redaccion-rapida`); pregunta solo lo que
bloquee y en una única ronda.

1. **Prescripción (art. 131 CP)** a la fecha de los hechos. Si prescribió, es **artículo de previo
   pronunciamiento**: sede en la **audiencia preliminar (785.1)**, y una resolución estimatoria **pone
   fin al procedimiento** → **apelable (785.3)**.
2. **Plazo de instrucción (art. 324 LECrim).** 12 meses + prórrogas de ≤6 meses por auto motivado
   **previo**. **324.3:** sin ese auto, o revocado en recurso, **no son válidas las diligencias
   acordadas a partir de esa fecha**. Si la acusación se sostiene sobre diligencias inválidas, la vía
   es la **nulidad en la audiencia preliminar (785.1)** — no el recurso contra la apertura.
3. **Ley penal más favorable (art. 2.2 CP).** LO 1/2025 y LO 1/2026 (que **reescribió el art. 248 CP** —
   relevante porque el **art. 253.1 remite a «las penas del artículo 248»**, ver abajo).
4. **Prueba ilícita:** art. 11.1 LOPJ; art. 238 LOPJ; arts. 18 y 24 CE. Sede: **785.1** («nulidad de
   actuaciones» y «nulidad de las pruebas propuestas»).

---

## Fondo — apropiación indebida y excusa absolutoria entre parientes

### Art. 253 CP — apropiación indebida (redacción LO 14/2022, vigente 12-1-2023, verificado)

- **253.1:** «Serán castigados con las **penas del artículo 248** o, en su caso, del **artículo 250**,
  salvo que ya estuvieran castigados con una pena más grave en otro precepto de este Código, los que,
  **en perjuicio de otro, se apropiaren para sí o para un tercero, de dinero, efectos, valores o
  cualquier otra cosa mueble, que hubieran recibido en depósito, comisión, o custodia, o que les
  hubieran sido confiados en virtud de cualquier otro título que produzca la obligación de entregarlos
  o devolverlos, o negaren haberlos recibido**.»
- **253.2:** cuantía **≤ 400 €** → **multa de 1 a 3 meses**.
- **⭐ Atención al encadenamiento de reformas.** La LO 14/2022 cambió la remisión del art. **249** al
  art. **248**; y la **LO 1/2026** (vigente 10-4-2026) **reescribió el art. 248**, que hoy contiene la
  definición de estafa (párr. 1), la **pena de prisión de 6 meses a 3 años** (párr. 2) y el subtipo de
  **≤400 €** con **multirreincidencia** (párr. 3). **La pena de la apropiación indebida se determina hoy
  a través del art. 248 vigente.** Verifica con `buscar_articulo` la redacción **a la fecha de los
  hechos** y compara (art. 2.2 CP): puede haber ley más favorable.
- **Deslinde con la administración desleal (art. 252 CP):** apropiación = **hacer propio** lo recibido
  con obligación de devolver; administración desleal = **exceso en las facultades de administrar**
  patrimonio ajeno causando perjuicio. Si dudas del encaje, **dilo y verifica** — no lo des por supuesto.

### Art. 268 CP — excusa absolutoria entre parientes (redacción LO 1/2015, verificado)

- **268.1:** «Están **exentos de responsabilidad criminal y sujetos únicamente a la civil** los
  **cónyuges que no estuvieren separados legalmente o de hecho o en proceso judicial de separación,
  divorcio o nulidad** de su matrimonio y los **ascendientes, descendientes y hermanos por naturaleza o
  por adopción**, así como los **afines en primer grado si viviesen juntos**, por los **delitos
  patrimoniales que se causaren entre sí**, siempre que **no concurra violencia o intimidación, o abuso
  de la vulnerabilidad de la víctima**, ya sea por razón de **edad**, o por tratarse de una **persona con
  discapacidad**.»
- **268.2:** «Esta disposición **no es aplicable a los extraños que participaren en el delito**.»

**Lectura precisa del ámbito subjetivo — el error más común:**

| Parientes | ¿Convivencia exigida? |
|---|---|
| Cónyuges (no separados legalmente o de hecho, ni en proceso de separación/divorcio/nulidad) | **No** |
| **Ascendientes, descendientes y hermanos** (por naturaleza o adopción) | **NO.** El texto **solo** exige convivencia a los afines |
| **Afines en primer grado** | **SÍ** — «**si viviesen juntos**» |

**Límites negativos, que la acusación intentará activar:** violencia o intimidación; **abuso de la
vulnerabilidad** de la víctima **por razón de edad** o por **discapacidad**. ⚠️ Este último inciso es
capital en el supuesto típico (hijo que dispone de las cuentas del progenitor anciano): **si el
instructor aprecia abuso de vulnerabilidad por edad, la excusa decae**. Anticípalo y desmóntalo.

> ⚠️ **Sobre el Acuerdo no jurisdiccional del Pleno de la Sala Segunda:** **no lo cites de memoria ni
> por su fecha.** El texto vigente del 268.1 **ya no exige convivencia** a ascendientes, descendientes
> y hermanos — el argumento se sostiene **en la ley**, que es más fuerte que un acuerdo. Si aun así
> quieres invocar doctrina, **verifícala primero con `buscar_sentencias` / `buscar_por_cita`**. Sin
> verificación → `[verificar]` y no se cita.

**Naturaleza y sede procesal:** es **excusa absolutoria** (exención de responsabilidad **criminal**, con
subsistencia de la **civil**), no causa de atipicidad. Encaje como **artículo de previo pronunciamiento**
y/o **art. 637.3.º** («aparezcan exentos de responsabilidad criminal»). **Su sede tras la apertura es la
audiencia preliminar (785.1)** — y una estimación **pone fin al procedimiento** → **apelable (785.3)**.
[verificar el criterio de la Sección sobre su apreciación anticipada con `buscar_sentencias`]

> **⭐ Escenario mixto, y el punto que decide la estrategia:** por el **268.2**, la excusa **no alcanza a
> los extraños partícipes**. Si defiendes a la pariente **y** a una tercera, la excusa exonera solo a la
> primera: **para la segunda hay que alegar atipicidad o ausencia de indicios, por separado**. Y
> **comprueba el conflicto de interés** antes de asumir ambas defensas: la estrategia de una puede
> perjudicar a la otra. Ver `CLAUDE.md`.

---

## Estructura del escrito

### Opción A — Escrito de OPOSICIÓN a la apertura (antes del auto). **Preferente.**

1. Encabezamiento a la **Sección de Instrucción del Tribunal de Instancia**, nº de diligencias
   previas.
   > ⭐ **Copia la denominación exacta que figure en la resolución que contestas o en la carátula del
   > procedimiento.** Es lo que nunca falla, diga «Sección de Instrucción del Tribunal de Instancia»
   > o siga diciendo «Juzgado de Instrucción». La nomenclatura vigente (art. 14 LECrim, desde el
   > 3-10-2025) es la de **Sección**; la antigua no invalida el escrito (DA 1.ª LO 1/2025).
2. Comparecencia de procurador y letrado de `[QUERELLADA]`.
3. Fórmula: al amparo del **art. 783.1 LECrim**, se opone a la apertura e interesa el **SOBRESEIMIENTO**
   (art. 637.2.º o 3.º / art. 641), por atipicidad, ausencia de indicios racionales o concurrencia de
   **excusa absolutoria (art. 268 CP)**.
4. Alegaciones, ancladas al folio. **SUPLICO** de sobreseimiento libre y archivo.

### Opción B — Alegaciones para la AUDIENCIA PRELIMINAR (tras el auto). **La vía real.**

1. Encabezamiento al **órgano de enjuiciamiento**, nº de procedimiento abreviado.
2. Fórmula: al amparo del **art. 785.1 LECrim**, y a fin de que se sustancien en la audiencia
   preliminar, plantea: (i) **artículo de previo pronunciamiento** por **excusa absolutoria del
   art. 268 CP**; (ii) **nulidad de actuaciones** (art. 324.3 LECrim / art. 11.1 LOPJ); (iii) nulidad de
   las pruebas; (iv) competencia.
3. Alegaciones. **SUPLICO** de resolución que **ponga fin al procedimiento** — **con la mención expresa
   de que, conforme al art. 785.3, sería apelable** ex arts. 790 y ss.
4. **OTROSÍ: PROTESTA anticipada** a los efectos del **art. 785.3**, para su reproducción en el recurso
   contra la sentencia.

**Reparto para la redacción rápida (opciones A y B):** 01 encabezamiento, comparecencia y fórmula con el cauce invocado · 02 alegaciones, una sección por cuestión (excusa absolutoria del 268 CP, atipicidad o falta de indicios, nulidades), cada una con sus búsquedas · 03 suplico, otrosíes (en B, la protesta del 785.3), lugar, fecha y firma. Si el escrito no pasa de tres páginas, redáctalo sin equipo.

### Opción C — Recurso contra el auto de apertura. **Solo situación personal.**

1. Fórmula: al amparo de los **arts. 211, 216 y ss. y 766 LECrim**, y **exclusivamente en lo relativo a
   la situación personal**, **único extremo recurrible conforme al art. 783.3 LECrim**, interpone
   **RECURSO DE REFORMA y, SUBSIDIARIAMENTE, DE APELACIÓN** contra el auto de fecha `[FECHA]`, notificado
   el `[FECHA]`, dentro del **plazo de 3 días** del art. 211.
2. Alegaciones **ceñidas a las medidas cautelares personales** (arts. 502 y ss., 528 y ss.).
3. **SUPLICO** y **OTROSÍ:** **solicitud de vista ex art. 766.5** si hay prisión provisional; particulares
   a testimoniar (art. 766.3).
4. **⚠️ No mezcles**: no introduzcas la atipicidad ni la falta de indicios. Contaminar el recurso con lo
   irrecurrible es invitar a la inadmisión **del conjunto**.

**Reparto para la redacción rápida (opción C):** recurso breve, ceñido a la situación personal: no necesita equipo; redáctalo tú en un único archivo de `secciones/`.

---

## Errores típicos

| Error | Corrección |
|---|---|
| Recurrir la apertura por falta de indicios o atipicidad | **Art. 783.3: «no se dará recurso alguno.»** Inadmisión segura |
| Creer que la excepción del 783.3 cubre todo el auto | Cubre **solo la situación personal** |
| Dar por recurrible la fianza / responsabilidad civil del 783.2 | **[verificar]** con `buscar_sentencias`. No está en la excepción literal |
| Plantear las cuestiones previas al inicio del juicio | Su sede es la **audiencia preliminar (785.1)**. El **787.3** ya no las admite |
| Citar el «turno de intervenciones del art. 786.2» | **Derogado.** El 786 es hoy el **señalamiento** |
| Creer que el 783.3 deja sin tutela | **Reproducción** ante el órgano de enjuiciamiento; y el 785.3 **sí** permite apelar lo que ponga fin al procedimiento |
| Exigir convivencia a hermanos para el art. 268 | El texto **solo** la exige a los **afines en primer grado** |
| Olvidar el límite de **abuso de vulnerabilidad por edad** | Desactiva la excusa. Anticípalo |
| Extender la excusa al partícipe extraño | **268.2**: no se aplica a los extraños |
| Citar el Acuerdo del Pleno de memoria | **Prohibido.** Verifica o no cites. La ley ya te da el argumento |
| Calcular la pena del 253 sin mirar el 248 | El **253.1 remite al 248**, **reescrito por la LO 1/2026**. Arts. 2 y 2.2 CP |
| Defender a pariente y a extraña sin analizar el conflicto | Estrategias incompatibles. Compruébalo **antes** de aceptar |
| No formular la protesta del 785.3 | Sin protesta **no hay motivo** en el recurso contra la sentencia |

## Reglas de trabajo

- **PRIMERO comprueba la recurribilidad** (art. 783.3). Si el auto no es recurrible, **dilo con
  claridad al cliente** y redirige a la vía útil. No redactes recursos inadmisibles.
- **Verifica con `buscar_articulo` antes de citar.** Anclas: `references/anclas-normativas-penal.md`.
- **Jurisprudencia solo vía `jurisprudenciator`** (`buscar_sentencias`, `buscar_por_cita`,
  `leer_sentencias`): art. 268 CP, apreciación anticipada de la excusa, deslinde 253/252. **Prohibido
  inventar o reproducir párrafos no verificados**; prohibido citar ECLI, ROJ, fechas o acuerdos de
  memoria. Sin verificar → `[verificar]`.
- **Prohibido inventar** penas, plazos, ordinales o artículos. Lo no verificable → `[verificar]`.
- **Ancla al folio**: «(f. …)».
- **Anonimización:** `[QUERELLADA]`, `[ACUSADO]`, `[VÍCTIMA]`, `[TESTIGO]`. Datos de infracciones y
  condenas = **categoría especial (art. 10 RGPD)**; extremar la cautela en asuntos intrafamiliares. Ver
  `PROTECCION-DATOS.md`.
- **Instruye el Juez de Instrucción.** No existe el «fiscal instructor» en Derecho vigente.
- Terminología LO 1/2025: Tribunales de Instancia, LAJ, audiencia preliminar (art. 785).

## Entrega

Word `.docx`, que genera el ensamblado de `redaccion-rapida`, maquetado para LexNET, **del escrito que
proceda** según el análisis de recurribilidad — oposición a la apertura (A), alegaciones para la audiencia
preliminar (B) o recurso limitado a la situación personal (C). Encabeza el resumen de la entrega con una
**nota de viabilidad** de dos líneas: qué es recurrible, qué no, y por qué vía se combate lo demás.
