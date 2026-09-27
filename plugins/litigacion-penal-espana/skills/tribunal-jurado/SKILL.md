---
name: tribunal-jurado
description: >-
  Guia practica del procedimiento ante el Tribunal del Jurado (LO 5/1995) para la defensa y la acusacion. Competencia del art. 1, instruccion propia, audiencia preliminar del art. 30, auto de hechos justiciables, objeto del veredicto y protesta, mayorias, devolucion del acta y apelacion ante el TSJ. Usar con "tribunal del jurado", "objeto del veredicto", "jurado popular", "me toca un jurado", "audiencia preliminar del jurado (art. 30 LOTJ)", "hechos justiciables", "veredicto", "recusacion de jurados", "apelacion del jurado", "LOTJ". Requisito previo: el delito es de los del art. 1 LOTJ y el procedimiento se sigue por los tramites del jurado. Ojo: su audiencia preliminar es la del art. 30 LOTJ y NO tiene nada que ver con la audiencia preliminar del art. 785 LECrim del procedimiento abreviado → /audiencia-preliminar-abreviado.
---

# Tribunal del Jurado — LO 5/1995

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Competencia, instrucción, objeto del veredicto y mayorías** → `buscar_articulo` (`ley="LOTJ"`; si no resuelve, su ID BOE con `buscar_boe`).
- **Apelación ante el TSJ (arts. 846 bis a – 846 bis f LECrim)** → `buscar_articulo` (`ley="LECrim"`, `articulo="846 bis a"`… hasta `"846 bis f"`), uno por uno.
- **Tipo y pena del delito del catálogo del art. 1.2 LOTJ** → `buscar_articulo` (`ley="CP"`).
- **Doctrina sobre el objeto del veredicto, el art. 46.5 y la motivación** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.
- **Criterio del TSJ en la apelación del jurado** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="TSJ"`, `provincia`).
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

> **Anclas:** `references/anclas-normativas-penal.md` (BOE, 2026-07-17). LOTJ verificada con
> `buscar_articulo` el 2026-07-17. Jurisprudencia **solo** con `buscar_sentencias`. **Prohibido
> inventar** ECLI, ROJ, fechas o ponentes. Lo no verificable → **`[verificar]`**, y se dice.
>
> ⛔ **NO existe el «fiscal instructor».** Instruye el **Juez de Instrucción** (art. 24.1 LOTJ,
> literal). ⛔ **Nada de MASC**: orden civil.
>
> **Nomenclatura (LO 1/2025, DF 38.3, desde 3-10-2025):** el **órgano** instructor es la **Sección de
> Instrucción del Tribunal de Instancia** (art. 14 LECrim) — usarla en encabezamientos; «Juez de
> Instrucción» solo al citar el texto literal. El juicio se celebra en el ámbito de la **AP**.

---

## ⚠️ 0. LA ADVERTENCIA QUE GOBIERNA ESTA SKILL

**El jurado NO es un abreviado con nueve señores al lado.** Instrucción, comparecencia, audiencia
preliminar, auto, reglas probatorias, mayorías y recursos son **propios**. Calcar del abreviado es la
fuente número uno de desastres.

| ❌ NO confundir | ✅ Es esto |
|---|---|
| Audiencia preliminar del **art. 785 LECrim** (abreviado, LO 1/2025) | **Art. 30 LOTJ** — **procedencia de la apertura del juicio oral**, ante el instructor |
| Art. 36 LOTJ = «auto de hechos justiciables» | **Art. 36 = CUESTIONES PREVIAS** al personarse. El auto es el **art. 37** |
| Lectura de sumariales (art. 714 LECrim) | **Art. 46.5 LOTJ: NO se puede dar lectura.** Régimen propio y más estricto |

---

## 1. Competencia — art. 1 LOTJ (vigente 3-7-2021, LO 9/2021)

**Rúbricas (1.1):** a) contra las **personas**; b) de **funcionarios públicos en el ejercicio de sus
cargos**; c) contra el **honor**; d) contra la **libertad y la seguridad**.

### ⭐ Catálogo cerrado (art. 1.2) — LITERAL VERIFICADO

| | Delito | CP |
|---|---|---|
| **a)** | Del **homicidio** | **138 a 140** |
| **b)** | De las **amenazas** | **169.1.º** |
| **c)** | De la **omisión del deber de socorro** | **195 y 196** |
| **d)** | Del **allanamiento de morada** | **202 y 204** |
| **e)** | De la **infidelidad en la custodia de documentos** | **413 a 415** |
| **f)** | Del **cohecho** | **419 a 426** |
| **g)** | Del **tráfico de influencias** | **428 a 430** |
| **h)** | De la **malversación de caudales públicos** | **432 a 434** |
| **i)** | De los **fraudes y exacciones ilegales** | **436 a 438** |
| **j)** | De las **negociaciones prohibidas a funcionarios** | **439 y 440** |
| **k)** | De la **infidelidad en la custodia de presos** | **471** |

> ⭐⭐ **LA TRAMPA: los INCENDIOS FORESTALES ya NO son competencia del jurado.** Estuvieron en el
> catálogo originario y **desaparecieron**; **no figuran en ninguna letra del 1.2 vigente**
> (verificado 2026-07-17). Material que los incluya está desactualizado.
> Otras que se fallan: **amenazas solo 169.1.º**; **allanamiento 202 y 204 — el 203 NO**; **homicidio
> 138-140** incluye asesinato (139) y agravado (140), pero **aborto, lesiones e inducción al suicidio
> NO**, pese a ser «delitos contra las personas».

**Órgano y exclusiones (1.3):** solo en el ámbito de la **AP** y, en su caso, tribunales por
**aforamiento**. **Excluidos:** delitos de la **Audiencia Nacional** y los de competencia asumida por
la **Fiscalía Europea**.

> **Conexidad** con delito ajeno al catálogo: litigiosa y **no resuelta en el art. 1** →
> **`[verificar]` con `buscar_sentencias`**. No improvisar de memoria.

---

## 2. Instrucción propia — arts. 24 a 27

**Art. 24.2: la LECrim es SUPLETORIA «en lo que no se oponga» a la LOTJ.**

- **Art. 24 — incoación:** cuando de la denuncia, querella o **cualquier actuación procesal** resulte
  contra **persona determinada** la imputación de un delito del catálogo, **previa valoración de su
  verosimilitud**, se incoa, practicando las **actuaciones inaplazables**.
- **⭐ Art. 25 — traslado de la imputación y comparecencia** (trámite propio, inexistente en el
  abreviado): conocimiento **inmediato** y convocatoria **en 5 días** a comparecencia para
  **concretar la imputación**, con MF y partes; traslado de denuncia o querella; letrado **necesario**
  (25.1). **Ofendidos y perjudicados no personados**: **citados para ser oídos** e instruidos **por
  escrito** de los **arts. 109 y 110 LECrim**, con indicación del derecho a **formular alegaciones si
  se personan en legal forma en dicho acto** y a la **justicia gratuita** (25.2). **Orden (25.3):**
  **MF** → **acusadores personados**, que **concretan la imputación** → **letrado del imputado**, que
  **puede instar el SOBRESEIMIENTO** (arts. 637 o 641 LECrim). Las partes **pueden pedir diligencias**.
  > ⭐ **Primera oportunidad formal de pedir el sobreseimiento** y de **fijar el perímetro de la
  > imputación** — perímetro que condiciona el auto del 37 y, con él, el objeto del veredicto. **No se
  > acude a escuchar.**
- **Art. 26:** continuación o **sobreseimiento** (637/641); si **MF y todas las partes lo instan**,
  arts. 642 y 644. **El auto de sobreseimiento es apelable ante la AP.**
- **Art. 27 — diligencias:** solo las **IMPRESCINDIBLES** para decidir la **apertura del juicio oral**
  y que **no puedan practicarse en la audiencia preliminar** (27.1); nuevas **en 5 días** desde la
  comparecencia o la última practicada (27.2); de oficio solo **como complemento**, limitadas al
  **hecho justiciable** y a las personas **imputadas por las acusaciones** (27.3); si las deniega,
  **nuevo traslado de 5 días** para instar la apertura **formulando conclusiones provisionales** (27.4).
  > ⚠️ **El estándar es «imprescindibles», no «pertinentes»**: la instrucción del jurado está
  > deliberadamente adelgazada. Argumentar en esa clave o llegan denegaciones sistemáticas.

> **Plazos:** el **art. 324 LECrim** rige por supletoriedad (12 meses + prórroga por auto motivado
> **anterior** al vencimiento; sin él, las diligencias posteriores **no son válidas** — anclas § 3.1).

---

## 3. Audiencia preliminar — art. 30

> ⚠️ **NO es la del art. 785 LECrim** (abreviado, LO 1/2025, ante el órgano de enjuiciamiento, sobre
> conformidad/cuestiones previas/prueba). **Esta es del jurado, ante el instructor, y versa sobre la
> PROCEDENCIA DE LA APERTURA DEL JUICIO ORAL.**

- **30.1:** **presentado el escrito de calificación de la defensa**, señalamiento **del día más próximo
  posible** —salvo diligencias pendientes de la defensa declaradas pertinentes—, resolviendo al tiempo
  sobre las diligencias **para el acto**. ⭐ **Si el Juez NO la convoca → QUEJA ante la AP.**
- **30.2:** **renunciable por la defensa** (art. 33), pero **solo surte efecto si la solicitan las
  defensas de TODOS los acusados**.

> ⭐ **Última oportunidad de evitar el juicio.** Renunciar solo tiene sentido si el sobreseimiento es
> inalcanzable. **Basta una defensa que no renuncie**: con pluralidad de acusados, coordinar antes.

---

## 4. Preparación del juicio y constitución

### 4.1 ⚠️ Art. 36 — cuestiones previas AL TIEMPO DE PERSONARSE (no es el auto)

**a)** artículos de previo pronunciamiento del **art. 666 LECrim**, competencia o **inadecuación de
procedimiento**; **b)** **vulneración de derecho fundamental**; **c)** **ampliación** a hechos cuya
apertura inadmitió el instructor; **d)** **exclusión de hechos** no incluidos en los escritos de
acusación; **e)** **impugnar prueba** ajena y **proponer** nueva → traslado de **3 días** para instar
su inadmisión. Tramitación: **arts. 668 a 677 LECrim** (36.2).

> ⭐ **Ventana corta y preclusiva.** La **prueba ilícita (art. 11.1 LOPJ)** y las vulneraciones de
> derechos fundamentales tienen su sede **aquí**, no al inicio de las sesiones: perderlo compromete el
> motivo de apelación. La letra d) es la herramienta contra la **sorpresa acusatoria**.

### 4.2 ⭐ Art. 37 — auto de hechos justiciables, prueba y señalamiento

Lo dicta **el Magistrado que vaya a presidir**:
- **a) Hechos justiciables** en **párrafos separados**; **no** cabe incluir en un párrafo términos
  susceptibles de tenerse unos por probados y otros no; **excluye toda mención no absolutamente
  imprescindible para la calificación**. Incluye hechos de **acusación y defensa**; pero **si la
  afirmación de uno supone la negación del otro, solo se incluye una proposición**.
- **b)** grado de **ejecución**, **participación** y **exención, agravación o atenuación**. **c)**
  **delito o delitos**. **e)** **señalamiento** (arts. 660-664 LECrim).
- **d) Prueba.** ⭐ **Verificado:** contra la resolución que **declare la procedencia** de un medio de
  prueba **no cabe recurso**; si **se deniega**, las partes **pueden formular OPOSICIÓN a efectos de
  ulterior recurso**.
  > **Si te deniegan prueba, FORMULA OPOSICIÓN EN EL ACTO.** Sin ella no hay recurso. **Primera** de
  > las dos protestas que deciden el pleito (la segunda: art. 53).

> ⭐⭐ **El auto del 37 es el molde del objeto del veredicto: lo que no entra aquí, no entra luego.**
> Atención a la **proposición única**: es donde la tesis de la defensa se queda fuera por absorción en
> la de la acusación.

### 4.3 ⭐ Art. 40 — sorteo, constitución y recusación

- **NUEVE jurados + DOS suplentes** por sorteo sucesivo, con lectura en alta voz (40.1-40.2).
- **Recusación sin causa (40.3):** tras las **preguntas** que las partes formulen y el
  Magistrado-Presidente declare pertinentes → **hasta CUATRO por las acusaciones y CUATRO por las
  defensas**. Varios acusadores o acusados: **de mutuo acuerdo**; **sin acuerdo se sortea el orden**
  hasta agotar el cupo. ⚠️ **Actor civil y terceros responsables civiles NO pueden recusar sin causa.**
- **40.4:** igual para suplentes; **cuando solo resten dos, no cabe recusación sin causa**. **40.5:**
  culminado el sorteo, **se constituye el Tribunal**.

> **Operativo:** las **preguntas previas** son el único instrumento real de conocimiento del jurado —
> llevarlas preparadas. Las cuatro recusaciones son recurso escaso: **no gastarlas al principio**; con
> pluralidad de defensas, **pactar el reparto antes** o se acabará sorteando.
>
> Constitución y recusación **con causa**: **arts. 38 y 39 — `[verificar]`**.

---

## 5. Juicio oral — arts. 45 a 49

- **Art. 45 — alegaciones previas:** lectura de los **escritos de calificación**; después, turno para
  **explicar al Jurado** las calificaciones y **la finalidad de la prueba**; cabe **proponer nuevas
  pruebas en el acto**.
  > ⭐ *Opening statement* español y momento **más infravalorado**: la primera y única vez que se habla
  > al jurado **sin la mediación de un testigo**. Ver § 9.
- **Art. 46 — especialidades:** los jurados **preguntan por escrito** vía Magistrado-Presidente, previa
  pertinencia (46.1); **ven por sí** las piezas de convicción (46.2); en **inspección ocular** el
  Tribunal se constituye **en su integridad, con los jurados**, en el lugar (46.3); las **diligencias
  del instructor pueden exhibirse** (46.4).
  > La pregunta de un jurado revela **qué le preocupa**: única ventana a su deliberación. Ajustar el
  > interrogatorio a lo que revela.

### ⭐⭐ Art. 46.5 — LA REGLA QUE GENERA LAS NULIDADES

Literal verificado: cabe **interrogar sobre las contradicciones** entre lo dicho en juicio y en
instrucción, pero «**no podrá darse lectura a dichas previas declaraciones**, aunque **se unirá al
acta el testimonio que quien interroga debe presentar en el acto**». Y: «**Las declaraciones efectuadas
en la fase de instrucción, salvo las resultantes de prueba anticipada, NO tendrán valor probatorio de
los hechos en ellas afirmados.**»

| Sí se puede | No se puede |
|---|---|
| **Interrogar sobre la contradicción** | **Dar LECTURA** a la sumarial (≠ art. 714 LECrim) |
| **Unir al acta el testimonio**, que **quien interroga presenta EN EL ACTO** | Usar la sumarial como **prueba de los hechos** |
| Usar la **prueba anticipada** con valor probatorio | Convertir la retractación del testigo en condena vía sumario |

- ⭐ **Carga preclusiva: el testimonio lo lleva quien interroga, a la sala.** Nadie te lo va a buscar.
- ⭐ **En jurado el testigo que se retracta vacía la acusación**, porque lo dicho en instrucción **no
  tiene valor probatorio**. Diferencia estructural con el resto de procedimientos.
  > Su alcance exacto, la relación con el 714 y con la prueba preconstituida es **fuente constante de
  > nulidades y NO es pacífico**: **`[verificar]` SIEMPRE con `buscar_sentencias`**.

- **Art. 48 — conclusiones definitivas:** modificables (48.1). ⭐ **48.3:** aunque en definitivas se
  califique un delito **NO atribuido al jurado, este CONTINÚA CONOCIENDO** (*perpetuatio
  iurisdictionis*: no se vacía la competencia recalificando a la baja).
  > ⚠️ **48.2 — remisión desfasada** al **art. 793.6 LECrim**, **renumerado hace años** (y el abreviado
  > se reestructuró de nuevo con la LO 1/2025 — anclas § 2). **`[verificar]` el precepto equivalente**
  > con `buscar_articulo` y contrastar con `buscar_sentencias`. Mismo defecto que anclas § 2.2 (784.3
  > y 801).
- **⭐ Art. 49 — disolución anticipada:** **concluidos los informes de la ACUSACIÓN**, la defensa puede
  pedir —o el Magistrado-Presidente acordar de oficio— la **disolución** si **del juicio no resulta
  prueba de cargo que pueda fundar una condena**; si solo afecta a algunos hechos o acusados, cabe
  declarar **no haber lugar a veredicto** sobre ellos → **sentencia absolutoria motivada dentro de
  TERCERO DÍA**.
  > ⭐ *Directed verdict* español; no existe en el abreviado. **Anotar la ventana en el guion de la
  > vista** — se pierde por despiste. Si la acusación naufragó (típicamente vía 46.5), **pedirla
  > siempre**: absolución sin someter el caso a nueve legos.

---

## 6. ⭐⭐ OBJETO DEL VEREDICTO — art. 52 — LA PIEZA CLAVE

> **La redacción del objeto del veredicto decide el juicio.** El jurado **no responde a lo que ocurrió:
> responde a lo que se le pregunta.**

**Momento (52.1):** concluido el juicio oral, **tras los informes y oídos los acusados**, se somete
**por escrito**:

| Regla | Contenido |
|---|---|
| **a) HECHOS** | Párrafos **separados y numerados**, **diferenciando CONTRARIOS y FAVORABLES**. ⛔ **Prohibido mezclar en un mismo párrafo** favorables y desfavorables, o hechos de los que unos puedan tenerse por probados y otros no ← **causa típica de impugnación**. Empieza por el **hecho principal de la acusación**, después las **defensas**. **Proposición única** si la consideración simultánea no es posible sin contradicción. **Prioridad lógica**: si un hecho se infiere de otro, este se propone **con prioridad y separación** |
| **b) EXENCIÓN** | Hechos que puedan determinar una **causa de exención**, con igual separación y numeración |
| **c)** | **Grado de ejecución, participación y modificación** de la responsabilidad, en párrafos sucesivos |
| **d)** | **Finalmente**, el **hecho delictivo** por el que será declarado **culpable o no culpable** |
| **e) y f)** | Redacción **separada y sucesiva por cada delito** y **por cada acusado** |
| **g)** | ⭐ Puede **añadir hechos o calificaciones FAVORABLES** si **no implican variación sustancial ni indefensión**; si de la prueba deriva variación sustancial → **deduce tanto de culpa** |

**52.2:** recaba, **en su caso**, el criterio del jurado sobre **remisión condicional de la pena** e
**indulto**.
> ⚠️ **Nomenclatura:** «remisión condicional» es terminología del CP de 1973 que la LOTJ conserva; hoy
> equivale a la **suspensión de la ejecución (art. 80 CP**, LO 1/2026, vigente 10-4-2026 — anclas § 6).
> **Usar el término de la LOTJ** en el objeto del veredicto y explicar la correspondencia.

### ⭐⭐ Art. 53 — audiencia a las partes y PROTESTA

> **SIN PROTESTA NO HAY MOTIVO DE APELACIÓN.** Si retienes una sola frase de esta skill, que sea esta.

- **53.1:** **antes de entregar** el escrito a los jurados, se **oye a las partes**, que pueden pedir
  **inclusiones o exclusiones**; el Magistrado-Presidente decide **de plano**.
- **53.2:** ⭐⭐ las partes cuyas peticiones **fueran rechazadas** «podrán formular **PROTESTA a los
  efectos del recurso** que haya lugar contra la sentencia».
- **53.3:** el Secretario **incorpora el escrito al acta**, entrega copia **a las partes y a cada
  jurado** y **hace constar las peticiones denegadas**.

**Protocolo en sala:**
1. **Llevar redactada la propia propuesta desde el auto del art. 37.** No se improvisa la última noche.
2. **Pedir inclusiones** de hechos favorables, **exención** (52.1.b) y **atenuación** (52.1.c) — **una
   a una y numeradas**.
3. **Pedir exclusiones** de párrafos que **mezclen** favorables y desfavorables (52.1.a), contengan
   **conceptos jurídicos** en vez de hechos o rompan la **prioridad lógica**.
4. **Rechazada cualquier petición → PROTESTA EXPRESA, EN EL ACTO y por CADA una.** No genérica:
   **identificada**.
5. **Verificar que consta en el acta** (53.3); si no consta, **exigirlo y protestar de nuevo**. El acta
   es la única prueba de la protesta ante el TSJ.

> Las dos llaves de la apelación: **37.d)** (prueba denegada) y **53.2** (objeto del veredicto).

---

## 7. Deliberación, veredicto y devolución — arts. 54 a 65

- **Art. 54 — instrucciones:** en **audiencia pública** y **en presencia de las partes** (54.1-54.2).
  ⭐ **54.3:** **no puede aludir a su opinión sobre el resultado probatorio**; **sí** debe advertir de
  **no atender a la prueba cuya ilicitud o nulidad haya declarado**; e **informar de que, si tras
  deliberar no pueden resolver sus dudas sobre la prueba, deben decidir EN EL SENTIDO MÁS FAVORABLE AL
  ACUSADO**.
  > ⭐ *In dubio pro reo* **con rango de instrucción legal expresa**. Si la omite o desliza su opinión,
  > **hacerlo constar y protestar en el acto**.
- **Art. 55:** preside inicialmente el primero del sorteo; **eligen portavoz**; deliberación **SECRETA**.
- **Art. 57:** ante **duda**, petición **por escrito** vía Secretario y comparecencia **en audiencia
  pública** con MF y partes (57.1). Pasados **2 días** sin acta, puede convocarles; si nadie expresa
  duda, emite las instrucciones del **art. 64.1 con los efectos de la devolución del acta** (57.2).
  > **Estar presente: la duda del jurado es información de oro, y la ampliación puede ser objeto de
  > protesta.**

### ⭐⭐ MAYORÍAS — arts. 59 y 60 — VERIFICADO Y CONFIRMADO (literal)

**Art. 59.1 — HECHOS**, párrafo por párrafo tal como fueron propuestos:

| | Votos (de 9) |
|---|---|
| Hechos **CONTRARIOS al acusado** | ⭐ **SIETE (7), al menos** |
| Hechos **FAVORABLES** | ⭐ **CINCO (5)** |

**Art. 60 — CULPABILIDAD** (si hubo mayoría en los hechos), por cada acusado y cada hecho delictivo:

| | Votos (de 9) |
|---|---|
| **CULPABILIDAD** | ⭐ **SIETE (7)** |
| **INCULPABILIDAD** | ⭐ **CINCO (5)** |
| **Remisión condicional** e **indulto** (60.3) | ⭐ **CINCO (5)** |

> ✅ **Confirmado literalmente el 2026-07-17.**
>
> ⭐ **Lectura estratégica:** la asimetría **7/5** es **favor rei estructural**. Para condenar hacen
> falta **siete**: **tres jurados bastan para impedir la culpabilidad**. La defensa no necesita
> convencer a la mayoría, **necesita tres**.

**59.2 — reintento:** sin mayoría, cabe votar el hecho **con las precisiones** de quien proponga la
alternativa, **hasta obtenerla**. Límites: **no** puede dejar de someterse a votación la parte
propuesta por el Magistrado-Presidente; cabe **párrafo nuevo** **si no supone alteración sustancial ni
agravación** de la responsabilidad imputada.

**Art. 61 — acta (síntesis; literal con `buscar_articulo`):** cinco apartados — **a)** hechos
**probados** (por unanimidad o mayoría; basta el número si se votó el texto propuesto, se transcribe si
se modificó); **b)** **no probados**; **c)** **culpable / no culpable**, con **pronunciamiento separado
por cada delito y acusado**, más remisión condicional e indulto; **d)** ⭐ **elementos de convicción**,
con «**una sucinta explicación de las razones**»; **e)** **incidentes**, sin romper el secreto **salvo
la negativa a votar**. Redacta el **portavoz** salvo que disienta del parecer mayoritario (61.2);
**firman todos** y **la negativa a firmar se hace constar** (61.3).

> ⭐ **La motivación del veredicto vive en el apartado d) y es exigible.** Un apartado d) vacío,
> tautológico o de mera remisión al conjunto de la prueba es **el motivo de apelación más frecuente**.
> **El alcance exigible de esa «sucinta explicación» es doctrina viva: `[verificar]` con
> `buscar_sentencias`.**

### ⭐ Devolución — arts. 63 a 65

**Causas (63.1) — CINCO:** **a)** no pronunciarse sobre **la totalidad de los hechos**; **b)** no
hacerlo sobre **culpabilidad o inculpabilidad de todos los acusados** y **todos los hechos delictivos**;
**c)** **no obtenerse la mayoría**; **d)** **pronunciamientos CONTRADICTORIOS** (entre hechos probados,
o entre culpabilidad y hechos probados); **e)** **defecto relevante en la deliberación y votación**.

- **63.2:** hecho **no propuesto** que implique **alteración sustancial** o **responsabilidad más
  grave** → ⭐ **se tiene por NO PUESTO**.
- **63.3:** ⭐ **antes de devolver se procede conforme al ART. 53** → **segunda ventana para pedir
  inclusiones/exclusiones y PROTESTAR. No dejarla pasar.**
- **Art. 64:** al devolver, **constituido el Tribunal y en presencia de las partes**, se **explican las
  causas** y se **precisa cómo subsanar**.
- **⭐ Art. 65:** tras una **TERCERA devolución** sin subsanar o sin mayorías → **Jurado DISUELTO y
  nuevo juicio con nuevo Jurado** (65.1). Si el **segundo** Jurado **tampoco obtiene veredicto** →
  **disolución y SENTENCIA ABSOLUTORIA** (65.2).
  > **Jurado colgado dos veces = absolución.** Con la asimetría 7/5, la defensa tiene una **segunda vía
  > de victoria** que no pasa por convencer a nadie: **impedir los siete, dos veces**.

---

## 8. Sentencia y recursos

**Art. 70:** se dicta en la forma del **art. 248.3 LOPJ**, incluyendo **como hechos probados y delito el
contenido del VEREDICTO** (70.1). ⭐ **70.2:** si el veredicto es de **culpabilidad**, la sentencia
**concretará la existencia de PRUEBA DE CARGO exigida por la presunción de inocencia** — motivación
**añadida y propia del jurado**; su ausencia o carácter formulario es **motivo de recurso**. **70.3:**
se le **une el acta del Jurado**.

### ⚠️ 8.1 Apelación ante el TSJ — art. 846 bis a) y ss. LECrim

- Las sentencias del **Magistrado-Presidente** en el ámbito de la AP son apelables ante la **Sala de lo
  Civil y Penal del TSJ**.
- ⛔ **`[verificar]` — PLAZO y MOTIVOS. No verificables en esta pasada:** `buscar_articulo` **no indexa
  la numeración con letra «846 bis a)» / «846 bis c)»** (devuelve «no encuentro el artículo 846 bis»;
  probadas todas las variantes). **Este apartado NO afirma plazo ni elenco de motivos.**
- **Lo único seguro:** los **motivos del 846 bis c) son TASADOS**; **no es segunda instancia plena**, y
  **varios motivos exigen haber formulado PROTESTA u OPOSICIÓN en su momento** (§ 4.2 y § 6). **Sin
  protesta, el motivo no existe.**
- **Antes de preparar o interponer:** verificar los **arts. 846 bis a) a f)** en el BOE consolidado
  (`https://www.boe.es/buscar/act.php?id=BOE-A-1882-6036`) o con `buscar_boe`, y contrastar con
  `buscar_sentencias`. **Decírselo al usuario: está pendiente.**

### 8.2 Casación — art. 847 LECrim ✅ verificado (anclas § 4)

Contra la **sentencia de apelación del TSJ**, casación ante la **Sala Segunda** por **infracción de ley
Y quebrantamiento de forma** (**847.1.a.1.º**) — ⭐ **ambos motivos**, a diferencia de las sentencias de
apelación de las AP (847.1.b), donde **solo** cabe el 849.1.º. **847.2:** exceptuadas las que **se
limiten a declarar la nulidad**. **Preparación: 5 días** (art. 856).

> **Itinerario privilegiado:** AP → **TSJ** → **TS** (casación con los dos motivos). **La protesta desde
> la primera sesión es lo que mantiene vivo todo el recorrido.**

---

## 9. ⭐ Comunicación con un tribunal LEGO

1. **RELATO, no dogmática.** El jurado no decide tipicidad: decide **si pasó o no pasó** (52.1.a). La
   subsunción es del Magistrado-Presidente.
2. **Lenguaje llano.** Prohibido: *iter criminis*, *animus necandi*, dolo eventual, *in dubio pro reo*
   **en latín**, «elemento subjetivo del injusto». Se dice: «quería matarlo», «se lo imaginó y le dio
   igual», «si hay dudas, hay que absolver».
3. **Una idea por frase. Una tesis por caso.** Las defensas alternativas en cascada funcionan ante un
   juez técnico y **destruyen la credibilidad ante un jurado**. Elegir.
4. **Explotar el art. 45:** la primera versión que oye el jurado **ancla**. Prepararla con más cuidado
   que el informe final.
5. **Aritmética, no unanimidad:** **impedir siete**, no convencer a nueve. **Tres** bloquean; **dos
   jurados colgados = absolución** (65.2). Diseñar para el jurado **escéptico**, no para el hostil.
6. **Escuchar las preguntas (46.1) y las dudas (57):** única señal de lo que piensan.
7. **El objeto del veredicto se escribe para quien lo va a leer:** frases cortas, **un hecho por
   párrafo** — que es lo que **exige el 52.1.a)**.

---

## 10. Datos, entregable y reglas de la casa

- **Cero datos reales.** Marcadores: **`[ACUSADO]`**, **`[VÍCTIMA]`**, **`[ENTIDAD]`**, **`[CIF]`**,
  **`[REPRESENTANTE]`**. **Art. 10 RGPD** (infracciones y condenas): los delitos del art. 1 LOTJ son
  **los de mayor exposición mediática del ordenamiento**. **Nunca** el slug con el nombre del acusado o
  la víctima → `descriptor-delito-año` (`PROTECCION-DATOS.md`). Config:
  `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.
- **Entregable: Word `.docx`** (skill **`docx`**) para LexNET; estilo `estilo-escritos-judiciales`;
  toda afirmación de hecho **anclada al folio**.
- Análisis → `matters/<slug>/jurado-estrategia.md`: 1) **competencia** (catálogo literal del 1.2;
  conexidad; exclusión por AN o Fiscalía Europea); 2) **hitos** (24, 25, 27, 30, 36, 37) y **control del
  art. 324 LECrim**; 3) **mapa del 46.5** — testigos que se retractan y **testimonios a llevar
  físicamente**; 4) **objeto del veredicto propuesto**, párrafo a párrafo; 5) **lista de PROTESTAS**
  (37.d, 53.2, 63.3); 6) **aritmética** — dónde están los tres votos; 7) **`[verificar]`** pendientes,
  **incluido siempre el art. 846 bis**.

**Reglas:** **(1)** nada del abreviado se calca (§ 0); el catálogo del 1.2 **se lee, no se recuerda**
—**no hay incendios forestales**. **(2)** **PROTESTA SIEMPRE**: oposición (37.d), protesta por cada
petición denegada **comprobando que consta en acta** (53.2-53.3), segunda ventana (63.3). **Sin
protesta no hay apelación.** **(3)** **Mayorías 7/5** verificadas: no redondear ni improvisar.
**(4)** **Ley penal en el tiempo** (art. 2 CP): redacción a la fecha de los hechos y comparación si la
posterior es más favorable (2.2); **LO 1/2026** desde **10-4-2026** (anclas § 7.3). **(5)** Nada de
jurisprudencia de memoria → `buscar_sentencias` o `[verificar]`. **Pendientes hoy:** arts. **38 y 39
LOTJ**, **846 bis a) y c) LECrim**, **remisión del 48.2 al art. 793 LECrim** y **conexidad**.
