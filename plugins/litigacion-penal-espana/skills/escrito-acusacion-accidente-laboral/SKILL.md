---
name: escrito-acusacion-accidente-laboral
description: >-
  Redacta el escrito de acusación (calificación provisional y solicitud de apertura de juicio oral) en causa por accidente de trabajo o siniestralidad laboral — arts. 316-318 CP en concurso con lesiones u homicidio imprudente. Actívala ante "escrito de acusación por accidente laboral", "calificar la siniestralidad laboral al terminar la instrucción", "acusación por falta de medidas de seguridad", "solicitar apertura de juicio oral", o cuando actúes como acusación particular del trabajador perjudicado. Requisito previo: causa penal YA incoada e instrucción concluida, con traslado para calificar. Si todavía no hay procedimiento penal abierto y lo que procede es iniciarlo con el acta de la Inspección de Trabajo y el parte de la caída de altura, usar /denuncia-derechos-trabajadores.
---

# Escrito de acusación por accidente laboral (arts. 316-318 CP)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Tipos y penas** (arts. 316-318, 142 y 152 CP) → `buscar_articulo` (`ley="CP"`).
- **Obligación de seguridad incumplida** → `buscar_articulo` (`ley="LPRL"`); reglamentos sectoriales con `buscar_boe` y su ID BOE.
- **Non bis in idem con la sanción administrativa (art. 3 LISOS)** → `buscar_articulo` con `ley="Real Decreto Legislativo 5/2000"` (la sigla «LISOS» devuelve otra norma).
- **Convenio aplicable** (formación y medios preventivos exigibles, categoría del trabajador) → `buscar_convenio` → `leer_convenio` y `vigencia_convenio` a la fecha del accidente.
- **Empresa, contratas y administradores responsables (art. 318 CP)** → `buscar_empresa_mercantil` (administradores y apoderados con cargo vigente a la fecha del accidente).
- **Doctrina sobre imputación objetiva y deber de vigilancia** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

Redacta el escrito de acusación por siniestralidad laboral. **La causa se gana o se pierde en la
imputación objetiva: quién estaba legalmente obligado, qué medio concreto no facilitó y cómo ese
incumplimiento produjo el resultado.**

---

## Comprobaciones previas

1. **Prescripción (art. 131 CP).** El art. 316 CP tiene pena máxima de 3 años → **5 años**. El 317
   (imprudencia grave), pena inferior en grado → **5 años**. En concurso, **el plazo del delito más
   grave** (art. 131.4): con homicidio imprudente (art. 142.1, hasta 4 años) sigue siendo 5 años;
   verifica el cómputo en cada caso. Estas causas llegan tarde: **calcula desde el día del accidente**.
2. **Plazo de instrucción (art. 324 LECrim).** 12 meses + prórrogas de ≤6 meses por auto motivado
   **previo** al vencimiento; sin él, **inválidas las diligencias posteriores (324.3)**. Estas causas
   son largas (pericial, ITSS, testifical extensa): **es donde más prórrogas se pierden**. Si acusas,
   **pide la prórroga tú y a tiempo**; no confíes en el impulso de oficio.
3. **Ley penal más favorable (art. 2.2 CP).** LO 1/2025 y LO 1/2026. Los arts. 316-318 CP **no** han
   sido modificados por ellas (316 y 317 vigentes desde 1996; 318 desde 2003, LO 11/2003), pero
   comprueba los tipos de resultado concurrentes.
4. **Non bis in idem** con el expediente sancionador laboral (ver abajo).
5. **Posición procesal:** acusación particular del trabajador o de sus causahabientes (art. 109 bis
   LECrim en caso de muerte); actor civil; personación en plazo.

---

## Los tipos — verificados literalmente

### Art. 316 CP — delito DOLOSO de peligro (vigente desde 24-5-1996)

> «Los que **con infracción de las normas de prevención de riesgos laborales** y **estando legalmente
> obligados**, **no faciliten los medios necesarios** para que los trabajadores desempeñen su
> actividad **con las medidas de seguridad e higiene adecuadas**, de forma que **pongan así en peligro
> grave su vida, salud o integridad física**, serán castigados con las penas de **prisión de 6 meses a
> 3 años y multa de 6 a 12 meses**.»

**Elementos que hay que acreditar uno a uno, cada uno con su folio:**

1. **Norma de prevención infringida** — identifícala **con precisión**: LPRL y su reglamento de
   desarrollo aplicable (obra, equipos de trabajo, EPI, altura…). Es una **norma penal en blanco**:
   sin norma extrapenal concreta, no hay tipo.
2. **Posición de garante — «estando legalmente obligados»**. No basta el cargo: acredita el **deber
   concreto** y la **capacidad real de decisión**. Empresario, administrador, encargado, jefe de obra,
   recurso preventivo, coordinador de seguridad y salud.
3. **No facilitar los medios necesarios.** Concreta **qué medio faltó**: no «hubo un incumplimiento
   genérico de la LPRL», sino «no se instaló línea de vida ni protección perimetral en el borde del
   forjado (f. …)».
4. **Peligro grave** para vida, salud o integridad física. **Delito de peligro concreto**: se consuma
   con el peligro, **con o sin resultado lesivo**. Alegar el resultado no exime de probar el peligro.
5. **Dolo** — al menos eventual: conocimiento del riesgo y de la omisión. Se acredita por
   **requerimientos previos**, advertencias del servicio de prevención, actas anteriores de la ITSS,
   reiteración de la situación.

### Art. 317 CP — imprudencia grave (vigente desde 24-5-1996)

> «Cuando el delito a que se refiere el artículo anterior se cometa **por imprudencia grave**, será
> castigado con la **pena inferior en grado**.»

**Es el cauce realista en la mayoría de los casos.** Si no puedes acreditar el dolo eventual, acusa
por el 317 y **no** por el 316: una acusación por dolo sin soporte se desmonta y arrastra al resto.
Considera acusar por el **316 y, alternativamente, por el 317**.

### Art. 318 CP — atribución a personas jurídicas (vigente desde 1-10-2003)

> «Cuando los hechos previstos en los artículos de este título se atribuyeran a **personas jurídicas**,
> se impondrá la pena señalada a los **administradores o encargados del servicio que hayan sido
> responsables** de los mismos y **a quienes, conociéndolos y pudiendo remediarlo, no hubieran adoptado
> medidas para ello**. En estos supuestos la autoridad judicial podrá decretar, además, alguna o
> algunas de las **medidas previstas en el artículo 129** de este Código.»

**⚠️ Error conceptual capital.** El art. 318 **NO** es responsabilidad penal de la persona jurídica
del art. 31 bis CP. Es una **regla de traslado de la pena a personas físicas** determinadas cuando el
hecho se atribuye a la persona jurídica, más la posibilidad de las **consecuencias accesorias** del
art. 129 CP. **Los delitos contra los derechos de los trabajadores no están en el catálogo del
art. 31 bis**: la mercantil **no responde penalmente como tal** por el 316/317 — responde civilmente
(arts. 120.4 CP) y, en su caso, por el art. 129. **No pidas para la mercantil las penas del art. 33.7
CP por esta vía.** [verificar en el caso concreto si concurre algún otro tipo que sí active el 31 bis]

**Dos círculos de autores en el 318:** (a) administradores o encargados del servicio **responsables**;
y (b) **quienes, conociéndolos y pudiendo remediarlo, no adoptaron medidas** — la vía para alcanzar al
mando intermedio que sabía y calló.

---

## Concurso con el resultado — arts. 142 y 152 CP (verificados)

Los arts. 316/317 son de **peligro**; el resultado lesivo se castiga aparte.

- **Art. 142.1 CP — homicidio por imprudencia grave: prisión de 1 a 4 años.** Si es **imprudencia
  profesional**, además **inhabilitación especial de 3 a 6 años**.
- **Art. 142.2 — imprudencia menos grave: multa de 3 a 18 meses.** Fuera del vehículo a motor, **solo
  perseguible mediante denuncia** del agraviado o su representante legal. **Compruébalo**: sin
  denuncia no hay procedibilidad.
- **Art. 152.1 CP — lesiones por imprudencia grave**, «en atención al riesgo creado y el resultado
  producido»:
  - **1.º** lesiones del art. 147.1 → prisión de 3 a 6 meses **o** multa de 6 a 18 meses.
  - **2.º** lesiones del art. 149 → prisión de **1 a 3 años**.
  - **3.º** lesiones del art. 150 → prisión de **6 meses a 2 años**.
  - Imprudencia **profesional** → además **inhabilitación especial de 6 meses a 4 años**.
- **Art. 152.2 — imprudencia menos grave** (147.1 → multa 1-2 meses; 149 y 150 → multa 3-12 meses).
  **Solo perseguible mediante denuncia** del agraviado o su representante legal.
- **⚠️ El art. 152.1 no cubre las lesiones del art. 147.2** (leves): la imprudencia sobre ellas es
  atípica. Verifica el encaje del parte de lesiones.
- **Relación concursal:** la posición dominante trata el peligro (316/317) y el resultado (142/152)
  como **concurso ideal del art. 77 CP** cuando el resultado es consecuencia del mismo incumplimiento,
  y como **concurso real (art. 73)** cuando el peligro alcanzó a **otros trabajadores** distintos del
  accidentado. **La cuestión no es pacífica: contrasta con `buscar_sentencias`** antes de fijar la
  calificación, y plantea la alternativa subsidiaria. Marca `[verificar]` la regla concursal si el
  criterio de la Sección es desconocido.
  > **Argumento de peso para el concurso real:** si el andamio sin protección exponía a toda la
  > cuadrilla, el peligro del 316 tiene **más víctimas** que el resultado del 152 — no hay unidad de
  > hecho.

---

## Responsabilidad civil — donde está el interés real del cliente

- **Aseguradora — responsable civil DIRECTO (art. 117 CP, verificado):** «Los aseguradores que
  hubieren asumido el riesgo de las responsabilidades pecuniarias derivadas del **uso o explotación de
  cualquier bien, empresa, industria o actividad**, cuando, como consecuencia de un hecho previsto en
  este Código, se produzca el evento que determine el riesgo asegurado, serán **responsables civiles
  directos hasta el límite de la indemnización** legalmente establecida o convencionalmente pactada,
  sin perjuicio del **derecho de repetición**.»
  > **Operativo:** **demanda a la aseguradora de RC de la empresa desde el escrito de acusación.** Es
  > responsable **directa**, no subsidiaria: no hay que agotar el patrimonio del condenado. Pide el
  > **oficio para que se aporte la póliza** — límites, franquicia y exclusiones. Es la diferencia entre
  > una indemnización cobrable y un papel.
- **Empresario — responsable civil SUBSIDIARIO (art. 120.4 CP, verificado):** «Las personas naturales
  o jurídicas dedicadas a cualquier género de industria o comercio, por los delitos que hayan cometido
  sus **empleados o dependientes, representantes o gestores en el desempeño de sus obligaciones o
  servicios**.» Vía para llevar a la mercantil, que no responde penalmente por el 316/317.
  Considera también el **art. 120.3** (titulares de establecimientos con infracción de reglamentos).
- **Empresa principal — solidaria en el orden laboral (art. 42.3 LISOS, verificado):** responde
  solidariamente con contratistas y subcontratistas del art. 24.3 LPRL, durante la contrata, respecto
  de los trabajadores que ocupen **en los centros de trabajo de la principal**, siempre que la
  infracción se haya producido allí. Es norma **sancionadora laboral**: úsala como argumento de la
  posición de garante y de la RC, no como tipo penal.
- **Contenido:** arts. 109-115 CP. Baremo de tráfico (Ley 35/2015) como **criterio orientativo** —
  no vinculante fuera de la circulación; razona la desviación al alza. Deduce lo percibido por
  prestaciones de Seguridad Social y **recargo de prestaciones** (art. 164 LGSS) para evitar
  enriquecimiento injusto [verificar el criterio de la Sección con `buscar_sentencias`].

---

## ⚖️ Non bis in idem con el sancionador laboral (art. 3 RDL 5/2000 — LISOS, verificado)

- **3.1:** «**No podrán sancionarse los hechos que hayan sido sancionados penal o administrativamente,
  en los casos en que se aprecie identidad de sujeto, de hecho y de fundamento.**»
- **3.2 — prejudicialidad penal:** si las infracciones pudieran ser constitutivas de ilícito penal, la
  Administración **pasa el tanto de culpa** al órgano judicial o al Fiscal y **se abstiene** de seguir
  el procedimiento sancionador mientras no recaiga sentencia firme o resolución que ponga fin al
  procedimiento, o el Fiscal comunique la improcedencia de actuar.
- **3.3:** de no estimarse ilícito penal, la Administración continúa el expediente **sobre los hechos
  que los Tribunales hayan declarado probados**.
- **3.4:** el tanto de culpa **no afecta** al cumplimiento inmediato de las medidas de **paralización
  de trabajos** por riesgo grave e inminente, ni a los requerimientos de subsanación, ni a los
  expedientes **sin conexión directa** con lo penal.
- **Operativo para la acusación:** la **triple identidad** (sujeto, hecho, fundamento) rara vez
  concurre plenamente — el sujeto sancionado suele ser la **empresa** y el acusado la **persona
  física**, y el fundamento del 316 CP (peligro grave) no coincide con el de la infracción
  administrativa. **Anticipa la excepción en el escrito y desmóntala**, identificando la asimetría.

---

## Prueba — el corazón del escrito

| Medio | Qué aporta | Cautela |
|---|---|---|
| **Acta de infracción de la ITSS** | Presunción de certeza de los **hechos** constatados por el Inspector (art. 23 LOITSS / art. 53 LISOS — [verificar el precepto]) | La presunción alcanza a los **hechos**, **no a la calificación jurídica** ni al juicio de culpabilidad. No sustituye la prueba del dolo ni de la causalidad |
| **Informe de investigación del accidente** de la ITSS y del **técnico de la autoridad laboral** | Mecánica del siniestro, causas, incumplimientos | Pide la **ratificación** del inspector/técnico: sin contradicción, vale menos |
| **Plan de prevención** (art. 16.1 LPRL) | Estructura organizativa, responsabilidades, funciones, procedimientos y recursos | Su **inexistencia o carácter meramente formal** es el argumento central |
| **Evaluación de riesgos y planificación** (art. 16.2 LPRL) | Si el riesgo estaba evaluado y qué medida se planificó | Riesgo **no evaluado** o medida planificada **no ejecutada** (16.2.b in fine: «deberá asegurarse de la efectiva ejecución») |
| **Investigación interna del accidente** (art. 16.3 LPRL) | Reconocimiento de causas por la propia empresa | Obligatoria tras un daño: su ausencia es indiciaria |
| **Formación e información** (arts. 18 y 19 LPRL) y **entrega de EPI** (art. 17) | Acreditación documental firmada | «Firmó el recibí» ≠ formación real y eficaz |
| **Coordinación de actividades** (art. 24 LPRL) | Deberes de cooperación, información e instrucciones; **24.3**: vigilancia del cumplimiento por contratistas de la **propia actividad** en centros propios | Clave en obra y subcontratación en cadena |
| **Pericial técnica de PRL de parte** | Norma infringida, mecánica, nexo causal, evitabilidad | El **juicio contrafáctico** es imprescindible: qué medida concreta habría evitado el resultado |
| **Pericial médico-forense / médica de parte** | Lesiones, secuelas, perjuicio | Base de la responsabilidad civil |
| **Testifical** | Compañeros, encargado, recurso preventivo, coordinador | **Cadena de mando y orden recibida** |
| **Documental societaria y laboral** | Nota simple registral, escritura de nombramiento, organigrama, contrata y subcontratas, TC2, póliza de RC | Acredita **quién estaba legalmente obligado** |

---

## Estructura del escrito

1. Encabezamiento a la **Sección de Instrucción del Tribunal de Instancia** con nº de diligencias
   previas / procedimiento abreviado.
   > ⭐ **Copia la denominación exacta que figure en la resolución que contestas o en la carátula del
   > procedimiento.** Es lo que nunca falla, diga «Sección de Instrucción del Tribunal de Instancia»
   > o siga diciendo «Juzgado de Instrucción». La nomenclatura vigente (art. 14 LECrim, desde el
   > 3-10-2025) es la de **Sección**; la antigua no invalida el escrito (DA 1.ª LO 1/2025).
2. Comparecencia de procurador y letrado de `[PERJUDICADO]` / `[CAUSAHABIENTES]`.
3. Fórmula: evacuando el traslado del **art. 780.1 LECrim** (plazo **común de 10 días** — verificado),
   **solicita la APERTURA DEL JUICIO ORAL** ante la **Sección de lo Penal** contra `[ACUSADO 1]`
   (administrador), `[ACUSADO 2]` (encargado / jefe de obra), y formula **ESCRITO DE ACUSACIÓN** con
   las siguientes conclusiones provisionales.
4. **CONCLUSIONES (art. 650):**
   - **PRIMERA — HECHOS PUNIBLES.** Empresa, actividad y centro de trabajo. **Puesto y funciones** del
     trabajador. Antigüedad y **formación efectivamente recibida**. **Cadena de mando** y orden
     concreta recibida; si la tarea era **atípica** de su puesto, dilo y pruébalo. **Estado de las
     medidas de seguridad** en el momento del accidente. **Mecánica del accidente**, minuto a minuto.
     **Lesiones y secuelas**. **Norma de prevención infringida**, con cita del precepto. Antecedentes:
     requerimientos, actas previas, advertencias del servicio de prevención (**el sustrato del dolo**).
     Todo **anclado al folio**.
   - **SEGUNDA — CALIFICACIÓN.** Art. 316 CP (o, alternativamente, art. 317) en concurso —**ideal
     (art. 77) o real (art. 73), razonado**— con el art. 142 o el art. 152 CP, con el apartado exacto.
     Art. 318 CP como regla de atribución.
   - **TERCERA — PARTICIPACIÓN.** Autoría de cada acusado **por separado**, con su título de garante y
     su capacidad real de decisión. Distingue los dos círculos del art. 318.
   - **CUARTA — CIRCUNSTANCIAS MODIFICATIVAS.** Agravantes; en su defecto, ninguna. Anticipa las
     atenuantes previsibles (reparación, dilaciones).
   - **QUINTA — PENAS**, individualizadas por acusado y por delito, con las reglas concursales y los
     arts. 66 y ss. CP. Incluye **inhabilitación especial** si es imprudencia profesional.
   - **SEXTA — RESPONSABILIDAD CIVIL.** Cuantía desglosada por conceptos. **Responsables civiles
     directos** (acusados; **aseguradora ex art. 117 CP**) y **subsidiarios** (mercantil ex art. 120.4
     CP). Intereses del art. 20 LCS frente a la aseguradora [verificar procedencia].
   - **SÉPTIMA —** en su caso, **medidas del art. 129 CP** para la persona jurídica (art. 318 in fine).
5. **PRUEBA** para el juicio oral, del cuadro anterior, con la **pertinencia de cada medio**.
6. **SUPLICO** y **OTROSÍES** (medidas cautelares reales del art. 764 LECrim / **fianza al responsable
   civil ex art. 783.2**; oficio para aportación de la póliza). Lugar, fecha y firma.

---

## Errores típicos

| Error | Corrección |
|---|---|
| Tratar el art. 318 CP como responsabilidad penal de la persona jurídica | Es **traslado de pena a personas físicas** + art. 129. El 316/317 **no** está en el catálogo del 31 bis |
| Acusar por el 316 (doloso) sin sustrato de dolo | Acusa por el **317**, o por el 316 con el 317 **alternativo** |
| Invocar «infracción de la LPRL» en abstracto | Norma penal **en blanco**: cita el **precepto reglamentario concreto** |
| Dar por probado el peligro con el resultado | El **peligro grave** es elemento **autónomo** del 316 |
| Cargo = posición de garante | Hay que probar el **deber concreto** y la **capacidad real de decisión** |
| Olvidar a la aseguradora | Es responsable civil **directo** (art. 117 CP). Sin ella, sentencia incobrable |
| Pedir penas del art. 33.7 CP a la mercantil por el 318 | Improcedente. El 318 remite al **art. 129** (consecuencias accesorias) |
| Tratar el acta de la ITSS como prueba plena | Presunción de certeza **de los hechos constatados**; no de la calificación ni de la culpabilidad |
| Ignorar el art. 3.2 LISOS | La prejudicialidad penal **suspende** el sancionador: comprueba en qué estado está |
| Dejar caer la prórroga del art. 324 | Sin auto previo, **inválidas** las diligencias posteriores (324.3). En estas causas es lo más frecuente |
| Perseguir imprudencia menos grave sin denuncia | Arts. 142.2 y 152.2: **requieren denuncia** del agraviado |
| Pericial sin juicio contrafáctico | Sin «qué medida lo habría evitado» no hay imputación objetiva |

## Reglas de trabajo

- **Verifica con `buscar_articulo` antes de citar.** Anclas: `references/anclas-normativas-penal.md`.
- **Jurisprudencia solo vía `jurisprudenciator`** (`buscar_sentencias`, `buscar_por_cita`,
  `leer_sentencias`) — especialmente la regla concursal 316/152 y la eficacia del acta de la ITSS.
  **Prohibido inventar** ECLI, ROJ, fechas o ponentes. Sin verificar → `[verificar]`.
- **Prohibido inventar** penas, plazos, ordinales o preceptos reglamentarios de PRL. Lo no verificable
  → `[verificar]`, y se advierte.
- **Ancla al folio**: «(f. …)». Sin folio, no se escribe.
- **Anonimización:** `[ACUSADO]`, `[PERJUDICADO]`, `[TESTIGO]`, `[MERCANTIL]`, `[CIF]`. Datos de
  infracciones y condenas = **categoría especial (art. 10 RGPD)**. Ver `PROTECCION-DATOS.md`.
- **Instruye el Juez de Instrucción.** No existe el «fiscal instructor» en Derecho vigente.
- Terminología LO 1/2025: Tribunales de Instancia, LAJ, audiencia preliminar (art. 785).

## Entrega

Word `.docx` (skill `docx`) con conclusiones provisionales, proposición de prueba, suplico y otrosíes,
maquetado para LexNET. Adjunta un **cuadro de responsables** (persona → título de garante → deber
infringido → folio) y el **desglose de la responsabilidad civil** por conceptos.
