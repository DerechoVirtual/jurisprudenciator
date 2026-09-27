---
name: preparacion-interrogatorio
description: >-
  Prueba personal en el contencioso-administrativo, donde la prueba reina es el expediente y la pericial. Interrogatorio del perito y testifical de los funcionarios intervinientes. Reglas propias del abreviado (art. 78.13-78.17 LJCA) que desplazan a la LEC: sin pliegos, sin escritos de preguntas, SIN TACHAS. Usar con preparar interrogatorio o guion para la vista.
---

# Preparación de prueba personal — contencioso-administrativo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Reglas de la prueba personal** → `buscar_articulo` (`ley="LJCA"`, artículos 60 y 78; `ley="LEC"`, artículos 301 a 316, 360 a 381 y 377, como supletoria).
- **Valor de las actas y denuncias del agente** → `buscar_articulo` (`ley="LPAC"`, `articulo="77"`).
- **Lex artis referida a la fecha del hecho (pericial sanitaria)** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`, `terminos="lex artis"`).
- **Premisas del perito tasador o arquitecto** → `consultar_catastro` (superficie, año de construcción y uso) y, si aplica una ordenanza, `leer_ordenanza` con `articulo`.
- **Límite deontológico (Estatuto General de la Abogacía)** → `buscar_boe` + `leer_boe` (RD 135/2021) para confirmar la numeración vigente.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## ⚠️ Lee esto antes de preparar nada: aquí el interrogatorio no es la prueba reina

**En el contencioso-administrativo la prueba reina es el EXPEDIENTE ADMINISTRATIVO y la PERICIAL.**
No el interrogatorio. Conviene decirlo abiertamente porque el reflejo civilista lleva a perder el
tiempo donde no hay rendimiento:

- **El interrogatorio de parte contra la Administración es excepcional y de escasa utilidad.** La
  Administración es una **persona jurídica**: no hay un "demandado" que se siente a declarar y se
  contradiga. Su posición consta **por escrito** en el expediente y en la contestación, y su
  conocimiento se vehicula por **informe**. Proponer interrogatorio de la Administración suele
  producir, en el mejor de los casos, la remisión a un informe que ya obra en autos.
- **El pleito se gana en el expediente.** Lo que la Administración hizo, cuándo lo hizo, qué motivó
  y qué omitió está en los folios. La contradicción se busca **entre documentos**, no entre
  declaraciones.
- **Dónde sí rinde la prueba personal** — y hacia ahí orienta esta skill:
  1. **Interrogatorio del PERITO** — contradicción del informe pericial de la Administración
     (el terreno donde de verdad se decide el sanitario, el viario y el valorativo).
  2. **Testifical de los FUNCIONARIOS intervinientes** en el expediente — el agente denunciante,
     el instructor, el técnico que firmó el informe. Son quienes tienen percepción directa de los
     hechos que el expediente documenta (o silencia).

> **Consecuencia práctica:** si la pregunta del usuario es "prepara el interrogatorio de la
> Administración", la respuesta correcta casi siempre es reorientar: proponer pericial y testifical
> de funcionarios, y **discutir el expediente**. Decirlo, no ejecutarlo en silencio.

## Cuándo activar

- "Preparar interrogatorio de [perito / funcionario / agente]"
- "Guion para la vista"
- "Preguntas para contradecir el informe pericial de la Administración"
- Al preparar el **otrosí de recibimiento a prueba** (art. 60.1 LJCA — la prueba **solo** se pide
  por otrosí en demanda o contestación, expresando los **puntos de hecho** y los **medios**)
- Antes de la vista del **abreviado** (art. 78 LJCA)

## Marco normativo — LEC supletoria, pero el abreviado tiene reglas propias

La LJCA no regula el detalle de la prueba personal: la **LEC se aplica supletoriamente**
(**DF 1.ª LJCA**). Base:

- **Interrogatorio de parte: LEC 301-316** (incluida la ficta confessio del art. 304)
- **Testigos: LEC 360-381**
- **Ordinario contencioso:** la prueba se desarrolla "con arreglo a las normas generales
  establecidas para el proceso civil", con plazo de **30 días** para practicarla (**art. 60.4 LJCA**)

### 🚨 En PROCEDIMIENTO ABREVIADO el art. 78 LJCA desplaza a la LEC

Reglas propias, verificadas (art. 78 LJCA, redacción vigente). **Prevalecen sobre la LEC**:

| Regla | Norma | Contenido |
|---|---|---|
| Medios de prueba | **art. 78.12** | Se practican "del modo previsto para el juicio ordinario", **en cuanto no sea incompatible** con los trámites del abreviado — la incompatibilidad es lo que activa las reglas siguientes |
| **Sin pliegos** | **art. 78.13** | "Las preguntas para la prueba de interrogatorio de parte se propondrán **verbalmente, sin admisión de pliegos**" |
| **Sin escritos de preguntas y repreguntas** | **art. 78.14** | "**No se admitirán escritos de preguntas y repreguntas** para la prueba testifical" |
| **Límite discrecional de testigos** | **art. 78.14** | Si el número de testigos fuese excesivo y, a criterio del órgano judicial, sus manifestaciones pudieran constituir **inútil reiteración** sobre hechos suficientemente esclarecidos, **podrá limitarlos discrecionalmente** |
| 🚨 **NO HAY TACHAS** | **art. 78.15** | "**Los testigos no podrán ser tachados** y, **únicamente en conclusiones**, las partes podrán hacer las observaciones que sean oportunas respecto de sus circunstancias personales y de la veracidad de sus manifestaciones" |
| **Sin insaculación de peritos** | **art. 78.16** | "En la práctica de la prueba pericial **no serán de aplicación las reglas generales sobre insaculación de peritos**" |
| **Protesta por denegación de prueba** | **art. 78.17** | Contra la denegación de pruebas (o la admisión de las denunciadas como obtenidas con violación de derechos fundamentales), las partes pueden interponer **en el acto** recurso de **súplica**, que se sustancia y resuelve seguidamente |

> 🚨 **CORRECCIÓN EXPRESA — las tachas del art. 377 LEC NO se aplican en el abreviado.**
> El reflejo civilista dice: "detectar tachas, plantearlas por escrito antes de declarar el
> testigo". **En el abreviado contencioso eso es un error frontal**: el **art. 78.15 LJCA** dispone
> que los testigos **no podrán ser tachados**. La circunstancia que en civil fundaría una tacha
> (dependencia del testigo respecto de la Administración, interés, subordinación jerárquica al
> instructor) **no se articula como incidente de tacha**: se guarda y se hace valer **en
> conclusiones**, como "observación sobre sus circunstancias personales y la veracidad de sus
> manifestaciones".
>
> Esto cambia la táctica, no el objetivo. **No se pierde la munición: se difiere.** Las preguntas
> de acreditación (relación con la Administración, dependencia, quién le encargó el informe) se
> hacen igual — pero su rendimiento no es un incidente previo, sino el material que se explota en
> conclusiones.
>
> En el **ordinario** contencioso el art. 78 no rige. La LEC entra supletoriamente (DF 1.ª LJCA);
> si se pretende articular tacha ex art. 377 LEC, **verificar su encaje** antes de proponerla y no
> asumirlo como automático.

## Flujo

### 1. Identificar al interrogado y descartar lo inútil

- **¿Perito?** → vía principal (§ 5.A)
- **¿Funcionario interviniente en el expediente?** → vía principal (§ 5.B)
- **¿Representante de la Administración, como parte?** → **Avisar de la escasa utilidad** antes de
  preparar nada. Explicar que la Administración declara por escrito / vía informe y que su
  posición ya consta en el expediente. Preparar solo si el usuario insiste tras el aviso, o si
  concurre un supuesto excepcional (p. ej. un hecho personal de una autoridad concreta, no
  documentado, y decisivo).
- **¿Cliente/recurrente persona física?** → puede ser interrogado a instancia de la Administración:
  preparar en clave **defensiva** (anticipar lo que le preguntarán).

### 2. Determinar el CAUCE — condiciona todo el formato

| | **Abreviado** (art. 78 LJCA) | **Ordinario** |
|---|---|---|
| Preguntas de parte | **Verbales, sin pliego** (78.13) | LEC supletoria |
| Testifical | **Sin escritos de preguntas/repreguntas** (78.14) | LEC supletoria |
| Tachas | **NO existen** (78.15) — a conclusiones | LEC 377 `[verificar encaje]` |
| Nº de testigos | Limitable discrecionalmente (78.14) | — |
| Insaculación pericial | No aplica (78.16) | — |
| Denegación de prueba | Súplica en el acto (78.17) | Protesta `[verificar]` |

> ⚠️ **Si es abreviado, el guion NO es un pliego.** Es un **guion de mano** para preguntar de viva
> voz. Formatearlo como pliego articulado ("Diga ser cierto que...") induce al error de intentar
> presentarlo: **no se admite** (78.13/78.14).

### 3. Cargar fuentes

- `matters/<slug>/matter.md` (tesis)
- `matters/<slug>/cronologia.md` (hitos por fecha y **folio del expediente**)
- `matters/<slug>/cuadro-elementos.md` (qué hay que probar o refutar)
- **Expediente administrativo** — los folios en que aparece o interviene el interrogado
- **Informe pericial** de la Administración y, en su caso, el de parte

### 4. Definir objetivos

Priorizar (dos o tres, no más):
- **Acreditar lo que el expediente calla** (la omisión del trámite, la prueba no practicada)
- **Contradecir el informe pericial** de la Administración (método, premisas, alcance)
- **Confirmar el hecho no documentado** que sostiene nuestro elemento
- **Reunir material para conclusiones** (en abreviado: las circunstancias del testigo)

### 5. Redactar el guion

#### A. INTERROGATORIO DEL PERITO — la vía de mayor rendimiento

El objetivo **no** es que el perito se retracte: es **acotar el alcance** de su informe y exponer
sus **premisas**. Un perito que admite que no examinó algo, o que partió de un dato que le dio la
Administración, ya ha rendido lo que tenía que rendir.

```
INTERROGATORIO DEL PERITO — [PERITO], perito de [ÓRGANO] / perito judicial
Asunto: [slug] · Cauce: [abreviado / ordinario]
Informe objeto de contradicción: EA folio [N] / autos folio [N]
Objetivos: [1] acotar alcance · [2] exponer premisas recibidas · [3] [...]

BLOQUE 1 — ALCANCE (qué NO hizo)
- ¿Examinó usted personalmente [objeto / paciente / lugar], o dictaminó sobre documentación?
  · Si "sobre documentación": ¿qué documentación exactamente? ¿Quién se la facilitó?
  · [Objetivo: separar percepción directa de valoración documental]
- ¿Consta en su informe [el extremo X]? [señalar EA folio [N]]
  · Si "no": ¿por qué no formaba parte de su encargo?
  · [Objetivo: acotar — lo que el informe no cubre, no lo prueba]

BLOQUE 2 — PREMISAS (de dónde partió)
- Su informe parte del dato de que [premisa]. ¿De dónde procede ese dato?
  · [Objetivo: si la premisa se la dio la Administración, el informe no la acredita: la asume]
- ¿Qué habría cambiado en su conclusión si [premisa] fuera [alternativa]?
  · [Objetivo: mostrar la dependencia de la conclusión respecto de una premisa discutida]

BLOQUE 3 — MÉTODO
- ¿Qué método o protocolo aplicó? ¿Es el estándar en [ÁMBITO] a [FECHA]?
  · [Sanitario: la lex artis se mide por el estado de los conocimientos de la ciencia o de la
     técnica EN EL MOMENTO (art. 34.1 Ley 40/2015). Anclar la pregunta a la fecha del hecho,
     no a la de hoy]
- [Si hay informe de parte contradictorio] Su informe concluye [X]; el informe de parte concluye
  [Y]. ¿En qué punto concreto divergen los métodos?

BLOQUE 4 — CIRCUNSTANCIAS (material para conclusiones)
- ¿Qué relación tiene usted con [ÓRGANO]? ¿Es personal de la Administración demandada?
- ¿Quién le encargó el informe y en qué momento del procedimiento?
  · ⚠️ ABREVIADO: esto NO es una tacha (art. 78.15). Es material que se explota EN CONCLUSIONES
    como observación sobre sus circunstancias y la veracidad de sus manifestaciones.

MATERIAL DE CONTRADICCIÓN A MANO
- Si afirma [X] → EA folio [N] dice [Y]
- Si niega haber recibido [dato] → EA folio [N] (oficio de remisión)

NOTA — ACLARACIONES AL DICTAMEN (art. 60.6 LJCA)
En el acto de emisión de la prueba pericial, el juez otorgará, A PETICIÓN de cualquiera de las
partes, un plazo NO SUPERIOR A CINCO DÍAS para solicitar aclaraciones al dictamen emitido.
→ PEDIRLO. Es una segunda oportunidad de contradicción que se pierde por no solicitarla.

NOTA — INSACULACIÓN (abreviado)
Art. 78.16: no rigen las reglas generales sobre insaculación de peritos.
```

#### B. TESTIFICAL DEL FUNCIONARIO INTERVINIENTE

Quien instruyó, quien denunció, quien firmó el informe. Preguntas **abiertas**, sobre percepción
directa. El objetivo suele ser el **procedimiento**, no el fondo: qué se hizo, qué no se hizo, qué
se decidió y por qué no consta.

```
TESTIFICAL — [FUNCIONARIO], [cargo] de [ÓRGANO]
Asunto: [slug] · Cauce: [abreviado / ordinario]
Intervención en el expediente: EA folios [rango]
Circunstancias relevantes: [dependencia jerárquica de [ÓRGANO] / instructor del expediente]
  ⚠️ ABREVIADO — NO SE TACHA (art. 78.15). Estas circunstancias se hacen valer EN CONCLUSIONES.

PREGUNTAS (abiertas — que narre)

1. ¿Cuál era su función en el expediente [referencia]?
   [Situar su percepción directa: lo que no hizo él, no lo sabe]

2. El [FECHA] usted firmó [actuación] (EA folio [N]). ¿Puede explicar cómo se practicó?
   [Objetivo: que narre; comparar con lo que el folio documenta]

3. En el escrito de alegaciones (EA folio [N]) esta parte propuso la práctica de [prueba].
   ¿Se practicó? ¿Consta en el expediente la razón de no practicarla?
   [Objetivo: acreditar la omisión → indefensión, art. 48.2 LPAC]
   [Si dice que sí se practicó: pedir el folio. Si no puede señalarlo, el expediente lo desmiente]

4. ¿Recuerda si se le comunicó a [CLIENTE] [trámite]? ¿Por qué medio?
   [Objetivo: notificación — de ella cuelga el dies a quo]

5. [Sancionador] ¿En qué se basó para afirmar [elemento del tipo]? ¿Consta soporte en el
   expediente?
   [Objetivo: presunción de inocencia — si el elemento no está acreditado, la carga es de la
    Administración, no nuestra]

MATERIAL DE CONTRADICCIÓN A MANO
- Si afirma que se practicó [prueba] → EA folios [rango]: no consta
- Si afirma que se notificó el [FECHA] → EA folio [N] (acuse con fecha distinta)

NOTAS TÁCTICAS
- ABREVIADO: sin escritos de preguntas ni repreguntas (78.14). Guion de mano, preguntas verbales.
- ABREVIADO: el juez puede LIMITAR el número de testigos si son reiterativos (78.14).
  → No proponer cinco funcionarios para el mismo extremo. Elegir al que tuvo percepción directa
    y justificar en el otrosí por qué cada uno aporta un punto de hecho DISTINTO.
- Si se deniega la prueba: SÚPLICA EN EL ACTO (art. 78.17) — dejar constancia. Sin protesta no
  hay gravamen que sostener en apelación.
```

#### C. INTERROGATORIO DE PARTE (excepcional)

Solo tras el aviso del § 1. Si el interrogado es **nuestro cliente** a instancia de la
Administración: preparación defensiva — repasar los hechos que constan en el expediente y
advertirle de la **ficta confessio** (LEC 304, supletoria): si no comparece, responde de forma
evasiva o se niega a contestar, el tribunal puede tener por reconocidos los hechos.

> **Abreviado:** las preguntas se proponen **verbalmente, sin pliego** (art. 78.13). No preparar
> pliego articulado.

### 6. Output

`matters/<slug>/prueba-personal/[perito|funcionario]-[rol].md`

Guion + material de contradicción anclado a **folio del expediente** + cronología filtrada +
**apuntes para conclusiones** (en abreviado, el destino de las circunstancias del testigo).

### 7. Decision tree

> 1. **Otrosí de recibimiento a prueba** — art. 60.1 LJCA: **solo por otrosí** en demanda o
>    contestación, con los **puntos de hecho** ordenados y los **medios** propuestos. Si no se pide
>    ahí, no hay prueba.
> 2. **Sancionador** — art. 60.3 LJCA: si el objeto del recurso es una **sanción administrativa o
>    disciplinaria**, el proceso **se recibirá siempre a prueba** cuando exista disconformidad en
>    los hechos. Invocarlo expresamente.
> 3. **Aclaraciones al dictamen** — art. 60.6 LJCA: pedir el plazo (≤ 5 días). Se pierde si no se
>    solicita.
> 4. **Guion de conclusiones** — en abreviado es donde aterrizan las circunstancias del testigo
>    (art. 78.15)

## Reglas

1. **El expediente y la pericial son la prueba reina.** El interrogatorio no. Si el usuario pide
   interrogatorio de la Administración, **avisar de su escasa utilidad** y reorientar a pericial,
   testifical de funcionarios y discusión del expediente.
2. **Determinar el cauce ANTES de escribir una pregunta.** Abreviado y ordinario tienen reglas de
   prueba distintas. En abreviado manda el **art. 78 LJCA**, no la LEC.
3. 🚨 **En abreviado NO HAY TACHAS (art. 78.15 LJCA).** No articular tacha del art. 377 LEC. Las
   circunstancias del testigo se hacen valer **únicamente en conclusiones**, como observaciones
   sobre sus circunstancias personales y la veracidad de sus manifestaciones. Todo guion de
   abreviado debe llevar el apartado de "apuntes para conclusiones".
4. **En abreviado no hay pliegos ni escritos de preguntas** (arts. 78.13 y 78.14). El guion es de
   mano, para preguntar verbalmente. No formatearlo como pliego articulado.
5. **La LEC es supletoria (DF 1.ª LJCA), y hay que decir que lo es.** Interrogatorio LEC 301-316 y
   testigos LEC 360-381 son la base, pero ceden ante la regla propia de la LJCA. Nunca citar la
   LEC como si fuera la norma principal de este orden.
6. **Solo hechos de percepción directa.** Las valoraciones jurídicas son del letrado. A un
   funcionario **no** se le pregunta si el acto era conforme a Derecho: se le pregunta qué hizo,
   qué vio y qué consta.
7. **Todo se ancla al FOLIO del expediente.** El material de contradicción es `EA folio [N]`, no
   "Doc nº X".
8. **Sancionador: la carga es de la Administración.** No construir el interrogatorio para probar
   la inocencia. Construirlo para exhibir que el elemento del tipo **no está acreditado**.
9. **Protesta obligatoria si se deniega la prueba** — súplica en el acto (art. 78.17 LJCA en
   abreviado). Sin constancia no hay gravamen para apelar.
10. **Deontología (art. 11 EGA `[verificar numeración vigente]`)** — no instruir al testigo en
    sentido contrario a la verdad. Ensayar el orden y el alcance, nunca el contenido.
11. **Protección de datos.** `[CLIENTE]`, `[ÓRGANO]`, `[PERITO]`, `[FUNCIONARIO]`, `[FECHA]`,
    `[IMPORTE]`. Cero DNI, nombres, direcciones o teléfonos reales. ⚠️ El expediente contiene datos
    de **terceros** (denunciantes, otros interesados) y datos de **salud** (art. 9 RGPD, categoría
    especial). En sanitario, el guion pericial roza permanentemente la historia clínica:
    **referenciar el folio, nunca transcribir el dato de salud** en el guion.
