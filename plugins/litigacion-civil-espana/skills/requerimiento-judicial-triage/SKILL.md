---
name: requerimiento-judicial-triage
description: Triage de requerimientos judiciales, exhortos, oficios y diligencias preliminares art 256 LEC. Clasifica, analiza alcance, plazo y oposicion. Usar con hemos recibido requerimiento judicial o exhorto.
---

# Triage de requerimiento judicial

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazos de la tabla (arts. 404, 438, 556, 557, 739 y 815 LEC; arts. 256-263 LEC para diligencias preliminares) en su redacción vigente** → `buscar_articulo` (`ley="LEC"`).
- **Deber de colaboración del tercero (art. 591 LEC) y límite del secreto profesional (art. 542.3 LOPJ)** → `buscar_articulo`.
- **Oposición por secreto profesional: doctrina aplicable** → `buscar_sentencias` (`base="TS"`; `base="TC"` si se invoca el derecho de defensa) + `leer_sentencias` (`parrafos=3`).
- **Requirente o ejecutante sociedad (monitorio de un cesionario de créditos, ejecución de una entidad)** → `buscar_empresa_mercantil`.
- **Notificación por edictos que el cliente no recibió en persona** → `novedades_boe` (por texto o NIF, hasta 31 días) → `leer_boe`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Hemos recibido requerimiento judicial / exhorto / oficio"
- "Diligencias preliminares art. 256 LEC"
- "Auto de admisión de demanda" (preámbulo a contestar)
- "Auto despachando ejecución" frente a nosotros

## Flujo

### 1. Clasificar el documento

Tipos habituales:

| Tipo | Plazo crítico | Acción típica |
|---|---|---|
| Auto admisión demanda + emplazamiento | 20 días contestación (LEC 404/438) | Asunto-intake + redactar-contestacion |
| Petición monitorio + requerimiento | 20 días para pagar/oponerse/silencio (LEC 815) | Asunto-intake o pagar |
| Auto despachando ejecución | 10 días oposición (LEC 556/557) | Asunto-intake + oposición ejecución |
| Auto medidas cautelares adoptadas | 20 días oposición (LEC 739) | Asunto-intake + oposición cautelares |
| Diligencias preliminares art. 256 LEC | 5 días oposición + obligación de cumplir | Triagear contenido + responder |
| Exhorto / oficio (juzgado en otra causa) | Plazo del oficio | Cumplir según contenido |
| Citación judicial a vista | Fecha de la vista | Comparecer o justificar incomparecencia |
| Citación a tomar declaración | Fecha | Asistir o justificar |
| Otros (notificación sentencia, etc.) | Variable | Calcular plazo + acción |

### 2. Extraer datos

- **Tribunal/Órgano** emisor (TI Civil [N] Sección X, AP Sección Y, etc.)
- **Procedimiento** + número
- **Partes** (¿somos parte? ¿somos terceros?)
- **Petición concreta** del tribunal/órgano
- **Fecha del documento + fecha notificación** (cómputo desde notificación)
- **Plazo concedido** (en días — calcular hábiles)
- **Documentos adjuntos**

### 3. Cross-check cartera

Buscar en `_log.yaml`:
- ¿Asunto abierto coincidente?
- ¿Procedimiento ya conocido o nuevo?

### 4. Análisis de respuesta

#### Si somos parte:
- ¿Procede cumplir lo solicitado? (entregar documentación, comparecer, etc.)
- ¿Procede oponernos? Motivos posibles (vulneración secreto profesional, datos protegidos, ámbito excesivo, etc.)
- ¿Procede recurso de reposición? (si la resolución es providencia/auto no definitivo)

#### Si somos terceros (ej. nuestro cliente recibe oficio de embargo de tercero):
- Obligación de cumplir como tercero (LEC 591 — obligación de colaboración)
- Posibles motivos para limitar el ámbito (secreto profesional, secreto bancario, etc.)

### 5. Output

`inbound/<slug>/triage.md`:

```markdown
# Triage — Requerimiento judicial [slug]

**Tipo:** [...]
**Órgano:** [...]
**Procedimiento:** [...]
**Fecha notificación:** [...]
**Plazo concedido:** [...] días (vence [...])

## Petición concreta del tribunal
[...]

## Análisis
- ¿Somos parte? [sí/no]
- ¿Asunto abierto en cartera? [sí: slug / no]
- ¿Procede cumplir? [sí/no/parcial — razón]
- ¿Procede oponerse o recurrir? [sí: motivos / no]

## Plan de actuación
[Pasos concretos con responsable]
```

### 6. Decision tree

> **¿Qué hago ahora?**
> 1. **Abrir asunto** — `/asunto-intake` si no existe
> 2. **Redactar respuesta** — escrito de cumplimiento / oposición
> 3. **Recurso de reposición** — `/recurso-reposicion` si procede
> 4. **Comunicar al cliente** — borrador de email con análisis
> 5. **Vigilancia de plazo** — `/actualizar-asunto` con vencimiento

## Reglas

1. **Plazo desde notificación**, no desde firma del auto.
2. **Plazos hábiles** (LEC 133). Sábados no hábiles. Agosto inhábil salvo medidas urgentes.
3. **Si la notificación llega al procurador**, el plazo arranca ahí — confirmar día.
4. **Secreto profesional como límite** (art. 542.3 LOPJ): si el oficio pide documentación cubierta por secreto, oposición motivada antes de entregar.
