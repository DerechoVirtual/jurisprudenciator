---
name: costas-ca
description: Catálogo (sin plantilla). Costas en el orden contencioso-administrativo (art. 139 LJCA, redacción del RD-ley 6/2023 en vigor 20-3-2024) y tasación e impugnación por remisión a la LEC (arts. 242-246). Estima el riesgo de costas del cliente aplicando el tope de un tercio de la cuantía, redacta la solicitud de no imposición por serias dudas de hecho o de derecho, y revisa tasaciones detectando partidas indebidas, excesivas o que superen el tope. Activar con "costas", "condena en costas", "riesgo de costas", "cuánto me puede costar si pierdo", "tope de costas", "tercio de la cuantía", "tasación de costas", "impugnar la tasación", "costas excesivas", "costas indebidas", "no imposición de costas", "serias dudas de derecho", "minuta del abogado del Estado", "¿me van a condenar en costas?", "art. 139 LJCA".
---

# Costas en el contencioso-administrativo (art. 139 LJCA) — catálogo (sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen vigente de costas** → `buscar_articulo` (`ley="LJCA"`, artículos 139 y 93; artículos 40 a 42 para la cuantía).
- **Tasación e impugnación por remisión a la LEC** → `buscar_articulo` (`ley="LEC"`, artículos 242 a 246 y 394).
- **«Serias dudas de derecho»: criterios contradictorios o cambio de criterio** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`; `base="AN"` con `tipo_organo="TSJ"` para contrastar Salas, `base="TS"` para el cambio de criterio) + `leer_sentencias` (`parrafos=3`).
- **Cuestión de interés casacional admitida y pendiente** → `buscar_sentencias` (`base="TS"`, `tipo_resolucion="AUTO"`).
- **Norma reciente o reformada como argumento de serias dudas** → `buscar_boe` + `leer_boe` (fecha de publicación y de entrada en vigor).
- **Escrito de no imposición o de impugnación de la tasación** → `verificar_escrito` antes de presentarlo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

Tres funciones: **(a)** estimar el riesgo económico antes de interponer o recurrir; **(b)** redactar
la solicitud de **no imposición**; **(c)** revisar una **tasación** recibida. Preceptos verificados
contra el BOE el **2026-07-17**; **reverifica con `buscar_articulo` antes de citar**.

> ⚠️ **El régimen cambió el 20-3-2024** (RD-ley 6/2023). Cualquier nota, plantilla o criterio anterior
> a esa fecha sobre el **tope del art. 139.4** está obsoleto. Comprueba la fecha de la fuente.
>
> ⛔ **Nada de MASC.** El art. 245.5 LEC permite pedir exoneración o moderación de costas por haber
> formulado propuesta en un MASC: **es del orden civil y NO se aplica aquí**. No lo invoques ni lo
> incluyas en escritos contenciosos.

---

## 1. Régimen del art. 139 LJCA (vigente desde 20-3-2024)

### 1.1 Primera o única instancia — art. 139.1
- **Vencimiento objetivo:** al dictar sentencia **o al resolver por auto los recursos o incidentes**
  que ante él se promuevan, el órgano **impondrá las costas a la parte que haya visto rechazadas
  TODAS sus pretensiones**, **salvo que aprecie —y así lo razone— que el caso presentaba serias dudas
  de hecho o de derecho**. El «salvo» exige **motivación expresa**: una sentencia que impone costas
  sin responder a la petición razonada de no imposición es atacable por falta de motivación.
- **Estimación o desestimación PARCIAL:** cada parte abona **las causadas a su instancia y las
  comunes por mitad**, salvo que el órgano, **razonándolo debidamente**, las imponga a una de ellas
  **por haber sostenido su acción o interpuesto el recurso con mala fe o temeridad**.
  → **Consecuencia estratégica de primer orden:** la estimación parcial neutraliza la condena. Si el
  asunto es dudoso, **articula pretensiones susceptibles de estimación parcial** (p. ej., subsidiaria
  de reducción del importe o de la sanción junto a la principal de anulación) en lugar de una única
  pretensión de todo o nada. Es la vía más eficaz de gestión del riesgo de costas.

### 1.2 Recursos — art. 139.2
- Se imponen al **recurrente si se desestima TOTALMENTE** el recurso, salvo que el órgano,
  **razonándolo debidamente**, aprecie **circunstancias que justifiquen su no imposición**. Nota la
  diferencia con el 139.1: aquí la excusa no está tasada en «serias dudas», es más abierta
  («circunstancias») — aprovéchalo al pedir la no imposición en apelación.

### 1.3 Casación — art. 139.3 → art. 93.4 LJCA (verificado)
- **Regla:** la sentencia resuelve sobre las **costas de la instancia conforme al art. 139.1** y
  dispone, **en cuanto a las del recurso de casación, que cada parte abone las causadas a su
  instancia y las comunes por mitad**.
- **Excepción:** podrá imponer las de la casación **a una sola parte** cuando la sentencia **aprecie
  y motive mala fe o temeridad**; imposición que **podrá limitar a una parte de ellas o hasta una
  cifra máxima**.
- → **Dato de asesoramiento:** en casación admitida, el escenario ordinario es **cada parte las
  suyas**. El riesgo de costas **no** es un argumento serio para desaconsejar una casación admitida;
  sí lo es para la instancia. (La inadmisión tiene su propio régimen — verifica el auto aplicable.)

### 1.4 ⚠️ EL TOPE — art. 139.4 (RD-ley 6/2023, en vigor 20-3-2024). El dato más rentable
> «En primera o única instancia, la parte condenada en costas estará obligada a pagar una cantidad
> total que **no exceda de la tercera parte de la cuantía del proceso, por cada uno de los favorecidos
> por esa condena**; a estos solos efectos, las **pretensiones de cuantía indeterminada se valorarán
> en 18.000 euros**, salvo que, **por razón de la complejidad del asunto, el tribunal disponga
> razonadamente otra cosa**.
> En los recursos, y sin perjuicio de lo previsto en el apartado anterior, la imposición de costas
> podrá ser **a la totalidad, a una parte de éstas o hasta una cifra máxima**.»

Léelo con precisión — cuatro trampas:
1. El tope opera **en primera o única instancia**. Para los **recursos** rige el párrafo 2.º: no hay
   tope automático del tercio, sino la facultad de limitar (total / parte / cifra máxima).
2. Es **por cada uno de los favorecidos**: con Administración demandada **y** codemandado (p. ej.
   aseguradora o tercero interesado personado), el riesgo real es **1/3 × n favorecidos**. Cuenta
   siempre las partes personadas al estimar, no solo a la Administración.
3. Los **18.000 €** son un valor **ficticio y a los solos efectos del tope**, no la cuantía del
   pleito, y **decae si el tribunal razona otra cosa por complejidad**.
4. El tope limita la **cantidad total a pagar**, no la minuta que el contrario puede reclamar: se
   aplica **al tasar**. Si la tasación lo supera, hay que **impugnarla** (§ 4).

### 1.5 Apartados 5 a 7
- **139.5 — exacción frente a particulares:** la **Administración acreedora** utilizará el
  **procedimiento de apremio**, en defecto de pago voluntario. Adviértelo al cliente: si pierde
  frente a la Administración, ésta **no** ejecuta por vía judicial, **apremia**, con sus recargos.
- **139.6 — en ningún caso** se imponen las costas **al Ministerio Fiscal**.
- **139.7 — tasación y regulación** conforme a la **Ley de Enjuiciamiento Civil** (§ 3-4).

---

## 2. Estimación del riesgo de costas ANTES de interponer

**Procedimiento a seguir siempre que el cliente pregunte «¿cuánto me puede costar si pierdo?»:**

1. **Fija la cuantía del proceso** (§ 5). Es la variable de la que depende todo.
2. **Cuenta los favorecidos potenciales:** Administración demandada + codemandados personados.
3. **Aplica el tope:** riesgo máximo en instancia = **(cuantía / 3) × n.º de favorecidos**.
   Si la cuantía es **indeterminada**: base **18.000 €** → **6.000 € por favorecido**, salvo que el
   tribunal razone otra cosa por complejidad.
4. **Contrasta con la minuta previsible** del contrario (criterios del Colegio, § 4): el cliente paga
   **la menor** de las dos cifras. El tope solo muerde si la minuta lo supera.
5. **Aplica el filtro de escenarios** y explícalo por escrito:
   - Desestimación **total** → condena (salvo serias dudas razonadas).
   - Estimación o desestimación **parcial** → **cada parte las suyas** (art. 139.1, párr. 2.º).
   - Recurso desestimado **totalmente** → costas del recurso (art. 139.2), sin tope automático del
     tercio pero con facultad de limitación.
6. **Documenta la advertencia** en la hoja de encargo (skill `hoja-encargo`).

**Ejemplo numérico (importes ficticios; usa marcadores en los entregables reales):**

> `[CLIENTE]` impugna ante `[ÓRGANO]` una liquidación de **[IMPORTE] = 24.000 €**. Se persona la
> Administración demandada y, además, un **codemandado** interesado. Cuantía del proceso: 24.000 €
> (art. 42.1.a) LJCA: contenido económico del acto, sin recargos ni costas).
> - Tope por favorecido: 24.000 / 3 = **8.000 €**. Favorecidos: **2** → **riesgo máximo 16.000 €**.
> - Si la minuta del contrario asciende a 5.500 €, se paga 5.500 € (no llega al tope).
> - Si asciende a 11.000 €, la tasación **debe reducirse a 8.000 €** por ese favorecido: si no lo
>   hace, **impugna por indebida en cuanto al exceso** (§ 4).
> - Cuantía ≤ 30.000 € → **abreviado** (art. 78.1 LJCA) y sentencia **no apelable** (art. 81.1.a)).
> - Si la misma pretensión se hubiera articulado como **cuantía indeterminada**: tope 18.000 / 3 =
>   **6.000 €** por favorecido → **12.000 €**. Pero perdería el abreviado y ganaría la apelabilidad.
>   **Ése es el intercambio: no fijes la cuantía pensando solo en las costas.**

---

## 3. Solicitud de no imposición de costas — cómo redactarla

Se pide en el **suplico** de la demanda o del recurso (y se reitera en **conclusiones** — skill
`escrito-conclusiones-ca`). **No la des por hecha: si no se pide y razona, el juez no tiene que
motivar por qué no la aprecia.**

- **Petición:** que no se impongan las costas por concurrir **serias dudas de hecho o de derecho**
  (art. 139.1) o, en recurso, **circunstancias que justifiquen su no imposición** (art. 139.2).
  **Subsidiariamente**, que se limiten **hasta una cifra máxima** (facultad del art. 139.4, párr. 2.º,
  en recursos) y, en todo caso, que se respete el **tope del tercio** del art. 139.4.
- **Argumentos de «serias dudas de DERECHO»** — desarrolla al menos uno, con material verificable:
  - Norma de **reciente entrada en vigor** o **reformada**, sin criterio consolidado.
  - **Jurisprudencia contradictoria** entre TSJ o entre secciones, o **cambio de criterio** del TS.
  - **Cuestión de interés casacional objetivo admitida** y pendiente sobre la misma cuestión.
  - **Cuestión prejudicial ante el TJUE** o de inconstitucionalidad planteada.
  - Concepto jurídico **indeterminado** o potestad discrecional cuyo control exige valoración.
  - La propia Administración **cambió de criterio** o resolvió de forma distinta casos iguales.
- **Argumentos de «serias dudas de HECHO»:** prueba pericial **contradictoria**; hechos que solo se
  esclarecen con la prueba practicada en el proceso; expediente **incompleto o remitido tarde** por la
  Administración; hechos negativos.
- **Refuerzo:** que el asunto se admitiera a trámite, que se acordara la **medida cautelar** (implica
  apariencia de buen derecho) o que hubiera **votos particulares** en resoluciones análogas.
- **Prohibido:** citar sentencias de memoria. Localiza y **verifica cada apoyo** con
  `buscar_sentencias` / `buscar_por_cita` antes de incluirlo; si no se verifica, `[verificar]` y dilo.

---

## 4. Revisión e impugnación de una tasación recibida (arts. 242-246 LEC, ex art. 139.7 LJCA)

**Marco (verificado):** tasación por el **LAJ** del tribunal que conoció del proceso o del encargado
de la ejecución (art. 243.1 LEC). Traslado a las partes por **plazo común de 10 días** (art. 244.1);
transcurrido sin impugnar, se aprueba por **decreto**, recurrible en **revisión directa**
(art. 244.3). **Una vez acordado el traslado no se admite la inclusión o adición de partida alguna**
(art. 244.2).

**Checklist de revisión — recórrelo entero sobre la tasación recibida:**
1. **¿Supera el tope del art. 139.4 LJCA?** Calcula cuantía/3 por cada favorecido. El exceso es
   **partida indebida**. Es el primer control y el más olvidado: el LAJ no siempre lo aplica de oficio.
2. **¿Hay condena?** Sin pronunciamiento firme de condena no hay tasación (art. 242.1: exacción por
   apremio **una vez firme**).
3. **Partidas excluibles ex art. 243.2 LEC:**
   - Escritos y actuaciones **inútiles, superfluas o no autorizadas por la ley**.
   - Partidas de minutas **no expresadas detalladamente**, o referidas a **honorarios no devengados
     en el pleito** (asesoramiento previo, vía administrativa, otros procedimientos).
   - Derechos de procurador por actuaciones **meramente facultativas** que hubieran podido practicar
     las Oficinas judiciales. **Recuerda:** ante **órganos unipersonales** el procurador es
     **potestativo** (art. 23.1 LJCA) — examina con lupa esa partida en un abreviado.
   - El LAJ **reducirá** los honorarios de abogados y demás profesionales no sujetos a arancel cuando
     excedan del límite del **art. 394.3 LEC**, salvo declaración de temeridad. **⚠️ En el contencioso
     el límite aplicable es el especial del art. 139.4 LJCA**, no el civil; cita el 139.4 como norma
     de cobertura y usa el 243.2 solo como cauce de reducción. Si el asunto exige apoyarse en el
     395/394 LEC, **verifica su texto con `buscar_articulo` antes** `[verificar]`.
   - **Art. 243.3:** no se incluyen las costas de **actuaciones o incidentes en que la parte
     favorecida hubiese sido expresamente condenada** (p. ej., perdió el incidente cautelar).
4. **¿Se aportaron los justificantes** de haber satisfecho las cantidades cuyo reembolso se reclama
   (art. 242.2)? ¿Minuta **detallada** y cuenta justificada (art. 242.3)?
5. **IVA y suplidos:** revisa duplicidades y la repercusión; comprueba la condición del cliente.
6. **Peritos:** ¿fue la pericia pertinente y practicada a instancia del favorecido?

**Motivos y trámite de impugnación (arts. 245-246 LEC):**
- **Por INDEBIDAS** (art. 245.2, 1.ª parte): partidas, derechos o gastos **indebidos** — incluye el
  **exceso sobre el tope del art. 139.4 LJCA**. Trámite (art. 246.4): traslado a la otra parte por
  **3 días**; el LAJ resuelve por **decreto en los 3 días siguientes**; cabe **recurso directo de
  revisión**, y contra el auto que lo resuelva **no cabe recurso alguno**.
- **Por EXCESIVOS** (art. 245.2, 2.ª parte): solo respecto de **honorarios de abogados, peritos o
  profesionales no sujetos a arancel**. Trámite (art. 246.1): se oye al abogado por **5 días** y, si
  no acepta la reducción, se pasa testimonio al **Colegio de Abogados para informe**; el LAJ resuelve
  por decreto (246.3), recurrible en revisión. Para peritos, dictamen de su Colegio, Asociación o
  Corporación (246.2).
- **Impugnación simultánea (art. 246.5):** si se alega que una partida de honorarios de abogados o
  peritos es **indebida y, de no serlo, excesiva**, se tramitan **ambas a la vez**, pero la
  decisión sobre si es excesiva **queda en suspenso** hasta resolver si es debida. **Plantéalo así
  siempre que quepa: no elijas entre los dos motivos, acumúlalos en ese orden.**
- **Requisito formal ineludible (art. 245.4):** el escrito debe mencionar **las cuentas o minutas y
  las partidas concretas** a que se refiere la discrepancia **y las razones de ésta**. Sin esa
  mención, el LAJ **inadmite a trámite** por decreto (cabe revisión). **Nunca impugnes en bloque ni
  de forma genérica: partida por partida, con su razón.**
- **Costas del incidente (art. 246.4, último párrafo):** si la impugnación se desestima **totalmente**,
  se imponen al impugnante **si hubiera obrado con abuso del servicio público de Justicia**; si se
  estima total o parcialmente, se imponen —también en ese caso de abuso— al perito o a la parte
  defendida por el abogado cuyos honorarios se consideraron excesivos o indebidos. **No es una
  condena automática:** exige abuso. Dilo al cliente al valorar si impugnar.
- **Plazo:** el del art. 244.1 → **10 días** desde el traslado (art. 245.1). Es común e improrrogable.
- **Justicia gratuita (art. 246.6):** en el incidente **no se discute** la obligación de la
  Administración de pagar por la Ley de Asistencia Jurídica Gratuita.
- ⛔ **NO invoques el art. 245.5 LEC** (exoneración o moderación por propuesta en MASC): es del orden
  civil y no rige en contencioso.
- La parte **favorecida** también puede impugnar (art. 245.3): por no incluirse gastos justificados y
  reclamados, la totalidad de la minuta o los derechos del procurador. Úsalo cuando defiendas al
  vencedor.

Ver también la skill `impugnacion-tasacion-costas` si existe en el perfil del despacho.

---

## 5. Conexión con la cuantía del proceso (arts. 40-42 LJCA) — fíjala con criterio

La cuantía **no es un trámite**: decide tres cosas a la vez. Fijarla mal encarece o abarata las costas
y cambia el procedimiento y el acceso al recurso.

| La cuantía decide | Regla |
|---|---|
| **Tope de costas** | 1/3 de la cuantía por cada favorecido; indeterminada = **18.000 €** (art. 139.4) |
| **Procedimiento** | **abreviado** si ≤ **30.000 €** (art. 78.1 LJCA) |
| **Apelabilidad** | **no** hay apelación si ≤ **30.000 €** (art. 81.1.a) LJCA) |

**Reglas de fijación (art. 42 LJCA, verificado):** se aplican las normas de la **legislación procesal
civil**, con estas especialidades:
- **42.1.a)** Si solo se pide la **anulación** del acto: **contenido económico** del acto, atendiendo
  al **débito principal**, **sin recargos, costas ni otras responsabilidades**, salvo que alguno de
  éstos sea **de importe superior** al principal.
- **42.1.b)** Si además se pide el **reconocimiento de una situación jurídica individualizada** o el
  **cumplimiento de una obligación**: 1.º **valor económico total** del objeto de la reclamación si la
  Administración denegó **totalmente** en vía administrativa; 2.º la **diferencia** entre lo reclamado
  y el acto recurrido si reconoció **parcialmente**.
- **42.2 — cuantía indeterminada:** impugnación **directa** de disposiciones generales (incluidos los
  **instrumentos normativos de planeamiento urbanístico**); asuntos de **funcionarios públicos** que
  **no versen sobre derechos o sanciones susceptibles de valoración económica**; y aquellos en que
  junto a pretensiones evaluables **se acumulen otras no valorables**. También ciertos actos de
  **Seguridad Social** (inscripción de empresas, formalización de cobertura de riesgos profesionales,
  tarifación, cobertura de IT, afiliación, alta, baja y variaciones de datos).

**Instrucción:** al fijar la cuantía, expón al cliente el intercambio completo — tope de costas **vs.**
abreviado **vs.** apelabilidad — y deja constancia de la decisión. No la infles ni la deprimas para
manipular las costas: la cuantía se fija con arreglo al art. 42 y el tribunal puede corregirla.
Verifica los arts. 40 y 41 LJCA con `buscar_articulo` antes de citarlos `[verificar]`.

---

## 6. Salidas y entregables

- **Escritos:** otrosí / suplico de no imposición de costas; escrito de impugnación de tasación
  (por indebidas y, subsidiariamente, por excesivas); alegaciones al informe del Colegio; recurso de
  revisión contra el decreto; nota de riesgo de costas para el cliente.
- **Estilo:** skill `estilo-escritos-judiciales`. **Entrega:** Word `.docx` maquetado (skill `docx`).
- **Jurisprudencia:** **prohibido** citar ECLI, ROJ, fecha o ponente de memoria. Verifica con
  `buscar_sentencias` / `buscar_por_cita`. Sin verificación → `[verificar]` y dilo.
- **Normativa autonómica y local:** el conector **no la cubre**. Los criterios orientadores de
  honorarios son **colegiales**: pídeselos al usuario, **no los cites de memoria** `[verificar]`.
- **Datos personales:** cero datos reales. Usa `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`.
- **Perfil del despacho:** `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/`.
- **Anclas:** `references/anclas-normativas-ca.md` § 7 (costas) y § 3 (umbrales).
