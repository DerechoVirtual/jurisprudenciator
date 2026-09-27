---
name: recurso-reforma-apelacion-auto-archivo
description: >-
  Redacta recurso de reforma y subsidiario de apelación contra el auto de sobreseimiento y archivo YA DICTADO en instrucción, para la acusación particular o el perjudicado. Actívala ante "recurrir el archivo de la causa", "recurso contra el auto de sobreseimiento ya notificado", "reforma y subsidiaria apelación", "han archivado mis diligencias", "auto de sobreseimiento inmotivado", "quiero reabrir la causa", "el juez ha archivado sin practicar mis diligencias" o cuando la acusación quiera revocar un archivo ya acordado. Requisito previo: existe auto de archivo notificado y corre el plazo de recurso. Si todavía no hay auto y solo se ha dado traslado a la acusación para alegar sobre el archivo propuesto, lo que procede es oponerse antes → /alegaciones-oposicion-sobreseimiento.
---

# Recurso de reforma y subsidiario de apelación contra auto de archivo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazos y régimen del recurso** (arts. 211, 212, 766 y 779.1.1.ª LECrim) → `buscar_articulo` (`ley="LECrim"`).
- **Clase de sobreseimiento** (arts. 637 y 641 LECrim) → `buscar_articulo`.
- **Criterio de la Audiencia que resolverá la apelación** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="AP"`, `provincia` de la causa, `tipo_resolucion="AUTO"`) + `leer_sentencias` con `parrafos=3`.
- **Tutela judicial de la acusación frente a un archivo inmotivado o prematuro** → `buscar_sentencias` (`base="TC"`).
- **Resoluciones que cita el auto de archivo** → `buscar_por_cita`.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

Redacta el recurso frente al auto de sobreseimiento y archivo. **Es el recurso de la acusación: aquí
la causa se muere o revive.**

---

## ⏱️ PLAZOS Y RÉGIMEN — verificados literalmente contra el BOE

| Recurso | Plazo | Precepto | Verificado |
|---|---|---|---|
| **Reforma** | **3 días** desde la notificación | **art. 211** LECrim | «Los recursos de reforma o de súplica … se interpondrán en el plazo de los **tres días siguientes a su notificación**» |
| **Apelación** (régimen general) | **5 días** desde la última notificación | **art. 212** LECrim | «El recurso de apelación se entablará dentro de **cinco días**» |
| **Apelación en abreviado** | **5 días** desde la notificación del auto **o del resolutorio de la reforma** | **art. 766.3** LECrim | Ver abajo |
| **⭐ Víctima NO personada** | **20 días** | **art. 779.1.1.ª** LECrim | Ver abajo |

### ⚠️ La reforma es POTESTATIVA, no obligatoria — art. 766.2, verificado

> «El recurso de apelación podrá interponerse **subsidiariamente con el de reforma o por separado**.
> **En ningún caso será necesario interponer previamente el de reforma para presentar la apelación.**»

**No hay reforma preceptiva.** Tres opciones:

1. **Reforma + subsidiaria apelación** (lo habitual): un solo escrito, dentro de los **3 días** del
   art. 211. Conserva las dos instancias. **Es la opción por defecto** salvo razón para lo contrario.
2. **Apelación directa**, en **5 días** (art. 766.3), sin pasar por el mismo juez que archivó.
   Racional cuando el instructor ya ha manifestado un criterio firme y la reforma es un trámite
   perdido — **pero renuncias a la vía rápida de la revocación en instancia**.
3. Reforma sola: **no lo hagas**. Desestimada, el plazo de apelación corre desde la notificación del
   resolutorio (766.3) y habrás gastado tiempo sin red.

> **⚠️ La trampa del plazo:** si vas por la vía 1, el escrito debe entrar en **3 días** (art. 211), no
> en 5. El plazo de 5 días del 766.3 rige la apelación **autónoma** o la que se interpone tras la
> notificación del auto resolutorio de la reforma. **Contar 5 desde el archivo para un escrito conjunto
> es perder la reforma.**

### Tramitación de la apelación (art. 766.3 y 766.4, verificado)

- Escrito con **los motivos**, señalando los **particulares que hayan de testimoniarse** y acompañando
  los documentos justificativos. **Señala tú los particulares**: la Audiencia resuelve sobre testimonio,
  no sobre las actuaciones completas. Si no los señalas bien, resuelve a ciegas.
- Admitido: traslado a las demás partes por **plazo común de 5 días**. En los **2 días** siguientes, se
  remite testimonio a la Audiencia, que resuelve **sin más trámites en los 5 días** siguientes.
  Excepcionalmente puede reclamar las actuaciones (devolución en **3 días** máximo).
- **⭐ 766.4 — si la apelación fue subsidiaria** y la reforma se desestima total o parcialmente: **antes**
  de dar traslado a las demás partes, se da traslado **al recurrente por 5 días** para que **formule
  alegaciones** y presente documentos. **No lo desaproveches**: es tu oportunidad de reformular el
  recurso contra la motivación del auto que resolvió la reforma, que es la que la Audiencia leerá.
- **766.1:** reforma y apelación **no suspenden** el curso del procedimiento, salvo que la ley disponga
  otra cosa.
- **766.5:** vista solo si el auto acordó prisión provisional (o potestativa con otras cautelares).
  Irrelevante aquí.

### ⭐ La víctima no personada: 20 días — art. 779.1.1.ª, verificado

> «**Las víctimas podrán recurrir el auto de sobreseimiento dentro del plazo de veinte días aunque no
> se hubieran mostrado como parte en la causa.**»

- El auto de sobreseimiento **se comunica a las víctimas** en la dirección designada conforme al
  art. 5.1.m) de la Ley 4/2015 (Estatuto de la Víctima). En caso de **muerte o desaparición**, también
  a las personas del art. 109 bis.1 párr. 2.
- Transcurridos **5 días** desde la comunicación, se entiende **válidamente efectuada**, salvo que la
  víctima acredite justa causa de imposibilidad de acceso.
- **Operativo:** si llegas tarde y tu cliente **no estaba personado**, **no des la causa por perdida**:
  tienes **20 días**. Verifica siempre la fecha y el modo de la comunicación del auto — si fue
  defectuosa, el plazo no ha corrido.

---

## Comprobaciones previas — antes de recurrir

1. **⭐ PRESCRIPCIÓN — la urgencia real (art. 132.2 CP, verificado).** La prescripción se interrumpió
   cuando se dictó **resolución judicial motivada** atribuyendo la participación (132.2.1.ª), pero
   **vuelve a correr «desde que se paralice el procedimiento o termine sin condena»**. **El archivo es
   terminación sin condena: el reloj arranca de nuevo.** Calcula cuánto plazo queda (art. 131 CP) antes
   de decidir la estrategia. Y recuerda: la **denuncia o querella no interrumpe** — solo **suspende 6
   meses** (132.2.2.ª); si en ese plazo no recae resolución del 132.2.1.ª, el cómputo **continúa desde
   la fecha de presentación**. Un archivo mal recurrido puede significar la prescripción.
2. **Plazo de instrucción (art. 324 LECrim).** ¿El archivo se dicta por agotamiento del plazo (324.4)?
   Distinto de archivar por falta de indicios. Si quedaban diligencias pendientes y el plazo venció por
   inactividad **del juzgado**, dilo. ⚠️ Y comprueba el **reverso**: si pides diligencias fuera de plazo
   sin prórroga vigente, serían **inválidas (324.3)** — no las pidas sin pedir antes la prórroga.
3. **Ley penal más favorable (art. 2.2 CP).** LO 1/2025 y LO 1/2026. ⭐ **Relevante aquí**: la LO 1/2026
   creó **tipos agravados por multirreincidencia** (arts. 234.2, 235.1.7.º y 10.º, 248 párr. 3,
   250.1.8.º). Un hecho archivado como **delito leve** puede ser hoy **delito menos grave** por
   multirreincidencia — pero **solo si le es aplicable** (art. 2 CP: irretroactividad desfavorable).
   Comprueba la fecha de los hechos **antes** de invocarlo.
4. **⭐ Art. 105.3 LECrim (nuevo, LO 1/2026):** «las **entidades locales** podrán ejercer la acción
   penal por los delitos de **hurto**» del capítulo I del título XIII del libro II CP. Legitimación
   nueva: verifica si abre una vía de personación.
5. **Días inhábiles** (art. 183 LOPJ y régimen propio de la instrucción, art. 201 LECrim). Ver
   `CLAUDE.md`.

---

## Qué auto tienes delante — la clasificación decide el recurso

| Resolución | Precepto | Efecto |
|---|---|---|
| **Sobreseimiento LIBRE** | **art. 637** LECrim | Efecto de **cosa juzgada**. Cierra |
| **Sobreseimiento PROVISIONAL** | **art. 641** LECrim | **No** cierra: cabe reapertura con nuevos elementos |
| Archivo del abreviado | **art. 779.1.1.ª** LECrim | Ver abajo |

**Art. 637 — sobreseimiento libre** (verificado): 1.º cuando **no existan indicios racionales de
haberse perpetrado el hecho**; 2.º cuando **el hecho no sea constitutivo de delito**; 3.º cuando
**aparezcan exentos de responsabilidad criminal** los procesados.

**Art. 641 — sobreseimiento provisional** (verificado): 1.º cuando **no resulte debidamente justificada
la perpetración** del delito; 2.º cuando, habiéndose cometido un delito, **no haya motivos suficientes
para acusar** a determinadas personas.

**Art. 779.1.1.ª — el cauce del abreviado** (verificado): «Si estimare que **el hecho no es constitutivo
de infracción penal** o que **no aparece suficientemente justificada su perpetración**, acordará el
sobreseimiento que corresponda. Si, aun estimando que el hecho puede ser constitutivo de delito, **no
hubiere autor conocido**, acordará el sobreseimiento **provisional** y ordenará el archivo.»

> ⚠️ **Corrección de un error frecuente:** el archivo del abreviado es el **779.1.1.ª**. El **779.1.4.ª**
> es el **auto de transformación** en procedimiento abreviado (lo contrario del archivo). Y el
> **779.1.5.ª** es la conformidad *in situ* del art. 801. No los confundas al citar.

**⭐ El punto que gana recursos:** el instructor califica a menudo como **libre** (art. 637) lo que solo
puede ser **provisional** (art. 641), o al revés. **Ataca la calificación misma del sobreseimiento**:

- Si el auto archiva por **falta de acreditación** de los hechos pero lo llama **libre**, es un error de
  cauce: la insuficiencia probatoria es **641.1.º**, no 637. Y el libre produce **cosa juzgada** — te
  cierra la reapertura futura. **Alégalo aunque no discutas el archivo en sí.**
- Si archiva por **atipicidad** (637.2.º), el debate es **jurídico**, no probatorio: no discutas prueba,
  discute subsunción.

**Art. 782 — sobreseimiento a petición de las acusaciones** (verificado). Si el Fiscal y el acusador
particular **piden** el sobreseimiento, el juez **lo acuerda** (salvo eximentes del art. 20.1.º, 2.º,
3.º, 5.º y 6.º CP, en que devuelve para calificación a efectos de medidas de seguridad y acción civil).
**782.2 — si solo lo pide el Fiscal y no hay acusador particular personado**, antes de acordarlo el juez
**podrá**: a) hacerlo saber a los **ofendidos o perjudicados conocidos no personados** para que en
**15 días** comparezcan a defender su acción; o b) remitir la causa al **superior jerárquico del
Fiscal** para que resuelva si procede sostener la acusación (respuesta en **10 días**).
> **Uso táctico:** si tu cliente es perjudicado no personado y el Fiscal pide el archivo, el 782.2.a) es
> tu ventana. Son facultades del juez («**podrá**»), no deberes: **pídelas expresamente y razona por
> qué procede**.

---

## Motivos del recurso — por orden de eficacia

1. **Falta de motivación (art. 24.1 CE y art. 120.3 CE; art. 248 LOPJ).** El auto que archiva sin
   razonar por qué los indicios son insuficientes, o que no da respuesta a las diligencias interesadas,
   vulnera la tutela judicial efectiva. **Cita el auto literalmente** para exhibir su vacío: la cita
   textual es más eficaz que la doctrina.
   > ⚠️ **Verifica la doctrina constitucional con `buscar_sentencias` antes de invocarla.** No cites
   > ninguna STC ni STS sin haberla localizado y leído. Sin verificación → `[verificar]`.
2. **Archivo prematuro: diligencias pendientes.** El motivo **más eficaz y el menos usado**. Enumera
   **una a una** las diligencias interesadas y **no practicadas**, con: (i) **folio** de la solicitud;
   (ii) resolución que las denegó o **silencio**; (iii) **qué acreditaría cada una**; (iv) por qué es
   **imposible archivar** sin ellas. Un archivo con diligencias pertinentes pendientes es archivo sin
   agotar la instrucción.
3. **Error en la valoración indiciaria.** El estándar del art. 779.1.1.ª es de **indicios**, no de
   certeza de condena. **El instructor no puede anticipar el juicio de culpabilidad**: la valoración
   plenaria corresponde al órgano de enjuiciamiento con inmediación. Si el auto dice «no ha quedado
   acreditado» o «existen versiones contradictorias», **está juzgando en instrucción** — ese es el
   argumento. Contrapón los indicios **enumerados y con folio**.
4. **Error de subsunción**, si el archivo es por atipicidad (637.2.º / 779.1.1.ª primer inciso).
   Debate jurídico puro: elementos del tipo, uno a uno, contra el hecho indiciario.
5. **Error de cauce**: libre (637) cuando procedía provisional (641), o viceversa. Ver arriba.
6. **Estatuto de la víctima (Ley 4/2015):** derechos de información y participación; comunicación
   defectuosa del auto.

---

## Estructura del escrito

1. Encabezamiento a la **Sección de Instrucción del Tribunal de Instancia** con nº de diligencias
   previas.
   > ⭐ **Copia la denominación exacta que figure en el auto que recurres o en la carátula del
   > procedimiento.** Es lo que nunca falla, diga «Sección de Instrucción del Tribunal de Instancia»
   > o siga diciendo «Juzgado de Instrucción». La nomenclatura vigente (art. 14 LECrim, desde el
   > 3-10-2025) es la de **Sección**; la antigua no invalida el escrito (DA 1.ª LO 1/2025).
2. Comparecencia de procurador y letrado de `[PERJUDICADO]` / acusación particular.
3. **Fórmula, con el cauce y el plazo correctos:** «Que, notificado el auto de fecha `[FECHA]` el
   `[FECHA]`, y **dentro del plazo de tres días** del **art. 211 LECrim**, al amparo de los **arts. 216
   y ss.** y del **art. 766 LECrim**, interpone **RECURSO DE REFORMA y, SUBSIDIARIAMENTE, DE APELACIÓN**
   contra el auto de sobreseimiento `[libre/provisional]` y archivo dictado conforme al art. `[637 /
   641 / 779.1.1.ª]`, con base en las siguientes alegaciones.»
   > Si la víctima **no está personada** y usas los **20 días** del **art. 779.1.1.ª**, dilo
   > expresamente y **acredita la fecha de la comunicación**.
4. **ALEGACIONES numeradas**, de las del bloque anterior, ordenadas por fuerza. Cada alegación:
   **qué dice el auto (cita literal) → por qué es erróneo → qué folio lo desmiente → qué pide**.
5. **SUPLICO:** que se **revoque** el auto, se deje sin efecto el sobreseimiento y el archivo, y se
   acuerde la **continuación** de la instrucción con la **práctica de las diligencias** que se
   relacionan; **subsidiariamente**, y para el caso de desestimarse la reforma, que se **tenga por
   interpuesto el recurso de apelación** y se **admita a trámite** para ante la Audiencia Provincial,
   **con expresa mención de los particulares que han de testimoniarse** (art. 766.3).
6. **OTROSÍES:** relación de **particulares a testimoniar** (art. 766.3); documentos justificativos;
   en su caso, petición del art. 782.2.a) o b); **solicitud de prórroga del plazo de instrucción
   (art. 324)** si va a vencer.
7. Lugar, fecha y firma de letrado y procurador.

---

## Errores típicos

| Error | Corrección |
|---|---|
| Presentar el escrito conjunto en 5 días | La **reforma** son **3 días** (art. 211). En 5 solo cabe apelación autónoma |
| Creer que la reforma es previa obligatoria | **766.2:** «**En ningún caso será necesario**» |
| Dar la causa por perdida si el cliente no estaba personado | La víctima tiene **20 días** (art. 779.1.1.ª) aunque no sea parte |
| Citar el **779.1.4.ª** como cauce del archivo | Es el **779.1.1.ª**. El 4.ª es el auto de **transformación** |
| No señalar los particulares a testimoniar | **766.3**: la Audiencia resuelve sobre **testimonio**. Sin ellos, resuelve sin tu prueba |
| Desaprovechar el traslado del **766.4** | 5 días para reformular contra el auto que **la Audiencia leerá** |
| Recurrir sin comprobar la **prescripción** | El archivo **reanuda** el cómputo (art. 132.2 CP). Puede ser tarde |
| No distinguir sobreseimiento **libre** del **provisional** | El libre produce **cosa juzgada**. El error de cauce es un motivo por sí solo |
| Argumentar «no está probado que fuera él» | El estándar es de **indicios**, no de certeza. Ese es el error **del auto**, no tuyo |
| Alegar falta de motivación sin citar el auto | La **cita literal** del vacío es la mejor prueba |
| Pedir diligencias con el plazo del 324 vencido | Serían **inválidas (324.3)**. Pide **antes** la prórroga |
| Invocar STC/STS de memoria | **Prohibido.** Verifica con `buscar_sentencias` o no cites |

## Reglas de trabajo

- **Verifica con `buscar_articulo` antes de citar.** Anclas: `references/anclas-normativas-penal.md`.
- **Jurisprudencia solo vía `jurisprudenciator`** (`buscar_sentencias`, `buscar_por_cita`,
  `leer_sentencias`): doctrina constitucional sobre motivación y sobre el estándar indiciario en
  instrucción. **Prohibido inventar** ECLI, ROJ, fechas, ponentes o fundamentos, y **prohibido
  transcribir párrafos no verificados**. Sin verificar → `[verificar]`.
- **Prohibido inventar** plazos, ordinales o artículos. Lo no verificable → `[verificar]`, y se advierte.
- **Ancla al folio**: «(f. …)». Un recurso contra un archivo **se gana con folios**, no con adjetivos.
- **Anonimización:** `[PERJUDICADO]`, `[INVESTIGADO]`, `[TESTIGO]`. Datos de infracciones y condenas =
  **categoría especial (art. 10 RGPD)**. Ver `PROTECCION-DATOS.md`.
- **Instruye el Juez de Instrucción.** No existe el «fiscal instructor» en Derecho vigente.
- Terminología LO 1/2025: Tribunales de Instancia, LAJ, Audiencia Provincial.

## Entrega

Word `.docx` (skill `docx`) con alegaciones, suplico y otrosíes, maquetado para LexNET. Adjunta un
**cuadro de diligencias pendientes** (diligencia → folio de la solicitud → resolución o silencio → qué
acreditaría) y el **cómputo de plazos**: fecha del auto, notificación, vencimiento de los 3 días
(art. 211) y de los 5 (art. 766.3), con el margen de seguridad de la casa.
