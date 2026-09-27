---
name: violencia-genero-orden-proteccion
description: >-
  Violencia de género y doméstica — competencia de las Secciones de Violencia sobre la Mujer (art. 89 LOPJ y art. 14.5 LECrim; el 87 ter LOPJ está SUPRIMIDO), orden de protección del art. 544 ter (audiencia urgente, 72 horas, estatuto integral, medidas civiles 30+30), medidas cautelares del art. 544 bis reescrito por la LO 1/2026, quebrantamiento del art. 468 CP y dispensa del art. 416 LECrim. Sirve a la defensa y a la acusación. Actívala ante "orden de protección", "alejamiento", "violencia de género", "violencia doméstica", "juzgado de violencia sobre la mujer", "quebrantamiento", "544 ter", "544 bis", "dispensa de declarar", "LO 1/2004", "pulsera telemática", "violencia contra la infancia". Es el régimen ESPECIALIZADO: úsala siempre que la relación entre las partes sea de pareja o expareja, familiar o de violencia contra la infancia. Si no concurre ese contexto, la prohibición de aproximación genérica del art. 544 bis y las demás cautelares se tramitan con /medidas-cautelares-penales-catalogo.
---

# Violencia de género y orden de protección

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Competencia** (art. 89 LOPJ; art. 14.5 a 14.7 LECrim) → `buscar_articulo` (`ley="LOPJ"` / `ley="LECrim"`).
- **Orden de protección y medidas del art. 544 bis** → `buscar_articulo` (`ley="LECrim"`, `articulo="544 ter"` y `"544 bis"`).
- **Tipos y penas** (arts. 153, 171, 172, 173.2 y 468 CP) → `buscar_articulo` (`ley="CP"`).
- **LO 1/2004 y Estatuto de la víctima** → `buscar_boe` para su ID BOE y `buscar_articulo` con él (el Estatuto es `BOE-A-2015-4606`).
- **Consentimiento de la víctima en el quebrantamiento y dispensa del art. 416** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`; para la dispensa, `fecha_desde="25/06/2021"`) + `leer_sentencias` con `parrafos=3`.
- **Proporcionalidad de las cautelares y presunción de inocencia** → `buscar_sentencias` (`base="TC"`).
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Materia sensible. Rigor y cero sesgo. Esta skill sirve a las dos posiciones.**

- **Acusación:** construir la protección con el instrumento correcto y en plazo, sin perder el asunto
  por un defecto procesal.
- **Defensa:** ejercer la presunción de inocencia y controlar la proporcionalidad de las cautelares.
  Es un derecho, no una concesión.

**La violencia de género es un fenómeno real y grave; la presunción de inocencia es un derecho
fundamental de todo investigado. Las dos cosas son verdad a la vez** y esta skill las trata así.

> **Verifica cada precepto con `buscar_articulo` antes de citarlo.** Aquí se da la *regla*, no el BOE:
> el texto está a una llamada de distancia. Anclas: `references/anclas-normativas-penal.md` §§ 7.2,
> 11 bis y 11 ter. Verificado el 2026-07-17.

---

## 🚨 0. Dos erratas estructurales — léelas antes de escribir nada

### 0.1 El art. 87 ter LOPJ está SUPRIMIDO

| Cita **INCORRECTA** | Cita **VIGENTE** |
|---|---|
| «art. 87 ter LOPJ» (competencia de los JVM) | **art. 89 LOPJ** (LO 1/2025, desde 23-1-2025) + **art. 14.5 LECrim** |
| «art. 44.5 LOPJ» (prohibición de mediación) | **art. 89.9 LOPJ** — y veda **todos los MASC**, no solo la mediación |

> El **art. 44.5 de la LO 1/2004** fue el que en su día *introdujo* el hoy derogado 87 ter LOPJ: de ahí
> la confusión. El **art. 44 LOPJ** regula otra cosa (preferencia del orden penal). Todo material que
> cite el 87 ter como vigente está desfasado.

### 0.2 Nomenclatura — art. 14 LECrim (vigente **3-10-2025**, DF 38.3 LO 1/2025)

| Denominación **DEROGADA** | Denominación **VIGENTE** |
|---|---|
| Juzgado de Violencia sobre la Mujer | **Sección con competencia en materia de violencia sobre la mujer** del Tribunal de Instancia |
| Juzgado de Instrucción / de lo Penal | **Sección de Instrucción / de lo Penal** del Tribunal de Instancia |
| — (no existía) | ⭐ **Sección de Violencia contra la Infancia y la Adolescencia** (art. 14.6) |

> **Úsala en encabezamientos y en competencia.** Excepción: al **transcribir literalmente** un precepto
> (544 ter, 962.5…), reprodúcelo como está — la LO 1/2025 **no** actualizó esos textos, que siguen
> diciendo «Juez de guardia» o «Juzgado de Violencia sobre la Mujer». Advierte del desajuste.
> ⚠️ El propio **art. 14.4** conserva la referencia a «la circunscripción del **Juzgado de Violencia
> sobre la Mujer**»: descoordinación del legislador, verificada. No la tomes por vigencia del órgano.

---

## 1. Competencia — art. 89 LOPJ y art. 14.5 LECrim (verificados)

### 1.1 Orden PENAL (89.5 LOPJ = 14.5 LECrim)

- **a)** **Instrucción** de homicidio, aborto, lesiones, lesiones al feto, contra la libertad, contra la
  integridad moral, contra la libertad e indemnidad sexual, contra la intimidad y la propia imagen,
  contra el honor, **o cualquier otro delito cometido con violencia o intimidación**, contra **quien sea
  o haya sido esposa o mujer ligada por análoga relación de afectividad, aun sin convivencia**; y sobre
  descendientes o menores/personas con discapacidad del entorno de la esposa o conviviente, **cuando
  también se haya producido un acto de violencia de género**.
  > **El inciso final es un filtro real**, no retórico: respecto de descendientes y menores exige que
  > **además** concurra un acto de violencia de género.
- **b)** Delitos **contra las relaciones familiares** con víctima de la letra a).
- **c)** **Órdenes de protección**, **sin perjuicio de las competencias del juez de guardia** (§ 2).
- **d)** **Conocimiento y fallo de los DELITOS LEVES** que la ley atribuya, con víctima de la letra a).
- **e)** **Sentencia de conformidad** en los casos legalmente establecidos. **f)** Reconocimiento mutuo
  en la UE.
- **g)** ⭐ Instrucción del **quebrantamiento del art. 468 CP** cuando la ofendida sea de la letra a) — o
  de la letra h).
- **h)** ⭐ Instrucción de **delitos contra la libertad sexual** (título VIII libro II CP), **mutilación
  genital femenina**, **matrimonio forzado**, **acoso con connotación sexual** y **trata con fines de
  explotación sexual**, **cuando la ofendida sea mujer**. **En vigor desde el 3-10-2025.** Ya **no** se
  limita a la violencia de pareja: es la ampliación competencial más relevante.

### 1.2 ⭐ Sección de Violencia contra la Infancia y la Adolescencia — art. 14.6 (ÓRGANO NUEVO)

Instruye, con víctima **niño, niña o adolescente**: homicidio, aborto, lesiones y lesiones al feto;
delitos contra la libertad, torturas e integridad moral, intimidad, propia imagen e inviolabilidad del
domicilio, honor, relaciones familiares, **o cualquier delito con violencia o intimidación**; **trata
(art. 177 bis)** con al menos una víctima menor; y el **quebrantamiento del art. 468** con víctima menor.
Además: **medidas cautelares de protección** de víctimas menores (sin perjuicio del juez de guardia),
**conocimiento y fallo de delitos leves** con víctima menor, **sentencia de conformidad** y
reconocimiento mutuo en la UE.

> **⭐ Art. 14.7 — regla de conflicto:** si los hechos pueden ser conocidos por la Sección de Violencia
> contra la Infancia **y** por la de Violencia sobre la Mujer, la competencia es **en todo caso de la
> segunda**. Compruébalo siempre que haya menores implicados: es el error de competencia más probable
> del órgano nuevo.

### 1.3 ⭐ *Vis atractiva* civil (89.6 y 89.7 LOPJ)

**89.6 — materias** (11, verifícalas): crisis matrimonial y régimen económico; guarda, custodia y
alimentos de hijos menores; modificación de medidas; filiación y adopción; relaciones paternofiliales;
protección del menor; jurisdicción voluntaria de familia; liquidación del régimen instada por los
herederos de la mujer víctima; resoluciones eclesiásticas y extranjeras; art. 160 CC.

**⭐ 89.7 — competencia EXCLUSIVA Y EXCLUYENTE: CUATRO requisitos SIMULTÁNEOS:**
1. Proceso civil sobre **materia del 89.6**;
2. **alguna parte sea víctima** de violencia de género (89.5.a) **o sexual** (89.5.h);
3. **alguna parte esté imputada** como autor, inductor o cooperador necesario;
4. se hayan **iniciado actuaciones penales** ante la Sección **o** se haya **adoptado orden de
   protección**.

> **No opera por la mera denuncia.** Comprueba los cuatro. El **4.º** es el que se discute.

- **89.8:** si el juez aprecia que los actos, **«de forma notoria»**, no son expresión de violencia de
  género o sexual, **puede inadmitir** y remitir al órgano competente. *(Estándar exigente: no lo infles.)*
- **⭐ 89.9 — MASC VEDADOS:** «está vedada la utilización de los **medios adecuados de solución de
  controversias**». Prohibición general y sin excepciones. Recuerda además que el MASC de la LO 1/2025 es
  requisito del orden **civil** y no rige en penal en ningún caso.

---

## 2. ⭐ Orden de protección — art. 544 ter LECrim (redacción LO 8/2021)

### 2.1 Presupuesto (544 ter.1) — dos requisitos acumulativos

- **Indicios fundados** de delito contra la vida, integridad física o moral, libertad sexual, libertad o
  seguridad de alguna de las personas del **art. 173.2 CP**; **y**
- **situación objetiva de riesgo** que **requiera** alguna de las medidas del artículo.

> **El debate real casi nunca está en los indicios, sino en la SITUACIÓN OBJETIVA DE RIESGO.** Es
> requisito autónomo y «objetiva» significa que **no basta el temor subjetivo manifestado**. Ahí litiga
> la defensa; ahí la acusación debe **acreditar**, no afirmar.

### 2.2 Legitimación y solicitud (544 ter.2 y .3)

**De oficio**, a instancia de la **víctima**, de persona con alguna relación del 173.2, o del **Ministerio
Fiscal**. Las **entidades u organismos asistenciales** que conozcan los hechos **deben comunicarlo
inmediatamente** al juez de guardia o al Fiscal (sin perjuicio del art. 262). Se solicita ante autoridad
judicial, Fiscal, **FCSE**, oficinas de atención a la víctima o **servicios sociales**; se remite **de
forma inmediata** al juez competente. **Dudas de competencia territorial: inicia y resuelve el juez ante
el que se solicitó** (regla antibloqueo).

### 2.3 ⭐ Audiencia urgente y las 72 horas (544 ter.4)

El **Juez de guardia** convoca **audiencia urgente**: víctima o su representante, solicitante, **presunto
agresor asistido en su caso de Abogado**, y **Ministerio Fiscal**. Puede sustanciarse **simultáneamente**
con la del art. 505, la del art. 798 (juicio rápido) o el juicio por delito leve.

> **⭐ Precisión verificada:** «En cualquier caso la audiencia habrá de **celebrarse** en un plazo máximo
> de **setenta y dos horas desde la presentación de la solicitud**». Las 72 horas son para **CELEBRAR LA
> AUDIENCIA**, contadas **desde la solicitud** — **no** son un plazo genérico «para resolver». Celebrada,
> el juez **resuelve por auto** sobre la orden y sobre el **contenido y vigencia** de las medidas.

- **En la audiencia:** el juez adopta medidas para **evitar la confrontación** entre presunto agresor y
  víctima, hijos y familiares, **disponiendo que declaren POR SEPARADO**. *(Exígelo la acusación;
  contrólalo la defensa: su omisión es un defecto del acto.)*
- El **Juez de instrucción puede adoptar en cualquier momento** las medidas del **544 bis** (§ 3).

### 2.4 Estatuto integral y medidas penales (544 ter.5 y .6)

**Estatuto integral de protección**: medidas **penales** + **civiles** + **de asistencia y protección
social**. **Puede hacerse valer ante cualquier autoridad y Administración pública.**

> **Por eso se pide la orden de protección y no solo un 544 bis:** es la **llave de acceso** a derechos
> laborales, prestaciones y ayudas de la **LO 1/2004**. *(Verifica cada derecho con `buscar_articulo`
> antes de prometer nada: no los enumeres de memoria.)*

**Medidas penales (.6):** cualesquiera de las previstas en la legislación procesal criminal, con sus
requisitos y vigencia generales, atendiendo a la **protección integral e inmediata** de la víctima y de
las personas bajo su patria potestad, tutela, curatela, guarda o acogimiento.

### 2.5 Medidas civiles (544 ter.7)

- **Han de solicitarse** por la víctima o su representante, **o por el Fiscal si hay hijos menores o
  personas con capacidad modificada**; salvo que ya las acordara el orden civil, y sin perjuicio del
  **art. 158 CC**.
- **⭐ De oficio obligatorio:** si hay **menores o personas con discapacidad que convivan con la víctima y
  dependan de ella**, el juez **debe pronunciarse en todo caso, incluso de oficio**.
- **Contenido:** patria potestad, guarda; **uso de la vivienda familiar**; **custodia**; **suspensión o
  mantenimiento de visitas**; **alimentos**; y cuanto evite peligro o perjuicio a los menores.
- **⭐ Suspensión de visitas:** con **medidas penales** e **indicios fundados de que los hijos menores
  presenciaron, sufrieron o convivieron con la violencia**, la autoridad judicial **suspenderá** el
  régimen de visitas, de oficio o a instancia de parte. **Excepción: solo A INSTANCIA DE PARTE**, por
  **resolución motivada en el interés superior del menor** y **previa evaluación de la relación
  paternofilial**.
  > **Defensa:** la excepción existe pero **hay que pedirla**, y motivada en el **interés del menor** —no
  > en el del investigado—, que es el estándar legal.

**🚨 VIGENCIA — el error más frecuente de la materia. Literal verificado:**
> «Las medidas de carácter civil contenidas en la orden de protección tendrán una **vigencia temporal de
> treinta días**. Si dentro de este plazo fuese incoado a instancia de la víctima o de su representante
> legal un proceso de familia ante la jurisdicción civil, las medidas adoptadas permanecerán en vigor
> durante los **treinta días siguientes a la presentación de la demanda**. En este término las medidas
> **deberán ser ratificadas, modificadas o dejadas sin efecto** por el Juez de primera instancia que
> resulte competente.»

**Calendario — a la agenda el día 0:**
1. **Día 0:** orden con medidas civiles → **30 días**.
2. **Antes del día 30:** **demanda de familia** ante el civil, **a instancia de la víctima o su
   representante**. Si no → **las medidas civiles decaen** (las penales, no).
3. **Presentada:** **30 días más**.
4. **En ese término:** el **Juez de primera instancia** debe **ratificar, modificar o dejar sin efecto**.
   **Hay que instarlo: no ocurre solo.**

> **Es una caducidad que corre en silencio.** Una víctima con vivienda atribuida y custodia puede perder
> ambas por no presentar la demanda civil a tiempo, con la orden penal viva dando falsa sensación de
> cobertura. **Advíértelo por escrito el día uno.**

### 2.6 Notificación, información, registro (544 ter.8 a .11)

**.8** comunicación inmediata por el LAJ, mediante **testimonio íntegro**, a la víctima y a las
Administraciones competentes. **⭐ .9** deber de **informar permanentemente a la víctima** de la situación
procesal del investigado y del alcance y vigencia de las medidas; **en particular, en todo momento de su
situación penitenciaria**. **.10** inscripción en el **Registro Central para la Protección de las
Víctimas** (art. 10 RGPD por definición). **.11** en procedimiento en curso, el órgano que conozca de la
causa puede acordar la orden.

---

## 3. ⭐ Art. 544 bis — REESCRITO por la LO 1/2026 (vigente 10-4-2026)

### 3.1 Presupuesto y estándar

En delitos del **art. 57 CP**, el juez puede, **de forma MOTIVADA** y **cuando resulte ESTRICTAMENTE
NECESARIO** para **proteger a la víctima** **o** ⭐ **evitar la reiteración delictiva** (finalidad añadida
por la LO 1/2026), imponer cautelarmente las medidas del apartado siguiente.

> **Doble filtro para la defensa:** «motivada» + «estrictamente necesario». No basta que sea conveniente
> ni prudente: la ley exige **necesidad estricta**, y una resolución de formulario **no cumple** el
> estándar. En sentido inverso, la LO 1/2026 **amplió** la finalidad legítima a la **reiteración
> delictiva**: facilita a la acusación fundar la medida más allá del riesgo para esta víctima concreta.

### 3.2 Contenido

**Prohibición de residir** y **prohibición de acudir** a determinado **lugar, barrio, municipio, provincia
u otra entidad local, o comunidad autónoma**; o de **aproximarse o comunicarse, con la graduación que sea
precisa**, a determinadas personas.

> **«Con la graduación que sea precisa»** es literal: la ley **no** impone un alejamiento estándar de 500
> metros. Pide graduación concreta y motivada.

### 3.3 ⭐⭐ PONDERACIÓN OBLIGATORIA — la novedad decisiva (literal verificado)

> «Para la adopción de estas medidas **se tendrán en cuenta la situación económica del inculpado y los
> requerimientos de su salud, situación familiar y actividad laboral. Se atenderá especialmente a la
> posibilidad de continuidad de esta última, tanto durante la vigencia de la medida como tras su
> finalización.**»

**Munición directa para la defensa frente a alejamientos desproporcionados.** «Se tendrán en cuenta», no
«podrán»: es **obligatoria**.

| Factor | Cómo acreditarlo |
|---|---|
| **Situación económica** | Nóminas, renta, cargas, pensiones que abona |
| **Salud** | Informes médicos, tratamientos, centro donde se dispensan |
| **Situación familiar** | Otros hijos, dependientes a su cargo, domicilio de estos |
| **⭐ Actividad laboral** | Contrato, centro de trabajo, radio de desplazamiento, **imposibilidad de mantener el empleo** |
| **⭐ Continuidad tras la medida** | Que la prohibición **no destruya el empleo de forma irreversible** |

**Escrito de la defensa:** (1) no discutas la protección en abstracto, discute **la extensión geográfica
concreta**; (2) **acredita documentalmente** los cuatro factores —alegarlos no basta—; (3) demuestra que
la prohibición pretendida **impide la continuidad laboral**; (4) invoca «estrictamente necesario» y la
atención especial a la continuidad laboral **también tras la medida**; (5) **ofrece SIEMPRE alternativa
graduada** (aproximación a la persona, domicilio y trabajo, en vez de prohibición territorial amplia). Un
escrito que solo pide que no se acuerde nada rara vez prospera.

> **Acusación:** la ponderación es obligatoria pero **no es un derecho de veto**: la ley manda
> **ponderar**, no **ceder**. Anticípate acreditando por qué la alternativa graduada **no protege
> suficientemente** en el caso concreto.

### 3.4 Incumplimiento y control telemático

- **Incumplimiento** → el juez **convoca la comparecencia del art. 505** para **prisión provisional**
  (art. 503), **orden de protección** (544 ter) u **otra medida más limitativa**, valorando **incidencia,
  motivos, gravedad y circunstancias**, **sin perjuicio de las responsabilidades que pudieran resultar**
  (→ art. 468 CP, § 6).
  > Doble consecuencia: comparecencia del 505 **y** posible delito. Explícaselo al cliente por escrito el
  > día de la notificación. Pero la ley **ordena valorar motivos y circunstancias**: no todo
  > incumplimiento lleva automáticamente a prisión.
- **Delitos del art. 3 LO 10/2022** → **control telemático** por **resolución motivada**. Conexos:
  **art. 48.4 CP** (control por medios electrónicos) y **⭐ art. 468.3 CP**: inutilizar o perturbar los
  dispositivos, **no llevarlos consigo** u omitir las medidas para su funcionamiento → **multa**.
  *(Delito autónomo: el cliente que se deja la pulsera cargando en casa está delinquiendo.)*

## 4. Art. 13 LECrim — la protección es una PRIMERA DILIGENCIA (LO 1/2026)

Las primeras diligencias incluyen **proteger a los ofendidos o perjudicados, a sus familiares o a otras
personas**, **o evitar la reiteración delictiva**, **pudiendo acordarse el 544 bis o la orden de
protección del 544 ter**. No es un incidente posterior: se acuerda desde el minuto uno.

Párrafo 2 (subsistente) — delitos por **internet, teléfono o TIC**: **retirada provisional de contenidos
ilícitos**, **interrupción de servicios** o **bloqueo** cuando radiquen en el extranjero. Relevante en
violencia digital (difusión no consentida, acoso, suplantación). **Pídelo expresamente: no se acuerda
solo.**

---

## 5. Tipos penales y penas accesorias — **verifica cada pena antes de citarla**

| Precepto | Regla que importa |
|---|---|
| **173.2** | Violencia **habitual**. **Mitad superior** si hay menores presentes, armas, domicilio común o de la víctima, o quebrantamiento del art. 48 |
| **⭐ 173.3** | **Habitualidad**: número de actos y **proximidad temporal**, **con independencia de que fueran sobre la misma o distintas víctimas** y **de que se enjuiciaran antes**. **No exige condenas previas** — es lo que más se discute |
| **⭐ 173.4** | Injuria o vejación **leve**: localización permanente **siempre en domicilio distinto y alejado**, TBC o multa (esta **solo** con el art. 84.2). **Solo perseguible mediante DENUNCIA** |
| **153.1 / .2** | Lesión de menor gravedad o maltrato de obra sin lesión: **.1** si la ofendida es o fue esposa o mujer ligada por análoga relación **aun sin convivencia**; **.2** demás personas del 173.2 |
| **153.3** | **Mitad superior**: menores presentes, armas, domicilio común o de la víctima, quebrantamiento |
| **⭐ 153.4** | El juez, **razonándolo en sentencia**, atendidas las circunstancias personales del autor y del hecho, **podrá imponer la PENA INFERIOR EN GRADO**. Petición estándar de la defensa: motívala y **pruébala** |
| **148.4.º / 5.º** | Lesiones del 147.1 **podrán** castigarse más gravemente si la víctima es o fue esposa/mujer ligada por análoga relación (4.º) o persona especialmente vulnerable conviviente (5.º). **Facultativo** |

**Alejamiento (arts. 57 y 48 CP):**
- **⭐ 57.2 — IMPERATIVO:** en los delitos del 57.1 contra cónyuge o persona ligada por análoga relación
  aun sin convivencia, ascendientes, descendientes, hermanos, menores del núcleo o personas bajo custodia,
  **«se acordará, en todo caso, la aplicación de la pena prevista en el apartado 2 del artículo 48»**.
  > **No es discrecional.** No gastes el informe pidiendo que no se imponga: **discute la extensión
  > temporal**, que sí es graduable.
- **57.1 párr. 2:** con condena a **prisión**, las prohibiciones duran **más** que la prisión impuesta y se
  cumplen **simultáneamente**. **57.3:** en **delitos leves**, prohibiciones del art. 48 por tiempo
  limitado *(verifica la cifra)*.
- **Art. 48:** **.1** residir/acudir; **.2** aproximación (a la víctima **en cualquier lugar donde se
  encuentre**, domicilio, trabajo y lugares frecuentados); **.3** comunicación por cualquier medio,
  incluidos informáticos o telemáticos; **.4** control electrónico.
  > ⭐ **Inciso del 48.2 que se pasa por alto constantemente:** la prohibición de aproximación deja **«en
  > suspenso, respecto de los hijos, el régimen de visitas, comunicación y estancia que se hubiere
  > reconocido en sentencia civil hasta el total cumplimiento de esta pena»**. **Automático, ex lege.**

---

## 6. ⭐ Quebrantamiento (art. 468 CP) y el consentimiento de la víctima

- **468.1:** quebrantar condena, medida de seguridad, prisión, medida cautelar, conducción o custodia.
- **⭐ 468.2:** «**Se impondrá en todo caso la pena de PRISIÓN**» a quien quebrante **una pena del art. 48**
  o medida cautelar o de seguridad de la misma naturaleza **cuando el ofendido sea del art. 173.2**, y a
  quien quebrante la **libertad vigilada**.
  > **«En todo caso» y prisión, sin alternativa de multa.** La diferencia con el 468.1 es radical y depende
  > solo de que el ofendido sea del 173.2. *(Verifica los marcos penales exactos.)*
- **468.3:** manipulación u omisión respecto de los **dispositivos telemáticos** → multa.
- **Competencia:** instrucción a la **Sección de Violencia sobre la Mujer** (**89.5.g) LOPJ / 14.5.g)
  LECrim**); si la víctima es **menor**, a la **Sección de Violencia contra la Infancia** (**14.6.d**) —
  **salvo concurrencia**, en que gana la de la Mujer (**14.7**).

### 🚨 El consentimiento de la víctima — **NO cites doctrina de memoria**

**La cuestión más litigiosa de la materia.** Supuesto cotidiano: prohibición de aproximación **vigente** y
víctima e investigado **reanudan voluntariamente** el contacto. ¿Hay delito del 468.2?

Términos del debate: **atipicidad** (el bien jurídico incluiría la libertad de la víctima; su
consentimiento excluiría la lesión; autonomía de la mujer adulta) frente a **tipicidad** (el bien jurídico
sería la **efectividad de las resoluciones judiciales**; la medida la impone el juez y la víctima **no
puede disponer de su vigencia**). Vías intermedias que se manejan: **error de prohibición** (art. 14.3 CP),
incidencia en la **culpabilidad**, atenuación, o **pedir la modificación o alzamiento** de la medida.

> ⛔ **PROHIBIDO afirmar cuál es la doctrina vigente de la Sala Segunda o citar resolución alguna (ECLI,
> ROJ, fecha, ponente) de memoria.** La jurisprudencia ha oscilado y un dato desfasado destruye el asunto
> y la credibilidad del letrado.
>
> **OBLIGATORIO antes de asesorar:** (1) `buscar_sentencias` con `"quebrantamiento 468.2 consentimiento de
> la víctima"`, `"reanudación de la convivencia quebrantamiento medida cautelar"`, `"468.2 error de
> prohibición alejamiento"` — `jurisdiccion: "PENAL"`, `base: "TS"`, `anios: 3-4`; (2) `leer_sentencias`
> las seleccionadas; (3) comprueba si hay **acuerdo de Pleno no jurisdiccional** aplicable y vigente;
> (4) cita **solo** lo verificado. Lo no verificable → `[verificar]` y **dilo al cliente**.

**Consejo que NO depende de la jurisprudencia y siempre es correcto:**
> **La vía limpia es pedir al juez la modificación o el alzamiento.** Mientras la resolución esté vigente,
> **el riesgo penal es real** con independencia de lo que la víctima quiera. Dile al cliente —por escrito—
> que **el consentimiento de la víctima NO deja sin efecto la resolución judicial** y que reanudar el
> contacto **antes** del alzamiento le expone al **468.2**.

---

## 7. ⭐ Dispensa del art. 416 LECrim — muy acotada desde el 25-6-2021

**Dispensados de declarar** (416.1): parientes en línea directa ascendente y descendente, **cónyuge o
persona unida por relación de hecho análoga a la matrimonial**, hermanos consanguíneos o uterinos y
colaterales consanguíneos hasta el 2.º grado civil. El juez **advierte** que no tiene obligación de
declarar en contra, **pero que puede hacer las manifestaciones que considere oportunas**, y **se consigna
la contestación**. También: **abogado** del procesado (416.2) e **intérpretes** (416.3).

**⭐ Las CINCO excepciones — literal verificado. La dispensa NO se aplica:**
> **1.º** Cuando el testigo tenga atribuida la **representación legal o guarda de hecho de la víctima
> menor de edad o con discapacidad** necesitada de especial protección.
> **2.º** Cuando se trate de un **delito grave**, el testigo sea **mayor de edad** y la víctima sea
> **menor de edad** o **persona con discapacidad** necesitada de especial protección.
> **3.º** Cuando **por razón de su edad o discapacidad el testigo no pueda comprender el sentido de la
> dispensa** (el juez le oirá previamente, pudiendo recabar peritos).
> **4.º** Cuando el testigo **esté o haya estado personado en el procedimiento como acusación particular**.
> **5.º** Cuando el testigo **haya aceptado declarar durante el procedimiento después de haber sido
> debidamente informado de su derecho a no hacerlo**.

> 🚨 **«La víctima siempre puede acogerse a la dispensa en el juicio» ES FALSO desde el 25-6-2021.** Las
> excepciones **4.º y 5.º** vacían el supuesto más frecuente.

- **4.º:** basta **haber estado** personada — «esté **o haya estado**». **La renuncia posterior no recupera
  la dispensa.** Revisa el historial completo del procedimiento.
- **5.º:** dos elementos probatorios: que **aceptó declarar** **y** que fue **debidamente informada** antes.
  - **Defensa:** verifica **cada** acta e instructiva. Si la información del derecho **no consta**
    correctamente practicada, la excepción **no opera** y la dispensa revive. Punto de ataque concreto y
    documental.
  - **Acusación:** asegura que **conste en acta**, con precisión, la advertencia y la aceptación. Sin esa
    constancia, la declaración sumarial puede quedar inservible.
- ⚠️ **Ámbito subjetivo:** el texto dice cónyuge o persona unida por relación **análoga a la matrimonial**
  —relación **actual**—. Si la dispensa alcanza a la **expareja** o a quien ya no convive al declarar es
  **discutido**: `buscar_sentencias` en cada asunto. `[verificar]`
- ⚠️ **Efecto de la dispensa ejercida** sobre las **declaraciones sumariales previas** (arts. 714 y 730):
  **cuestión jurisprudencial**. `buscar_sentencias` **antes** de invocarla. No la anticipes al cliente.

---

## 8. Perspectiva de defensa — con rigor y sin sesgo

No cuestiona el fenómeno: enumera los derechos que la defensa **tiene el deber profesional** de ejercer.

1. **Presunción de inocencia (art. 24.2 CE).** Rige igual que en cualquier proceso: prueba de cargo válida,
   suficiente y racionalmente valorada. **Sin excepciones por razón de la materia.**
2. **Declaración de la víctima como única prueba de cargo.** Puede serlo, con **parámetros de valoración**
   jurisprudenciales.
   > ⛔ **No los enumeres de memoria ni les atribuyas formulación canónica.** `buscar_sentencias` (`PENAL`,
   > `TS`) con `"declaración de la víctima única prueba de cargo parámetros de valoración"` +
   > `leer_sentencias`. Cita solo lo verificado, con el ECLI que devuelva el conector → si no,
   > `[verificar]`.
3. **Proporcionalidad de las cautelares.** El terreno más productivo, con **anclaje legal expreso** en el
   544 bis (§ 3.3). **Acredita, no alegues**, y ofrece alternativa graduada.
4. **Motivación y necesidad estricta** (544 bis) y **situación objetiva de riesgo** como requisito autónomo
   (544 ter.1). Los autos de formulario son atacables.
5. **Art. 153.4 CP:** pena inferior en grado, razonada en sentencia, con prueba de las circunstancias.
6. **Denuncias instrumentales en crisis familiares.** Existen, como la denuncia falsa en cualquier delito.
   > ⚖️ **Sin sesgo y SIN GENERALIZAR.**
   > - **NO** afirmes ni sugieras que sean frecuentes, ni manejes porcentajes o estadísticas de memoria:
   >   sería un **dato inventado** sobre materia sensible. Verifica la fuente oficial o **no lo digas**.
   > - **NO** construyas la defensa sobre el **perfil** de la denunciante ni sobre relatos genéricos de
   >   «cómo son estos casos». Mala técnica, y suele volverse en contra.
   > - **SÍ**: hechos concretos y verificables — contradicciones objetivas, cronología incompatible,
   >   documentos, testigos, prueba de descargo. **Ancla al folio.** La coincidencia con una crisis
   >   familiar es **un dato a valorar, no una conclusión**.
7. **Lo que NO cabe:** mediación ni ningún MASC (**art. 89.9 LOPJ**). **Legalmente vedado**: no lo
   propongas.

---

## 9. ⚠️ Protección de datos — máxima cautela

**El riesgo más alto del plugin:** concurren **tres** categorías especialmente protegidas. **Art. 9 RGPD**
(salud: informes médicos y forenses, lesiones, salud mental, tratamientos, adicciones; y vida sexual) —
prohibido salvo excepciones del **9.2**, entre ellas la **9.2.f): defensa de reclamaciones**. **Art. 10
RGPD** (infracciones y condenas penales): todo el objeto de esta skill. Y **menores**, con el **interés
superior del menor** como criterio rector.

| Regla dura | Detalle |
|---|---|
| **Marcadores** | `[VÍCTIMA]`, `[INVESTIGADO]`, `[MENOR]`, `[TESTIGO]`, `[FAMILIAR]` |
| **Cero datos reales** | Ni nombres, DNI, domicilios, teléfonos, centros de trabajo, colegios ni matrículas |
| **Ni detalles identificativos** | Profesión poco común + localidad pequeña + fechas **reidentifican**. Generaliza o suprime |
| **Domicilio de la víctima** | **Jamás** en un borrador, nota o prompt. Su filtración causa **daño físico** |
| **Salud** | Solo lo estrictamente necesario. No transcribas informes íntegros |
| **Slug** | `descriptor-delito-año`. **Nunca** el nombre del cliente ni de la víctima. Ver `PROTECCION-DATOS.md` |

> **Un listado de carpetas que revele quién está investigado por violencia de género —o quién es víctima—
> es una brecha de datos de categoría especial y un daño irreversible para ambas personas.**

---

## Errores típicos

| Error | Corrección verificada |
|---|---|
| Citar el **art. 87 ter LOPJ** | ⛔ **SUPRIMIDO** (LO 1/2025). Sede: **art. 89 LOPJ** + **art. 14.5 LECrim** |
| «Juzgado de Violencia sobre la Mujer» | **Sección** con competencia en violencia sobre la mujer del **Tribunal de Instancia** (art. 14, vigente 3-10-2025) |
| Ignorar la **Sección de Violencia contra la Infancia** | **Órgano nuevo** (14.6). Si concurre con la de la Mujer, **gana esta** (**14.7**) |
| «La mediación se prohíbe en el art. 44.5 LOPJ» | **Art. 89.9 LOPJ**, y veda **todos los MASC**. El 44.5 **de la LO 1/2004** introdujo el derogado 87 ter |
| «Las 72 horas son para resolver» | Son para **CELEBRAR LA AUDIENCIA**, **desde la presentación de la solicitud** |
| Creer que las **medidas civiles** duran lo que el proceso penal | **30 + 30 días**, y **deben ratificarse** por el juez de primera instancia. **Caducan en silencio** |
| Pensar que la *vis atractiva* opera con la sola denuncia | **Cuatro requisitos SIMULTÁNEOS** (89.7) |
| Alegar el 544 bis sin acreditar la ponderación | Obliga a ponderar **economía, salud, familia y trabajo**, con atención especial a la **continuidad laboral, también tras la medida** |
| Pedir que **no se imponga** el alejamiento del 57.2 | **Imperativo** («se acordará en todo caso»). Discute la **extensión temporal** |
| Ignorar que el **48.2** suspende el régimen de visitas | **Automático, ex lege**, hasta el total cumplimiento |
| Afirmar que el consentimiento de la víctima atipifica el 468.2 | **Jurisprudencial y no pacífico.** `buscar_sentencias` obligatorio. Vía limpia: **pedir el alzamiento** |
| «La víctima siempre puede acogerse a la dispensa» | **Falso desde el 25-6-2021**: excepciones **4.º** y **5.º** |
| Citar de memoria parámetros de valoración o estadísticas de denuncias falsas | **Verifícalos o no los digas** |

## Reglas de trabajo

- **`buscar_articulo` antes de citar cualquier precepto.** Anclas: `references/anclas-normativas-penal.md`
  §§ 7.2, 11 bis y 11 ter. **Prohibido inventar** penas, plazos u ordinales → `[verificar]` y dilo.
- **⭐ Jurisprudencia SOLO vía `jurisprudenciator`.** **PROHIBIDO citar ECLI, ROJ, fechas o ponentes de
  memoria.** Aquí —quebrantamiento con consentimiento, dispensa del 416, valoración de la declaración de la
  víctima— **la jurisprudencia es el Derecho aplicable y ha oscilado**. Verifica siempre, `anios: 3-4`.
- **Ley penal en el tiempo:** redacción vigente **a la fecha de los hechos** (art. 2 CP) y comparación con
  la más favorable (art. 2.2 CP). **544 bis** cambió el **10-4-2026**; **87 ter LOPJ** desapareció el
  **23-1-2025**; **art. 14 LECrim** y la competencia sobre **violencia sexual**, desde el **3-10-2025**.
- **Nomenclatura:** **Secciones de los Tribunales de Instancia**, **LAJ**. Al transcribir preceptos no
  actualizados, reproduce el literal y advierte del desajuste.
- **Instruye el Juez de Instrucción** (la Sección correspondiente). **No existe el «fiscal instructor»**.
- **Nada de MASC**: requisito del orden civil, inaplicable en penal y **expresamente vedado** aquí (89.9).
- **Sin sesgo en las dos direcciones.** Ni presumir culpabilidad, ni presumir falsedad. **Hechos, folios y
  prueba.**
- **Protección de datos:** § 9. **Arts. 9 y 10 RGPD.** **Cero datos reales.**
- **Conflicto de interés:** no asesorar a víctima e investigado, ni sucesivamente sobre los mismos hechos.
- Config del despacho: `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.

## Entrega

Word `.docx` (skill `docx`): **solicitud de orden de protección** (544 ter, con el calendario 30+30
advertido por escrito); **oposición a medidas cautelares** del 544 bis con la **ponderación del § 3.3
acreditada** y alternativa graduada; **solicitud de modificación o alzamiento** (§ 6); o **nota de
estrategia** con las verificaciones jurisprudenciales pendientes marcadas `[verificar]`.
