---
name: admisibilidad-ca
description: >-
  Checklist de DIAGNÓSTICO previo (art. 69 LJCA) que debe correrse ANTES de redactar cualquier escrito, administrativo o judicial. Comprueba jurisdicción, legitimación, acto impugnable, agotamiento de la vía, documentos del art. 45.2, competencia objetiva y plazo. Activar con "¿es recurrible esto?", "¿puedo recurrir?", "¿me lo van a inadmitir?", "control de admisibilidad", "¿esto agota la vía administrativa?", "¿recurro en alzada o voy directo al contencioso?", "acto de trámite", "acto confirmatorio", "acto firme y consentido", "legitimación", "acuerdo corporativo", "¿qué juzgado es competente?", "antes de redactar la demanda". No redacta escritos: solo decide. Si el resultado es que falta agotar la vía administrativa, el escrito lo redacta /recurso-alzada-reposicion-ca; si la vía ya está agotada, se pasa a /interposicion-recurso-contencioso-ca.
---

# Control de admisibilidad — art. 69 LJCA

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Jurisdicción, acto impugnable, causas del art. 69 y competencia objetiva** → `buscar_articulo` (`ley="LJCA"`, artículos 1 a 3, 8 a 14, 19, 25, 45 y 69).
- **Agotamiento de la vía y trampas de la reposición y del reglamento** → `buscar_articulo` (`ley="LPAC"`, artículos 112, 114 y 123).
- **Doctrina del acto confirmatorio, del interés legítimo y de la desviación procesal** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3` y `terminos` del punto que se discute).
- **Acuerdo corporativo del art. 45.2.d) cuando recurre una sociedad** → `buscar_empresa_mercantil` (denominación o CIF) para ver el órgano de administración y los apoderados inscritos; los estatutos y la certificación del acuerdo se piden al cliente.
- **Acto dictado en aplicación de una ordenanza** (recurso indirecto del art. 112.3 LPAC) → `buscar_ordenanzas` + `leer_ordenanza` con `articulo`, para identificar la disposición aplicada y su órgano autor.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

---

**En lo contencioso se pierden más asuntos por inadmisión que por el fondo.** El mejor recurso del
mundo se archiva si la sociedad recurrente no aportó el acuerdo del órgano competente para litigar.
Esta skill se corre **antes** de redactar nada: interposición, demanda, apelación o casación.

## Cuándo activar

- Antes de cualquier escrito inicial. **Siempre.** Aunque el usuario solo pida "redáctame la demanda".
- En el intake del asunto (`/asunto-intake`) y en toda re-evaluación de estrategia.
- Cuando el usuario pregunta si algo es recurrible, o cuando duda de la vía.
- Cuando el acto impugnado es de **trámite**, **confirmatorio** o de fecha antigua.
- Cuando el recurrente es **persona jurídica**, **sindicato**, **asociación** o **comunidad**.
- Al recibir alegación de inadmisibilidad de la Administración demandada.

## Flujo — las siete comprobaciones

Correr **todas**, en este orden, y no saltar ninguna por obvia. Cada una devuelve 🔴 / ⚠️ / ✅.

### 1. 🔴 PLAZO — art. 69.e LJCA

**La primera, porque es la irreparable.** «Que se hubiera presentado el escrito inicial del recurso
fuera del plazo establecido» (verificado). Delegar el cálculo íntegro en **`/computo-plazos-ca`** —
no calcular aquí. Recordar: es **caducidad**, no se interrumpe por burofax ni reclamación
extrajudicial. Si 🔴 → **parar y avisar antes de redactar nada**.

### 2. Jurisdicción — art. 69.a LJCA

«Que el Juzgado o Tribunal Contencioso-administrativo carezca de jurisdicción» (verificado).
Comprobar que la pretensión no es en realidad civil, social o penal. Casos fronterizos que hay que
mirar dos veces: responsabilidad patrimonial sanitaria con aseguradora codemandada; contratos
privados de la Administración; personal **laboral** al servicio de las AAPP (→ orden social);
Seguridad Social (prestaciones → social; actas de liquidación → contencioso). Ante duda, verificar
con `buscar_articulo("LJCA","1")` a `("LJCA","3")` y advertir del riesgo de declinatoria.

### 3. Acto impugnable — art. 25 LJCA y art. 69.c LJCA

**Art. 25 LJCA (verificado, literal):** el recurso es admisible frente a:
- **Disposiciones de carácter general.**
- **Actos expresos y presuntos** que **pongan fin a la vía administrativa**, ya sean **definitivos**
  o **de trámite**, si estos últimos:
  - **deciden directa o indirectamente el fondo** del asunto,
  - **determinan la imposibilidad de continuar** el procedimiento,
  - **producen indefensión** o
  - **perjuicio irreparable** a derechos o intereses legítimos.
  → Son los **actos de trámite cualificados**. Fuera de esos cuatro supuestos, **el acto de trámite
  no es recurrible**: se impugna al recurrir la resolución final (art. 112.1 LPAC). Intentar
  recurrir un trámite simple es inadmisión segura (art. 69.c).
- **Inactividad** de la Administración (art. 29) y **vía de hecho** (art. 30) — art. 25.2.

**⚠️ Trampa del acto CONFIRMATORIO.** Si se dejó pasar el plazo contra el acto originario y después
se pide de nuevo lo mismo para provocar una segunda resolución, esa segunda resolución es un **acto
confirmatorio** de uno **firme y consentido**: impugnarla en lugar del originario es **causa de
inadmisión** (art. 69.c — «actuaciones no susceptibles de impugnación»). No se puede reabrir por
esta vía un plazo perdido. **Detectarlo así:** ¿existe un acto anterior de idéntico contenido?
¿se recurrió en plazo? ¿la nueva resolución aporta algún elemento nuevo, o se limita a reiterar?
Si solo reitera → 🔴. Solo salvan: (i) que el segundo acto resuelva sobre **hechos o fundamentos
nuevos**, (ii) que el primero fuera **nulo de pleno derecho** (art. 47.1 LPAC → vía del art. 106
LPAC), o (iii) que el primero **no se notificara válidamente**. El alcance concreto del acto
confirmatorio es doctrina jurisprudencial: **verificarla con `buscar_sentencias`, nunca citarla de
memoria.**

**⚠️ Acto FIRME Y CONSENTIDO.** El no recurrido en plazo. Comprobar siempre si el acto que se quiere
atacar trae causa de otro anterior consentido (típico: se impugna la providencia de apremio para
discutir la liquidación que se dejó firme; se recurre la licencia para discutir el planeamiento
consentido). Contra un acto de aplicación **no** se puede discutir lo que quedó firme, salvo los
motivos tasados que permita la norma sectorial. Verificar la norma sectorial antes de afirmar nada.

### 4. Agotamiento de la vía administrativa

El equivalente funcional del MASC civil en este orden — **y no hay MASC aquí**. Si el acto **no**
agota la vía, el contencioso es **prematuro** y se inadmite: falta la **alzada**, que es
**preceptiva**.

**Verificar SIEMPRE con `buscar_articulo("LPAC","114")` antes de afirmar.** Ponen fin a la vía
administrativa (art. 114.1, verificado):
- a) Las **resoluciones de los recursos de alzada**.
- b) Las resoluciones de los procedimientos sustitutivos del art. 112.2.
- c) Las resoluciones de **órganos que carezcan de superior jerárquico**, salvo que una Ley diga
  otra cosa.
- d) Los acuerdos, pactos, convenios o contratos finalizadores del procedimiento.
- e) La **resolución de los procedimientos de responsabilidad patrimonial**, cualquiera que sea el
  tipo de relación de que derive.
- f) La resolución de los procedimientos complementarios en materia sancionadora (art. 90.4).
- g) Las demás cuando una disposición legal o reglamentaria así lo establezca.

En el **ámbito estatal**, además (art. 114.2): actos de miembros y órganos del Gobierno; de
Ministros y Secretarios de Estado; de órganos directivos con nivel de Director general o superior
**en materia de personal**; y de los máximos órganos de dirección de organismos públicos.

> **Consecuencias operativas:** ⑴ la **responsabilidad patrimonial** agota la vía por sí sola —
> **no hay que interponer alzada**, y hacerlo puede hacer perder el plazo contencioso; ⑵ en la
> **Administración local**, comprobar la legislación de régimen local: los actos de Alcalde y Pleno
> ponen fin a la vía y el recurso propio es la **reposición potestativa**; ⑶ la **reposición es
> potestativa** (art. 123.1 LPAC, verificado) — no exigirla nunca como requisito.

**Dos trampas simétricas, ambas verificadas:**
- **Reposición interpuesta = puerta cerrada hasta que se resuelva.** Art. 123.2 LPAC: «**No se podrá
  interponer recurso contencioso-administrativo hasta que sea resuelto expresamente o se haya
  producido la desestimación presunta del recurso de reposición interpuesto.**» Si se interpuso
  reposición y aún no ha vencido el mes del art. 124.2, el contencioso es **prematuro**. Es
  potestativo interponerla; **una vez interpuesta, ya no**.
- **Contra reglamentos NO cabe recurso administrativo.** Art. 112.3 LPAC: «Contra las disposiciones
  administrativas de carácter general **no cabrá recurso en vía administrativa**». Quien "recurre en
  reposición" una ordenanza o un reglamento **no interrumpe nada** y consume los 2 meses del
  art. 46.1 LJCA. Contra la disposición general se va **directamente** al contencioso. Sí cabe, en
  cambio, recurrir un **acto de aplicación** fundándolo únicamente en la nulidad de la disposición,
  **ante el órgano que dictó la disposición** (art. 112.3, párr. 2.º) — es el **recurso indirecto**.
- **Actos de trámite en vía administrativa (art. 112.1, verificado):** solo caben alzada o reposición
  contra los **cualificados** (mismos cuatro supuestos del art. 25.1 LJCA). Contra los demás, la
  oposición «podrá alegarse por los interesados **para su consideración en la resolución que ponga
  fin al procedimiento**». No se pierde nada por no recurrirlos; se pierde por recurrirlos mal.

### 5. Legitimación — art. 19 LJCA y art. 69.b LJCA

Art. 69.b: inadmisión si el recurso se interpuso «por persona incapaz, no debidamente representada
o **no legitimada**» (verificado).

Art. 19.1 LJCA (verificado; redacción vigente desde 3-4-2025 por LO 1/2025):
- **a) Personas físicas o jurídicas que ostenten un derecho o interés legítimo.** Es la regla
  general. El **interés legítimo** es más amplio que el derecho subjetivo pero exige un beneficio o
  perjuicio **cierto, propio y actual** derivado de la estimación del recurso: no basta el interés
  en la legalidad. Su delimitación es **jurisprudencial** → verificar con `buscar_sentencias`.
- **b) Corporaciones, asociaciones, sindicatos, grupos y entidades del art. 18** afectados o
  legalmente habilitados para la defensa de intereses **legítimos colectivos**.
- **c)-e), g)** Administraciones (Estado, CCAA, entidades locales, entes de Derecho público) en los
  términos de cada letra. **f)** Ministerio Fiscal.
- **h) ACCIÓN POPULAR** — «cualquier ciudadano, **en los casos expresamente previstos por las
  Leyes**». La LJCA **no** la concede por sí: la concede la **ley sectorial**. Es habitual en
  **urbanismo** y en **medio ambiente**, pero **verificar la norma concreta** (estatal, y sobre todo
  **autonómica**) antes de invocarla. ⚠️ El conector **no cubre normativa autonómica**: si la acción
  popular depende de una ley autonómica, **pedírsela al usuario y no citarla de memoria**.
- **i)-j)** Legitimaciones específicas en igualdad de trato / no discriminación y derechos LGTBI,
  con **autorización de la persona afectada**. En acoso, **solo la persona acosada** está legitimada.
- **k) SINDICATOS** (añadida por LO 1/2025, en vigor **3-4-2025**): legitimados para actuar en
  nombre del **personal funcionario y estatutario** afiliado **que lo autorice**, en defensa de sus
  derechos individuales, recayendo los efectos sobre el afiliado. → **Arrastra la carga documental
  de la letra e) del art. 45.2. Ver punto 6.**
- **19.2:** la Administración autora de un acto, previa **declaración de lesividad**.
- **19.4:** recurso contra resoluciones de los tribunales administrativos de contratación, sin
  necesidad de declaración de lesividad.

### 6. ⚠️ Documentos del art. 45.2 LJCA — la causa de inadmisión más frecuente y más evitable

Verificado. Con el escrito de interposición se acompaña:

| | Documento |
|---|---|
| a) | El que **acredite la representación** del compareciente (salvo que ya conste en otro recurso pendiente ante el mismo órgano → pedir certificación). |
| b) | El que acredite la **legitimación** cuando se ostente **por transmisión** (herencia u otro título). |
| c) | **Copia o traslado del acto o disposición** impugnados, o indicación del expediente o del diario oficial. En inactividad y vía de hecho: mención del órgano o dependencia y del expediente de origen. |
| **d)** | 🔴 **PERSONAS JURÍDICAS: el «acuerdo corporativo».** |
| e) | **Sindicatos** ex art. 19.1.k). |

**d) EL ACUERDO CORPORATIVO — leer despacio.** El art. 45.2.d) exige «el documento o documentos que
acrediten el **cumplimiento de los requisitos exigidos para entablar acciones** las personas
jurídicas **con arreglo a las normas o estatutos que les sean de aplicación**», salvo que se hayan
incorporado o insertado en lo pertinente **dentro del cuerpo del poder** de la letra a).

- **NO basta el poder notarial.** El poder acredita la *representación*; la letra d) exige acreditar
  la **voluntad social de litigar**: el **acuerdo del órgano competente según los estatutos**
  (administrador único, consejo, junta, asamblea, junta de propietarios…).
- **Qué hacer, en concreto:** ⑴ pedir los **estatutos** y leer **qué órgano** es competente para
  entablar acciones; ⑵ pedir la **certificación del acuerdo** de ese órgano, con fecha **anterior**
  a la interposición; ⑶ si el poder notarial **inserta** la acreditación del acuerdo y de la
  competencia estatutaria, puede bastar — **leer el poder entero antes de decidirlo**, no fiarse de
  la fórmula de estilo.
- **Afecta a todas las personas jurídicas**: sociedades, asociaciones, fundaciones, cooperativas,
  comunidades de propietarios. Es la inadmisión que más asuntos buenos ha matado. **Cuesta un
  correo evitarla.**

**e) SINDICATOS** (LO 1/2025, en vigor **3-4-2025**): cuando el sindicato actúe ex art. 19.1.k),
hay que acreditar **tres** cosas: ⑴ la **afiliación** del funcionario o estatutario; ⑵ la
**comunicación del sindicato al afiliado** de la voluntad de iniciar el proceso; y ⑶ la
**autorización expresa del afiliado**. Las tres. Faltar una es faltar todas.

**Subsanación — art. 45.3 LJCA (verificado):** el LAJ examina de oficio la validez de la
comparecencia; si faltan documentos o son incompletos, **requiere la subsanación en 10 días**; si no
se subsana, el Juez o Tribunal **se pronuncia sobre el archivo**. → El defecto es subsanable, pero
**no se juega con eso**: aportarlo bien desde el principio.

> En el **procedimiento abreviado** el recurso se inicia **por demanda**, y con ella se acompañan
> igualmente los documentos del art. 45.2 (**art. 78.2 LJCA**, verificado). La letra d) aplica igual.

### 7. Competencia objetiva — arts. 8-14 LJCA

Umbrales **verificados** en `references/anclas-normativas-ca.md` (no calcular de memoria):

- **Juzgados de lo CA:** actos de **entidades locales** — **excluidas las impugnaciones de
  instrumentos de PLANEAMIENTO URBANÍSTICO** (van al TSJ); actos de **CCAA** en materia de personal
  (salvo nacimiento/extinción de la relación de funcionarios de carrera), **sanciones ≤ 60.000 €**
  y **responsabilidad patrimonial ≤ 30.050 €**; **Administración periférica del Estado**, salvo
  actos **> 60.000 €** o de **dominio público, obras públicas, expropiación forzosa y propiedades
  especiales**; **extranjería**. Autorizaciones judiciales del art. 8.6.
- Fuera de esos supuestos → **Sala del TSJ / AN / TS**, según arts. 10-12.
- **Consecuencia inmediata:** si el asunto va a **Sala** (órgano colegiado), el **procurador es
  preceptivo** (art. 23.2 LJCA); ante **Juzgado** es potestativo. Actualizar `procurador` en el asunto.
- Ante duda de umbral o materia, verificar con `buscar_articulo("LJCA","8")` … `("LJCA","14")`.

## Desviación procesal — el error que se comete después de admitido el recurso

No es causa del art. 69, pero mata pretensiones igual. Dos reglas:

1. **Interposición → demanda.** El art. 56.1 LJCA (verificado) permite alegar en la demanda
   «**cuantos motivos procedan, hayan sido o no planteados ante la Administración**». Ojo a la
   distinción, que es exactamente donde se falla: **los MOTIVOS son libres; la PRETENSIÓN no.** La
   pretensión queda acotada por el **acto impugnado** identificado en la interposición (art. 45.1) y
   por los límites del art. 31 (anulación; y reconocimiento de situación jurídica individualizada
   con las medidas de restablecimiento, incluida indemnización). Introducir en la demanda una
   pretensión ajena a ese acto = **desviación procesal**. El juez juzga **dentro del límite de las
   pretensiones formuladas** (art. 33.1). El perfil concreto de la doctrina es jurisprudencial:
   **verificar con `buscar_sentencias`**.
2. **Demanda → conclusiones.** El art. 65.1 (verificado): «en el acto de la vista o en el escrito de
   conclusiones **no podrán plantearse cuestiones que no hayan sido suscitadas en los escritos de
   demanda y contestación**». Sin válvula de parte. La única salida es la del **art. 33.2**
   (verificado): si el **órgano** aprecia motivos distintos susceptibles de fundar el recurso, lo
   somete a las partes por **providencia** con plazo común de **10 días** —irrecurrible— suspendiendo
   el plazo para el fallo. Es una facultad **del tribunal**, no un derecho de la parte: **no se puede
   provocar**. Todo lo que importe, va en la demanda.

## Salida

```
## Control de admisibilidad — [slug]

| # | Causa | Estado | Motivo / norma |
|---|---|---|---|
| 1 | Plazo (art. 69.e) | ✅/⚠️/🔴 | [fecha caducidad + art. 46.x LJCA] |
| 2 | Jurisdicción (art. 69.a) | ✅/⚠️/🔴 | |
| 3 | Acto impugnable (arts. 25 / 69.c) | ✅/⚠️/🔴 | [definitivo / trámite cualificado / confirmatorio] |
| 4 | Agotamiento de la vía (art. 114 LPAC) | ✅/⚠️/🔴 | [letra aplicable] |
| 5 | Legitimación (arts. 19 / 69.b) | ✅/⚠️/🔴 | [letra del art. 19.1] |
| 6 | Documentos art. 45.2 | ✅/⚠️/🔴 | [a) b) c) **d)** e) — uno a uno] |
| 7 | Competencia objetiva (arts. 8-14) | ✅/⚠️/🔴 | [órgano + procurador sí/no] |
| — | Cosa juzgada / litispendencia (art. 69.d) | ✅/⚠️/🔴 | |

**VEREDICTO: [RECURRIBLE / RECURRIBLE CON RESERVAS / INADMISIBLE]**

[Si CON RESERVAS: qué reserva, qué la resuelve y para cuándo.]
[Si INADMISIBLE: la causa, la norma y qué alternativa queda —revisión de oficio (art. 106 LPAC),
resolución expresa tardía, notificación defectuosa— o ninguna, dicho sin rodeos.]

**Acciones antes de redactar:** [lista concreta: pedir estatutos y certificación del acuerdo;
pedir el acuse de notificación; confirmar el órgano; etc.]
```

## Reglas

1. **🔴 en plazo o en acto impugnable → PARAR.** Avisar **antes de redactar nada**. No entregar un
   escrito impecable de un recurso que se va a inadmitir: es una factura sin objeto y una falsa
   seguridad para el cliente.
2. **El veredicto no se suaviza.** «Inadmisible» se dice con esa palabra. Si el asunto está perdido,
   se dice, y se habla de la RC profesional si procede. Esta skill existe precisamente para dar la
   mala noticia a tiempo.
3. **Nunca dar por buena la letra d) del art. 45.2 sin haber leído los estatutos o el poder entero.**
   La fórmula «con facultades suficientes» del poder **no** acredita el acuerdo corporativo.
4. **Prohibido inventar** artículos, letras, umbrales o plazos. Lo que no esté en
   `references/anclas-normativas-ca.md` se verifica con `buscar_articulo` en el momento. Si no se
   puede → `[verificar]` y decirlo.
5. **Prohibido citar jurisprudencia concreta** (ECLI/ROJ/fecha) sin `buscar_sentencias` /
   `buscar_por_cita`. Las doctrinas del interés legítimo, el acto confirmatorio y la desviación
   procesal son **jurisprudenciales**: se verifican o no se citan.
6. **Normativa autonómica y local: no se cita de memoria.** El conector no la cubre (salvo
   ordenanzas de los municipios cubiertos). Pedírsela al usuario.
7. **Nada de MASC.** No existe en esta jurisdicción. Nunca pedirlo ni bloquear un escrito por su
   ausencia. El equivalente es el **agotamiento de la vía administrativa** (art. 25.1 LJCA).
8. **Cero datos personales** en cuadros y ejemplos: `[RECURRENTE]`, `[ADMINISTRACIÓN]`, `[TERCERO]`.
9. Config del plugin: `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/`.
