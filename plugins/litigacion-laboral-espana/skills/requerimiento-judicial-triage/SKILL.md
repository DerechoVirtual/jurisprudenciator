---
name: requerimiento-judicial-triage
description: >-
  Triage de notificaciones y requerimientos en el orden social: citaciones a conciliacion y juicio, resoluciones del INSS, requerimientos de subsanacion, autos de ejecucion, oficios y citaciones del SMAC. Clasifica, analiza alcance, plazo y reaccion. Usar con hemos recibido notificacion, citacion o requerimiento.
---

# Triage de requerimiento judicial / notificación

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo de cada tipo de notificación** (arts. 43, 71, 81, 186-188, 194, 197, 220 y 239.4 LRJS) → `buscar_articulo` (`ley="LRJS"`).
- **Identificación de la empresa que cita o demanda al cliente** → `buscar_empresa_mercantil`.
- **Edictos y notificaciones publicadas en el BOE** (cuando un juzgado de lo social no localiza a una parte) → `novedades_boe` (nombre o NIF, periodo de hasta 31 días) → `leer_boe`.
- **Oficio de embargo de salarios a un tercero** → `buscar_articulo` (`ley="LEC"`, `articulo="607"`) y salario mínimo interprofesional del año con `buscar_boe` → `leer_boe`.
- **Requerimiento de la Inspección de Trabajo** (tipificación y cuantía de la posible infracción) → `buscar_articulo` (`ley="LISOS"`).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Hemos recibido una notificación / citación / requerimiento / oficio"
- Citación del SMAC a acto de conciliación (el cliente es la empresa)
- Resolución del INSS/TGSS notificada (denegación de prestación, alta médica, revisión de grado)
- Requerimiento de subsanación de demanda (art. 81 LRJS)
- Auto despachando ejecución frente a nosotros
- Actuación de la Inspección de Trabajo con requerimiento

## Flujo

### 1. Clasificar el documento

Tipos habituales:

| Tipo | Plazo crítico | Acción típica |
|---|---|---|
| Citación del SMAC (cliente = empresa demandada) | Fecha del acto de conciliación | Asunto-intake + preparar postura (avenencia/no) — la papeleta anticipa la futura demanda |
| Admisión de demanda + citación a conciliación y juicio | Fecha del juicio (no hay contestación escrita: oposición oral, art. 85 LRJS) | Asunto-intake + preparar defensa completa y prueba para ese día |
| Requerimiento de subsanación de demanda | 4 días (art. 81.1 LRJS); 15 días si es acreditar conciliación/mediación (art. 81.3) | Subsanar YA — el archivo es la sanción |
| Resolución del INSS/TGSS (denegación, grado, contingencia) | 30 días reclamación previa (art. 71.2 LRJS); 11 días si impugnación de alta médica | `/reclamacion-previa-seguridad-social` |
| Desestimación de reclamación previa (expresa o silencio 45 días) | 30 días para demandar (art. 71.6 LRJS); 20 días en altas médicas | `/incapacidad-permanente` o `/seguridad-social-contingencia` |
| Sentencia notificada | 5 días anuncio suplicación (art. 194 LRJS) | Decidir recurso — `/recurso-suplicacion` |
| Traslado del recurso de la contraria | 5 días impugnación (art. 197 LRJS) | Escrito de impugnación |
| Sentencia del TSJ notificada | 10 días preparación RCUD (art. 220 LRJS) | `/recurso-casacion-unificacion-doctrina` |
| Auto despachando ejecución frente al cliente | 3 días recurso de reposición (arts. 186-187, 239.4 LRJS) | Analizar oposición + reposición |
| Citación a incidente de no readmisión | Fecha de la comparecencia (art. 280 LRJS) | Preparar comparecencia |
| Oficio / exhorto (órgano en otra causa) | Plazo del oficio | Cumplir según contenido |
| Requerimiento de la Inspección de Trabajo | Plazo del requerimiento | Responder / subsanar; valorar impacto en litigios abiertos |
| Citación a interrogatorio de parte | Fecha del juicio | Preparar con `/preparacion-interrogatorio` — ojo al apercibimiento de ficta confessio (art. 91.2 LRJS) |

### 2. Extraer datos

- **Órgano** emisor (Sección de lo Social del TI de [X] / Sala de lo Social del TSJ / SMAC / Dirección Provincial INSS-TGSS / ITSS)
- **Procedimiento** + número (autos, recurso, expediente administrativo)
- **Partes** (¿somos parte? ¿somos terceros?)
- **Petición concreta** del órgano
- **Fecha del documento + fecha de notificación** (cómputo desde notificación)
- **Plazo concedido** (en días — calcular hábiles conforme al art. 43 LRJS, con la lista de modalidades urgentes del 43.4 para agosto y Navidad)
- **Documentos adjuntos**

### 3. Cross-check cartera

Buscar en `_log.yaml`:
- ¿Asunto abierto coincidente?
- ¿Procedimiento ya conocido o nuevo?

### 4. Análisis de respuesta

#### Si somos parte:
- ¿Procede cumplir lo solicitado? (aportar documentación, comparecer, subsanar)
- ¿Procede oponernos? Motivos posibles (secreto profesional, datos de salud de terceros, ámbito excesivo)
- ¿Procede recurso de reposición? (arts. 186-187 LRJS: 3 días contra providencias y autos; 3 días revisión contra decretos del LAJ, art. 188)

#### Si somos terceros (ej. el cliente recibe oficio de embargo de salarios de un empleado):
- Obligación de colaboración (art. 241 LRJS; LEC 591 supletoria)
- Límites de embargabilidad de salarios (LEC 607) — calcular correctamente antes de retener
- Posibles motivos para limitar el ámbito (secreto profesional, datos protegidos)

### 5. Output

`inbound/<slug>/triage.md`:

```markdown
# Triage — Notificación / requerimiento [slug]

**Tipo:** [...]
**Órgano:** [...]
**Procedimiento:** [...]
**Fecha notificación:** [...]
**Plazo concedido:** [...] días hábiles (vence [...])

## Petición concreta del órgano
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
> 2. **Redactar respuesta** — escrito de cumplimiento / subsanación / oposición
> 3. **Recurso** — reposición (3 días) / suplicación (`/recurso-suplicacion`) según la resolución
> 4. **Comunicar al cliente** — borrador de email con análisis
> 5. **Vigilancia de plazo** — `/actualizar-asunto` con vencimiento

## Reglas

1. **Plazo desde notificación**, no desde la fecha de la resolución.
2. **Plazos hábiles** (art. 43 LRJS). Sábados no hábiles. Agosto y 24-dic/6-ene inhábiles SALVO modalidades urgentes del art. 43.4 (despido, extinción, MSCT, vacaciones, tutela DDFF, conflictos colectivos...).
3. **En lo social no hay contestación escrita a la demanda**: si llega una citación a juicio, la fecha del juicio ES el plazo — toda la defensa y la prueba se preparan para ese día.
4. **Secreto profesional como límite** (art. 542.3 LOPJ): si el oficio pide documentación cubierta por secreto, oposición motivada antes de entregar.
