---
name: juicio-rapido
description: >-
  Enjuiciamiento rápido de determinados delitos (arts. 795-803 LECrim) — ámbito y catálogo del art. 795, diligencias urgentes ante la Sección de Instrucción en funciones de guardia, apertura de juicio oral en el acto (art. 800) y conformidad premiada del art. 801 con reducción de un tercio. Incluye el cálculo estratégico de conformarse o no en la guardia y el plazo de apelación de 5 días. Actívala ante "juicio rápido", "diligencias urgentes", "guardia", "juzgado de guardia", "me han citado para mañana en el juzgado", "conformidad con rebaja de un tercio en la guardia", "atestado y juicio rápido", "alcoholemia", "seguridad vial", "delito flagrante". Es la conformidad de la GUARDIA (art. 801), en horas y sin instrucción real: si el asunto ya está tramitándose como abreviado con audiencia preliminar señalada, usar /audiencia-preliminar-abreviado; para comparar todos los cauces de conformidad, /conformidad-penal-catalogo.
---

# Juicio rápido — arts. 795 a 803 LECrim

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Ámbito, diligencias urgentes y conformidad premiada** → `buscar_articulo` (`ley="LECrim"`, arts. 795-803).
- **Delitos contra la seguridad vial y sus penas** → `buscar_articulo` (`ley="CP"`, arts. 379-385); la reducción de un tercio del art. 801 se calcula sobre la pena verificada.
- **Criterio de la Audiencia que resolverá la apelación** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="AP"`, `provincia` de la causa) + `leer_sentencias` con `parrafos=3`.
- **Doctrina de la Sala Segunda sobre la conformidad del art. 801** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`).
- **Revisar el escrito de defensa o el acta de conformidad** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

Todo ocurre en horas y **sin instrucción real**. La decisión que define el asunto —conformarse en la
guardia o no— se toma con el atestado en la mano y sin tiempo. **Prepárala antes de entrar.**

> **Verifica cada precepto con `buscar_articulo` antes de citarlo.** Aquí va la *regla*, no el BOE.
> Anclas: `references/anclas-normativas-penal.md` §§ 5 y 11 bis. Verificado el 2026-07-17.

> ⚠️ **Nomenclatura (art. 14 LECrim, vigente 3-10-2025).** El órgano de guardia es hoy la **Sección de
> Instrucción del Tribunal de Instancia con competencia en materia de guardia** (art. 14.3), y el de
> enjuiciamiento la **Sección de lo Penal** (art. 14.3). **Los arts. 795-803 NO fueron actualizados** y
> siguen diciendo «Juzgado de guardia» y «Juzgado de lo Penal». **Al transcribirlos, reproduce el
> literal; en encabezamientos y competencia, usa la denominación vigente.**

---

## 1. Ámbito — art. 795 (redacción LO 1/2025, vigente 3-4-2025)

Han de concurrir **todos** los presupuestos del bloque A **y** **alguna** circunstancia del bloque B.

### Bloque A — presupuestos (los tres a la vez)

1. **Límite de pena: privativa de libertad que NO exceda de 5 AÑOS**, o cualesquiera otras penas
   —únicas, conjuntas o alternativas— **cuya duración no exceda de 10 años, cualquiera que sea su
   cuantía**.
   > ⚠️ **Son 5 años, no 3.** Los 3 años son el techo del **art. 801** (conformidad premiada): cosa
   > distinta. No confundas el ámbito del procedimiento con el de la conformidad.
2. **Incoación en virtud de ATESTADO POLICIAL.** Sin atestado no hay juicio rápido: una denuncia directa
   ante el juzgado o una querella no abren esta vía.
3. **Detenido puesto a disposición del juzgado de guardia**, **o** —aun sin detención— **citado a
   comparecer** por tener la calidad de **denunciado en el atestado**.

### Bloque B — circunstancias (basta UNA)

- **1.ª FLAGRANCIA.** Definición legal: el delito que se estuviese cometiendo o se acabare de cometer
  cuando el delincuente **sea sorprendido en el acto**; también el **detenido o perseguido inmediatamente
  después** si la persecución no se suspende mientras no se ponga fuera del inmediato alcance; y aquel
  sorprendido inmediatamente después **con efectos, instrumentos o vestigios** que permitan presumir su
  participación.
- **2.ª ⭐ CATÁLOGO del art. 795.1.2.º — literal verificado:**

  | | Delito |
  |---|---|
  | a) | **Lesiones, coacciones, amenazas o violencia física o psíquica habitual** contra las personas del **art. 173.2 CP** |
  | b) | **Hurto** · c) **Robo** · d) **Hurto y robo de uso de vehículos** |
  | e) | **Delitos contra la seguridad del tráfico** |
  | f) | **Daños** del **art. 263 CP** |
  | g) | **Contra la salud pública** del **art. 368, INCISO SEGUNDO, CP** |
  | h) | **Flagrantes** de **propiedad intelectual e industrial** — arts. **270, 273, 274 y 275 CP** |
  | i) | ⭐ **Allanamiento de morada** — **art. 202 CP** *(añadido por LO 1/2025)* |
  | j) | ⭐ **Usurpación** — **art. 245 CP** *(añadido por LO 1/2025)* |

  > ⚠️ **Erratas corregidas aquí.** La salud pública es el **368 inciso 2.º**, **no** el «270.1»: el 270
  > es propiedad intelectual y va en la **letra h)**, y solo **flagrante**. Y **las letras i) y j) son
  > nuevas**: ningún material anterior a abril de 2025 las recoge. Allanamiento y ocupación entraron en
  > juicio rápido con la LO 1/2025.
- **3.ª** Hecho punible **cuya instrucción sea presumible que será sencilla**.

### Exclusiones

- **795.2:** **NO** se aplica a delitos **conexos** con otros no comprendidos en el apartado 1.
- **795.3:** **NO** se aplica cuando proceda el **secreto de las actuaciones** (art. 302).
- **795.4:** supletoriamente, las normas del **procedimiento abreviado**.

> **Táctica de defensa.** El encaje en el 795 no es una formalidad: si el hecho no cabe en el catálogo,
> no es flagrante y la instrucción **no** es sencilla, la vía correcta son las **diligencias previas**
> —con instrucción, tiempo y diligencias de descargo—. **Cuestiona el encaje cuando te convenga
> litigar**, sobre todo por **conexidad (795.2)** o falta de sencillez (795.1.3.ª).

---

## 2. Policía Judicial — art. 796

Diligencias **en el tiempo imprescindible y, en todo caso, durante la detención**: informe de asistencia
al ofendido y médico forense si no puede desplazarse; **información del derecho a comparecer asistido de
abogado** —aun sin detención—, con designación de oficio por el Colegio si no lo manifiesta; citación con
**apercibimiento** de denunciado y testigos (**no** de los agentes cuya declaración conste en el
atestado); citación de las **aseguradoras del art. 117 CP**; remisión de sustancias a Toxicología; y
tasación pericial *in situ*, cuyo informe **puede emitirse oralmente** ante el juzgado.

- **⭐ 796.1.7.ª — seguridad vial:** alcoholemia conforme a la legislación de seguridad vial. Drogas:
  **test indiciario salival obligatorio**; positivo o signos de consumo → obligación de **facilitar saliva
  suficiente**, analizada en laboratorio homologado, **garantizándose la cadena de custodia**. **Todo
  conductor puede solicitar prueba de contraste** (sangre, orina u análogas).
  > **Filón de la defensa:** cadena de custodia, homologación y calibración del etilómetro, derecho a la
  > **segunda prueba** y al contraste, e información de derechos. **Pídelo todo en el atestado antes de
  > decidir nada.**
- **796.4:** si el responsable **no fue detenido ni localizado** pero es previsible su rápida
  identificación, la Policía sigue investigando en **un único atestado**, que remite en cuanto sea
  detenido o citado y **en todo caso dentro de los 5 días**. Instruye **en exclusiva** el juzgado de
  guardia que lo recibió.

## 3. Diligencias urgentes — art. 797

Se incoan por **auto irrecurrible** y se practican **con participación activa del Ministerio Fiscal**:
**antecedentes penales por el medio más rápido** (1.ª) —*decisivo tras la LO 1/2026: ver la skill
`delitos-leves`*—; periciales, **forense** y **tasación** (2.ª); **declaración del investigado** (3.ª,
art. 775; incomparecencia → art. 487); testigos (4.ª; incomparecencia → art. 420); informaciones del
art. 776 (5.ª); **rueda** (6.ª); **careos** (7.ª); citaciones, incluso verbales (8.ª; **no** de los
agentes salvo resolución motivada excepcional); y cualquier diligencia practicable en el acto o dentro del
plazo del art. 799 (9.ª).

- **⭐ 797.2 — prueba preconstituida:** si es de temer razonablemente que una prueba **no podrá practicarse
  en el juicio** o lo suspendería, el juez **la practica inmediatamente asegurando la contradicción**,
  documentada en soporte de grabación o acta. **Para valorarla, la parte interesada DEBE instar en el
  juicio oral la reproducción o la lectura literal** (art. 730).
  > **Si no se insta, esa prueba no entra.** Contrólalo en ambas posiciones.
- **⭐ 797.3 — dos reglas de oro:** (i) el abogado designado tiene **habilitación legal para la
  representación** en todas las actuaciones ante el juzgado de guardia — **no hace falta procurador**;
  (ii) incoadas las diligencias, el juez **dispondrá que se dé traslado de copia del atestado** y de
  cuantas actuaciones se realicen. **Exígelo y léelo antes de aconsejar nada.**
- **Art. 799:** las diligencias se practican **durante el servicio de guardia**. En partidos con guardia
  **no permanente de duración superior a 24 h**, prórroga de **72 horas adicionales** si el atestado se
  recibió dentro de las **48 h** anteriores a su finalización.

## 4. Resolución del juzgado de guardia — art. 798

Oídos el Fiscal y las partes (que **pueden pedir cautelares**), el juez resuelve:
- **1.º Diligencias suficientes** → **auto oral, documentado e irrecurrible**, ordenando seguir por los
  arts. 800-801, salvo que proceda alguna decisión de las **reglas 1.ª y 3.ª del art. 779.1**. Si reputa
  **delito leve** el hecho → **enjuiciamiento inmediato del art. 963** (skill `delitos-leves`).
- **2.º Diligencias insuficientes** → continúa como **diligencias previas** del abreviado, **señalando
  motivadamente** qué diligencias faltan o qué lo impide.
- **798.3:** contra el pronunciamiento sobre **cautelares**, los recursos del **art. 766**. **798.4:**
  devolución de objetos.

> **Petición de la defensa que casi nadie formula:** pedir el **798.2.2.º** (transformación en diligencias
> previas) **motivando qué diligencias de descargo son necesarias** —pericial de parte, testigos no
> citados, informe médico, revisión del etilómetro—. Es la vía para **recuperar el tiempo de instrucción**
> que el juicio rápido te quita. Denegada → **haz constar la protesta**.

## 5. Apertura del juicio oral — art. 800

- **800.1:** en el mismo acto se oye sobre **apertura o sobreseimiento**. Fiscal **y** acusador particular
  piden sobreseimiento → art. 782. Piden apertura → art. 783.1, por **auto oral motivado, documentado e
  irrecurrible**.
- **⭐ 800.2 — el momento decisivo:** abierto el juicio oral, **si no hay acusación particular**, el Fiscal
  presenta **de inmediato** su acusación **o la formula oralmente**. El acusado, **a la vista de la
  acusación**, puede en el mismo acto: **conformarse (art. 801)**; **o** presentar **inmediatamente** su
  defensa, oral o escrita; **o ⭐ solicitar plazo**, que el juez fija **dentro de los 5 días siguientes**,
  citándose en el acto a las partes.
  > **Pide siempre el plazo del 800.2 si no vas a conformarte.** Redactar una defensa de viva voz en la
  > guardia, sin haber estudiado el atestado, es indefensión autoinfligida.
- **800.3:** señalamiento del juicio **dentro de los 15 días siguientes**.
- **800.4:** **con acusación particular**, emplazamiento en el acto a esta y al Fiscal para presentar
  escritos en plazo **improrrogable no superior a 2 días**.
- **800.5:** si el Fiscal no acusa en plazo, se **requiere a su superior jerárquico** (2 días); si tampoco
  → se entiende que **no pide apertura** y procede el **sobreseimiento libre**.
- **800.7:** las partes pueden pedir al juzgado de guardia —**que así lo acordará**— la **citación de
  testigos o peritos**. **Úsalo: es gratis y asegura la comparecencia.**

> ⚠️ **Descoordinación — art. 800.6 `[verificar]`.** El 800.6 (Ley 13/2009) remite al «**apartado 1 del
> artículo 785**». Pero la **LO 1/2025** convirtió el 785.1 en la **audiencia preliminar** y el **art.
> 802.1 vigente la excluye expresamente** en juicio rápido (§ 7). La remisión quedó **desfasada** y su
> alcance no es pacífico: **contrasta con `buscar_sentencias`** antes de fundar en ello una estrategia y
> marca `[verificar]` si el criterio del órgano es desconocido. Ídem la remisión del **800.3 al «785.2»**:
> el señalamiento es hoy el **art. 786**.

---

## 6. ⭐ Art. 801 — conformidad ante el juzgado de guardia, con reducción de UN TERCIO

**El único descuento legalmente tasado del proceso penal español.** Requisitos **ACUMULATIVOS** (801.1):

1. Que **NO se haya constituido acusación particular** y el Fiscal haya pedido la apertura del juicio
   oral, **acordada por el juez**, presentando **en el acto** escrito de acusación.
2. Pena de **hasta 3 años de prisión**, **multa cualquiera que sea su cuantía**, u **otra pena de distinta
   naturaleza cuya duración no exceda de 10 años**.
3. Que, tratándose de privativa de libertad, la solicitada **o la suma** **no supere, REDUCIDA EN UN
   TERCIO, los 2 años**.
   > **El filtro opera sobre la pena YA reducida.** 3 años → 2 tras el tercio: **cabe**. 3 años y 1 mes →
   > 2 años y ~20 días: **no cabe**.

- **801.2:** control judicial, **sentencia oral** (art. 789.2), pena **reducida en un tercio** **aun cuando
  suponga imponer pena inferior al límite mínimo del CP**. Si Fiscal y partes **no recurren** → **firmeza
  oral en el acto** y resolución sobre **suspensión o sustitución**.
- **⭐ 801.3 — suspensión con MERO COMPROMISO:** basta el **compromiso de satisfacer las responsabilidades
  civiles** en el plazo prudencial que fije el juzgado; y, si se precisa certificación de deshabituación
  (art. 87.1.1.ª CP), **basta el compromiso de obtenerla**.
  > ⚠️ El 801.3 remite al «**art. 81.3.ª CP**», **derogado** por la LO 1/2015. Léelo como **art. 80.2.3.ª
  > CP**.
- **801.4:** el juez resuelve sobre libertad o ingreso, practica requerimientos y remite a la **Sección de
  lo Penal**, que **ejecuta**. **801.5:** **con acusador particular**, el acusado puede conformarse **en su
  escrito de defensa** con la más grave de las acusaciones.
- **Puerta adicional — art. 779.1.5.ª:** si el investigado, **asistido de abogado**, reconoce los hechos
  ante el juez y caben en los límites del 801, se incoan diligencias urgentes por los arts. 800 y 801.
- **Competencia (art. 14.3):** la **Sección de Instrucción con competencia en materia de guardia** es
  competente para **dictar sentencia de conformidad** en los términos del 801 — y también las Secciones de
  **violencia sobre la mujer** o **contra la infancia y la adolescencia**, en su caso.

### ⚠️ Descoordinación del 801 con la LO 1/2025 — señálalo y verifícalo

El **801.1 y 801.2 remiten al art. 787** para el control de la conformidad. Pero la **LO 1/2025** (vigente
**3-4-2025**) **trasladó el régimen de la conformidad al art. 785** (apdos. 4-11) y convirtió el **787 en
la celebración del juicio oral**. La remisión **no se actualizó**.

> **Regla de la casa:** cita el **801** como sede de la conformidad premiada y el **785** como régimen
> sustantivo del control. Si reproduces la remisión al 787, hazlo **con conciencia del desajuste** y
> adviértelo en nota. **Contrasta con `buscar_sentencias`** antes de fundar una estrategia en ello. Ver
> `conformidad-penal-catalogo` y anclas § 2.

---

## 7. Juicio oral y recursos — arts. 802 y 803

**Art. 802 (LO 1/2025):** el juicio se desarrolla como en el abreviado, ⭐ **salvo en lo relativo a la
audiencia preliminar previa del art. 785** → **en juicio rápido NO hay audiencia preliminar**. Si no puede
celebrarse o concluirse en un acto, nueva fecha **dentro de los 15 días**. **Sentencia en 3 días** desde
la terminación de la vista (art. 789).

**⭐ Art. 803 — EL PLAZO ES DISTINTO DEL GENERAL:**

| Trámite | Juicio rápido | Regla general |
|---|---|---|
| **Formalización de la apelación** | **5 días** (803.1.1.ª) | **10 días** (art. 790.1) |
| Alegaciones de las demás partes | **5 días** (803.1.2.ª) | 10 días comunes (790.5) |
| Sentencia de apelación | **3 días** tras la vista, o **5** desde la recepción si no hay vista (803.1.3.ª) | — |

- **803.1.4.ª:** tramitación y resolución **PREFERENTES**. **803.2:** sentencias en **ausencia** →
  art. 793. **803.3:** firme, **ejecución inmediata** (art. 794). Por lo demás, arts. **790 a 792**.

> 🚨 **El error más caro de esta skill.** Apelar con el plazo de 10 días del art. 790.1 = **fuera de plazo
> y recurso perdido**. **Son 5 días.** A la agenda **el mismo día de la notificación**.

---

## 8. Guía táctica — ¿conformidad en la guardia o juicio?

**No se improvisa: se calcula.** Antes de aconsejar, **lee el atestado completo** (te lo debe entregar el
juez, 797.3) y responde por escrito:

**Paso 1 — ¿Cabe el 801?** Sin acusación particular + Fiscal que acusa en el acto + pena ≤3 años (o multa,
u otra ≤10 años) + **pena reducida en un tercio ≤2 años**. Si falla uno, **no hay tercio**: la conversación
es otra (801.5).

**Paso 2 — Calcula el resultado real, no la rebaja nominal.** Escribe la cadena: **pena solicitada → −1/3 →
pena resultante → ¿art. 80 CP?**
- **La conformidad solo es buena si la pena resultante es SUSPENDIBLE:** ≤2 años (80.2.2.ª), primariedad
  (80.2.1.ª) y responsabilidades civiles (80.2.3.ª — **basta el compromiso**, y en guardia lo dice el
  **801.3**).
- ⭐ **LO 1/2026:** no computan los antecedentes de delitos que **«carezcan de relevancia para valorar la
  probabilidad de comisión de delitos futuros»** (80.2.1.ª). Argumento nuevo para salvar la primariedad.
- Añade **siempre** lo que no es prisión: **privación del permiso de conducir** (en seguridad vial es lo
  que más duele al cliente — y **también se reduce en un tercio**: cuantifícala), multa y su
  responsabilidad personal subsidiaria, decomiso, y **extranjería** (art. 89 CP).

**Paso 3 — Pondera contra las posibilidades reales de absolución.**
- **A favor de conformarse:** atestado sólido (flagrancia, etilómetro correcto y calibrado, agentes como
  testigos directos, reconocimiento previo); **el coste de que NO haya instrucción** —en la guardia **no
  hay tiempo de practicar diligencias de descargo**: si tu tesis exige una pericial, un testigo no citado o
  un informe médico, **hoy no los tienes**, y ese es el precio real del juicio rápido—; pena resultante
  suspendible + **firmeza en el acto** (801.2) = el asunto termina hoy.
- **A favor de litigar:** defectos en la **cadena de custodia** o en las pruebas de alcohol/drogas;
  vulneración de derechos en la detención (art. 520; entrevista reservada previa, 520.6.d); encaje dudoso
  en el 795 → **798.2.2.º**; prueba de cargo dependiente de un testigo sin contradicción; **pena no
  suspendible aun con el tercio** —si va a entrar en prisión igualmente, la rebaja no compra nada—.

**Paso 4 — Explica que la conformidad CIERRA EL FONDO.** **Art. 785.10:** solo son recurribles las
sentencias de conformidad cuando **no se hayan respetado los requisitos o términos**; **el acusado NO puede
impugnar por razones de fondo su conformidad libremente prestada**. Al cliente, claro: **hoy firmas y se
acabó. No hay arrepentimiento el mes que viene.**

**Paso 5 — ⭐ Cumple el art. 785.7 in fine.** «**El letrado o la letrada facilitará por escrito a la persona
a quien defiende la información sobre el acuerdo alcanzado.**» **Obligación legal, no cortesía**, y tu
prueba de diligencia. Genera el documento con `conformidad-penal-catalogo` (Entregable 2): hechos
aceptados, pena exacta y cómputo, responsabilidad civil, suspensión y condiciones, antecedentes y
cancelación (art. 136 CP), advertencia del 785.10 y alternativa de ir a juicio. **Acuse de recibo firmado.**

---

## 9. Perfil típico — seguridad vial (arts. 379-385 CP)

El grueso de los juicios rápidos. **Verifica las penas con `buscar_articulo` antes de citarlas**; lo
verificado el 2026-07-17:

| Tipo | Conducta |
|---|---|
| **379.1** | Velocidad **> 60 km/h** sobre el límite en vía **urbana** o **> 80 km/h** en **interurbana**. Prisión, multa o TBC alternativas **y, en todo caso, privación del permiso** |
| **379.2** | Conducción **bajo la influencia** de drogas o alcohol. **En todo caso** si **> 0,60 mg/l en aire espirado** o **> 1,2 g/l en sangre**. **Mismas penas del 379.1** |
| **383** | **Negativa** a someterse a las pruebas. **Solo prisión** (sin alternativa de multa) **y** privación del permiso |
| **384** | Conducir con **pérdida de vigencia** por pérdida total de puntos; **o** tras privación **cautelar o definitiva judicial**; **o sin haber obtenido nunca** permiso |

- **⭐ El 383 es más grave que el 379.2:** su mínimo es **prisión sin alternativa de multa**. Es la razón por
  la que negarse a soplar rara vez compensa al cliente. **Dilo sin rodeos.**
- **⭐ Art. 520.8 LECrim — renuncia a la asistencia letrada:** **solo** cabe si la detención lo es por hechos
  tipificables **exclusivamente como delitos contra la seguridad del tráfico**, previa información clara y
  comprensible, y es **revocable en cualquier momento**. Única excepción del sistema: compruébala si el
  atestado la invoca.

---

## Errores típicos

| Error | Corrección verificada |
|---|---|
| «El juicio rápido llega hasta 3 años» | **5 años** de privativa, u otras ≤ **10** (795.1). Los 3 años son el techo del **801** |
| «La salud pública del catálogo es el art. 270» | Es el **art. 368, inciso 2.º**. El 270 es **propiedad intelectual** (letra h, y solo flagrante) |
| Omitir allanamiento (202) y usurpación (245) | **Letras i) y j)**, añadidas por la **LO 1/2025** |
| Apelar en **10 días** | **5 días** (803.1.1.ª). Fuera de plazo = recurso perdido |
| Aplicar el tercio y luego mirar si llega a 2 años | El **filtro del 801.1.3.º opera sobre la pena YA reducida** |
| Citar el **art. 787** como sede de la conformidad | Desde el **3-4-2025** es el **785.4-11**. El 801 remite al 787 por **descoordinación** |
| Creer que hay **audiencia preliminar** en juicio rápido | **802.1 la excluye expresamente** |
| Conformarse sin calcular el **art. 80 CP** | Una conformidad no suspendible suele ser peor que el juicio |
| Formular la defensa oralmente sin leer el atestado | Pide el **plazo del 800.2** (5 días) y el **traslado del 797.3** |
| Omitir el documento del **785.7 in fine** | **Incumplimiento de un deber legal** del letrado |
| No instar la reproducción de la prueba preconstituida | **797.2 + art. 730**: sin instarlo, no se valora |
| Conformidad del 801 **con acusación particular** | Imposible (**801.1.1.º**). Solo el **801.5**, sin tercio tasado |
| «Juzgado de Instrucción» / «Juzgado de lo Penal» en el encabezamiento | **Secciones** del **Tribunal de Instancia** (art. 14, vigente 3-10-2025) |

## Reglas de trabajo

- **`buscar_articulo` antes de citar.** Anclas: `references/anclas-normativas-penal.md` §§ 5 y 11 bis.
  **Prohibido inventar** penas, plazos u ordinales → `[verificar]` y dilo.
- **Jurisprudencia solo vía `jurisprudenciator`.** **Prohibido citar ECLI, ROJ, fechas o ponentes de
  memoria.**
- **Ley penal en el tiempo:** redacción vigente **a la fecha de los hechos** (art. 2 CP) y comparación con
  la más favorable (art. 2.2 CP). Reformas recientes: **LO 1/2025** y **LO 1/2026**.
- **Nomenclatura:** **Secciones de los Tribunales de Instancia**, **LAJ**. Al transcribir los arts.
  795-803, reproduce el literal («Juzgado de guardia») y advierte del desajuste.
- **Instruye el Juez de Instrucción.** **No existe el «fiscal instructor»** en Derecho vigente.
- **Nada de MASC:** requisito del orden **civil**. En penal no existe.
- **Anonimización:** `[INVESTIGADO]`, `[VÍCTIMA]`, `[TESTIGO]`. Infracciones y condenas penales son
  **categoría especial (art. 10 RGPD)**. Ver `PROTECCION-DATOS.md`.
- Config del despacho: `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.

## Entrega

Word `.docx` (skill `docx`): la **nota de guardia** con el cálculo del § 8 (encaje en el 801, cadena pena →
tercio → art. 80 CP, recomendación motivada) y, si hay conformidad, el documento del **art. 785.7 in fine**
para el defendido.
