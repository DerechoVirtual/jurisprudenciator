---
name: subsuncion-juridica
description: Pulido y revision de escritos contencioso-administrativos para conectar norma y jurisprudencia con los hechos del expediente. Silogismo sobre LJCA/LPAC/LRJSP y normativa sectorial. Jurisprudencia SIEMPRE con el conector MCP jurisprudenciator. Usar con pulir escrito o conectar jurisprudencia.
---

# Subsunción jurídica — pulido del escrito contencioso

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Premisa mayor vigente** → `buscar_articulo` (LJCA, LPAC —letra exacta del art. 47.1 y filtro del art. 48.2—, LRJSP y norma sectorial estatal).
- **Ordenanza municipal** → `buscar_ordenanzas` + `leer_ordenanza` con `articulo`; si el municipio no está cubierto, se pide al usuario.
- **Cada cita del escrito** → `buscar_por_cita` (ECLI, ROJ o la cita abreviada de una STC o de un asunto del TJUE) +`leer_sentencias` (`parrafos=3`, `terminos`) para extraer la doctrina concreta que se subsume.
- **Sustituir citas sueltas o de la Sala Primera** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`; `base="TS"`, o `base="AN"` con `tipo_organo="TSJ"` y `provincia` de la CCAA competente).
- **TC y TJUE** → `buscar_sentencias` con `base="TC"` o `base="TJUE"`.
- **Pasada final** → `verificar_escrito` sobre el escrito pulido.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- AUTOMÁTICAMENTE tras `redactar-demanda`, `redactar-contestacion`, `recurso-apelacion`, etc.
- Petición explícita: "pulir escrito", "conectar jurisprudencia con hechos"
- Cuando una primera versión cita sentencias pero no las aterriza en el expediente

## El silogismo contencioso: qué cambia respecto del civil

La premisa mayor **no** es el CC ni la LEC. Es:

- **LJCA** (Ley 29/1998) — jurisdicción, admisibilidad, pretensiones (art. 31), proceso, prueba
- **LPAC** (Ley 39/2015) — procedimiento, nulidad (art. 47.1), anulabilidad (art. 48), plazos de
  la vía administrativa, responsabilidad patrimonial (plazo, art. 67)
- **LRJSP** (Ley 40/2015) — responsabilidad patrimonial (arts. 32-37), potestad sancionadora
- **Normativa sectorial** — estatal, **autonómica** y **local** (ordenanzas)
- **LEC** — solo **supletoriamente** (DF 1.ª LJCA), y diciendo que lo es

La premisa menor **no** es "el contrato" ni "los documentos": es **el expediente administrativo**,
con su folio. Y la conclusión no es "condene a pagar": son las pretensiones del **art. 31 LJCA**
(declaración de disconformidad a Derecho y anulación; y, en su caso, reconocimiento de situación
jurídica individualizada e indemnización).

> ⚠️ **Contaminación civil a cazar en la pasada.** Si en el escrito aparece un artículo del **CC**
> (1101, 1124, 1902...) o de la **LEC** invocado como premisa mayor, o una referencia al **MASC**,
> es contaminación de plantilla: **eliminarla**. La LEC solo entra por remisión supletoria expresa
> (DF 1.ª LJCA) y debe presentarse como supletoria. El MASC es del orden civil y **no existe** en
> contencioso: el equivalente es el agotamiento de la vía administrativa (art. 25.1 LJCA).

## 🚫 Normativa autonómica: pedirla, nunca citarla de memoria

**Este es el riesgo de invención más alto de la skill.** Buena parte del Derecho administrativo
material es **autonómico y local**: urbanismo, actividades, comercio, sanidad, función pública
autonómica, tributos locales.

- El conector `jurisprudenciator` cubre: **BOE (Derecho estatal)**, **jurisprudencia**, **doctrina
  DGT** y **ordenanzas municipales** de los municipios cubiertos (`buscar_ordenanzas`,
  `leer_ordenanza`).
- **NO cubre** los boletines **autonómicos** ni los **BOP** no cubiertos.
- Por tanto: toda norma autonómica se **pide al usuario**. Si no se aporta, **marcar
  `[PEDIR AL USUARIO — norma autonómica no verificable]` y no redactar la subsunción**.
- **Nunca** inventar número, fecha, rúbrica o contenido de una ley autonómica, un decreto
  autonómico o un plan urbanístico. Un artículo autonómico citado de memoria es una cita falsa con
  apariencia de veracidad: el peor error posible.
- Ordenanzas municipales: intentar primero `buscar_ordenanzas` / `leer_ordenanza`. Si el municipio
  no está cubierto, pedirla.

## Patrón a corregir (citas "sueltas")

❌ MAL:

> "...la jurisprudencia del Tribunal Supremo en STS [ECLI] establece que el defecto de forma
> determina la anulabilidad del acto. En el presente caso, la Administración incurrió en defecto
> de forma..."

✅ BIEN (subsuntivo):

> "...el artículo 48.2 LPAC no anuda la anulabilidad a **todo** defecto de forma, sino únicamente a
> aquel que prive al acto de los requisitos formales indispensables para alcanzar su fin **o dé
> lugar a la indefensión de los interesados**. La STS [ECLI — verificado con `buscar_por_cita`]
> precisa que la indefensión relevante es material y no meramente formal.
>
> Aplicado al caso, el defecto no es ritual: esta parte propuso en su escrito de alegaciones
> (**EA folio 14-19**) la práctica de [prueba], dirigida precisamente a acreditar [elemento del
> tipo]. La propuesta de resolución (**EA folio 22**) **no se pronuncia** sobre esa proposición —
> ni la admite ni la rechaza motivadamente — y la resolución sancionadora (**EA folio 27-31**) tiene
> por acreditado ese mismo elemento sin soporte probatorio alguno en los folios 1 a 33 del
> expediente. La omisión privó a [CLIENTE] del único medio con que contaba para discutir el hecho
> sobre el que se asienta la sanción: la indefensión es material y determinante, y concurre el
> supuesto del artículo 48.2 LPAC."

Lo que hace bueno al segundo pasaje: **la norma se lee con su filtro** (el 48.2 no dice lo que la
cita suelta le hacía decir), **el hecho se ancla al folio**, y **la conclusión es la del art. 31
LJCA**, no una condena civil.

## Flujo

### 1. Leer escrito

Cargar el documento generado por la skill aguas arriba.

### 2. Pasada de descontaminación civil

Antes de subsumir, limpiar:
- Artículos del **CC** o de la **LEC** como premisa mayor → eliminar o reencuadrar como supletorio
  expreso (DF 1.ª LJCA)
- Referencias a **MASC**, burofax como requisito, "acto de conciliación" → eliminar
- "Doc. nº X" como anclaje único de un hecho del expediente → sustituir por **EA folio [N]**
- Suplico con pretensiones civiles (resolución contractual, condena a pagar sin más) →
  reencuadrar en el **art. 31 LJCA**
- Órgano mal nombrado ("Juzgado de Primera Instancia") → corregir

### 3. Verificar la premisa mayor

Para cada precepto citado:
- **`buscar_articulo`** — comprobar el texto **vigente** antes de darlo por bueno. La LJCA se ha
  modificado tres veces entre 2023 y 2025 (RD-ley 5/2023, RD-ley 6/2023, LO 1/2025 — ver
  `references/anclas-normativas-ca.md` § 1)
- Plazos y umbrales: **solo** desde las anclas o verificados en el momento. Nunca de memoria
- **Nulidad:** ¿se cita la **letra concreta** del art. 47.1 LPAC? "Art. 47 LPAC" a secas es una
  cita inútil: la lista es tasada y hay que decir en cuál se encaja. Verificar la letra
- **Anulabilidad:** ¿se ha superado el filtro del art. 48.2 (requisitos formales indispensables o
  indefensión)? Un defecto de forma sin ese puente no anula
- Normativa autonómica → `[PEDIR AL USUARIO]`

### 4. Localizar citas jurisprudenciales

Identificar cada STS / SAN / STSJ / TJUE / TC citado. Para cada una:
- **Verificar con `buscar_por_cita`.** Si no se verifica, **fuera** o `[VERIFICAR]`
- ¿Es de la **Sala Tercera**? Una STS de la Sala Primera (civil) invocada en un pleito contencioso
  es señal de contaminación de plantilla: revisar si aporta algo o es residuo
- ¿Es de un **TSJ de otra CCAA**? Puede ser útil, pero decir de dónde es y no venderla como
  doctrina consolidada

### 5. Para cada cita, comprobar la subsunción

- ¿Hay **hechos del expediente** citados expresamente, con folio?
- ¿La cita lleva al "aplicado al caso concreto..."?
- ¿Se nombra el **EA folio [N]** que sostiene la conexión?
- ¿La conclusión aterriza en una pretensión del **art. 31 LJCA**?

### 6. Si la cita está "suelta"

Reescribir añadiendo:
- **La doctrina concreta** que sienta la sentencia (no "la jurisprudencia mayoritaria entiende...")
- **La subsunción al expediente** — hecho concreto + folio
- **La conclusión jurídica derivada** — qué debe declarar el tribunal, en términos del art. 31 LJCA

### 7. Eliminar redundancia

Si dos sentencias dicen lo mismo, citar la más reciente y la unificadora. En este orden, preferir
**TS Sala Tercera** sobre TSJ para la doctrina general, y **TSJ de la CCAA competente** cuando la
cuestión sea de Derecho autonómico.

### 8. Output

Escrito pulido + diff frente al original, marcando los cambios y, separadamente, la **lista de
contaminación civil eliminada** y la **lista de normas autonómicas pendientes de aportar**.

## Reglas

1. **La premisa mayor es LJCA / LPAC / LRJSP + sectorial.** Si es CC o LEC sin decir que es
   supletoria (DF 1.ª LJCA), es contaminación: fuera.
2. **La premisa menor es el expediente, con folio.** `EA folio [N]` es la cuerda entre hecho y
   norma. Si la frase no cita el folio, no está subsumiendo.
3. **La conclusión es del art. 31 LJCA.** Anulación y, en su caso, reconocimiento de situación
   jurídica individualizada + indemnización. No condenas civiles.
4. **Normativa autonómica: pedirla, jamás citarla de memoria.** El conector no la cubre. Marcar
   `[PEDIR AL USUARIO — norma autonómica no verificable]` y no redactar sobre ella.
5. **Jurisprudencia que no conecta es jurisprudencia perdida.** Si una cita no aterriza en el
   expediente, fuera.
6. **Cada cita = un punto subsuntivo concreto.** No "como la jurisprudencia mayoritaria
   entiende..." sino "la STS [ECLI verificado] establece [doctrina concreta]; aplicado al caso,
   [hecho concreto + EA folio N]...".
7. **Verificar SIEMPRE.** Preceptos con `buscar_articulo`; ECLI/ROJ con `buscar_por_cita`. Nada de
   memoria: ni artículos, ni plazos, ni cifras, ni ponentes, ni fechas.
8. **NO inventar.** Si no se puede aterrizar la cita con el expediente existente, marcar
   `[REVISAR: jurisprudencia citada no aterrizada — eliminar o sustituir]`. Si no se puede
   verificar una cita, `[VERIFICAR]` y decirlo abiertamente al usuario.
9. **Nulidad con letra concreta.** Art. 47.1 LPAC citado sin letra es cita incompleta. Y la nulidad
   es de interpretación restrictiva: lo ordinario es la anulabilidad del art. 48.
10. **Protección de datos.** `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`. ⚠️ Al subsumir sobre
    el expediente se manejan datos de **terceros** (denunciantes, otros interesados) y de **salud**
    (art. 9 RGPD, categoría especial) — especialmente en responsabilidad patrimonial sanitaria,
    donde la subsunción sobre la lex artis descansa en la historia clínica. **Referenciar el folio,
    no reproducir el dato.** Si el escrito original reproduce datos de terceros, señalarlo como
    corrección en el diff.
