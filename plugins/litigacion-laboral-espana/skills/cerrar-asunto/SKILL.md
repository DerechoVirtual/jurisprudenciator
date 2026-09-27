---
name: cerrar-asunto
description: Cerrar asunto. Captura outcome, lecciones aprendidas y archiva fuera de la cartera activa sin borrar. Usar con cerrar asunto o asunto terminado.
---

# Cerrar asunto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Confirmar que no queda recurso abierto antes de cerrar** → `buscar_articulo` (`ley="LRJS"`, `articulo="194"` para la suplicación, `"220"` para el RCUD).
- **Seguimiento por insolvencia: situación de la empresa y FOGASA** → `buscar_empresa_mercantil`, `novedades_boe` (edictos concursales) y `buscar_articulo` (`ley="ET"`, `articulo="33"`).
- **Plazo para instar la ejecución o el incidente de no readmisión** → `buscar_articulo` (`ley="LRJS"`, `articulo="243"` y `"279"`).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Cerrar [slug]", "[asunto] está terminado"
- Sentencia firme + plazo de suplicación/RCUD agotado
- Avenencia en conciliación (SMAC o judicial) cumplida y cobrada
- Desistimiento firme
- Ejecución completada (cobro íntegro o insolvencia con FOGASA tramitado)
- Carencia de objeto sobrevenida

## Flujo

### 1. Verificar pertinencia

- Comprobar `status: open` en `_log.yaml`.
- Si ya está `closed`, avisar y no duplicar.
- Si `next_deadline` está a <14 días, preguntar dos veces.

### 2. Capturar outcome

Vía `AskUserQuestion`:

- **Tipo de cierre:**
  - Sentencia firme estimatoria total
  - Sentencia firme estimatoria parcial
  - Sentencia firme desestimatoria
  - Avenencia en conciliación SMAC (título ejecutivo, art. 68 LRJS)
  - Conciliación judicial / transacción homologada
  - Desistimiento del actor (o incomparecencia al juicio, art. 83.2 LRJS)
  - Allanamiento del demandado
  - Acumulación a otro asunto (apuntar slug receptor)
  - Renuncia / retirada del encargo
- **Cuantía finalmente recuperada / pagada** (si aplica; anotar si intervino FOGASA)
- **Costas:** solo en recursos (art. 235 LRJS) — a favor / en contra / sin pronunciamiento / no aplica (instancia)
- **Recursos pendientes:** sí (cuál) / no
- **Honorarios cobrados / pendientes**

### 3. Lecciones (opcional)

- Una frase: qué aprendiste del asunto
- ¿Cambiarías algo de la estrategia con la perspectiva de hoy?
- ¿Hay algo de este asunto que deba viajar al `CLAUDE.md` del despacho? (ej. "este tipo de cláusula se resuelve mejor con esta tesis")

### 4. Actualizar estado

#### `matters/<slug>/matter.md`

Añadir sección al final:
```
---

## Cierre — [AAAA-MM-DD]

**Outcome:** [tipo]
**Cuantía recuperada/pagada:** [€]
**Costas:** [a favor / en contra / sin pronunciamiento]
**Recursos pendientes:** [no / sí: <descripción>]
**Honorarios:** [cobrados / pendientes]

**Lección:** [una frase]
```

#### `matters/<slug>/history.md`

```
[AAAA-MM-DD] CIERRE — [tipo de cierre]. [resumen 1-2 frases]
```

#### `matters/_log.yaml`

- `status: closed`
- `closed: AAAA-MM-DD`
- `outcome: <tipo>`
- `last_updated: hoy`
- Si tiene recurso pendiente: NO cerrar — preguntar si crear sub-asunto de suplicación/RCUD y mantener el principal `stayed`.

### 5. Archivar artefactos

NO mover archivos. Quedan donde están en `matters/<slug>/` para histórico.

Si workspaces de asunto y el asunto cerrado era el activo, escribir `Asunto activo: ninguno` en CLAUDE.md.

### 6. Si el outcome implica seguimiento

- **Cobro pendiente tras sentencia firme o avenencia incumplida:** ofrecer `/ejecucion-laboral` (la avenencia SMAC y la conciliación judicial son títulos ejecutivos).
- **Readmisión incumplida tras sentencia de nulidad/improcedencia con opción readmisión:** ofrecer `/ejecucion-laboral` (incidente de no readmisión, arts. 279-281 LRJS — plazos: 20 días / 3 meses).
- **Insolvencia de la empresa:** recordar la solicitud de prestaciones al FOGASA (art. 33 ET).
- **Honorarios pendientes:** reclamarlos con el modelo del despacho (jura de cuentas LEC 34-35 o reclamación ordinaria).
- **Aprendizaje que toca al despacho:** si dijo "esto debería viajar al CLAUDE.md", proponer línea concreta a añadir y abrir `/customize`.

### 7. Output

```
✅ Asunto [slug] cerrado.

**Outcome:** [tipo]
**Cuantía:** [€]
**Costas:** [a favor / en contra]
**Archivado:** matters/<slug>/ (intacto, retenido en cartera con status=closed)

[Si tiene seguimientos pendientes:]
**Pendiente:** [tasación de costas / ejecución / honorarios]
**Sugerido:** [siguiente comando]
```

## Reglas

1. **No borrar.** Cerrar = `status: closed`. Los archivos quedan para histórico.
2. **Recurso pendiente bloquea cierre.** El asunto solo se cierra cuando es firme. Si hay suplicación o RCUD vivos, mantener `status: stayed` o abrir sub-asunto.
3. **Honorarios pendientes ≠ asunto abierto.** El asunto puede cerrarse aunque haya cobro pendiente; registrarlo en `outcome`.
4. **Lecciones que viajan al despacho** se escriben a CLAUDE.md, no a la carpeta del asunto cerrado.
