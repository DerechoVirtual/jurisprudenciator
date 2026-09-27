---
name: cronologia
description: Construir o actualizar cronologia del asunto desde fuentes documentales declaradas. Eventos taggeados por significacion segun la tesis. Variantes ofensiva, defensiva, de testigo. Usar con cronologia o timeline del asunto.
---

# Cronología del asunto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Hechos registrales de una sociedad implicada (constitución, nombramientos y ceses, cambios de domicilio)** → `buscar_empresa_mercantil` (últimos actos inscritos) y, para el acto publicado un día concreto, `sumario_borme` → `leer_boe`.
- **Publicaciones oficiales que fechan hechos (edictos, subastas, anuncios de concurso)** → `novedades_boe` (por texto o NIF, hasta 31 días) → `leer_boe`.
- **Sentencias previas entre las partes aportadas como soporte: fecha, órgano y número exactos** → `buscar_por_cita` (ECLI o ROJ).
- **Plazos que dependen de fechas de la cronología (prescripción, caducidad)** → `buscar_articulo`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Cronología", "timeline", "qué pasó cuándo"
- "Saca la cronología de [slug]"
- Antes de redactar demanda u contestación (alimenta el bloque HECHOS)
- Preparación de interrogatorio

## Flujo

### 1. Identificar variante

- **Ofensiva** (por defecto si side=actor): para sostener la demanda — eventos que prueban el incumplimiento de la contraria
- **Defensiva** (por defecto si side=demandado): para sostener la contestación — eventos que neutralizan la pretensión
- **De testigo**: para preparar interrogatorio — solo eventos relevantes al conocimiento del testigo

### 2. Cargar fuentes

- `matters/<slug>/matter.md` (tesis y hechos del intake)
- `matters/<slug>/history.md`
- Uploads del usuario (correos, contratos, facturas, escrituras, sentencias previas)
- Carpeta de documentos del asunto si está configurada

### 3. Extracción de eventos

Para cada documento:
- **Fecha** (la concreta — convertir relativas a absolutas)
- **Tipo de evento** (envío correo / firma contrato / pago / notificación / vista / sentencia / etc.)
- **Actor** (quién hace o recibe)
- **Resumen breve** (1 frase)
- **Documento de soporte** (qué archivo o página lo prueba)
- **Significación según la tesis** (alta/media/baja + nota del por qué)

### 4. Deduplicación

Si dos uploads referencian el mismo evento (ej. correo en su versión enviada y recibida), unificar.

### 5. Ordenación

Cronológica ascendente (puede haber sub-ordenación temporal en hechos del mismo día).

### 6. Tag de significación

Aplicar:
- 🔴 **Crítico** — evento decisivo para la tesis
- 🟠 **Alto** — evento que sostiene punto importante
- 🟡 **Medio** — evento contextual relevante
- 🟢 **Bajo** — contexto, no decisivo

### 7. Output

`matters/<slug>/cronologia.md`:

```markdown
# Cronología — [slug]
**Variante:** [ofensiva / defensiva / testigo de X]
**Última actualización:** [AAAA-MM-DD]

| Fecha | Sig. | Evento | Actor | Soporte |
|---|---|---|---|---|
| AAAA-MM-DD | 🔴 | Firma del contrato | Cliente / Contraparte | Doc Nº 3 (contrato firmado) |
| AAAA-MM-DD | 🟠 | Burofax reclamación | Cliente → Contraparte | Doc Nº 7 (acuse + certificado contenido) |
| AAAA-MM-DD | 🟡 | Reunión telefónica | Cliente y contraparte | Mensaje WhatsApp Cliente (Doc Nº 12) |
| .. | .. | .. | .. | .. |

## Hechos significativos (🔴 + 🟠) en narrativa

[Narrativa fluida que cuenta la "historia" del asunto siguiendo los hechos críticos.
Útil como punto de partida para los HECHOS del escrito.]

## Vacíos detectados

- [Hueco probatorio 1: ej. "no consta acuse de recibo del burofax — pedir copia al cliente"]
- [Hueco 2: ej. "fecha del pago al banco no documentada — solicitar movimiento bancario"]
```

### 8. Decision tree

> **¿Qué hago ahora?**
> 1. **Llevar la narrativa al escrito** — alimenta HECHOS de demanda/contestación
> 2. **Cubrir vacíos probatorios** — pedir al cliente documentos faltantes
> 3. **Cronología de testigo** — para preparar interrogatorio concreto
> 4. **Actualizar tras nuevos documentos** — re-ejecutar

## Reglas

1. **Hechos con fecha y soporte documental.** Sin soporte = nota lateral, no entrada principal.
2. **Tag de significación SUBJETIVO marcado.** Si dudoso, usar `🟡 [revisar]` para que el letrado confirme.
3. **No fabricar.** Si el documento no permite afirmar la fecha exacta, escribir "aprox. mes/año" con flag.
4. **Append-only spirit** — no borrar entradas anteriores al actualizar; añadir nuevas y marcar las que cambien con nota.
