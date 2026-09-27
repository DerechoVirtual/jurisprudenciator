---
name: solicitud-diligencias-instruccion-catalogo
description: Catálogo (sin plantilla). Redacta escritos solicitando la práctica de diligencias de investigación en instrucción. Actívala ante "pedir diligencias", "solicitar diligencias de investigación", "solicitar prueba en instrucción", "oficio a entidad bancaria", "oficio a la operadora", "declaración testifical", "careo", "pericial en instrucción", "solicitar diligencias complementarias", "entrada y registro", "intervención de comunicaciones", "pinchar el teléfono", "me han denegado las diligencias", "recurso contra la denegación de diligencias", "plazo de instrucción", "prórroga de la instrucción", "art. 324", o cuando una parte quiera impulsar o completar la investigación.
---

# Solicitud de diligencias de instrucción (catálogo — sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Reloj de la instrucción** → `buscar_articulo` (`ley="LECrim"`, `articulo="324"`).
- **Diligencias que afectan a derechos fundamentales** → `buscar_articulo` (`ley="LECrim"`) también para los arts. 588 bis a – 588 septies c, uno por uno (`articulo="588 bis a"`…).
- **Destinatarios de los oficios** → `buscar_empresa_mercantil` (sociedad: administradores, objeto, domicilio) y `consultar_catastro` (inmuebles en la averiguación patrimonial).
- **Oficio a la operadora: acceso a datos de tráfico** → `buscar_sentencias` (`base="TJUE"`, consulta sobre la Directiva 2002/58/CE) y (`jurisdiccion="PENAL"`, `base="TS"`).
- **Denegación de diligencias e indefensión** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="AP"`, `provincia` de la causa, `tipo_resolucion="AUTO"`) + `leer_sentencias` con `parrafos=3`.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Redacta el escrito por el que una parte interesa la práctica de diligencias de investigación.
Construye desde el marco legal. Orden: **control del plazo (324) → necesidad y relevancia → escrito**.

---

## ⏰ LO PRIMERO: EL RELOJ DEL ART. 324 LECrim — pedir tarde es NO pedir

**Antes de redactar una sola diligencia, calcula el plazo.** Es la comprobación que decide si el
escrito sirve para algo.

**Art. 324 LECrim (VERIFICADO, redacción Ley 2/2020, vigente 29-7-2020) — literal:**
- **324.1:** «La investigación judicial se desarrollará en un **plazo máximo de doce meses desde la
  incoación de la causa**.» Si antes del vencimiento se constata que no será posible finalizarla, el
  juez, **de oficio o a instancia de parte, oídas las partes**, podrá acordar **prórrogas sucesivas por
  periodos iguales o inferiores a seis meses**. Las prórrogas se adoptan mediante **auto** que exprese
  razonadamente: **las causas** que impidieron finalizar en plazo, **las concretas diligencias** que es
  necesario practicar y **su relevancia**. La **denegación** también por resolución motivada.
- **324.2:** «Las diligencias de investigación **acordadas con anterioridad** al transcurso del plazo o
  de sus prórrogas **serán válidas, aunque se reciban tras la expiración** del mismo.»
- **⭐ 324.3 — la clave:** «Si, **antes** de la finalización del plazo o de alguna de sus prórrogas, el
  instructor **no hubiere dictado** la resolución a la que hace referencia el apartado 1, **o bien esta
  fuera revocada por vía de recurso**, **NO serán válidas las diligencias acordadas a partir de dicha
  fecha**.»
- **324.4:** el juez concluye la instrucción cuando entienda cumplida su finalidad; transcurrido el
  plazo o sus prórrogas, dicta **auto de conclusión del sumario** o, en abreviado, **la resolución que
  proceda**.

### Protocolo obligatorio antes de redactar

1. **Localiza la fecha de INCOACIÓN** de la causa (no la del hecho, no la de la denuncia): es el
   *dies a quo*. **Cítala con su folio.**
2. **Reconstruye la cadena de prórrogas**: ¿hay auto? ¿es **anterior** al vencimiento? ¿está
   **motivado** con causas + diligencias concretas + relevancia? ¿fue **revocado** en recurso?
3. **Calcula el vencimiento vigente** y **dilo al usuario con la fecha**.
4. **Decide en consecuencia:**
   - **Con margen** → pide las diligencias **ya**, y **pide expresamente que se acuerden ANTES del
     vencimiento** (324.2 salva la recepción tardía, **no** el acuerdo tardío).
   - **Cerca del vencimiento** → **acumula en el mismo escrito** la petición de **prórroga** (324.1),
     motivada como exige el precepto: causas, **concretas diligencias** y **relevancia**. **La prórroga
     no se presume: hay que pedirla y el auto debe ser previo.**
   - **Vencido sin auto de prórroga previo** → ⚠️ **advierte al usuario**: lo que se acuerde a partir
     de esa fecha **no será válido** (324.3). Pedir diligencias entonces es inútil, y si acusas puede
     ser contraproducente. Si defiendes, **esto es un argumento de nulidad**: revísalo siempre.
5. **Déjalo escrito**: incoación, prórrogas y vencimiento, con sus folios, en un apartado del escrito.

> **Doble uso del 324 — no lo olvides:**
> - **Acusación:** el 324 es tu **calendario**. Lo que no se acuerde a tiempo, se pierde.
> - **Defensa:** el 324.3 es **el argumento de nulidad más rentable y más desatendido**. Revisa la
>   cadena de prórrogas en **toda** causa. Un solo auto tardío o revocado invalida todo lo acordado
>   después.
>
> ⚠️ El art. 324 es **precepto muy litigado**. Antes de fundar una nulidad en él, **contrasta la
> doctrina con `buscar_sentencias`** (alcance de la invalidez, diligencias afectadas, efectos sobre lo
> ya practicado). ⛔ **No afirmes de memoria** el alcance de la sanción del 324.3.

---

## Bloque previo de comprobaciones (OBLIGATORIO)

1. **Plazo del art. 324** → § anterior. **Innegociable.**
2. **¿Estás personado?** Solo el Ministerio Fiscal y **las partes personadas** proponen diligencias
   (art. 311). **El denunciante no es parte.** Si el usuario no está personado, primero
   → `personacion-acusacion-particular-catalogo` (o `querella-catalogo`).
3. **Fase del procedimiento** — determina el cauce:
   - Instrucción en curso → **arts. 311 / 776.3 / 777**.
   - Tras el traslado del art. 780.1 y **antes de acusar** → **diligencias complementarias del art.
     780.2**.
   - Sumario ordinario / abreviado: comprueba cuál es.
4. **Prescripción (art. 131 CP)** y **fecha de los hechos → ley aplicable (art. 2 CP)**: 5 años la
   mayoría de delitos, **1 año los leves**; **2.2 CP**: ley más favorable retroactiva (hechos anteriores
   al **10-4-2026** → comparar redacciones).
5. **Competencia** (art. 14 LECrim, verificado): Sección de Instrucción del Tribunal de Instancia; o
   Secciones de violencia sobre la mujer / infancia y adolescencia (14.5-14.7).
6. **¿La diligencia afecta a derechos fundamentales?** → § específico. Cambia por completo el estándar
   de motivación.
7. **Volatilidad de la fuente de prueba**: datos de tráfico, grabaciones de videovigilancia, chats,
   webs y publicidad **se destruyen por plazos de conservación**. Si la fuente es perecedera, **pídela
   ya y razona la urgencia**. Es la causa más común de prueba perdida.

---

## Marco normativo — VERIFICADO contra el BOE el 2026-07-17

**Art. 299 LECrim (verificado, literal):** «Constituyen el **sumario** las actuaciones encaminadas a
**preparar el juicio** y practicadas para **averiguar y hacer constar la perpetración de los delitos**
con todas las circunstancias que puedan influir en su **calificación** y la **culpabilidad** de los
delincuentes, **asegurando sus personas y las responsabilidades pecuniarias** de los mismos.»
> **Úsalo como marco de la petición:** toda diligencia debe reconducirse a una de estas cuatro
> finalidades. Si tu diligencia no encaja en ninguna, es **prospectiva** y se denegará.

**Art. 311 LECrim (verificado, literal) — el precepto nuclear:**
> «El Juez que instruya el sumario **practicará las diligencias que le propusieran el Ministerio Fiscal
> o cualquiera de las partes personadas SI NO LAS CONSIDERA INÚTILES O PERJUDICIALES**.
> Contra el auto denegatorio de las diligencias pedidas **podrá interponerse recurso de apelación, que
> será admitido en un solo efecto** para ante la respectiva Audiencia o Tribunal competente.»
- ⭐ **El estándar es favorable a la parte y muchos escritos lo desaprovechan:** la regla es
  **practicar**; la denegación es la **excepción**, y solo por **dos** causas tasadas: **inútil** o
  **perjudicial**. **No** «innecesaria», **no** «reiterativa», **no** «prospectiva» *por sí solas*.
- **Consecuencia redaccional:** tu escrito debe hacer **imposible** calificar la diligencia de inútil
  (demuestra su **utilidad** = aptitud para acreditar un extremo relevante) o perjudicial. Si el auto
  deniega con otra fórmula, **es materia de recurso**.
- **311 III:** si el Fiscal no está en la misma localidad, en vez de apelar **recurre en queja**.

**Art. 776.3 LECrim** — los personados pueden **tomar conocimiento de lo actuado e instar la práctica
de diligencias** y cuanto a su derecho convenga, acordando el juez lo procedente. ⚠️ La **LO 1/2025
reescribió los apartados 1 y 2 del art. 776**; el apartado 3 figura en el texto consolidado.
**Verifica su vigencia y numeración con `buscar_articulo` antes de citarlo** → **`[verificar]`**.

**Art. 777.1 LECrim (verificado):** el juez ordenará a la Policía Judicial o practicará por sí «**las
diligencias necesarias encaminadas a determinar la naturaleza y circunstancias del hecho, las personas
que en él hayan participado y el órgano competente para el enjuiciamiento**», dando cuenta al Fiscal.

**⭐ Art. 777.2 LECrim (verificado) — PRUEBA PRECONSTITUIDA, la diligencia que más se olvida:**
> «Cuando, **por razón del lugar de residencia de un testigo o víctima, o por otro motivo**, fuere de
> temer razonablemente que **una prueba no podrá practicarse en el juicio oral, o pudiera motivar su
> suspensión**, el Juez de Instrucción **practicará inmediatamente la misma, asegurando en todo caso la
> posibilidad de contradicción de las partes**.»
- Documentación: **soporte apto para la grabación y reproducción del sonido y de la imagen**, o acta
  autorizada por el LAJ con expresión de los intervinientes.
- ⚠️ **«A efectos de su valoración como prueba en sentencia, la parte a quien interese deberá INSTAR EN
  EL JUICIO ORAL la reproducción de la grabación o la lectura literal de la diligencia, en los términos
  del art. 730.»** ← **Si no lo instas en el juicio, la preconstituida no se valora.** Anótalo en el
  expediente: es una trampa clásica.
- **Art. 777.3:** **menor de 14 años** o **persona con discapacidad necesitada de especial
  protección** que deba declarar como testigo → se aplica el **art. 449 ter** y **debe** practicarse
  **prueba preconstituida**, siempre que el objeto del procedimiento sea alguno de los delitos de ese
  artículo. Valoración: instar en juicio la reproducción **audiovisual** (art. 730.2). **Verifica el
  art. 449 ter con `buscar_articulo`** antes de desarrollar su catálogo de delitos.

**Art. 780 LECrim (verificado) — diligencias complementarias:**
- **780.1:** acordado el trámite del abreviado, se da traslado de las diligencias previas al Fiscal y a
  **las acusaciones personadas** para que, en **plazo común de DIEZ DÍAS**, soliciten la **apertura del
  juicio oral** formulando escrito de acusación, o el **sobreseimiento**, o, **excepcionalmente**, la
  práctica de **diligencias complementarias**.
- **⭐ 780.2 — asimetría que debes conocer y explotar:**
  - Cuando **el Ministerio Fiscal** manifieste la **imposibilidad de formular escrito de acusación por
    falta de elementos esenciales para la tipificación de los hechos**, podrá instar las diligencias
    **indispensables para formular acusación**, **«en cuyo caso ACORDARÁ el Juez lo solicitado»** →
    **vinculante para el juez**.
  - "El Juez **acordará lo que estime procedente** cuando tal solicitud sea formulada por **la acusación
    o acusaciones personadas**" → **discrecional**.
  > **Traducción práctica:** la petición del **Fiscal** vincula; la de la **acusación particular**, no.
  > Si eres acusación particular y necesitas una diligencia indispensable, **considera interesar del
  > Fiscal que la haga suya**: es la vía más eficaz. Y en tu escrito, **razona la
  > indispensabilidad**, no la mera conveniencia.
  - En todo caso se cita para su práctica al Fiscal, a las partes personadas y **siempre al
    encausado**, dándose luego **nuevo traslado** de las actuaciones.
- ⚠️ El **carácter excepcional** («excepcionalmente», 780.1) es real: no uses el 780.2 como cajón de
  sastre para lo que debiste pedir en instrucción.

---

## Diligencias que afectan a DERECHOS FUNDAMENTALES

Estándar de motivación **radicalmente superior**. Si no puedes motivarlas así, no las pidas.

**Entrada y registro en domicilio — arts. 545 y ss. LECrim:**
- **Art. 545 (verificado, literal):** «**Nadie podrá entrar en el domicilio** de un español o extranjero
  residente en España **sin su consentimiento**, excepto en los casos y en la forma **expresamente
  previstos en las leyes**.»
- **Art. 550 (verificado):** el juez instructor puede ordenar la entrada y registro, **de día o de
  noche si la urgencia lo hiciere necesario**, en cualquier edificio o lugar cerrado que constituya
  domicilio, «precediendo siempre el **consentimiento** del interesado… **o, a falta de consentimiento,
  en virtud de AUTO MOTIVADO, que se notificará a la persona interesada inmediatamente, o lo más tarde
  dentro de las VEINTICUATRO HORAS de haberse dictado**».
- **Verifica con `buscar_articulo`** los arts. **546, 547, 548, 552, 558, 566 y 569** (supuestos,
  concepto de domicilio, contenido del auto, presencia del LAJ, requisitos del acta) **antes de citar su
  contenido**. **No des por buena de memoria la lista de requisitos del auto.**
- **Art. 18.2 CE**: inviolabilidad del domicilio.

**Interposición de comunicaciones y medidas tecnológicas — arts. 588 bis a y ss. LECrim:**
- Sedes: **art. 588 bis a y ss.** (disposiciones comunes), y las medidas específicas (intervención de
  comunicaciones telefónicas y telemáticas, datos de tráfico, registro de dispositivos, geolocalización,
  grabación de imagen y sonido, agente encubierto). **Art. 18.3 CE**: secreto de las comunicaciones.
- **⚠️ `[verificar]` — LIMITACIÓN DEL CONECTOR CONSTATADA (2026-07-17):** `buscar_articulo` **no
  resuelve los artículos con sufijo «bis a» / «ter a»** (trunca la referencia a «588 bis» y devuelve
  «no encuentro el artículo»). Se probaron múltiples variantes (`588 bis a`, `588 bis a)`,
  `588bis a`, `art. 588 bis a`, con `LECrim`, con el nombre completo y con el ID BOE) — **todas
  fallan**. **No es que el precepto no exista: el conector no puede resolverlo.**
- **Instrucción, y es obligatoria:** los **principios rectores** del **art. 588 bis a** (que la
  doctrina y la práctica citan como **especialidad, idoneidad, excepcionalidad, necesidad y
  proporcionalidad**) **NO están verificados con el conector**. **Antes de enunciarlos o de fundar un
  escrito en ellos:**
  1. Consulta el **texto consolidado del BOE**: `https://www.boe.es/buscar/act.php?id=BOE-A-1882-6036`.
  2. O usa **`buscar_boe`** / **`verificar_escrito`** para contrastar la cita.
  3. O contrasta con **`buscar_sentencias`**, que suele transcribir los principios.
  - **Si no lo verificas, márcalo `[verificar]` en el escrito y adviértelo al usuario.**
  ⛔ **PROHIBIDO transcribir de memoria** el listado de principios, sus definiciones o el contenido del
  auto habilitante. Es exactamente el tipo de cita que hunde un escrito.
- **Regla de oro:** estas diligencias exigen **auto judicial motivado**, **indicios objetivos previos**
  (no la mera petición de parte), **delito de la gravedad legalmente exigida**, **plazo** y **control
  judicial** de la ejecución. **Verifica cada uno de esos extremos antes de afirmarlo.**
- **Consecuencia de la ilicitud:** **art. 11.1 LOPJ** — no surtirán efecto las pruebas obtenidas,
  directa o indirectamente, violentando los derechos o libertades fundamentales. **Verifícalo con
  `buscar_articulo`** antes de transcribirlo. Es el motivo por el que la motivación no es un trámite.

---

## Cómo se pide una diligencia — la regla que decide

**Una diligencia mal pedida se deniega aunque sea buena.** Por **cada** diligencia, y **numeradas**:

| Elemento | Qué escribir |
|---|---|
| **Qué** | La diligencia, **delimitada**: qué documento, qué periodo, qué cuenta, qué persona. Nada de «todo lo relativo a» |
| **A quién** | Destinatario exacto del oficio: `[ENTIDAD]`, `[CIF]`, organismo, unidad |
| **Para qué** | **El hecho concreto** que trata de acreditar, con su ordinal en el relato |
| **Por qué es ÚTIL** | Aptitud para acreditarlo → **cierra la puerta al art. 311** («inútil») |
| **Por qué es NECESARIA** | No hay medio menos gravoso ni consta ya en autos |
| **Urgencia** | Si la fuente es **volátil** (datos de tráfico, videovigilancia, chats): **razónalo** |
| **Plazo** | Encaje en el **art. 324**: pide que se acuerde **antes del vencimiento** |

- **Sé específico.** Una petición genérica es **prospectiva** y se deniega. «Extractos de la cuenta
  `[IBAN]` de `[ENTIDAD]` entre `[FECHA]` y `[FECHA]`» se acuerda; «la documentación bancaria del
  investigado» no.
- **No repitas lo que ya consta.** Cita el folio y **pide solo lo que falta**.
- **Proporcionalidad**: pedir de más invita a la denegación **en bloque** — y la denegación en bloque
  te deja sin las buenas.

### Catálogo orientativo
- **Declaraciones**: investigado (art. 775 — **verifícalo**), testigos `[TESTIGO]`, **careo** (residual
  y de escaso rendimiento: úsalo con criterio).
- **Documental y oficios**: entidades bancarias (titularidad, autorizados, extractos, **trazabilidad**
  de fondos), Registro Mercantil (administradores, objeto, **depósito de cuentas** — también con
  `buscar_empresa_mercantil`), AEAT/TGSS, operadoras, plataformas, aseguradoras, Ayuntamiento.
- **Periciales**: contable, informática forense, médico-forense, de seguridad, caligráfica.
- **Preconstituida** (art. 777.2 y 777.3): **valórala siempre** si hay testigo residente en el
  extranjero, víctima vulnerable, o menor de 14 años.
- **Aseguramiento**: preservación de datos, volcado de dispositivos, acta notarial de páginas web.
- **Medidas cautelares reales** y **averiguación patrimonial**: no son diligencias de investigación en
  sentido estricto, pero **pídelas a tiempo** — se ganan pleitos incobrables.

---

## Recurso contra la denegación — y el GRAVAMEN posterior

**Esto es lo más importante de la skill después del 324. No lo omitas nunca.**

- **Art. 311 II (verificado):** contra el auto denegatorio de las diligencias pedidas cabe **recurso de
  apelación**, **admitido en UN SOLO EFECTO** (no suspende).
- **Régimen general (art. 766 LECrim, verificado):** caben **reforma** y **apelación**; la apelación
  puede interponerse **subsidiariamente con la reforma o por separado**, y **«en ningún caso será
  necesario interponer previamente el de reforma para presentar la apelación»** (766.2). **Plazo de
  apelación: CINCO DÍAS** desde la notificación del auto recurrido o del resolutorio de la reforma
  (766.3). Traslado a las demás partes: **5 días** comunes. **Reforma: 3 días (art. 211 LECrim —
  `[verificar]` antes de citarlo).**

> ### ⚠️ POR QUÉ HAY QUE RECURRIR SIEMPRE: EL GRAVAMEN
> **Recurrir la denegación no sirve solo para obtener la diligencia. Sirve para PODER ALEGARLO
> DESPUÉS.**
> - Quien **no pide** la diligencia no puede quejarse de que no se practicó.
> - Quien la pide, se la deniegan y **NO recurre**, **consiente la denegación**: pierde el **gravamen**
>   y, con él, la posibilidad de fundar en ella un recurso contra la sentencia (indefensión, art. 24
>   CE) o una casación por quebrantamiento de forma.
> - **Por eso, aunque la apelación tenga pocas probabilidades, se interpone.** El coste es un escrito;
>   el beneficio es **conservar el motivo**.
> - **Deja constancia de la protesta** y **documenta** petición → denegación → recurso → resultado, con
>   folios. Esa cadena es lo que sostiene el motivo meses después.
> - ⚠️ **Recuerda la sede nueva:** las cuestiones sobre prueba en el abreviado se sustancian hoy en la
>   **audiencia preliminar del art. 785** (LO 1/2025, vigente 3-4-2025), **no** al inicio del juicio.
>   **Art. 785.3 (verificado):** contra lo resuelto **no cabe recurso**, «sin perjuicio de la pertinente
>   **protesta** y de que la cuestión pueda ser **reproducida en el recurso frente a la sentencia**» —
>   salvo que ponga fin al procedimiento (entonces, apelación de los arts. 790 y ss.). **La protesta es
>   obligatoria: sin protesta no hay motivo.**
> - **Verifica el alcance del gravamen y de la protesta con `buscar_sentencias`** antes de construir el
>   motivo. ⛔ No cites doctrina de memoria.

---

## Estructura del escrito

1. **Encabezamiento:** «A LA SECCIÓN DE INSTRUCCIÓN DEL TRIBUNAL DE INSTANCIA DE [PARTIDO]» + **nº de
   Diligencias Previas [X/AÑO]** (art. 14 LECrim, LO 1/2025).
   > ⭐ **Regla práctica: copia la denominación EXACTA que figure en la resolución que contestas o en
   > la carátula del procedimiento.** Espejar al órgano nunca falla, diga «Sección de Instrucción del
   > Tribunal de Instancia» o siga rotulándose «Juzgado de Instrucción». Usar la denominación antigua
   > **no invalida** el escrito: la **DA 1.ª de la LO 1/2025** manda entenderla hecha a la Sección.
2. **Comparecencia:** procurador `[PROCURADOR]` y letrado/a, **en la representación ya acreditada** en
   autos (indica el folio de la personación).
3. **PRIMERO — Estado de las actuaciones y PLAZO DEL ART. 324:** fecha de **incoación** (folio),
   prórrogas acordadas (folios) y **fecha de vencimiento**. Es el apartado que casi nadie escribe y el
   que más pesa.
4. **SEGUNDO — Objeto de la investigación** y extremos **pendientes** de acreditar (art. 299).
5. **TERCERO — Diligencias que se interesan:** **numeradas**, cada una con **qué / a quién / para qué /
   utilidad / necesidad / urgencia** (tabla anterior). Si alguna afecta a derechos fundamentales,
   apartado **separado** con motivación reforzada.
6. **CUARTO — Encaje temporal:** que se acuerden **antes del vencimiento** (324.2); **y, si procede,
   PETICIÓN DE PRÓRROGA** (324.1) motivada con **causas + concretas diligencias + relevancia**.
7. **SUPLICO:** que se acuerde la práctica de las diligencias interesadas [y, en su caso, la prórroga
   del plazo de instrucción].
8. **OTROSÍES:** urgencia; designación de domicilio/dirección electrónica; copias.
9. Lugar, fecha y firma.

> **Anclaje al folio — regla innegociable.** Cada extremo que se dice pendiente, cada prórroga, cada
> diligencia ya practicada: **con su folio**. Un escrito de diligencias sin folios parece un formulario
> y se trata como tal.

---

## Errores típicos que hunden el escrito

1. **No calcular el art. 324.** Pedir tras el vencimiento sin prórroga previa = **pedir nada** (324.3).
2. **Creer que basta pedir la prórroga**: hace falta **AUTO previo** al vencimiento (324.3).
3. **Confundir 324.2 con 324.3:** el 324.2 salva que la diligencia **se reciba** tarde, **no** que se
   **acuerde** tarde.
4. **Peticiones genéricas y prospectivas** («toda la documentación relativa a…») → denegación.
5. **No razonar la UTILIDAD** → se lo pones fácil al art. 311 («inútil»).
6. **No recurrir la denegación** → **se pierde el gravamen**. Error estructural, no menor.
7. **No formular protesta** en la audiencia preliminar del art. 785 → sin protesta no hay motivo
   (785.3).
8. **Pedir diligencias sin estar personado.**
9. **Usar el 780.2 como cajón de sastre**: es **excepcional**, y solo vincula al juez cuando lo insta
   **el Fiscal**.
10. **Motivar una diligencia invasiva como si fuera un oficio**: entrada y registro o intervención de
    comunicaciones exigen **indicios objetivos previos**, no sospechas de parte.
11. **Enunciar de memoria los principios del art. 588 bis a.** ⛔ **No verificados** — ver
    `[verificar]` arriba.
12. **Olvidar instar en el juicio oral la reproducción de la preconstituida** (art. 777.2 in fine, 730)
    → la prueba **no se valora**.
13. **No pedir a tiempo la prueba volátil** (datos de tráfico, videovigilancia) → se destruye.
14. **Citar jurisprudencia sin conector.** ⛔ Prohibido.

---

## Datos personales — categoría reforzada

- Marcadores: `[INVESTIGADO]`, `[TESTIGO]`, `[ENTIDAD]`, `[CIF]`, `[DOMICILIO]`, `[IMPORTE]`,
  `[PERJUDICADO]`, `[PROCURADOR]`. **Nunca datos reales de terceros en la salida.**
- ⚠️ **Infracciones y condenas penales = categoría especial del art. 10 RGPD.** Esta skill es la de
  **mayor riesgo del plugin**: los oficios **recaban datos de terceros** (cuentas, comunicaciones,
  salud, ubicación). **Pide lo mínimo indispensable y delimita el periodo**: la proporcionalidad no es
  solo un requisito procesal, es también protección de datos. Cuidado extremo con **menores** (art.
  777.3, 449 ter) y **víctimas**.
- Slug del expediente: `descriptor-delito-año`, **nunca con el nombre del cliente**
  (`PROTECCION-DATOS.md`).

---

## Reglas de trabajo

- **Cifras y artículos:** fuente única `references/anclas-normativas-penal.md` (§ 3.1 para el 324) o
  verificación en el momento con **`buscar_articulo`**. ⛔ **Prohibido inventar** artículos, plazos o
  requisitos. Lo no verificable → **`[verificar]`** y **dilo**.
- **Jurisprudencia:** solo `buscar_sentencias` / `buscar_por_cita` / `leer_sentencias`. ⛔ Nunca de
  memoria.
- **Instruye el Juez de Instrucción** (Sección de Instrucción del Tribunal de Instancia). ⛔ **No existe
  el «fiscal instructor»**: reforma en tramitación (prevista 1-1-2028), **no es Derecho vigente**. No
  la menciones, ni cites un «art. 4 bis EOMF». Las diligencias **se piden AL JUEZ**, no al Fiscal —
  aunque el Fiscal pueda hacerlas suyas (780.2).
- ⛔ **Nada de MASC**: es del orden **civil**.
- **Días inhábiles — VERIFICADO, y la instrucción tiene régimen propio:**
  - **Art. 183 LOPJ** (verificado, redacción **LO 14/2022**, vigente 23-12-2022): «Serán inhábiles los
    días del **mes de agosto**, así como **todos los días desde el 24 de diciembre hasta el 6 de enero**
    del año siguiente, ambos inclusive, para todas las actuaciones judiciales, **excepto las que se
    declaren urgentes por las leyes procesales**.»
  - **⭐ Art. 201 LECrim** (verificado, literal): «**Todos los días y horas del año serán hábiles para la
    instrucción de las causas criminales, sin necesidad de habilitación especial.**»
  > **Consecuencia:** **la instrucción NO se paraliza** en agosto ni en Navidad. Y **el plazo del art.
  > 324 no se suspende** por ello. ⛔ No cuentes con agosto como colchón: es el error de cálculo que
  > deja diligencias fuera de plazo.

## Entrega

Escrito final en **Word `.docx`** con la skill **`docx`**, maquetado como escrito judicial
(encabezamiento, alegaciones numeradas, suplico, otrosíes), listo para **LexNET**.
