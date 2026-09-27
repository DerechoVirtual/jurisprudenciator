---
name: escrito-conclusiones-ca
description: Redacta el escrito de conclusiones del proceso contencioso-administrativo — trámite escrito del art. 64 LJCA (ordinario, 10 días) y conclusiones del procedimiento abreviado (art. 78). Cubre nulidad de pleno derecho, responsabilidad patrimonial sanitaria, urbanismo y Seguridad Social. Activar con "conclusiones contencioso", "escrito de conclusiones", "evacuar traslado de conclusiones", "me han dado traslado para conclusiones".
---

# Escrito de conclusiones contencioso-administrativo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Límites del trámite** (cuestiones nuevas, providencias de los arts. 33.2 y 65.2, pronunciamiento del art. 65.3) → `buscar_articulo` (`ley="LJCA"`, artículos 33, 62, 64, 65 y 78).
- **Letra exacta de la nulidad y requisitos de la responsabilidad patrimonial** → `buscar_articulo` (`ley="LPAC"`, artículos 47, 48 y 67; `ley="LRJSP"`, artículos 32 y 34).
- **Doctrina de cada alegación** (lex artis, nulidad, motivación del acta de liquidación) → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`, `terminos`).
- **Variante de urbanismo** → `buscar_ordenanzas` + `leer_ordenanza` con `articulo`, y `consultar_catastro` para identificar la finca.
- **Antes de entregar** → `verificar_escrito` sobre el borrador, comprobando además que ninguna cita introduce una cuestión que no estuviera en la demanda.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

---

Instrucciones PARA Claude. Fuente única de plazos y umbrales: `references/anclas-normativas-ca.md`.
Lo que no esté allí, verifícalo con `buscar_articulo` o márcalo `[verificar]`. **No inventes nunca**
plazos, letras de artículo ni cifras.

## 1. Función del trámite — y su límite

Las conclusiones son **alegaciones SUCINTAS** sobre **los hechos, la prueba practicada y los
fundamentos jurídicos** en que se apoyan las pretensiones (**art. 64.1**). No son una segunda
demanda. Su valor está en **una sola cosa**: demostrar que **la prueba practicada acredita** los
hechos afirmados en la demanda. Si el escrito no menciona la prueba, sobra.

> ⛔ **PROHIBIDO: cuestiones nuevas — art. 65.1.** «En el acto de la vista o en el escrito de
> conclusiones **no podrán plantearse cuestiones que no hayan sido suscitadas en los escritos de
> demanda y contestación**.» Una cuestión nueva no se estima y **desacredita** el resto. Antes de
> entregar, **comprueba que cada alegación tiene anclaje en la demanda** y dilo si no lo tiene.

**Si el motivo relevante lo aprecia el ÓRGANO, hay cauce — no lo confundas con el art. 65.1:**
- **Art. 65.2:** si el Juez o Tribunal juzga oportuno que **en la vista o en las conclusiones** se
  traten **motivos relevantes para el fallo distintos de los alegados**, lo pone en conocimiento de
  las partes por **providencia**, con plazo de **10 días** para ser oídas. **No cabe recurso.**
- **Art. 33.2:** si es **al dictar sentencia** cuando estima que la cuestión pudo no ser apreciada
  debidamente por existir **en apariencia otros motivos**, lo somete a las partes por **providencia**
  —advirtiendo que no prejuzga el fallo—, con plazo común de **10 días** y **suspensión del plazo
  para el fallo**. **No cabe recurso.** (Art. 33.3: igual si, impugnados preceptos de una disposición
  general, procede extender el enjuiciamiento a otros por conexión o consecuencia.)
- **Art. 33.1 — congruencia:** el órgano juzga dentro del límite de **las pretensiones** y de **los
  motivos** de recurso y oposición. Ese es el marco.

> ⚠️ **Si recibes una providencia del art. 65.2 o del art. 33.2, es una oportunidad, no un trámite.**
> El órgano está señalando por dónde puede ganarse el asunto. Responde en los **10 días** y
> **argumenta a fondo**.

**Baza que casi nadie usa — art. 65.3:** en la vista o en el escrito de conclusiones, **el demandante
puede solicitar que la sentencia formule pronunciamiento concreto sobre la EXISTENCIA y la CUANTÍA
de los daños y perjuicios** de cuyo resarcimiento se trate, **si constasen ya probados en autos**.
**Comprueba siempre si la prueba practicada lo permite**: evita remitir el quantum a ejecución.

## 2. Cuándo hay conclusiones y con qué plazo

### 2.1 Procedimiento ordinario — art. 64

- **Plazo: 10 DÍAS SUCESIVOS** para demandantes y demandados; **simultáneo** dentro de cada grupo si
  hay más de una parte sin representación común (**art. 64.2**).
- **Cómo se llega al trámite — art. 62:** se pide **por otrosí en demanda o contestación**, o por
  escrito en **5 días** desde la diligencia que declare concluso el período de prueba (art. 62.2).
  El LAJ provee según lo coincidente; en otro caso **solo acuerda vista o conclusiones cuando lo
  solicite el DEMANDANTE**, o cualquiera de las partes si **se practicó prueba** (art. 62.3).
  Excepcionalmente puede acordarlo el órgano de oficio (art. 62.4).
- **Art. 64.4:** celebrada la vista o presentadas las conclusiones, se declara el pleito **concluso
  para sentencia**, salvo diligencias finales (art. 61.2).
- **Agosto — art. 128.2 LJCA:** no corre ningún plazo de la LJCA, **salvo derechos fundamentales**,
  donde agosto **sí** es hábil. **No cites el art. 133 LEC.**

### 2.2 Procedimiento abreviado — art. 78

> ⛔ **ERRATA VERIFICADA — NO REINTRODUCIR.** Versiones anteriores situaban las conclusiones orales
> en el **art. 78.6**. **ES FALSO:** el art. 78.6 es la **apertura de la vista** por el demandante
> («la vista comenzará con exposición por el demandante de los fundamentos de lo que pida o
> ratificación de los expuestos en la demanda»). Verificado contra el BOE el 2026-07-17.

- **Conclusiones ORALES, en la vista:** tras fijar los hechos y practicar la prueba (**art. 78.10**),
  **antes del informe final** (**art. 78.19**: «tras la práctica de la prueba, si la hubiere, y, en
  su caso, **de las conclusiones**, oídos los Letrados...»). Si no hay prueba ni conclusiones y
  concurren las circunstancias del **art. 78.11**, el juez puede dictar **sentencia sin más
  dilación**. **Único momento para observaciones sobre los testigos:** los testigos **no pueden ser
  tachados** y **únicamente en conclusiones** cabe hacer observaciones sobre sus circunstancias
  personales y la veracidad de sus manifestaciones (**art. 78.15**). No lo desperdicies.
- **Conclusiones ESCRITAS, 5 DÍAS SUCESIVOS (art. 78.3 in fine):** solo cuando el actor pidió el
  fallo **sin vista ni prueba**, el juez **rechazó la vista por auto** y **el actor las había
  SOLICITADO EN SU DEMANDA**. Sin esa petición previa, **no hay trámite**.
- **Sentencia oral (art. 78.20, LO 1/2025):** puede dictarse **oralmente al concluir la vista**, con
  los requisitos de los apartados **3 y 4 del art. 210 LEC**. Las conclusiones orales pueden ser **lo
  último que oiga el juez antes de fallar**: prepáralas por escrito y léelas con estructura.

## 3. Estructura (según las plantillas reales del despacho — conservar)

1. **Encabezamiento:** «A LA SALA DE LO CONTENCIOSO-ADMINISTRATIVO DEL [ÓRGANO]» / «AL JUZGADO DE LO
   CONTENCIOSO-ADMINISTRATIVO Nº [ÓRGANO] DE [ÓRGANO]»; procurador y letrado, representación de
   `[CLIENTE]`, **nº de autos** y procedimiento.
2. **Fórmula de evacuación:** «Que dentro del plazo conferido para conclusiones esta parte evacua
   dicho traslado **reiterando** cuantos antecedentes de hecho y de derecho se consignaron en la
   demanda y en base a las siguientes **ALEGACIONES**».
3. **ALEGACIONES numeradas** (PRIMERA, SEGUNDA...), cada una abriendo con el resultado probatorio:
   > «**Ha resultado probado** por la prueba documental / por el expediente administrativo **que**
   > [hecho], según consta al **folio [N]** del expediente administrativo / al **documento nº [N]**
   > de la demanda / de la **pericial** practicada en autos.»
   **Regla de hierro:** un hecho sin **folio** o sin **documento** identificado no entra. Y cada
   alegación cierra ligando el hecho probado con **su consecuencia jurídica**.
4. **Valoración de la prueba de contrario:** qué **no** probó la Administración, y sobre quién pesaba
   la carga. En **sancionador**, invoca la **presunción de inocencia** y que la carga de acreditar
   los hechos típicos corresponde a la Administración (verifica el precepto antes de citarlo).
5. **Recapitulación jurídica** breve — sin reabrir la demanda.
6. **Art. 65.3** cuando proceda: pronunciamiento concreto sobre existencia y cuantía de los daños,
   por constar ya probados en autos.
7. **SUPLICO:** reiterar la **estimación del recurso** en los términos del **art. 31 LJCA** —
   **anulación** (31.1), **reconocimiento de la situación jurídica individualizada** y medidas de
   pleno restablecimiento, e **indemnización** cuando proceda (31.2) — **y costas** (art. 139). El
   suplico **debe coincidir con el de la demanda**: cualquier desviación es cuestión nueva.

## 4. Variantes

### 4.1 Nulidad de pleno derecho (Seguridad Social y urbanismo)
Invoca **la letra exacta** del **art. 47.1 LPAC** que proceda — típicamente **b)** órgano
manifiestamente incompetente por materia o territorio, o **e)** haber prescindido **total y
absolutamente** del procedimiento legalmente establecido o de las reglas esenciales de formación de
la voluntad de los órganos colegiados. **Verifica siempre la letra.** Argumenta **falta de
motivación** y **ausencia de imputación directa**. Si el vicio es formal y no encaja en el art. 47,
reconduce al **art. 48.2** (anulabilidad) y **acredita la indefensión material concreta**: qué no
pudo alegarse y qué habría cambiado. No fuerces la nulidad: mal invocada, arrastra al resto.

### 4.2 Responsabilidad patrimonial sanitaria
- **Cronología clínica** construida **sobre la historia clínica del expediente**, folio a folio.
- **Requisitos (art. 32.1 Ley 40/2015):** lesión **efectiva, evaluable económicamente e
  individualizada**; **nexo causal** con el funcionamiento **normal o anormal** del servicio;
  **antijuridicidad** (ausencia de deber jurídico de soportar el daño). La **fuerza mayor** excluye;
  el **caso fortuito** no.
- **Art. 34.1:** no son indemnizables los daños que el particular tenga el **deber jurídico de
  soportar**; el estándar es la **lex artis** y **el estado de los conocimientos de la ciencia o de
  la técnica** al tiempo de los hechos. Ata la pericial a ese estándar, no a la mala evolución.
- **Plazo (art. 67 Ley 39/2015):** **1 año**; en **daños físicos o psíquicos**, desde la **curación o
  la determinación del alcance de las secuelas**. Si la Administración opone prescripción, ésta es la
  alegación decisiva.
- **Sin doble silencio:** la responsabilidad patrimonial está **excluida** del silencio estimatorio
  del art. 24.1 LPAC. No lo alegues.
- ⚠️ **Datos de salud = categoría especial (art. 9 RGPD).** **Nunca** reproduzcas datos clínicos
  reales de terceros ni del cliente en borradores: `[CLIENTE]`, `[FECHA]`, `[DATO CLÍNICO]`.

### 4.3 Urbanismo y licencias
Competencia del órgano, procedimiento seguido, y **normativa autonómica y local** (planeamiento,
ordenanzas). ⚠️ **El conector NO cubre la normativa autonómica ni los BOP no incluidos** (sí las
ordenanzas de los municipios cubiertos, vía `buscar_ordenanzas` / `leer_ordenanza`). **Pide al
usuario la norma aplicable y NO la cites de memoria.** Recuerda: la impugnación **directa** de
instrumentos **normativos de planeamiento** es de **cuantía indeterminada** (art. 42.2) y las
impugnaciones de planeamiento urbanístico **quedan fuera** de los Juzgados (art. 8.1).

### 4.4 Seguridad Social y responsabilidad solidaria
**Falta de motivación del acta de liquidación** y **ausencia de acción u omisión imputable** al
`[CLIENTE]`. Ancla al expediente cada elemento del que la Administración hace derivar la
responsabilidad; si no consta, dilo: **la carga es suya**. Muchos actos en materia de Seguridad
Social son de **cuantía indeterminada** (art. 42.2: inscripción de empresas, formalización de la
protección frente a riesgos profesionales, tarifación, cobertura de IT, afiliación, alta, baja y
variaciones de datos) — con efecto directo en el **tope de costas** (art. 139.4: **18.000 €** a esos
solos efectos).

## 5. Errores que pierden el asunto

- **Introducir cuestiones nuevas** (art. 65.1): no se estiman y restan credibilidad.
- **Reescribir la demanda** en vez de valorar **la prueba practicada** (art. 64.1: alegaciones
  **sucintas**).
- **Afirmar hechos sin folio ni documento.**
- **Desaprovechar la providencia del art. 65.2 o del art. 33.2** — son 10 días y no cabe recurso.
- **No pedir el pronunciamiento del art. 65.3** cuando el quantum ya está probado en autos.
- **Desviar el suplico** respecto del de la demanda, o **pedir solo la anulación** olvidando el
  reconocimiento de la situación jurídica individualizada y la indemnización (art. 31.2).
- **Citar el art. 78.6 como conclusiones** (es la apertura de la vista).
- **Contar con conclusiones escritas en el abreviado** sin haberlas pedido en la demanda (art. 78.3).
- **Reproducir datos de salud o de terceros** del expediente.

## 6. Cierre

- **Jurisprudencia:** verifica **PRIMERO** toda sentencia (TS, TC, TSJ) con el conector
  `jurisprudenciator` — `buscar_sentencias` (lista con ROJ/ECLI/fecha/ponente), `buscar_por_cita`
  (verificar un ECLI/ROJ exacto), `leer_sentencias` (texto íntegro). **Prohibido inventar** ECLI,
  ROJ, fechas, ponentes o fundamentos. Sin verificación, `[verificar]` y dilo.
- **Normativa autonómica y local:** pídesela al usuario; no la cites de memoria.
- **Protección de datos:** `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`, `[EXPEDIENTE]`,
  `[DATO CLÍNICO]`. Cero datos reales.
- **Nada de MASC:** es del orden civil.
- **Entregable:** Word `.docx` maquetado (skill `docx`), con encabezamiento, alegaciones y suplico
  listos para firma. Aplica `estilo-escritos-judiciales`.
