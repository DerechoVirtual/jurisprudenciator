---
name: impugnacion-disposiciones-generales-ca
description: Impugnación de reglamentos, ordenanzas municipales, planes y demás disposiciones de carácter general — recurso directo (art. 46.1 LJCA), recurso indirecto contra actos de aplicación (art. 26 LJCA), cuestión de ilegalidad (arts. 27 y 123-126 LJCA) y efectos erga omnes de la sentencia anulatoria (art. 72.2 LJCA). Activar con "recurrir un reglamento", "impugnar una ordenanza", "recurso contra el plan general", "recurso indirecto", "cuestión de ilegalidad", "la ordenanza es ilegal", "se me pasó el plazo para recurrir el reglamento", "atacar la norma en que se basa la multa", "anular el plan urbanístico", "efectos erga omnes de la anulación".
---

# Impugnación de disposiciones generales (arts. 26, 27, 72 y 123-126 LJCA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Disposición estatal impugnada: texto, boletín y fecha (plazo del recurso directo)** → `buscar_boe` + `leer_boe`, o `sumario_boe` del día de publicación.
- **Ordenanza municipal impugnada** → `buscar_ordenanzas` + `leer_ordenanza` con `articulo` para cada precepto que se ataca.
- **Preceptos procesales** → `buscar_articulo` (`ley="LJCA"`, artículos 8, 21, 26, 27, 72, 81 y 123 a 126 y 129; `ley="LPAC"`, artículos 47 y 112).
- **Trámites esenciales de elaboración** → `buscar_articulo` (`ley="LPAC"`, `articulo="133"`; `ley="Ley 50/1997"`, `articulo="26"` para normas estatales; `ley="LBRL"`, `articulo="49"` para ordenanzas).
- **Efectos de la anulación, cosa juzgada del directo desestimado y art. 73** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Reserva de ley y jerarquía normativa** → `buscar_sentencias` (`base="TC"`); **vulneración del Derecho de la UE** → `buscar_sentencias` (`base="TJUE"`) y `buscar_articulo` con la norma europea.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

---

Plazos y cifras: `references/anclas-normativas-ca.md`. Lo que no esté allí, verifícalo con
`buscar_articulo` antes de escribirlo o márcalo `[verificar]`.

> ⚠️ **La decisión que define el asunto: ¿directo o indirecto?** El directo **caduca a los 2 meses
> desde la publicación** (art. 46.1) y no se recupera. El **indirecto no tiene plazo propio**: nace con
> cada acto de aplicación. Ante un reglamento lesivo publicado hace años, la respuesta casi nunca es
> «es tarde» — es **esperar o provocar el acto de aplicación y atacar por el art. 26**.

---

## 1. Bloque previo

1. **¿Es disposición general?** Norma que innova el ordenamiento y no se agota con su aplicación.
   Distinguir de acto general de destinatario plural (convocatoria, bases, deslinde), instrucción y acto
   plúrimo. La calificación decide plazo, cauce y efectos: si es acto, no hay art. 26 que valga.
2. **Fecha y boletín de publicación.** El directo corre desde el **día siguiente** (art. 46.1).
3. **¿Hay acto de aplicación?** Si lo hay, hay indirecto. Si no, y el directo caducó, evaluar
   **provocarlo** (solicitud cuya denegación se funde en la norma, autoliquidación e impugnación).
4. **Competencia** (art. 8, verificado): art. 8.1 — los Juzgados conocen de actos de entidades locales
   **excluidas las impugnaciones de cualquier clase de instrumentos de planeamiento urbanístico** → el
   planeamiento va a la **Sala del TSJ**; error de competencia que cuesta el asunto. Art. 8.3 — los
   Juzgados sí conocen de **disposiciones** de la Administración periférica del Estado y de las CCAA,
   con sus excepciones (> 60.000 €, dominio público, obras públicas, expropiación, propiedades
   especiales). El resto va a Sala: confirmar órgano con los arts. 10-12.
5. **Legitimación** (art. 19): en el directo el interés legítimo debe ser real — no basta el interés en
   la legalidad; corporaciones, colegios y asociaciones son la vía habitual. En el indirecto la da la
   condición de destinatario del acto: **mucho más cómoda**.
6. **Procurador preceptivo ante órganos colegiados** (art. 23.2) — y el directo suele ir a Sala.
7. **⚠️ Cautelar** (art. 129.2): la **suspensión de la vigencia** de los preceptos debe pedirse **en el
   escrito de interposición o en el de demanda**; fuera de ahí **precluye**. Ver `medidas-cautelares-ca`.
8. **Art. 45.2.d)** — **acuerdo corporativo** de la persona jurídica. Causa de inadmisión evitable nº 1.

---

## 2. Directo vs. indirecto

| | **Directo** | **Indirecto** (art. 26) |
|---|---|---|
| Objeto | La disposición | El **acto de aplicación**, fundado en que la disposición no es conforme a Derecho |
| Plazo | **2 meses** desde el día siguiente a la publicación (art. 46.1) | El del **acto** (2 meses expreso / 6 presunto). **La norma no tiene plazo propio** |
| Si el directo caducó | No cabe | **Cabe igual** (art. 26.2) |
| Si el directo se desestimó | Cosa juzgada sobre lo resuelto | **Cabe igual** (art. 26.2) |
| Qué anula | La disposición, erga omnes (art. 72.2) | Solo el **acto**, salvo art. 27 |
| Apelación | Reglas generales (art. 81.1) | **SIEMPRE apelable**, con independencia de la cuantía (art. 81.2.d, verificado) |

**Art. 26 verificado.** *26.1:* «Además de la impugnación directa [...] también es admisible la de los
actos que se produzcan en aplicación de las mismas, **fundada en que tales disposiciones no son
conformes a Derecho**.» *26.2:* «**La falta de impugnación directa de una disposición general o la
desestimación del recurso que frente a ella se hubiera interpuesto no impiden la impugnación de los
actos de aplicación** con fundamento en lo dispuesto en el apartado anterior.»

> **Táctica del art. 26.2:** la firmeza de un reglamento **no sana su ilegalidad**. Ni dejar pasar el
> directo ni perderlo cierran el indirecto. Decírselo al cliente: el reglamento no es inatacable por
> viejo.
> **Límite honesto:** el indirecto se funda en la **ilegalidad de la disposición**, no en vicios propios
> del acto ni en discrepancia. Y el alcance de la cosa juzgada cuando el directo se desestimó es
> **jurisprudencial**: verificar con `buscar_sentencias`, no afirmarlo de memoria.

**Parte demandada** (art. 21.4, verificado): quien funda su pretensión en la ilegalidad de una
disposición general debe demandar **también a la Administración autora de la disposición**, aunque no
proceda de ella la actuación recurrida (p. ej. el Pleno junto a la Alcaldía que sancionó). Omitirlo
genera problemas de emplazamiento e indefensión.

---

## 3. Cuestión de ilegalidad (arts. 27 y 123-126) — el punto que más se confunde

**Art. 27 verificado:**
- **27.1 (regla).** Juez o Tribunal que dicta **sentencia firme estimatoria** por considerar **ilegal el
  contenido de la disposición aplicada** → **deberá plantear** la cuestión ante el Tribunal competente
  para el **recurso directo**, salvo 27.2 y 27.3.
- **27.2.** Si ese órgano **era también competente para el directo**, **no plantea nada**: **su propia
  sentencia declarará la validez o nulidad** de la disposición. *Este es el apartado que se confunde.*
- **27.3.** **Sin necesidad de cuestión**, el **TS anulará** cualquier disposición general cuando, **en
  cualquier grado**, conozca de un recurso contra un acto fundado en la ilegalidad de la norma.

> **Decisión en tres pasos.** (1) ¿Sentencia estimatoria **firme** fundada en la ilegalidad del
> reglamento? (2) ¿El órgano sería competente para el **directo**? → **Sí: anula él (27.2). No: plantea
> (27.1).** (3) ¿Es el **TS**? → anula él sin cuestión (27.3).
> **Calendario:** en el escenario 27.1 la plantea **el órgano de oficio**, **tras la firmeza**. El
> despacho no la interpone: la prepara argumentalmente en la demanda y **comparece** en ella.

| Trámite | Regla verificada |
|---|---|
| Planteamiento | **Auto**, dentro de los **5 días** siguientes a que conste la **firmeza** (art. 123.1) |
| Alcance | **Ceñida exclusivamente** a los preceptos cuya ilegalidad **sirvió de base a la estimación** (art. 123.1) |
| Recurso contra el auto | **Ninguno** (art. 123.1) |
| Personación | **15 días** para comparecer y alegar. **Transcurrido, no se admitirá la personación** (art. 123.2) ⚠️ preclusión dura: calendar el día 1 |
| Publicidad | Remisión urgente de certificación, autos y expediente (124.1); **publicación del auto de planteamiento** en el mismo periódico oficial de la disposición (124.2) |
| Sentencia | **10 días** desde que se declare concluso (125.2); cabe **rechazo en admisión**, por auto y **sin audiencia**, si faltan condiciones procesales |
| Interrupción | Si se reclama el **expediente de elaboración** o hay prueba de oficio; audiencia común de **5 días** (125.3) |
| Preferencia | Tramitación **preferente** si es de especial trascendencia para otros procedimientos (126.4) |

**Art. 126:** estima/desestima total o parcialmente, o inadmite por requisito procesal insubsanable
(126.1); se le aplican los arts. **33.3, 66, 70, 71.1.a), 71.2, 72.2 y 73**, y se publican también las
firmes **desestimatorias** (126.2).

> **126.5 — la clave para el cliente:** «La sentencia que resuelva la cuestión de ilegalidad **no
> afectará a la situación jurídica concreta derivada de la sentencia dictada por el Juez o Tribunal que
> planteó aquélla**.» **El cliente ya ganó y no pierde nada** aunque la cuestión se desestime. Mira al
> futuro, no a su caso. **No** vender la cuestión como un riesgo para lo obtenido.

---

## 4. Efectos de la sentencia (art. 72, verificado)

- **72.1** — Inadmisibilidad o desestimación: **solo efectos entre las partes**. Un reglamento
  «confirmado» frente a otro no vincula al despacho (art. 26.2).
- **72.2** — «La **anulación** de una disposición o acto producirá efectos **para todas las personas
  afectadas**. Las sentencias firmes que anulen una disposición general tendrán **efectos generales
  desde el día en que sea publicado su fallo y preceptos anulados en el mismo periódico oficial** en que
  lo hubiera sido la disposición anulada.» También se publican las firmes que anulen un acto que afecte
  a **pluralidad indeterminada**. → **Dos consecuencias:** el erga omnes nace con la **publicación del
  fallo**, no con la sentencia (no darlo por operativo antes); y hay que **exigir la publicación en
  ejecución** si la Administración se demora.
- **72.3** — El reconocimiento o restablecimiento de **situación jurídica individualizada** solo produce
  efectos **entre las partes**, salvo **extensión de efectos** de los arts. 110-111 (personal y
  tributaria — ver `ejecucion-sentencias-ca`).

> **Para el cliente:** ganar el **indirecto** anula **su acto**; no borra el reglamento (salvo 27.2/27.3).
> Ganar el **directo** o la cuestión expulsa la norma erga omnes desde la publicación del fallo. Si el
> objetivo es tumbar la norma para todo el sector, el indirecto **solo** no basta.
> **Efectos sobre situaciones consumadas y actos firmes anteriores (art. 73):** jurisprudencia viva y
> matizada — verificar con `buscar_sentencias` **antes de prometer la revisión de lo firme**.

---

## 5. Motivos de nulidad

**Art. 47.2 LPAC (verificado).** ⚠️ **Aviso de cita: el art. 47.2 NO está dividido en letras** — las
letras a)-g) son del **47.1**, referido a los **actos**. Citar «art. 47.2.a)» es un error: se cita
**«art. 47.2 LPAC»** a secas o se transcribe el inciso. Son nulas de pleno derecho las disposiciones que:

1. **Vulneren la Constitución, las leyes u otras disposiciones administrativas de rango superior** →
   jerarquía normativa. Motivo estrella: confrontar preceptos **uno a uno**, no en bloque.
2. **Regulen materias reservadas a la Ley** (típico en sancionador y tributario).
3. **Establezcan la retroactividad de disposiciones sancionadoras no favorables o restrictivas de
   derechos individuales**.

Motivos de construcción jurisprudencial o de la norma habilitante — **desarrollar con la ley en la mano**:

4. **Ultra vires** — exceso sobre la habilitación legal: citar la **norma habilitante concreta**.
5. **Falta de competencia** del órgano, y vicios en la formación de la voluntad del órgano colegiado
   (convocatoria, quórum, orden del día).
6. **Omisión de trámites esenciales de elaboración**: audiencia e información pública, informes
   preceptivos, memoria del análisis de impacto normativo, informe de secretaría/intervención en el
   ámbito local. ⚠️ Esto **no se rige por el art. 47.2** sino por la norma que regula el procedimiento en
   cada nivel: **verificar el precepto exacto con `buscar_articulo`**; para el nivel autonómico/local,
   pedir la norma al usuario. Marcar `[verificar]` lo no confirmado.
7. **Vulneración del Derecho de la UE** (primacía, efecto directo).
8. **Arbitrariedad / falta de justificación** de la potestad reglamentaria (art. 9.3 CE).

> **Método:** el **expediente de elaboración** es la mina — pedirlo siempre; en la cuestión, el Tribunal
> puede reclamarlo para mejor proveer (art. 125.3). Los vicios de procedimiento se prueban con el
> expediente, no con adjetivos.

---

## 6. Ordenanzas y normativa autonómica — cómo obtener el texto

- **Municipios cubiertos:** `buscar_ordenanzas` → `leer_ordenanza`. **Comprobar la cobertura** antes de
  darla por hecha.
- **Municipios no cubiertos y toda la normativa AUTONÓMICA:** el conector **no la cubre**. **Pedir el
  texto al usuario** y **no citarla de memoria**. En urbanismo y actividades es la regla: la ley del
  suelo aplicable es casi siempre autonómica.
- **Estatal:** `buscar_articulo` / `buscar_boe`.
- Citar la disposición con boletín, fecha, número y **precepto exacto**. Si solo se atacan algunos
  preceptos, **decir cuáles**: el art. 123.1 ciñe la cuestión a los que fundaron la estimación.

---

## 7. Estructura y SUPLICO

1. **Encabezamiento** (¡competencia, § 1.4!); calificación expresa como **recurso directo** o **recurso
   contra acto de aplicación con impugnación indirecta del art. 26**.
2. **Objeto preciso:** disposición (boletín, fecha, preceptos) y, en el indirecto, también **el acto**.
3. **Demandados:** autor del acto **y** autor de la disposición (art. 21.4).
4. **HECHOS** con folio (`(doc. núm. X, folio Y)`), incluida la publicación y el expediente de elaboración.
5. **FUNDAMENTOS PROCESALES:** jurisdicción, competencia, legitimación, **plazo** — en el indirecto
   invocar el **art. 26.2** de entrada, para blindar frente a la extemporaneidad que se opondrá; art. 45.2.
6. **FONDO:** un ordinal **por precepto atacado y por motivo** (§ 5), con confrontación literal.
7. **SUPLICO** y **OTROSÍES:** cautelar (⚠️ art. 129.2: aquí o en la demanda, o precluye); prueba;
   petición del **expediente de elaboración**.

**Reparto para la redacción rápida:** encabezamiento, objeto, demandados y hechos con folio (una sección) · fundamentos procesales, con el art. 26.2 de entrada en el indirecto (una sección) · una sección por precepto atacado o por motivo (§ 5), con confrontación literal · cierre con suplico según el escenario del § 3 y otrosíes (cautelar del art. 129.2, prueba, expediente de elaboración).

**Directo:**

> **SUPLICO A LA SALA** que [...] tenga por interpuesto **recurso contencioso-administrativo directo**
> contra **[los arts. X, Y y Z de la DISPOSICIÓN]**, aprobada por **[ÓRGANO]** y publicada en
> **[BOLETÍN]** de **[FECHA]**, y dicte sentencia que **declare la nulidad de pleno derecho** de dichos
> preceptos, con **publicación del fallo** conforme al **art. 72.2 LJCA**, e imposición de costas.

**Acto de aplicación con impugnación indirecta:**

> **SUPLICO** [...] tenga por interpuesto recurso contra **[ACTO]**, de **[ÓRGANO]**, de **[FECHA]**, y,
> **por vía de impugnación indirecta del art. 26 LJCA**, contra **[los arts. X e Y de la DISPOSICIÓN]**
> en que se funda, y dicte sentencia que: **1.º) anule el acto** por fundarse en preceptos no conformes
> a Derecho; **2.º) [si el órgano es competente para el directo]** conforme al **art. 27.2 LJCA**,
> **declare la nulidad** de dichos preceptos; **[en otro caso]** acuerde, firme la sentencia, el
> **planteamiento de la cuestión de ilegalidad** del **art. 27.1 LJCA**; **3.º)** con costas.

- Redactar el ordinal 2.º **según el escenario del § 3**, no los dos. Si el órgano es el TS, invocar el
  **art. 27.3**.
- La cuestión **no se suplica como pretensión autónoma**: la plantea el órgano de oficio tras la firmeza
  (art. 123.1). El escrito la **anticipa y facilita** identificando con precisión los preceptos, porque
  el auto se ceñirá a ellos.

## 8. Reglas de la casa

- **Protección de datos:** cero datos reales. `[CLIENTE]`, `[ÓRGANO]`, `[DOMICILIO]`, `[FECHA]`, `[IMPORTE]`.
- **Jurisprudencia:** aquí es **decisiva** (efectos de la anulación, art. 73, cosa juzgada del directo
  desestimado, control de la potestad reglamentaria). **Prohibido citar ECLI/ROJ/fecha/ponente de
  memoria.** `buscar_sentencias` para localizar, `buscar_por_cita` para verificar. Lo no verificado se
  marca `[verificar]` y se dice.
- **Normativa autonómica y local:** § 6. Pedírsela al usuario.
- **Nada de MASC:** es del orden **civil**; no existe en esta jurisdicción.
- **Entregable:** Word `.docx` maquetado, que genera el ensamblado de `redaccion-rapida`.
