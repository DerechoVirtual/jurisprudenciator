---
name: colaboradores-status
description: Genera borradores semanales de emails de estado a colaboradores externos como procurador, perito o abogado colaborador. Usar con estado a colaboradores o emails al procurador esta semana.
---

# Estado a colaboradores externos

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Pregunta concreta al procurador sobre un plazo: precepto que lo fija** → `buscar_articulo` (`ley="LEC"`).
- **Edictos o subastas publicados en el BOE sobre asuntos de la cartera, para preguntar por ellos** → `novedades_boe` (por texto o NIF, hasta 31 días) → `leer_boe`.
- **Contraparte sociedad con cambios que haya que comunicar al procurador (disolución, concurso, nuevo domicilio)** → `buscar_empresa_mercantil`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- Lunes mañana (rutina recomendada)
- "Estado al procurador", "emails de la semana"
- Tras hitos procesales que requieran activar colaboradores

## Flujo

### 1. Leer cartera

`matters/_log.yaml` filtrar `status: open` y agrupar por procurador / perito / abogado colaborador.

### 2. Para cada colaborador

Generar un borrador con TODOS los asuntos donde participa:

```
Para: [procurador@email]
Asunto: Asuntos activos — petición de estado [semana del AAAA-MM-DD]

Estimado/a [Procurador],

Por favor, me confirmes el estado actualizado de los siguientes asuntos:

1. [Slug 1] — [Nombre] — TI Civil [N] Sección [X] de [Provincia]
   - Procedimiento: [tipo + nº]
   - Último plazo conocido: [fecha + acción]
   - Pregunta concreta: [si tiene resolución pendiente / notificación / etc.]

2. [Slug 2] — [Nombre] — [...]
   ..

Especialmente urgente: [los que tengan plazo en <14 días]

Gracias.

[NOMBRE DEL LETRADO]
Colegiado nº [...] [COLEGIO DE ABOGADOS]
```

### 3. Gmail MCP

Si Gmail MCP está autenticado, crear borrador real en Gmail listo para revisar y enviar.

Si no, escribir markdown en `colaboradores-status/[fecha]/[slug-colaborador].md`.

### 4. Resumen general

`colaboradores-status/[fecha]/_summary.md`:

```markdown
# Estado a colaboradores — Semana del [AAAA-MM-DD]

## Procuradores
- [Procurador 1]: N asuntos — borrador generado
- [Procurador 2]: M asuntos — borrador generado

## Peritos
- [Perito 1]: K asuntos — borrador generado

## Abogados colaboradores
- [Colaborador 1]: J asuntos — borrador generado

## Asuntos sin colaborador asignado
[Listar para que el letrado los revise]
```

### 5. Decision tree

> 1. **Revisar y enviar borradores** desde Gmail
> 2. **Personalizar uno concreto** — dime cuál
> 3. **Programar como recurrente cada lunes** — vía scheduled-tasks

## Reglas

1. **NO enviar automáticamente.** Solo borradores. el letrado revisa y dispara.
2. **Una pregunta concreta por asunto** — no "estado en general".
3. **Agrupar por colaborador**, no por asunto. Más eficiente para el colaborador.
4. **Marcar urgencias** explícitamente al principio del email.
