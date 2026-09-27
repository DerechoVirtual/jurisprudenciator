---
name: personacion-acusacion-particular-catalogo
description: >-
  Catálogo (sin plantilla). Redacta el escrito de personación del perjudicado como acusación particular en una causa YA INICIADA. Actívala ante "personarme como acusación particular", "mostrarse parte en la causa", "constituirse en acusación particular", "ofrecimiento de acciones", "me han ofrecido las acciones", "¿hasta cuándo puedo personarme?", "plazo para personarse", "apud acta", "designación apud acta", "reservar la acción civil", "renunciar a la indemnización", "derechos de la víctima", "Estatuto de la víctima", "quiero acusar además del fiscal", "el fiscal va a conformar", o cuando la víctima o perjudicado quiera intervenir en la causa tras los arts. 109, 109 bis o 776 LECrim. Requisito previo: existe ya procedimiento penal abierto. Si aún no hay causa y hay que iniciarla siendo parte desde el primer momento, usar /querella-catalogo.
---

# Personación como acusación particular (catálogo — sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo y legitimación** (arts. 109 bis, 110, 761, 776 y 785.4 LECrim) → `buscar_articulo` (`ley="LECrim"`).
- **Derechos de la víctima** → `buscar_articulo` con el Estatuto de la víctima por su nombre completo o su ID `BOE-A-2015-4606` (la sigla «Ley 4/2015» a secas devuelve otra ley).
- **Directiva 2012/29/UE de derechos de las víctimas** → `buscar_articulo` (`ley="Directiva 2012/29/UE"`) y, para su interpretación, `buscar_sentencias` (`base="TJUE"`).
- **Doctrina sobre la personación tardía y la adhesión** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.
- **Perjudicado, víctima o responsable civil que sea persona jurídica** → `buscar_empresa_mercantil` (denominación, CIF, domicilio y representantes).
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Redacta el escrito por el que el perjudicado se persona como acusación particular. Construye desde el
marco legal: no hay plantilla. Orden: **comprobaciones previas → plazo → escrito**.

---

## Bloque previo de comprobaciones (OBLIGATORIO)

1. **¿Hay causa abierta y cuál?** Órgano, **nº de diligencias previas** y fase. Sin esto no hay
   escrito. Si aún no hay causa → `denuncia-estafa` / `querella-catalogo`.
2. **Legitimación: ¿ofendido, perjudicado o ninguno?**
   - **Ofendido/víctima directa** → acusación particular sin fianza (art. 281.1.º LECrim).
   - **Solo perjudicado patrimonial** (no ofendido) → puede ejercer la **acción civil**; comprueba su
     posición para la penal.
   - **Ni uno ni otro** → sería **acción popular**, con fianza (art. 280) y límite jurisprudencial →
     `querella-catalogo`. **No lo disfraces de acusación particular.**
3. **⚠️ PLAZO — la duda más frecuente. Resuélvela ANTES de redactar** (§ siguiente).
4. **Prescripción del delito (art. 131 CP, verificado):** 20/15/10 años según pena; **5 años** los
   demás delitos; **1 año** delitos leves e injurias y calumnias. Pena compuesta → la que exija mayor
   tiempo (131.2); concurso o conexas → delito más grave (131.4). Compruébala: personarse en una causa
   por un delito ya prescrito no aprovecha a nadie.
   - **Cómputo (art. 132.1 CP, verificado):** desde la comisión; **continuado** → última infracción.
     ⭐ **Muy relevante para víctimas:** si la víctima es **menor de 18 años**, el plazo se computa
     **desde que alcanza la mayoría de edad** en los delitos de aborto no consentido, lesiones, contra
     la libertad, torturas e integridad moral, intimidad/propia imagen/inviolabilidad del domicilio y
     relaciones familiares; y **desde que cumple 35 años** en tentativa de homicidio, lesiones de los
     arts. 149 y 150, **maltrato habitual (art. 173.2)**, **delitos contra la libertad sexual** y
     **trata de seres humanos**. **Verifica el supuesto exacto en el art. 132.1** antes de descartar un
     asunto por prescripción: muchas víctimas creen que su acción caducó y **no es así**.
   - **🚨 Art. 132.2 CP (verificado):** la denuncia o querella **NO interrumpe**: solo **suspende 6
     meses**. Interrumpe la **resolución judicial motivada** que dirige el procedimiento contra persona
     determinada (regla 1.ª). Sin ella en 6 meses, el cómputo **continúa desde la fecha de la
     denuncia**. Si te personas en una causa parada, **comprueba si hay resolución de la regla 1.ª y su
     fecha**: puede que el delito esté prescrito pese al procedimiento abierto.
5. **Fecha de los hechos → redacción del CP aplicable (art. 2 CP).** 2.1 irretroactividad; **2.2 ley
   más favorable retroactiva**. Hechos anteriores al **10-4-2026** (LO 1/2026) → **compara
   redacciones**. Como acusación **no pidas** agravaciones inaplicables *ratione temporis* (p. ej.
   multirreincidencia de los arts. 248 párr. 3 o 250.1.8.º para hechos anteriores): es
   retroactividad desfavorable y desacredita el escrito.
6. **Competencia** (art. 14 LECrim, verificado): Sección de Instrucción del Tribunal de Instancia del
   partido; o Secciones de **violencia sobre la mujer** / **violencia contra la infancia y la
   adolescencia** (14.5, 14.6; y **14.7**: si concurren ambas, prevalece violencia sobre la mujer).
7. **Naturaleza del delito** (público / semipúblico / privado) y, si es semipúblico, **si consta la
   denuncia del ofendido** como requisito de procedibilidad.
8. **Conflicto de intereses** y **pluralidad de víctimas** (art. 109 bis.2 — § legitimación).

---

## ⚠️ EL PLAZO — art. 109 bis y art. 110 LECrim (VERIFICADOS)

**No hay un «plazo» único: hay un sistema de dos tramos.** Es la duda más frecuente y la que más
derechos hace perder. Explícasela siempre al usuario.

**Art. 109 bis.1 LECrim (literal, LO 8/2021, vigente 25-6-2021):**
> «Las víctimas del delito que no hubieran renunciado a su derecho podrán ejercer la acción penal **en
> cualquier momento antes del trámite de calificación del delito**, si bien ello **no permitirá
> retrotraer ni reiterar las actuaciones ya practicadas antes de su personación**. **Si se personasen
> una vez transcurrido el término para formular escrito de acusación podrán ejercitar la acción penal
> hasta el inicio del juicio oral adhiriéndose al escrito de acusación formulado por el Ministerio
> Fiscal o del resto de las acusaciones personadas.**»

**Art. 110 LECrim (literal, misma reforma)** — reproduce la regla para «las personas perjudicadas por
un delito que no hubieren renunciado a su derecho», que podrán mostrarse parte «**si lo hicieran antes
del trámite de calificación del delito**… **sin que por ello se retroceda en el curso de las
actuaciones**», con idéntica regla de adhesión posterior.

### Los dos tramos — tradúcelo así al cliente

| Momento de la personación | Qué puede hacer | Qué pierde |
|---|---|---|
| **Antes del trámite de calificación** | Acusación particular **plena**: proponer diligencias, intervenir, **formular escrito de acusación propio**, recurrir | **Nada hacia delante**. Pero **no se retrotraen ni se reiteran** las actuaciones ya practicadas (109 bis.1, 110) |
| **Después del término para formular escrito de acusación, y hasta el INICIO DEL JUICIO ORAL** | Ejercer la acción penal **solo por ADHESIÓN** al escrito de acusación del Fiscal o de otra acusación personada | **La acusación autónoma**: ya no puede pedir hechos, calificación ni pena distintos de aquellos a los que se adhiere |
| **Iniciado el juicio oral** | **Preclusión de la acción penal** | Todo (queda la acción civil no renunciada — art. 110 II) |

> **Conclusión operativa — dilo sin rodeos:**
> **Sí hay preclusión, y opera en dos escalones.** El límite absoluto es el **inicio del juicio oral**;
> pero el límite **útil** es el **trámite de calificación**: pasado este, la acusación particular queda
> **atada a la acusación ajena**. **Personarse pronto no es una formalidad: es lo que preserva la
> acusación autónoma.**
> **Corolario decisivo:** si el Fiscal **no acusa** y tú te personaste tarde, **no tienes a qué
> adherirte** — te quedas sin acusación. Esa es la razón real para personarse cuanto antes.

> ⚠️ **Coste de la personación tardía (109 bis.1, 110):** «no permitirá **retrotraer ni reiterar** las
> actuaciones ya practicadas». Las diligencias practicadas sin ti **no se repiten**. Si hay prueba
> preconstituida o testificales ya tomadas, **las pierdes como contradicción propia**. Adviértelo.

**Art. 110 II LECrim (verificado) — la acción civil sobrevive:**
> «Aun cuando las personas perjudicadas **no se muestren parte** en la causa, **no por esto se entiende
> que renuncian** al derecho de restitución, reparación o indemnización… siendo necesario que la
> renuncia de este derecho se haga **de una manera clara y terminante**.»
→ **No personarse NO es renunciar.** La renuncia debe ser **expresa, clara y terminante**. Nunca
consientas una renuncia tácita ni la des por hecha.

---

## Legitimación — arts. 109 bis y 761 LECrim (VERIFICADOS)

**Art. 761.2 LECrim (literal):** el LAJ instruirá al ofendido o perjudicado de sus derechos conforme a
los arts. 109 y 110, **«pudiendo mostrarse parte en la causa SIN NECESIDAD DE FORMULAR QUERELLA»**.
> ⭐ **Regla de oro del abreviado.** El perjudicado **no necesita querella** para ser acusación
> particular: basta el escrito de personación. **No propongas una querella a quien ya tiene causa
> abierta y solo quiere personarse**: es coste y demora inútiles.

**Art. 761.1:** el ejercicio por particulares de la acción penal o civil se hará en la forma del Título
II del Libro II, **«expresando la acción que se ejercite»** → **dilo expresamente** en el escrito.

**Art. 109 bis.1 II y III — muerte o desaparición de la víctima:** la acción penal puede ejercerla el
**cónyuge no separado** legalmente o de hecho, los **hijos** de la víctima o del cónyuge que
convivieran con ellos, la **pareja de hecho** análoga y sus hijos convivientes, los **progenitores** y
**parientes en línea recta o colateral hasta el tercer grado** bajo su guarda, personas sujetas a
tutela o curatela o en acogimiento familiar. En su defecto: **demás parientes en línea recta y
hermanos**, con preferencia del que ostentara la representación legal.

**Art. 109 bis.2 — pluralidad de víctimas (VERIFICADO):**
- El ejercicio por uno de los legitimados **no impide** el posterior por cualquier otro.
- **Todas pueden personarse independientemente con su propia representación.**
- **PERO:** cuando pueda verse afectado el **buen orden del proceso** o el **derecho a un proceso sin
  dilaciones indebidas**, el órgano, **en resolución motivada y tras oír a todas las partes**, **podrá
  imponer que se agrupen** en una o varias representaciones y sean dirigidos por la misma o varias
  defensas, **en razón de sus respectivos intereses**.
> Anticípalo en macrocausas: si hay intereses divergentes, **razónalo en el escrito** para resistir la
> agrupación forzosa.

**Art. 109 bis.3:** también pueden ejercerla **asociaciones de víctimas** y **personas jurídicas**
legitimadas para defender los derechos de las víctimas, **siempre que lo autorice la víctima**; y la
**Administración local** cuando el delito tenga por finalidad impedir u obstaculizar a los miembros de
las corporaciones locales el ejercicio de sus funciones públicas.

---

## Ofrecimiento de acciones y derechos de información

**Art. 109 LECrim (verificado, RD-ley 6/2023, vigente 20-3-2024):** al recibirse declaración al
ofendido o perjudicado, **el LAJ** le instruye del derecho a **mostrarse parte** y a **renunciar o no**
a la restitución, reparación e indemnización, y le informa de los derechos de la legislación vigente
(puede delegar en personal especializado). Si es **menor**, igual diligencia con su **representante
legal**.
- **Personas con discapacidad:** el art. 109 impone **adaptaciones y ajustes** — comunicación en
  **lenguaje claro, sencillo y accesible** (incluida **lectura fácil**), **lengua de signos** y medios
  de apoyo a la comunicación oral, **facilitador** profesional, y derecho a estar **acompañada de una
  persona de su elección desde el primer contacto**. **Invócalo si es el caso: es exigible.**
- **Delitos del art. 57 CP:** el LAJ **asegurará la comunicación a la víctima de los actos procesales
  que puedan afectar a su seguridad**.

**Art. 776.1 LECrim (verificado, LO 1/2025, vigente 3-4-2025):** el LAJ informa al ofendido y
perjudicado en los términos de los arts. 109 y 110 **cuando no lo hubiera hecho antes la Policía
Judicial**; y **si ya la hizo la Policía Judicial**, el LAJ **notifica el número de procedimiento, el
juzgado que lo tramita y las vías de contacto**, **sin necesidad de comparecencia** para un nuevo
ofrecimiento de acciones — **sin perjuicio del derecho de la víctima a la información actualizada del
estado del proceso** conforme a la **Ley 4/2015, de 27 de abril, del Estatuto de la víctima del
delito**.
> ⚠️ **Ojo:** ese ofrecimiento «simplificado» significa que **muchas víctimas nunca comparecen** y se
> confían. **El plazo del art. 109 bis corre igual.** No esperes a un ofrecimiento formal que puede no
> llegar.

**Estatuto de la víctima — Ley 4/2015, de 27 de abril (BOE-A-2015-4606):**
- **Art. 11 (verificado, literal):** toda víctima tiene derecho «a) A **ejercer la acción penal y la
  acción civil** conforme a lo dispuesto en la Ley de Enjuiciamiento Criminal, sin perjuicio de las
  excepciones que puedan existir. b) A **comparecer ante las autoridades encargadas de la
  investigación para aportarles las fuentes de prueba y la información** que estime relevante para el
  esclarecimiento de los hechos.» ← **el b) se puede ejercer sin estar personado**: úsalo mientras se
  tramita la personación.
- **Art. 5 (verificado):** derecho a información **desde el primer contacto**, incluido el **momento
  previo a la denuncia**: medidas de asistencia, derecho a denunciar, asesoramiento y **defensa
  jurídica gratuita**, medidas de protección, **indemnizaciones**, intérprete, **recursos que puede
  interponer contra las resoluciones contrarias a sus derechos**, y **art. 5.1.m)**: derecho a ser
  **notificada de las resoluciones del art. 7**, designando al efecto **dirección de correo
  electrónico** o, en su defecto, postal.
  > **Operativo:** **designa esa dirección expresamente** en un OTROSÍ. De ella depende que te
  > notifiquen el **auto de sobreseimiento** (art. 779.1.1.ª LECrim) y que corra tu plazo de recurso.
- **Art. 12 (verificado):** comunicación del **sobreseimiento** a las víctimas directas que denunciaron
  y a las demás conocidas; y **12.2: «La víctima podrá recurrir la resolución de sobreseimiento…
  SIN QUE SEA NECESARIO PARA ELLO QUE SE HAYA PERSONADO ANTERIORMENTE EN EL PROCESO.»**
- **Verifica con `buscar_articulo` (por nombre completo)** cualquier otro precepto del Estatuto antes
  de citarlo (arts. 7, 13, 2…).

> ⚠️ **Sigla ambigua — no falles aquí:** «**Ley 4/2015**» a secas resuelve en el conector a la *Ley
> 4/2015, de 17 de junio, de mejora de la estructura territorial agraria de **Galicia***. El Estatuto
> de la víctima es la **Ley 4/2015, de 27 de abril**. **Búscalo siempre por su nombre completo**
> («Estatuto de la víctima del delito») y **cítalo con la fecha**.

---

## ⭐ NOVEDAD LO 1/2025 — art. 785.4 párr. 2: el Fiscal debe oír a la víctima antes de la conformidad

**Baza nueva de la acusación particular. Verificado literalmente** (art. 785 LECrim, vigente 3-4-2025):

> «**El Ministerio Fiscal oirá previamente a la víctima o perjudicado, aunque no estén personados en
> la causa**, siempre que hubiera sido posible y se estime necesario para ponderar correctamente los
> efectos y el alcance de tal conformidad, **y en todo caso cuando la gravedad o trascendencia del
> hecho o la intensidad o la cuantía sean especialmente significativos**, así como **en todos los
> supuestos en que víctimas o perjudicados se encuentren en situación de especial vulnerabilidad**.»

**Cómo se usa — esto es lo que debes hacer con ello:**
- **La conformidad se sustancia hoy en la AUDIENCIA PRELIMINAR del art. 785** (LO 1/2025). ⚠️ **No en
  el art. 787**: el 787 es ahora la **celebración del juicio oral**. Material anterior a abril de 2025
  dice lo contrario y **está desfasado**.
- El deber de audiencia **opera aunque la víctima NO esté personada**. Es un derecho **autónomo**.
- **Tres supuestos, dos niveles de exigencia:**
  1. **Regla general** — «siempre que hubiera sido posible **y se estime necesario**»: modulable.
  2. **«En todo caso»** — gravedad o trascendencia del hecho, o intensidad o **cuantía especialmente
     significativas**: **no modulable**.
  3. **«En todos los supuestos»** de **especial vulnerabilidad** de la víctima: **no modulable**.
- **Estrategia:** si tu cliente entra en (2) o (3), **hazlo constar por escrito y por anticipado** —en
  la propia personación, en un OTROSÍ— **razonando la gravedad, la cuantía o la vulnerabilidad**, y
  **designando el medio de contacto**. Así el deber del Fiscal queda documentado **antes** de que se
  negocie nada, y su omisión queda acreditada.
- **Si se conformó sin oír a tu cliente** estando en (2) o (3): es un **incumplimiento de un deber
  legal expreso**. Combínalo con el **art. 785.10** (verificado): «Únicamente serán recurribles las
  sentencias de conformidad **cuando no hayan respetado los requisitos o términos de la
  conformidad**». **Verifica el encaje y la doctrina con `buscar_sentencias` antes de construir el
  recurso**: es precepto **nuevo** y su interpretación está abierta. **Márcalo `[verificar]` si no
  encuentras doctrina.**
- **Recuerda el límite estructural:** el art. 785.4 permite conformarse con «el escrito de acusación
  que contenga **pena de mayor gravedad**». **Si estás personado y acusas más gravemente que el
  Fiscal, la conformidad debe pasar por tu escrito.** Estar personado sigue siendo la protección
  fuerte; el 785.4 párr. 2 es la red de seguridad de quien no lo está.

---

## Acción penal y acción civil — ejercicio conjunto, reserva o renuncia

- **Art. 100 LECrim (verificado):** «De todo delito o falta nace **acción penal** para el castigo del
  culpable, y **puede nacer también acción civil** para la **restitución de la cosa**, la **reparación
  del daño** y la **indemnización de perjuicios** causados por el hecho punible.»
- **Art. 108 LECrim (verificado):** «La **acción civil ha de entablarse juntamente con la penal por el
  Ministerio Fiscal, haya o no en el proceso acusador particular**; pero **si el ofendido renunciare
  expresamente** su derecho de restitución, reparación o indemnización, el Ministerio Fiscal se
  limitará a pedir el castigo de los culpables.»
  > ⭐ **Consecuencia que debes explicar:** **el Fiscal ejercita la acción civil por ti aunque no te
  > persones.** Personarse **no** es imprescindible para que se pida indemnización. Lo que aporta la
  > personación es **cuantificarla tú**, **probarla** y **no depender del criterio del Fiscal**.
- **Tres opciones — plantéaselas al cliente y déjalo escrito:**
  1. **Ejercicio conjunto** (regla general): acción penal + civil en el proceso penal. Lo normal.
  2. **RESERVA de la acción civil** para el orden civil: se **reserva expresamente**, no se renuncia.
     Útil si la cuantificación exige prueba pericial compleja, si hay aseguradora o responsables
     civiles ajenos al proceso penal, o si el proceso penal va a demorarse. **Coste:** perder la
     gratuidad relativa y la ejecución conjunta; y afrontar un pleito civil autónomo.
     **Verifica el precepto exacto de la reserva (arts. 112 y 114 LECrim) con `buscar_articulo` antes
     de citarlo.**
  3. **RENUNCIA**: extingue el derecho. Debe ser **expresa, clara y terminante** (art. 110 II).
     **Adviértelo por escrito y no la sugieras nunca sin instrucción expresa del cliente.**
  > ⚠️ **No confundas reserva con renuncia.** Es el error más caro de esta skill: la reserva conserva
  > el derecho, la renuncia lo extingue. Y **guardar silencio no es ninguna de las dos** (110 II).
- **Cuantificación:** principal + intereses; **art. 116 CP (verificado)**: con varios responsables el
  tribunal **señala la cuota** de cada uno; autores y cómplices responden **solidariamente entre sí por
  sus cuotas** y **subsidiariamente** por las de los demás. **116.3:** la persona jurídica responde
  civilmente **de forma solidaria** con las personas físicas condenadas por los mismos hechos.
  **Responsable civil subsidiario (art. 120 CP)** y **partícipe a título lucrativo (art. 122 CP)**:
  **verifícalos con `buscar_articulo`** antes de invocarlos.

---

## Postulación: apud acta vs poder notarial

- **Poder notarial general para pleitos** con la mención de la causa: válido; coste y demora notarial.
  ⚠️ Para **querella** haría falta **poder especial** (art. 277 LECrim); **para la personación como
  acusación particular NO se necesita querella** (art. 761.2) y por tanto **no se exige poder
  especial**.
- **Apoderamiento *apud acta***: comparecencia ante el LAJ (o electrónico). **Gratuito e inmediato**:
  es la vía preferente cuando el plazo aprieta. **Verifica el precepto (art. 24 LEC, supletorio, y el
  régimen de apud acta electrónico) con `buscar_articulo` antes de citarlo.**
- **Regla práctica:** si el trámite de calificación está cerca, **persónate ya** e indica que el
  apoderamiento se otorgará *apud acta*, solicitando su señalamiento. **No pierdas el tramo de la
  acusación autónoma esperando una notaría.**
- Menores y personas con discapacidad: comprueba **representación legal** y **conflicto de intereses**
  (si el investigado es el representante legal → **defensor judicial**).

---

## Estructura del escrito

1. **Encabezamiento:** «A LA SECCIÓN DE INSTRUCCIÓN DEL TRIBUNAL DE INSTANCIA DE [PARTIDO]» + **nº de
   Diligencias Previas [X/AÑO]** (art. 14 LECrim, LO 1/2025).
   > ⭐ **Regla práctica: copia la denominación EXACTA que figure en la resolución que contestas o en
   > la carátula del procedimiento.** Espejar al órgano nunca falla, diga «Sección de Instrucción del
   > Tribunal de Instancia» o siga rotulándose «Juzgado de Instrucción». Usar la denominación antigua
   > **no invalida** el escrito: la **DA 1.ª de la LO 1/2025** manda entenderla hecha a la Sección.
2. **Comparecencia:** procurador `[PROCURADOR]` en nombre de `[PERJUDICADO]`, con poder que se
   acompaña **o** con indicación de que se otorgará **apud acta**; letrado/a director/a.
3. **PRIMERO — Condición de ofendido/perjudicado:** hechos que la acreditan, **anclados al folio**.
4. **SEGUNDO — Ofrecimiento de acciones:** si se practicó (art. 109 / 776.1) y su fecha; o que no
   consta practicado, **sin que ello precluya el derecho** (arts. 109 bis.1 y 110).
5. **TERCERO — Tempestividad:** que se formula **antes del trámite de calificación** (art. 109 bis.1)
   → acusación **plena**. Si es posterior al término para acusar, **dilo con franqueza** y funda la
   **adhesión** al escrito del Fiscal o de otra acusación (109 bis.1 in fine).
6. **CUARTO — Acciones que se ejercitan** (art. 761.1: «expresando la acción que se ejercite»):
   **acción penal** y **acción civil** (arts. 100 y 108); **o** acción penal con **reserva expresa** de
   la civil. **Nunca lo dejes implícito.**
7. **SUPLICO:** tener por **personado y parte** como **ACUSACIÓN PARTICULAR**; entender con el
   procurador las sucesivas diligencias; **traslado de lo actuado**; e intervención en las diligencias.
8. **OTROSÍES:**
   - **1.º Designación de dirección electrónica** a efectos del **art. 5.1.m) de la Ley 4/2015** y de
     las notificaciones (incluido el **auto de sobreseimiento**, art. 779.1.1.ª LECrim).
   - **2.º Audiencia previa a la conformidad** — art. **785.4 párr. 2** LECrim: razona **gravedad,
     cuantía o especial vulnerabilidad** y pide que se haga constar.
   - **3.º Diligencias** que se interesan → `solicitud-diligencias-instruccion-catalogo`.
   - **4.º Apoderamiento apud acta** (si procede) y **copias**.
9. Lugar, fecha y firma (procurador y letrado).

> **Anclaje al folio — regla innegociable.** Todo hecho afirmado (la condición de perjudicado, el
> ofrecimiento, el perjuicio) se ancla al **folio de las actuaciones** o al **documento** aportado. Sin
> ancla no hay indicio.

---

## Errores típicos que hunden el escrito

1. **Personarse tarde** y perder la **acusación autónoma** (109 bis.1). **El error más caro.** Y si el
   Fiscal no acusa, no hay a qué adherirse.
2. **Creer que el límite es el juicio oral** y confiarse: el límite **útil** es el **trámite de
   calificación**.
3. **Confundir RESERVA con RENUNCIA** de la acción civil.
4. **Dar por renunciada** la acción civil por no personarse: la renuncia ha de ser **clara y
   terminante** (110 II).
5. **Formular querella** cuando basta la personación (art. 761.2) → coste y demora inútiles.
6. **Exigir poder especial** para personarse: solo lo requiere la **querella** (277).
7. **Esperar a la notaría** en vez de usar **apud acta** con el plazo encima.
8. **No designar dirección electrónica** (art. 5.1.m) → no te notifican el sobreseimiento y **pierdes
   el plazo de recurso**.
9. **No invocar el art. 785.4 párr. 2** cuando hay especial vulnerabilidad o cuantía significativa.
10. **Citar el art. 787 como sede de la conformidad**: desde el 3-4-2025 es el **785**.
11. **No expresar la acción que se ejercita** (art. 761.1).
12. **Pedir la retroacción** de actuaciones al personarse: **el 109 bis.1 y el 110 lo excluyen**
    expresamente.
13. **Ignorar la agrupación** del art. 109 bis.2 en macrocausas.
14. **Buscar «Ley 4/2015» a secas** → ley agraria de Galicia, no el Estatuto de la víctima.
15. **Citar jurisprudencia sin conector.** ⛔ Prohibido.

---

## Datos personales — categoría reforzada

- Marcadores: `[PERJUDICADO]`, `[INVESTIGADO]`, `[TESTIGO]`, `[ENTIDAD]`, `[CIF]`, `[DOMICILIO]`,
  `[IMPORTE]`, `[PROCURADOR]`. **Nunca datos reales de terceros en la salida.**
- ⚠️ **Infracciones y condenas penales = categoría especial del art. 10 RGPD.** Aquí el cliente **es la
  víctima**: extrema el cuidado con datos de **salud** (informes de lesiones, periciales psicológicas),
  con **menores** y con víctimas en **especial vulnerabilidad**. En delitos del art. 57 CP, la
  seguridad de la víctima está en juego: no expongas domicilios ni centros de trabajo.
- Slug del expediente: `descriptor-delito-año`, **nunca con el nombre del cliente**
  (`PROTECCION-DATOS.md`).

---

## Reglas de trabajo

- **Cifras y artículos:** fuente única `references/anclas-normativas-penal.md` (§ 2.2 para el 785) o
  verificación en el momento con **`buscar_articulo`**. ⛔ **Prohibido inventar** artículos, plazos o
  penas. Lo no verificable → **`[verificar]`** y **dilo**.
- **Jurisprudencia:** solo `buscar_sentencias` / `buscar_por_cita` / `leer_sentencias`. ⛔ Nunca de
  memoria.
- **Instruye el Juez de Instrucción** (Sección de Instrucción del Tribunal de Instancia). ⛔ **No existe
  el «fiscal instructor»**: reforma en tramitación (prevista 1-1-2028), **no es Derecho vigente**. No
  la menciones, ni cites un «art. 4 bis EOMF».
- ⛔ **Nada de MASC**: es del orden **civil**.
- ⚠️ **Defecto de coordinación legislativa:** la LO 1/2025 **no** actualizó las remisiones internas —el
  **art. 784.3** y el **art. 801.1 y 2** siguen remitiendo al **art. 787** para la conformidad, cuyo
  régimen está hoy en el **785**. Cita el **785** como sede, y si reproduces la remisión legal, hazlo
  con conciencia del desajuste. **Contrasta con `buscar_sentencias`** antes de fundar una estrategia en
  ello.

## Entrega

Escrito final en **Word `.docx`** con la skill **`docx`**, maquetado como escrito judicial
(encabezamiento, alegaciones, suplico, otrosíes), listo para **LexNET**.
