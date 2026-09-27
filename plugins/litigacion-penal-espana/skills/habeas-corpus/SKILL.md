---
name: habeas-corpus
description: >-
  Procedimiento de habeas corpus (LO 6/1984 y art. 17.4 CE) — supuestos de detención ilegal (art. 1), legitimación (art. 3, incluido el abogado defensor tras la LO 5/2024), competencia (art. 2), escrito de solicitud (art. 4, sin abogado ni procurador preceptivos), tramitación y resolución en 24 horas (art. 7) y resoluciones posibles (art. 8). Actívala ante "habeas corpus", "detención ilegal", "lleva más de 72 horas detenido", "no lo ponen a disposición judicial", "está detenido y no le dejan ver al abogado", "detención sin motivo". Cauce URGENTE y exclusivo para cuestionar la LEGALIDAD de una privación de libertad todavía en curso y forzar la puesta a disposición judicial o en libertad. No sirve para pedir, oponerse ni recurrir la prisión o la libertad provisional acordadas por el juez (eso es /medidas-cautelares-penales-catalogo), ni sustituye a la asistencia letrada ordinaria en comisaría (/asistencia-detenido).
---

# Habeas corpus — LO 6/1984

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Supuestos, legitimación, competencia y plazo de la LO 6/1984** → `buscar_articulo` (`ley="LO 6/1984"`; si no resuelve, localízala con `buscar_boe` y usa su ID BOE); art. 17 CE con `ley="CE"`.
- **Límites temporales de la detención** → `buscar_articulo` (`ley="LECrim"`, `articulo="520"`).
- **Doctrina constitucional sobre la inadmisión *a limine* del habeas corpus** → `buscar_sentencias` (`base="TC"`) + `leer_sentencias` con `parrafos=3`.
- **Resoluciones que se citen en la solicitud** → `buscar_por_cita`; si el tiempo apremia, presenta sin citas antes que con citas sin verificar.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

> **Fuente:** LO 6/1984 (arts. 1 a 9) y art. 17 CE, **verificados con `buscar_articulo` el
> 2026-07-17**. El art. 3 tiene redacción de la **LO 5/2024** (vigente 4-12-2024).

## 🚨 Esto es cuestión de HORAS

**El habeas corpus solo sirve mientras dura la privación de libertad.** Si el detenido ya está libre o ya fue
puesto a disposición judicial, el procedimiento **pierde su objeto**. **No lo dejes para mañana. No lo "prepares
bien". Preséntalo.**

- **Art. 17.4 CE:** la ley regulará un habeas corpus para producir la **inmediata puesta a disposición judicial**
  de toda persona detenida ilegalmente. **Art. 17.2 CE:** la detención no puede durar más del **tiempo
  estrictamente necesario** y, **en todo caso**, en **72 horas** el detenido debe ser puesto en libertad o a
  disposición judicial.

Llega también por derivación desde `/asistencia-detenido`, cuando el checklist arroja **detención ilegal**.

## 1. Supuestos — art. 1 (verificado)

Objeto: la **inmediata puesta a disposición judicial de cualquier persona detenida ilegalmente**. Lista
**tasada**: encaja tu caso en una letra concreta y **dilo expresamente en el escrito**.

| | Supuesto | Uso práctico |
|---|---|---|
| **a)** | Detenidas por **autoridad, agente, funcionario público o particular**, **sin que concurran los supuestos legales**, o **sin haberse cumplido las formalidades y requisitos** exigidos por las leyes | El más amplio. **Dos causas distintas**: no hay supuesto legal / lo hay pero se incumplieron formalidades. ⭐ Incluye la detención por **PARTICULAR** |
| **b)** | **Ilícitamente internadas** en cualquier establecimiento o lugar | Lugar inadecuado; internamientos no judiciales |
| **c)** | Detenidas **por plazo superior al legal**, si transcurrido no fueren puestas en libertad o **entregadas al Juez más próximo** al lugar de la detención | **Superadas las 72 h** |
| **d)** | Privadas de libertad **a quienes no les sean respetados los derechos** que la Constitución y las leyes procesales garantizan | ⭐ **La más rentable y la más olvidada** |

> **⭐ La letra d) es la puerta de entrada real de la defensa.** **No hace falta que hayan pasado las 72 h: basta
> con que se haya vulnerado un derecho del art. 520.2 LECrim.** Denegación del acceso a los elementos esenciales
> (520.2.d), falta de información de derechos por escrito, retirada de la declaración escrita de derechos,
> negativa a la entrevista reservada previa (520.6.d), falta de intérprete, negativa al forense (520.2.i)..
> **todo eso es habeas corpus.** Cruza el checklist de `/asistencia-detenido` con esta letra.
>
> **⚠️ El «tiempo estrictamente necesario» también.** Una detención prolongada sin practicar diligencia que la
> justifique es ilegal **aunque no se agoten las 72 h**: encaja en la letra a) (ex arts. 17.2 CE y 520.1 LECrim).

## 2. ⛔ Qué NO es — el error más común

> **🚨 EL HABEAS CORPUS NO ES UN RECURSO CONTRA LA PRISIÓN PROVISIONAL ACORDADA JUDICIALMENTE.**
>
> Si un **juez** la acordó por auto, la privación **tiene título judicial habilitante** y no es
> «detención ilegal» del art. 1. Dilo con claridad al cliente y a la familia, que casi siempre lo piden
> así. El cauce es **otro**:
> - **Reforma**: **3 días** (art. 211 LECrim, verificado)
> - **Apelación**: **5 días** (art. 766.3, verificado), **directa, sin reforma previa** (766.2), y **con
>   VISTA** si el auto acuerda prisión provisional (766.5) — **pídela siempre**
> - **Modificación por cambio de circunstancias** (art. 505)
> - **Vencimiento de los plazos máximos** del art. 504 → `/computo-plazos-penal`
>
> Presentarlo contra una prisión provisional judicial es un **billete seguro a la inadmisión**, quema
> credibilidad ante la guardia y **consume el tiempo del recurso que sí procede**.

**Tampoco es:** discutir el **fondo** de la imputación o la suficiencia de indicios · impugnar una **condena**
firme o su ejecución (→ vigilancia penitenciaria) · anticipar el acceso al atestado (eso es el 520.2.d ante el
instructor). **Sí lo es** la privación **gubernativa o de hecho sin título judicial**: detención policial,
detención por particular, internamiento en lugar inadecuado, y siempre los supuestos del art. 1.

## 3. Competencia — art. 2 (verificado)

**Juez de Instrucción**, por este orden: (1) del **lugar en que se encuentre** la persona privada de libertad;
(2) si **no constare**, el del **lugar de la detención**; (3) en defecto, el del lugar de las **últimas
noticias** sobre su paradero. Detención por la ley orgánica del **art. 55.2 CE** → **Juez Central de
Instrucción**. Jurisdicción **militar** → **Juez Togado Militar de Instrucción** de la cabecera de la
circunscripción donde se efectuó la detención.

> **⚠️ Nomenclatura.** La LO 6/1984 **no fue actualizada** por la LO 1/2025 y sigue diciendo «Juez de
> Instrucción»; desde el **3-10-2025** el **órgano** es la **Sección de Instrucción del Tribunal de Instancia**
> (art. 14 LECrim). **En el encabezamiento usa la denominación vigente**; al citar el art. 2 puedes reproducir su
> literalidad. En la práctica: **la Sección de Instrucción en funciones de GUARDIA** del lugar de custodia.

## 4. Legitimación — art. 3 (verificado, redacción LO 5/2024)

| | Legitimado |
|---|---|
| **a)** | El **privado de libertad**; **cónyuge o persona unida por análoga relación de afectividad**; **descendientes, ascendientes, hermanos**; **menores** → sus **representantes legales**; **personas con discapacidad con medidas de apoyo judiciales** → quien preste el apoyo **con facultad de representación específica para este acto concreto** |
| **b)** | El **Ministerio Fiscal** |
| **c)** | El **Defensor del Pueblo** |
| **d)** | ⭐ **El ABOGADO DEFENSOR del privado de libertad** |
| — | **De oficio, el Juez competente** del art. 2 |

> **⭐ NOVEDAD LO 5/2024: la letra d).** El **abogado defensor está hoy legitimado EXPRESAMENTE** —antes se
> discutía y era causa habitual de inadmisión—. **Cita el art. 3.d) en su redacción vigente**: ya no necesitas
> instrumentalizar a un familiar. Todo material anterior a diciembre de 2024 está obsoleto. **⭐ Y el juez puede
> incoarlo DE OFICIO**: argumento para pedir la incoación aunque se discuta tu legitimación.

**Art. 5 (verificado) — obligación de quien custodia:** la autoridad gubernativa, agente o funcionario **deben
poner INMEDIATAMENTE en conocimiento del Juez la solicitud** formulada por quien está bajo su custodia; si lo
incumplen → **apercibimiento judicial** y **responsabilidades penales y disciplinarias**. **⭐ Úsalo:** es
frecuente que en comisaría se disuada al detenido («eso no sirve, ya lo verá el juez») o que la solicitud no
se curse. **Esa conducta es ilícita.** Hazlo constar en acta (520.6.b LECrim), invoca el art. 5 y
**preséntalo tú** al amparo del art. 3.d).

## 5. Procedimiento — arts. 4, 6 y 7 (verificados)

**Iniciación (art. 4):** por **escrito o comparecencia**. **⭐ NO es preceptiva la intervención de Abogado
ni de Procurador** — el detenido o su familia pueden presentarlo solos, incluso verbalmente ante la
guardia. **La falta de postulación no es causa de inadmisión.** Contenido obligatorio: a) **nombre y
circunstancias personales** del solicitante y de la persona para quien se pide; b) **lugar** y **autoridad
o persona bajo cuya custodia** esté, si fueren conocidos; c) **⭐ el MOTIVO CONCRETO**.

> **El apartado c) es donde se pierden los habeas corpus.** «Motivo concreto» = **letra del art. 1
> invocada + hecho que la integra + norma vulnerada**. No basta «detención ilegal». Escribe: *«Art. 1.d):
> no se ha respetado el derecho del art. 520.2.d LECrim, al denegarse el acceso a los elementos
> esenciales, según consta en acta de [HORA]»*.

**Admisión (art. 6):** el Juez examina **los requisitos**, da **traslado al Ministerio Fiscal** y, **por
auto**, acuerda la **incoación** o **deniega por improcedente**. Se notifica **en todo caso** al MF.
**⭐ Contra esa resolución NO CABE RECURSO ALGUNO.**

> **⚠️ La inadmisión a trámite sistemática es un problema real, y el art. 6 lo agrava.** Es habitual que se
> inadmita *a limine* razonando sobre el **fondo** (que la detención fue legal) en vez de sobre los
> **requisitos** — lo que vacía el procedimiento: si la detención fue legal es justo lo que debe decidirse
> **tras** la comparecencia del art. 7, no antes.
>
> **⭐ Hay doctrina consolidada del TC sobre esto y es tu mejor argumento. NO LA CITES DE MEMORIA:
> verifícala con `buscar_sentencias`** (*habeas corpus inadmisión a trámite*, *habeas corpus art. 17.4
> CE*, *inadmisión liminar motivos de fondo*). Cita solo lo que devuelva el conector.
>
> **Operativo:** (1) **anticípate** — que los requisitos del art. 4 sean evidentes y el motivo esté
> encajado en una letra; (2) **separa requisitos y fondo** en el escrito, para que inadmitir obligue a
> razonar el fondo; (3) inadmitido, **no hay recurso**: la vía es el **amparo** — valóralo y adviértelo,
> verificando antes plazos y requisitos.

**Tramitación (art. 7):** en el auto de incoación el Juez ordena que le **pongan de manifiesto** al detenido
**«sin pretexto ni demora alguna»**, o **se constituye en el lugar**. Antes de resolver **oye**: (1) al
**privado de libertad** o su representante legal y **Abogado**; (2) al **Ministerio Fiscal**; (3) **acto
seguido**, a la **autoridad, agentes o persona que ordenó o practicó** la detención y, **en todo caso**, a
**quien la custodia**; y **da a conocer a todos ellos las declaraciones del privado de libertad**. Admite las
pruebas pertinentes y **las que puedan practicarse EN EL ACTO** → **lleva tu prueba contigo y practicable en
el acto**: acta con la incidencia consignada, informe del forense, declaración del detenido.

### ⭐ EL PLAZO — art. 7, párr. 4 (literal verificado)

> **«En el plazo de VEINTICUATRO HORAS, contadas desde que sea dictado el AUTO DE INCOACIÓN, los Jueces
> practicarán todas las actuaciones a que se refiere este artículo y dictarán la resolución que
> proceda.»**

**Precisión que decide casos:** las 24 h corren **desde el auto de incoación**, **no desde la
presentación**. Entre solicitud y auto media el trámite del art. 6, **sin plazo propio en la ley**: es
un espacio real de demora. **Presiona por que se dicte el auto** y deja constancia de la **hora de
presentación**. **Las 72 h del art. 17.2 CE siguen corriendo en paralelo**: el habeas corpus no las
suspende.

## 6. Resoluciones — art. 8 (verificado)

Por **AUTO MOTIVADO**, **una** de estas:

| | Resolución | Contenido |
|---|---|---|
| **8.1** | **Archivo** | No concurre ninguna circunstancia del art. 1 → archivo **declarando conforme a Derecho la privación de libertad y las circunstancias en que se realiza** |
| **8.2.a)** | **⭐ PUESTA EN LIBERTAD** | Si lo fue ilegalmente |
| **8.2.b)** | **Cambio de condiciones** | Que continúe la privación conforme a las disposiciones aplicables pero, si lo considera necesario, **en establecimiento distinto o bajo custodia de personas distintas** |
| **8.2.c)** | **Puesta INMEDIATA a disposición judicial** | Si **ya transcurrió el plazo legal** de detención |

> **⭐ No pidas solo la libertad.** **La letra b) es la gran desconocida**: si el problema es el **trato o el
> lugar** (malos tratos, lugar inadecuado, custodia por los mismos agentes denunciados), lo idóneo es **cambiar
> establecimiento o custodia**, no liberar. **Un suplico que solo pide libertad se desestima entero** cuando
> procedía la b). **Formula petición principal y subsidiarias** cubriendo a), b) y c).

## 7. ⚠️ Art. 9 — el riesgo del solicitante (verificado)

- El Juez **deduce testimonio** para perseguir los delitos que hayan podido cometer quienes ordenaron la
  detención o custodiaron al privado de libertad.
- En **denuncia falsa o simulación de delito**, deduce testimonio igualmente contra el solicitante.
- **⭐ «Si se apreciase TEMERIDAD o MALA FE, será condenado el solicitante al pago de las COSTAS»**; en
  caso contrario, de oficio.

> **Advertencia obligatoria y filtro de la skill:** el habeas corpus **no es gratis en riesgo**. Uno
> manifiestamente improcedente —el ejemplo típico: **contra una prisión provisional judicial** (§ 2)—
> puede acabar en **condena en costas por temeridad**. Presenta cuando haya un motivo del art. 1 real y
> encajable; **no como gesto** ante la familia. Si no procede, **dilo y explica el cauce que sí procede**.

## 8. Salida

### (a) Triaje previo — decide ANTES de redactar

```markdown
| Pregunta | Respuesta | Consecuencia |
|---|---|---|
| ¿Sigue privado de libertad AHORA? | [sí/no] | **NO → no hay habeas corpus** (sin objeto) |
| ¿Hay AUTO JUDICIAL de prisión provisional? | [sí/no] | **SÍ → NO es habeas corpus** → reforma 3 d / apelación 5 d |
| ¿Qué letra del art. 1 se invoca? | [a/b/c/d] | Ninguna encaja → **no presentar** (riesgo art. 9) |
| Hecho concreto que la integra | [hecho + hora + folio/acta] | Es el «motivo concreto» del art. 4.c |
| Norma vulnerada | [520.2.x / 17.2 CE / ...] | — |
| Horas desde la detención | [N] h (límite [FECHA] [HORA]) | ≥ 72 h → art. 1.c |
| Órgano competente (art. 2) | [Sección de Instrucción de guardia de [LUGAR]] | — |
| Legitimación (art. 3) | [d) abogado defensor / a) ...] | — |
```

### (b) Escrito de solicitud

**Breve, telegráfico y verificable — se lee en la guardia, no se estudia.**

1. **Encabezamiento**: A LA SECCIÓN DE INSTRUCCIÓN DEL TRIBUNAL DE INSTANCIA DE [PARTIDO], EN FUNCIONES
   DE GUARDIA (art. 2 LO 6/1984; art. 14 LECrim).
2. **Solicitante y legitimación**: circunstancias personales del solicitante y del privado de libertad
   (**art. 4.a**) + **art. 3.d)** o la letra que proceda; hacer constar que **no es preceptiva la intervención
   de abogado ni procurador (art. 4)**.
3. **HECHOS**, numerados, **cada uno con hora**: detención ([FECHA] [HORA], [COMISARÍA]); autoridad y **lugar**
   de custodia (**art. 4.b**); incidencias **con remisión al acta** (520.6.b LECrim); horas transcurridas.
4. **⭐ MOTIVO CONCRETO (art. 4.c)**: *«Detención ilegal ex art. 1.[letra] LO 6/1984, por [hecho], que vulnera
   el art. [norma]»*. Una letra, un hecho, una norma. **Sin retórica.**
5. **FUNDAMENTOS**: arts. 17.1, 17.2 y 17.4 CE; art. 1.[letra] LO 6/1984; norma vulnerada (art. 520 LECrim).
   **Separar expresamente requisitos (art. 4) y fondo**, para dificultar la inadmisión liminar. Doctrina del TC
   → **`buscar_sentencias` primero**; si no se verifica, **no se cita**. **PRUEBA practicable EN EL ACTO**
   (art. 7): acta de consignación, informe del forense, declaración del detenido, exhibición del atestado.
6. **SUPLICO**: incoación; puesta de manifiesto «sin pretexto ni demora alguna» (art. 7); comparecencia; y
   **principal y subsidiariamente**: a) **libertad** (8.2.a); b) **establecimiento o custodia distintos**
   (8.2.b); c) **puesta inmediata a disposición judicial** (8.2.c).
7. **OTROSÍ** si procede: deducción de testimonio (art. 9); **constancia de la HORA de presentación**. Cierra con
   lugar, **fecha y HORA**, y firma.

> **¿Qué hago ahora?**
> 1. **Preséntalo YA** si hay motivo del art. 1 — el objeto se pierde con la libertad
> 2. **Auto judicial de prisión** → **NO es esta skill**: reforma (3 d, art. 211) o apelación (5 d,
>    art. 766.3, con vista ex 766.5) → `/medidas-cautelares-penales-catalogo` y `/computo-plazos-penal`
> 3. Detención en curso con derechos vulnerados → `/asistencia-detenido` (el acta **es la prueba**)
> 4. **Inadmitido** → no cabe recurso (art. 6): valorar **amparo**; verificar plazos y doctrina del TC
> 5. Tras la resolución → `/cronologia` (detención y habeas corpus son hitos del carril procesal)

## Reglas

1. **Verificar antes de afirmar.** La LO 6/1984 está verificada aquí (2026-07-17). Lo demás →
   `buscar_articulo`; lo no verificable → `[verificar]`. **Prohibido citar jurisprudencia de memoria**
   (ECLI, ROJ, fecha, ponente): la doctrina del TC **se verifica con `buscar_sentencias`** o **no se cita**.
2. **Honestidad con el cliente.** Si no procede, **decirlo** y ofrecer el cauce correcto: el art. 9 hace
   que el habeas corpus de gesto tenga coste real.
3. **Encaje obligatorio en una letra del art. 1.** Sin letra + hecho + norma vulnerada, no se redacta.
4. **Nomenclatura (LO 1/2025, desde 3-10-2025):** órgano = **Sección de Instrucción del Tribunal de
   Instancia** (art. 14 LECrim) en los encabezamientos, aunque la LO 6/1984 siga diciendo «Juez de
   Instrucción».
5. **Protección de datos.** `[DETENIDO]`, `[INVESTIGADO]`, `[COMISARÍA]`, `[FECHA]`, `[HORA]`, `[LUGAR]`.
   **Cero datos reales.** Infracciones y condenas = **categoría especial (art. 10 RGPD)**. **Perfil:**
   `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md`.

## ⛔ Fuera de esta skill

- **El habeas corpus contra la prisión provisional judicial** (§ 2). El error más común.
- **El «fiscal instructor». NO EXISTE.** El habeas corpus lo conoce el **juez de instrucción** (art. 2);
  el MF es **oído** (arts. 6 y 7) y está **legitimado** (art. 3.b), pero **no instruye ni resuelve**. La
  reforma que atribuiría la instrucción al MF está **en tramitación** (prevista 1-1-2028): **no se menciona
  como Derecho vigente**, ni se cita «art. 4 bis EOMF». **MASC y burofax:** orden **civil**, no existen aquí.
