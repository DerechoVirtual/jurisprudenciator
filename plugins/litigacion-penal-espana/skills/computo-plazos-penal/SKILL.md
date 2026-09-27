---
name: computo-plazos-penal
description: Calcula y audita plazos penales — plazo máximo de instrucción y sus prórrogas (art. 324 LECrim, con detección de diligencias inválidas del 324.3), prescripción del delito (arts. 131 y 132 CP, con el régimen de interrupción y el dies a quo en delitos contra menores), prescripción de la pena (arts. 133 y 134 CP), plazos de recurso (reforma, apelación, casación), plazos de la detención (72 h) y de la prisión provisional (art. 504), y cómputo de días inhábiles y agosto (arts. 182-183 LOPJ y 201 LECrim). Actívala ante "cuándo prescribe", "está prescrito", "se ha pasado el plazo de instrucción", "art. 324", "cuántos días tengo para recurrir", "calcula el plazo", "cuándo vence", "¿llego a tiempo?", "agosto cuenta", "lleva mucho en prisión provisional".
---

# Cómputo y auditoría de plazos penales

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo de instrucción y validez de las diligencias** → `buscar_articulo` (`ley="LECrim"`, `articulo="324"`).
- **Prescripción del delito y de la pena** → `buscar_articulo` (`ley="CP"`, `articulo="131"`, `"132"`, `"133"` y `"134"`) y la pena máxima del tipo concreto en la redacción vigente a la fecha de los hechos.
- **Días inhábiles y cómputo** → `buscar_articulo` (`ley="LOPJ"`, `articulo="182"` y `"183"`; `ley="LECrim"`, `articulo="201"`).
- **Plazos de recurso y de prisión provisional** → `buscar_articulo` (`ley="LECrim"`, arts. 211, 212, 504, 766, 790 y 856).
- **Doctrina sobre la interrupción de la prescripción y las diligencias acordadas fuera de plazo** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

> **Fuente:** anclas § 3 (art. 324, recursos, arts. 131 y 133 CP). Verificados con `buscar_articulo` el
> 2026-07-17: **arts. 132 y 134 CP**; **arts. 201, 211, 504 y 766 LECrim**; **arts. 182 y 183 LOPJ**.

## 🥇 REGLA DE ORO

> **Ante cualquier duda sobre si un plazo venció, DILO CON CLARIDAD y recomienda VERIFICACIÓN HUMANA INMEDIATA.
> NUNCA tranquilices con un cálculo dudoso.** En penal el coste no es una condena en costas: es **la libertad del
> cliente** o **la pérdida irreversible del recurso**. Formato de la incertidumbre: **`⚠️ [verificar] — dos
> hipótesis: [A] vence [FECHA]; [B] vence [FECHA]. Actuar sobre la MÁS CORTA.`** Y siempre: *«confírmalo en el
> calendario judicial del partido y en las actuaciones antes de actuar»*. Actívala también **de oficio** al recibir
> cualquier notificación, auto o sentencia, y en cartera (`/portfolio-status`).

## 1. ⚠️ EL CENTRAL — art. 324 LECrim (anclas § 3.1, Ley 2/2020)

**El control más rentable de la defensa y el más desatendido. Constrúyelo SIEMPRE, aunque la causa parezca en
plazo. Si falta la fecha de incoación, párate y pídela:** sin ella no hay control del 324 y el cálculo es
ficción — no la deduzcas de la denuncia ni del atestado, **no son la incoación**.

- **12 meses** desde la **INCOACIÓN** — no desde los hechos ni la denuncia: **desde el auto**. **Prórrogas** por
  periodos **≤ 6 meses**, de oficio o a instancia de parte, **oídas las partes**, por **AUTO MOTIVADO** que
  exponga **causas** + **concretas diligencias** pendientes + **su relevancia**.
- **324.2:** las diligencias **acordadas ANTES** del vencimiento son **válidas aunque se reciban después**. ← No
  confundas la fecha en que se **ACUERDA** con la fecha en que se **RECIBE**.
- **⭐ 324.3 — LA CLAVE (literal):** si **antes** del vencimiento el instructor **no dictó** el auto de prórroga,
  **o este fue REVOCADO por vía de recurso**, **NO serán válidas las diligencias acordadas a partir de esa fecha**.
- **324.4:** vencido el plazo o sus prórrogas → auto de conclusión del sumario o, en abreviado, la resolución que
  proceda.

**Auditoría de CADA prórroga:** (1) **¿es ANTERIOR al vencimiento?** Si es posterior **no sana nada** — *el fallo
más frecuente*; (2) ¿periodo **≤ 6 meses**?; (3) **¿se oyó a las partes?**; (4) **¿motiva los tres contenidos?**
Un auto estereotipado que no identifica las diligencias concretas es **recurrible**.

> **⭐ El 324.3 tiene DOS puertas.** La conocida (no se dictó el auto) y la que casi nadie explota: **«o este fue
> revocado por vía de recurso»**. **Recurrir el auto de prórroga mal motivado** (reforma 3 d / apelación 5 d)
> puede convertir **retroactivamente** en inválidas todas las diligencias posteriores. **Búscala.**

**Sede:** la **audiencia preliminar del art. 785** (la nulidad de actuaciones y de las pruebas están en su objeto,
785.1) — desde la **LO 1/2025** las cuestiones previas **ya no se plantean al inicio del juicio** (787.3). Si se
desestima → **protesta** y reproducción en el recurso (785.3).

**Línea temporal obligatoria — va la PRIMERA, nunca se omite:**

```markdown
## 🚨 CONTROL DEL PLAZO DE INSTRUCCIÓN — art. 324 LECrim
| Hito | Fecha del AUTO | Folio | Plazo | Vencimiento |
|---|---|---|---|---|
| **AUTO DE INCOACIÓN** | [FECHA] | f. [N] | 12 meses | **[FECHA + 12 m]** |
| 1.ª prórroga — auto de [FECHA] | [FECHA] | f. [N] | ≤ 6 m ([N]) | [FECHA] |
| **VENCIMIENTO VIGENTE** | — | — | — | **[FECHA]** |
**Estado:** [ ✅ en plazo — quedan [N] días / 🚨 VENCIDO desde [FECHA] ]

### Diligencias potencialmente INVÁLIDAS (art. 324.3)
| Diligencia | Fecha en que se ACORDÓ | Folio | ¿Prórroga previa vigente? | Consecuencia |
|---|---|---|---|---|
| [Diligencia] | [FECHA] | f. [N] | ❌ NO | **INVÁLIDA — art. 324.3** |
| [Diligencia] | [FECHA] (recibida [FECHA]) | f. [N] | ✅ acordada antes del vencimiento | **Válida — 324.2** |
```

## 2. Prescripción del DELITO — arts. 131 y 132 CP

**Plazos (art. 131, anclas § 3.3):** **20 años** prisión ≥ 15 · **15** inhabilitación > 10 o prisión > 10 y < 15 ·
**10** prisión/inhabilitación > 5 y ≤ 10 · **5** los demás · **1 año** **delitos leves** e **injurias y
calumnias**. **131.2:** pena compuesta → la que exija **MAYOR** tiempo. **131.4:** concurso o **conexos** → plazo
del **DELITO MÁS GRAVE**. **131.3:** imprescriptibles (lesa humanidad, genocidio, conflicto armado salvo art. 614,
terrorismo **con resultado de muerte**). **⚠️ El plazo se calcula sobre la pena EN ABSTRACTO del tipo**, no la
pedida ni la impuesta, y sobre la **redacción vigente a la fecha de los hechos** (art. 2 CP) — con la **LO 1/2025**
y la **LO 1/2026** ya no es teórico.

### 2.1 ⭐ Dies a quo — art. 132.1 (VERIFICADO, LO 4/2023)

General: **desde el día en que se cometió la infracción**. **Continuado** → desde la **última infracción**;
**permanente** → desde que **se eliminó la situación ilícita**; **habitualidad** → desde que **cesó la conducta**.

**⭐ DELITOS CONTRA MENORES — DOS regímenes. No los confundas: es decisivo.**

| Régimen | Delitos (víctima **menor de 18 años**) | Dies a quo |
|---|---|---|
| **① Mayoría de edad** | aborto no consentido, **lesiones**, contra la **libertad**, **torturas** y contra la **integridad moral**, contra la **intimidad, propia imagen e inviolabilidad del domicilio**, y contra las **relaciones familiares** — *excluidos los del ②* | desde que la víctima **cumple 18 años**; si **fallece antes**, desde el **fallecimiento** |
| **② ⭐ 35 AÑOS** | **tentativa de homicidio**; **lesiones de los arts. 149 y 150**; **maltrato habitual del art. 173.2**; **delitos contra la LIBERTAD SEXUAL**; **trata de seres humanos** | desde que la víctima **cumple 35 AÑOS**; si **fallece antes** de esa edad, desde el **fallecimiento** |

> **⭐ El régimen ② difiere el cómputo hasta los 35 años de la víctima.** En delitos contra la libertad sexual con
> víctima menor, un hecho de hace 25 años **puede estar vivo**. Es el error más grave y más caro de esta materia
> —en defensa (dar por prescrito lo que no lo está) y en acusación (renunciar a un asunto viable)—. **Verifica
> siempre la fecha de nacimiento de la víctima.**

### 2.2 ⭐⭐ INTERRUPCIÓN — art. 132.2 (VERIFICADO — el artículo que más se falla)

> **Literal:** «La prescripción se interrumpirá, **quedando sin efecto el tiempo transcurrido**, cuando el
> procedimiento **se dirija contra la persona indiciariamente responsable del delito**, comenzando a correr
> de nuevo **desde que se paralice el procedimiento o termine sin condena**, de acuerdo con las reglas
> siguientes:»

**⚠️ INTERRUPCIÓN ≠ SUSPENSIÓN. El 132.2 usa las dos:** interrupción (regla 1.ª) → el tiempo transcurrido **queda SIN
EFECTO**, el plazo vuelve a cero. Suspensión (regla 2.ª) → el cómputo **se detiene** hasta 6 meses y, según lo que
ocurra, la interrupción se produce **retroactivamente** o el cómputo **continúa** desde la presentación.

**Regla 1.ª (literal):** se entiende dirigido el procedimiento desde que, **al incoar la causa o con posterioridad**,
se dicte **RESOLUCIÓN JUDICIAL MOTIVADA** que le **atribuya su presunta participación** en un hecho que pueda ser
constitutivo de delito. **No basta** la incoación, ni la denuncia, ni figurar en el atestado. **132.3:** la persona
debe quedar **suficientemente determinada** — **identificación directa** o **datos que permitan concretarla después
en el seno de la organización o grupo**.

**⭐ Regla 2.ª (literal):** «la presentación de **querella** o la **denuncia formulada ante un órgano judicial**, en
la que se **atribuya a una persona determinada** su presunta participación (...), **suspenderá el cómputo de la
prescripción por un plazo máximo de SEIS MESES**, a contar **desde la misma fecha de presentación**». **Los TRES
desenlaces — el mecanismo completo:**

| Dentro de los 6 meses | Efecto |
|---|---|
| **Se dicta** contra el querellado/denunciado —**o contra cualquier otra persona implicada en los hechos**— alguna **resolución de la regla 1.ª** | La interrupción se entiende **RETROACTIVAMENTE producida, a todos los efectos, en la FECHA DE PRESENTACIÓN** ⭐ |
| Recae **resolución judicial FIRME de INADMISIÓN** a trámite, **o** que acuerde **no dirigir el procedimiento** contra él | El cómputo **CONTINÚA desde la fecha de presentación** (la suspensión **no aprovecha**) |
| **El juez NO adopta NINGUNA** de las resoluciones previstas | El cómputo **CONTINÚA igualmente desde la fecha de presentación** ⭐ **la inactividad judicial NO beneficia a quien denuncia** |

> **⭐⭐ El plazo de la regla 2.ª es de SEIS MESES, Y SOLO SEIS.** La redacción anterior distinguía **6 meses
> para el delito y 2 MESES para el delito leve**; **la LO 4/2023 (vigente 29-4-2023) SUPRIMIÓ el de 2 meses**.
> Hoy es **único, sin distinguir por gravedad**. **Todo material que hable de «2 meses para los delitos leves»
> está OBSOLETO.**

**132.4 — Fiscalía Europea:** interrumpen a) el **Decreto motivado** que dirige la investigación contra persona
determinada; b) la querella o denuncia ante ella, **con la regla 2.ª**. ⚠️ Régimen **excepcional y tasado** (intereses
financieros de la UE): **no lo generalices** — fuera de su ámbito **el fiscal no interrumpe, solo la resolución
JUDICIAL motivada**.

## 3. Prescripción de la PENA — arts. 133 y 134 CP

**Plazos (art. 133, anclas § 3.4):** **30 años** prisión > 20 · **25** prisión 15-20 · **20** inhabilitación
> 10 o prisión > 10 y < 15 · **15** inhabilitación > 6 y ≤ 10, o prisión > 5 y ≤ 10 · **10** restantes
**graves** · **5** **menos graves** · **1 año** **leves**. Imprescriptibles: los del 131.3 (133.2). **⚠️ Aquí el
plazo se calcula sobre la pena IMPUESTA**, no sobre la del tipo en abstracto: es la diferencia con el 131.
**Art. 134 (verificado):** **dies a quo** = **fecha de la SENTENCIA FIRME**, o **desde el QUEBRANTAMIENTO** si ya
había comenzado a cumplirse; queda **EN SUSPENSO** a) durante la **suspensión de la ejecución** (art. 80 CP →
anclas § 6) y b) durante el **cumplimiento de otras penas** cuando sea aplicable el **art. 75**. **⭐ Dos errores
frecuentes:** el 134 contempla **suspensión, no interrupción** —el tiempo anterior **no se pierde**, el reloj se
detiene y **se reanuda**—; y el dies a quo es la **firmeza**, no la fecha de la sentencia ni la de su notificación.

## 4. Plazos de recurso

| Recurso | Plazo | Norma |
|---|---|---|
| **Reforma** (y súplica) | **3 días** desde la notificación | **art. 211** ✅ |
| **Reposición/revisión** contra resoluciones del **LAJ** | **3 días** | art. 211 párr. 2 ✅ (el texto dice «Secretarios judiciales») |
| **Apelación contra AUTOS** (abreviado) | **5 días** desde la notificación del auto o del resolutorio de la reforma | **art. 766.3** ✅ |
| **Apelación contra SENTENCIA** | **10 días** desde la notificación | art. 790.1 |
| — ⭐ **suspensión por copia de las grabaciones** | solicitud en los **3 primeros días**; **se reanuda** al entregarse | art. 790.1 |
| — adhesión (**supeditada** a que el apelante mantenga el suyo) / impugnación / traslado / subsanación | en alegaciones del 790.5 (10 d) / **2 d** / 10 d comunes / ≤ 3 d | arts. 790.1, 790.5 y 790.4 |
| **Preparación de casación** | **5 días** desde la última notificación | art. 856 |
| **Escrito de defensa** / comparecencia con abogado y procurador | **10 días** comunes / 3 días | art. 784.1 |

**⭐ La suspensión por copia de las grabaciones (790.1) alarga el plazo y casi nadie la usa.** Los **3 días son de
caducidad**: pedirlo el día 4 **no suspende nada**. **Regla de la casa: ante cualquier sentencia apelable, pedir
copia de las grabaciones en las primeras 72 h**, aunque no se haya decidido recurrir. Consigna **fecha de solicitud**
y **de entrega**: el plazo restante se recalcula sobre ellas. **Matices del 766 (verificado): 766.2: NO hace falta
reforma previa** (cabe subsidiaria o por separado); **766.1:** reforma y apelación **no suspenden** el procedimiento;
**⭐ 766.5: si el auto acuerda PRISIÓN PROVISIONAL el apelante puede pedir VISTA en el escrito de interposición y la
Audiencia la acordará** — **pídela siempre**.

## 5. ⭐ CÓMPUTO — inhábiles y el problema de AGOSTO

**Los preceptos (verificados):** **art. 182 LOPJ** — inhábiles **sábados, domingos, fiestas nacionales y festivos
autonómicos o LOCALES**; **horas hábiles 8:00-20:00**, salvo que la ley disponga otra cosa. **Art. 183 LOPJ (LO
14/2022)** — inhábiles **los días de AGOSTO y todos los del 24 de DICIEMBRE al 6 de ENERO**, ambos inclusive, **para
todas las actuaciones judiciales, EXCEPTO las declaradas URGENTES por las leyes procesales**. **Art. 201 LECrim** —
«**Todos los días y horas del año serán hábiles para la INSTRUCCIÓN de las causas criminales, sin necesidad de
habilitación especial.**»

> **⭐ El art. 183 ya no habla solo de agosto.** Tras la LO 14/2022 el periodo **24-dic a 6-ene** es **también
> inhábil**, con idéntico régimen: aplícale **la misma lógica** que a agosto en todo este § 5.

**✅ SE PUEDE AFIRMAR:** (1) **las ACTUACIONES DE INSTRUCCIÓN son hábiles en agosto y en Navidad, y a cualquier hora**
(art. 201: *todos los días y horas*, **sin habilitación especial** — no hay que pedirla ni justificar urgencia);
(2) las **declaradas URGENTES**, también (183); (3) agosto y 24-dic/6-ene son **INHÁBILES para las demás actuaciones
judiciales**; (4) **sábados, domingos y festivos** —también los **locales**— son inhábiles.

**⚠️ NO SE PUEDE AFIRMAR — `[verificar]` obligatorio:**

> **¿El plazo para RECURRIR un auto dictado en instrucción corre en agosto?**
> El art. 201 declara hábiles todos los días **«para la instrucción de las causas criminales»**. **El texto no
> define si el PLAZO DE INTERPOSICIÓN DE UN RECURSO por una parte es "actuación de instrucción"** (→ corre en
> agosto) **o actuación judicial ordinaria del art. 183 LOPJ** (→ se excluye agosto). **Los preceptos, por sí
> solos, no lo resuelven. ⛔ NO lo resuelvas por intuición ni presentes una lectura como pacífica.**
>
> **Ante todo plazo de recurso que atraviese agosto o el 24-dic/6-ene:**
> 1. **Marca `[verificar]`.** 2. **CALCULA LAS DOS HIPÓTESIS:** **A (agosto HÁBIL — art. 201)** vence **[FECHA]**
>    ← más corta · **B (agosto INHÁBIL — art. 183)** vence **[FECHA]**.
> 3. **🥇 ACTÚA SOBRE LA MÁS CORTA.** Presentar antes no cuesta nada; presentar tarde pierde el recurso de forma
>    irreversible.
> 4. **Recomienda verificación humana inmediata**: criterio del órgano, calendario judicial del partido y, si es
>    determinante, jurisprudencia con `buscar_sentencias` (**nunca de memoria**).

**Otras reglas:** plazos **por días** → **días hábiles**; **por meses o años** (prescripción, 324) → **de fecha a
fecha, sin descontar inhábiles** (los 12 meses del 324 **no** se cuentan en días hábiles). **Dies a quo de los
recursos: la NOTIFICACIÓN**; para el **art. 324, la fecha del AUTO** — consigna ambas cuando difieran. **⚠️ Margen
de la casa: presentar con 2 días hábiles de antelación** (CLAUDE.md, ajustable con `/customize`): **el cálculo da
la fecha límite; la regla de la casa, la fecha objetivo — comunica las dos**.

## 6. Detención y PRISIÓN PROVISIONAL

**Detención — 72 h:** máximo **72 horas** y **tiempo estrictamente necesario** como límite autónomo (arts. 17.2 CE y
520.1 LECrim — anclas § 8), **por horas desde la hora de la detención** que consta en el atestado. **Superado →
detención ilegal** (art. 1.c LO 6/1984) → **`/habeas-corpus` inmediato**. En curso → `/asistencia-detenido`.

**Prisión provisional — art. 504 (verificado, LO 13/2015).** Regla general: **el tiempo imprescindible** para los
fines del art. 503 y **mientras subsistan los motivos** (504.1). **Máximos según el FIN que la motivó:**

| Fin (art. 503) | Pena del delito | Máximo | Prórroga (**UNA SOLA**, por auto, ex art. 505) |
|---|---|---|---|
| **503.1.3.º a)** fuga · **c)** reiteración · **503.2** | **≤ 3 años** | **1 año** | **+ hasta 6 meses** |
| ídem | **> 3 años** | **2 años** | **+ hasta 2 años** |
| **⭐ 503.1.3.º b)** ocultar/alterar/destruir pruebas | cualquiera | **⭐ 6 MESES** | — |

- La prórroga exige **circunstancias que hagan prever que la causa no podrá juzgarse en plazo** (504.2).
  **⭐ Condenado con sentencia RECURRIDA (504.2 in fine):** puede prorrogarse **hasta la MITAD de la pena
  efectivamente impuesta** — régimen **autónomo**, no lo confundas con el anterior. **504.4:** la libertad por
  transcurso **no impide** nueva prisión si, **sin motivo legítimo**, deja de comparecer.
- **⭐ 504.3:** si se decretó **incomunicación o secreto** y **se levanta** antes de los 6 meses, el juez **ha de
  MOTIVAR la subsistencia del presupuesto**. **Exígelo: sin esa motivación la medida decae.**
- **⭐ 504.5 — cómputo:** **se COMPUTA la detención o prisión previa por la MISMA CAUSA** (incluidas las 72 h);
  **se EXCLUYE el tiempo de DILACIONES NO IMPUTABLES a la Administración de Justicia** ← **las dilaciones
  causadas por la defensa alargan de hecho el máximo**: tenlo presente antes de una estrategia dilatoria con el
  cliente en prisión.
- **⭐ 504.6 — alerta de los 2/3:** superadas **las dos terceras partes** del máximo, el órgano **y** el MF
  **comunican** al **presidente de la sala de gobierno** y al **fiscal-jefe** para imprimir **máxima celeridad**,
  y la tramitación **goza de PREFERENCIA**. **Calcula los 2/3 y, alcanzados, pide que se cumpla**: es un **deber
  legal**, no una gracia.

**🚨 ALERTA AUTOMÁTICA — muéstrala sin que la pidan siempre que haya prisión provisional:**

```markdown
## 🚨 PRISIÓN PROVISIONAL — art. 504
- **Ingreso:** [FECHA] · **Detención previa computable (504.5):** [N] días desde [FECHA]
- **Fin que la motivó (503):** [1.3.º a) fuga / b) pruebas / c) reiteración / 503.2]
- **Pena del delito:** [≤ 3 / > 3 años] → **Máximo: [1 año / 2 años / 6 MESES si 503.1.3.º b]** → vence **[FECHA]**
- **Prórroga:** [auto de [FECHA], +[N]] → **nuevo vencimiento [FECHA]** · **Dilaciones excluibles (504.5):** [N] días → [FECHA] ajustada
- **⭐ 2/3 del máximo (504.6):** **[FECHA]** → [ alcanzado: **PEDIR PREFERENCIA** / faltan [N] días ]
- **Estado:** [ ✅ / ⚠️ próximo / 🚨 **VENCIDO — PEDIR LIBERTAD YA** ]
- **Condenado con sentencia recurrida (504.2 in fine):** mitad de la pena impuesta = [FECHA] · **¿se levantó secreto/incomunicación (504.3)?** ¿motivó la subsistencia? [sí/no → **exigirlo**]
```

## 7. Salida

En `matters/<slug>/plazos.md`, por este orden: (1) **🚨 línea temporal del art. 324** (§ 1) — **siempre la
primera**, con las diligencias inválidas; (2) **🚨 control del art. 504** (§ 6) si hay prisión provisional; (3)
**⚖️ prescripción** — hechos y cese · **víctima menor** → régimen 132.1 [① 18 / ② 35 años] y fecha de nacimiento
→ **dies a quo** · redacción del CP aplicable (art. 2 CP) · pena en abstracto y plazo del 131 · **tabla de
interrupciones/suspensiones** (fecha, actuación, folio, efecto del 132.2) · **vencimiento** y estado; en
ejecutoria, lo mismo con los arts. 133-134; (4) **tabla maestra**:

```markdown
| Hito | Norma aplicada | Dies a quo | Vencimiento | Días restantes | Estado |
|---|---|---|---|---|---|
| Plazo de instrucción | art. 324.1 | auto incoación [FECHA] | [FECHA] | [N] | ✅ / 🚨 |
| Apelación de sentencia | art. 790.1 | notificación [FECHA] | [FECHA] | [N] | ⚠️ |
| — copia de grabaciones | art. 790.1 | notificación [FECHA] | **[FECHA+3 d]** | [N] | ⭐ pedir YA |
| Prescripción del delito | arts. 131/132 CP | [FECHA] | [FECHA] | [N] | ✅ |
| Prisión provisional | art. 504.2 | ingreso [FECHA] | [FECHA] | [N] | 🚨 |
```
Estados: **✅ holgado** · **⚠️ < 5 días o dentro del margen de la casa** · **🚨 vencido o vence hoy/mañana** · **❓
`[verificar]` — dos hipótesis calculadas**. Y **(5) actualiza el asunto** → **`/actualizar-asunto`** (vencimiento
del 324, próxima prórroga, prescripción, prisión provisional, próximo vencimiento crítico); **append-only** en
`history.md`.

> **¿Qué hago ahora?**
> 1. **🚨 324 vencido sin prórroga previa** → nulidad de las diligencias posteriores (**audiencia preliminar del art.
>    785**); valorar recurrir el auto de prórroga defectuoso (324.3, 2.ª puerta). **🚨 Delito prescrito** → artículo
>    de previo pronunciamiento / audiencia preliminar
> 2. **🚨 Prisión provisional vencida** → **libertad inmediata**; 2/3 → preferencia (504.6) →
>    `/medidas-cautelares-penales-catalogo` · Detención → `/asistencia-detenido` · ilegal → `/habeas-corpus`
> 3. Sentencia notificada → **copia de grabaciones en 3 días** → `/recurso-apelacion-sentencia-penal-catalogo` ·
>    Hitos → `/cronologia`

## Reglas

1. **🥇 Ante la duda, dilo y recomienda verificación humana inmediata.** Dos hipótesis → **actuar sobre la más
   corta**. Nunca tranquilices con un cálculo dudoso.
2. **Verificar antes de afirmar.** Anclas o `buscar_articulo`; lo no verificable → `[verificar]`. **Nunca
   inventar** plazo, pena, artículo ni fecha: si falta la fecha de incoación, de notificación o de nacimiento
   de la víctima → **pedirla y parar**. **Prohibido citar jurisprudencia concreta** (ECLI, ROJ, fecha,
   ponente) → **`buscar_sentencias`** o no se cita.
3. **Distinguir siempre:** fecha del **AUTO** (324) vs. **NOTIFICACIÓN** (recursos); fecha en que se **ACUERDA** una
   diligencia (324.3) vs. en que se **RECIBE** (324.2). **Mostrar el cálculo**: norma + dies a quo + operación +
   vencimiento — un plazo sin ellos no es auditable.
4. **Protección de datos.** `[INVESTIGADO]`, `[DETENIDO]`, `[VÍCTIMA]`, `[ÓRGANO]`, `[FECHA]`, `[HORA]`. **Cero datos
   reales.** Infracciones y condenas = **categoría especial (art. 10 RGPD)**. **Perfil** (margen, partido y
   **festivos locales**): `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md`.

## ⛔ Fuera de esta skill

- **El «fiscal instructor». NO EXISTE.** Los 12 meses del 324 corren desde el auto de incoación **del juez de
  instrucción**, y solo la **resolución JUDICIAL motivada** interrumpe la prescripción (132.2.1.ª) — salvo el
  régimen tasado de la **Fiscalía Europea** (132.4), que **no se generaliza**. La reforma que la atribuiría al MF
  está **en tramitación** (prevista 1-1-2028): **no se menciona como Derecho vigente**, ni se cita «art. 4 bis
  EOMF». **MASC y plazos civiles** (arts. 130-136 LEC): otro orden.
- **«2 meses» para la suspensión por denuncia en delitos leves.** **Suprimido por la LO 4/2023**: hoy son **6 meses
  únicos**. No reproducir materiales obsoletos.
