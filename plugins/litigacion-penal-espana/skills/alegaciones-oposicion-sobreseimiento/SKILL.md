---
name: alegaciones-oposicion-sobreseimiento
description: >-
  Redacta escritos de alegaciones de la acusación oponiéndose al archivo o sobreseimiento en fase de instrucción, ANTES de que el auto se dicte. Actívala ante "me van a archivar la causa", "el fiscal pide el sobreseimiento", "el fiscal no acusa", "existen indicios racionales de criminalidad", "no procede el archivo", "sobreseimiento libre o provisional", "traslado del art. 779", "superior jerárquico del fiscal", "art. 782", o cuando se dé traslado a la acusación para alegar sobre el archivo. Requisito previo: el auto de sobreseimiento NO se ha dictado todavía y aún se está a tiempo de alegar. Si el auto de archivo YA está dictado y notificado y corre el plazo de recurso, usar /recurso-reforma-apelacion-auto-archivo.
---

# Alegaciones de oposición al sobreseimiento / archivo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Cauce y clase de sobreseimiento** (arts. 637, 641, 642, 779, 780 y 782.2 LECrim) → `buscar_articulo` (`ley="LECrim"`) con el texto vigente de cada precepto.
- **Criterio de la Audiencia que resolverá una eventual apelación sobre indicios racionales y archivo prematuro** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="AP"`, `provincia` de la causa) + `leer_sentencias` con `parrafos=3` y `terminos` («indicios racionales de criminalidad», «sobreseimiento prematuro»).
- **Doctrina de la Sala Segunda sobre el art. 782.2 y la acusación que sostiene sola la causa** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.
- **Tutela judicial de la acusación frente a un archivo sin investigar** → `buscar_sentencias` (`base="TC"`, consulta sobre tutela judicial efectiva del denunciante y archivo prematuro).
- **Resoluciones que invoque el Fiscal o la defensa para pedir el archivo** → `buscar_por_cita` con su ECLI o ROJ.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Redacta el escrito con el que la acusación se opone al archivo. Orden: **identificar el cauce y la
clase de sobreseimiento → estándar indiciario → escrito**. Equivocar el cauce o la clase es el error
que más veces convierte una oposición sólida en un escrito inútil.

---

## Bloque previo de comprobaciones (OBLIGATORIO)

1. **¿Qué resolución o trámite exactamente?** No es lo mismo:
   - **Traslado del art. 780.1** para acusar o pedir sobreseimiento (10 días comunes).
   - **Auto de sobreseimiento del art. 779.1.1.ª** ya dictado → **recurso**, no alegaciones.
   - **Petición de sobreseimiento del Fiscal** con el juez aún sin resolver → **arts. 782.2 / 642**.
   - **Solicitud de archivo de la defensa** → alegaciones de oposición.
   **Identifícalo y cita el folio.** El escrito cambia por completo según el caso.
2. **¿Sobreseimiento LIBRE o PROVISIONAL?** → § siguiente. **Los efectos son radicalmente distintos**;
   la oposición se argumenta distinto y, si no lo evitas, cabe **pedir subsidiariamente** que sea
   provisional y no libre.
3. **¿Estás personado?** Para alegar hay que ser parte. **PERO ojo:** para **recurrir el auto de
   sobreseimiento**, **no hace falta** (art. 779.1.1.ª LECrim y art. 12.2 Ley 4/2015 — § recursos).
   Si el usuario no está personado y aún hay margen → `personacion-acusacion-particular-catalogo`.
4. **Fecha de notificación** del traslado o del auto → **calcula el plazo y dilo con la fecha**.
5. **Prescripción (art. 131 CP, verificado)** y **art. 132.2 CP (verificado)**: la denuncia/querella
   **no interrumpe**, solo **suspende 6 meses**; interrumpe la **resolución judicial motivada** que
   dirige el procedimiento contra persona determinada. ⚠️ En una causa que va a archivarse, **comprueba
   si el delito está prescrito**: a veces el archivo es inevitable por esta vía y hay que decírselo al
   cliente.
6. **Fecha de los hechos → ley aplicable (art. 2 CP):** 2.1 irretroactividad; **2.2 ley más favorable
   retroactiva**. Hechos anteriores al **10-4-2026** (LO 1/2026) → **compara redacciones**. Si el
   archivo se funda en atipicidad sobrevenida por reforma, **verifícalo**.
7. **⏰ Art. 324 LECrim:** ¿está vivo el plazo de instrucción? Si pides diligencias subsidiariamente,
   **solo sirven si pueden acordarse antes del vencimiento** (324.3) → ver
   `solicitud-diligencias-instruccion-catalogo`. **Pedir diligencias fuera de plazo es pedir nada.**
8. **Competencia** (art. 14 LECrim, verificado): Sección de Instrucción del Tribunal de Instancia.

---

## LIBRE vs PROVISIONAL — la distinción que decide el escrito

**Art. 637 LECrim (VERIFICADO, literal) — sobreseimiento LIBRE:**
> «Procederá el sobreseimiento libre:
> **1.º** Cuando **no existan indicios racionales** de haberse perpetrado el hecho que hubiere dado
> motivo a la formación de la causa.
> **2.º** Cuando **el hecho no sea constitutivo de delito**.
> **3.º** Cuando aparezcan **exentos de responsabilidad criminal** los procesados como autores,
> cómplices o encubridores.»

**Art. 641 LECrim (VERIFICADO, literal) — sobreseimiento PROVISIONAL:**
> «Procederá el sobreseimiento provisional:
> **1.º** Cuando **no resulte debidamente justificada la perpetración del delito** que haya dado motivo
> a la formación de la causa.
> **2.º** Cuando **resulte del sumario haberse cometido un delito y no haya motivos suficientes para
> acusar a determinada o determinadas personas** como autores, cómplices o encubridores.»

### Diferencia de EFECTOS — explícala siempre al cliente

| | **LIBRE (637)** | **PROVISIONAL (641)** |
|---|---|---|
| **Naturaleza** | Juicio **definitivo**: el hecho no existió, no es delito, o hay exención | Juicio **de insuficiencia**: no está *acreditado* (aún) |
| **Efectos** | Produce **COSA JUZGADA**: cierra el asunto de forma **definitiva** | **NO** produce cosa juzgada: la causa **puede REABRIRSE** si aparecen nuevos elementos |
| **Reapertura** | **No** cabe | **Sí**, con nuevas pruebas — mientras **no haya prescrito** el delito |
| **Riesgo real para la acusación** | **Máximo** | Contenido: deja la puerta abierta |

> **⭐ ESTRATEGIA CENTRAL — la petición subsidiaria que casi nadie formula.**
> Si el archivo es **inevitable**, **no te limites a oponerte en bloque**: pide **subsidiariamente** que,
> de acordarse, lo sea **PROVISIONAL del art. 641** y **no libre del art. 637**. La diferencia es
> **cosa juzgada o puerta abierta**. Un sobreseimiento provisional conserva el asunto; uno libre lo
> mata.
> **Cómo se argumenta:** el 637 exige un juicio **definitivo y categórico** (el hecho **no existe**, **no
> es** delito, **hay** exención). Basta acreditar que subsiste **duda** o que **falta acreditación** —no
> certeza de inexistencia— para que el cauce correcto sea el **641**, no el 637. **Es un argumento más
> fácil de ganar que la oposición total: úsalo siempre como subsidiario.**

> ⚠️ **Matiz que debes verificar, no afirmar:** la **cosa juzgada** del sobreseimiento libre y su
> alcance exacto (según el ordinal del 637, y según se haya dictado en instrucción o tras
> procesamiento) es cuestión **jurisprudencial matizada**. **Contrástalo con `buscar_sentencias` antes
> de afirmar el alcance concreto** en un caso. ⛔ No lo des por sabido.

**Art. 634 LECrim** (efectos y alzamiento de medidas) y **art. 638** (forma del auto): **verifícalos con
`buscar_articulo` antes de citar su contenido** → `[verificar]`.

---

## El cauce en el ABREVIADO

**Art. 779.1.1.ª LECrim (VERIFICADO):** practicadas las diligencias, el juez adopta por **auto** alguna
de las resoluciones del precepto:
> «**1.ª** Si estimare que **el hecho no es constitutivo de infracción penal** o que **no aparece
> suficientemente justificada su perpetración**, acordará **el sobreseimiento que corresponda**. Si, aun
> estimando que el hecho puede ser constitutivo de delito, **no hubiere autor conocido**, acordará el
> **sobreseimiento provisional** y ordenará el archivo.»
- ⭐ **«El sobreseimiento que corresponda»** = la remisión a los arts. 637 y 641. **Ahí se juega la
  clase**: exige que se motive **cuál** y **por qué**.
- ⭐ **Autor no conocido → provisional por mandato legal.** Si te archivan por autor desconocido, **no
  puede ser libre**.

**⭐ 779.1.1.ª — COMUNICACIÓN Y RECURSO DE LA VÍCTIMA (VERIFICADO, literal):**
- «El auto de sobreseimiento **será comunicado a las víctimas del delito**, en la **dirección de correo
  electrónico** y, en su defecto, dirección postal o domicilio que hubieran designado en la solicitud
  prevista en el **art. 5.1.m) de la Ley del Estatuto de la Víctima**.»
- Muerte o desaparición causada por delito → comunicación a las personas del **art. 109 bis.1 II**. El
  juez puede **motivadamente** prescindir de comunicarlo a todos los familiares si ya se dirigió con
  éxito a varios o si las gestiones de localización resultaron infructuosas.
- Residentes **fuera de la UE** sin dirección conocida → remisión a la **oficina diplomática o
  consular** para su publicación.
- «**Transcurridos CINCO DÍAS desde la comunicación, se entenderá que ha sido efectuada válidamente** y
  desplegará todos sus efectos», salvo que la víctima acredite **justa causa** de imposibilidad de
  acceso.
- **⭐ «Las víctimas podrán RECURRIR el auto de sobreseimiento dentro del plazo de VEINTE DÍAS aunque NO
  se hubieran mostrado como parte en la causa.»** ← § recursos.

**Art. 780.1 (verificado):** traslado al Fiscal y a **las acusaciones personadas** para que, en **plazo
común de DIEZ DÍAS**, pidan **apertura del juicio oral** con escrito de acusación, **sobreseimiento**,
o **excepcionalmente** diligencias complementarias (**780.2**).

**Art. 782.1 (VERIFICADO):** «**Si el Ministerio Fiscal Y el acusador particular solicitaren el
sobreseimiento** de la causa por cualquiera de los motivos que prevén los **arts. 637 y 641**, **lo
acordará el Juez**», salvo los supuestos de los **números 1.º, 2.º, 3.º, 5.º y 6.º del art. 20 CP**
(causas de exención), en que **devolverá las actuaciones a las acusaciones para calificación,
continuando el juicio hasta sentencia** a efectos de **medidas de seguridad** y de la **acción civil**.
Al acordar el sobreseimiento, el juez **deja sin efecto la prisión y demás medidas cautelares**.
> **Lectura clave:** si **ambas** acusaciones piden el archivo, el juez **lo acordará** — vinculado.
> **Por eso la acusación particular personada es determinante: mientras tú sostengas la acusación, el
> art. 782.1 no opera.** Es el argumento más contundente para explicar al cliente por qué personarse.

---

## ⭐ EL ART. 782.2 — la baza frente a un Fiscal que no acusa

**Este es el punto central de la skill. Verificado literalmente contra el BOE (2026-07-17).**

**Art. 782.2 LECrim (redacción Ley 38/2002, vigente 28-4-2003) — literal:**
> «**Si el Ministerio Fiscal solicitare el sobreseimiento de la causa y NO se hubiere personado en la
> misma acusador particular dispuesto a sostener la acusación**, **antes de acordar el sobreseimiento**
> el Juez de Instrucción:
> **a)** **Podrá acordar que se haga saber la pretensión del Ministerio Fiscal a los directamente
> ofendidos o perjudicados conocidos, no personados, para que dentro del plazo máximo de QUINCE DÍAS
> comparezcan a defender su acción si lo consideran oportuno.** Si no lo hicieren en el plazo fijado, se
> acordará el sobreseimiento solicitado por el Ministerio Fiscal, sin perjuicio de lo dispuesto en el
> párrafo siguiente.
> **b)** **Podrá remitir la causa al SUPERIOR JERÁRQUICO DEL FISCAL para que resuelva si procede o no
> sostener la acusación, quien comunicará su decisión al Juez de Instrucción en el plazo de DIEZ
> DÍAS.**»

### Cómo se usa — instrucciones operativas

- **Presupuesto:** el 782.2 opera **solo** si el Fiscal pide sobreseimiento **y NO hay acusador
  particular personado dispuesto a sostener la acusación**. **Si tú estás personado y acusas, el 782.2
  no entra en juego —y tampoco el 782.1: la causa sigue.** Personarse es la protección **fuerte**; el
  782.2 es la red de seguridad de quien no lo está.
- **Dos vías, ambas POTESTATIVAS («podrá»), y no alternativas excluyentes:** el juez puede usar **a)**,
  **b)**, o **ambas**. El literal del a) («sin perjuicio de lo dispuesto en el párrafo siguiente») lo
  confirma: **aunque los ofendidos no comparezcan, el juez todavía puede acudir al superior
  jerárquico**.
- **Vía a) — llamada a los ofendidos (15 días).** Si tu cliente recibe esa comunicación: **es su última
  oportunidad**. Comparecer = personarse y sostener la acusación. **Si no comparece en 15 días, se
  acuerda el sobreseimiento.** Trátalo como plazo perentorio.
- **Vía b) — el superior jerárquico del Fiscal (10 días).** Es **la baza de la acusación frente a un
  Fiscal que no acusa**: se somete el criterio del Fiscal a revisión **dentro de la propia Fiscalía**.
  **Instrucción: si el Fiscal pide archivo y hay indicios sólidos, SOLICITA EXPRESAMENTE al juez que
  haga uso del art. 782.2.b).** No es automático: **es potestativo y hay que pedirlo y motivarlo**.
  Casi nadie lo pide, y es gratis.
- **Cómo motivar la petición del 782.2.b):** no basta discrepar. Razona que la petición del Fiscal
  **desconoce elementos obrantes en autos** (con folios), o que **se aparta del criterio de la propia
  Fiscalía**, o que hay **diligencias pendientes** que la desmienten. Sé concreto: es una petición de
  **revisión jerárquica**, no un desahogo.
- ⚠️ **No confundas 782.2 con 642.** El **art. 642 LECrim** (verificado) contiene la regla **paralela
  del sumario ordinario**: cuando el Fiscal pida el sobreseimiento conforme a los arts. 637 y 641 y **no
  se hubiere presentado querellante particular** dispuesto a sostener la acusación, **el Tribunal podrá
  acordar que se haga saber la pretensión del Fiscal a los interesados** en el ejercicio de la acción
  penal, «para que dentro del **término prudencial** que se les señale comparezcan a defender su acción
  si lo consideran oportuno»; si no comparecen, **se acordará el sobreseimiento**.
  > **Diferencias:** el 642 es del **ordinario**, fija un **término prudencial** (no 15 días) y **no
  > contempla la remisión al superior jerárquico**. **El recurso al superior jerárquico es propio del
  > abreviado (782.2.b).** No lo invoques en el ordinario sin verificarlo.
- **Verifica la doctrina** sobre el 782.2 y sobre el alcance del control judicial de la petición de
  archivo del Fiscal con **`buscar_sentencias`** antes de construir la estrategia. ⛔ No la afirmes de
  memoria.

---

## El estándar de la instrucción — el eje del escrito

**Este es el argumento de fondo. Constrúyelo bien y repítelo con disciplina.**

- En instrucción **no se exige certeza condenatoria**, sino **indicios racionales de criminalidad**. La
  instrucción **prepara el juicio** (**art. 299 LECrim**, verificado: «actuaciones encaminadas a
  **preparar el juicio**… para averiguar y hacer constar la perpetración de los delitos… y la
  culpabilidad»). **No lo sustituye.**
- **El juicio de tipicidad definitivo, la valoración de la prueba, la credibilidad de los testigos y la
  determinación de la autoría se reservan al JUICIO ORAL**, con inmediación y contradicción. Archivar
  porque «hay versiones contradictorias» o porque «la prueba no es concluyente» es **anticipar el
  juicio**: eso es precisamente lo que **no** puede hacerse en instrucción.
- **Reconduce el debate al ordinal correcto.** Si el archivo se pretende por el **637.2.º** (el hecho
  no es delito), el debate es **de subsunción**, no de prueba: discútelo en el plano jurídico. Si se
  pretende por el **641.1.º o 2.º** (falta de justificación o de motivos suficientes), el debate es de
  **suficiencia indiciaria**: enumera los indicios.
- **Tutela judicial efectiva — art. 24.1 CE**: el archivo prematuro, sin agotar diligencias
  pertinentes propuestas y pendientes, lesiona el derecho de acceso al proceso. Si **pediste
  diligencias y te las denegaron o no se practicaron**, **álegalo aquí**: es el nexo entre la
  denegación y el gravamen.
- ⚠️ **Verifica la doctrina** sobre el estándar indiciario y sobre el alcance de la instrucción con
  **`buscar_sentencias`** (TS Sala Segunda; AAP y SAP) y **confirma cada cita con `buscar_por_cita`**.
  ⛔ **Prohibido citar ECLI/ROJ/fecha/ponente de memoria.**

### Cómo se rebate una petición de archivo — método

1. **Aísla el motivo exacto** que invoca quien pide el archivo (ordinal del 637 o del 641) y **cítalo**.
2. **Enumera los indicios** que lo desmienten, **uno por uno, cada uno con su FOLIO**. No adjetives:
   **enumera**. «Consta al folio X que…» vale; «es evidente que…» no vale nada.
3. **Rebate la tesis del archivo** en sus propios términos. Si se alega «falta de participación» o
   «actos de mera buena voluntad», **enumera los actos concretos** que acreditan **cooperación
   decisiva**: qué hizo, cuándo, con qué efecto, en qué folio consta.
4. **Individualiza por investigado.** El indicio ha de ser **de cada uno**. La imputación en bloque es
   lo que hace prosperar los archivos parciales.
5. **Recuerda el estándar**: no se pide condena, se pide **continuar**.
6. **Subsidiario 1:** diligencias pendientes (con el **art. 324** vivo).
7. **Subsidiario 2:** que el sobreseimiento sea **PROVISIONAL (641)**, no libre (637).

---

## Estructura del escrito

1. **Encabezamiento:** «A LA SECCIÓN DE INSTRUCCIÓN DEL TRIBUNAL DE INSTANCIA DE [PARTIDO]» + **nº de
   Diligencias Previas [X/AÑO]** (art. 14 LECrim, LO 1/2025).
   > ⭐ **Regla práctica: copia la denominación EXACTA que figure en la resolución que contestas o en
   > la carátula del procedimiento.** Espejar al órgano nunca falla, diga «Sección de Instrucción del
   > Tribunal de Instancia» o siga rotulándose «Juzgado de Instrucción». Usar la denominación antigua
   > **no invalida** el escrito: la **DA 1.ª de la LO 1/2025** manda entenderla hecha a la Sección.
2. **Comparecencia:** procurador `[PROCURADOR]` y letrado/a de la parte **acusadora**, en la
   representación **ya acreditada** en autos (folio de la personación).
3. **Referencia al traslado**: providencia/diligencia de ordenación, **fecha de notificación** y plazo
   en que se evacua. Deja constancia de que se presenta **en plazo**.
4. **ALEGACIONES.** Puede ser **una única** alegación densa (uso frecuente) o varias. Contenido:
   - **I.** Motivo del archivo que se combate (ordinal exacto del 637/641) y por qué es erróneo.
   - **II.** **Indicios racionales de criminalidad**: enumerados, **cada uno con su folio**.
   - **III.** Rebate de la tesis contraria, **individualizada por investigado**.
   - **IV.** **Estándar de la instrucción** (art. 299; art. 24.1 CE): en instrucción **no** se exige
     certeza; el juicio de autoría y la valoración probatoria se reservan al juicio oral.
   - **V.** Apoyo jurisprudencial **verificado con el conector** (§ estándar). Si no lo verificas, **no
     lo cites**.
   - **VI.** Diligencias pendientes o denegadas, y su relevancia (con el **art. 324** vivo).
5. **SUPLICO:**
   - **Principal:** que **NO se acuerde** el sobreseimiento y **continúe** el procedimiento.
   - **Subsidiario 1.º:** que se acuerde la práctica de las diligencias interesadas.
   - **Subsidiario 2.º:** que, de acordarse el sobreseimiento, lo sea **PROVISIONAL (art. 641)** y **no
     libre (art. 637)**.
   - **Si el Fiscal pide archivo y no hay acusación particular** → que se acuerde lo previsto en el
     **art. 782.2.b)**: remisión al **superior jerárquico del Fiscal**; y/o el **782.2.a)**.
6. **OTROSÍES:** designación de **dirección electrónica** a efectos del art. 5.1.m) de la Ley 4/2015 y
   de la comunicación del auto (art. 779.1.1.ª); copias.
7. Lugar, fecha y firma.

> **Anclaje al folio — regla innegociable y aquí más que en ninguna otra skill.** Un escrito de
> oposición al archivo **es una enumeración de indicios**; un indicio sin folio **no es un indicio, es
> una opinión**. Todo hecho afirmado, con su folio.

---

## Recursos contra el auto de sobreseimiento

- **Régimen general (art. 766 LECrim, verificado):** contra los autos del Juez de Instrucción caben
  **reforma** y **apelación**; la apelación puede interponerse **subsidiariamente con la reforma o por
  separado**, y **«en ningún caso será necesario interponer previamente el de reforma para presentar la
  apelación»** (766.2). **Plazo de apelación: CINCO DÍAS** desde la notificación del auto recurrido o
  del resolutorio de la reforma (766.3). Traslado a las demás partes: **5 días** comunes. **Reforma: 3
  días (art. 211 LECrim — `[verificar]`).**
- **⭐ PLAZO ESPECIAL DE LA VÍCTIMA — 20 DÍAS (art. 779.1.1.ª LECrim, VERIFICADO):** «Las víctimas
  podrán recurrir el auto de sobreseimiento dentro del plazo de **veinte días** **aunque no se hubieran
  mostrado como parte en la causa**.»
- **Art. 12.2 de la Ley 4/2015, de 27 de abril, del Estatuto de la víctima (VERIFICADO, literal):** «La
  víctima podrá recurrir la resolución de sobreseimiento conforme a lo dispuesto en la Ley de
  Enjuiciamiento Criminal, **sin que sea necesario para ello que se haya personado anteriormente en el
  proceso**.»
  > ⭐ **Consecuencia práctica de primer orden:** **la víctima NO personada puede recurrir el archivo, y
  > dispone de 20 días.** Es la vía de rescate cuando el cliente llega tarde al despacho, con la causa
  > ya archivada. **Compruébalo siempre antes de decirle que no hay nada que hacer.**
  > ⚠️ **Coordina los dos plazos:** el **general del 766.3 es de 5 días**; el **especial de la víctima
  > es de 20** (779.1.1.ª). **Si tu cliente está personado, no juegues con el plazo largo sin
  > verificarlo**: la relación entre ambos plazos —y si el de 20 días alcanza también a la víctima ya
  > personada— **debe contrastarse con `buscar_sentencias`**. **En la duda, recurre en 5 días.** Es
  > gratis y elimina el riesgo. **Márcalo `[verificar]` y dilo al usuario.**
- **Cómputo de la comunicación (779.1.1.ª):** transcurridos **5 días desde la comunicación** se entiende
  **válidamente efectuada**, salvo **justa causa** acreditada de imposibilidad de acceso. **Vigila la
  dirección electrónica designada**: de ella depende que el plazo corra sin que te enteres.
- **Contra qué se recurre:** si el auto acuerda sobreseimiento **libre**, combate **la subsunción** y,
  subsidiariamente, pide su conversión en **provisional**. Si es **provisional**, valora si compensa
  recurrir o **reservar** la reapertura para cuando aparezcan nuevos elementos (**mientras no prescriba**
  — art. 131 CP).
- **Reapertura del provisional:** cabe con nuevos elementos. **Verifica el cauce con `buscar_articulo`**
  (arts. 641 y ss., y el régimen del abreviado) antes de afirmarlo → `[verificar]`.

---

## Errores típicos que hunden el escrito

1. **No distinguir LIBRE de PROVISIONAL** y perder la **cosa juzgada** sin pelearla.
2. **No pedir subsidiariamente el 641** cuando el archivo es inevitable. **El subsidiario más rentable
   del penal, y el más olvidado.**
3. **Indicios sin folio.** Un escrito de oposición sin folios no es nada.
4. **Adjetivar en vez de enumerar** («es evidente», «resulta palmario»): no acredita nada.
5. **Argumentar como si fuera el juicio oral**: pedir que se declare probado. **Se pide continuar**, no
   condenar.
6. **No individualizar por investigado** → archivos parciales.
7. **No invocar el art. 782.2.b)** cuando el Fiscal pide archivo y no hay acusación particular. **Es
   potestativo: hay que PEDIRLO.** Gratis y desaprovechado.
8. **Confundir el 782.2 (abreviado, con superior jerárquico y 15 días) con el 642 (ordinario, término
   prudencial, sin superior jerárquico).**
9. **Perder el plazo de 15 días** del art. 782.2.a) cuando llaman a los ofendidos: **precluye**.
10. **Creer que sin personarse no se puede recurrir el archivo**: **se puede, y en 20 días**
    (779.1.1.ª; art. 12.2 Ley 4/2015).
11. **No designar dirección electrónica** (art. 5.1.m Ley 4/2015) → no te comunican el auto y **el plazo
    corre igual** (779.1.1.ª: 5 días desde la comunicación).
12. **Pedir diligencias con el plazo del art. 324 vencido** → inútil (324.3).
13. **Olvidar que si el Fiscal Y el acusador particular piden archivo, el juez lo acordará** (782.1):
    mientras sostengas la acusación, la causa sigue.
14. **Buscar «Ley 4/2015» a secas** → devuelve la **ley agraria de Galicia**. El Estatuto de la víctima
    es la **Ley 4/2015, de 27 de abril**.
15. **Citar jurisprudencia sin conector.** ⛔ Prohibido.

---

## Datos personales — categoría reforzada

- Marcadores: `[INVESTIGADO]`, `[PERJUDICADO]`, `[TESTIGO]`, `[ENTIDAD]`, `[CIF]`, `[DOMICILIO]`,
  `[IMPORTE]`, `[GESTORÍA]`, `[PROCURADOR]`. **Nunca datos reales de terceros en la salida.**
- ⚠️ **Infracciones y condenas penales = categoría especial del art. 10 RGPD.** Este escrito **enumera
  indicios incriminatorios contra personas que pueden acabar sobreseídas**: extrema el cuidado. Cuidado
  con **menores** y **víctimas**.
- Slug del expediente: `descriptor-delito-año`, **nunca con el nombre del cliente**
  (`PROTECCION-DATOS.md`).

---

## Reglas de trabajo

- **Cifras y artículos:** fuente única `references/anclas-normativas-penal.md` o verificación en el
  momento con **`buscar_articulo`**. ⛔ **Prohibido inventar** artículos, ordinales o plazos. Si dudas
  entre 641.1.º y 641.2.º, o entre 637.1.º y 637.2.º, **verifícalo**; y si no puedes, **márcalo
  `[verificar]` y dilo**.
- **Jurisprudencia:** solo `buscar_sentencias` / `buscar_por_cita` / `leer_sentencias`. ⛔ Nunca de
  memoria.
- **Instruye el Juez de Instrucción** (Sección de Instrucción del Tribunal de Instancia). ⛔ **No existe
  el «fiscal instructor»**: reforma en tramitación (prevista 1-1-2028), **no es Derecho vigente**. No la
  menciones, ni cites un «art. 4 bis EOMF». ⚠️ Cuidado especial en esta skill: que el art. 782.2 permita
  acudir al **superior jerárquico del Fiscal** **no** significa que el Fiscal instruya. **El juez
  instruye y el juez decide el sobreseimiento.**
- ⛔ **Nada de MASC**: es del orden **civil**.
- **Días inhábiles:** **art. 183 LOPJ** (verificado, LO 14/2022): inhábiles **agosto** y **del 24 de
  diciembre al 6 de enero**, salvo actuaciones **declaradas urgentes**. **Pero art. 201 LECrim**
  (verificado, literal): «**Todos los días y horas del año serán hábiles para la instrucción de las
  causas criminales, sin necesidad de habilitación especial**». ⚠️ **La instrucción no se paraliza**;
  para los **plazos de recurso**, aplica el art. 183 LOPJ. **No los confundas.**

## Entrega

Escrito final en **Word `.docx`** con la skill **`docx`**, maquetado como escrito judicial
(encabezamiento, alegaciones, suplico principal y subsidiarios, otrosíes), listo para **LexNET**.
