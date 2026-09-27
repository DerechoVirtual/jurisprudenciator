---
name: ley-penal-en-el-tiempo
description: Determina qué redacción del Código Penal se aplica a unos hechos y si la ley posterior es más favorable al reo (arts. 2 y 7 CP, art. 9.3 CE), con aplicación concreta a la LO 1/2026 de multirreincidencia (vigente 10-4-2026) y a la LO 1/2025. Actívala ante "ley más favorable", "ley penal en el tiempo", "retroactividad", "irretroactividad", "qué ley se aplica", "los hechos son de antes de la reforma", "revisión de condena", "revisar la condena", "revisar la sentencia firme", "la reforma me beneficia", "multirreincidencia", "me denegaron la suspensión", "antecedentes irrelevantes", "disposición transitoria", "comparación de penas".
---

# Ley penal en el tiempo — arts. 2 y 7 CP

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Redacción vigente y norma que la dio** → `buscar_articulo` (`ley="CP"`, `articulo` del tipo): indica desde cuándo rige.
- **Redacción anterior y disposiciones transitorias de la reforma** → `buscar_boe` (LO 1/2025, LO 1/2026 u otra reforma) → `leer_boe`.
- **Doctrina sobre la comparación en bloque y la revisión de sentencias firmes** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.
- **Irretroactividad y retroactividad favorable como garantía constitucional** (art. 9.3 CE) → `buscar_sentencias` (`base="TC"`).
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Con **dos reformas penales en 15 meses** (**LO 1/2025**, vigente 3-4-2025, y **LO 1/2026**, vigente **10-4-2026**), determinar qué ley se aplica ha dejado de ser una cuestión teórica. En **todo** asunto con hechos anteriores al 10-4-2026 hay que hacer la comparación.

> **Regla de oro:** identificar **siempre** la redacción del CP vigente **a la fecha de los hechos** y compararla con la vigente. Verificar **ambas** — `buscar_articulo` devuelve la **vigente** e indica desde cuándo lo está y qué norma le dio la redacción actual.

---

## 1. La regla — arts. 2.1 y 7 CP, art. 9.3 CE

### Art. 7 CP — tiempo de comisión
Verificado (`buscar_articulo`, BOE-A-1995-25444, redacción LO 1/2015, vigente desde 1-7-2015), **literal**:

> **Artículo 7.**
> A los efectos de determinar la ley penal aplicable en el tiempo, **los delitos se consideran cometidos en el momento en que el sujeto ejecuta la acción u omite el acto que estaba obligado a realizar.**

**Teoría de la acción, no del resultado.** Cuenta el momento de la **conducta**, no el del resultado. Determinante cuando acción y resultado se separan en el tiempo y entre medias entra en vigor una reforma.

> **Delitos permanentes, continuados y de hábito** `[verificar]`: si la conducta se prolonga a caballo de la entrada en vigor, la determinación del *tempus commissi delicti* es problemática y su solución es **jurisprudencial**. **Verificar con `buscar_sentencias`** antes de afirmar nada. No resolverlo de memoria.

### Art. 2 CP — irretroactividad y retroactividad favorable
Verificado (`buscar_articulo`, redacción LO 1/2015, vigente desde 1-7-2015), **literal e íntegro**:

> **Artículo 2.**
> **1.** No será castigado ningún delito con pena que no se halle prevista por ley anterior a su perpetración. Carecerán, igualmente, de efecto retroactivo las leyes que establezcan **medidas de seguridad**.
> **2.** No obstante, tendrán **efecto retroactivo** aquellas leyes penales que **favorezcan al reo**, **aunque al entrar en vigor hubiera recaído sentencia firme y el sujeto estuviese cumpliendo condena**. En caso de duda sobre la determinación de la Ley más favorable, **será oído el reo**. Los hechos cometidos bajo la vigencia de una **Ley temporal** serán juzgados, sin embargo, conforme a ella, salvo que se disponga expresamente lo contrario.

### ⭐ El alcance exacto respecto de sentencias firmes — leer con precisión
El art. 2.2 CP es **literal y terminante**: la retroactividad favorable opera **«aunque al entrar en vigor hubiera recaído sentencia firme y el sujeto estuviese cumpliendo condena»**.

**Es decir: la firmeza NO es obstáculo.** Ni la firmeza, ni el hecho de estar cumpliendo. Esto es lo que abre la vía de la **revisión de condena** (§ 6). No es una construcción doctrinal: está en el texto de la ley.

**Tres precisiones que no deben perderse:**
- **Las medidas de seguridad** están expresamente excluidas de la retroactividad **desfavorable** (art. 2.1 in fine): las leyes que las establezcan carecen de efecto retroactivo.
- **Leyes temporales** (art. 2.2 in fine): excepción a la retroactividad favorable — los hechos cometidos bajo su vigencia se juzgan **conforme a ella**, salvo disposición expresa en contrario.
- **El procedimiento concreto** de revisión de sentencias firmes lo fijan normalmente las **disposiciones transitorias** de cada reforma. Comprobarlas siempre (§ 3 y § 4).

### Art. 9.3 CE — el anclaje constitucional
Verificado (`buscar_articulo`, BOE-A-1978-31229), **literal**:

> **Artículo 9.**
> **3.** La Constitución garantiza el principio de legalidad, la jerarquía normativa, la publicidad de las normas, **la irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales**, la seguridad jurídica, la responsabilidad y la interdicción de la arbitrariedad de los poderes públicos.

**Ojo a la asimetría:** la CE garantiza la **irretroactividad de lo desfavorable**. La **retroactividad de lo favorable** es de configuración **legal** (art. 2.2 CP), no una garantía expresa del art. 9.3 CE. `[verificar]` su exacto encaje constitucional con `buscar_sentencias` antes de construir sobre ello un motivo de amparo.

---

## 2. ⚠️ Cómo se compara — **EN BLOQUE**

**El error clásico**, y el que más veces arruina un escrito de revisión: **coger lo mejor de cada ley**.

**No se puede.** La comparación se hace **en bloque**: se aplica **íntegramente una ley o íntegramente la otra**. No cabe construir un régimen híbrido tomando el tipo de la ley antigua, la pena de la nueva y las atenuantes de la que convenga. **Esa "tercera ley" no existe y ningún tribunal la acepta.**

### Método
1. **Fijar la fecha de los hechos** (art. 7 CP: momento de la **acción**).
2. **Identificar la redacción vigente entonces** de **todos** los preceptos en juego: tipo, subtipos, circunstancias, reglas de determinación de la pena, penalidad.
3. **Identificar la redacción vigente ahora** de los mismos.
4. **Liquidar la pena resultante COMPLETA bajo cada ley**, por separado y hasta el final: tipo aplicable → grado → circunstancias (arts. 21-23 CP) → reglas de aplicación (arts. 61 y ss., 66 CP) → pena concreta → **penas accesorias** → **multa** → **responsabilidad civil** → **suspensión y sustitución** (art. 80 CP) → **prescripción**.
5. **Comparar los dos resultados finales.** Gana el bloque más favorable **en su conjunto**.
6. **⭐ Oír al reo** — art. 2.2 in fine, **verificado literalmente**: «**En caso de duda sobre la determinación de la Ley más favorable, será oído el reo.**» **Es un trámite legal, no una cortesía.** Documentar la audiencia y la opción del reo. Su omisión, cuando había duda, es alegable.

> **Matiz importante:** «favorable» **no es solo pena más baja**. Puede serlo la **destipificación**, un **plazo de prescripción** menor, un **régimen de suspensión** más accesible (§ 5), la desaparición de una agravante, o un requisito de procedibilidad nuevo. Liquidar el bloque **entero** antes de concluir.

---

## 3. ⭐ Aplicación a la LO 1/2026 — multirreincidencia (vigente **10-4-2026**)

### 3.1 Disposición transitoria
Ancla § 7.3 (verificada): los delitos cometidos **hasta** la entrada en vigor se juzgan conforme a la **ley vigente al tiempo de su comisión**; **pero se aplica la LO 1/2026 si es más favorable al reo**, aunque los hechos sean anteriores (art. 2.2 CP).

**Operativo:** en **todo** asunto con hechos anteriores al **10-4-2026**, comparar redacciones y **pedir la más favorable**. Verificar el texto exacto de la disposición transitoria con `buscar_boe` / `leer_boe` (**BOE-A-2026-7966**) antes de transcribirla en un escrito.

### 3.2 Focos — todos verificados con `buscar_articulo` el 2026-07-17

| Precepto | Qué cambió (LO 1/2026) | Veredicto |
|---|---|---|
| **248** (estafa) | **Reescrito.** Hoy: definición (párr. 1) + **pena 6 meses-3 años** con criterios de fijación (párr. 2) + **≤ 400 € → multa 1-3 meses**, salvo circunstancias del 250; **y multirreincidencia** (tres delitos de la misma naturaleza del capítulo, al menos uno **leve**) → **pena del párr. 2** (párr. 3) | **DESFAVORABLE** en el punto de la multirreincidencia (**agrava** el leve a prisión) → **NO retroactivo** |
| **234.2** (hurto leve) | Multa 1-3 meses si ≤ 400 €; **pero** si condenado ejecutoriamente por **al menos tres delitos de la misma naturaleza** del Título, **siendo al menos uno leve** → **pena del 234.1** (prisión 6-18 meses) | **DESFAVORABLE** → NO retroactivo |
| **235.1.10.º** (teléfonos móviles) | Tipo agravado **NUEVO**: móviles y cualquier **dispositivo móvil de comunicación o de almacenamiento masivo** de información digital susceptible de contener datos personales. **Excluidos** los que estén a la venta, en almacén o exposición en establecimientos comerciales | **DESFAVORABLE** — tipo nuevo → **NO aplicable a hechos anteriores** |
| **235.1.4.º** (agrario) | Requisito **simplificado**: productos agrarios o ganaderos, o instrumentos/medios para su obtención, en explotaciones agrícolas o ganaderas, **y el valor de lo sustraído exceda de 400 €** | **Puede ser DESFAVORABLE** — **amplía** el tipo. Comparar con la redacción anterior caso a caso |
| **250.1.8.º** | **Multirreincidencia**: condena ejecutoria previa por **al menos tres delitos menos graves o graves** del capítulo, de la misma naturaleza | **DESFAVORABLE** → NO retroactivo |
| **22.8.ª** y **66.2** | Los antecedentes por **delitos leves** ahora **sí** computan **cuando integran tipos agravados por multirreincidencia de delitos leves** | **DESFAVORABLE** → NO retroactivo |
| **255.3** (NUEVO) | Defraudación de **energía eléctrica**, cualquiera que sea la cuantía, para abastecer instalaciones usadas para conductas del **art. 368** → prisión 6-18 meses o multa 12-24 meses | **DESFAVORABLE** — tipo nuevo → irretroactivo |
| **568.2** (NUEVO, *petaqueo*) | Sustancia inflamable que sea **combustible líquido** → prisión **3-5 años**; posible pena inferior en grado en conductas de menor entidad | **DESFAVORABLE** — tipo nuevo → irretroactivo |
| **⭐ 80.2.1.ª** (suspensión) | **Ver § 5** | **⭐ FAVORABLE → RETROACTIVO** |

> **Lectura de conjunto:** la LO 1/2026 es, en lo sustantivo, una reforma **agravatoria**. Para hechos anteriores al 10-4-2026, la regla general es que **NO se aplica**: rige la redacción anterior. **La excepción —y la baza— es el art. 80.2.1.ª.**

> **⛔ Antes de aplicar cualquier fila:** verificar **también** la **redacción anterior** del precepto (la vigente a la fecha de los hechos). `buscar_articulo` devuelve la **vigente**; para la histórica, acudir al **BOE consolidado** (BOE-A-1995-25444) y su histórico de versiones. **No reconstruirla de memoria.**

---

## 4. Aplicación a la LO 1/2025 — **no la mezcles con el art. 2 CP**

La **LO 1/2025** (vigente 3-4-2025) es, en lo que afecta al abreviado, una reforma **PROCESAL** (arts. 785-787 LECrim: audiencia preliminar, señalamiento, celebración del juicio oral), no penal sustantiva.

- **Los arts. 2 y 7 CP NO se aplican a las normas procesales.** Su ámbito es la **ley penal** (tipos, penas, medidas de seguridad). Aplicar el art. 2.2 CP a un cambio procesal es un **error de categoría**.
- Rige, en su lugar, el principio ***tempus regit actum***: cada acto procesal se rige por la norma vigente **al tiempo de realizarse el acto**, con independencia de la fecha de los hechos. Un hecho de 2023 enjuiciado hoy se tramita con la **audiencia preliminar del art. 785** vigente.
- **⚠️ Con sus disposiciones transitorias por delante:** la LO 1/2025 tiene un régimen transitorio propio y una entrada en vigor **escalonada** (la reestructuración de los arts. 785-787 entró el **3-4-2025** por su **DF 38.1**). **Verificar la disposición transitoria aplicable** al procedimiento concreto con `buscar_boe` / `leer_boe` (**BOE-A-2025-76**) — sobre todo en procedimientos ya en trámite al 3-4-2025. `[verificar]`
- **⛔ Verificar antes de afirmar.** El principio *tempus regit actum* y su alcance en el proceso penal son de perfil **jurisprudencial**. Contrastar con `buscar_sentencias` antes de fundar una estrategia. **No dar por sentado** que toda la LO 1/2025 es procesal: comprobar precepto a precepto qué se modificó.

> **Regla práctica:** **dos análisis separados, nunca mezclados.**
> - **¿Qué delito y qué pena?** → art. 2 CP, ley vigente a la fecha de los **hechos** + comparación de favorabilidad.
> - **¿Cómo se tramita?** → *tempus regit actum* + disposiciones transitorias.

---

## 5. ⭐ Art. 80.2.1.ª — la baza más rentable de la reforma para la defensa

**FAVORABLE → RETROACTIVO.** Verificado literalmente (`buscar_articulo`, **art. 80 CP, redacción LO 1/2026, vigente desde 10-4-2026**). Condición **1.ª** del art. 80.2:

> «**1.ª** Que el condenado haya delinquido por primera vez. A tal efecto no se tendrán en cuenta las anteriores condenas por delitos imprudentes o por delitos leves, **salvo que estos integren un tipo agravado por multirreincidencia de delitos leves**, ni los antecedentes penales que hayan sido cancelados, o debieran serlo con arreglo a lo dispuesto en el artículo 136. **Tampoco se tendrán en cuenta los antecedentes penales correspondientes a delitos que, por su naturaleza o circunstancias, carezcan de relevancia para valorar la probabilidad de comisión de delitos futuros.**»

### Por qué importa
La reforma introduce **dos incisos de signo opuesto**:
- El primero (**«salvo que estos integren un tipo agravado por multirreincidencia de delitos leves»**) es **desfavorable**: recupera el cómputo de leves en ese supuesto.
- **El segundo es FAVORABLE y de alcance general**: manda **no computar** los antecedentes de delitos que, **«por su naturaleza o circunstancias, carezcan de relevancia para valorar la probabilidad de comisión de delitos futuros»**.

Ese segundo inciso **rompe el automatismo**. Antes, un antecedente vivo por un delito **inconexo** bloqueaba la condición 1.ª y con ella la suspensión ordinaria. Ahora la condición 1.ª incorpora un **juicio material de relevancia prospectiva**, coherente con el criterio-guía del **art. 80.1** (que la ejecución no sea necesaria «para evitar la comisión futura por el penado de nuevos delitos»).

### ⭐ Efecto retroactivo: permite REVISAR suspensiones denegadas
Es **ley penal más favorable** → **retroactiva ex art. 2.2 CP**, **«aunque al entrar en vigor hubiera recaído sentencia firme y el sujeto estuviese cumpliendo condena»**.

**Barrido obligatorio de la cartera.** Revisar **todo** penado con:
- pena privativa de libertad **≤ 2 años** (o suma ≤ 2 años, sin computar la derivada del impago de multa — condición 2.ª), **y**
- **suspensión denegada** —o no solicitada— **por antecedentes**, **y**
- antecedentes por delitos de **naturaleza o circunstancias ajenas** al delito enjuiciado.

**Cómo argumentarlo:**
1. **Identificar cada antecedente** y describir su **naturaleza** y **circunstancias**: tipo delictivo, bien jurídico, antigüedad, contexto, modo de comisión.
2. **Argumentar la IRRELEVANCIA PROSPECTIVA** — es el núcleo. No basta con decir que es antiguo o de otro título: hay que razonar por qué **no sirve para valorar la probabilidad de comisión de delitos futuros**. Ejes: **heterogeneidad** del bien jurídico y de la dinámica comisiva; **lejanía temporal**; **carácter episódico**; **cambio de circunstancias personales** del penado; ausencia de continuidad criminal.
3. **Enlazar con el art. 80.1**: los criterios legales de valoración (circunstancias del delito y personales, antecedentes, **conducta posterior, en particular el esfuerzo para reparar el daño**, circunstancias familiares y sociales, efectos esperables de la suspensión) apuntan en la misma dirección.
4. **Comprobar la condición 3.ª**: responsabilidades civiles satisfechas y decomiso efectivo — o **compromiso** de satisfacerlas **de acuerdo a su capacidad económica** y de facilitar el decomiso, si es razonable esperar su cumplimiento en el plazo prudencial. Documentarlo.
5. **Verificar con `buscar_sentencias`** cómo se está interpretando el inciso: es **muy reciente** (10-4-2026) y su perfil se está construyendo. **No inventar** criterios ni citar resoluciones de memoria.
6. **Cuidado con el otro inciso**: si los antecedentes leves **integran un tipo agravado por multirreincidencia de delitos leves**, la ley nueva es en ese punto **desfavorable** — y ahí no se aplica retroactivamente. **La comparación sigue siendo en bloque** (§ 2).
7. **Vías subsidiarias**: si la condición 1.ª no se salva, valorar la **suspensión excepcional del art. 80.3** (penas que individualmente no excedan de 2 años, siempre que no se trate de **reos habituales**), el **art. 80.4** (enfermedad muy grave con padecimientos incurables) y el **art. 80.5** (penas ≤ 5 años, dependencia de las sustancias del art. 20.2.º, con certificación de deshabituación o tratamiento).

---

## 6. Salida

### 6.1 Tabla comparativa
| | **Redacción a la fecha de los hechos** ([FECHA]) | **Redacción vigente** |
|---|---|---|
| Norma que dio la redacción | | LO 1/2026 (BOE-A-2026-7966) / LO 1/2025 |
| Tipo aplicable | | |
| Subtipo / agravado | | |
| Circunstancias (arts. 21-23) | | |
| Reglas de aplicación (arts. 61 y ss., 66) | | |
| **Pena resultante** | | |
| Penas accesorias | | |
| Multa | | |
| Prescripción (arts. 131, 133) | | |
| **Suspensión (art. 80)** | | |
| **⭐ VEREDICTO — más favorable EN BLOQUE** | | |

Cada celda con su **fuente verificada**. Lo no verificado → `[verificar]` **y decirlo**.

### 6.2 Borrador de escrito
Según proceda:

**(a) Escrito de REVISIÓN DE CONDENA** (sentencia firme, hechos anteriores, ley nueva más favorable):
- Al órgano **sentenciador** — verificar la competencia y el cauce en la **disposición transitoria** de la reforma (`leer_boe`, BOE-A-2026-7966) antes de dirigirlo. `[verificar]`
- Hechos: fecha de los **hechos** (art. 7 CP), sentencia, firmeza, pena impuesta, situación de ejecución.
- Fundamentos: **art. 2.2 CP** —transcrito— con énfasis en «**aunque al entrar en vigor hubiera recaído sentencia firme y el sujeto estuviese cumpliendo condena**»; disposición transitoria de la LO 1/2026; **comparación en bloque** (tabla).
- **SUPLICO**: revisión y aplicación de la redacción más favorable; nueva pena; **nueva liquidación de condena**; y, en su caso, **suspensión ex art. 80 CP**.
- **OTROSÍ — audiencia al reo**: que se le oiga conforme al **art. 2.2 in fine CP**.

**(b) Escrito de ALEGACIÓN DE LEY MÁS FAVORABLE** (causa en trámite): mismo esquema, incorporado al escrito de defensa (art. 784.1) o planteado en la **audiencia preliminar del art. 785.1** — coordinar con `audiencia-preliminar-abreviado`.

**(c) Escrito de SOLICITUD / REVISIÓN DE SUSPENSIÓN** ex art. 80.2.1.ª (§ 5): al órgano de ejecución, con el análisis de irrelevancia prospectiva de **cada** antecedente.

Entregable en Word **`.docx`** para LexNET (skill `docx`). Estilo: `estilo-escritos-judiciales`.

---

## 7. Reglas de la casa

- **⛔ NO existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. Reforma en tramitación prevista para **1-1-2028**: no como Derecho vigente, ni «art. 4 bis EOMF».
- **⛔ Nada de MASC.** Orden **civil**.
- **⛔ Prohibido inventar** penas, plazos, ordinales o artículos — **especialmente las redacciones históricas**, que `buscar_articulo` **no** devuelve: hay que ir al **BOE consolidado** y su histórico de versiones. Lo no verificable → `[verificar]` **y decirlo**.
- **⛔ Prohibido citar jurisprudencia** (ECLI, ROJ, fecha, ponente) sin verificarla con `buscar_sentencias` / `buscar_por_cita` / `leer_sentencias`.
- **Datos personales:** `[ACUSADO]`, `[INVESTIGADO]`, `[VÍCTIMA]`, `[FECHA]`. Los antecedentes penales son **categoría especial**: **art. 10 RGPD** (infracciones y condenas) — extremar el cuidado en esta skill, que trabaja precisamente con hojas histórico-penales. **Cero datos reales.** Ver `PROTECCION-DATOS.md`.
- Perfil del despacho: `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.
- Anclas: `references/anclas-normativas-penal.md` § 1 (reformas), § 3.3-3.4 (prescripción), § 6 (art. 80 CP), § 7 (LO 1/2026).
- **Caducidad:** las anclas se verificaron el **2026-07-17**. Si han pasado más de 6 meses, **re-verificar**.

## 8. Skills relacionadas

`audiencia-preliminar-abreviado` (sede de la alegación) · `ejecucion-penal-liquidacion-condena-suspension-catalogo` (suspensión y liquidación) · `subsuncion-juridica` (tipo aplicable) · `cuadro-elementos` · `prueba-ilicita-nulidad`.
