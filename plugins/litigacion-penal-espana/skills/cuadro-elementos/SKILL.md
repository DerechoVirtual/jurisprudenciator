---
name: cuadro-elementos
description: Cuadro de subsuncion del tipo penal. Fila 0 transversal (prescripcion art. 131 CP, plazo de instruccion art. 324 LECrim, prueba ilicita art. 11.1 LOPJ, presuncion de inocencia art. 24.2 CE, ley mas favorable art. 2.2 CP) y despues tipicidad objetiva, tipicidad subjetiva, antijuridicidad, culpabilidad, punibilidad, iter criminis, autoria y participacion y circunstancias modificativas. Prueba anclada al folio. Usar con cuadro de elementos, subsuncion del tipo, que falta para acusar o para defender.
---

# Cuadro de subsunción del tipo penal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Tipo penal, pena y circunstancias modificativas** → `buscar_articulo` (`ley="CP"`), en la redacción aplicable a la fecha de los hechos.
- **Doctrina sobre cada elemento del tipo** (engaño bastante, dolo, autoría, iter criminis) → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3` y `terminos` del elemento.
- **Fila 0: presunción de inocencia y prueba ilícita** → `buscar_sentencias` (`base="TC"`).
- **Fila 0: plazos** (art. 324 LECrim; art. 131 CP) → `buscar_articulo`.
- **ECLI que aporte la acusación o la defensa contraria** → `buscar_por_cita`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

> **Fuente de cifras:** `references/anclas-normativas-penal.md`. Ninguna pena, plazo o artículo se
> afirma sin estar ahí o sin verificarlo en el momento con `buscar_articulo`.

## Cuándo activar

- "¿Concurren los elementos del tipo?"
- "Cuadro de elementos", "cuadro de subsunción", "matriz de prueba"
- "¿Qué le falta a la acusación?" / "¿Qué tenemos para defender?"
- Antes del escrito de acusación o del escrito de defensa
- **Antes de la audiencia preliminar del art. 785** ← sede de las cuestiones que decide el asunto
- Al valorar una conformidad

## Variantes

- `--defensivo` (por defecto): buscar el elemento que **falta** a la acusación. **Basta con que uno
  no concurra** para que el tipo no se realice.
- `--acusacion`: acreditar que **todos** concurren, cada uno con su folio.
- `--cruzado`: varios investigados con posiciones distintas, o concurso de delitos.

---

## ⭐ FILA 0 — TRANSVERSAL. Se resuelve ANTES que el fondo.

**Obligatoria. Nunca se omite.** Estas comprobaciones ganan el asunto sin llegar a discutir si hubo
engaño bastante o ánimo de lucro. Si alguna prospera, el fondo sobra.

| # | Comprobación | Artículo | Qué mirar | Estado |
|---|---|---|---|---|
| 0.1 | **Prescripción del delito** | **art. 131 CP** | Fecha de los hechos (o de **cese** si continuado/permanente) + plazo según pena máxima: **20/15/10/5 años**; **1 año** delitos leves e injurias y calumnias. Concurso o conexos → plazo del **más grave** (131.4). Pena compuesta → la que exija **mayor** tiempo (131.2). ¿Qué actuación interrumpió y en qué folio? | |
| 0.2 | **Plazo de instrucción** | **art. 324 LECrim** | **12 meses** desde la **incoación** + prórrogas por periodos **≤ 6 meses** mediante **auto motivado previo al vencimiento**. **324.3: sin auto previo (o revocado en recurso), las diligencias acordadas después son INVÁLIDAS.** Las acordadas **antes** son válidas aunque se reciban después (324.2). | |
| 0.3 | **Prueba ilícita** | **art. 11.1 LOPJ** | «**No surtirán efecto las pruebas obtenidas, directa o indirectamente, violentando los derechos o libertades fundamentales**» (verificado). Mirar: entrada y registro, intervención de comunicaciones, cadena de custodia, detención (art. 520), declaración sin información de derechos (art. 118). **Y la conexión de antijuridicidad con el resto del material** — el «directa o indirectamente» es la palanca. | |
| 0.4 | **Presunción de inocencia** | **art. 24.2 CE** | ¿Hay prueba **de cargo**, **válida**, **suficiente** y **practicada en el juicio oral**? La carga es de la acusación: la defensa **no prueba su inocencia**. Diligencias sumariales no reproducidas en juicio → arts. 714 y 730 LECrim. | |
| 0.5 | **Ley penal más favorable** | **art. 2.2 CP** | Redacción del CP vigente **a la fecha de los hechos** (art. 2.1) vs. posterior. Con **LO 1/2025** (3-4-2025) y **LO 1/2026** (10-4-2026), **hechos anteriores al 10-4-2026 exigen comparación de penas**. «En caso de duda sobre la determinación de la Ley más favorable, **será oído el reo**» (art. 2.2 in fine, verificado). | |

> **Sede procesal:** todas se plantean en la **audiencia preliminar del art. 785** — su objeto
> incluye expresamente competencia, **vulneración de derechos fundamentales**, artículos de previo
> pronunciamiento, **nulidad de actuaciones** y **nulidad de las pruebas** propuestas (art. 785.1).
> Desde la LO 1/2025 **ya no se plantean al inicio del juicio** (art. 787.3). Si se resuelven en
> contra: **protesta** y reproducción en el recurso contra la sentencia (art. 785.3).

---

## Estructura del cuadro — las siete capas

Se recorren **en orden**. Cada capa presupone la anterior: sin tipicidad no se discute
antijuridicidad; sin antijuridicidad no se discute culpabilidad.

### 1. TIPICIDAD OBJETIVA

| Elemento | Qué acreditar |
|---|---|
| **Acción u omisión** | Conducta humana descrita en el tipo. En omisión: **posición de garante** y equivalencia (art. 11 CP — *verificar antes de citar*) |
| **Sujeto activo** | ¿Delito común o **especial**? Si es especial, ¿el investigado reúne la cualidad exigida? Si no la reúne, no puede ser autor |
| **Sujeto pasivo** | Titular del bien jurídico. No siempre coincide con el perjudicado |
| **Objeto material** | Sobre qué recae la acción |
| **Resultado** | Solo en delitos de resultado. En los de mera actividad, no hay que probarlo |
| **Nexo causal** | Relación de causalidad naturalística |
| **Imputación objetiva** | Creación de un **riesgo jurídicamente desaprobado** que se **realiza en el resultado**, dentro del **fin de protección de la norma**. Contra-argumentos de defensa: riesgo permitido, autopuesta en peligro de la víctima, prohibición de regreso, comportamiento alternativo conforme a Derecho |

### 2. TIPICIDAD SUBJETIVA

| Elemento | Qué acreditar |
|---|---|
| **Dolo** | Conocimiento y voluntad de los elementos objetivos. Directo de primer grado / de segundo grado / **eventual**. El dolo se acredita por **inferencia** de datos externos: consignar **cada indicio con su folio** |
| **⚠️ Imprudencia** | **art. 12 CP (verificado):** «Las acciones u omisiones imprudentes **sólo se castigarán cuando expresamente lo disponga la Ley**». → **Comprobar en el tipo concreto que existe modalidad imprudente.** Si el tipo no la prevé, la ausencia de dolo es **absolución**, no condena por imprudencia. Este es un argumento de defensa de primer orden y se pasa por alto constantemente |
| **Elementos subjetivos del injusto** | Exigencias anímicas adicionales al dolo: **ánimo de lucro** (hurto, robo, estafa), ánimo de injuriar, finalidad específica. Si el tipo lo exige y no se prueba, **no hay tipo** |
| **Error de tipo** | **art. 14.1 CP (verificado):** error **invencible** sobre un hecho constitutivo de la infracción → **excluye la responsabilidad criminal**. **Vencible** → se castiga **como imprudente** «en su caso» ← y solo si el tipo tiene modalidad imprudente (art. 12). **art. 14.2:** el error sobre un hecho que **cualifique** la infracción o sobre una **circunstancia agravante** **impide su apreciación** |

### 3. ANTIJURIDICIDAD — causas de justificación (art. 20 CP, verificado)

| Causa | Requisitos |
|---|---|
| **Legítima defensa** (art. 20.4.º) | 1.º **Agresión ilegítima** (en defensa de bienes: ataque que constituya delito y los ponga en grave peligro de deterioro o pérdida inminentes; en defensa de la morada: **entrada indebida**); 2.º **necesidad racional del medio** empleado para impedirla o repelerla; 3.º **falta de provocación suficiente** por parte del defensor |
| **Estado de necesidad** (art. 20.5.º) | 1.º que el **mal causado no sea mayor** que el que se trate de evitar; 2.º que la situación **no haya sido provocada intencionadamente**; 3.º que el necesitado **no tenga por su oficio o cargo obligación de sacrificarse** |
| **Cumplimiento de un deber / ejercicio legítimo de un derecho, oficio o cargo** (art. 20.7.º) | Habilitación legal + **proporcionalidad** + necesidad. Sede típica de la actuación policial |

> **⭐ Si falta algún requisito no esencial → eximente INCOMPLETA del art. 21.1ª CP** («las causas
> expresadas en el capítulo anterior, cuando no concurrieren todos los requisitos necesarios para
> eximir», verificado), con la rebaja del art. 68 CP (*verificar*). **La agresión ilegítima es
> requisito esencial de la legítima defensa: sin ella no hay ni eximente incompleta.**

### 4. CULPABILIDAD

| Elemento | Contenido |
|---|---|
| **Imputabilidad** | Causas de inimputabilidad del **art. 20.1.º a 3.º CP** (verificado): **1.º anomalía o alteración psíquica** que impida comprender la ilicitud o actuar conforme a esa comprensión (el **trastorno mental transitorio** no exime si fue provocado con propósito de delinquir o si se previó o debió preverse); **2.º intoxicación plena** por alcohol o drogas, o **síndrome de abstinencia**, con los mismos límites; **3.º alteraciones en la percepción** desde el nacimiento o la infancia con grave alteración de la conciencia de la realidad. En estos tres casos **se aplican, en su caso, medidas de seguridad**. Menores de 18 años → **LO 5/2000** |
| **Conocimiento de la antijuridicidad — error de prohibición** | **art. 14.3 CP (verificado):** error **invencible** sobre la **ilicitud** del hecho → **excluye la responsabilidad criminal**. **Vencible** → **pena inferior en UNO o DOS grados**. ⚠️ No confundir con el error de tipo del 14.1: distinto objeto y distinta consecuencia |
| **Exigibilidad** | **Miedo insuperable** (art. 20.6.º CP, verificado). Estado de necesidad exculpante |

### 5. PUNIBILIDAD

| Elemento | Contenido |
|---|---|
| **Excusas absolutorias** | P. ej. la **excusa absolutoria entre parientes** en delitos patrimoniales sin violencia ni intimidación (**art. 268 CP** — *verificar contenido y límites antes de invocarla*). Regularización tributaria. **Concurren todos los elementos del delito pero no se impone pena** |
| **Condiciones objetivas de punibilidad** | Exigencias ajenas al dolo de las que depende la pena |
| **Requisitos de procedibilidad** | **Denuncia previa del ofendido** en delitos semipúblicos; **querella** en delitos privados; **acto de conciliación del art. 804 LECrim** en injurias y calumnias. ⛔ **No es un MASC**: no hay requisito de MASC ni de burofax en penal |

### 6. ITER CRIMINIS (arts. 15-16 CP)

| Grado | Contenido |
|---|---|
| **Consumación** | Realización de todos los elementos del tipo |
| **Tentativa** (**art. 16.1 CP**, verificado) | «Da principio a la ejecución del delito **directamente por hechos exteriores**, practicando **todos o parte** de los actos que objetivamente deberían producir el resultado, y sin embargo este **no se produce por causas independientes de la voluntad del autor**». Rebaja del art. 62 CP (*verificar*) |
| **⭐ Desistimiento** (**art. 16.2 CP**, verificado) | «Quedará **exento de responsabilidad penal por el delito intentado** quien **evite voluntariamente la consumación**, bien desistiendo de la ejecución ya iniciada, bien impidiendo la producción del resultado» — **sin perjuicio de la responsabilidad por los actos ya ejecutados si fueren constitutivos de otro delito**. **art. 16.3:** si intervienen varios, quedan exentos quienes desistan e **impidan o intenten impedir, seria, firme y decididamente**, la consumación |
| **Actos preparatorios** | Conspiración, proposición y provocación: punibles **solo cuando la ley lo prevé** (arts. 17-18 CP — *verificar*) |
| **Punibilidad** | **art. 15 CP** (*verificar*): la tentativa de **delito leve** no es punible con carácter general — comprobar redacción vigente |

### 7. AUTORÍA Y PARTICIPACIÓN (arts. 27-31 CP)

| Categoría | Contenido |
|---|---|
| **Autores** (**art. 28 CP**, verificado) | «Quienes realizan el hecho **por sí solos, conjuntamente o por medio de otro del que se sirven como instrumento**» → autoría directa, **coautoría** (dominio funcional + acuerdo previo o simultáneo) y **autoría mediata** |
| **Considerados autores** (art. 28, párr. 2) | a) **Inductores** — «los que **inducen directamente** a otro u otros a ejecutarlo»; b) **cooperadores necesarios** — «los que cooperan a su ejecución con un acto **sin el cual no se habría efectuado**» |
| **Cómplices** (art. 29 CP — *verificar*) | Cooperación **no necesaria**. Rebaja del art. 63 CP (*verificar*). **La frontera cooperador necesario / cómplice es la discusión que más pena mueve en la práctica** |
| **Persona jurídica** | **art. 31 bis CP** (*verificar contenido antes de aplicar*). ⚠️ **Conflicto estructural** si se defiende a la vez a la persona jurídica y a la persona física por los mismos hechos |

### 8. CIRCUNSTANCIAS MODIFICATIVAS (arts. 21-23 CP)

**Atenuantes — art. 21 CP (verificado íntegramente):**

| # | Circunstancia | Nota práctica |
|---|---|---|
| 1.ª | **Eximente incompleta** | Las causas del art. 20 «cuando no concurrieren todos los requisitos necesarios para eximir» |
| 2.ª | **Grave adicción** a las sustancias del art. 20.2.º | Exige **grave adicción** y relación causal con el hecho |
| 3.ª | **Arrebato, obcecación** u otro estado pasional de entidad semejante | «Causas o estímulos tan poderosos» |
| 4.ª | **Confesión** | Solo si se confiesa **antes de conocer que el procedimiento se dirige contra él** |
| 5.ª | **⭐ REPARACIÓN DEL DAÑO** | «Reparar el daño ocasionado a la víctima, **o disminuir sus efectos**, **en cualquier momento del procedimiento y con anterioridad a la celebración del acto del juicio oral**». **La que más rinde y la más controlable por la defensa**: depende solo del cliente y de la fecha. **Consignar con anterioridad al juicio y dejar constancia en autos.** Además refuerza la suspensión del art. 80 CP («esfuerzo para reparar el daño») |
| 6.ª | **⭐ DILACIONES INDEBIDAS** | «**Dilación extraordinaria e indebida** en la tramitación del procedimiento, siempre que **no sea atribuible al propio inculpado** y que **no guarde proporción con la complejidad de la causa**». **Tres extremos que hay que probar con la cronología**: identificar los **periodos concretos de paralización con folios**. Sin tabla de fechas, no se sostiene → `/cronologia` la genera |
| 7.ª | **Analógica** | «Cualquier otra circunstancia de análoga significación» |

**Agravantes — art. 22 CP** (*verificar cada una antes de invocarla*). ⚠️ **Reincidencia (art. 22.8ª)
— redacción de la LO 1/2026 (vigente 10-4-2026)**: no se computan antecedentes cancelados o que
debieran serlo, **ni los de delitos leves**, salvo lo dispuesto para los **tipos agravados por
multirreincidencia de delitos leves**. Las condenas firmes de otros **Estados de la UE** producen
efectos de reincidencia salvo cancelación conforme al Derecho español.

**Mixta de parentesco — art. 23 CP** (*verificar*).

> **Muy atenuadas:** valorar si la 5.ª o la 6.ª pueden apreciarse como **muy cualificadas** →
> rebaja del art. 66.1.2ª CP (*verificar*). Es donde está el margen real de pena.

---

## ⚠️ EJEMPLO OBLIGADO — ESTAFA (verificado en BOE el 2026-07-17)

> **La trampa:** todo material anterior a abril de 2026 dice que «el art. 248 define la estafa y el
> art. 249 la castiga». **Eso ya no es cierto y produce un escrito incorrecto.**

**Art. 248 CP — redacción de la LO 1/2026, vigente desde el 10-4-2026 (verificado literalmente).**
Hoy el art. 248 contiene **la definición Y la pena Y el delito leve**:

- **Párr. 1 — definición:** «Cometen estafa los que, con **ánimo de lucro**, utilizaren **engaño
  bastante** para producir **error** en otro, induciéndolo a realizar un **acto de disposición** en
  **perjuicio** propio o ajeno.»
- **Párr. 2 — pena:** «Los reos de estafa serán castigados con la pena de **prisión de seis meses a
  tres años**.» Criterios de fijación: importe de lo defraudado, quebranto económico causado al
  perjudicado, relaciones entre este y el defraudador, medios empleados y demás circunstancias.
- **Párr. 3 — delito leve:** cuantía **≤ 400 €** → **multa de 1 a 3 meses**, salvo que concurra
  alguna circunstancia del art. 250. **⭐ Multirreincidencia:** si el culpable fue condenado
  ejecutoriamente **al menos por tres delitos de la misma naturaleza** del capítulo, **siendo al
  menos uno de ellos leve** → se impone la **pena del párrafo segundo** (prisión 6 meses-3 años).
  **No se computan los antecedentes cancelados o que debieran serlo.**

**⛔ El art. 249 CP YA NO es la penalidad de la estafa.** Desde la **LO 14/2022** (vigente
**12-1-2023**, verificado) el art. 249 regula la **estafa informática y con instrumentos de pago**:
249.1.a) manipulación informática con transferencia no consentida de activo patrimonial;
249.1.b) uso fraudulento de tarjetas, cheques de viaje u otros instrumentos de pago distintos del
efectivo; 249.2 fabricación o facilitación de medios; 249.3 posesión o distribución (mitad inferior).

**Art. 250.1 CP — estafa agravada** (prisión 1-6 años y multa 6-12 meses): 1.º cosas de primera
necesidad, viviendas o bienes de reconocida utilidad social; 2.º abuso de firma o sustracción de
documento público; 3.º patrimonio artístico, histórico, cultural o científico; 4.º **especial
gravedad**; 5.º **valor > 50.000 €** o elevado número de personas; 6.º abuso de relaciones
personales o credibilidad empresarial/profesional; 7.º **estafa procesal**; **8.º multirreincidencia**
(tres delitos menos graves o graves del capítulo, de la misma naturaleza). **Art. 250.2:** 4.º, 5.º,
6.º o 7.º **con** 1.º → prisión **4-8 años** y multa 12-24 meses; **igual si el valor > 250.000 €**.

### Cuadro aplicado — estafa básica (art. 248 CP)

| Capa | Elemento | Artículo | Hecho | Prueba (folio) | Estado |
|---|---|---|---|---|---|
| **0** | Prescripción (pena máx. 3 años → **5 años**, art. 131 CP) | 131 CP | Hechos [FECHA] → vence [FECHA] | f. [N] | |
| **0** | Plazo de instrucción | 324 LECrim | Incoación [FECHA]; prórroga auto [FECHA] | f. [N] | |
| **0** | **Ley más favorable** | **2.2 CP** | Hechos anteriores al 10-4-2026 → comparar art. 249 (redacción LO 14/2022) con art. 248 vigente | — | 🟡 |
| **1** | **Engaño bastante** | 248 párr. 1 | [Maniobra concreta] | f. [N] | |
| **1** | **Error** en la víctima | 248 párr. 1 | [VÍCTIMA] creyó [X] | f. [N] (declaración) | |
| **1** | **Acto de disposición** | 248 párr. 1 | Transferencia de [importe] el [FECHA] | f. [N] (extracto) | |
| **1** | **Perjuicio patrimonial** | 248 párr. 1 | [importe] € | f. [N] (pericial) | |
| **1** | **Nexo**: engaño → error → disposición → perjuicio | 248 párr. 1 | Secuencia sin ruptura | f. [N] | |
| **2** | **Dolo** (antecedente al engaño) | 248 + 12 CP | Indicios: [enumerar] | f. [N] | |
| **2** | **⭐ Ánimo de lucro** | 248 párr. 1 | Destino de los fondos | f. [N] | |
| **2** | **⚠️ ¿Modalidad imprudente?** | **12 CP** | **NO existe estafa imprudente** → sin dolo, **absolución**, no condena imprudente | — | ✅ |
| **8** | Reparación del daño | **21.5ª CP** | Consignación de [importe] el [FECHA] | f. [N] | |
| **8** | Dilaciones indebidas | **21.6ª CP** | Paralización [FECHA]-[FECHA] | f. [N]-[N] | |

> **Puntos de ataque de la defensa en la estafa, por orden de rendimiento:**
> 1. **Engaño bastante** — «bastante» es normativo: si la víctima pudo desplegar la autotutela
>    exigible, decae el tipo. La discusión sobre **deberes de autoprotección** es la más productiva.
> 2. **Dolo antecedente** — si el propósito de no cumplir surgió **después** del contrato, es
>    **incumplimiento civil**, no estafa. ⚠️ Frontera crítica: no importar aquí razonamiento del
>    art. 1101 CC; el argumento penal es que **falta el dolo antecedente**, no que haya
>    responsabilidad contractual.
> 3. **Cuantía ≤ 400 €** → delito **leve** → **prescripción de 1 año** (art. 131 CP). Comprobar
>    siempre la cuantía **antes** que el fondo.

---

## Flujo

### 1. Identificar el tipo penal y su redacción aplicable

- ¿Qué delito imputa cada acusación? (Fiscal, particular, popular — **pueden divergir**)
- **Fecha de los hechos** → **redacción del CP vigente entonces** (art. 2.1 CP)
- **`buscar_articulo` sobre el tipo concreto**, siempre, antes de construir el cuadro
- ¿Ley posterior más favorable? (art. 2.2 CP)

### 2. Cargar el expediente

- `matters/<slug>/matter.md`
- `matters/<slug>/cronologia.md` (aporta la Fila 0 y la tabla de dilaciones)
- Las actuaciones, por folios

### 3. Construir el cuadro capa por capa

Fila 0 → tipicidad objetiva → tipicidad subjetiva → antijuridicidad → culpabilidad → punibilidad →
iter criminis → autoría y participación → circunstancias.

Para CADA elemento: **Artículo (CP/LECrim) · Hecho concreto · Prueba (folio) · Estado**.

### 4. Estado

- ✅ **Acreditado** — hay prueba de cargo válida con folio
- 🟡 **Parcial / discutible** — hay prueba pero admite contra-lectura
- 🔴 **No acreditado** — no hay prueba, o no la hay válida

### 5. Output

`matters/<slug>/cuadro-elementos.md`:

```markdown
# Cuadro de subsunción — [slug]
**Tipo penal:** [ej. Estafa — art. 248 CP, redacción [LO X], vigente a la fecha de los hechos]
**Acusaciones:** [MF: art. X · Acusación particular: art. Y]
**Variante:** [defensivo / acusación / cruzado]
**Fecha de los hechos:** [FECHA] · **Redacción aplicable:** [norma]

## FILA 0 — TRANSVERSAL
[tabla]

## CUADRO POR CAPAS
| Capa | # | Elemento | Artículo | Hecho | Prueba (folio) | Estado |
|---|---|---|---|---|---|---|

## Análisis de cobertura
- Elementos acreditados: [N]/[N]
- **Eslabón más débil de la acusación:** [cuál y por qué]

## GAPS
🔴 [Elemento no acreditado — y qué se sigue de ello]
🟡 [Elemento discutible — contra-argumento disponible]

## Estrategia
1. [Cuestión de Fila 0 a plantear en la audiencia preliminar del art. 785]
2. [Elemento del tipo a combatir en el informe]
3. [Atenuantes a construir — 21.5ª reparación (¡antes del juicio!) / 21.6ª dilaciones]
```

### 6. Decision tree

> 1. **🚨 Si prospera algo de la Fila 0** — es la vía principal: audiencia preliminar del art. 785
> 2. **Si falta un elemento del tipo (🔴)** — tesis absolutoria; construir el informe sobre él
> 3. **Si el tipo concurre** — bajar a **iter criminis** (¿tentativa? ¿desistimiento del 16.2?),
>    **participación** (¿cómplice y no cooperador necesario?) y **atenuantes**
> 4. **Si todo concurre y no hay margen** — valorar **conformidad** (art. 785.4 y ss.; ante el
>    juzgado de guardia, art. 801) y **suspensión** (art. 80 CP)
> 5. **Construir los escritos** — `/redactor-escrito-seccion` (conclusiones del art. 650 LECrim)

## Reglas

1. **Pin-cite al FOLIO en cada celda.** `f. [N]` (con tomo o pieza si procede). Sin folio, el
   elemento **no está acreditado**. ⛔ **Nunca «Doc. nº X»** — nomenclatura civil.
2. **Columna "Artículo" solo CP / LECrim / LOPJ / CE / leyes penales especiales.** ⛔ **Jamás LEC ni
   CC.** Si aparece un artículo del CC o de la LEC en este cuadro, el cuadro está mal.
3. **La Fila 0 va primero y nunca se omite**, aunque parezca que no hay nada: es donde está el 80 %
   del valor de la defensa.
4. **Basta un elemento ausente.** Para la defensa, el cuadro no es una suma: **un solo 🔴 en el tipo
   derriba la acusación**. Identificar el eslabón más débil y concentrar el informe ahí.
5. **Conservador en el estado.** Si dudoso, ✅ → 🟡. La duda favorece al reo (**in dubio pro reo**),
   pero eso se argumenta en el informe: en el cuadro se refleja como 🟡, no como ✅.
6. **Verificar el tipo con `buscar_articulo` SIEMPRE.** El CP se ha modificado dos veces entre 2025
   y 2026. Lo que no se pueda verificar se marca `[verificar]`.
7. **⛔ Prohibido citar jurisprudencia concreta** (ECLI/ROJ/fecha) sin verificarla con
   `buscar_sentencias` / `buscar_por_cita`. Si la doctrina sostiene un elemento (p. ej. los deberes
   de autoprotección en el engaño bastante), escribir `[verificar con buscar_sentencias]`.
8. **Protección de datos.** Marcadores `[INVESTIGADO]`, `[ACUSADO]`, `[VÍCTIMA]`, `[TESTIGO]`,
   `[ÓRGANO]`, `[FECHA]`. **Cero datos reales.** Infracciones y condenas = **art. 10 RGPD**. Cuidado
   extremo con **víctimas menores** y **delitos contra la libertad sexual**.

## ⛔ Fuera de esta skill

- **La tabla de acciones civiles.** Eliminada: desahucio LAU/LEC 250.1.1, incumplimiento 1124/1101
  CC, responsabilidad extracontractual 1902 CC, cláusulas abusivas, cláusula suelo, divorcio. **Nada
  de eso pertenece al orden penal.** La única vertiente civil admisible es la **responsabilidad
  civil derivada del delito** (arts. 109-126 CP y 100, 108-117 LECrim), que se ejercita **dentro**
  del proceso penal y va en la conclusión correspondiente del art. 650 LECrim — no en este cuadro.
- **MASC y burofax.** Del orden civil. No son requisito de procedibilidad en penal.
- **El «fiscal instructor».** Instruye el **Juez de Instrucción**.
