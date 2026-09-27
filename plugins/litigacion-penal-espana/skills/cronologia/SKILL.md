---
name: cronologia
description: Cronologia penal de doble carril — carril de los HECHOS (fija la redaccion del CP aplicable ex art. 2 CP y el computo de prescripcion del art. 131 CP) y carril PROCESAL (incoacion, plazo del art. 324 LECrim y sus prorrogas, transformacion, acusacion, defensa, audiencia preliminar del art. 785, juicio, sentencia, recursos, ejecutoria). Anclaje al folio de las actuaciones. Usar con cronologia del asunto, timeline penal, control del plazo de instruccion.
---

# Cronología penal — doble carril

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Redacción del CP vigente en cada fecha del carril de los hechos** → `buscar_articulo` (`ley="CP"`): devuelve la vigente, desde cuándo rige y qué norma la dio; si la reforma es posterior a los hechos, la redacción anterior se obtiene con `buscar_boe` → `leer_boe` de la ley de reforma.
- **Plazos del carril procesal** (art. 324 LECrim; arts. 131 y 132 CP) → `buscar_articulo`.
- **Hitos societarios en delitos económicos** (nombramientos, ceses, cambios de domicilio, ampliaciones) → `buscar_empresa_mercantil` y, para fechar un acto concreto, `sumario_borme` del día → `leer_boe`.
- **Paralizaciones que sostienen la atenuante de dilaciones indebidas (art. 21.6.ª CP)** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

> **Fuente de cifras:** `references/anclas-normativas-penal.md`. Ningún plazo, pena o artículo se
> afirma sin estar ahí o sin verificarlo en el momento con `buscar_articulo`.

## Cuándo activar

- "Cronología", "timeline", "qué pasó cuándo"
- "Saca la cronología de [slug]"
- **"¿Está prescrito?"** / **"¿Se ha pasado el plazo de instrucción?"** ← la salida más rentable
- Antes de redactar escrito de defensa, de acusación o cualquier recurso (alimenta el bloque HECHOS)
- Preparación de interrogatorio
- Al recibir un nuevo tomo o pieza de las actuaciones

## ⚠️ Regla estructural: en penal hay DOS carriles y NO se mezclan

| Carril | Qué contiene | Para qué sirve |
|---|---|---|
| **① HECHOS** | Los hechos del delito: la conducta, el resultado, la última actuación delictiva | **Fija la redacción del CP aplicable** (art. 2 CP) y **arranca la prescripción** (art. 131 CP) |
| **② PROCESAL** | Lo que hace el juzgado y las partes desde el atestado | **Fija el plazo de instrucción** (art. 324 LECrim), los plazos de recurso y las nulidades |

Confundirlos es el error que arruina el análisis: la fecha de la denuncia no determina qué ley se
aplica, y la fecha de los hechos no cuenta para el art. 324.

---

## Flujo

### 1. Identificar variante

- **Defensiva** (por defecto — posición habitual del despacho): eventos que sostienen la
  presunción de inocencia, las causas de nulidad y las atenuantes.
- **De acusación** (particular o popular): eventos que sostienen la tipicidad y el perjuicio.
- **De testigo / perito**: solo eventos dentro del conocimiento directo del declarante — alimenta
  `preparacion-interrogatorio`.

### 2. Cargar fuentes

- `matters/<slug>/matter.md` (tesis, calificación provisional, hechos del intake)
- `matters/<slug>/history.md`
- **Las actuaciones**: atestado, declaraciones, autos, informes periciales, escritos de las partes
- Documentación aportada por el cliente

### 3. Carril ① — HECHOS

Para cada hecho:

- **Fecha** (la concreta; si es de tracto continuado o delito permanente, **fecha de inicio y de
  cese** — el cómputo de prescripción arranca del **cese**)
- **Conducta** y **quién** la realiza (`[INVESTIGADO]`, `[VÍCTIMA]`, `[TESTIGO]`)
- **Resultado** y **nexo**
- **Folio** de las actuaciones que lo soporta
- **Significación** según la tesis

> **⚠️ Salida obligatoria del carril ①** — bloque destacado al principio del documento:
>
> 1. **Redacción del CP aplicable** (art. 2 CP): ¿qué texto estaba vigente el día de los hechos?
>    Con **LO 1/2025** (vigente 3-4-2025) y **LO 1/2026** (vigente 10-4-2026) esto no es teórico.
>    **Si los hechos son anteriores al 10-4-2026, comparar penas y pedir la más favorable**
>    (art. 2.2 CP; DT de la LO 1/2026). En caso de duda sobre la ley más favorable, **será oído el
>    reo** (art. 2.2 CP in fine).
> 2. **Prescripción del delito** (art. 131 CP): plazo según la pena máxima del tipo →
>    **20 / 15 / 10 / 5 años**, y **1 año** para delitos leves e injurias y calumnias. Concurso o
>    conexos → plazo del **delito más grave** (art. 131.4). Pena compuesta → la que exija **mayor**
>    tiempo (art. 131.2).
> 3. **Fecha de vencimiento de la prescripción** y **qué actuación la interrumpió**, con su folio.

### 4. Carril ② — PROCESAL

Secuencia típica. Cada hito con **fecha** y **folio**:

1. **Atestado / denuncia / querella** (con fecha de presentación)
2. **⭐ AUTO DE INCOACIÓN** (diligencias previas o sumario) — **arranca los 12 meses del art. 324**
3. **Declaración del investigado** (art. 118 LECrim) — comprobar que se le instruyó de sus derechos
   y que **examinó las actuaciones antes de declarar** (art. 118.1.b)
4. **Diligencias de instrucción** (periciales, testificales, entradas y registros, intervenciones)
5. **⭐ AUTOS DE PRÓRROGA de la instrucción** — **fecha de cada auto**, plazo concedido y nuevo
   vencimiento
6. **Auto de transformación** (procedimiento abreviado) / de procesamiento (sumario)
7. **Escritos de acusación** (Fiscal, acusación particular, popular)
8. **Auto de apertura del juicio oral**
9. **Emplazamiento y escrito de defensa** (art. 784.1: **3 días** para comparecer con abogado y
   procurador; **10 días comunes** para el escrito de defensa)
10. **⭐ AUDIENCIA PRELIMINAR (art. 785)** — sede de las cuestiones previas y de la conformidad
    desde la LO 1/2025. **Ya NO se plantean al inicio del juicio** (art. 787.3)
11. **Señalamiento** (art. 786) y **juicio oral** (art. 787)
12. **Sentencia** (fecha de notificación — es la que cuenta para el recurso)
13. **Recursos**: apelación **10 días** desde la notificación (art. 790.1); preparación de casación
    **5 días** (art. 856)
14. **Firmeza** y **ejecutoria**

### 5. ⭐ FILA DESTACADA OBLIGATORIA — control del art. 324 LECrim

**Nunca se omite. Va al principio del documento, antes que nada.**

```markdown
## 🚨 CONTROL DEL PLAZO DE INSTRUCCIÓN — art. 324 LECrim

| Hito | Fecha | Folio | Vencimiento resultante |
|---|---|---|---|
| **AUTO DE INCOACIÓN** | [FECHA] | f. [N] | **[FECHA + 12 meses]** |
| 1.ª prórroga — auto de [FECHA] | [FECHA] | f. [N] | [FECHA] (+ [N] meses) |
| 2.ª prórroga — auto de [FECHA] | [FECHA] | f. [N] | [FECHA] (+ [N] meses) |
| **VENCIMIENTO VIGENTE** | — | — | **[FECHA]** |

**Estado:** [ ✅ en plazo / 🚨 VENCIDO desde [FECHA] ]

### Diligencias acordadas DESPUÉS de un vencimiento sin auto de prórroga previo

| Diligencia | Fecha en que se acordó | Folio | ¿Auto de prórroga previo? | Consecuencia |
|---|---|---|---|---|
| [Diligencia] | [FECHA] | f. [N] | ❌ NO | **INVÁLIDA — art. 324.3** |
```

**Reglas del art. 324 que gobiernan esta tabla:**

- **12 meses** desde la **incoación**.
- Prórrogas sucesivas por periodos **iguales o inferiores a 6 meses**, de oficio o a instancia de
  parte, **oídas las partes**, mediante **auto motivado** que exponga las causas, **las concretas
  diligencias** pendientes y **su relevancia**.
- **324.2:** las diligencias **acordadas antes** del vencimiento son **válidas aunque se reciban
  después**. ← No confundir la fecha en que se *acuerda* con la fecha en que se *recibe*.
- **⭐ 324.3:** si **antes** del vencimiento el instructor **no dictó** el auto de prórroga, **o este
  fue revocado por vía de recurso**, **NO son válidas las diligencias acordadas a partir de esa
  fecha**. **Este es el argumento de nulidad más rentable y más desatendido del proceso penal.**
- **324.4:** vencido el plazo o sus prórrogas, el juez dicta auto de conclusión del sumario o, en
  abreviado, la resolución que proceda.

> **Sede procesal para hacerlo valer:** la **audiencia preliminar del art. 785** (nulidad de
> actuaciones y nulidad de las pruebas propuestas están expresamente en su objeto, art. 785.1). Si
> se resuelve en contra: **protesta** y reproducción en el recurso contra la sentencia (art. 785.3).

### 6. Deduplicación

Si dos documentos reflejan el mismo hito (p. ej. el auto y su notificación), unificar en una entrada
y consignar **ambos folios**. **La fecha del auto y la de su notificación son datos distintos**: la
del auto cuenta para el art. 324; la de la notificación, para el plazo de recurso.

### 7. Tag de significación

- 🔴 **Crítico** — decisivo (vencimiento del 324, fecha de los hechos, prescripción, prueba ilícita)
- 🟠 **Alto** — sostiene un punto importante
- 🟡 **Medio** — contextual relevante
- 🟢 **Bajo** — contexto

### 8. Output

`matters/<slug>/cronologia.md`:

```markdown
# Cronología — [slug]
**Variante:** [defensiva / acusación / testigo de [TESTIGO]]
**Órgano:** [ÓRGANO] · **Procedimiento:** [tipo y nº]
**Última actualización:** [AAAA-MM-DD]

## 🚨 CONTROL DEL PLAZO DE INSTRUCCIÓN — art. 324 LECrim
[tabla del § 5]

## ⚖️ LEY PENAL APLICABLE Y PRESCRIPCIÓN
- **Fecha de los hechos:** [FECHA] (cese: [FECHA] si continuado/permanente)
- **Redacción del CP aplicable** (art. 2 CP): [texto vigente a esa fecha — identificar la reforma]
- **¿Ley posterior más favorable?** (art. 2.2 CP): [comparación de penas — SÍ/NO + cuál se pide]
- **Plazo de prescripción** (art. 131 CP): [N] años → **vence [FECHA]**
- **Interrupción:** [actuación + fecha + folio]
- **Estado:** [ ✅ vivo / 🚨 PRESCRITO ]

## ① CARRIL DE LOS HECHOS

| Fecha | Sig. | Hecho | Sujeto | Folio |
|---|---|---|---|---|
| [FECHA] | 🔴 | [Conducta] | [INVESTIGADO] | f. [N] |
| .. | .. | .. | .. | .. |

## ② CARRIL PROCESAL

| Fecha | Sig. | Hito | Resolución / actuación | Folio |
|---|---|---|---|---|
| [FECHA] | 🟠 | Atestado | [Cuerpo policial] | f. 1-[N] |
| [FECHA] | 🔴 | **AUTO DE INCOACIÓN** | Diligencias previas [nº] | f. [N] |
| [FECHA] | 🟠 | Declaración del investigado (art. 118) | [ÓRGANO] | f. [N] |
| [FECHA] | 🔴 | **AUTO DE PRÓRROGA** (+[N] meses) | [ÓRGANO] | f. [N] |
| [FECHA] | 🟠 | Auto de transformación | [ÓRGANO] | f. [N] |
| [FECHA] | 🟠 | Escrito de acusación del Ministerio Fiscal | | f. [N] |
| [FECHA] | 🟠 | Escrito de defensa | | f. [N] |
| [FECHA] | 🟠 | Audiencia preliminar (art. 785) | | f. [N] |
| [FECHA] | 🔴 | Juicio oral (art. 787) | | f. [N] |
| [FECHA] | 🔴 | Sentencia — **notificada el [FECHA]** | | f. [N] |

## Narrativa de los hechos significativos (🔴 + 🟠)

[Narrativa fluida y neutra de los hechos con anclaje al folio. Punto de partida para las
CONCLUSIONES PRIMERAS del escrito de calificación o de defensa (art. 650 LECrim).]

## Dilaciones indebidas — insumo para la atenuante del art. 21.6ª CP

| Periodo de paralización | Desde | Hasta | Duración | Folios | ¿Atribuible a la defensa? |
|---|---|---|---|---|---|
| [Descripción] | [FECHA] | [FECHA] | [N] meses | f. [N]-[N] | NO |

> La atenuante exige **dilación extraordinaria e indebida**, **no atribuible al inculpado** y que
> **no guarde proporción con la complejidad de la causa** (art. 21.6ª CP, verificado). Esta tabla es
> la prueba de esos tres extremos: sin fechas y folios, la atenuante no se sostiene.

## Vacíos detectados

- [Hueco: p. ej. "no consta en autos el auto de prórroga que la causa presupone — pedir testimonio"]
- [Hueco: p. ej. "falta el folio de la cadena de custodia entre la intervención y el análisis"]
```

### 9. Decision tree

> **¿Qué hago ahora?**
> 1. **🚨 Si el art. 324 está vencido sin prórroga previa** — nulidad de las diligencias posteriores;
>    plantearlo en la **audiencia preliminar del art. 785**
> 2. **🚨 Si el delito está prescrito** — artículo de previo pronunciamiento / audiencia preliminar
> 3. **Si hay ley posterior más favorable** — `/subsuncion-juridica` para la comparación de penas
> 4. **Llevar la narrativa al escrito** — alimenta las conclusiones de `/redactor-escrito-seccion`
> 5. **Construir el cuadro de subsunción** — `/cuadro-elementos`
> 6. **Cronología de testigo** — `/preparacion-interrogatorio`

## Reglas

1. **Anclaje al FOLIO de las actuaciones.** Siempre `f. [N]` o `f. [N]-[N]`, con tomo o pieza si la
   causa está dividida (`t. II, f. 340`). **Nunca "Doc. nº X"**: esa es nomenclatura civil y en
   penal no identifica nada.
2. **Los dos carriles no se mezclan.** Un hito procesal jamás entra en el carril de los hechos.
3. **La fila del art. 324 es obligatoria** aunque la causa esté en plazo. Si falta la fecha de
   incoación, **pararse y pedirla**: sin ella no hay control de plazo.
4. **Fecha del AUTO, no de la notificación**, para el art. 324. Fecha de la **notificación** para los
   plazos de recurso. Consignar ambas cuando difieran.
5. **No fabricar.** Si el folio no permite afirmar la fecha exacta, escribir `[aprox. mes/año —
   verificar en actuaciones]`. Nunca inventar el número de folio.
6. **Delito continuado o permanente:** consignar inicio **y cese**. La prescripción del art. 131 CP
   se computa desde el **cese**.
7. **Append-only** — no borrar entradas al actualizar; añadir y marcar las que cambien con nota y
   fecha.
8. **Protección de datos.** Marcadores `[INVESTIGADO]`, `[ACUSADO]`, `[VÍCTIMA]`, `[TESTIGO]`,
   `[ÓRGANO]`, `[FECHA]`. **Cero datos reales.** Los datos de infracciones y condenas son de
   **categoría especial (art. 10 RGPD)**. Extremar el cuidado con **víctimas menores** y **delitos
   contra la libertad sexual**: ni el slug ni la cronología revelan identidad.

## ⛔ Fuera de esta skill

- **MASC y burofax como hito.** Son del orden civil. **No existe** intento previo de MASC en penal.
  Lo más próximo, y solo en supuestos tasados: **querella** o **denuncia del ofendido** en delitos
  privados y semipúblicos, y el **acto de conciliación del art. 804 LECrim** en injurias y calumnias.
- **El «fiscal instructor».** Instruye el **Juez de Instrucción**. La reforma que atribuiría la
  instrucción al Ministerio Fiscal está **en tramitación** (prevista 1-1-2028): no se menciona como
  Derecho vigente.
