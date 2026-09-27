---
name: denuncia-estafa
description: Redacta denuncias por delito de estafa (arts. 248, 250 y 251 CP) ante la Sección de Instrucción del Tribunal de Instancia. Actívala cuando el usuario pida "denunciar una estafa", "me han estafado", "escrito de denuncia por engaño", "estafa de inversión", "estafa piramidal", "timo", "estafa en una compraventa", "me han dado un pufo", "engaño bastante", "negocio civil criminalizado", "dolo antecedente", "estafa agravada", "estafa procesal", "estafa continuada", "phishing", "fraude del CEO", "estafa informática", o mencione impago fraudulento, disposición patrimonial, ánimo de lucro, cooperador necesario, o estafa cometida por una sociedad.
---

# Denuncia por delito de estafa

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Tipo y penas vigentes** (arts. 248-251 CP, con la redacción de la LO 1/2026) → `buscar_articulo` (`ley="CP"`); compáralo con la redacción vigente a la fecha de los hechos.
- **Doctrina de la Sala Segunda sobre engaño bastante y negocio civil criminalizado** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3` y `terminos` («engaño bastante», «dolo antecedente»).
- **Sociedad denunciada y sus administradores** → `buscar_empresa_mercantil` (estado, domicilio, administradores y fecha de nombramiento, últimos actos inscritos); para fechar un acto concreto, `sumario_borme` → `leer_boe`.
- **Inmueble objeto de la estafa** (doble venta o venta de cosa ajena, art. 251 CP) → `consultar_catastro` por referencia catastral o dirección.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

Redacta la denuncia penal por estafa. Sigue este orden: **comprobaciones previas → subsunción →
escrito**. No empieces a redactar sin cerrar el bloque de comprobaciones: en estafa, casi todos los
escritos que fracasan lo hacen por un defecto detectable antes de escribir la primera línea.

---

## 🚨 BANNER DE ERRATA — NO REINTRODUCIR

> **La penalidad de la estafa común NO está en el art. 249 CP.** Está en el **art. 248, párrafo 2**.
>
> Verificado contra el BOE (`buscar_articulo`, 2026-07-17):
> - **LO 14/2022** (vigente 12-1-2023) convirtió el **art. 249** en la **estafa informática y con
>   instrumentos de pago** (manipulación informática, transferencia no consentida, uso fraudulento de
>   tarjetas, fabricación de dispositivos). El art. 249 **ya no contiene** la pena de la estafa común.
> - **LO 1/2026** (vigente **10-4-2026**) **reescribió el art. 248**, que hoy alberga definición, pena
>   y delito leve.
>
> ⛔ **Citar el art. 249 CP en una estafa común (no informática) es un error de bulto.** Nunca
> escribas «penalidad: art. 249» ni denuncies «por los arts. 248, 249, 250 y 251 bis» en bloque.
> Cita **solo** los preceptos que correspondan a la modalidad real de los hechos.

---

## Bloque previo de comprobaciones (OBLIGATORIO — resolver antes de redactar)

Recorre los seis puntos y **plantea al usuario lo que falte**. No inventes ni presupongas.

1. **Fecha de los hechos → redacción del CP aplicable (art. 2 CP, verificado).**
   Art. 2.1: irretroactividad. Art. 2.2: **retroactividad de la ley más favorable**, aun con sentencia
   firme, y **«en caso de duda sobre la determinación de la Ley más favorable, será oído el reo»**.
   - Hechos **desde el 10-4-2026** → redacción vigente sin más.
   - Hechos **anteriores al 10-4-2026** → **compara obligatoriamente** las dos redacciones y pide la
     más favorable. La comparación **no es opcional ni retórica**: hazla pena por pena, en bloque (no
     se pueden mezclar preceptos de ambas redacciones), y déjala escrita en el escrito.
   - Punto crítico: antes de la LO 1/2026 **no existía la multirreincidencia del art. 248 párr. 3 ni
     el 250.1.8.º**. Si la acusación pretende aplicarlos a hechos anteriores, es **retroactividad
     desfavorable prohibida**. Si defiendes, alégalo. Si acusas, no lo pidas.
2. **Prescripción (art. 131 CP, verificado).**
   - Estafa común (prisión 6 meses – 3 años) → **5 años** («los demás delitos»).
   - Estafa **agravada** del art. 250.1 (prisión 1-6 años) → pena máxima > 5 años → **10 años**.
   - Estafa del art. 250.2 (prisión 4-8 años) → **10 años**.
   - Estafa **leve** (≤ 400 €, multa 1-3 meses) → **1 año**. Es el plazo que se escapa: una estafa de
     300 € denunciada a los catorce meses está prescrita.
   - Art. 131.2: pena compuesta → se estará a la que **exija mayor tiempo**.
   - Art. 131.4: concurso o infracciones conexas → plazo del **delito más grave**.
   - **Cómputo — art. 132.1 CP (verificado):** desde el día de comisión; en **delito continuado**,
     **desde el día en que se realizó la última infracción**; en delito permanente, desde que se
     eliminó la situación ilícita. ⚠️ **Delito continuado (art. 74 CP, verificado):** en estafas
     seriadas el *dies a quo* se desplaza al **último acto**. Es a menudo lo que salva una denuncia
     aparentemente tardía. Compruébalo antes de descartar por prescripción.
   - **🚨 Art. 132.2 CP (verificado) — LA DENUNCIA NO INTERRUMPE POR SÍ SOLA.** Regla capital y
     habitualmente ignorada:
     - **Interrumpe** la prescripción que el procedimiento **se dirija contra la persona
       indiciariamente responsable**, lo que ocurre (regla **1.ª**) cuando se dicta **resolución
       judicial motivada** que le atribuya su presunta participación.
     - **La denuncia o querella solo SUSPENDE el cómputo por un plazo MÁXIMO DE SEIS MESES** (regla
       **2.ª**), desde su presentación.
     - Si **dentro de esos 6 meses** recae alguna de las resoluciones de la regla 1.ª → la interrupción
       se entiende producida **retroactivamente** en la fecha de la denuncia.
     - **Si NO recae** (o recae inadmisión firme, o el juez **no adopta ninguna** resolución) → **el
       cómputo CONTINÚA desde la fecha de la denuncia**, como si no se hubiera presentado.
     > **Operativo:** presentar la denuncia **no «para el reloj»**. Si el delito está cerca de
     > prescribir, **vigila los 6 meses** y **pide expresamente** que se dicte resolución motivada
     > dirigiendo el procedimiento contra `[DENUNCIADO]`. Si el juzgado no se mueve, **reclama e
     > impulsa**: la prescripción puede consumarse con la denuncia ya presentada.
3. **Competencia (arts. 14 y 15 LECrim).**
   Art. 14.2 (verificado, redacción vigente 3-10-2025): instruye la **Sección de Instrucción del
   Tribunal de Instancia del partido en que el delito se hubiere cometido**. En estafa el *locus
   delicti* es discutible (lugar del engaño, del acto de disposición, del perjuicio). Si es dudoso o
   los hechos son a distancia/online, **no fuerces una tesis**: expón el punto de conexión y, si
   procede, invoca el art. 15 LECrim. Si no puedes fijarlo, dilo.
4. **Naturaleza perseguible: la estafa es delito PÚBLICO.**
   Se persigue de oficio: **basta la denuncia**, no hace falta querella ni denuncia del ofendido como
   requisito de procedibilidad. → Si el usuario quiere **ser parte** desde el inicio, no le basta
   denunciar: remítelo a `querella-catalogo` o a
   `personacion-acusacion-particular-catalogo`. **El denunciante no es parte.**
5. **Legitimación.** Denunciante = perjudicado patrimonial. Si es persona jurídica, comprueba
   representación orgánica y acuerdo social si el estatuto lo exige.
6. **Frontera con el ilícito civil.** Cierra el § siguiente antes de seguir. Si no hay **dolo
   antecedente** sostenible, **dilo al usuario con claridad**: una denuncia abocada al archivo con
   imposición de costas y riesgo de una reconvención por denuncia falsa (art. 456 CP) es un mal
   servicio, no una posición combativa.

---

## Marco normativo — VERIFICADO contra el BOE el 2026-07-17

**Art. 248 CP** (vigente **10-4-2026**, redacción **LO 1/2026**) — tres párrafos:
- **Párr. 1 — definición:** «Cometen estafa los que, con **ánimo de lucro**, utilizaren **engaño
  bastante** para producir **error** en otro, induciéndolo a realizar un **acto de disposición** en
  **perjuicio** propio o ajeno.»
- **Párr. 2 — PENA: prisión de 6 meses a 3 años.** Criterios de fijación: importe de lo defraudado,
  quebranto económico causado al perjudicado, relaciones entre este y el defraudador, medios
  empleados y demás circunstancias que valoren la gravedad. **Úsalos expresamente**: son la sede
  natural de la petición de pena, y casi nadie los argumenta.
- **Párr. 3 — delito leve:** cuantía **≤ 400 €** → **multa de 1 a 3 meses**, salvo que concurra
  alguna circunstancia del art. 250. **Multirreincidencia:** si el culpable fue condenado
  ejecutoriamente al menos por **tres delitos de la misma naturaleza del capítulo**, y **al menos uno
  de ellos leve** → se impone la **pena del párrafo segundo**. No se computan antecedentes cancelados
  o que debieran serlo.

**Art. 249 CP** (vigente **12-1-2023**, LO 14/2022) — **estafa informática y con instrumentos de
pago**, prisión 6 meses – 3 años. **Solo se cita si los hechos encajan aquí:**
- 249.1.a) manipulación informática / interferencia en sistema de información / alteración de datos →
  **transferencia no consentida** de activo patrimonial.
- 249.1.b) uso fraudulento de **tarjetas** de crédito o débito, cheques de viaje u otro instrumento de
  pago distinto del efectivo, o de sus datos.
- 249.2 fabricación, importación, posesión o facilitación de dispositivos/programas para cometerlas;
  sustracción o adquisición ilícita de tarjetas para uso fraudulento.
- 249.3 posesión/adquisición/transferencia/distribución de tarjetas sabiendo su origen ilícito → pena
  en su **mitad inferior**.
> **Criterio de deslinde:** si hubo una **persona engañada** que decidió disponer, es art. 248. Si el
> desplazamiento patrimonial se logró **sobre una máquina o un sistema**, sin engaño a persona, es
> art. 249. En el *phishing* clásico conviven ambos: engaño a la víctima (248) + transferencia por
> manipulación (249). Motiva la elección; no acumules por inercia.

**Art. 250.1 CP** (vigente **10-4-2026**, LO 1/2026) — estafa agravada: **prisión 1-6 años y multa
6-12 meses**:
1.º cosas de primera necesidad, **viviendas** u otros bienes de reconocida utilidad social.
2.º abuso de firma de otro, o sustracción/ocultación/inutilización de proceso, expediente, protocolo
o documento público u oficial.
3.º bienes del patrimonio artístico, histórico, cultural o científico.
4.º **especial gravedad**, atendiendo a la entidad del perjuicio y a la **situación económica en que
deje a la víctima o a su familia**.
5.º **valor de la defraudación > 50.000 €**, o que **afecte a un elevado número de personas**.
6.º **abuso de relaciones personales** entre víctima y defraudador, o aprovechamiento de su
**credibilidad empresarial o profesional**.
7.º **estafa procesal** (manipulación de pruebas en procedimiento judicial que induce al juez a
dictar resolución que perjudica económicamente a otra parte o a un tercero).
8.º **multirreincidencia**: condena ejecutoria previa por **al menos tres delitos menos graves o
graves del capítulo, de la misma naturaleza**. No computan antecedentes cancelados o que debieran
serlo.

**Art. 250.2 CP:** concurrencia de **4.º, 5.º, 6.º o 7.º CON el 1.º** → **prisión 4-8 años y multa
12-24 meses**. **La misma pena si el valor de la defraudación supera los 250.000 €.**

**Art. 251 CP** — **estafa impropia** (verificado, sin cambios desde 1996), **prisión 1-4 años**:
1.º atribuirse falsamente facultad de disposición sobre cosa mueble o inmueble (por no haberla tenido
nunca o por haberla ya ejercitado) y enajenarla, gravarla o arrendarla.
2.º disponer de cosa **ocultando una carga**, o **doble venta** (haberla enajenado como libre y
gravarla o enajenarla de nuevo antes de la transmisión definitiva).
3.º **otorgar en perjuicio de otro un contrato simulado**.
> No exige engaño bastante ni error en los términos del 248: es un tipo autónomo. En fraudes
> inmobiliarios, **compruébalo antes de forzar el 248**.

**Art. 251 bis CP** — **personas jurídicas** (verificado; redacción **LO 5/2010**, vigente
23-12-2010). Cuando conforme al **art. 31 bis** la persona jurídica sea responsable de los delitos de
**esta Sección**:
- a) **multa del triple al quíntuple** de lo defraudado, si la pena de prisión de la persona física es
  **> 5 años**;
- b) **multa del doble al cuádruple** de lo defraudado, en el resto de casos.
- Conforme al **art. 66 bis**, además pueden imponerse las penas de las letras **b) a g) del art.
  33.7**.
> ⚠️ **Solo procede si se dirige la acción contra la persona jurídica.** No lo cites como adorno: el
> 251 bis no es una coletilla de la denuncia contra el administrador. Si acusas a la sociedad,
> identifícala y razona el **art. 31 bis** (delito cometido por quienes la representan o por
> subordinados, en su nombre, por cuenta y **beneficio directo o indirecto**, con incumplimiento
> grave de los deberes de supervisión). **Verifica el art. 31 bis con `buscar_articulo` antes de
> desarrollarlo.**

**Concursos y reglas de aplicación:**
- **Art. 74 CP — delito continuado** (verificado): plan preconcebido o aprovechamiento de idéntica
  ocasión, pluralidad de acciones que infringen el mismo precepto → pena de la infracción más grave
  **en su mitad superior**, pudiendo llegar hasta la mitad inferior de la superior en grado.
  **Art. 74.2 (patrimoniales):** se atiende al **perjuicio total causado**; y el tribunal impondrá
  motivadamente la pena **superior en uno o dos grados** si el hecho reviste **notoria gravedad** y
  ha perjudicado a **una generalidad de personas**.
  > **Clave práctica:** en estafas seriadas de poca cuantía, la continuidad delictiva **suma los
  > importes**, y la suma puede cruzar el umbral de los 400 € (deja de ser leve) o el de los 50.000 €
  > (art. 250.1.5.º). Alégalo expresamente; es lo que convierte muchas denuncias «pequeñas» en un
  > delito menos grave.
- **Falsedad documental**: si hubo documento falso como instrumento del engaño, valora el concurso.
  **Verifica los arts. 390-395 CP con `buscar_articulo` antes de citarlos.**

**Procesal:** arts. 259, 264, 266, 269 LECrim (deber y forma de denunciar). **Art. 269 LECrim**
(verificado): formalizada la denuncia se procederá **inmediatamente** a la comprobación del hecho,
**salvo** que no revista carácter de delito o la denuncia fuere **manifiestamente falsa**.

---

## La batalla real: negocio civil criminalizado

**Esto decide el asunto.** La mayoría de las denuncias por estafa se archivan aquí, no en la prueba.

- El **incumplimiento contractual NO es estafa**. Que alguien no pague, no entregue o no devuelva es,
  por sí solo, materia **civil**. El orden penal no es un mecanismo de cobro reforzado.
- Lo que convierte el incumplimiento en estafa es el **DOLO ANTECEDENTE**: el propósito de no cumplir
  **ya existía al tiempo de contratar**, y el contrato fue el **instrumento del engaño**, no una
  obligación que después se frustró.
- El ***dolus subsequens* NO integra estafa**: quien contrató de buena fe y **después** decidió no
  cumplir, o no pudo cumplir, no comete estafa. Sobrevenir no es preordenar.
- **Engaño BASTANTE:** el engaño ha de ser idóneo *ex ante* para vencer las cautelas exigibles al
  concreto perjudicado. Se pondera junto con los **deberes de autoprotección** de la víctima —y aquí
  la valoración cambia mucho según se trate de un consumidor o de un empresario con medios de
  comprobación a su alcance.

**Cómo se acredita el dolo antecedente — indícalo en el escrito con hechos, no con adjetivos.**
Busca y alega los **indicios externos** disponibles:
- **insolvencia o inactividad de la sociedad ya al contratar** (cuentas no depositadas, sin
  trabajadores, sin actividad real, capital simbólico, domicilio ficticio);
- **desvío inmediato** de los fondos a finalidad distinta de la pactada, o a cuentas personales;
- **imposibilidad originaria** de la prestación (se vende lo que no se tiene o no se puede entregar);
- **apariencia fabricada**: sede, web, cargos, sellos, referencias, avales, contratos o
  certificaciones inexistentes;
- **pluralidad de perjudicados** con idéntico patrón (revela plan, no infortunio);
- **desaparición** tras el cobro; cambio de identidad, de teléfono o de domicilio;
- **pago inicial simbólico** para generar confianza antes de la disposición principal.

> ⚠️ **Regla de honestidad profesional.** Si los indicios solo acreditan un incumplimiento, **dilo**.
> Propón la vía civil. No maquilles un impago de estafa: el archivo es seguro y la denuncia puede
> volverse contra el cliente.

**Verifica la doctrina, no la cites de memoria.** Antes de invocar jurisprudencia sobre dolo
antecedente, engaño bastante o autoprotección de la víctima, **búscala con `buscar_sentencias`** (TS,
Sala Segunda) y **confirma cada cita con `buscar_por_cita`**. ⛔ **Prohibido escribir un ECLI, un ROJ,
una fecha o un ponente que no venga del conector.**

---

## Elementos del tipo — subsúmelos UNO A UNO

No los enuncies: **acredítalos**. Por cada elemento, un párrafo con el hecho y su **folio**.

| Elemento | Qué debes acreditar | Riesgo si falla |
|---|---|---|
| **Engaño bastante** | Maniobra concreta, previa a la disposición, idónea *ex ante* | Atipicidad |
| **Error** | El engaño **causó** la falsa representación; nexo, no coincidencia | Atipicidad |
| **Acto de disposición** | Acto **voluntario** del engañado que merma su patrimonio | Puede ser hurto/apropiación, no estafa |
| **Perjuicio** | Patrimonial, **evaluable**, propio o ajeno | Sin perjuicio no hay estafa consumada |
| **Ánimo de lucro** | Propósito de enriquecimiento propio o de tercero | Atipicidad |
| **Dolo antecedente** | Propósito de no cumplir **ya al contratar** | **Negocio civil criminalizado → archivo** |

**Orden causal — es un requisito, no una redacción:** engaño → error → disposición → perjuicio. La
secuencia debe leerse en ese orden en el relato. Si el «engaño» es **posterior** a la disposición, no
hay estafa: revisa la calificación.

**Autoría y participación:** identifica el rol de cada denunciado (autor, **cooperador necesario**,
cómplice) con **actos concretos**. No imputes en bloque a todos los administradores por serlo: la
responsabilidad penal es personal y por hechos propios. En instrucción basta el **indicio racional**,
pero el indicio ha de ser **de cada uno**.

---

## Estructura del escrito

1. **Encabezamiento:** «**A LA SECCIÓN DE INSTRUCCIÓN DEL TRIBUNAL DE INSTANCIA DE [PARTIDO] QUE POR
   REPARTO CORRESPONDA**». (Nomenclatura del art. 14 LECrim tras la LO 1/2025, vigente 3-10-2025. Si
   el perfil del despacho acredita otro uso en su partido, respétalo.)
2. **Comparecencia:** denunciante (persona física, o mercantil con `[ENTIDAD]`, `[CIF]`,
   `[DOMICILIO]`) y letrado/a. **La denuncia no exige procurador ni poder especial** — a diferencia de
   la querella (art. 277 LECrim). Si se comparece con procurador, indícalo, pero no lo presentes como
   requisito.
3. **Fórmula de interposición:** «formula **DENUNCIA** por un posible delito de estafa del **art. 248
   CP** [+ «agravada del art. 250.1.[ordinal] CP» / «impropia del art. 251.[ordinal] CP» /
   «informática del art. 249.1.[letra] CP» — **solo lo que corresponda**] contra `[DENUNCIADO]` y
   contra cuantos resulten de la investigación».
4. **HECHOS**, numerados (PRIMERO, SEGUNDO…), **cronológicos** y circunstanciados: origen de la
   relación, maniobra de engaño, error, entrega/disposición, destino real de los fondos, descubrimiento
   y reclamación. Un hecho por ordinal. **Cada afirmación con su folio o su documento.**
5. **CALIFICACIÓN JURÍDICA:** subsunción elemento por elemento (tabla anterior) + **dolo antecedente**
   con sus indicios + continuidad (art. 74) si procede + agravación del art. 250 con su ordinal exacto
   + persona jurídica (art. 251 bis) **si se dirige contra ella**.
6. **DILIGENCIAS que se interesan** (§ siguiente).
7. **RESPONSABILIDAD CIVIL:** cuantificación y fundamento (§ siguiente).
8. **DOCUMENTOS** que se acompañan, numerados y correlacionados con los hechos.
9. **SUPLICO:** admisión a trámite, **incoación de diligencias previas**, práctica de las diligencias
   interesadas y —si procede— medidas cautelares reales.
10. **OTROSÍES** (medidas cautelares, designación de domicilio a efectos de notificaciones, copias) —
    lugar, fecha y firma.

> **Anclaje al folio — regla innegociable.** Todo hecho afirmado se ancla al **folio de las
> actuaciones** («folio X»), o al documento que se acompaña («documento nº X»). En la denuncia inicial
> no hay folios aún: **ancla al documento**, y en cuanto haya actuaciones **cita folio**. Un hecho sin
> ancla es una alegación, y una alegación no sostiene un indicio racional.

---

## Diligencias útiles — pídelas ya en la denuncia

Pedirlas tarde es no pedirlas: rige el **art. 324 LECrim** (12 meses prorrogables; sin auto de
prórroga previo al vencimiento las diligencias posteriores **no son válidas**). Para el detalle y para
diligencias que afecten a derechos fundamentales → **`solicitud-diligencias-instruccion-catalogo`**.

- **Documental bancaria (la decisiva):** oficio a `[ENTIDAD]` bancaria para que aporte **titularidad y
  autorizados** de la cuenta de destino, **extractos** del periodo, y la **trazabilidad** de los
  fondos (transferencias de salida, beneficiarios finales, retiradas en efectivo). El desvío inmediato
  del dinero a finalidad distinta de la pactada es **el mejor indicio de dolo antecedente**: pídelo
  siempre.
- **Mercantil:** nota simple o certificación del **Registro Mercantil** (administradores y fecha de su
  nombramiento, objeto, capital, **depósito de cuentas**). Si la sociedad no depositaba cuentas o
  estaba inactiva al contratar, es un indicio de primer orden. (Puede consultarse con
  `buscar_empresa_mercantil`.)
- **Declaración** de los investigados (art. 775 LECrim) y **testificales** `[TESTIGO]` de quienes
  presenciaron la maniobra o intervinieron en la negociación.
- **Oficios** a AEAT/TGSS (alta real de la actividad, trabajadores), a operadoras (titularidad de
  líneas), a plataformas (titularidad de perfiles/webs).
- **Pericial** contable o informática forense si el engaño es documental o digital.
- **Aseguramiento de fuentes de prueba volátiles**: web, perfiles, chats, publicidad. Pide su
  **preservación** cuanto antes y aporta acta notarial o volcado si el cliente lo tiene: desaparecen.
- **Averiguación patrimonial** y **medidas cautelares reales** (embargo/fianza) — solicítalas
  **pronto**: en estafa el dinero se disipa en semanas. Es el error de gestión más caro.

---

## Responsabilidad civil derivada del delito

Se ejercita **en el proceso penal** salvo reserva o renuncia expresa (arts. 100, 108-117 LECrim; arts.
109-126 CP).
- **Contenido:** restitución, reparación del daño e indemnización de perjuicios (art. 100 LECrim,
  verificado).
- **Art. 116 CP (verificado):** todo responsable criminal lo es civilmente si del hecho se derivan
  daños; con **varios responsables**, el tribunal **señalará la cuota** de cada uno; autores y
  cómplices responden **solidariamente entre sí por sus cuotas** y **subsidiariamente** por las de los
  demás (primero bienes de los autores, después de los cómplices). **116.3:** la responsabilidad penal
  de la persona jurídica lleva consigo su responsabilidad civil **solidaria** con las personas físicas
  condenadas por los mismos hechos.
- **Cuantifica**: principal + intereses. **Verifica con `buscar_articulo`** el precepto de intereses
  que vayas a citar antes de escribirlo.
- **Responsable civil subsidiario** (art. 120 CP) y **partícipe a título lucrativo** (art. 122 CP):
  quien se lucró del delito sin ser responsable penal responde hasta la cuantía de su
  participación —vía útil contra testaferros y familiares receptores de los fondos. **Verifica ambos
  con `buscar_articulo` antes de invocarlos.**
- Advierte al cliente: **la renuncia debe ser expresa, clara y terminante** (art. 110 II LECrim,
  verificado); no personarse **no** equivale a renunciar.

---

## Errores típicos que hunden el escrito

1. **Citar el art. 249 en una estafa común.** Errata capital → ver banner.
2. **Denunciar «por los arts. 248, 249, 250 y 251 bis» en bloque.** Delata plantilla y desconocimiento:
   son modalidades **incompatibles entre sí**. Elige y motiva.
3. **Invocar un ordinal del art. 250 sin comprobarlo.** El **5.º** es la cuantía > 50.000 € o el
   elevado número de personas; el **8.º** es la multirreincidencia. Verifícalo siempre.
4. **Aplicar el art. 250.2 por cuantía sin llegar a 250.000 €**, o sin la concurrencia del 1.º con
   4.º/5.º/6.º/7.º.
5. **No hacer la comparación de leyes** en hechos anteriores al 10-4-2026 (art. 2.2 CP).
6. **Pedir multirreincidencia para hechos anteriores al 10-4-2026** → retroactividad desfavorable.
7. **Confundir incumplimiento con estafa**: relato sin **dolo antecedente** → archivo.
8. **Relato desordenado** que rompe la secuencia engaño → error → disposición → perjuicio.
9. **Hechos sin folio ni documento.**
10. **Imputar en bloque** a todos los administradores sin actos concretos de cada uno.
11. **Olvidar la continuidad (art. 74)** en estafas seriadas → se pierde la agravación y, a veces, el
    propio carácter no leve del delito.
12. **No pedir la traza bancaria** ni las cautelares reales a tiempo: se gana el pleito y no se cobra.
13. **Dejar prescribir la estafa leve** (1 año).
14. **Creer que la denuncia interrumpe la prescripción.** No: **solo suspende 6 meses** (art. 132.2.2.ª
    CP). Sin resolución judicial motivada en ese plazo, el reloj **sigue corriendo desde la fecha de la
    denuncia**.
15. **Creer que denunciar convierte en parte.** No: hay que personarse.
16. **Citar jurisprudencia de memoria.** ⛔ Prohibido.

---

## Datos personales — categoría reforzada

- Usa siempre marcadores: `[DENUNCIADO]`, `[PERJUDICADO]`, `[TESTIGO]`, `[ENTIDAD]`, `[CIF]`,
  `[DOMICILIO]`, `[IMPORTE]`. **Nunca reproduzcas datos reales de terceros en la salida.**
- ⚠️ En penal, los datos relativos a **infracciones y condenas penales** son **categoría especial del
  art. 10 RGPD**: tratamiento reforzado. Cuidado extremo con **menores** y **víctimas**.
- No construyas el slug del expediente con el nombre del cliente (ver `CLAUDE.md` y
  `PROTECCION-DATOS.md`): usa `descriptor-delito-año`.

---

## Reglas de trabajo

- **Cifras y artículos:** la fuente única es `references/anclas-normativas-penal.md` (§ 7.1) o una
  verificación en el momento con **`buscar_articulo`**. ⛔ **Prohibido inventar** penas, plazos,
  ordinales o artículos. Lo que no puedas verificar → márcalo **`[verificar]`** y **dilo al usuario**.
- **Jurisprudencia:** siempre con `buscar_sentencias` / `buscar_por_cita` / `leer_sentencias`. ⛔ Nunca
  un ECLI/ROJ/fecha/ponente de memoria.
- **Instruye el Juez de Instrucción** (Sección de Instrucción del Tribunal de Instancia). ⛔ **No
  existe el «fiscal instructor»**: esa reforma está en tramitación (prevista 1-1-2028) y **no es
  Derecho vigente**. No la menciones jamás, ni cites un «art. 4 bis EOMF».
- ⛔ **Nada de MASC**: es requisito del orden **civil**. En penal no hay intento previo ni burofax
  preceptivo.
- Antes de dar por buena una cifra de estas anclas, comprueba la **regla de caducidad** (§ del
  documento): si han pasado más de 6 meses desde el 2026-07-17, **re-verifica**.

## Entrega

Genera el escrito final en **Word `.docx`** con la skill **`docx`**, maquetado como escrito judicial
(encabezamiento, hechos, calificación, suplico, otrosíes), listo para presentación por **LexNET**.
