---
name: preparacion-interrogatorio
description: Preparacion del interrogatorio en el juicio oral penal. El acusado NO es testigo — tiene derecho a guardar silencio y no hay ficta confessio (arts. 24.2 CE, 118 y 520.2 LECrim). Interrogatorio del acusado o su silencio estrategico, contradiccion de testigos con la declaracion sumarial (art. 714 LECrim) anclada al folio, contradiccion del perito, y victima como testigo con su estatuto (Ley 4/2015). Usar con preparar interrogatorio, guion para el juicio oral penal.
---

# Preparación del interrogatorio — juicio oral penal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen de cada interrogado** (arts. 118, 410, 416, 701, 714 y 730 LECrim) → `buscar_articulo` (`ley="LECrim"`).
- **Protección de la víctima-testigo** → `buscar_articulo` con el Estatuto de la víctima por su ID `BOE-A-2015-4606`.
- **Doctrina sobre las contradicciones del art. 714 y la declaración de la víctima como prueba de cargo** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.
- **Dispensa del art. 416 tras la LO 8/2021** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`, `fecha_desde="25/06/2021"`).
- **Derecho a no declarar y presunción de inocencia** → `buscar_sentencias` (`base="TC"`).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

> **Fuente de cifras:** `references/anclas-normativas-penal.md`. Verificado contra el BOE.

## Cuándo activar

- "Preparar interrogatorio de [ACUSADO] / [TESTIGO] / [perito]"
- "Guion para el juicio"
- "¿Declara o se acoge al silencio?" ← **la decisión más importante de la defensa**
- Antes de la **audiencia preliminar del art. 785** (se decide la prueba)
- Antes del juicio oral

---

## 🚨 REGLA CARDINAL — EL ACUSADO NO ES UN TESTIGO

**Esta skill procede de un plugin civil y el texto anterior afirmaba lo contrario. Se corrige aquí de
forma expresa porque la contradicción es grave y produciría un daño real al cliente.**

| ❌ FALSO (régimen civil — **NO aplicar en penal**) | ✅ VERDADERO (régimen penal, verificado) |
|---|---|
| «La parte debe responder; si no responde o lo hace evasivamente, **ficta confessio** (LEC 304)» | **El acusado NO tiene obligación de declarar.** Tiene derecho a **guardar silencio**, a **no declarar contra sí mismo** y a **no confesarse culpable** — **art. 24.2 CE**, **art. 118.1.g) y h) LECrim**, **art. 520.2.a) y b) LECrim** |
| El silencio de la parte puede tenerse por reconocimiento de los hechos | **NO EXISTE LA FICTA CONFESSIO EN EL PROCESO PENAL.** El silencio del acusado **no puede valorarse como confesión** ni como indicio de culpabilidad. La carga de la prueba es **íntegramente de la acusación** (presunción de inocencia, art. 24.2 CE) |
| Preguntas articuladas asertivas que la parte debe contestar | El acusado **puede negarse a contestar a alguna o algunas de las preguntas** que se le formulen (**art. 118.1.g) LECrim**, literal verificado) — p. ej. contestar solo a su defensa |

**Texto literal verificado — art. 118.1 LECrim:**
- g) «Derecho a **guardar silencio y a no prestar declaración si no desea hacerlo**, y a **no
  contestar a alguna o algunas de las preguntas** que se le formulen.»
- h) «Derecho a **no declarar contra sí mismo y a no confesarse culpable**.»

**Texto literal verificado — art. 24.2 CE:** «...a **no declarar contra sí mismos**, a **no
confesarse culpables** y a la **presunción de inocencia**.»

> **⚠️ Matiz que hay que conocer y que NO contradice lo anterior:** el silencio no es prueba de
> cargo ni puede sustituirla. La discusión sobre si un silencio ante un cuadro probatorio ya cerrado
> puede tener algún alcance valorativo es **jurisprudencial y matizada**: **verificar con
> `buscar_sentencias` antes de fundar cualquier estrategia en ello**. La regla de partida no se
> toca: **silencio ≠ confesión**.

### 🚨 TAMPOCO EXISTEN LAS TACHAS DE TESTIGOS DEL ART. 377 LEC

**Las tachas son una institución del proceso civil. En el proceso penal no existen.** El testigo
penal **declara**, y su credibilidad **se combate en el informe final** valorando su declaración —
no mediante un incidente previo de tacha.

**Régimen penal de testigos, verificado:**

- **Art. 410 LECrim (verificado):** «Todos los que residan en territorio español, nacionales o
  extranjeros, que no estén impedidos, tendrán **obligación de concurrir al llamamiento judicial
  para declarar** cuanto supieren sobre lo que les fuere preguntado.»
- **Art. 707 LECrim (verificado):** «Todos los testigos están **obligados a declarar** lo que
  supieren sobre lo que les fuere preguntado, **con excepción de las personas expresadas en los
  artículos 416, 417 y 418**.»
- **⭐ Art. 416 LECrim — DISPENSA del deber de declarar (verificado). Esto sí existe en penal, y es
  lo que hay que dominar:**
  1. **Parientes** del procesado en **línea directa ascendente y descendente**, **cónyuge o persona
     unida por relación de hecho análoga a la matrimonial**, **hermanos** consanguíneos o uterinos y
     **colaterales consanguíneos hasta el segundo grado civil**. El juez **debe advertir** al
     testigo de que no tiene obligación de declarar en contra del procesado, y **se consigna en acta
     su contestación a la advertencia**.
     **⚠️ Excepciones — NO hay dispensa cuando:**
     - 1.º el testigo tenga **representación legal o guarda de hecho** de la víctima menor de edad o
       con discapacidad necesitada de especial protección;
     - 2.º se trate de **delito grave**, el testigo sea **mayor de edad** y la víctima sea **menor de
       edad o persona con discapacidad** necesitada de especial protección;
     - 3.º por razón de edad o discapacidad el testigo **no pueda comprender el sentido de la
       dispensa**;
     - 4.º **el testigo esté o haya estado personado como acusación particular**;
     - 5.º **el testigo haya aceptado declarar durante el procedimiento** tras ser debidamente
       informado de su derecho a no hacerlo.
  2. **El abogado del procesado**, respecto de los hechos que este le hubiese confiado como defensor.
  3. **Traductores e intérpretes** de esas comunicaciones.
  - Si el testigo está en esa relación con **uno** de varios procesados, **está obligado a declarar
    respecto de los demás**, salvo que su declaración pudiera comprometer a su pariente o defendido.
- **Arts. 417 y 418 LECrim** — otras excepciones (*verificar contenido antes de invocarlas*).

> **Operativo:** la falta de advertencia del art. 416 al testigo dispensado es un **defecto de la
> declaración** con consecuencias. Comprobar **en el folio** que la advertencia se hizo y que consta
> la contestación. Y comprobar si concurre la **excepción 4.ª o 5.ª**, que neutralizan la dispensa.

---

## Sujetos del interrogatorio penal

| Sujeto | Régimen |
|---|---|
| **ACUSADO** | Derecho al silencio. **No presta juramento ni promesa.** No hay ficta confessio. Puede contestar solo a su defensa |
| **TESTIGO** | **Obligado** a declarar (arts. 410, 707), **salvo dispensa del art. 416**. Presta juramento o promesa. Falso testimonio: arts. 458 y ss. CP (*verificar*) |
| **VÍCTIMA-TESTIGO** | Testigo + **estatuto de la Ley 4/2015**. Suele ser la única prueba de cargo en delitos sin testigos |
| **PERITO** | Declara sobre su dictamen. Se combate su **método**, no su persona |
| **TESTIGO-PERITO** | Percibió los hechos **y** tiene conocimientos técnicos (p. ej. el médico que atendió a la víctima). Régimen mixto — *verificar el encaje concreto antes de proponerlo* |

## Orden de la prueba — art. 701 LECrim (verificado, redacción LO 1/2025)

- La prueba se practica empezando por la del **Ministerio Fiscal**, siguiendo con la de **los demás
  actores** y **por último la de los procesados**. Dentro de cada parte, según el orden propuesto en
  su escrito; los testigos, por el orden de las listas.
- **⭐ NOVEDAD LO 1/2025 — el acusado puede declarar EN ÚLTIMO LUGAR:** «si **a propuesta de su
  defensa** el acusado solicitara declarar **en último lugar**, el Presidente **así lo acordará
  expresamente**». El Presidente puede alterar el orden de oficio o a instancia de parte «**sin
  revocar el derecho del acusado a testificar en último lugar**».
  > **Operativo: es una decisión táctica de primer orden.** Declarar al final permite al acusado
  > pronunciarse **después** de haber oído toda la prueba de cargo. **Pedirlo expresamente y que
  > conste.**
- **Art. 688 LECrim (verificado, LO 1/2025):** abierta la sesión, el Presidente pregunta a cada
  acusado **si se confiesa reo** del delito imputado en el escrito de calificación y responsable
  civil. → Preparar la respuesta con el cliente **antes** del juicio.

---

## Flujo

### 1. Identificar al interrogado y su régimen

- ¿**Acusado** (¿el nuestro u otro coacusado?), **testigo**, **víctima**, **perito**?
- ¿**De cargo o de descargo**?
- **Si es testigo: ¿concurre la dispensa del art. 416?** ¿Alguna de sus cinco excepciones?

### 2. Cargar fuentes

- `matters/<slug>/matter.md` (tesis y calificación)
- `matters/<slug>/cronologia.md` (hitos con folio)
- `matters/<slug>/cuadro-elementos.md` (**qué elemento del tipo se juega en esta declaración**)
- **Todas las declaraciones sumariales del interrogado, por folio** ← materia prima del art. 714
- El atestado (declaraciones policiales) y los dictámenes periciales

### 3. Filtrar la cronología al interrogado

Solo hechos dentro de su **percepción directa**. El testigo declara sobre **lo que supiere** de lo
que se le pregunte (arts. 410, 707): **el testigo de referencia y las valoraciones no son objeto de
la testifical**.

### 4. Fijar el objetivo — anclado al cuadro de subsunción

Todo interrogatorio sirve a **un elemento concreto del tipo**. Si no se sabe a cuál, no se hace.

- **Derribar un elemento** (defensa): que el testigo admita el hecho que impide la subsunción
- **Acreditar un elemento** (acusación)
- **Destruir credibilidad** (defensa): **contradicción con el folio** vía art. 714
- **Construir una atenuante**: reparación (21.5ª), dilaciones (21.6ª)

---

## 5. Guiones

### A) ACUSADO — decisión previa: DECLARAR o SILENCIO

**Se decide con el cliente, se documenta, y se decide antes del juicio.**

```
DECISIÓN SOBRE LA DECLARACIÓN — [ACUSADO]
Procedimiento: [tipo y nº] · Órgano: [ÓRGANO]
Acusación: [tipo penal y pena solicitada por cada acusación]

MATRIZ DE DECISIÓN

A FAVOR DE DECLARAR:
- [ ] Hay una versión exculpatoria coherente y sostenible bajo interrogatorio cruzado
- [ ] Hay un elemento subjetivo (dolo, ánimo de lucro) que solo él puede explicar
- [ ] Se construye una atenuante que exige su intervención (21.5ª reparación)
- [ ] Ya declaró en instrucción y el silencio ahora crearía un contraste desfavorable
      → si declaró antes, valorar art. 714: la acusación pedirá la lectura

A FAVOR DEL SILENCIO:
- [ ] La acusación NO ha acreditado algún elemento del tipo → el cuadro ya se sostiene solo
      (🔴 en `/cuadro-elementos`) y declarar solo puede aportarle a la acusación lo que le falta
- [ ] Sus declaraciones sumariales son contradictorias entre sí → el 714 se volvería en su contra
- [ ] No resiste el interrogatorio cruzado
- [ ] Hay riesgo de autoincriminación en otra causa

DECISIÓN: [ DECLARA / SILENCIO / DECLARA SOLO A PREGUNTAS DE SU DEFENSA (art. 118.1.g) ]

ADVERTENCIAS DOCUMENTADAS AL CLIENTE:
- Su silencio NO puede valorarse como confesión (arts. 24.2 CE, 118 LECrim). La carga de la
  prueba es de la acusación.
- Puede negarse a contestar a alguna o algunas preguntas (art. 118.1.g).
- No presta juramento ni promesa: no comete falso testimonio.
- Puede solicitar declarar EN ÚLTIMO LUGAR (art. 701 LECrim, redacción LO 1/2025) —
  se pedirá expresamente.
- Al inicio se le preguntará si se confiesa reo (art. 688 LECrim). Respuesta acordada: [...]
```

**Si declara — guion:**

```
INTERROGATORIO DEL ACUSADO — [ACUSADO]
Objetivo por elemento del tipo: [remitir a /cuadro-elementos]
Orden solicitado: ÚLTIMO LUGAR (art. 701 LECrim)

PREGUNTAS DE LA DEFENSA (abiertas — que narre; no se le sugiere la respuesta)

1. ¿Qué relación tenía usted con [VÍCTIMA] en [FECHA]?
   [Elemento: relaciones entre defraudador y perjudicado — art. 248 párr. 2]

2. Cuando usted [conducta] el [FECHA], ¿cuál era su intención respecto de [X]?
   [Elemento: DOLO ANTECEDENTE — el núcleo. Que explique la voluntad real de cumplir]
   [Soporte documental: f. [N]]

3. ¿Qué hizo usted con [objeto/fondos]?
   [Elemento: ánimo de lucro]

ANTICIPACIÓN DEL INTERROGATORIO DE LA ACUSACIÓN
- Le preguntarán por [punto débil] → f. [N]. Preparado: [...]
- ⚠️ Si contradice su declaración sumarial de f. [N], pedirán la lectura (art. 714).
  Repasar esa declaración con él ANTES del juicio, folio a folio.
```

### B) TESTIGO — la herramienta es el ART. 714 LECrim

**Art. 714 LECrim, texto literal verificado:**

> «Cuando la declaración del testigo en el juicio oral **no sea conforme en lo sustancial** con la
> prestada en el sumario, **podrá pedirse la lectura de ésta por cualquiera de las partes**.
> Después de leída, el presidente **invitará al testigo a que explique la diferencia o
> contradicción** que entre sus declaraciones se observe.»

**Cómo se usa — la secuencia, en este orden exacto:**

1. **Fijar la versión de hoy.** Preguntar en juicio hasta que el testigo se comprometa con una
   afirmación clara. **No advertirle de la contradicción todavía.**
2. **Cerrar las salidas.** «¿Está usted seguro?» «¿Lo recuerda con claridad?» — para que no pueda
   luego refugiarse en el olvido.
3. **Pedir la lectura del art. 714**, identificando **el folio exacto**: «Interesa esta parte, al
   amparo del art. 714 LECrim, la lectura de la declaración obrante **al folio [N]**, líneas
   [X]-[Y]».
4. **Dejar que el presidente le invite a explicar la contradicción.** La explicación —o su ausencia—
   es lo que queda en el acta y lo que se explota en el informe.
5. **No discutir con el testigo.** La contradicción ya está en el acta. **El combate a la
   credibilidad se hace en el INFORME FINAL**, no en el interrogatorio: no hay tachas.

**Requisito operativo:** el art. 714 exige **tener localizado el folio y la línea antes del juicio**.
Sin la tabla previa, la contradicción se pierde.

```
INTERROGATORIO DE TESTIGO — [TESTIGO]
Relación con las partes: [...]
⚠️ ¿DISPENSA DEL ART. 416 LECrim? [ NO / SÍ — vínculo: [...] ]
   Si SÍ → ¿concurre excepción? [ 4.ª ¿está o estuvo personado como acusación particular? /
   5.ª ¿aceptó declarar en instrucción tras ser informado? — comprobar en f. [N] ]
   Si SÍ y sin excepción → puede no declarar. Comprobar que se le advirtió y que consta
   la contestación en f. [N].
Elemento del tipo en juego: [...]

PREGUNTAS (abiertas — que narre; sin sugerir la respuesta)

1. ¿Dónde se encontraba usted el [FECHA]?
2. ¿Qué vio exactamente? [percepción directa — no referencias ni valoraciones]
3. [Pregunta que fija la versión sobre el punto contradictorio]

🎯 TABLA DE CONTRADICCIÓN — ART. 714 LECrim

| Punto | Dijo en instrucción | Folio y línea | Si hoy dice otra cosa |
|---|---|---|---|
| [Hora del hecho] | «[cita literal]» | **f. [N], l. [X]-[Y]** | Pedir lectura art. 714 |
| [Identificación] | «[cita literal]» | **f. [N], l. [X]-[Y]** | Pedir lectura art. 714 |

NOTAS PARA EL INFORME FINAL (aquí es donde se combate la credibilidad)
- Contradicción sobre [punto]: f. [N] vs. declaración en juicio. Explicación dada: [...]
- Interés en el resultado: [...]  ← argumento de valoración, NO tacha
```

### C) PERITO — se combate el MÉTODO

```
INTERROGATORIO DEL PERITO — [perito de [parte]]
Dictamen: f. [N]-[N] · Objeto: [...]
Elemento del tipo que sostiene: [...]

LÍNEAS DE CONTRADICCIÓN (por orden de rendimiento)

1. MATERIAL EXAMINADO — ¿sobre qué trabajó realmente?
   «¿Examinó usted personalmente [objeto], o trabajó sobre [copia/fotografía/documentación]?»
   [Si no examinó el original: el dictamen pierde base]

2. CADENA DE CUSTODIA — ¿el material es el intervenido?
   «¿Cómo le llegó la muestra? ¿Consta el precinto? ¿Qué número de referencia?» → f. [N]
   [Enlaza con Fila 0.3 — art. 11.1 LOPJ]

3. MÉTODO — ¿es el estándar? ¿validado? ¿margen de error?
   «¿Qué protocolo aplicó? ¿Cuál es el margen de error de esa técnica?»

4. PREMISAS DE HECHO — ¿de dónde salen?
   «El dictamen parte de que [premisa]. ¿Le fue facilitada, o la comprobó usted?»
   [⭐ La más rentable: si la premisa fáctica se cae, el dictamen se cae, por bueno que sea el
    método. El perito no prueba los hechos de los que parte]

5. ALCANCE — ¿qué NO dice el dictamen?
   «¿Su dictamen permite afirmar [X]?» [Que reconozca los límites de su propia conclusión]

⚠️ NO discutir de técnica con el perito en su terreno. Se le lleva a los límites del dictamen,
   a sus premisas y a lo que no comprobó.
```

### D) VÍCTIMA-TESTIGO — estatuto y protección

**En muchos delitos la declaración de la víctima es la única prueba de cargo.** De ahí que su
interrogatorio sea el más delicado del proceso: técnicamente y deontológicamente.

**Régimen de protección verificado:**

- **Art. 707 LECrim (verificado):** cuando deba intervenir en el juicio una **persona menor de 18
  años** o una **persona con discapacidad necesitada de especial protección**, su declaración se
  practica **evitando la confrontación visual con la persona inculpada**, cuando resulte necesario
  para impedir o reducir los perjuicios derivados del proceso. **Puede usarse cualquier medio
  técnico**, incluida la posibilidad de que **sean oídos sin estar presentes en la sala** mediante
  tecnologías de la comunicación accesible. **Estas medidas se aplican igualmente a las víctimas**
  cuando de su evaluación inicial o posterior derive la necesidad de tales medidas de protección.
- **Art. 449 bis LECrim (verificado) — prueba preconstituida:** la autoridad judicial **garantiza el
  principio de contradicción**; la ausencia de la persona investigada debidamente citada no impide
  la práctica, **pero su defensa letrada debe estar presente en todo caso**; se documenta en
  **soporte audiovisual** con comprobación inmediata de la calidad por el LAJ y acta sucinta.
- **Art. 730.2 LECrim (verificado):** a instancia de parte, **se puede reproducir en juicio la
  grabación audiovisual de la declaración de la víctima o testigo practicada como prueba
  preconstituida** conforme al art. 449 bis.
- **Art. 730.1 LECrim (verificado):** pueden leerse o reproducirse las diligencias sumariales que,
  **por causas independientes de la voluntad de las partes**, no puedan reproducirse en el juicio.
  > ⚠️ **Distinguir 714 de 730.** **714** = el testigo **declara** y se contradice → lectura para
  > que explique. **730** = el testigo **no declara** (irreproducible) → lectura como prueba. Son
  > cosas distintas y confundirlas es un error de recurso.
- **Ley 4/2015, Estatuto de la víctima** — derechos de información, protección, evaluación
  individual de necesidades y medidas de protección. *Verificar el articulado concreto con
  `buscar_articulo` antes de invocar un derecho específico.*
- **Art. 785.4 párr. 2 LECrim** — antes de una conformidad, el **Ministerio Fiscal oirá previamente
  a la víctima o perjudicado**, aunque no estén personados, **siempre** que esté en situación de
  **especial vulnerabilidad**.

```
INTERROGATORIO DE LA VÍCTIMA — [VÍCTIMA]
⚠️ ¿Menor / persona con discapacidad necesitada de especial protección / víctima vulnerable?
   → art. 707: evitación de confrontación visual + declaración por videoconferencia
   → ¿hay prueba preconstituida del art. 449 bis? → f. [N] — si la hay, art. 730.2
⚠️ ¿Concurre la dispensa del art. 416? (violencia de género/doméstica: comprobar SIEMPRE,
   y comprobar las excepciones 4.ª y 5.ª)

ENFOQUE
- Objetivo: [elemento del tipo]
- Tono: sobrio. Nunca hostil ni revictimizador — es contraproducente ante el tribunal
  además de deontológicamente inadmisible.
- La credibilidad NO se ataca con la persona: se contrasta con el FOLIO (art. 714) y con
  los datos objetivos (partes médicos, geolocalización, testigos).

TABLA DE CONTRADICCIÓN — art. 714 LECrim
| Punto | Declaración sumarial | Folio | Dato objetivo que la contrasta |
|---|---|---|---|
| [...] | «[cita]» | f. [N] | [parte médico f. [N] / mensajes f. [N]] |
```

### 6. Output

`matters/<slug>/interrogatorios/[rol-anonimizado].md` — guion + tabla de contradicción del art. 714
con folios + decisión documentada sobre el silencio (si es el acusado).

### 7. Decision tree

> 1. **Acusado** — decidir declarar/silencio **con el cliente y documentarlo**; si declara, pedir
>    **el último lugar** (art. 701)
> 2. **Testigos** — comprobar **dispensa del art. 416** y construir la **tabla del art. 714** con
>    folios
> 3. **Peritos** — atacar **premisas y cadena de custodia** antes que el método
> 4. **Víctima** — comprobar medidas de protección (art. 707) y prueba preconstituida (449 bis/730.2)
> 5. **Llevar las nulidades a la audiencia preliminar** (art. 785), no al inicio del juicio
> 6. **Preparar el INFORME FINAL** — donde se valora la credibilidad

## Reglas

1. **El acusado no es testigo.** Silencio (arts. 24.2 CE, 118.1.g y h, 520.2 LECrim). **No hay ficta
   confessio.** No presta juramento. Puede no contestar a alguna o algunas preguntas.
2. **No existen las tachas del art. 377 LEC.** La credibilidad se combate **en el informe final**.
3. **Art. 714 = folio + línea.** Sin la referencia exacta preparada de antemano, no hay
   contradicción posible. **Es la herramienta central del interrogatorio penal.**
4. **No confundir 714 con 730.** Contradicción vs. irreproducibilidad.
5. **Comprobar SIEMPRE la dispensa del art. 416** y sus cinco excepciones antes de contar con un
   testigo pariente.
6. **Cada pregunta sirve a un elemento del tipo.** Si no consta a cuál, se elimina.
7. **Testigo = percepción directa.** Ni valoraciones ni referencias.
8. **Deontología.** No instruir a nadie para declarar en sentido contrario a la verdad. Preparar a un
   testigo sobre el procedimiento y repasar con él lo que ya declaró es legítimo; sugerirle el
   contenido de su respuesta, no.
9. **Verificar antes de afirmar.** Los artículos de esta skill están verificados contra el BOE el
   2026-07-17. Lo que no lo esté va marcado `[verificar]`. **⛔ Prohibido citar jurisprudencia
   concreta** (ECLI/ROJ/fecha) sin `buscar_sentencias` / `buscar_por_cita`.
10. **Protección de datos.** `[ACUSADO]`, `[VÍCTIMA]`, `[TESTIGO]`, `[ÓRGANO]`, `[FECHA]`. **Cero
    datos reales.** Infracciones y condenas = **art. 10 RGPD**. **Cuidado extremo con víctimas
    menores y delitos contra la libertad sexual**: el nombre de archivo del guion no revela rol ni
    identidad.

## ⛔ Fuera de esta skill

- **LEC 301-316** (interrogatorio de parte), **LEC 360-381** (testigos), **LEC 304** (ficta
  confessio), **LEC 377** (tachas). **Todo el régimen civil está fuera y su aplicación en penal
  sería un error grave.**
- **Burofax, MASC, documentos «Doc. nº X».** En penal se cita el **folio de las actuaciones**.
- **El «fiscal instructor».** Instruye el **Juez de Instrucción**.
