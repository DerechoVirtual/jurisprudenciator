---
name: masc-acta
description: Generar documento de acreditacion del intento MASC art 5 Ley 1/2025. Requisito de admisibilidad de la demanda en juicios no exentos. Usar con preparar MASC o acreditar intento previo.
---

# Acta MASC — Acreditación del intento

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Exenciones, requisitos y eficacia del acuerdo en la LO 1/2025 (art. 5 y siguientes) y, si se usa mediación, la Ley 5/2012** → `buscar_articulo` (`ley="LO 1/2025"` o `ley="Ley 5/2012"` y el `articulo`).
- **Efecto del intento sobre la prescripción (art. 1973 CC y la previsión de la LO 1/2025)** → `buscar_articulo`.
- **Requerido persona jurídica: denominación, CIF y domicilio social inscrito, para que la comunicación llegue a quien debe** → `buscar_empresa_mercantil`.
- **Criterio de los tribunales sobre la suficiencia del intento como requisito de procedibilidad** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="AN"`, `tipo_organo="AP"`, `fecha_desde="03/04/2025"`) + `leer_sentencias` (`parrafos=3`).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- Tras `/asunto-intake` con tipo no exento y `masc_acreditado: no`
- Antes de `/redactar-demanda` cuando el asunto requiere MASC
- "Necesito acreditar MASC", "preparar el intento previo", "documento MASC"

## Exenciones del art. 5 Ley 1/2025

NO requieren MASC:
- Petición inicial del proceso monitorio (LEC 812 y ss)
- Procesos de ejecución (LEC 549 y ss)
- Medidas cautelares previas (LEC 730.2)
- Procesos de jurisdicción voluntaria
- Tutela judicial civil de derechos fundamentales (LEC 249.1.2º)
- Solicitud de alimentos a menores cuando se interesen como medida urgente
- Internamientos no voluntarios por trastorno psíquico

Si el asunto encaja en exención, marcar `masc_acreditado: no-aplica` y NO continuar con este skill.

## Tipos de MASC válidos

1. **Mediación** (Ley 5/2012) — formal, con mediador acreditado, acta de cierre
2. **Conciliación** (LJV) — ante LAJ o notario
3. **Oferta vinculante confidencial** — propuesta de acuerdo con plazo de respuesta
4. **Opinión de experto independiente** — dictamen no vinculante de tercero
5. **Derecho colaborativo** — proceso con abogados colaborativos formados
6. **Negociación directa documentada** — burofax con propuesta + plazo razonable + respuesta o silencio acreditado

## Flujo

### 1. Elegir tipo de MASC

Vía `AskUserQuestion`:

- ¿Hay relación cordial con la contraparte? → mediación / conciliación
- ¿La contraparte es grande / institucional? → oferta vinculante confidencial
- ¿Es asunto técnico? → opinión de experto
- ¿Cuál es el camino más rápido y barato? → negociación documentada por burofax (este es el más habitual)

### 2. Preparar el documento

Según el tipo elegido:

#### A) Negociación directa documentada (burofax)

El burofax DEBE contener:
- Identificación completa de ambas partes (nombre, DNI/NIF, domicilio)
- Identificación del asunto (qué se reclama y por qué)
- Propuesta concreta de solución (cifra, plazo, condiciones)
- Plazo razonable para respuesta (mínimo 30 días recomendable)
- Mención expresa: "El presente burofax constituye intento de MASC conforme al art. 5 de la Ley Orgánica 1/2025 de eficiencia del Servicio Público de Justicia."
- Firma del letrado o del cliente

Derivar a `/burofax-draft` con tipo `masc` para generarlo.

#### B) Mediación formal

- Carta al mediador acreditado contactando con la contraparte
- Si la contraparte se niega: acta de no aceptación
- Si acepta: sesión informativa + en su caso sesión de mediación + acta final (acuerdo o no acuerdo)

#### C) Conciliación

- Acudir a la oficina del LAJ o notario
- Acta levantada por el LAJ / notario

### 3. Documento de acreditación

Crear archivo `matters/<slug>/masc/acta-masc-[fecha].docx` con:

- Tipo de MASC intentado
- Fecha de inicio del intento
- Fecha de cierre (con acuerdo / sin acuerdo / sin respuesta)
- Comunicaciones acreditativas (acuse de Correos, certificado de contenido, acta del mediador, etc.)
- Resultado: acuerdo parcial / sin acuerdo / sin respuesta

### 4. Actualizar log

- `masc_acreditado: si`
- Fecha del intento
- Tipo
- Acuse / documento que lo prueba

### 5. Redacción del documento de acreditación

```
ACREDITACIÓN DE INTENTO PREVIO DE MEDIO ADECUADO DE SOLUCIÓN DE CONTROVERSIAS
(art. 5 LO 1/2025 de eficiencia del Servicio Público de Justicia)

I. PARTES
- Promotor: [cliente, DNI/NIF, domicilio]
- Requerido: [contraparte, datos identificativos]

II. OBJETO DE LA CONTROVERSIA
[Resumen del asunto y pretensión]

III. TIPO DE MASC INTENTADO
[Mediación / conciliación / oferta vinculante / opinión experto / negociación documentada]

IV. CRONOLOGÍA DEL INTENTO
- Fecha inicio: [...]
- [Cronología de actos: envíos, recepciones, respuestas]
- Fecha de cierre: [...]

V. RESULTADO
[Sin acuerdo / acuerdo parcial / contraparte no contestó / contraparte rechazó]

VI. DOCUMENTACIÓN ACREDITATIVA
[Lista de documentos adjuntos: acuse de Correos, certificado de contenido del burofax,
acta del mediador, oferta y respuesta, etc.]

[Lugar y fecha]
[Firma del letrado]
```

## Salida

- Documento Word .docx en `matters/<slug>/masc/`
- Si se ha enviado burofax como MASC, archivo del burofax + acuse de recibo + certificado de contenido también ahí.
- Actualizar `_log.yaml` con `masc_acreditado: si`.
- Mensaje al usuario: "MASC acreditado. Puedes proceder con `/redactar-demanda`. La demanda incluirá automáticamente la acreditación en su Fundamento de Derecho correspondiente."

## Reglas

1. **Plazo razonable mínimo: 30 días** desde envío del burofax hasta presentación de demanda (orientativo; la Ley 1/2025 no fija plazo concreto, pero <30 días es atacable como MASC ficticio).
2. **Certificado de contenido del burofax es OBLIGATORIO** para que el MASC vía burofax sea acreditable. Sin certificado, solo prueba envío, no contenido.
3. **NO falsificar fechas.** Si la contraparte respondió, archivar respuesta literal. Si no respondió, esperar el plazo razonable antes de demandar.
4. **El MASC NO interrumpe la prescripción salvo que la ley lo prevea**. Verificar art. 1973 CC y especialmente la previsión expresa del MASC en Ley 1/2025 — calcular bien plazos.
5. **Acta MASC con acuerdo puede tener fuerza ejecutiva** si está elevada a escritura pública o homologada judicialmente (art. 6 Ley 1/2025).
