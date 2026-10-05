---
name: conservacion-documental
description: Comunicacion al cliente sobre deber de conservacion documental ante litigio inminente. Equivalente civil español del legal hold. Usar con comunicar al cliente que conserve documentacion.
---

# Conservación documental — Comunicación al cliente

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazos y efectos legales citados en la comunicación** (art. 34.9 ET, arts. 90.3 y 94.2 LRJS, art. 30 del Código de Comercio) → `buscar_articulo` para citarlos en su redacción vigente.
- **Deberes de registro o conservación que imponga el convenio** (registro de jornada, cuadrantes) → `buscar_convenio` + `leer_convenio` (`buscar_en="registro de jornada"`).
- **Jurisprudencia sobre destrucción o pérdida de prueba mencionada en el marco legal** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`); no se cita ninguna STS sin su ECLI verificado con `buscar_por_cita`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

## Cuándo activar

- Tras `/asunto-intake` cuando hay correos / contratos / registros que el cliente debe conservar
- "El cliente puede destruir [documentación]"
- "Necesito que el cliente no borre los correos"
- Litigio inminente y prueba en poder del cliente

## Marco legal

- **Art. 94.2 LRJS** — Si la parte no aporta los documentos requeridos que obran en su poder sin causa justificada, podrán estimarse probadas las alegaciones de la contraria sobre su contenido
- **LEC 217 (supletoria)** — Carga de la prueba; **LEC 328-330** — exhibición de documentos entre partes y por terceros
- **Art. 90.3 LRJS** — Posibilidad de requerir de oficio o a instancia de parte la aportación anticipada de documentos (registros horarios, nóminas, expedientes)
- **STS sobre destrucción de prueba** — la pérdida culposa de prueba en poder de quien debía custodiarla puede llevar a presunción contra él
- **LOPDGDD 3/2018** — la conservación de datos personales debe respetar minimización + plazos legales aplicables
- **Plazos legales de conservación** específicos: mercantil (6 años art. 30 CCo), tributaria (4 años o más), laboral (4 años)

## Subcomandos

### `--emitir` (default)

Generar comunicación al cliente:

```
[Lugar y fecha]

Estimado/a [Cliente],

Como sabe, estamos preparando [el procedimiento / la papeleta de conciliación / la defensa] en el asunto
[referencia interna]. En este contexto, le recuerdo formalmente la importancia de
CONSERVAR Y NO DESTRUIR la siguiente documentación, que puede resultar relevante como
prueba en el procedimiento:

DOCUMENTACIÓN A CONSERVAR

1. [Categoría 1: ej. correos electrónicos con [contraparte] desde [fecha]]
2. [Categoría 2: ej. contratos firmados con [contraparte], incluidos borradores y anexos]
3. [Categoría 3: ej. facturas, albaranes, justificantes de pago]
4. [Categoría 4: ej. comunicaciones internas relativas al asunto]
5. [Etc.]

INSTRUCCIONES CONCRETAS

- NO borre los correos ni vacíe la papelera / archivo
- NO destruya documentos físicos (contratos, facturas)
- Si dispone de copias de seguridad, conserve las que existen al día de hoy
- Si hay empleados con acceso a esta documentación, comuníqueles este deber de
  conservación (puede reenviar este correo)
- Si los sistemas informáticos del cliente borran automáticamente correos pasado
  cierto tiempo, deshabilite ese borrado para las cuentas relevantes
- Conserve también los METADATOS (fechas de envío/recepción, autoría) — no convierta
  los documentos a formatos que los pierdan

DURACIÓN DEL DEBER

Hasta nueva comunicación por mi parte. El procedimiento puede durar varios años y la
documentación puede ser solicitada en distintas fases (conciliación, acto del juicio,
recurso, ejecución).

CONSECUENCIAS DE LA DESTRUCCIÓN

La pérdida culposa o dolosa de documentación relevante por la parte que debió custodiarla
puede llevar al tribunal a presumir hechos en su contra, además de la responsabilidad civil
por daños que cause a esta parte. Es por eso que insisto en cumplir estrictamente esta
recomendación.

Cualquier duda sobre qué conservar o cómo, contácteme antes de tomar decisión.

Atentamente,

[Firma del letrado]
[Despacho]
```

### `--refrescar`

Reenviar la comunicación tras paso del tiempo (ej. tras el señalamiento del juicio, tras la sentencia si hay recurso) para confirmar que sigue vigente el deber.

### `--liberar`

Si el asunto se cierra o si la documentación deja de ser relevante (ej. plazo de prescripción transcurrido), comunicar al cliente:

```
[...] el deber de conservación documental que le comuniqué en [fecha anterior] queda
LIBERADO en cuanto a [tipo de documentación], al haberse [cerrado el asunto / vencido
los plazos / ...]. Puede aplicar a esos documentos sus políticas habituales de
conservación o destrucción, sin perjuicio de los plazos legales generales (mercantil,
tributario, etc.).
```

### `--estado`

Mostrar tabla con asuntos y estado de conservación documental:

| Slug | Fecha emisión | Fecha último refresh | Estado |
|---|---|---|---|
| .. | .. | .. | activo / liberado |

## Flujo

### 1. Identificar categorías de documentación

Se deducen de la documentación y del asunto; pregunta solo lo que bloquee la carta, en una única ronda:
- ¿Qué tipos de documentación son relevantes al asunto?
- ¿En qué soporte? (correo electrónico, papel, sistemas internos)
- ¿Quién tiene acceso? (solo el cliente / sus empleados / terceros)

### 2. Redactar comunicación

Aplicar plantilla anterior con categorías concretas.

**Reparto para la redacción rápida:** carta de una página: sin equipo; la redacta el director en un único archivo de `secciones/`, con las consultas de los artículos lanzadas en paralelo.

### 3. Output

- Word .docx en `matters/<slug>/conservacion-v[N].docx`
- Actualizar `_log.yaml`: `conservacion_documental: emitida-AAAA-MM-DD`
- Apuntar próximo refresh en 90-180 días según duración esperada del asunto

### 4. Recordatorio al cliente

Si Gmail MCP está disponible, crear borrador en Gmail con el texto + el Word adjunto, listo para que el usuario lo envíe al cliente.

## Reglas

1. **No hay obligación legal genérica de "legal hold" en España** análoga a la anglosajona, pero la pérdida culposa de prueba en poder propio tiene consecuencias procesales (art. 94.2 LRJS, presunciones LEC 217 supletoria, valoración probatoria). En lo laboral, además, la empresa tiene deberes autónomos de conservación (registro horario 4 años — art. 34.9 ET; documentación de cotización).
2. **RGPD compatible**: la conservación por motivos litigiosos es base legal del art. 6.1.c o 6.1.f RGPD, pero hay que respetar minimización y purgar tras litigio.
3. **Plazos de conservación legales** (mercantil, tributario, laboral) prevalecen sobre la liberación — apuntarlo en la comunicación.
4. **Metadatos** son críticos para autenticidad — recordar al cliente.
5. **Si la contraparte detecta destrucción**, puede pedir presunciones contra el destructor — comunicar este riesgo al cliente.
