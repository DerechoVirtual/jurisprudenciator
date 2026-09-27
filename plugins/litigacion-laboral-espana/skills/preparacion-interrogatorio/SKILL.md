---
name: preparacion-interrogatorio
description: Outline de interrogatorio de parte (art. 91 LRJS) o testigo (art. 92 LRJS) para el acto del juicio laboral. Preguntas organizadas por la tesis y material de impugnacion. Usar con preparar interrogatorio o guion para el juicio.
---

# Preparación de interrogatorio

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Apercibimientos y reglas del acto** (ficta confessio del art. 91.2, persona jurídica del art. 91.3, circunstancias del testigo del art. 92 LRJS) → `buscar_articulo` (`ley="LRJS"`).
- **Quién debe declarar por la empresa** (administradores y apoderados inscritos, para pedir la citación de quien conoció los hechos) → `buscar_empresa_mercantil`.
- **Preguntas sobre condiciones del convenio** (jornada, horas extra, funciones de la categoría) → `leer_convenio` (`articulo` o `buscar_en`) para confrontar las respuestas con el texto.
- **Valoración de la ficta confessio y del testigo dependiente de la empresa** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Preparar interrogatorio de [nombre]"
- "Guion para el juicio"
- "Preguntas para [testigo / contraparte]"
- Al proponer prueba en la demanda (otrosí) o al preparar el acto del juicio — en lo social **no hay audiencia previa**: conciliación judicial y juicio se celebran en unidad de acto (arts. 82-89 LRJS), y toda la prueba se practica ese día

## Tipos

### Interrogatorio de PARTE (art. 91 LRJS; supletorio LEC 301-316)

- Preguntas orales, sin necesidad de pliego (art. 91.1: se formulan verbalmente, sin admisión previa)
- Pueden ser **asertivas** con respuesta sí/no sobre hechos personales
- Si la parte citada no comparece sin justa causa, o responde con evasivas, cabe tener por ciertos los hechos (ficta confessio, art. 91.2 LRJS)
- Si el interrogado es persona jurídica, debe declarar quien conoció personalmente los hechos (art. 91.3): exigir la citación de la persona concreta (encargado, jefe de RRHH), no del representante formal

### Interrogatorio de TESTIGOS (art. 92 LRJS; supletorio LEC 360-381)

- Preguntas **abiertas** preferentemente (narrativa del testigo)
- Sin sugestión del contenido de la respuesta
- Sólo sobre hechos que conozca por percepción directa
- No hay tacha formal en lo social (art. 92.2 LRJS): las circunstancias personales (parentesco, dependencia de la empresa, interés) se hacen constar y se valoran en sentencia — preguntarlas SIEMPRE al inicio

## Flujo

### 1. Identificar al interrogado

- Nombre + relación con el asunto (parte demandante / demandada / testigo)
- ¿Es nuestro o de la contraria?
- Si nuestro: estamos preparando la pregunta para que conteste a la otra parte (anticipar lo que le preguntarán)
- Si suyo: preparamos las preguntas que QUEREMOS hacerle

### 2. Cargar fuentes

- `matters/<slug>/matter.md` (tesis y hechos)
- `matters/<slug>/cronologia.md` (eventos por fecha)
- `matters/<slug>/cuadro-elementos.md` (qué hay que probar / refutar)
- Documentos donde aparece el interrogado (correos, contratos firmados, etc.)

### 3. Construir cronología del interrogado

Filtrar la cronología solo a eventos donde el interrogado fue actor o testigo directo.

### 4. Definir objetivos del interrogatorio

Tres objetivos posibles, priorizar:
- **Confirmar nuestros hechos** (el interrogado los corrobora)
- **Neutralizar los hechos contrarios** (que admita lo que la contraria no quiere oír)
- **Impugnar credibilidad** (si se contradice con documento del expediente)

### 5. Redactar guion

#### Para PARTE:

```
INTERROGATORIO DE LA PARTE — [Nombre]
Procedimiento: [...]
Variante: contradicción (de la contraria) / corroboración (de la nuestra)
Objetivos: [1, 2, 3]

PREGUNTAS

PRIMERA.- Diga ser cierto que a la fecha del despido el trabajador no tenía sanción
   previa alguna en su expediente.
   [Objetivo: que admita el expediente limpio — desmonta la "reiteración" de la carta]
   [Si niega: confrontar con DOC Nº 6 (certificado de vida laboral en la empresa / ausencia de sanciones)]

SEGUNDA.- Diga ser cierto que la empresa conocía la situación de baja médica del
   trabajador cuando le entregó la carta de despido.
   [Objetivo: que admita el conocimiento — sostiene el indicio de nulidad]
   [Si niega: confrontar con DOC Nº 5 (parte de baja comunicado) y DOC Nº 9 (correo a RRHH)]

TERCERA.- Diga ser cierto que con anterioridad al [fecha] la empresa no abonó las horas
   extraordinarias reclamadas, por importe de [...] €.
   [Objetivo: que admita el impago]
   [Si niega: confrontar con DOC Nº 11 (registro horario art. 34.9 ET) y nóminas]

[Continuar...]

NOTAS DE IMPUGNACIÓN

- Si dice "hubo amonestaciones verbales" → no constan por escrito: DOC Nº 6
- Si dice "no sabíamos de la baja" → DOC Nº 5 y Nº 9 (comunicación a RRHH)
- Si dice "las horas extra se compensaron" → DOC Nº 11 registro horario sin descansos compensatorios
```

#### Para TESTIGO:

```
INTERROGATORIO DE TESTIGO — [Nombre]
Procedimiento: [...]
Relación con las partes: [compañero de trabajo, encargado, delegado de personal, etc.]
Circunstancias a hacer constar (art. 92.2 LRJS): [dependencia de la empresa / parentesco / interés — anticipar]

PREGUNTAS

PRIMERA.- ¿Cuál es su relación con las partes? ¿Sigue trabajando en la empresa?
   [Circunstancia personal — hacer constar para la valoración]

SEGUNDA.- ¿Estuvo usted presente en la reunión del [fecha] en la que el encargado
   comunicó el despido? ¿Qué recuerda de esa reunión?
   [Objetivo: que cuente narración consistente con nuestra tesis]
   [Si su recuerdo difiere: confrontar con correo/mensajes si los hay]

TERCERA.- ¿Qué comentarios escuchó sobre la baja médica de [trabajador] en las semanas
   anteriores al despido? ¿De quién?
   [Objetivo: sostener el indicio de nulidad / represalia]

[Continuar...]

NOTAS
- Si nuestro testigo, ensayar con él (sin sugerirle respuesta, conforme deontología)
- Si contrario (p. ej. encargado aún en plantilla), abrir preguntas para que se extienda y se contradiga; recordar que su dependencia laboral queda constando
- Reservar las "preguntas trampa" para el final
```

### 6. Output

`matters/<slug>/interrogatorios/[nombre].md`:

Contiene el guion completo + notas de impugnación + cronología filtrada.

### 7. Decision tree

> 1. **Si es nuestro testigo: ensayo** — recordar deontología (no sugerirle respuestas, art. 11 EGA)
> 2. **Si es contrario: llevar el guion cerrado al juicio** — en lo social la prueba se admite y practica en el mismo acto (art. 87 LRJS), no hay segunda oportunidad
> 3. **Cuadro de impugnación** — lista compacta de documentos que tener a mano en el juicio

## Reglas

1. **Parte = preguntas asertivas** (sí/no); **testigo = abiertas** (narrativa).
2. **Sólo hechos personales o de conocimiento directo.** Las opiniones jurídicas son del letrado, no del interrogado.
3. **Material de impugnación a la mano** — cualquier respuesta evasiva o contradictoria con documento del expediente debe poder confrontarse en el momento.
4. **Ficta confessio (art. 91.2 LRJS)** — si la parte citada no comparece sin justa causa, o responde con evasivas, pedir expresamente que se tengan por ciertos los hechos. Para poder invocarla, la citación de la parte debe haberse pedido en la demanda (otrosí) con apercibimiento.
5. **Persona jurídica (art. 91.3 LRJS)** — exigir que declare quien conoció personalmente los hechos, no un apoderado sin conocimiento directo.
6. **Circunstancias del testigo (art. 92.2 LRJS)** — no hay tacha formal: hacer constar dependencia, parentesco o interés para la valoración en sentencia.
7. **Deontología (art. 11 EGA, art. 31-36 EGA)** — no instruir al testigo en sentido contrario a la verdad.
