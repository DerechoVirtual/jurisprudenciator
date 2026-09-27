---
name: asistencia-detenido
description: >-
  Asistencia letrada ORDINARIA al detenido en comisaría y en el juzgado de guardia (art. 520 LECrim) — checklist de control de la detención, los 10 derechos del art. 520.2, acceso a los elementos esenciales (520.2.d), consignación en acta de incidencias (520.6.b), entrevista reservada previa (520.6.d), incomunicación (arts. 509 y 527) y decisión razonada sobre declarar o no. Actívala ante "me han detenido a un cliente", "guardia", "asistencia al detenido", "estoy en comisaría", "me llaman del Colegio", "tengo una asistencia", "detención", "juzgado de guardia", "¿declara o no declara?". Es el acompañamiento del letrado durante la detención, dentro de sus plazos normales. Si lo que se pretende es impugnar la LEGALIDAD de la detención ante el juez y pedir la puesta en libertad o a disposición judicial inmediata, el cauce urgente es /habeas-corpus.
---

# Asistencia al detenido — art. 520 LECrim

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Derechos del detenido y plazos de la detención** (arts. 118, 509, 520 y 527 LECrim; art. 17 CE) → `buscar_articulo` (`ley="LECrim"` / `ley="CE"`), texto vigente antes de invocarlos en el acta.
- **Delito imputado y su pena** (decide la renuncia del art. 520.8, la incomunicación y la estrategia) → `buscar_articulo` (`ley="CP"`).
- **Normas de la UE sobre asistencia letrada e información** → `buscar_articulo` (`ley="Directiva 2013/48/UE"`; `ley="Directiva 2012/13/UE"`, `articulo="7"` para el acceso a los elementos esenciales).
- **Doctrina constitucional sobre el acceso a los elementos esenciales (art. 520.2.d) y el derecho a no declarar** → `buscar_sentencias` (`base="TC"`) + `leer_sentencias` con `parrafos=3`, para fundar la protesta que se consigna en el acta.
- **Interpretación europea del derecho de acceso y de la asistencia letrada** → `buscar_sentencias` (`base="TJUE"`, consulta sobre la Directiva 2012/13/UE o la 2013/48/UE).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

> **Fuente:** anclas § 8 (art. 520, verificado). Arts. 118, 509 y 527 LECrim y art. 17 CE verificados
> con `buscar_articulo` el 2026-07-17. Nada se afirma sin estar ahí o sin verificarlo en el momento.

## ⏱️ EL RELOJ — calcúlalo antes de nada y dilo en voz alta

Pregunta tres datos. Sin ellos no hay asistencia:

```
1. HORA DE LA DETENCIÓN: [FECHA] [HORA]  →  límite 72 h (520.1): [FECHA] [HORA]
2. HORA DEL ENCARGO:     [HORA]          →  comparecer antes de: [HORA]  (máx. 3 H, art. 520.5)
3. HECHOS IMPUTADOS:     [...]           →  determinan renuncia (520.8), incomunicación (509), estrategia
```

> **⚠️ Las 72 h son el TECHO, no el plazo.** Los arts. 17.2 CE y 520.1 LECrim exigen que la detención no dure más
> del **tiempo estrictamente necesario**: una detención que se prolonga sin practicar diligencia que la
> justifique es **ilegal aunque no llegue a las 72 h**. Casi nadie lo alega — no esperes a la hora 72.

**También a posteriori:** al recibir el atestado de una detención ya practicada, audítala igual — los vicios
pasados alimentan la nulidad.

## 1. CHECKLIST DE CONTROL — art. 520.2

**No preguntes «¿le han leído los derechos?». Verifica uno a uno, y verifica el CÓMO.** Rellena esto con el
detenido delante: es la salida (a) de la skill y la prueba de todo lo demás.

**El CÓMO — los cuatro requisitos se incumplen a diario y son autónomamente impugnables:**

| Punto de control | ¿Cumplido? | ¿Consignado en acta? |
|---|---|---|
| Información **por escrito** | | |
| En **lenguaje sencillo y accesible** — ¿la entendió de verdad? | | |
| En **lengua que comprenda** — ¿intérprete, o se asumió que «se defiende»? | | |
| De **forma inmediata** — hora: [HORA] vs. hora de la detención | | |
| **⭐ ¿CONSERVA EN SU PODER la declaración escrita de derechos?** — durante **toda** la detención. Leérsela y retirarla **incumple** el 520.2. Pregúntaselo y mira si la tiene encima | | |
| ¿Se le informó del **plazo máximo** y del **cauce para impugnar** la detención? | | |
| **Atestado**: ¿refleja **lugar y hora** de la detención y de la puesta a disposición (520.1)? Si no cuadra con lo que refiere el detenido → **consigna la discrepancia**: es la base de un habeas corpus | | |
| **520.2 bis**: ¿se adaptó la información a **edad, madurez, discapacidad** o intoxicación? | | |

**Los derechos (art. 520.2):**

| | Derecho | Qué verificar |
|---|---|---|
| a) | **Silencio** | — |
| b) | **No declarar contra sí mismo** ni confesarse culpable | — |
| c) | **Designar abogado**, asistido sin demora injustificada | ¿Pidió uno de confianza y se lo dieron? **Ninguna autoridad puede recomendar abogado** (520.5) |
| d) | **⭐ Acceder a los ELEMENTOS ESENCIALES para impugnar la detención** | → § 2 |
| e) | **Comunicar a un familiar** el hecho y el **lugar de custodia** | ¿Se hizo? ¿Consta? |
| f) | **Comunicarse telefónicamente con un tercero** | — |
| g) | **Autoridades consulares** | Extranjero → siempre |
| h) | **Intérprete gratuito** | — |
| i) | **Médico forense** | → § 3.a — **pídelo tú** |
| j) | **Asistencia jurídica gratuita** | — |

**🚨 Cierre:** irregularidades detectadas [lista con norma vulnerada] · **Estado:** [ ✅ regular / ⚠️ subsanables /
🚨 **ILEGAL → `/habeas-corpus` YA** ].

## 2. ⭐ Art. 520.2.d — el acceso a los elementos esenciales

**La palanca de toda la asistencia. Pídelo SIEMPRE, POR ESCRITO, antes de decidir nada.**

- Es el derecho a saber **qué hay** contra el detenido para poder impugnar la detención. **No** es el atestado
  íntegro: son los **elementos esenciales** para impugnar la **legalidad de la detención**.
- Si lo deniegan o lo recortan → **pide la consignación en acta de la denegación y su motivo** (520.6.b).
  Denegación sin motivo = habeas corpus (art. 1.d LO 6/1984: derechos no respetados).
- **⭐ Sobrevive a la incomunicación:** el art. 527.1.d permite privar del acceso a las actuaciones **«salvo a
  los elementos esenciales para poder impugnar la legalidad de la detención»** (verificado). **Ni el detenido
  incomunicado pierde este derecho:** reclámalo también ahí.

## 3. Art. 520.6 — las cuatro facultades del abogado. Úsalas las CUATRO

Esto no es presencia pasiva.

**a) Pedir información de derechos y RECONOCIMIENTO MÉDICO (forense).** Pídelo **siempre**, aunque diga que
está bien, y **siempre** ante lesión, malestar, consumo o abstinencia: es lo único que fija su estado físico
y psíquico para el futuro y, si no está en condiciones de declarar, **el forense es quien lo acredita**.
Incomunicado con restricción de comunicaciones → **al menos 2 reconocimientos cada 24 h** (527.3): contrólalo.

**b) Intervenir en declaración, reconocimientos y reconstrucción; y, ⭐ UNA VEZ TERMINADA la diligencia,
pedir la AMPLIACIÓN de extremos y la CONSIGNACIÓN EN ACTA DE CUALQUIER INCIDENCIA.**

> **⭐ La herramienta más infrautilizada de la asistencia letrada. Insiste.** El momento es **al terminar** la
> diligencia. **No te lo van a ofrecer: pídelo tú, expresamente, y que conste que lo pediste.**
> - **Consigna TODO lo anómalo:** horas reales de inicio y fin; que no tenía la declaración de derechos en su
>   poder; denegación del 520.2.d y su motivo; falta de intérprete; entrevista reservada no permitida antes de
>   declarar; estado físico visible; preguntas capciosas; horas sin dormir, comer o sin forense; cualquier presión.
> - **Lo que no consta en acta no existió.** En el juicio, un año después, el acta es lo único que queda: sin
>   consignación, la nulidad es tu palabra contra la del instructor del atestado.
> - Si **se niegan a consignar** → pide que conste **la negativa a consignar**. Y déjalo por escrito.

**c) Informar sobre el consentimiento a las diligencias — frotis bucal / ADN (LO 10/2007).**
Si el detenido **se opone**, esa oposición **puede vencerse**: el **juez** puede imponer la **ejecución
forzosa** con medidas coactivas **mínimas indispensables, proporcionadas y respetuosas con la
dignidad** (anclas § 8). **No le digas ni «no pasa nada por negarse» ni «es obligatorio»**: ninguna es
cierta. Negarse **no impide** la obtención, pero **la forma** está sujeta a esos tres límites.
Ejecución forzosa **sin resolución judicial** o excediendo lo mínimo → **consígnalo** (520.6.b): ahí
hay ilicitud probatoria (art. 11.1 LOPJ).

**d) ⭐ ENTREVISTARSE RESERVADAMENTE CON EL DETENIDO, INCLUSO ANTES DE QUE DECLARE** ante policía,
fiscal o autoridad judicial (salvo art. 527).

> **Ejércelo SIEMPRE y ANTES.** No es un favor: es el art. 520.6.d, reforzado por el **art. 118.2** (verificado),
> que lo reconoce en los mismos términos. **Sin entrevista previa no puedes aconsejar sobre si declarar: no sabes
> qué te va a contar.** Si te la deniegan o la condicionan a que sea después de declarar (sin auto de
> incomunicación del 527) → **la declaración está viciada**: consigna en acta y **no dejes que declare**.

## 4. ⚖️ La decisión central: ¿declarar o no declarar en comisaría?

> **🥇 REGLA DE ORO — dísela al cliente con estas palabras: EL SILENCIO NO PERJUDICA.**
> No hay *ficta confessio* en el proceso penal. **El silencio no puede valorarse como indicio de
> culpabilidad** ni construir la prueba de cargo. Es un derecho fundamental (art. 24.2 CE; arts.
> 118.1.g y 520.2.a-b LECrim, verificados), **no una maniobra sospechosa**. El cliente llega convencido
> de lo contrario («si no hablo, pensarán que soy culpable»): **desmóntalo de entrada**.

**Por defecto, en comisaría NO se declara**: sin conocer las actuaciones, sin tiempo, sin sosiego y en el peor
estado anímico posible. Apartarse del default exige razones concretas, no intuiciones.

| Factor | Pregunta | Empuja hacia |
|---|---|---|
| **¿Hay 520.2.d?** | ¿Sabes qué hay? | Sin acceso → **NO declarar**. Casi siempre decide por sí solo |
| **¿Hay prueba objetiva?** | ¿Grabación, testigos, ADN, in fraganti? | Prueba sólida + versión exculpatoria creíble → puede convenir |
| **¿Conviene versión temprana?** | ¿Hay explicación que evite una cautelar o el propio pase a disposición? | Legítima defensa clara, coartada verificable **ya** → considerar |
| **⚠️ Versión inamovible** | ¿Sabes lo bastante para que esta versión aguante 12 meses de instrucción? | **El mayor riesgo.** Una versión dada a ciegas te ata: cambiarla después destruye la credibilidad |
| **Estado del detenido** | ¿Ha dormido? ¿Intoxicado, en abstinencia, en shock? | Duda → **NO declarar** + **forense** |

**NO, sin ponderación:** no hay 520.2.d · no hubo entrevista reservada previa · no está en condiciones físicas o
psíquicas (→ forense) · no hay intérprete · **no entiendes aún qué se le imputa**.

> **Matiz honesto:** «no declarar» ≠ «no dar nunca una versión». El default es **no declarar en comisaría y
> reservar la declaración para el juzgado de guardia**, ya con acceso a las actuaciones (**art. 118.1.b**,
> verificado). Eso no es silencio definitivo: es silencio **informado**.

## 5. Reglas especiales

**Renuncia a la asistencia letrada — 520.8:** **solo** cabe si la detención lo es por hechos tipificables
**EXCLUSIVAMENTE como delitos contra la seguridad del tráfico**, previa información clara; **revocable en
cualquier momento**. Fuera de ahí **la renuncia es INVÁLIDA** aunque la firme e insista: si el atestado la
recoge en otra detención → **vicio grave**, explótalo. «Exclusivamente» es literal: si concurren lesiones,
desobediencia o atentado, **no cabe**.

**Menores — 520.4:** a disposición de la **Sección de Menores de la Fiscalía**; comunicación a titulares de
patria potestad, tutela o guarda. **⭐ Conflicto de intereses → defensor judicial** (detéctalo activamente:
hechos en ámbito familiar, interés del progenitor contrapuesto). **Menores de 16 años: NUNCA incomunicados**
(art. 509.4, verificado).

**Confidencialidad — 520.7 y 118.4 (verificados):** todas las comunicaciones abogado-investigado son
**confidenciales**; si se captaron o intervinieron, el juez **ordena eliminar la grabación** o entregar la
correspondencia, **dejando constancia**. **Única excepción:** **indicios objetivos de participación del
abogado** en el hecho investigado o de su implicación en otra infracción. **Operativo:** una entrevista a la
vista o al alcance del oído de los agentes **no es reservada** → pide otro lugar y **consigna**.

**Incomunicación — arts. 509 y 527 (verificados):** la acuerda **el juez o el tribunal**, **excepcionalmente**,
por **resolución motivada**, y solo si concurre **necesidad urgente** de: a) evitar graves consecuencias para la
**vida, libertad o integridad física**; o b) una **actuación inmediata** que evite comprometer gravemente el
proceso (509.1). Dura **el tiempo estrictamente necesario, máx. 5 días**; prórroga de **otros 5** solo en
delitos del **art. 384 bis** o cometidos **concertadamente y de forma organizada** por dos o más personas
(509.2). Solo pueden suspenderse **estos cuatro** derechos (527.1): a) abogado **de confianza** → de oficio;
b) **comunicarse** con terceros — **nunca** con la autoridad judicial, el MF ni el **forense**; c) **entrevista
reservada**; d) **acceso a las actuaciones — ⭐ SALVO a los elementos esenciales para impugnar la detención**.

> **Cuatro controles de defensa (527.2):** (1) **¿hay AUTO?**; (2) **⭐ si lo instó la Policía Judicial o el MF,
> las medidas se entienden acordadas solo por un MÁXIMO DE 24 H**, dentro de las cuales **el juez ha de
> pronunciarse** — pasadas sin auto, **la restricción decae**: pide ver el auto y **consigna si no existe**;
> (3) ¿**motiva cada excepción por separado**?; (4) ¿encaja en 509.1.a o b? Fallo en cualquiera → impugnable.

## 6. En el juzgado de guardia — qué cambia

**Art. 118.1.b (verificado):** derecho a **examinar LAS ACTUACIONES** —ya no solo «elementos esenciales»—
**con anterioridad a que se le tome declaración**. Ejércelo **antes**; si no te lo dan, **hazlo constar y
pide la suspensión**. **Reevalúa entonces el § 4**: la respuesta puede cambiar, y a menudo cambia. Juicio
rápido (art. 801, anclas § 5) → **no conformes sin haber leído las actuaciones y calculado la pena**.

## 7. Salida y derivación

En `matters/<slug>/asistencia-detenido-[FECHA].md`: **(a)** checklist del § 1 con el reloj y el estado
final; **(b)** **solicitud de acceso al 520.2.d** —al instructor del atestado o al órgano de guardia;
art. 520.2.d y **527.1.d in fine** si hay incomunicación; y, si se deniega, **que se consigne en acta la
denegación y su motivo** (520.6.b)—; **(c)** **queja / consignación en acta (520.6.b)** —una incidencia
por párrafo, **objetiva y fechada, sin adjetivos**: hecho + hora + norma vulnerada + petición de
consignación; incluir la **negativa a consignar** si la hubo—; **(d)** **decisión razonada sobre declarar
o no** (tabla del § 4 + recomendación + **motivo**): consérvala, es la prueba de que el consejo fue
informado.

> **¿Qué hago ahora?**
> 1. **🚨 Detención ILEGAL** (sin supuestos legales, sin formalidades, > 72 h, lugar inadecuado, derechos
>    vulnerados) → **`/habeas-corpus` YA** — solo sirve mientras dura la privación de libertad
> 2. Prisión provisional → `/medidas-cautelares-penales-catalogo` · Juicio rápido → `/conformidad-penal-catalogo`
> 3. La causa sigue → `/asunto-intake` y `/cronologia` · Plazos → `/computo-plazos-penal` · Encargo →
>    `/hoja-encargo`

## Reglas

1. **Verificar antes de afirmar.** Anclas § 8 para el 520; `buscar_articulo` para lo demás. Lo no
   verificable → `[verificar]`. **Prohibido citar jurisprudencia concreta** (ECLI, ROJ, fecha, ponente) →
   `buscar_sentencias` en el momento, o no se cita.
2. **Nunca tranquilices.** Si dudas de si un derecho se respetó, **dilo como duda y consígnalo**. Aquí el
   coste del error es la libertad del cliente.
3. **Lo que no consta en acta no existió.** Ante cualquier incidencia, la respuesta incluye siempre *«pide
   la consignación en acta (520.6.b)»*.
4. **Nomenclatura (LO 1/2025, desde 3-10-2025):** el órgano es la **Sección de Instrucción del Tribunal de
   Instancia** (art. 14 LECrim), aunque la LECrim siga llamando **«Juez de Instrucción»** al titular
   (arts. 509.1, 520). Usa la denominación de órgano correcta en todo encabezamiento.
5. **Protección de datos.** `[DETENIDO]`, `[INVESTIGADO]`, `[COMISARÍA]`, `[FECHA]`, `[HORA]`. **Cero
   datos reales.** Infracciones y condenas = **categoría especial (art. 10 RGPD)**. El slug nunca lleva el
   nombre del cliente. **Perfil:** `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md`.

## ⛔ Fuera de esta skill

- **El «fiscal instructor». NO EXISTE.** Instruye el **juez de instrucción**, y la incomunicación la
  acuerda **el juez** (509.1) — policía y fiscal solo pueden **instarla**, con el límite de 24 h del 527.2.
  La reforma que la atribuiría al MF está **en tramitación** (prevista 1-1-2028): **no se menciona como
  Derecho vigente**, ni se cita «art. 4 bis EOMF». **MASC y burofax:** orden **civil**, no existen en penal.
- **Aconsejar sobre el fondo sin haber ejercido el 520.2.d y la entrevista reservada.** Sin información, la
  recomendación es no declarar — no una opinión sobre los hechos.
