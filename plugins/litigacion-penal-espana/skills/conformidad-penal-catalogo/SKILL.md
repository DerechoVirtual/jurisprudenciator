---
name: conformidad-penal-catalogo
description: >-
  Catálogo (sin plantilla) de las conformidades penales — audiencia preliminar del abreviado (art. 785.4-785.11 LECrim), conformidad premiada del juzgado de guardia (art. 801), conformidad en el escrito de defensa (art. 784.3) y conformidad en el sumario (art. 655). Genera además el documento del art. 785.7 in fine (información escrita al defendido sobre el acuerdo). Actívala ante "escrito de conformidad", "conformidad con la acusación", "rebaja del tercio de la pena", "conformidad premiada", "acuerdo con el fiscal", "sentencia de conformidad", "conformarse antes del juicio", "hasta cuándo puedo conformarme". Es la skill TRANSVERSAL que compara los cuatro cauces: úsala cuando aún no esté claro en qué momento procesal se va a conformar. Si la conformidad se plantea en el juzgado de guardia dentro de un juicio rápido (art. 801), usar /juicio-rapido; si el asunto ya está en abreviado con audiencia preliminar señalada, usar /audiencia-preliminar-abreviado.
---

# Conformidad penal — catálogo (sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Cauce y requisitos de cada conformidad** → `buscar_articulo` (`ley="LECrim"`, arts. 655, 784, 785, 787 y 801).
- **Pena del delito, reducción de un tercio y suspensión** → `buscar_articulo` (`ley="CP"`, tipo aplicable y art. 80).
- **Doctrina de la Sala Segunda sobre el control judicial y los límites de la conformidad** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`; para el régimen de la LO 1/2025, `fecha_desde="03/04/2025"`) + `leer_sentencias` con `parrafos=3`.
- **Criterio de la Audiencia en conformidades de guardia y del abreviado** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="AP"`, `provincia` de la causa).
- **Persona jurídica que se conforma (art. 785.11)** → `buscar_empresa_mercantil` para comprobar quién la administra y puede representarla.
- **Revisar el escrito o el acta y el documento del art. 785.7 in fine** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Elige el cauce de conformidad, verifica sus requisitos y redacta el escrito o acta. **Cuatro cauces
distintos, con requisitos distintos.** Confundirlos es el error nuclear de esta materia.

---

## 🚨 ERRATA ESTRUCTURAL — «la conformidad está en el art. 787 LECrim» ES FALSO desde el 3-4-2025

La **LO 1/2025** (vigente **3-4-2025**) reordenó los arts. 785-787 LECrim. **Todo el material anterior
a abril de 2025 está desfasado en este punto**, incluidas versiones previas de esta misma skill.

| Artículo | ANTES (derogado) | **VIGENTE desde 3-4-2025** |
|---|---|---|
| **785** | admisión de prueba y señalamiento | **AUDIENCIA PRELIMINAR** (785.1-3) + **CONFORMIDAD** (785.4-11) |
| **786** | celebración del juicio oral | **señalamiento** |
| **787** | **CONFORMIDAD** | **celebración del juicio oral** |

> **Si un escrito, una minuta o un modelo dice «conformidad del art. 787», está mal.** La sede
> sustantiva de la conformidad en el abreviado es hoy el **art. 785.4 a 785.11**. Verificado
> literalmente contra el BOE el **2026-07-17**.

### ⭐ HALLAZGO VERIFICADO — el límite de los 6 años NO subsiste

El **art. 787.1 derogado** decía: «**Si la pena no excediere de seis años de prisión**, el Juez o
Tribunal dictará sentencia de conformidad…». **Ese inciso desapareció.** El art. 785.4 vigente dice
solo: «El juez, jueza o tribunal dictará sentencia de conformidad con la pena manifestada por la
defensa y el acusado, **si concurren los requisitos establecidos en los apartados siguientes**» — y
los apartados siguientes (785.5 a 785.11) **no contienen ningún límite de pena**.

- **Art. 655 (sumario):** tampoco. La redacción derogada lo limitaba a la «**pena correccional**»;
  la vigente (LO 1/2025) **suprimió** esa restricción y no la sustituyó por otra.
- **⚠️ Trampa: el «seis años» que hoy figura en el art. 787.1.a) NO es el límite de la conformidad.**
  Es el límite de la pena **de distinta naturaleza** para celebrar el juicio **en ausencia** del
  acusado. Cosa distinta. No lo cites como límite de la conformidad.
- **Operativo:** **no afirmes que existe un tope de 6 años** en el abreviado ni en el sumario. Si el
  cliente o el instructor lo invocan, señala que el texto vigente no lo recoge. Como el punto es
  reciente y de lectura no pacífica, **contrasta con `buscar_sentencias`** antes de fundar en ello
  una estrategia, y marca la conclusión `[verificar]` en el escrito si el criterio del órgano es
  desconocido. Lo que sí subsiste son los **topes propios del art. 801** (guardia).

### ⚠️ Defecto de coordinación legislativa — verificado

La LO 1/2025 **no** actualizó las remisiones internas. Verificado literalmente:

| Precepto | Remite a… | Estado |
|---|---|---|
| **784.3** | «conformidad … en los términos previstos en el **artículo 787**» | **Descoordinado** — el régimen está en el 785 |
| **801.1** | «Sin perjuicio de la aplicación en este procedimiento del **artículo 787**» | **Descoordinado** |
| **801.2** | «control de la conformidad … en los términos previstos en el **artículo 787**» | **Descoordinado** |
| **801.3** | «a los efectos de lo dispuesto en el **artículo 81.3.ª CP**» | **Doblemente desfasado** — el 81 CP fue derogado por la LO 1/2015; el requisito de responsabilidad civil está hoy en el **art. 80.2.3.ª CP** |

**Regla de la casa:** cita el **art. 785** como sede sustantiva. Si reproduces la remisión legal del
784.3 o del 801, hazlo con conciencia del desajuste y adviértelo en nota. **Contrasta con
`buscar_sentencias`** antes de construir una estrategia sobre el desajuste.

---

## Comprobaciones previas — antes de negociar nada

1. **Prescripción del delito (art. 131 CP).** Conformarse con un delito prescrito es mala praxis.
   5 años el común; 1 año delitos leves e injurias/calumnias. Ver `references/anclas-normativas-penal.md` § 3.3.
2. **Plazo de instrucción (art. 324 LECrim).** 12 meses + prórrogas de ≤6 meses por auto motivado
   **previo** al vencimiento. Sin ese auto, **las diligencias posteriores no son válidas (324.3)**.
   Si la acusación se sostiene sobre diligencias inválidas, **no negocies: pide la nulidad**.
3. **Ley penal más favorable (art. 2.2 CP).** Dos reformas recientes: **LO 1/2025** y **LO 1/2026**
   (multirreincidencia, vigente 10-4-2026, que reescribió el **art. 248** y tocó 22.8.ª, 66.2, 80.2,
   234.2, 235.1, 250.1.8.º). Hechos anteriores al 10-4-2026 → **compara penas y pide la más
   favorable**. Una conformidad sobre la redacción antigua cuando la nueva es más benigna es un error
   grave.
4. **Suspensión de la ejecución (art. 80 CP, redacción LO 1/2026).** Calcula **antes** de conformarte
   si la pena resultante es suspendible: ≤2 años (80.2.2.ª), primariedad delictiva (80.2.1.ª) y
   responsabilidades civiles (80.2.3.ª, basta el **compromiso**). ⭐ Novedad LO 1/2026: no computan
   los antecedentes de delitos que «**carezcan de relevancia** para valorar la probabilidad de
   comisión de delitos futuros». **La conformidad solo es buena si la pena es suspendible.**
5. **Conflicto de interés** si defiendes a persona física y jurídica por los mismos hechos.

---

## Cauce 1 — Conformidad en la AUDIENCIA PRELIMINAR (art. 785.4-785.11) · abreviado

**Sede:** comparecencia del art. 785, ante el órgano de enjuiciamiento, ya con las actuaciones a su
disposición. Requiere **asistencia del acusado y del abogado defensor** (785.2).

- **785.4:** conformidad con el escrito de acusación de **pena de mayor gravedad**, o con el que se
  presente **en el acto** — que **no puede referirse a hecho distinto ni contener calificación más
  grave** que la anterior.
- **⭐ 785.4 párr. 2 — DEBER NUEVO DEL FISCAL:** oirá **previamente a la víctima o perjudicado**,
  aunque **no estén personados**, siempre que sea posible y se estime necesario; **en todo caso**
  cuando la gravedad o trascendencia del hecho, o la intensidad o cuantía, sean especialmente
  significativas; y **siempre** que la víctima esté en **situación de especial vulnerabilidad**.
  > **Uso táctico:** si defiendes, comprueba que se ha cumplido — su omisión es un defecto de los
  > «requisitos o términos» del 785.10. Si acusas en nombre de la víctima, **exígelo**.
- **785.5:** control judicial de la corrección de la calificación y de la procedencia de la pena;
  audiencia al acusado sobre si su conformidad fue **libre** y con **conocimiento de sus
  consecuencias**.
- **785.6:** calificación incorrecta o pena improcedente → requerimiento a la acusación más grave;
  si no la modifica → **celebración del juicio**.
- **785.7:** informada la persona acusada, se le requiere para que preste conformidad. Si el órgano
  **duda de la libertad** de la conformidad → juicio. También si el defensor lo considera necesario y
  el órgano estima fundada su petición.
- **⭐ 785.7 in fine — DEBER NUEVO DEL LETRADO:** «**El letrado o la letrada facilitará por escrito a
  la persona a quien defiende la información sobre el acuerdo alcanzado.**» **Genera siempre ese
  documento** (ver abajo). Es obligación legal, no cortesía, y es tu prueba de diligencia.
- **785.8:** no vinculan las conformidades sobre **medidas protectoras** en casos de limitación de la
  responsabilidad penal.
- **785.9:** sentencia **oral**, documentada conforme al art. 789.2. Si Fiscal y partes manifiestan
  no recurrir → **firmeza declarada en el acto**, y pronunciamiento, previa audiencia, sobre
  **suspensión o sustitución**, **aplazamiento de responsabilidades pecuniarias**, requerimientos y
  **liquidación de condena**.
  > **Uso táctico:** lleva preparada la petición de suspensión y el plan de pago. El 785.9 permite
  > resolverlo **en el mismo acto**: se gana meses de incertidumbre.
- **785.10:** solo recurribles cuando **no se hayan respetado los requisitos o términos** de la
  conformidad. **El acusado no puede impugnar por razones de fondo su conformidad libremente
  prestada.** Explícaselo al cliente **antes**, y déjalo escrito.
- **785.11 — persona jurídica:** la conformidad la presta su **representante especialmente designado
  con poder especial**; es **independiente** de la posición de los demás acusados y **no vincula** en
  el juicio de estos.
- **785.12:** la comparecencia se registra conforme al art. 743.

---

## Cauce 2 — Conformidad PREMIADA ante el juzgado de guardia (art. 801) · juicio rápido

**Reducción de UN TERCIO**, «aun cuando suponga la imposición de una pena inferior al límite mínimo
previsto en el Código Penal» (801.2). Requisitos **ACUMULATIVOS** (801.1) — verificados:

1. Que **NO se haya constituido acusación particular**, y el Fiscal haya solicitado la apertura del
   juicio oral, acordada por el juez de guardia, presentando **en el acto** escrito de acusación.
2. Que los hechos se califiquen como delito castigado con pena de **hasta 3 años de prisión**, con
   **multa** cualquiera que sea su cuantía, o con otra pena de distinta naturaleza cuya duración **no
   exceda de 10 años**.
3. Que, tratándose de pena privativa de libertad, la solicitada o **la suma** de las solicitadas **no
   supere, REDUCIDA EN UN TERCIO, los 2 años** de prisión.

- **801.2:** control judicial de la conformidad; sentencia **oral**; pena **reducida en un tercio**;
  firmeza en el acto si nadie recurre; resolución sobre suspensión o sustitución.
- **801.3 — suspensión con MERO COMPROMISO:** basta el **compromiso** de satisfacer las
  responsabilidades civiles en el plazo prudencial que fije el juzgado. Y si se precisa certificación
  de deshabituación (art. 87.1.1.ª CP), basta el **compromiso de obtenerla**.
  > ⚠️ El 801.3 remite al **«art. 81.3.ª CP»**, precepto **derogado**. Léelo hoy como **art. 80.2.3.ª CP**.
- **801.4:** dictada la sentencia, el juez de guardia resuelve sobre libertad o ingreso, practica los
  requerimientos y remite las actuaciones al **«Juzgado de lo Penal que corresponda»**, que
  **ejecuta**.
  > 📌 El 801.4 conserva literalmente el rótulo «Juzgado de lo Penal» (redacción de 2009, no tocada
  > por la LO 1/2025). **Al citar el precepto se transcribe así.** El órgano es hoy la **Sección de
  > lo Penal** del Tribunal de Instancia: la **DA 1.ª de la LO 1/2025** ordena entender la mención
  > hecha a esa Sección.
- **801.5:** **si hay acusador particular**, el acusado puede conformarse **en su escrito de defensa**
  con la más grave de las acusaciones, según los apartados anteriores.
- **Puerta de entrada adicional (art. 779.1.5.ª):** si el investigado, **asistido de su abogado**,
  reconoce los hechos a presencia judicial y estos caben en los límites del 801, el juez convoca
  inmediatamente al Fiscal y a las partes e incoa diligencias urgentes por los trámites de los
  arts. 800 y 801.

> **La decisión estratégica más rentable del penal ordinario.** El tercio del 801 no se recupera
> después: fuera de la guardia, **no hay rebaja legal tasada**. Calcula el resultado **antes** de la
> guardia, no durante.

---

## Cauce 3 — Conformidad en el ESCRITO DE DEFENSA (art. 784.3)

- Escrito **firmado también por el acusado**, manifestando conformidad con la acusación.
- También cabe con el **nuevo escrito de calificación** que firmen conjuntamente las acusaciones, el
  acusado y su letrado, **en cualquier momento anterior a la celebración de las sesiones del juicio**.
- ⚠️ El 784.3 remite al «art. 787» **dos veces** (incluido un «art. 787.1» que hoy regula la
  asistencia al juicio). **Descoordinado**: el régimen es el del **art. 785**.

## Cauce 4 — Conformidad en el SUMARIO (art. 655) · procedimiento ordinario

- Al evacuar el traslado de calificación: conformidad absoluta con la más grave y con la pena pedida;
  la defensa expresa si aun así conceptúa **necesaria** la continuación del juicio.
- **Sin límite de pena** en la redacción vigente (la LO 1/2025 suprimió el «pena correccional»).
- **655.1 párr. 2** incorpora el mismo **deber del letrado** de facilitar por escrito la información
  del acuerdo. **655.2**: mismo deber del Fiscal de oír a la víctima. **655.6-655.8**: sentencia oral,
  recurribilidad limitada y persona jurídica, en paralelo al 785.
- **655.4:** disenso **solo** sobre responsabilidad civil → el juicio se limita a ese punto.
- El tribunal **no puede imponer pena mayor que la solicitada** (655.5).
- Varios procesados sin conformidad unánime → **continúa el juicio**.

---

## Entregable 1 — Escrito / acta de conformidad

1. Encabezamiento al órgano competente (**Sección de lo Penal** del Tribunal de Instancia, Audiencia
   Provincial o **Sección de Instrucción** en funciones de guardia), con nº de procedimiento.
   > ⭐ **Copia la denominación exacta que figure en la resolución que contestas o en la carátula del
   > procedimiento.** Es lo que nunca falla, diga «Sección» o siga diciendo «Juzgado».
2. Comparecencia de procurador y letrado de `[ACUSADO]`.
3. **Cauce invocado, con cita correcta**: art. 785.4 (audiencia preliminar), art. 801 (guardia),
   art. 784.3 (escrito de defensa) o art. 655 (sumario). **Nunca «art. 787»** para la conformidad.
4. Escrito de acusación al que se presta conformidad (el de **pena de mayor gravedad**) o nuevo
   escrito conjunto de calificación, con la constancia de que **no altera los hechos ni agrava la
   calificación**.
5. Pena aceptada, **con el cálculo escrito**: pena solicitada → reducción del tercio si es el 801 →
   pena resultante → **encaje en el art. 80 CP**.
6. Constancia de la **información al acusado** y de la **voluntariedad** (785.5 y 785.7).
7. En su caso: constancia de que el Fiscal ha **oído a la víctima** (785.4 párr. 2 / 655.2).
8. Responsabilidad civil: cuantía, forma de pago o **compromiso** (801.3 / art. 80.2.3.ª CP).
9. Petición expresa de los pronunciamientos del **785.9**: suspensión o sustitución, aplazamiento de
   responsabilidades pecuniarias y liquidación de condena.
10. Persona jurídica: identificación del **representante especialmente designado** y del **poder
    especial** (785.11 / 655.8).
11. SUPLICO: que se dicte sentencia de conformidad. Lugar, fecha y **firma del letrado y del
    acusado** cuando el cauce lo exija (784.3).

## Entregable 2 — ⭐ Información escrita al defendido (art. 785.7 in fine / 655.1)

**Obligatorio. Genéralo siempre, como documento separado**, dirigido a `[ACUSADO]` y no al juzgado:

1. Hechos que se aceptan y calificación jurídica.
2. **Pena exacta** que se impondrá y su cómputo (incluida la rebaja del tercio si es el 801).
3. **Responsabilidad civil** y plazos de pago.
4. **Si la pena quedará suspendida o no**, con qué condiciones y por cuánto tiempo, y **qué ocurre si
   se incumplen**.
5. **Antecedentes penales**: que se generan, su plazo de cancelación (art. 136 CP) y su efecto en una
   condena futura — con mención de la **agravante de reincidencia** (art. 22.8.ª CP) y de los tipos
   agravados por **multirreincidencia** de la LO 1/2026 si el delito es patrimonial.
6. Otras consecuencias: privación del permiso de conducir, inhabilitaciones, decomiso, efectos en
   materia de **extranjería** (art. 89 CP) si procede.
7. **⚠️ Advertencia capital del art. 785.10:** que **no podrá impugnar la sentencia por razones de
   fondo**; solo cabe recurso si no se respetan los requisitos o términos de la conformidad.
8. Alternativa: qué ocurriría si fuera a juicio (pena máxima solicitada, prueba de cargo, riesgos).
9. Fecha, firma del letrado y **acuse de recibo firmado por el defendido**. Consérvalo en el
   expediente.

---

## Errores típicos

| Error | Corrección |
|---|---|
| «Conformidad del art. 787 LECrim» | Falso desde el 3-4-2025. Es el **art. 785.4-11** |
| «El límite es de 6 años de prisión» | **No consta en el texto vigente.** Desapareció con la LO 1/2025 |
| Confundir el «6 años» del 787.1.a) con el límite de la conformidad | El 787.1.a) es el juicio **en ausencia**, pena de **distinta naturaleza** |
| Plantear la conformidad «al inicio del juicio» | Su sede es la **audiencia preliminar del 785**. El 787.3 solo admite ya documentos y prueba desconocida |
| Aplicar el tercio del 801 fuera de la guardia | El tercio es **exclusivo del 801**. Con acusación particular, ni siquiera ahí (salvo 801.5) |
| Conformarse sin calcular el art. 80 CP | Una conformidad no suspendible suele ser peor que el juicio |
| Omitir el documento del 785.7 in fine | **Incumplimiento de un deber legal** del letrado |
| No comprobar que el Fiscal oyó a la víctima | Defecto de los «términos» de la conformidad (785.10) |
| Conformidad de persona jurídica sin poder especial | Nula: 785.11 y 655.8 lo exigen |
| Ignorar la LO 1/2026 en delitos patrimoniales | Art. 2.2 CP: puede haber pena más favorable |

## Reglas de trabajo

- **Verifica con `buscar_articulo` antes de citar.** Anclas: `references/anclas-normativas-penal.md`.
- **Jurisprudencia solo vía `jurisprudenciator`** (`buscar_sentencias`, `buscar_por_cita`,
  `leer_sentencias`). **Prohibido inventar** ECLI, ROJ, fechas o ponentes. Sin verificar → `[verificar]`.
- **Prohibido inventar** penas, plazos u ordinales. Lo no verificable se marca `[verificar]` y se dice.
- **Ancla al folio** de las actuaciones toda afirmación de hecho.
- **Anonimización:** `[ACUSADO]`, `[VÍCTIMA]`, `[TESTIGO]`, `[MERCANTIL]`. Los datos de infracciones
  y condenas penales son de **categoría especial (art. 10 RGPD)**. Ver `PROTECCION-DATOS.md`.
- **Instruye el Juez de Instrucción.** No existe el «fiscal instructor» en Derecho vigente.
- Terminología LO 1/2025: Tribunales de Instancia, LAJ, audiencia preliminar.

## Entrega

Dos documentos Word `.docx` (skill `docx`): el **escrito/acta de conformidad** listo para LexNET y la
**información escrita al defendido** del art. 785.7 in fine.
