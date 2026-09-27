---
name: estilo-escritos-judiciales
description: Capa de estilo que aplica la pluma de la casa en cualquier escrito judicial. Estructura tripartita, contrastes, explicacion del por que antes del que, cero adjetivos vacios. Usar con aplica mi estilo o pluma de la casa.
---

# Pluma de la casa — estilo redaccional

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Citas legales del escrito antes de la entrega final** → `verificar_escrito` con el texto completo.
- **ECLI o ROJ citados** → `buscar_por_cita` como último paso (regla 4).
- **Citas literales que el pulido reformula o acorta** → recotejar el tenor con `buscar_articulo` (preceptos) o `leer_sentencias` (`parrafos=3`, párrafos de sentencias): el estilo no cambia el texto entrecomillado.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Perfil del abogado y estilo de la casa.** Si existe el perfil de estilo del despacho, manda sobre lo que describe esta skill en fórmulas, estructura, tono, forma de citar y maquetación; el estilo de la casa se aplica solo en lo que el perfil no diga.

> Nota: estos patrones son el estándar de buena redacción judicial de la casa. Calibrar con escritos reales del despacho cuando se disponga de muestras.

## Cuándo activar

- AUTOMÁTICAMENTE tras cualquier skill de redacción (`redactar-demanda-despido`, `reclamacion-cantidad`, `extincion-contrato-trabajador`, `recurso-suplicacion`, `recurso-casacion-unificacion-doctrina`, etc.)
- "Aplica mi estilo", "pásalo por mi pluma", "voz de la casa"
- Antes de la verificación ECLI y entrega final

## Patrones a inyectar

### 1. Estructura tripartita

Cuando el argumento tiene tres patas, presentarlas con paralelismo:

> "Tres son las razones que sostienen esta pretensión: PRIMERO, [...]; SEGUNDO, [...]; TERCERO, [...]"

> "El precepto exige tres requisitos copulativos: (a) que [...], (b) que [...], y (c) que [...]"

### 2. Contrastes "una cosa es X, otra cosa es Y"

Frase que separa supuestos cercanos pero distintos jurídicamente:

> "Una cosa es que la empresa atraviese dificultades transitorias de tesorería, y otra muy distinta es que pretenda valerse de ellas para incumplir de forma persistente la obligación salarial (art. 50.1.b ET)."

> "Una cosa es el ejercicio regular del poder de dirección (art. 20 ET), y otra la modificación sustancial de condiciones que menoscaba la dignidad del trabajador (art. 50.1.a ET)."

### 3. Explicación del por qué antes del qué

Antes de afirmar la conclusión jurídica, exponer la razón que la sostiene:

> "Por cuanto la carta de despido delimita los hechos enjuiciables (art. 105.2 LRJS) y dado que en el caso de autos la carta se limita a imputaciones genéricas sin fecha ni circunstancia alguna, debe concluirse que el despido no puede ser declarado procedente."

(NO: "El despido es improcedente. La carta es genérica.")

### 4. Cierre estratégico

Cada fundamento de derecho cierra con frase de tránsito hacia el siguiente o hacia el suplico:

> "En consecuencia, concurre el incumplimiento grave del art. 50.1.b) ET, lo que habilita a esta parte para instar la extinción indemnizada del contrato con los efectos del despido improcedente, como se solicita en el suplico."

### 5. Cero adjetivos vacíos

ELIMINAR:
- "absolutamente claro"
- "manifiestamente improcedente"
- "indubitadamente acreditado"
- "rotundamente probado"
- "evidente"

SUSTITUIR por:
- afirmación + cita + documento concreto
- Si está acreditado, decir cómo (con doc Nº X)
- Si es improcedente, decir por qué (con artículo Y)

### 6. Cero postureo

ELIMINAR:
- "Es de elemental que..."
- "Constituye un brocardo jurídico que..."
- "Como bien recordó el insigne jurista..."
- Latinajos no necesarios ("ad limine litis", "ex officio", "per se" — usar solo si añaden precisión)

MANTENER latinajos útiles:
- "in dubio pro operario" (laboral)
- "iura novit curia" (procesal)
- "ratio decidendi" (jurisprudencial)
- Locuciones jurídicas comprensibles para letrados

### 7. Voz activa, frases cortas

PREFERIR:
- "La contraparte incumplió el [fecha]" (activa, 5 palabras)
- en lugar de "El incumplimiento por parte de la contraparte se produjo el [fecha]" (pasiva, 12 palabras)

Frases de 15-25 palabras máximo. Si más, partir.

### 8. Negrita estratégica

- Encabezados de fundamento (FUNDAMENTO DE DERECHO PRIMERO)
- Conceptos clave que el tribunal debe retener (`cláusula esencial`, `plazo de prescripción`, `documento de mayor valor probatorio`)
- NO negritas decorativas que rompen el flujo

### 9. Conectores procesales típicos del despacho

Listado para reciclar:
- "Esta parte sostiene que..."
- "De cuanto antecede se desprende..."
- "Por todo ello, y al amparo de los preceptos citados..."
- "Lo dicho hasta aquí basta para acreditar que..."
- "En su virtud..."
- "Por lo demás, conviene precisar que..."

### 10. Cierre del Suplico — fórmula limpia

Fórmula recurrente:

> "En su virtud, SUPLICO al [Juzgado de lo Social / Sección de lo Social del Tribunal de
> Instancia / Sala de lo Social] que, teniendo por presentado este escrito junto con los
> documentos acompañados, lo admita, [me tenga por personado y parte / téngase por
> interpuesto el recurso], señale día y hora para los actos de conciliación y juicio, y,
> en su día, previos los trámites legales, dicte sentencia/resolución por la que: 1.º..
> 2.º.. [3.º Costas solo si es recurso — art. 235 LRJS; en la instancia social no hay
> condena en costas ordinaria]."

## Flujo

### 1. Cargar escrito

Leer el .docx generado por skill aguas arriba.

### 2. Pasada 1: estructura

- ¿Hay tres argumentos? Aplicar estructura tripartita
- ¿Hay matiz entre dos supuestos? Aplicar "una cosa es X, otra es Y"

### 3. Pasada 2: orden

- En cada FUNDAMENTO, ¿está el "por qué" antes del "qué"?
- Si no, reordenar

### 4. Pasada 3: limpiar adjetivos

- Buscar "absoluta", "manifiesta", "indudable", "rotunda" y eliminar o sustituir

### 5. Pasada 4: latinajos y postureo

- Eliminar latinajos no esenciales
- Eliminar postureo retórico

### 6. Pasada 5: voz activa y frases cortas

- Convertir pasivas en activas
- Partir frases >25 palabras

### 7. Pasada 6: negrita

- Reservar negrita para encabezados y conceptos clave

### 8. Output

Escrito con estilo aplicado, en el mismo formato (.docx). Generar diff frente al original mostrando los cambios.

## Reglas

1. **El estilo no cambia el fondo.** Subsunción jurídica, cita, pin-cite — todo se preserva.
2. **No reescribir lo que ya esté bien.** Si una sección ya cumple los patrones, no tocar.
3. **No aplicar a escritos no judiciales** (papeletas de conciliación, reclamaciones previas, emails) automáticamente; solo cuando se pida explícitamente.
4. **Verifica los ECLI/ROJ con `jurisprudenciator`** (`buscar_por_cita`) como último paso antes de entregar.
