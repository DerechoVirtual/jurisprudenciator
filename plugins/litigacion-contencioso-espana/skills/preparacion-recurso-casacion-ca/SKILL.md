---
name: preparacion-recurso-casacion-ca
description: Redacta el escrito de PREPARACIÓN del recurso de casación contencioso-administrativo ante la Sala de instancia, para su admisión por la Sala Tercera del TS por interés casacional objetivo (arts. 86-89 LJCA). Activar con "preparar casación contencioso", "interés casacional objetivo", "recurso de casación Sala Tercera", "casación contra sentencia del TSJ", "recurso de queja casación".
---

# Preparación del recurso de casación contencioso-administrativo (arts. 86-89 LJCA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Recurribilidad, plazos y los seis requisitos** → `buscar_articulo` (`ley="LJCA"`, artículos 86 a 89, 92 y 93).
- **Doctrina de admisión de la Sección Primera** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`, `tipo_resolucion="AUTO"`, `consulta` con la cuestión de interés casacional) + `opciones_busqueda` para acotar por sección o año.
- **Jurisprudencia infringida o contradictoria** → `buscar_por_cita` + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión).
- **Letra e): carácter estatal o de la UE de la norma infringida** → `buscar_articulo` o `buscar_boe` + `leer_boe`; `buscar_sentencias` (`base="TJUE"`) si se invoca Derecho de la Unión.
- **Antes de presentar** → `verificar_escrito` sobre los seis apartados.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

---

Redacta el escrito de **preparación** ante la **Sala de instancia**. Plazos y cifras:
`references/anclas-normativas-ca.md`. Lo no anclado, verificarlo con `buscar_articulo` o marcarlo
`[verificar]`.

> ⚠️ **Es casación CONTENCIOSA** — modelo de **interés casacional objetivo** tras la **LO 7/2015**.
> **No es casación civil.** No importar motivos tasados, cuantías, ni el régimen de la LEC. No hay
> «motivos» del art. 88 LEC: hay **infracción + interés casacional objetivo**.
>
> ⚠️ **La preparación NO es un trámite.** Es el escrito que decide el recurso. Un defecto aquí se paga
> con un auto teniendo por **no preparado** (art. 89.4), recurrible **solo en queja**.

---

## 1. Bloque de recurribilidad y plazo — cerrar ANTES de redactar

1. **¿Es recurrible la resolución?** Sentencias y **determinados autos**: **art. 87** LJCA.
   **Verificar el apartado exacto con `buscar_articulo` antes de afirmarlo** — no darlo por sabido.
   Comprobar también el **art. 86** (qué sentencias, de qué órganos, y la regla de las sentencias de
   los Juzgados). Si el asunto viene de un **TSJ**, ver además § 3, letra e).
2. **⚠️ Plazo: 30 DÍAS** desde el día siguiente al de la notificación de la resolución recurrida
   (art. 89.1, verificado), **ante la Sala de instancia** — la que dictó la resolución (TSJ, AN…),
   **NO ante el Tribunal Supremo**.
3. **⚠️ Si no se prepara en plazo (art. 89.3, verificado):** la sentencia o auto **queda firme**, y así
   lo declara el **Letrado de la Administración de Justicia mediante decreto**. Contra esa decisión
   **solo cabe el recurso directo de revisión del art. 102 bis** LJCA. No hay rescate.
4. **Legitimación (art. 89.1):** quienes hayan sido **parte en el proceso, o debieran haberlo sido**.
5. **Agosto NO corre** (art. 128.2) — salvo procedimiento de **derechos fundamentales**, donde agosto
   **es hábil**. ⚠️ Si la sentencia se dictó en DDFF, **el plazo de 30 días corre en agosto**.
   Comprobar el cauce antes de computar. Caducidad: no se interrumpe por nada.
6. **Procurador preceptivo** (órgano colegiado, art. 23.2 LJCA), tanto ante la Sala a quo como ante el TS.

---

## 2. ⚠️ SON SEIS REQUISITOS — art. 89.2 LJCA (texto verificado)

> **Encabezamiento imperativo del precepto:** «El escrito de preparación deberá, **en apartados
> separados que se encabezarán con un epígrafe expresivo de aquello de lo que tratan**: …»
>
> **Esto no es estilo: es forma legal.** Seis apartados, cada uno con su **epígrafe expresivo**. Un
> escrito corrido, sin epígrafes, o que funda dos requisitos en un mismo apartado, se expone al
> art. 89.4. **Reproducir la letra del artículo en el epígrafe** es la práctica segura.

| | Requisito (art. 89.2) |
|---|---|
| **a)** | **Acreditar** el cumplimiento de los requisitos **reglados**: **plazo**, **legitimación** y **recurribilidad** de la resolución impugnada. |
| **b)** | **Identificar con precisión** las **normas o la jurisprudencia** que se consideran **infringidas**, **justificando** que fueron **alegadas en el proceso**, o **tomadas en consideración** por la Sala de instancia, o que ésta **hubiera debido observarlas aun sin ser alegadas**. |
| **c)** | ⚠️ **Acreditar, si la infracción imputada lo es de normas o de jurisprudencia relativas a los ACTOS O GARANTÍAS PROCESALES que produjo INDEFENSIÓN, que se pidió la SUBSANACIÓN de la falta o transgresión EN LA INSTANCIA, de haber existido momento procesal oportuno para ello.** |
| **d)** | **Justificar** que la o las infracciones imputadas han sido **relevantes y determinantes de la decisión adoptada** en la resolución que se pretende recurrir. |
| **e)** | **Justificar**, si la resolución fue dictada por la **Sala de lo Contencioso-administrativo de un TSJ**, que la norma supuestamente infringida forma parte del **Derecho estatal o del de la Unión Europea**. |
| **f)** | **Especialmente**, **fundamentar con singular referencia al caso** que concurre alguno de los supuestos que, con arreglo a los **apartados 2 y 3 del art. 88**, permiten apreciar el **interés casacional objetivo** y la conveniencia de un pronunciamiento de la Sala Tercera del TS. |

### 2.1 ⚠️ La letra c) — el requisito que se olvida

**Es el requisito silencioso que más recursos mata.** Se olvida porque solo se activa en un supuesto
concreto, y precisamente por eso nadie lo tiene presente cuando ese supuesto concurre.

- **Cuándo se activa:** siempre que **alguna** de las infracciones que se imputan sea de **normas o
  jurisprudencia relativas a actos o garantías procesales** y **se alegue que produjo indefensión**.
  Típicamente: prueba denegada, incongruencia, falta de emplazamiento, defectos de notificación,
  irregularidades de la vista, vulneración del art. 24 CE en el proceso.
- **Qué exige:** **acreditar** —no afirmar— que **se pidió la subsanación de la falta o transgresión
  EN LA INSTANCIA**, **de haber existido momento procesal oportuno** para ello.
- **Cómo se acredita:** citando el **escrito, la protesta o el recurso concreto** con el que se pidió la
  subsanación, **con su fecha y su folio de los autos**. Protesta en el acto de la vista, recurso de
  reposición contra la denegación de prueba, escrito de subsanación, incidente de nulidad. **Sin folio,
  no está acreditado.**
- **Si no hubo momento procesal oportuno:** **decirlo y razonarlo expresamente** en el apartado c). El
  precepto lo contempla («de haber existido momento procesal oportuno»). **Lo que no cabe es callar.**
- **⚠️ Consecuencia de omitirlo:** el escrito no cumple el art. 89.2 → **auto motivado teniendo por NO
  PREPARADO** el recurso (art. 89.4), **denegando el emplazamiento** y la remisión al TS. **Solo queja.**
  Y el art. 93 contempla expresamente, entre las causas de inadmisión, el supuesto de que «siendo
  necesario haber pedido la subsanación de la falta, no hay constancia de que se haya hecho».
- **Regla operativa:** al preparar cualquier casación, **preguntar siempre**: ¿hay algún motivo
  procesal con indefensión? Si la respuesta es sí —o dudosa—, **abrir el apartado c) igualmente** y
  documentarlo. Un apartado c) sobrante no perjudica; su ausencia es letal.
- **Trabajo hacia atrás:** esto se prepara **en la instancia**. Si el asunto puede llegar a casación,
  **protestar y pedir subsanación siempre y por escrito**, y anotar el folio. Ver `recurso-apelacion-ca`.

## 3. Notas sobre las demás letras

- **a)** No basta afirmar que se está en plazo: **acreditar** con la fecha de notificación y el cómputo.
  Incluir la recurribilidad con cita del **art. 86/87** verificado.
- **b)** «Identificar **con precisión**»: artículo, apartado y **letra**. No vale «los arts. 47 y ss.».
  Y **justificar el pasaporte procesal** de cada norma: alegada, tomada en consideración por la Sala, o
  que debió observarse de oficio. **Norma no alegada y no justificada = motivo perdido.**
- **d)** El **juicio de relevancia** es un razonamiento, no una fórmula: explicar que **sin** la
  infracción **el fallo habría sido otro**. Si la sentencia tiene una *ratio* alternativa e
  independiente que sostiene el fallo, la infracción **no** es determinante — y hay que atacar **todas**
  las *rationes*.
- **e)** Solo si viene de un **TSJ**: justificar que la norma infringida es **estatal o de la UE**.
  ⚠️ Es una **trampa de materia**: si el pleito se resolvió aplicando **Derecho autonómico**, la vía se
  cierra. Buscar el anclaje real en norma estatal o de la UE, o en jurisprudencia estatal — sin forzarlo.
  Un anclaje artificial se detecta y hunde el recurso.
- **f)** El **corazón** del escrito. Ver § 4.

## 4. Interés casacional objetivo — art. 88 (apartados 2 y 3)

- **Verificar SIEMPRE la letra y el apartado exactos con `buscar_articulo`** antes de invocarlos. El
  art. 88.2 contiene **circunstancias** de las que **puede** apreciarse interés casacional; el art. 88.3,
  **presunciones**. **No citar de memoria «la letra c) del 88.2»**: comprobarlo. Si no se ha verificado,
  marcar `[verificar]` y decirlo.
- **«Con singular referencia al caso»** (art. 89.2.f) es una exigencia literal y el filtro real de la
  Sección de Admisión: no basta transcribir el supuesto legal. Hay que **conectarlo con los hechos y la
  ratio concretos** de la sentencia. Un apartado f) genérico = inadmisión.
- **Distinguir dos planos y no mezclarlos:** el **interés casacional** es una cuestión de **utilidad
  para formar jurisprudencia**, no de justicia del caso. El escrito que solo dice «la sentencia es
  injusta» no prepara nada. Formular la **cuestión jurídica** de forma abstracta y susceptible de
  respuesta general.
- **Alegar los supuestos que realmente concurran**, no una lista. Tres invocaciones sólidas y
  desarrolladas valen más que ocho enunciadas.
- **⚠️ Jurisprudencia — crítico en casación:** la **doctrina de admisión** de la Sección Primera (autos
  de admisión) es el material decisivo **y el más peligroso de citar de memoria**. **Prohibido** citar
  ECLI, ROJ, fecha o ponente sin verificar con `buscar_sentencias` / `buscar_por_cita`. Un auto de
  admisión inventado o mal citado ante la propia Sala que lo dictó es un daño reputacional grave. Si no
  se verifica: `[verificar]` y decírselo al usuario.
- Si se invoca **contradicción** con otras sentencias, hay que **identificarlas verificadas** y explicar
  la identidad sustancial de supuestos.

## 5. Qué pasa después (arts. 89.4-89.6, verificado)

| Escenario | Consecuencia |
|---|---|
| **Cumple** el art. 89.2 | La Sala de instancia, por **auto motivado**, tiene por **preparado** el recurso y ordena el **emplazamiento de las partes ante la Sala Tercera del TS** para comparecer en **⚠️ 15 DÍAS** (art. 89.5), con remisión de autos y expediente. Si lo estima oportuno, emite **opinión sucinta y fundada** sobre el interés objetivo, que une al oficio de remisión. |
| **No cumple** el art. 89.2 | **Auto motivado teniendo por NO PREPARADO**, denegando emplazamiento y remisión. **Únicamente recurso de QUEJA**, sustanciado conforme a la **LEC** (art. 89.4). |
| Fuera de plazo | **Firmeza** por **decreto del LAJ**; solo **revisión del art. 102 bis** (art. 89.3). |
| Auto **teniendo por preparado** | La **parte recurrida no puede recurrirlo**, pero **puede oponerse a la admisión** al comparecer ante el TS, dentro del término del emplazamiento (art. 89.6). |

> # ⚠️ EL EMPLAZAMIENTO ANTE EL TS ES DE **15 DÍAS**, NO DE 30
>
> Lo cambió el **RD-ley 5/2023**, en vigor desde el **29-7-2023** (art. 89.5). La redacción anterior
> decía **treinta días**, y sigue viva en formularios, manuales y en la memoria de muchos despachos.
> **Son 15.** Calendar 15 días desde el emplazamiento para la **comparecencia** ante la Sala Tercera —
> y coordinarlo **desde ya** con el procurador ante el TS. Perder este plazo tira a la basura una
> preparación impecable.
>
> **No confundir los tres plazos:** preparación **30 días** ante la Sala a quo (art. 89.1) ·
> emplazamiento/comparecencia ante el TS **15 días** (art. 89.5) · interposición ante el TS tras la
> admisión → **verificar el plazo con `buscar_articulo` (art. 92)** antes de calendarlo.

## 6. Costas en casación — régimen PROPIO (art. 93.4, verificado)

⚠️ **No aplicar aquí el art. 139.2.** El art. 139.3 **remite al art. 93.4**, y este tiene regla propia:

- La sentencia resuelve sobre las **costas de la instancia** conforme al **art. 139.1** (vencimiento
  objetivo, salvo serias dudas razonadas), **con el tope del art. 139.4**: máximo **un tercio de la
  cuantía del proceso por cada favorecido**; cuantía indeterminada = **18.000 €** a esos solos efectos,
  salvo que el tribunal razone otra cosa por complejidad.
- Y, **en cuanto a las del recurso de casación**, dispone que **cada parte abone las causadas a su
  instancia y las comunes por mitad**. **No hay vencimiento objetivo en casación.**
- **Excepción:** puede imponerlas a una sola parte cuando la sentencia **aprecie y motive mala fe o
  temeridad**; imposición que **podrá limitar a una parte de ellas o hasta una cifra máxima**.
- **Nunca** al **Ministerio Fiscal** (art. 139.6).
- **Uso con el cliente:** el riesgo de costas **del recurso** es bajo (cada uno las suyas); el de la
  **instancia** sigue vivo y sujeto al tope del art. 139.4. Explicarlo así, por escrito, y no como
  «costas al que pierde».
- ⚠️ **Inadmisión:** verificar el régimen de costas del auto de inadmisión con `buscar_articulo`
  (art. 90) antes de informar al cliente.

## 7. Errores típicos que pierden el asunto

1. **⚠️ Omitir el apartado c)** cuando se imputa infracción procesal con indefensión → **no preparado**.
2. **Escribir cinco apartados** en lugar de **seis**, o fundirlos sin **epígrafes expresivos**.
3. **Contar 30 días para el emplazamiento ante el TS.** Son **15** desde el RD-ley 5/2023.
4. **Presentar la preparación ante el TS** en lugar de ante la **Sala de instancia**.
5. **Apartado f) genérico**, sin «singular referencia al caso» → inadmisión.
6. **Confundir interés casacional con injusticia del caso.**
7. **Invocar norma autonómica** frente a sentencia de un **TSJ** (letra e).
8. **Citar normas no alegadas** sin justificar el pasaporte de la letra b).
9. **No atacar todas las *rationes decidendi*** → la infracción no es determinante (letra d).
10. **Citar autos de admisión o STS de memoria.** Verificar o `[verificar]`.
11. **Creer que el auto de no preparación se apela**: solo **queja**.
12. **Aplicar el art. 139.2 a las costas de la casación** en vez del **art. 93.4**.
13. **Aplicar la inhabilidad de agosto** a una casación que viene de **DDFF**.

## 8. Anclaje al expediente y a los autos

- **Todo hecho afirmado va con folio**, con **doble anclaje**:
  `(doc. núm. X del expediente administrativo, folio Y)` y `(folio Z de los autos)`.
- **Crítico en el apartado c):** la petición de subsanación se acredita **con el folio de los autos**
  donde consta el escrito o la protesta, y su fecha. Sin folio, no hay acreditación.
- **Crítico en el apartado b):** la alegación de cada norma en la instancia se acredita con el folio de
  la demanda, del escrito de conclusiones o del de apelación. La casación se **construye desde la
  instancia**; si el asunto es casacionable, **dejar los folios preparados** desde el primer escrito.
- En el apartado d), citar el **fundamento jurídico por su número** al explicar la *ratio* combatida.

## 9. Estructura del escrito

1. **«A LA SALA DE LO CONTENCIOSO-ADMINISTRATIVO DEL [TSJ DE [CCAA] / AUDIENCIA NACIONAL]»** — la
   preparación se presenta **ante la Sala a quo**, no ante el TS. Procurador, representación, autos.
2. **Identificación de la resolución recurrida**: órgano, número, fecha y **fecha de notificación**.
3. **ANTECEDENTES** sucintos — solo lo necesario para entender la infracción y la *ratio*.
4. **SEIS APARTADOS SEPARADOS, CADA UNO CON EPÍGRAFE EXPRESIVO:**
   - *PRIMERO. — Cumplimiento de los requisitos reglados: plazo, legitimación y recurribilidad
     (art. 89.2.a LJCA).*
   - *SEGUNDO. — Identificación precisa de las normas y la jurisprudencia infringidas y justificación
     de su alegación o consideración en la instancia (art. 89.2.b LJCA).*
   - *TERCERO. — Acreditación de haberse pedido la subsanación en la instancia de las infracciones de
     actos o garantías procesales productoras de indefensión (art. 89.2.c LJCA).* ⚠️ **No omitir.**
   - *CUARTO. — Juicio de relevancia: carácter relevante y determinante del fallo de las infracciones
     imputadas (art. 89.2.d LJCA).*
   - *QUINTO. — Carácter estatal o de la Unión Europea de las normas infringidas (art. 89.2.e LJCA).*
   - *SEXTO. — Fundamentación, con singular referencia al caso, del interés casacional objetivo para la
     formación de jurisprudencia (art. 89.2.f, en relación con los arts. 88.2 y 88.3 LJCA).*
5. **SUPLICO.**
6. **OTROSÍES:** opinión del art. 89.5; designación de procurador ante el TS; documentos.

## 10. SUPLICO — modelo

> **SUPLICO A LA SALA** que, teniendo por presentado este escrito, se sirva admitirlo, tener por
> **PREPARADO** en tiempo y forma **RECURSO DE CASACIÓN** contra la sentencia núm. [X], de [FECHA],
> dictada en el procedimiento [Nº], al cumplirse los requisitos exigidos por el **art. 89.2 LJCA** en
> los seis apartados que anteceden, y, en consecuencia, dictar **auto motivado teniendo por preparado
> el recurso**, **ordenar el emplazamiento de las partes para su comparecencia en el plazo de QUINCE
> DÍAS ante la Sala de lo Contencioso-administrativo del Tribunal Supremo** y **remitir a ésta los
> autos originales y el expediente administrativo**, conforme al **art. 89.5 LJCA**.
>
> **OTROSÍ DIGO** que, conforme al **art. 89.5 LJCA** *in fine*, **SUPLICO** que la Sala tenga por
> oportuno emitir **opinión sucinta y fundada** sobre el interés objetivo del recurso para la formación
> de jurisprudencia, que se unirá al oficio de remisión.

- ⚠️ **El suplico de la preparación NO pide la anulación de la sentencia.** Pide **que se tenga por
  preparado** y **que se emplace ante el TS**. La pretensión de fondo (art. 31 LJCA: anulación +
  reconocimiento de situación jurídica individualizada + indemnización) se articula **en el escrito de
  interposición ante el TS**, ya admitido el recurso. **Confundir ambos suplicos delata el escrito.**
- Anticipar, no obstante, **la pretensión de fondo** al identificar la cuestión de interés casacional:
  el TS necesita ver a dónde lleva la respuesta que se le pide.

## 11. Reglas de la casa

- **Protección de datos:** cero datos reales. Marcadores `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`,
  `[IMPORTE]`, `[TERCERO]`.
- **Jurisprudencia:** **especialmente crítico aquí.** Verificar **toda** cita —STS, autos de admisión de
  la Sección Primera, doctrina de admisión— con `buscar_sentencias` / `buscar_por_cita` **antes** de
  incluirla. Prohibido inventar ECLI, ROJ, fecha, ponente o fundamento. Sin verificación: `[verificar]`.
- **Normativa autonómica y local:** el conector no la cubre. Pedírsela al usuario; no citarla de
  memoria. Y recordar que el Derecho autonómico **cierra** la vía casacional frente a sentencias de TSJ.
- **Nada de MASC:** requisito del orden civil; no existe aquí.
- **Entregable:** Word `.docx` maquetado (skill `docx`), con antecedentes, los **seis apartados con
  epígrafe** y el suplico.
