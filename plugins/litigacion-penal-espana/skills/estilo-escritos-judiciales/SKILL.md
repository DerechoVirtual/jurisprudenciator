---
name: estilo-escritos-judiciales
description: Capa de estilo que aplica la pluma de la casa a cualquier escrito judicial penal. Estructura tripartita, contrastes, explicacion del por que antes del que, cero adjetivos vacios, anclaje al folio de las actuaciones. Respeta la estructura por conclusiones numeradas del art. 650 LECrim y el tono objetivo del relato de hechos. Usar con aplica mi estilo o pluma de la casa.
---

# Pluma de la casa — estilo redaccional penal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Pasada de anclaje: cada ECLI o ROJ del escrito** → `buscar_por_cita`.
- **Párrafo literal que se transcribe** → `leer_sentencias` con `parrafos=3` y `terminos`, para no alterar la cita al reescribir.
- **Artículos citados** → `buscar_articulo`; antes de entregar, `verificar_escrito` sobre el texto final.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Perfil del abogado y estilo de la casa.** Si existe el perfil de estilo del despacho, manda sobre lo que describe esta skill en fórmulas, estructura, tono, forma de citar y maquetación; el estilo de la casa se aplica solo en lo que el perfil no diga.

> Estos patrones son el estándar de buena redacción judicial de la casa. Calibrar con escritos
> reales del despacho cuando se aporten muestras.
>
> **Fuente de cifras:** `references/anclas-normativas-penal.md`.

## Cuándo activar

- AUTOMÁTICAMENTE tras cualquier skill de redacción penal (escritos de calificación, de defensa,
  denuncia, querella, recursos, alegaciones de la audiencia preliminar)
- "Aplica mi estilo", "pásalo por mi pluma", "voz de la casa"
- Antes de la verificación de citas y la entrega final

---

## ⚠️ Límite estructural — el estilo no reescribe la estructura legal

**En penal la estructura del escrito la impone la ley, no el gusto.** Antes de aplicar ningún
patrón:

- **El escrito de calificación va por CONCLUSIONES precisas y numeradas** (art. 650 LECrim,
  verificado). El estilo **no las convierte** en «fundamentos de derecho» ni en prosa corrida.
- **⭐ La conclusión PRIMERA (hechos punibles) es RELATO OBJETIVO.** Aquí **no se aplica** la
  retórica: ni tripartitas, ni contrastes, ni cierres estratégicos. Hechos desnudos, en tercera
  persona, en pasado, con fecha, lugar, sujeto y **folio**. **La argumentación va después.** Un
  relato de hechos adjetivado es un relato débil y da munición a la contraparte.
- El estilo se despliega en: **motivos de recurso**, **alegaciones de la audiencia preliminar
  (art. 785)**, **informe final** y **conclusiones definitivas**.

---

## Patrones a inyectar

### 1. Estructura tripartita

> «Tres son las razones que impiden la subsunción: PRIMERO, [...]; SEGUNDO, [...]; TERCERO, [...]»

> «El tipo exige tres requisitos copulativos: (a) que [...], (b) que [...], y (c) que [...]. Basta
> la ausencia de uno para que el tipo no se realice.»

### 2. Contrastes «una cosa es X, otra cosa es Y»

Separa supuestos cercanos pero jurídicamente distintos. **En penal es el patrón más rentable**,
porque casi toda defensa consiste en desplazar el hecho de una casilla a otra:

> «Una cosa es el **dolo antecedente** —el propósito de no cumplir ya presente al contratar, que es
> lo que exige el art. 248 CP—, y otra muy distinta la imposibilidad sobrevenida de cumplir, que no
> es delito.»

> «Una cosa es el **cooperador necesario** del art. 28.b) CP, que aporta un acto sin el cual el
> hecho no se habría efectuado, y otra el **cómplice** del art. 29 CP, cuya aportación era
> prescindible.»

> «Una cosa es el **error de tipo** del art. 14.1 CP, que recae sobre un hecho constitutivo de la
> infracción, y otra el **error de prohibición** del art. 14.3 CP, que recae sobre su ilicitud. Ni
> el objeto ni la consecuencia son los mismos.»

> «Una cosa es que **no exista prueba de cargo** —y entonces opera la presunción de inocencia del
> art. 24.2 CE—, y otra que, existiendo, **deje duda razonable** —y entonces opera el in dubio pro
> reo—. Se alegan por separado y en ese orden.»

### 3. Explicación del por qué antes del qué

> «Por cuanto el art. 12 CP dispone que las acciones u omisiones imprudentes solo se castigarán
> cuando expresamente lo disponga la Ley, y dado que el art. [N] CP no prevé modalidad imprudente
> alguna, la ausencia de dolo no conduce a una condena atenuada, sino a la **absolución**.»

(NO: «Procede la absolución. El art. 12 CP exige previsión expresa de la imprudencia.»)

### 4. Cierre estratégico

Cada motivo o alegación cierra con tránsito hacia el siguiente o hacia el suplico:

> «En consecuencia, no concurre el elemento del engaño bastante que el art. 248 CP exige, y sin él
> la conducta es atípica, sin que el art. 4.1 CP permita extender el precepto a un caso que su letra
> no comprende — como se interesa en el suplico.»

### 5. Cero adjetivos vacíos

ELIMINAR: «absolutamente claro», «manifiestamente atípico», «indubitadamente acreditado»,
«rotundamente probado», «evidente», «palmario», «notorio».

SUSTITUIR por: **afirmación + precepto + FOLIO**.
- Si está acreditado, decir **cómo** (f. [N]).
- Si es atípico, decir **por qué** (elemento [X] del art. [N] CP).

### 6. Cero postureo

ELIMINAR: «Es de elemental...», «Constituye un brocardo jurídico que...», «Como bien recordó el
insigne jurista...», latinajos ornamentales.

**MANTENER los latinajos que son términos técnicos con significado propio:**
- **in dubio pro reo** — regla de valoración; no hay equivalente breve
- **iter criminis** — arts. 15-16 CP
- **ratio decidendi** / **obiter dictum** — al citar jurisprudencia
- **in malam partem / in bonam partem** — art. 4.1 CP
- **ne bis in idem**, **nulla poena sine lege**

### 7. Voz activa, frases cortas

PREFERIR: «[ACUSADO] entregó el documento el [FECHA] (f. [N])»
EN LUGAR DE: «La entrega del documento por parte del acusado se produjo en fecha [FECHA]»

Frases de 15-25 palabras. Si más, partir. **En la conclusión primera (hechos), aún más cortas.**

### 8. Negrita estratégica

- Encabezados de conclusión o de motivo (`CONCLUSIÓN SEGUNDA`, `MOTIVO PRIMERO`)
- Conceptos que el tribunal debe retener: **engaño bastante**, **dolo antecedente**, **plazo de
  instrucción**, **prueba ilícita**, **presunción de inocencia**
- **Los folios clave** cuando sostienen el argumento central
- NO negritas decorativas

### 9. Conectores procesales típicos

- «Esta parte sostiene que...»
- «De cuanto antecede se desprende...»
- «Por todo ello, y al amparo de los preceptos citados...»
- «Lo dicho hasta aquí basta para acreditar que...»
- «En su virtud...»
- «Sin perjuicio de lo anterior, y con carácter subsidiario...» ← **imprescindible en penal**: las
  pretensiones van escalonadas (atipicidad → tentativa → complicidad → atenuantes)
- «Consta al folio [N] de las actuaciones que...»
- «Con la venia.» (informe oral)

### 10. Cierre del Suplico — fórmula limpia (penal)

> «En su virtud, SUPLICO AL [ÓRGANO] que, teniendo por presentado este escrito, se sirva admitirlo
> y, en su virtud, tenga por [formuladas las conclusiones provisionales de la defensa / interpuesto
> recurso de [tipo] / evacuado el traslado conferido], y, previos los trámites legales, dicte
> [sentencia / resolución] por la que: 1.º [pretensión principal]; 2.º [subsidiaria]; 3.º [costas].»

**Fórmulas de cierre habituales según la posición:**
- Defensa: «...dicte sentencia **absolutoria**, con todos los pronunciamientos favorables y
  **declaración de costas de oficio**.»
- Acusación: «...dicte sentencia **condenatoria** en los términos de las presentes conclusiones, con
  imposición de costas.»

---

## Flujo

### 1. Cargar escrito
Leer el documento generado por la skill aguas arriba.

### 2. Pasada 0 — estructura legal (antes que nada)
- ¿Es un escrito de calificación? → **¿respeta las conclusiones numeradas del art. 650 LECrim?** Si
  no, **eso se corrige antes que el estilo** → `/redactor-escrito-seccion`.
- **¿Hay alguna sección `FUNDAMENTOS DE DERECHO — MASC`? → ELIMINARLA.** El MASC es del orden civil
  y no existe en penal. Se suprime sin sustituto.
- ¿Queda algún resto civil? `DOCUMENTO Nº X` → **`f. [N]`**; `SUPLICO AL JUZGADO DE PRIMERA
  INSTANCIA` → encabezamiento penal; `demandante/demandado` → `[ACUSADO]`/`[VÍCTIMA]`; arts. 1101,
  1124, 1902 CC o LEC → fuera; `burofax` → fuera.
- ¿Aparece el «fiscal instructor»? → **eliminar**: instruye el **Juez de Instrucción**.

### 3. Pasada 1 — delimitar dónde NO se aplica el estilo
Marcar la **conclusión primera (hechos punibles)**: relato objetivo, sin retórica.

### 4. Pasada 2 — estructura
Tripartitas donde haya tres patas. Contrastes donde haya dos figuras próximas.

### 5. Pasada 3 — orden
En cada motivo, ¿está el «por qué» antes del «qué»? Si no, reordenar.

### 6. Pasada 4 — adjetivos
Buscar «absoluta», «manifiesta», «indudable», «rotunda», «palmario», «evidente», «notorio» →
eliminar o sustituir por precepto + folio.

### 7. Pasada 5 — latinajos y postureo
Eliminar el ornamento; conservar el término técnico.

### 8. Pasada 6 — voz activa y frases cortas

### 9. Pasada 7 — negrita
Encabezados, conceptos clave y folios decisivos.

### 10. Pasada 8 — anclaje
**Toda afirmación de hecho lleva folio.** Si no lo lleva, marcarla `[¿folio?]`.

### 11. Output
Escrito con estilo aplicado, mismo formato (`.docx`), + **diff** frente al original.

## Reglas

1. **El estilo no cambia el fondo.** Subsunción, precepto, folio, redacción aplicable (art. 2 CP) —
   todo se preserva.
2. **El estilo no reescribe la estructura legal.** Las conclusiones del art. 650 LECrim se respetan.
3. **⭐ En la conclusión primera (hechos punibles) NO se aplica retórica.** Relato objetivo con
   folio.
4. **No reescribir lo que ya está bien.**
5. **⛔ NO aplicar automáticamente a escritos de trámite ni a comunicaciones con el cliente.** Solo
   cuando se pida expresamente.
   - **Escritos de trámite**: personación, designación de procurador, solicitud de copia de
     actuaciones, señalamiento, aportación de documento, venias. Van **breves y neutros**: la pluma
     de la casa los empeora.
   - **Comunicaciones con el cliente**: correos, notas de estrategia, hojas de encargo, la
     información por escrito del acuerdo de conformidad que **el art. 785.7 in fine LECrim** impone
     facilitar al defendido. Van **en lenguaje llano y comprensible**: la retórica forense es
     contraproducente y, tratándose del deber del art. 785.7, **es exactamente lo contrario de lo
     que la norma persigue**.
6. **Verificar las citas antes de entregar:** cada precepto con `buscar_articulo`; cada ECLI/ROJ con
   `buscar_por_cita` (`jurisprudenciator` — única vía). **⛔ Prohibido inventar** ECLI, ROJ, fechas,
   ponentes o fundamentos, y **prohibido citar jurisprudencia concreta sin verificarla**. Opcional:
   `verificar_escrito` sobre el texto final.
7. **Protección de datos.** `[INVESTIGADO]`, `[ACUSADO]`, `[VÍCTIMA]`, `[TESTIGO]`, `[ÓRGANO]`,
   `[FECHA]`. **Cero datos reales.** Infracciones y condenas = **art. 10 RGPD**. **Cuidado extremo
   con víctimas menores y delitos contra la libertad sexual.** Si en la pasada de estilo aparece un
   dato real, **sustituirlo por el marcador y advertirlo**.

## ⛔ Fuera de esta skill

- **Ejemplos y razonamiento civiles.** Eliminados: cláusula penal (arts. 1152-1153 CC), resolución
  del art. 1124 CC, «unidad de acto entre el cumplimiento y la liberación», «téngase por contestada
  la demanda», «el deudor debe pagar».
- **`FD — MASC`** y **burofax**. Del orden civil.
- **El «fiscal instructor».** Instruye el **Juez de Instrucción**; la reforma está **en tramitación**
  (prevista 1-1-2028).
