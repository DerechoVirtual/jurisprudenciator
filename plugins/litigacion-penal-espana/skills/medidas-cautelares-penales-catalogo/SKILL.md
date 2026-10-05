---
name: medidas-cautelares-penales-catalogo
description: >-
  Catálogo (sin plantilla). Redacta solicitudes, oposiciones e impugnaciones de medidas cautelares penales personales y reales (prisión provisional, libertad provisional con fianza, prohibiciones del art. 544 bis, orden de protección del 544 ter, fianza y embargo). Actívala ante "solicitar prisión provisional", "oponerse a la prisión provisional", "medidas cautelares penales", "orden de alejamiento en caso NO de violencia de género", "prohibición de aproximación", "fianza y embargo art. 589", "comparecencia del art. 505", "recurrir el auto de prisión", o "medida cautelar frente al investigado". Presupone una causa penal en marcha y una medida que pedir, combatir o recurrir ante el juez de instrucción. NO es la skill para cuestionar la legalidad de una detención policial aún no judicializada: eso es /habeas-corpus. Si el caso es de violencia de género, doméstica o contra la infancia, la orden de protección tiene régimen especializado → /violencia-genero-orden-proteccion.
---

# Medidas cautelares penales (catálogo — sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Prisión provisional, art. 544 bis, orden de protección y primeras diligencias** → `buscar_articulo` (`ley="LECrim"`, arts. 13, 502-505, 544 bis y 544 ter).
- **Doctrina constitucional sobre motivación y proporcionalidad de la prisión provisional** → `buscar_sentencias` (`base="TC"`) + `leer_sentencias` con `parrafos=3`.
- **Criterio de la Audiencia que resolverá la apelación** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="AP"`, `provincia` de la causa, `tipo_resolucion="AUTO"`).
- **Medidas reales: bienes del investigado o del responsable civil** → `consultar_catastro` (inmuebles sobre los que pedir el embargo) y `buscar_empresa_mercantil` (sociedades vinculadas, administradores).
- **Comprobar las citas de normas** → `verificar_escrito`: cada redactor lo pasa solo con las frases de su sección que citan artículos o leyes; el ensamblado comprueba que cada ECLI o ROJ procede de una fuente leída.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Solicitudes, oposiciones e impugnaciones de medidas cautelares penales. Anclas:
`references/anclas-normativas-penal.md` (§ 7.2). Perfil:
`~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.

## 1. Comprobaciones previas

Se responden con la documentación aportada (paso 2 de `redaccion-rapida`); pregunta solo lo que
bloquee y en una única ronda.

1. **Posición procesal**: ¿solicitas (acusación), te opones (defensa) o impugnas una ya acordada?
2. **Órgano (art. 502.1)**: el juez instructor, el que forme las primeras diligencias, o el órgano de
   enjuiciamiento que conozca. ⚠️ **Nomenclatura LO 1/2025** (DF 38.3, desde 3-10-2025; art. 14
   LECrim): **Sección de Instrucción del Tribunal de Instancia**, no «Juzgado de Instrucción». En
   protección: **Sección de Violencia sobre la Mujer** (14.5), incluidos ⭐ **delitos contra la libertad
   sexual con víctima mujer** (14.5.h); ⭐ **Sección de Violencia contra la Infancia y la Adolescencia**
   (14.6, **nueva**); si concurren, **prevalece en todo caso** la primera (14.7).
3. **Fase**: ¿hay detenido a disposición judicial? → **comparecencia del art. 505 en 72 horas**.
4. **Título**: ¿544 bis, 544 ter, prisión provisional, o cautelar real (589)?
5. **Prescripción** (arts. 131 y 133 CP — anclas §§ 3.3 y 3.4): sobre delito prescrito no hay
   presupuesto.
   > ⭐ **Verificado (132.2.2.ª CP):** la **querella o denuncia NO interrumpe**: **suspende el cómputo un
   > máximo de 6 MESES**. Solo interrumpe la **resolución judicial motivada** que atribuya a persona
   > determinada su participación (regla 1.ª); si recae en esos 6 meses, la interrupción se retrotrae a
   > la querella/denuncia, **pero si el juez no adopta ninguna** —o hay inadmisión firme— **el cómputo
   > continúa desde la presentación**. (Rige la prescripción **del delito**, no la de la pena.)
6. ⭐ **Días hábiles — régimen propio (verificado):** el **art. 183 LOPJ** (LO 14/2022) declara inhábiles
   **agosto** y **del 24-dic al 6-ene**, salvo actuaciones urgentes. **Pero el art. 201 LECrim: «todos
   los días y horas del año serán hábiles para la instrucción de las causas criminales, sin necesidad de
   habilitación especial».** → La instrucción **no se paraliza**: el 505 (72 h), el 544 ter (72 h) y el
   art. 13 corren en agosto y en Navidad. Los plazos de **recurso** sí siguen el 183 LOPJ.
7. **Ley penal más favorable (art. 2.2 CP)**: retroactividad de la favorable **aunque haya sentencia
   firme**; **en caso de duda será oído el reo**. Con LO 1/2025 y **LO 1/2026** (vigente 10-4-2026),
   comprueba la redacción a la fecha de los hechos. Anclas §§ 1 y 7.
8. **Plazo de instrucción** (art. 324 — anclas § 3.1): sin auto de prórroga previo al vencimiento, las
   diligencias posteriores **no son válidas** (324.3). Controla incoación y cada prórroga.

## 2. ⭐ Art. 13 LECrim — primeras diligencias (reformado por la LO 1/2026, vigente 10-4-2026)

Las primeras diligencias incluyen ya, además de asegurar pruebas e identificar al delincuente,
**proteger a ofendidos, perjudicados, familiares u otras personas**, ⭐ **o EVITAR LA REITERACIÓN
DELICTIVA**, **pudiendo acordarse a tal efecto el 544 bis o la orden de protección del 544 ter**.

> **Operativo:** protección y reiteración son contenido expreso de las primeras diligencias desde el
> minuto uno. Si acusas, es el anclaje para pedirlas de inmediato. Si defiendes, **amplía el margen del
> instructor**: la batalla está en la motivación y la proporcionalidad, no en la competencia.

Mantiene, en delitos por internet/teléfono/TIC, la **retirada de contenidos ilícitos**, la **interrupción
de servicios** y el **bloqueo** cuando radiquen en el extranjero.

## 3. ⚠️ Art. 544 bis — REESCRITO por la LO 1/2026 (vigente 10-4-2026)

**Verificado el 2026-07-17. Todo material anterior está obsoleto.**

**Presupuestos:** delito del **art. 57 CP**; resolución **motivada**; que resulte **estrictamente
necesario** para **proteger a la víctima** ⭐ **o EVITAR LA REITERACIÓN DELICTIVA** (**finalidad nueva**,
autónoma). → Defensa: exige que se motive **cuál** de las dos finalidades se persigue y por qué es
*estrictamente* necesaria; el adverbio es de la ley y es exigible.

**Contenido (ámbito ampliado):** prohibición de **residir** o de **acudir** a un **lugar, barrio,
municipio, provincia u otra entidad local, o comunidad autónoma**; o de **aproximarse o comunicarse,
«con la graduación que sea precisa»**, a determinadas personas. → «Graduación» es literal: **pide
graduación, no todo o nada**.

### ⭐⭐ Ponderación obligatoria — munición directa para la defensa (literal)

> «Para la adopción de estas medidas **se tendrán en cuenta la situación económica del inculpado y los
> requerimientos de su salud, situación familiar y actividad laboral**. **Se atenderá especialmente a
> la posibilidad de continuidad de esta última, tanto durante la vigencia de la medida como tras su
> finalización.**»

No es retórica: es **mandato legal de ponderación**. Un auto que impone un 544 bis **sin ponderar los
cuatro factores** —y **especialmente** la continuidad laboral— está **inmotivado** en un extremo que la
ley impone. Constrúyelo con **prueba documental**: **económica** (nóminas, vida laboral, cargas);
**salud** (informes y **dónde** se dispensa el tratamiento — si el centro cae en la zona vetada, dilo);
**familiar** (empadronamiento, menores, personas a cargo); y **laboral** (contrato, **dirección exacta
del centro de trabajo**, ruta, turnos). Si el perímetro abarca el trabajo o el trayecto, **la medida
destruye el empleo** → propón **graduación**: excepción horaria, exclusión del centro del perímetro, o
radio menor. La ley obliga a mirar **tras la finalización** de la medida.

**Si acusas:** ponderar no es descartar. Acredita que la protección o la evitación **no se alcanza con
menos** y propón tú la graduación viable: un perímetro razonado se acuerda; uno desmedido se revoca.

**Incumplimiento — consecuencia tasada:** el juez **convoca la comparecencia del art. 505** para acordar
**prisión provisional** (503), **orden de protección** (544 ter) **u otra medida más limitativa**,
**valorando la incidencia del incumplimiento, sus motivos, gravedad y circunstancias**, sin perjuicio de
otras responsabilidades (quebrantamiento).
> **Defensa:** el incumplimiento **no lleva automáticamente a prisión**. La ley ordena valorar esos
> **cuatro factores**: alégalos uno a uno — un incumplimiento fortuito, aislado y sin contacto real no es
> un acercamiento buscado. Y la comparecencia del 505 es **contradictoria**.

**Control telemático:** en delitos del **art. 3 de la LO 10/2022**, posible por **resolución motivada**.

## 4. Orden de protección — art. 544 ter (síntesis; texto íntegro vía `buscar_articulo`)

- **Presupuestos (.1):** indicios fundados de delito contra vida, integridad física o moral, libertad
  sexual, libertad o seguridad de una persona del **art. 173.2 CP** **+ situación objetiva de riesgo**.
- **Legitimación (.2 y .3):** de oficio, víctima o persona con esa relación, o Fiscal. Cabe pedirla ante
  juez, Fiscal, **FCS**, oficinas de atención a la víctima o **servicios sociales**. Ante dudas de
  competencia territorial, **resuelve el juez ante el que se solicitó**.
- **⭐ Plazo (.4):** audiencia urgente (víctima, solicitante, presunto agresor **asistido de abogado**,
  Fiscal); puede sustanciarse **junto con la del 505**, la del 798 o el juicio de delito leve. **En todo
  caso, máximo 72 HORAS desde la solicitud.** Declaraciones **por separado**. Resuelve por **auto**. El
  instructor puede adoptar el **544 bis en cualquier momento**.
- **Estatuto integral (.5, .6 y .8-.11):** medidas penales + civiles + asistencia social; **oponible ante
  cualquier autoridad y Administración**; **deber de informar permanentemente a la víctima** de la
  situación procesal y **penitenciaria** del agresor; inscripción en el **Registro Central**; adoptable
  **en cualquier momento** si el riesgo surge durante la causa.
- **⚠️ Medidas civiles (.7):** deben **solicitarse** (víctima, representante, o Fiscal si hay menores).
  **Vigencia: 30 DÍAS**; si en ese plazo la víctima incoa proceso de familia, siguen **30 días más desde
  la demanda**, en los que el órgano civil ha de ratificarlas, modificarlas o dejarlas sin efecto.
  **Calendarízalo: se pierde por olvido.** Si hay indicios fundados de que hijos menores **presenciaron,
  sufrieron o convivieron** con la violencia y se dictan medidas penales → **suspensión del régimen de
  visitas**, salvo resolución motivada en el interés superior del menor previa evaluación de la relación
  paternofilial.

## 5. Prisión provisional

### 5.1 Principios (art. 502; arts. 17 y 24.2 CE)
- **Excepcionalidad y subsidiariedad (502.2):** solo cuando **objetivamente sea necesaria** y **no
  existan otras medidas menos gravosas** para los mismos fines. **Cítalo siempre**: la carga de
  descartar la alternativa menos gravosa es del auto; omitirla lo vicia.
- **Proporcionalidad (502.3):** repercusión de la medida, circunstancias del investigado y del hecho, y
  **entidad de la pena** que pudiera imponerse.
- **⭐ 502.4 — límite absoluto:** **no se adoptará en ningún caso** cuando se infiera racionalmente que
  el hecho **no es constitutivo de delito** o se cometió **concurriendo causa de justificación**.
  Argumento de primer orden si hay legítima defensa.

### 5.2 Requisitos (art. 503.1) — ACUMULATIVOS
1. **1.º** Hecho con caracteres de delito con pena **cuyo máximo sea ≥ 2 años** de prisión; **o** pena
   inferior **si tiene antecedentes no cancelados ni cancelables por delito doloso**.
2. **2.º** **Motivos bastantes** para creerle responsable criminalmente. **3.º** Alguno de estos
   **FINES**:
   - **a) Riesgo de fuga** — **conjuntamente**: naturaleza del hecho, gravedad de la pena, **situación
     familiar, laboral y económica** e **inminencia del juicio oral**. ⚠️ Con **≥ 2 requisitorias** en
     los **2 años anteriores**, **no rige el límite de pena** del 1.º.
   - **b) Evitar ocultación, alteración o destrucción de fuentes de prueba**, con **peligro fundado y
     concreto**. ⭐ **NO procede cuando el peligro pretenda inferirse ÚNICAMENTE del ejercicio del
     derecho de defensa o de la falta de colaboración del investigado.** **Cítalo literalmente**: es de
     los pasajes más útiles y más ignorados. Se valora la capacidad de acceder a las fuentes o influir
     sobre coinvestigados, testigos o peritos.
   - **c) Evitar que actúe contra bienes jurídicos de la víctima**, especialmente las del **173.2 CP**.
     Aquí **tampoco rige el límite de pena**.
4. **503.2 — reiteración delictiva:** con los requisitos 1.º y 2.º. ⭐ **Solo si el hecho es DOLOSO.**
   El límite de pena no rige si se infiere racionalmente actuación **concertada y organizada** o con
   **habitualidad**.

### 5.3 ⚠️ Plazos máximos — art. 504 (verificados; decisivos)

**504.1:** durará **el tiempo imprescindible** y **en tanto subsistan los motivos**. La subsistencia
**se reexamina**: lo que la justificó el primer mes puede no justificarla el décimo.

| Fin que la fundamenta | Máximo | Prórroga |
|---|---|---|
| Fuga (3.º a), víctima (3.º c) o reiteración (503.2) — pena **≤ 3 años** | **1 año** | **≤ 6 meses** |
| Los mismos fines — pena **> 3 años** | **2 años** | **≤ 2 años** |
| Ocultación/alteración de pruebas (3.º b) | **6 meses** | — |

- **Prórroga (504.2):** solo si **circunstancias que hicieran prever que la causa no podrá ser juzgada**
  en plazo; **una sola**, por **auto** y **en los términos del art. 505** → **con comparecencia
  contradictoria**. No es un trámite: se combate. **Condenado con sentencia recurrida:** prórroga **hasta
  la mitad de la pena efectivamente impuesta**.
- **504.3 y .4:** si se decretó **incomunicación** o **secreto** y se levantan antes de los 6 meses, el
  juez **habrá de motivar la subsistencia** del presupuesto (**pídeselo**). La libertad por transcurso
  del plazo **no impide** nueva prisión si, **sin motivo legítimo**, deja de comparecer.
- **⭐ 504.5 — cómputo:** se **suma** la **detención** y la prisión provisional **por la misma causa**;
  **se EXCLUYE** el tiempo de **dilaciones no imputables a la Administración de Justicia**. Ese
  descuento es el campo de batalla: **discútelo con fechas y folios**.
- **⭐ 504.6:** superadas las **2/3 partes** del máximo, juez y fiscal **comunican** a **presidente de
  sala de gobierno** y **fiscal-jefe**; tramitación **preferente**. **Invócalo**: es un derecho del
  preso preventivo.

### 5.4 Comparecencia — art. 505
- **505.2 — plazo:** **en el plazo más breve posible dentro de las 72 HORAS** desde la puesta a
  disposición judicial. Citación del investigado **asistido de letrado**, Fiscal y partes personadas.
  **También** para el **no detenido**.
- **505.3:** alegaciones y prueba practicable **en el acto o dentro de esas 72 horas**. ⭐ **«El Abogado
  del investigado o encausado tendrá, EN TODO CASO, acceso a los elementos de las actuaciones que
  resulten esenciales para impugnar la privación de libertad.»** (concordante con **520.2.d**). **Si te
  lo niegan, pídelo por escrito y haz constar la negativa en acta**: es el germen de la nulidad.
- **⭐ 505.4 — regla de oro de la defensa:** **«Si ninguna de las partes las instare, acordará
  necesariamente la inmediata puesta en libertad.»** → **El juez NO puede acordar de oficio la prisión
  provisional.** Si el Fiscal no la pide, no hay prisión. **Compruébalo antes de argumentar de más.**
- **505.5 y .6:** si la audiencia no puede celebrarse, cabe acordar la prisión (con los presupuestos del
  503), pero **en las siguientes 72 horas** se convoca **nueva audiencia**. Si el detenido se pone a
  disposición de juez distinto del de la causa, procede este; recibidas las diligencias, el de la causa
  **oirá al investigado con su abogado tan pronto como sea posible**.

## 6. ⭐ Cómo IMPUGNAR la prisión provisional

### 6.1 Recursos
- **Reforma: 3 días** (art. 211). **Apelación: 5 días** desde la notificación del auto o del que
  resuelva la reforma (**766.3**). **No hace falta reforma previa** (766.2); cabe subsidiaria o
  separada. **No suspenden** el curso del procedimiento (766.1).
- **⭐ 766.5 — VISTA, arma infrautilizada:** si el auto recurrido **acuerda la prisión provisional**, el
  apelante **puede solicitar en el escrito de interposición la celebración de vista, «que ACORDARÁ la
  Audiencia respectiva»**. → **No es discrecional: se pide y se acuerda.** El LAJ la señala **dentro de
  los 10 días** siguientes a la recepción. **Pídela siempre**: es defender la libertad ante la Sala, en
  vivo. (Para **otras** cautelares, la vista sí es potestativa.)
- **Tramitación (766.3):** escrito **con los motivos**, señalando **particulares a testimoniar**;
  traslado **5 días**; testimonio en **2 días**; la Audiencia resuelve en **5 días**.
- **Reproducción:** la prisión es ***rebus sic stantibus***. **Pide la libertad en cualquier momento** con
  **hechos nuevos** (arraigo sobrevenido, decaimiento del riesgo, transcurso del tiempo, levantamiento
  del secreto, cambio de calificación). No agotes la estrategia en un solo auto.

### 6.2 Habeas corpus — LO 6/1984 (verificado)
Obtiene la **inmediata puesta a disposición judicial** del **detenido ilegalmente**. Lo están (art. 1):
**a)** sin concurrir los supuestos legales **o sin cumplir las formalidades y requisitos** exigidos;
**b)** internamiento ilícito; **c)** **plazo superior al legal** (→ **72 h**, 520.1); **d)** **no
respetar los derechos** garantizados al detenido (→ **520.2**; anclas § 8: **3 horas** del abogado
(520.5), **entrevista reservada previa** a la declaración (520.6.d), acceso a elementos esenciales
(520.2.d)).
> **Delimita:** ataca la **detención ilegal** —típicamente gubernativa—, **no** el auto judicial de
> prisión, que se combate por **reforma/apelación** (§ 6.1). Verifica procedimiento y plazos de la
> LO 6/1984 con `buscar_articulo` antes de redactar.

## 7. Medidas cautelares reales — arts. 589 y ss.

- **589:** con **indicios de criminalidad**, el juez manda **prestar fianza bastante** para asegurar las
  responsabilidades pecuniarias, **decretando en el mismo auto el embargo** de bienes suficientes **si
  no la prestare**. **⭐ Cuantía:** se fija en el mismo auto y **«no podrá bajar de la tercera parte MÁS
  de todo el importe probable de las responsabilidades pecuniarias»** (= importe probable **+ 1/3**). Es
  la regla que más se cita mal: **léela literalmente antes de discutir la cifra**.
- **Arts. 590 y ss.** (clases de fianza, tercero responsable civil, ampliación y reducción) y el cauce
  del **responsable civil subsidiario** y de las **personas jurídicas**: **verifícalos con
  `buscar_articulo`**; si no lo confirmas → `[verificar]`.

## 8. Estructura del escrito

1. Encabezamiento a la **Sección de Instrucción del Tribunal de Instancia** (o de **Violencia sobre la
   Mujer** / **Violencia contra la Infancia y la Adolescencia**, o el órgano que conozca — 502.1 y 14).
2. Comparecencia (acusación que solicita; defensa que se opone o pide libertad).
3. **Antecedentes** con **folio**: detención (fecha y hora del atestado), puesta a disposición,
   calificación provisional, situación personal.
4. **Presupuestos**: *fumus* (503.1.1.º y 2.º, con folios) y *periculum* (**el fin concreto** del
   503.1.3.º o 503.2 que se invoca o se niega, **uno por uno**).
5. **Proporcionalidad, excepcionalidad y subsidiariedad** (502.2-502.3): **alternativas menos gravosas**
   — *apud acta*, retirada de pasaporte, fianza, 544 bis graduado, control telemático. En el 544 bis, la
   **ponderación del § 3** con prueba documental. **Medida interesada** (o alternativa), con **duración**
   y **graduación**.
6. **SUPLICO**; **comparecencia del 505** cuando proceda; en apelación contra auto de prisión, **VISTA
   (766.5)** en el propio escrito de interposición. Lugar, fecha y firma.

**Reparto para la redacción rápida:** 01 encabezamiento, comparecencia y antecedentes con folio · 02 presupuestos: *fumus* y *periculum* uno por uno (sus búsquedas de doctrina del TC y del TS) · 03 proporcionalidad, alternativas menos gravosas y medida interesada, con la ponderación del 544 bis si procede · 04 suplico, comparecencia del 505 o vista del 766.5, lugar, fecha y firma. Si la solicitud cabe en tres páginas, redáctala sin equipo.

## 9. Errores típicos

- ❌ Citar el **544 bis en su redacción anterior**, u omitir en defensa la **ponderación laboral**: el
  argumento más concreto y más desaprovechado.
- ❌ Olvidar que **el juez no puede acordar de oficio** la prisión (**505.4**).
- ❌ Confundir los **plazos del 504** según el **fin** (6 meses el probatorio; 1 o 2 años los demás), o no
  discutir el descuento de **detención previa** y **dilaciones** (504.5).
- ❌ Aceptar que el riesgo probatorio se infiera del **ejercicio de la defensa o la falta de
  colaboración** (503.1.3.º b) — **la ley lo prohíbe**.
- ❌ **No pedir VISTA** en la apelación contra el auto de prisión (**766.5**), donde **se acuerda**; o usar
  **habeas corpus** contra un auto judicial de prisión (cauce equivocado).
- ❌ Dejar caducar los **30 días** de las medidas civiles del 544 ter.
- ❌ Tratar el incumplimiento del 544 bis como prisión automática: hay que valorar **incidencia, motivos,
  gravedad y circunstancias**, en **comparecencia del 505**.
- ❌ Pedir prisión por **reiteración** en delito **imprudente** (503.2 exige **doloso**).
- ❌ Contar con el parón de agosto en instrucción (**201 LECrim**), o encabezar a un «Juzgado de
  Instrucción» (hoy **Sección del Tribunal de Instancia**, art. 14).

## 10. Reglas de trabajo

- **Jurisprudencia — verificación PREVIA y obligatoria** con `jurisprudenciator` (`buscar_sentencias`,
  `buscar_por_cita`, `leer_sentencias`): doctrina del **TC** y del **TS** sobre prisión provisional,
  motivación reforzada y proporcionalidad. ⛔ **PROHIBIDO inventar o citar de memoria** ECLI, ROJ, fechas
  o ponentes. Sin verificación → `[verificar]`, y decirlo.
- **Prohibido inventar** artículos, plazos o penas. Confirma con `buscar_articulo` si el cauce es
  **544 bis** o **544 ter**, y los preceptos de fianza/embargo (**590 y ss.**).
  > ⚠️ **Límite de la herramienta (anclas § 12):** `buscar_articulo` **trunca el sufijo alfabético**
  > (`846 bis a` → busca `846 bis` → «no encontrado»). Afecta a **588 bis/ter/quater...** y **846 bis
  > a-f**: márcalos `[verificar]` y remite al **BOE consolidado**. (`544 bis` y `544 ter` resuelven bien.)
- **Anclaje al folio**: detención, hora, atestado, prórrogas y notificaciones.
- **Marcadores:** `[INVESTIGADO]`, `[ACUSADO]`, `[VÍCTIMA]`, `[DATO]`. **Nunca datos reales**:
  investigaciones, infracciones y condenas son de **categoría especial** (**art. 10 RGPD**); aquí hay
  además **datos de salud**. Ver `PROTECCION-DATOS.md`.
- **Terminología (LO 1/2025, DF 38.3, desde 3-10-2025):** **Secciones de los Tribunales de Instancia**
  (art. 14 LECrim); LAJ. Al **citar el texto legal**, respeta su literalidad («el Juez de Instrucción
  dictará…», 544 ter).
- ⛔ **NO existe el «fiscal instructor».** Instruye el **Juez de Instrucción**; **quien pide** la prisión
  es el **Ministerio Fiscal o las acusaciones** (505.1) y **quien la acuerda** es el **juez**. Reforma en
  tramitación (prevista 1-1-2028): **nunca** como Derecho vigente.
- ⛔ **Nada de MASC**: es del orden civil.

## Entrega

Escrito final en **Word `.docx`** (lo genera el ensamblado de `redaccion-rapida`), maquetado para LexNET.
