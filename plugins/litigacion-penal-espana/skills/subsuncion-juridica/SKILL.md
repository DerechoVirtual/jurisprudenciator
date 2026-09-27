---
name: subsuncion-juridica
description: Silogismo de subsuncion sobre el tipo penal. Impone identificar la redaccion del CP vigente a la fecha de los hechos (art. 2 CP) y comprobar si la posterior es mas favorable (art. 2.2 CP) — con la LO 1/2025 y la LO 1/2026 esto ya no es teorico. Principio de legalidad y prohibicion de analogia in malam partem (art. 4.1 CP). In dubio pro reo y presuncion de inocencia (art. 24.2 CE). Jurisprudencia SIEMPRE con el conector MCP jurisprudenciator. Usar con subsumir, pulir escrito penal, conectar jurisprudencia con los hechos.
---

# Subsunción jurídico-penal — el silogismo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Paso 0: redacción aplicable** → `buscar_articulo` (`ley="CP"`): indica desde cuándo rige y qué norma la dio; si la reforma es posterior a los hechos, la anterior sale de `buscar_boe` → `leer_boe`.
- **Premisa mayor jurisprudencial** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3` y `terminos`; si la lectura pide una comprobación, completa con `continuar_lectura`.
- **Presunción de inocencia e in dubio pro reo** → `buscar_sentencias` (`base="TC"`).
- **Cada cita del borrador** → `buscar_por_cita`.
- **Borrador reescrito** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

> **Fuente de cifras:** `references/anclas-normativas-penal.md`. El texto vigente de cualquier
> artículo se comprueba con `buscar_articulo` **antes** de citarlo.

## Cuándo activar

- AUTOMÁTICAMENTE tras `redactor-escrito-seccion`, escritos de acusación o defensa, y recursos
- "Subsumir los hechos en el tipo", "pulir escrito", "conectar jurisprudencia con los hechos"
- Cuando un borrador cita una STS pero no la aterriza en el folio
- **Siempre que los hechos sean anteriores al 10-4-2026** ← comparación de penas obligatoria

---

## 🚨 PASO 0 — OBLIGATORIO E INELUDIBLE: ¿QUÉ LEY SE APLICA?

**Antes de subsumir nada hay que saber en qué texto se subsume.** Con **LO 1/2025** (vigente
**3-4-2025**) y **LO 1/2026** (vigente **10-4-2026**), esto **ya no es un ejercicio teórico**: es la
primera fuente de error del plugin.

**Art. 2 CP — texto literal verificado:**

> «1. **No será castigado ningún delito con pena que no se halle prevista por ley anterior a su
> perpetración.** Carecerán, igualmente, de efecto retroactivo las leyes que establezcan medidas de
> seguridad.
> 2. No obstante, **tendrán efecto retroactivo aquellas leyes penales que favorezcan al reo**,
> aunque al entrar en vigor hubiera recaído sentencia firme y el sujeto estuviese cumpliendo
> condena. **En caso de duda sobre la determinación de la Ley más favorable, será oído el reo.** Los
> hechos cometidos bajo la vigencia de una Ley temporal serán juzgados, sin embargo, conforme a
> ella, salvo que se disponga expresamente lo contrario.»

### Protocolo del Paso 0

1. **Fijar la fecha de los hechos** (`/cronologia`, carril ①). Delito continuado o permanente → la
   del **cese**.
2. **`buscar_articulo` sobre el tipo** → identificar **qué redacción estaba vigente ese día**
   (art. 2.1 CP).
3. **`buscar_articulo` de nuevo** → **redacción vigente hoy**.
4. **Si difieren → COMPARACIÓN DE PENAS OBLIGATORIA** (art. 2.2 CP y DT de la LO 1/2026: los hechos
   cometidos hasta la entrada en vigor se juzgan conforme a la ley del tiempo de su comisión, **pero
   se aplica la LO 1/2026 si es más favorable al reo**).
5. **La comparación se hace en BLOQUE, no artículo por artículo:** se compara el resultado punitivo
   íntegro de cada redacción (tipo + agravaciones + reglas de determinación + suspensión), no
   preceptos sueltos. *Regla de bloque: contrastar con `buscar_sentencias` antes de fundar la
   estrategia.*
6. **Pedir expresamente la más favorable** en el escrito, con la comparación explicitada.
7. **En caso de duda, el reo debe ser oído** (art. 2.2 in fine).

```markdown
## LEY PENAL APLICABLE (art. 2 CP)

| | Redacción a la fecha de los hechos | Redacción vigente hoy |
|---|---|---|
| **Norma** | [LO X, vigente desde FECHA] | [LO Y, vigente desde FECHA] |
| **Precepto** | art. [N] CP | art. [N] CP |
| **Pena** | [pena] | [pena] |
| **Agravaciones aplicables** | [...] | [...] |
| **Resultado punitivo en bloque** | [...] | [...] |

**Más favorable:** [cuál] → **se solicita su aplicación** al amparo del **art. 2.2 CP**.
```

> **⚠️ Trampa concreta y frecuente — ESTAFA.** Todo material anterior a abril de 2026 razona que «el
> art. 248 CP define y el art. 249 CP pena». **Falso desde el 10-4-2026**: hoy el **art. 248**
> contiene definición **y** pena (prisión 6 meses-3 años) **y** el delito leve (≤ 400 € → multa 1-3
> meses, con regla de **multirreincidencia**). El **art. 249** regula desde la **LO 14/2022**
> (vigente 12-1-2023) la **estafa informática y con instrumentos de pago**. Un escrito que cite el
> art. 249 como penalidad de la estafa común está mal. Ver `references/anclas-normativas-penal.md`.

---

## 🚨 PASO 1 — LEGALIDAD Y PROHIBICIÓN DE ANALOGÍA IN MALAM PARTEM

**Art. 4.1 CP — texto literal verificado:**

> «**Las leyes penales no se aplicarán a casos distintos de los comprendidos expresamente en
> ellas.**»

**Consecuencias operativas sobre la subsunción:**

- **La analogía in malam partem está prohibida.** No se puede extender un tipo a un supuesto que su
  letra no comprende **por muy merecedor de reproche que parezca**. Si el hecho no está
  expresamente comprendido, **no hay delito**: la respuesta es la **absolución**, no la
  interpretación extensiva.
- **La interpretación extensiva contra reo es el límite.** Toda subsunción debe poder anclarse en el
  **tenor literal posible** del precepto. **Test operativo: ¿resiste esta subsunción la lectura
  literal del tipo? Si hay que forzar la palabra, la subsunción es inválida.**
- **La analogía in bonam partem sí es admisible** — y el propio CP la incorpora: la **atenuante
  analógica del art. 21.7ª** («cualquier otra circunstancia de análoga significación», verificado).
- **Art. 4.2 CP (verificado):** si el juez estima digna de represión una conducta no penada, **se
  abstiene de todo procedimiento** y lo expone al Gobierno. → **La laguna la colma el legislador, no
  el tribunal.** Es un argumento de defensa citable literalmente.
- **Art. 4.3 y 4.4 CP (verificado):** vía de indulto y **suspensión de la ejecución cuando el
  cumplimiento pudiera vulnerar el derecho a un proceso sin dilaciones indebidas**.

> **Uso defensivo:** cuando la acusación construye el tipo «por equivalencia» o «por identidad de
> razón», el art. 4.1 CP es la respuesta directa y literal.

---

## 🚨 PASO 2 — PRESUNCIÓN DE INOCENCIA E IN DUBIO PRO REO

**Art. 24.2 CE — verificado:** derecho «a **no declarar contra sí mismos**, a **no confesarse
culpables** y a la **presunción de inocencia**».

| | **Presunción de inocencia** | **In dubio pro reo** |
|---|---|---|
| **Naturaleza** | **Derecho fundamental** (art. 24.2 CE) — amparable | **Regla de valoración** de la prueba |
| **Opera cuando** | **NO hay** prueba de cargo válida y suficiente | **SÍ hay** prueba, pero deja **duda razonable** |
| **Se combate en** | Casación / amparo — pero ⚠️ ver límite del art. 847 | Instancia y apelación |
| **Consecuencia** | Absolución por vacío probatorio | Absolución por duda |

**No son lo mismo y confundirlas debilita el escrito.** Se alegan **por separado y en este orden**:
primero que **no hay prueba de cargo** (presunción de inocencia); **subsidiariamente**, que si la
hay, **no despeja la duda razonable** (in dubio pro reo).

**Exigencias de la prueba de cargo — todas deben concurrir:**

1. **Existente** — que la haya
2. **Válida** — no obtenida violentando derechos fundamentales (**art. 11.1 LOPJ**, verificado: «no
   surtirán efecto las pruebas obtenidas, **directa o indirectamente**, violentando los derechos o
   libertades fundamentales»)
3. **Practicada en el juicio oral** — con contradicción, salvo las excepciones tasadas de los
   **arts. 714 y 730 LECrim** y la prueba preconstituida del **art. 449 bis**
4. **Suficiente** — que soporte racionalmente la conclusión
5. **Racionalmente valorada** — motivación

**La carga es íntegramente de la acusación. La defensa no prueba la inocencia.** Y el **silencio del
acusado no es prueba de cargo ni suple su ausencia** (arts. 24.2 CE, 118.1.g y h LECrim).

> **⚠️ Límite de casación que condiciona cómo se redacta desde la instancia — art. 847 LECrim:**
> contra sentencias dictadas **en apelación por las Audiencias Provinciales** (y por la Sala de lo
> Penal de la AN) **solo cabe el motivo de infracción de ley del art. 849.1.º**. **No caben** el
> 849.2.º, ni 850/851, ni **852 (infracción de precepto constitucional)**. → **Si la vulneración de
> la presunción de inocencia solo se va a poder residenciar por 849.1.º, hay que haberla construido
> desde el principio como error de subsunción sobre hechos probados.** Ver
> `references/anclas-normativas-penal.md` § 4.

---

## El silogismo penal

```
PREMISA MAYOR — el tipo penal
  Art. [N] CP, en la redacción dada por [LO X], vigente a la fecha de los hechos ([FECHA]).
  Texto literal (verificado con buscar_articulo): «[...]»
  Elementos que exige: [enumerados — remitir a /cuadro-elementos]

PREMISA MENOR — los hechos, con folio
  [Hecho concreto que realiza cada elemento] — f. [N]
  [Hecho concreto que realiza cada elemento] — f. [N]

CONCLUSIÓN
  [Concurre / NO concurre el tipo] porque [el elemento X] [se realiza / no se realiza],
  al no obrar en las actuaciones [prueba de cargo sobre ese extremo].
```

**El silogismo se rompe por la premisa menor mucho más a menudo que por la mayor.** La discusión
sobre el Derecho suele ser estéril; la que gana es **«ese hecho no está en ningún folio»**.

## Patrón a corregir — citas «sueltas»

❌ **MAL:**

> «...la jurisprudencia del Tribunal Supremo establece que el engaño ha de ser bastante. En el
> presente caso, el acusado no engañó a nadie...»

✅ **BIEN (subsuntivo, penal, anclado al folio y a la redacción aplicable):**

> «...el **art. 248 CP**, en la redacción vigente a la fecha de los hechos, exige un **engaño
> bastante** para producir error en otro. La Sala Segunda ha precisado que el carácter «bastante»
> del engaño se determina en atención a los **deberes de autoprotección** exigibles a la víctima
> según las circunstancias `[verificar doctrina y ECLI con buscar_sentencias antes de citar]`.
> Aplicada esta exigencia a los hechos de autos: [VÍCTIMA] es [cualidad profesional acreditada al
> **f. [N]**], recibió la documentación obrante al **f. [N]** —cuya sola lectura revelaba
> [circunstancia]— y dispuso de [plazo] antes de realizar el acto de disposición del **f. [N]**. El
> engaño que se imputa a [ACUSADO] no era, por tanto, **bastante** para producir el error en esa
> concreta persona y en esas concretas circunstancias. **Falta un elemento del tipo objetivo y, con
> él, la tipicidad**, sin que el art. 4.1 CP permita extender el precepto a un supuesto que su
> letra no comprende.»

**Anatomía de la versión correcta:**
1. **Premisa mayor con la redacción aplicable identificada** (no «el art. 248» a secas)
2. **Doctrina concreta**, marcada para verificación si no está verificada
3. **Subsunción hecho a hecho, cada uno con su FOLIO**
4. **Conclusión en clave de elemento del tipo** («falta el elemento X»), no en clave narrativa
5. **Cierre con el límite de legalidad** (art. 4.1 CP)

---

## Flujo

### 1. Paso 0 — ley aplicable
Fecha de los hechos → redacción vigente entonces → redacción hoy → **comparación en bloque si
difieren** → pedir la más favorable (art. 2.2 CP).

### 2. Cargar
Escrito o borrador + `matters/<slug>/cuadro-elementos.md` + `matters/<slug>/cronologia.md` + las
actuaciones por folios.

### 3. Verificar cada precepto citado
`buscar_articulo` sobre **cada** artículo del escrito. **El CP se ha modificado dos veces entre 2025
y 2026**: ningún precepto se da por sabido.

### 4. Verificar cada cita jurisprudencial
`buscar_por_cita` para cada ECLI/ROJ. **Si no se verifica, se elimina o se marca**
`[verificar con buscar_sentencias]`. **⛔ Prohibido inventar ECLI, ROJ, fechas, ponentes o
fundamentos.**

### 5. Reescribir las citas sueltas
Añadir: doctrina concreta → subsunción al folio → conclusión sobre el elemento del tipo.

### 6. Comprobar los tres controles
- ¿Está identificada la **redacción aplicable** y hecha la **comparación** si procede? (art. 2)
- ¿Hay alguna **subsunción que fuerce el tenor literal**? (art. 4.1)
- ¿Está alegada **por separado** la presunción de inocencia y, subsidiariamente, el in dubio pro reo?

### 7. Eliminar redundancia
Si dos resoluciones dicen lo mismo, la más reciente y la unificadora. No abrumar.

### 8. Output
Escrito pulido + **diff** frente al original, marcando los cambios y las verificaciones hechas.

## Reglas

1. **El Paso 0 no se salta nunca.** Un escrito penal que no identifica la redacción aplicable está
   incompleto, y si los hechos son anteriores al 10-4-2026 y no hay comparación de penas, **está
   mal**.
2. **Jurisprudencia que no aterriza en un folio es jurisprudencia perdida.** Fuera.
3. **El FOLIO es la cuerda** entre el hecho y la doctrina. Si la frase no cita folio, no está
   subsumiendo. ⛔ **Nunca «Doc. nº X»**.
4. **Cada cita = un punto subsuntivo concreto.** No «como la jurisprudencia mayoritaria entiende...».
5. **Conclusión en clave de elemento del tipo**, no narrativa.
6. **⛔ Prohibido inventar** penas, plazos, artículos, ECLI, ROJ, fechas o ponentes. Lo no
   verificable se marca `[verificar]` **y se dice**.
7. **⛔ Prohibida la analogía in malam partem** (art. 4.1 CP), también al construir el propio
   argumento de acusación.
8. **Protección de datos.** `[INVESTIGADO]`, `[ACUSADO]`, `[VÍCTIMA]`, `[TESTIGO]`, `[ÓRGANO]`,
   `[FECHA]`. **Cero datos reales.** Infracciones y condenas = **art. 10 RGPD**; cuidado extremo con
   **víctimas menores** y **delitos contra la libertad sexual**.

## ⛔ Fuera de esta skill

- **Razonamiento civil.** Arts. 1101, 1124, 1902 CC, LEC, cláusulas abusivas, incumplimiento
  contractual. ⚠️ **Riesgo real en delitos patrimoniales**: en la estafa, la frontera con el
  incumplimiento civil se argumenta como **ausencia de dolo antecedente** (art. 248 CP), **jamás**
  invocando el art. 1101 CC.
- **MASC y burofax.** Del orden civil.
- **El «fiscal instructor».** Instruye el **Juez de Instrucción**; la reforma está **en tramitación**
  (prevista 1-1-2028) y no se cita como Derecho vigente.
