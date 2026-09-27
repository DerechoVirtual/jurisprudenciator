---
name: audiencia-preliminar-abreviado
description: >-
  Prepara la AUDIENCIA PRELIMINAR del art. 785 LECrim, el trámite nuevo creado por la LO 1/2025 (vigente 3-4-2025) que reordenó el juicio oral del procedimiento abreviado y trasladó a él la conformidad. Actívala ante "audiencia preliminar", "art. 785", "cuestiones previas", "artículos de previo pronunciamiento", "vista previa del abreviado", "conformidad en la audiencia preliminar", "negociar la conformidad antes de la vista previa", "cuándo se plantea la nulidad", "el 785 ya no es admisión de prueba", "señalamiento del juicio", "qué llevo a la audiencia preliminar". Requisito previo: procedimiento ABREVIADO con juicio oral ya abierto y audiencia preliminar señalada. Si la conformidad es en el juzgado de guardia (art. 801), usar /juicio-rapido; si se trata de comparar cauces de conformidad, /conformidad-penal-catalogo; si el procedimiento es ante el Tribunal del Jurado, su audiencia preliminar es la del art. 30 LOTJ → /tribunal-jurado.
---

# Audiencia preliminar del procedimiento abreviado — art. 785 LECrim

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Texto vigente de los arts. 785, 786 y 787 LECrim tras la LO 1/2025** → `buscar_articulo` (`ley="LECrim"`), para no arrastrar la numeración anterior al 3-4-2025.
- **Criterio de las Audiencias sobre la nueva audiencia preliminar** (cuestiones previas, nulidades, prueba) → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="AP"`, `provincia` de la causa, `fecha_desde="03/04/2025"`) + `leer_sentencias` con `parrafos=3`.
- **Doctrina de la Sala Segunda sobre las nulidades y la prueba ilícita que se plantearán** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3`; en presunción de inocencia y prueba ilícita, también `base="TC"`.
- **Pena del delito y margen de la conformidad** → `buscar_articulo` (`ley="CP"`, tipo aplicable y reglas de determinación de la pena).
- **Persona jurídica acusada que se conforma (art. 785.11)** → `buscar_empresa_mercantil` para comprobar quién la administra y la representa.
- **Revisar el guion y el escrito de alegaciones antes de la vista** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Trámite **NUEVO** creado por la **LO 1/2025**, de 2 de enero (eficiencia del Servicio Público de Justicia), **en vigor desde el 3-4-2025**. Ha cambiado la práctica del abreviado: **es ahora el momento decisivo del procedimiento.**

> ## 🚨 BANNER DE ERRATA — leer antes de usar cualquier material
>
> La LO 1/2025 **reordenó los arts. 785-787 LECrim**. Todo material, formulario, plantilla, manual o apunte **anterior a abril de 2025 cita mal estos artículos**:
>
> | Artículo | Contenido **ANTERIOR** (derogado) | Contenido **VIGENTE** desde 3-4-2025 |
> |---|---|---|
> | **785** | Admisión de prueba y señalamiento | **AUDIENCIA PRELIMINAR** + **CONFORMIDAD** (apdos. 4-11) |
> | **786** | Celebración del juicio oral (y cuestiones previas del 786.2) | **Señalamiento** del juicio oral |
> | **787** | **CONFORMIDAD** | **Celebración del juicio oral** (asistencia, ausencia, lectura de escritos) |
>
> **Consecuencias prácticas:**
> - «Cuestiones previas del art. 786.2» → **ya no existe**. Su sede es la **audiencia preliminar del art. 785.1**.
> - «Conformidad del art. 787» → **ya no es correcto**. La conformidad está hoy en el **art. 785.4 a 785.11** (pero ojo al § 6: la ley **no actualizó las remisiones**).
> - «El 785 es la admisión de prueba» → derogado.
>
> **Verificado literalmente con `buscar_articulo` (BOE-A-1882-6036, redacción LO 1/2025) el 2026-07-17.** Anclas: `references/anclas-normativas-penal.md` § 2.

---

## 1. Qué es y por qué importa

Convocatoria del fiscal y de las partes por el **órgano competente para el enjuiciamiento** —no el instructor— **«en cuanto las actuaciones se encontraren a disposición»** de aquel (art. 785.1), a una audiencia previa al juicio en la que se depura **todo** lo que antes se dispersaba entre el escrito de defensa, el auto de admisión de prueba y el trámite de cuestiones previas del inicio del juicio.

**Por qué es ahora el momento decisivo:** concentra en un solo acto la **conformidad**, las **nulidades**, la **prueba** y las **excepciones**; y el **art. 787.3** cierra la puerta a replantear en el juicio lo que pudo plantearse aquí. Lo que no se lleve preparado a la audiencia preliminar, se pierde.

---

## 2. Objeto de la audiencia — art. 785.1

Texto verificado: las partes **«podrán exponer lo que estimen oportuno acerca de»**:

1. La posibilidad de **conformidad** del acusado o acusados.
2. La **competencia** del órgano judicial.
3. La **vulneración de algún derecho fundamental**.
4. La existencia de **artículos de previo pronunciamiento**.
5. **Causas de la suspensión** del juicio oral.
6. **Nulidad de actuaciones**.
7. El **contenido, finalidad o nulidad de las pruebas propuestas**.

Y además (párr. 2 del 785.1):

8. Proponer la **incorporación de informes, certificaciones y otros documentos**.
9. Proponer la práctica de **pruebas de las que no se hubiera tenido conocimiento** al formular los escritos de acusación o defensa.

> El **art. 785.3** añade la función que antes tenía el viejo 785: el órgano **examina las pruebas propuestas y resuelve admitiendo las pertinentes y rechazando las demás**, y **previene lo necesario para la práctica de la prueba anticipada**.

---

## 3. Asistencia — art. 785.2

- **Asistencia PRECEPTIVA** del **acusado** y del **abogado defensor**: «La celebración de la audiencia preliminar requiere la asistencia del acusado y del abogado defensor.»
- **NO se suspende** por la **inasistencia injustificada del acusado debidamente citado**, ni por la **incomparecencia injustificada de las demás partes citadas en forma**: se celebra **«a los efectos de sustanciar las cuestiones que puedan resolverse en ausencia»**.
- **La citación debe advertirlo**: «En la citación se informará al acusado y a las partes que su injustificada incomparecencia no suspenderá la audiencia preliminar.»

> **⚠️ Tensión que debe manejarse.** La asistencia es «preceptiva» (785.2 párr. 1) pero la ausencia injustificada no suspende (párr. 2). El acusado ausente **pierde** la posibilidad de conformarse —que exige su presencia y su manifestación personal (785.5 y 785.7)—, mientras las cuestiones resolubles en ausencia (nulidades, prueba, competencia) se sustancian igualmente. **Comprobar siempre que la citación contenía la advertencia legal**: su ausencia es materia de nulidad.

---

## 4. Resolución y régimen de recursos — art. 785.3

- **Forma:** resolución **oral**, salvo que, **por la complejidad de las cuestiones planteadas**, hubiera de serlo **por escrito**, en cuyo caso el **auto** se dicta en el plazo de **10 días**.
- **Recursos:** «**Contra la resolución adoptada no cabrá recurso alguno, sin perjuicio de la pertinente protesta y de que la cuestión pueda ser reproducida, en su caso, en el recurso frente a la sentencia**».
- **⭐ Excepción:** «**salvo que dicha resolución ponga fin al procedimiento, en cuyo caso será susceptible de recurso de apelación**, en el plazo y con las formalidades prevenidas en los artículos 790 y siguientes».

> **⭐ SIN PROTESTA NO HAY GRAVAMEN.** La regla general es la **irrecurribilidad**. La **única** llave para reproducir la cuestión en el recurso contra la sentencia es la **protesta formulada en el acto**. Omitirla equivale a consentir la resolución. **Formularla siempre, expresamente, y comprobar que queda registrada** — la comparecencia se registra conforme al art. 743 (art. 785.12).

---

## 5. Conformidad — arts. 785.4 a 785.11

### 5.1 Objeto y límites (785.4)
Las partes pueden pedir sentencia de conformidad **con el escrito de acusación que contenga pena de mayor gravedad**, o con el que se presente **en ese acto**, que **«no podrá referirse a hecho distinto ni contener calificación más grave que la del escrito de acusación anterior»**. El órgano dictará sentencia de conformidad con la pena manifestada por la defensa y el acusado si concurren los requisitos siguientes.

> **Nota:** el vigente art. 785.4 **no reproduce** el límite de «seis años de prisión» que figuraba en el viejo art. 787.1. **Verificar el límite punitivo aplicable** con `buscar_articulo` y contrastar con `buscar_sentencias` antes de asesorar sobre una conformidad de pena elevada. `[verificar]`

### 5.2 ⭐ NOVEDAD — audiencia previa a la víctima (785.4 párr. 2)
El **Ministerio Fiscal oirá previamente a la víctima o perjudicado**, **aunque no estén personados en la causa**:
- siempre que **hubiera sido posible** y **se estime necesario** para ponderar correctamente los efectos y el alcance de la conformidad;
- **y en todo caso** cuando la **gravedad o trascendencia del hecho** o la **intensidad o la cuantía** sean **especialmente significativos**;
- **así como en todos los supuestos** en que víctimas o perjudicados se encuentren en **situación de especial vulnerabilidad**.

**Táctica:** es un **trámite del Fiscal**, no de la defensa. Pero condiciona la negociación (tiempos, posición del Fiscal) y su **omisión** en un caso en que era obligada es un **defecto alegable**. Como acusación particular, exigir su cumplimiento.

### 5.3 Control judicial (785.5 y 785.6)
- **785.5:** si, a partir de la **descripción de los hechos aceptada por todas las partes**, el órgano entiende que la **calificación es correcta** y que la **pena es procedente** según dicha calificación, dicta sentencia de conformidad. **Habrá oído en todo caso al acusado acerca de si su conformidad ha sido prestada libremente y con conocimiento de sus consecuencias.**
- **785.6:** si considera **incorrecta la calificación** o entiende que la **pena no procede legalmente**, **requiere a la parte que presentó el escrito de acusación más grave** para que manifieste si se ratifica. **Solo** si la modifica en términos tales que la calificación sea correcta y la pena procedente, **y el acusado presta de nuevo su conformidad**, puede dictarse sentencia de conformidad. **En otro caso, ordenará la celebración del juicio.**

### 5.4 ⭐ NOVEDAD — deber del letrado (785.7)
Una vez que la defensa manifiesta su conformidad, el juez **informa al acusado de sus consecuencias** y le requiere para que manifieste si presta la suya. Si el órgano **alberga dudas** sobre la libertad de la conformidad, **acuerda la celebración del juicio**. También puede acordarla cuando, pese a la conformidad del acusado, **su defensor lo considere necesario** y el órgano estime **fundada** su petición.

> **⭐ 785.7 in fine — DEBER NUEVO Y LITERAL:**
> **«El letrado o la letrada facilitará por escrito a la persona a quien defiende la información sobre el acuerdo alcanzado.»**
>
> **Documentarlo SIEMPRE.** Es una obligación legal del letrado y la mejor protección frente a una futura reclamación del cliente («no me explicaron lo que firmaba»). Ver § 8.3: hay que **llevar el documento redactado** a la audiencia. Conservarlo en el expediente con acuse de recibo firmado.

### 5.5 Medidas protectoras (785.8)
**No vinculan** al órgano las conformidades sobre la **adopción de medidas protectoras** en los casos de **limitación de la responsabilidad penal**.

### 5.6 ⭐ Sentencia oral y firmeza en el acto (785.9)
- La sentencia de conformidad se dicta **oralmente** y se documenta conforme al **art. 789.2**, sin perjuicio de su ulterior redacción.
- Si el **fiscal y las partes**, conocido el fallo, expresan su **decisión de no recurrir**, el juez, **en el mismo acto, declara oralmente la FIRMEZA** de la sentencia.
- Y se pronuncia, **previa audiencia de las partes**, sobre la **suspensión de la pena impuesta o su sustitución**, cuando proceda.
- También resuelve sobre los **aplazamientos de las responsabilidades pecuniarias** y se realizan, **en cuanto fuera posible**, los **requerimientos y liquidaciones de condena** de las penas impuestas.

> **⚠️ Todo se juega en un solo acto.** Firmeza, suspensión y liquidación salen de la misma comparecencia. **Ir con la suspensión preparada** (art. 80 CP): requisitos, documentación de la responsabilidad civil o del compromiso, y —si hay antecedentes— el argumento del **art. 80.2.1.ª** en su redacción de la LO 1/2026 (antecedentes irrelevantes para valorar la probabilidad de comisión de delitos futuros). Ver skill `ley-penal-en-el-tiempo` § 5 y `ejecucion-penal-liquidacion-condena-suspension-catalogo`.

### 5.7 Recurribilidad limitada (785.10)
«**Únicamente serán recurribles las sentencias de conformidad cuando no hayan respetado los requisitos o términos de la conformidad, sin que la persona acusada pueda impugnar por razones de fondo su conformidad libremente prestada.**»

**Advertir al cliente por escrito**: conformarse **cierra el fondo**. No hay arrepentimiento posterior.

### 5.8 Persona jurídica (785.11)
La conformidad la presta su **representante especialmente designado**, **siempre que cuente con PODER ESPECIAL**. Se sujeta a los requisitos de los apartados anteriores, puede realizarse **con independencia de la posición de las demás personas acusadas**, y **su contenido no vincula en el juicio** que se celebre respecto de estas.

> **Comprobar el poder especial ANTES de la audiencia.** Su falta impide la conformidad. Y recordar el **conflicto estructural**: defender a la persona jurídica y a la persona física investigada por los mismos hechos genera **conflicto de interés**.

### 5.9 Registro (785.12)
La comparecencia se registra en el modo previsto en el **art. 743**.

---

## 6. ⚠️ Descoordinación legislativa — señalarla siempre

**La LO 1/2025 NO actualizó las remisiones internas.** Verificado con `buscar_articulo`:

- **Art. 784.3 LECrim** — sigue con **redacción de la LO 13/2015, vigente desde 6-12-2015**, y dice literalmente que la defensa podrá manifestar su conformidad con la acusación **«en los términos previstos en el artículo 787»**, y añade «sin perjuicio de lo dispuesto en el **artículo 787.1**».
- **Art. 801.1 y 801.2 LECrim** — siguen remitiendo al **art. 787** para el control de la conformidad ante el juzgado de guardia. `[verificar la redacción exacta con buscar_articulo antes de citar]`

**Pero el art. 787 vigente ya no regula la conformidad**: regula la **celebración del juicio oral**. El régimen sustantivo de la conformidad está hoy en el **art. 785.4 a 785.11**.

**Cómo operar:**
1. **Citar el art. 785** como sede de la conformidad. Es donde está el régimen.
2. Si se reproduce la remisión legal del **784.3** o del **801**, hacerlo **con conciencia del desajuste** y explicándolo — no copiar «art. 787» sin más, porque hoy conduce a un precepto que no dice lo que la remisión presupone.
3. **⚠️ Contrastar con `buscar_sentencias`** cómo están resolviendo los tribunales esta remisión antes de fundar una estrategia en ella. **No inventar** la solución ni citar doctrina de memoria.
4. Como argumento, es de **doble filo**: sirve para atacar, pero también puede volverse en contra. Valorar antes de invocarlo.

---

## 7. Guía táctica — por qué es el momento decisivo

**Lo que se pierde si no se plantea aquí.** Verificado — **art. 787.3 LECrim** (redacción LO 1/2025): al inicio de las sesiones del juicio **«únicamente podrá solicitarse la incorporación de informes, certificaciones y otros documentos»** y proponerse la práctica de pruebas **«de las que las partes no hubieran tenido conocimiento al momento de celebrar la comparecencia prevista en el artículo 785»**.

→ **Las nulidades, las excepciones y la prueba conocida NO se replantean en el juicio.** Quien las reserve, las pierde.

### Qué llevar preparado

| Bloque | Preparación |
|---|---|
| **Nulidades** | Informe de viabilidad cerrado, con **folio** de cada vulneración y **árbol de derivadas**. Doctrina **verificada** con `buscar_sentencias`. Skill `prueba-ilicita-nulidad`. |
| **Plazo de instrucción** | Línea temporal del **art. 324**: incoación, cada auto de prórroga y su fecha de **dictado**, diligencias acordadas tras el vencimiento → **inválidas ex art. 324.3**. Skill `cronologia`. |
| **Competencia** | Objetiva, funcional y territorial. Comprobada antes, no improvisada. |
| **Artículos de previo pronunciamiento** | Identificados y fundados. Verificar el catálogo con `buscar_articulo` antes de invocarlos. |
| **Prueba** | Pertinencia y **necesidad** de cada medio propuesto, uno a uno. Preparar la **impugnación** de la prueba de la acusación (contenido, finalidad o nulidad — 785.1). Prueba anticipada. |
| **Conformidad negociada** | Banda de pena aceptable **cerrada con el cliente por escrito ANTES**. Suspensión (art. 80 CP) preparada. Responsabilidad civil documentada. **Documento del 785.7 in fine redactado.** |
| **Protesta** | Redactada. Para **cada** cuestión que pueda desestimarse. |
| **Persona jurídica** | **Poder especial** comprobado y aportado. |

### Reglas de oro
1. **Ir con la conformidad decidida, no decidirla en la sala.** El cliente debe llegar con la banda de pena aceptada por escrito.
2. **Protesta para todo lo que se desestime.** Sin excepción. Es la única llave del recurso.
3. **La suspensión se juega aquí** (785.9). Llevarla preparada.
4. **Comprobar la citación** del acusado y la advertencia del 785.2.
5. **Nada que pueda plantearse aquí se reserva para el juicio.** El 787.3 lo impide.

---

## 8. Salida

### 8.1 Guion de la audiencia preliminar
Cuestiones **ordenadas** en el orden lógico de planteamiento (de lo que puede poner fin al procedimiento a lo que solo afecta a la prueba):

1. **Competencia** del órgano.
2. **Artículos de previo pronunciamiento**.
3. **Vulneración de derechos fundamentales** → art. 11.1 LOPJ.
4. **Nulidad de actuaciones** (arts. 238/240 LOPJ) — incluida la del **art. 324.3**.
5. **Nulidad / contenido / finalidad de las pruebas** propuestas de contrario.
6. **Causas de suspensión**, si las hay.
7. **Prueba propia**: pertinencia y necesidad; incorporación de documentos; prueba sobrevenida; prueba anticipada.
8. **Conformidad**, si procede.

Para cada una: **fundamento verificado**, **folio**, petición concreta y **protesta prevista**.

### 8.2 Protesta a formular
Fórmula lista para el acto, por cada cuestión desestimada:
> «Con la venia. Desestimada la cuestión, esta parte formula **expresa PROTESTA** a los efectos del **art. 785.3 LECrim**, y deja reservada la reproducción de la cuestión en el recurso frente a la sentencia. Interesa que quede constancia en el registro de la comparecencia (art. 785.12 en relación con el art. 743 LECrim).»

### 8.3 ⭐ Documento del art. 785.7 in fine (si hay conformidad)
Documento **escrito** al defendido con la **información sobre el acuerdo alcanzado**. Contenido mínimo:
- Hechos que se aceptan y **calificación** conforme.
- **Pena** exacta conformada (todas: privativas de libertad, multa, accesorias, privación del permiso, etc.).
- **Responsabilidad civil** y forma de pago o compromiso.
- **Suspensión o sustitución**: si se pedirá, requisitos del art. 80 CP y **riesgo de que se deniegue**.
- **⚠️ Advertencia expresa**: la sentencia **solo es recurrible si no se respetan los requisitos o términos de la conformidad**; **no cabe impugnar por razones de fondo** la conformidad libremente prestada (**art. 785.10**). Y si fiscal y partes no recurren, la **firmeza se declara oralmente en el acto** (785.9).
- **Alternativa**: qué ocurriría si se va a juicio (pronóstico honesto).
- **Fecha, firma del letrado y acuse de recibo firmado por el defendido.**

Entregable en Word **`.docx`** (skill `docx`). Marcadores `[ACUSADO]`, `[FECHA]`. **Cero datos reales.** Conservar en el expediente.

---

## 9. Reglas de la casa

- **⛔ NO existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. La reforma que atribuiría la instrucción al Ministerio Fiscal está **en tramitación**, prevista para **1-1-2028**: nunca como Derecho vigente, ni citar «art. 4 bis EOMF». (El Fiscal sí interviene en la audiencia preliminar y tiene el deber de oír a la víctima del 785.4 — eso es otra cosa.)
- **⛔ Nada de MASC.** Orden **civil**. En el abreviado no existe.
- **⛔ Prohibido inventar** penas, plazos, ordinales o artículos. Verificar con `buscar_articulo`. Lo no verificable → `[verificar]` **y decirlo**.
- **⛔ Prohibido citar jurisprudencia** (ECLI, ROJ, fecha, ponente) sin verificarla con `buscar_sentencias` / `buscar_por_cita` / `leer_sentencias`.
- **Datos personales:** `[ACUSADO]`, `[INVESTIGADO]`, `[VÍCTIMA]`, `[FECHA]`. Categoría especial: **art. 10 RGPD** (infracciones y condenas). Ver `PROTECCION-DATOS.md`.
- Perfil del despacho: `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.
- Anclas: `references/anclas-normativas-penal.md` § 2 (LO 1/2025), § 3.1 (art. 324), § 5 (art. 801), § 6 (art. 80 CP).

## 10. Skills relacionadas

`prueba-ilicita-nulidad` (nulidades a plantear) · `conformidad-penal-catalogo` · `escrito-defensa-calificacion` · `cronologia` (art. 324) · `ley-penal-en-el-tiempo` (ley más favorable y art. 80.2.1.ª) · `ejecucion-penal-liquidacion-condena-suspension-catalogo` (suspensión del 785.9).
