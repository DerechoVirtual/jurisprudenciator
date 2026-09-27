---
name: cerrar-asunto
description: Cerrar un asunto contencioso-administrativo. Captura el modo de terminación (sentencia firme, desistimiento, allanamiento, reconocimiento en vía administrativa, acuerdo), costas, ejecución pendiente y lecciones, y archiva fuera de la cartera activa sin borrar. Usar con cerrar asunto o asunto terminado.
---

# Cerrar asunto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Firmeza antes de cerrar** (apelación, preparación de casación y agosto) → `buscar_articulo` (`ley="LJCA"`, artículos 85, 89 y 128).
- **Norma del modo de terminación y régimen de costas** → `buscar_articulo` (`ley="LJCA"`, artículos 74 a 77 y 139).
- **Extensión de efectos antes de archivar un asunto de personal o tributario** → `buscar_articulo` (`ley="LJCA"`, artículos 110 y 111).
- **Lección sobre el «criterio reiterado de un órgano» que viaja al perfil** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"`, `tipo_organo="TSJ"` o el órgano que corresponda, `provincia`) para comprobar que el criterio es de verdad reiterado antes de anotarlo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Cerrar [slug]", "[asunto] está terminado"
- Sentencia firme + plazos de apelación (15 días, art. 85.1) o de preparación de casación (30 días, art. 89.1) agotados
- Auto de terminación por **reconocimiento en vía administrativa** de las pretensiones (art. 76 LJCA)
- Auto de terminación por **acuerdo** homologado (art. 77 LJCA)
- Desistimiento firme (art. 74 LJCA) o allanamiento con sentencia firme (art. 75 LJCA)
- Inadmisión firme (art. 69 LJCA)
- **Sentencia ejecutada en sus propios términos** (art. 103 LJCA) — no antes
- Renuncia o retirada del encargo
- Vía administrativa: el asunto se resolvió favorablemente en alzada o reposición y no hay contencioso

## Flujo

### 1. Verificar pertinencia

- Comprobar `status: open` en `_log.yaml`.
- Si ya está `closed`, avisar y no duplicar.
- Si `next_deadline` está a <14 días, preguntar dos veces.
- **Comprobar firmeza antes que nada.** Un asunto con plazo de apelación o de preparación de casación aún vivo **no se cierra**: `status: stayed`.

### 2. Capturar el modo de terminación

Vía `AskUserQuestion`:

- **Tipo de cierre:**
  - Sentencia firme **estimatoria total** (anulación del acto)
  - Sentencia firme **estimatoria parcial**
  - Sentencia firme **desestimatoria** (acto confirmado)
  - **Inadmisión** firme (art. 69 LJCA) — anotar la causa concreta: extemporaneidad, acto no impugnable, falta de legitimación, falta del acuerdo corporativo del art. 45.2.d), vía previa no agotada
  - **Reconocimiento en vía administrativa** de las pretensiones → auto de terminación y archivo (art. 76 LJCA)
  - **Acuerdo** que pone fin a la controversia, homologado por auto (art. 77 LJCA)
  - **Desistimiento** del recurrente (art. 74 LJCA)
  - **Allanamiento** de la Administración demandada (art. 75 LJCA)
  - **Pérdida sobrevenida de objeto** (revocación del acto, cambio normativo)
  - **Extensión de efectos** de sentencia firme dictada en otro asunto (arts. 110-111 LJCA)
  - Acumulación a otro asunto (apuntar slug receptor)
  - Renuncia / retirada del encargo
  - Resuelto en vía administrativa sin llegar al contencioso
- **Resultado material:** ¿qué le pasa al acto impugnado? (anulado / anulado parcialmente / confirmado / revocado por la propia Administración / sustituido)
- **Cuantía reconocida o sanción anulada / reducida** (si aplica)
- **Costas:** a favor / en contra / sin pronunciamiento / cada parte las suyas
  - Si en contra: comprobar el **tope del art. 139.4 LJCA** — la parte condenada no paga más de **1/3 de la cuantía del proceso** por cada favorecido; cuantía indeterminada = **18.000 €** a estos solos efectos, salvo que el tribunal razone otra cosa por complejidad.
- **Recursos pendientes:** sí (cuál + plazo) / no
- **Ejecución:** cumplida / pendiente / no procede
- **Honorarios cobrados / pendientes**

### 3. Lecciones (opcional)

- Una frase: qué aprendiste del asunto.
- ¿Cambiarías algo de la estrategia con la perspectiva de hoy? (motivo de impugnación que funcionó, cautelar que debió pedirse antes, hueco del expediente que decidió el pleito)
- ¿Hay algo que deba viajar al `CLAUDE.md` del despacho? (p. ej. criterio reiterado de un órgano concreto, práctica de una Administración en la remisión del expediente, tipo de acto que conviene atacar por un motivo determinado)

### 4. Actualizar estado

#### `matters/<slug>/matter.md`

Añadir sección al final:
```
---

## Cierre — [AAAA-MM-DD]

**Modo de terminación:** [tipo + norma: art. 74/75/76/77 LJCA o sentencia firme]
**Suerte del acto impugnado:** [anulado / anulado parcialmente / confirmado / revocado]
**Cuantía reconocida / sanción anulada o reducida:** [€]
**Costas:** [a favor / en contra / sin pronunciamiento] — [tope art. 139.4 aplicable: X €]
**Firmeza:** [fecha en que ganó firmeza + por qué: plazos agotados / auto de terminación]
**Recursos pendientes:** [no / sí: <descripción>]
**Ejecución:** [cumplida / pendiente / no procede]
**Honorarios:** [cobrados / pendientes]

**Lección:** [una frase]
```

#### `matters/<slug>/history.md`

```
[AAAA-MM-DD] CIERRE — [tipo de terminación]. [resumen 1-2 frases]
```

#### `matters/_log.yaml`

- `status: closed`
- `closed: AAAA-MM-DD`
- `outcome: <tipo>`
- `last_updated: hoy`
- Si tiene recurso pendiente: **NO cerrar** — preguntar si crear sub-asunto de apelación o casación y mantener el principal `stayed`.
- Si la ejecución está pendiente: **NO cerrar** — ver § 6.

### 5. Archivar artefactos

NO mover archivos. Quedan donde están en `matters/<slug>/` para histórico.

Si workspaces de asunto y el asunto cerrado era el activo, escribir `Asunto activo: ninguno` en CLAUDE.md.

### 6. Si el resultado implica seguimiento

- **Sentencia estimatoria sin ejecutar:** el asunto **no está terminado**. Las sentencias se ejecutan **en sus propios términos** (art. 103 LJCA) y la Administración no siempre cumple sola. Mantener `stayed` y derivar a `/ejecucion-sentencias-ca`: requerimiento (art. 104), multas coercitivas y responsabilidad personal (art. 112), incidente de ejecución (art. 109).
- **Condena dineraria a la Administración:** seguimiento del pago (art. 106 LJCA) antes de cerrar.
- **Imposibilidad legal o material de ejecutar:** no es un cierre limpio — procede indemnización sustitutoria (art. 105 LJCA). Registrar y no archivar sin resolver.
- **Sentencia firme favorable en personal o tributaria:** valorar **extensión de efectos** a terceros en idéntica situación jurídica (arts. 110-111 LJCA). Es la vía de mayor rendimiento del contencioso: antes de cerrar, preguntar si hay más clientes en la misma situación y ofrecer abrir asuntos derivados.
- **Costas a favor pendientes de tasación:** la tasación se hace conforme a la **LEC** por remisión del art. 139.7 LJCA. Ofrecer seguimiento; contra particulares la exacción va por **vía de apremio** (art. 139.5).
- **Costas en contra:** verificar que la tasación respeta el tope del art. 139.4 antes de dar el asunto por liquidado.
- **Aprendizaje que toca al despacho:** si dijo "esto debería viajar al CLAUDE.md", proponer línea concreta y abrir `/customize`.

### 7. Output

```
✅ Asunto [slug] cerrado.

**Terminación:** [tipo + norma]
**Acto impugnado:** [anulado / confirmado / revocado]
**Cuantía:** [€]
**Costas:** [a favor / en contra] [— tope art. 139.4: X €]
**Firme desde:** [fecha]
**Archivado:** matters/<slug>/ (intacto, retenido en cartera con status=closed)

[Si tiene seguimientos pendientes:]
**Pendiente:** [ejecución / tasación de costas / extensión de efectos / honorarios]
**Sugerido:** [siguiente comando]
```

## Reglas

1. **No borrar.** Cerrar = `status: closed`. Los archivos quedan para histórico.
2. **Recurso pendiente bloquea el cierre.** Solo se cierra lo firme. Comprobar que están agotados los **15 días** de apelación (art. 85.1) y los **30 días** de preparación de casación (art. 89.1) — y recordar que **en agosto esos plazos no corren** (art. 128.2 LJCA), de modo que la firmeza puede ser posterior a lo que parece. En DDFF, agosto sí es hábil.
3. **Sentencia ganada ≠ asunto terminado.** Contra la Administración, el asunto acaba cuando la sentencia **se ejecuta** (art. 103 LJCA), no cuando se dicta. Si hay ejecución pendiente, `stayed`.
4. **Registrar la causa de inadmisión, si la hubo.** Es la información más valiosa que produce un asunto perdido: alimenta el checklist del art. 45.2 en los siguientes intakes.
5. **Antes de cerrar un asunto de personal o tributario ganado**, preguntar por la **extensión de efectos** (arts. 110-111 LJCA).
6. **Honorarios pendientes ≠ asunto abierto.** Puede cerrarse aunque haya cobro pendiente; registrarlo en `outcome`.
7. **Lecciones que viajan al despacho** se escriben a CLAUDE.md, no a la carpeta del asunto cerrado.
8. **No inventar cifras de costas.** El tope del art. 139.4 se calcula sobre la cuantía del proceso que conste en `_log.yaml`; si es indeterminada, 18.000 € **a los solos efectos del tope**.
