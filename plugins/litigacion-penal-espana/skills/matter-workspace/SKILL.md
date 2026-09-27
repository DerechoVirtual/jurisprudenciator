---
name: matter-workspace
description: Gestionar workspaces de asunto penal. Crear, listar, cambiar, cerrar o desligar el asunto activo, mostrando fase, posicion, situacion personal y el plazo de instruccion del art. 324 LECrim. Usar con cambiar asunto, listar mis asuntos o asunto activo.
---

# Gestión de workspaces de asunto — penal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo de instrucción que muestra `status`** → `buscar_articulo` (`ley="LECrim"`, `articulo="324"`) si el vencimiento no está verificado en el asunto.
- **Plazos máximos de prisión provisional** (situación personal) → `buscar_articulo` (`ley="LECrim"`, `articulo="504"`).
- **ECLI anotados en un asunto que se reutilizan en otro** → `buscar_por_cita`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- "Nuevo asunto" → derivar a `/asunto-intake`
- "Listar mis asuntos" / "qué tengo abierto" → `list`
- "Cambiar a asunto X" / "trabaja en X" → `switch`
- "Cerrar asunto X" → derivar a `/cerrar-asunto`
- "Trabaja a nivel despacho" / "sin asunto activo" → `detach`
- Cuando un skill necesita saber qué asunto está activo

## Ubicación

- Configuración y asunto activo:
  `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md`
- Cartera:
  `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/matters/_log.yaml`
- Carpeta de cada asunto:
  `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/matters/<slug>/`

> ⚠️ **Directorio propio del plugin penal.** No compartir carpeta con el plugin de litigación civil:
> mezclar las dos carteras es una brecha de datos, porque en penal el mero listado de asuntos revela
> quién está investigado (**art. 10 RGPD**).

## Subcomandos

### `list`

Leer `matters/_log.yaml`. Mostrar tabla compacta:

| Slug | Delitos | Posición | Fase | Órgano | Sit. personal | Riesgo | Instrucción vence | Próximo plazo |
|---|---|---|---|---|---|---|---|---|
| .. | .. | .. | .. | .. | .. | .. | .. | .. |

- La columna **"Instrucción vence"** muestra `fecha_vencimiento_instruccion` y los días restantes;
  si `art_324_3_alerta: sí`, marcarla ⚠️. Si el asunto no está en instrucción, "—".
- **Sin nombres.** La tabla se construye desde `_log.yaml`, que no los tiene. El slug identifica el
  asunto; el cliente, solo en `matter.md`.

Filtros opcionales:
- `--active` (default): solo `status: open`
- `--all`: incluir cerrados
- `--closed`: solo cerrados
- `--risk-high`: solo riesgo alto/crítico
- `--instruccion`: solo con instrucción viva, ordenados por días restantes del art. 324
- `--presos`: solo `situacion_personal: prision-provisional`
- `--posicion <valor>`: defensa / acusacion-particular / acusacion-popular / actor-civil /
  responsable-civil-subsidiario

### `switch <slug>`

1. Verificar que el slug existe en `_log.yaml`.
2. Si existe, escribir `## Workspaces de asuntos` → `Asunto activo: <slug>` en el CLAUDE.md de
   configuración.
3. Confirmar con la ficha corta:
   > ✅ Asunto activo: `<slug>` (`<nombre>`).
   > Posición: `<posicion>` · Fase: `<fase>` · Procedimiento: `<procedimiento>` · Órgano: `<organo>`
   > Situación personal: `<situacion_personal>` · Riesgo: `<risk>`
   > ⚠️ Instrucción (art. 324): vence `<fecha>` — restan `<N>` días · prórrogas: `<N>` · 324.3: ✅/⚠️
   > Próximo plazo: `<next_deadline>` — `<next_deadline_concepto>`
4. Si no existe, mostrar fuzzy match con los más cercanos y preguntar. **Nunca** buscar por nombre de
   cliente: los slugs no lo llevan.

### `new <nombre>`

Derivar a `/asunto-intake` con `<nombre>` como sugerencia. Recordar que el slug se construye como
`descriptor-delito-año` y **nunca** con el nombre del cliente.

### `close <slug>`

Derivar a `/cerrar-asunto`. Recordar: **sentencia firme ≠ asunto cerrado** — si queda **ejecutoria**
viva (liquidación de condena, suspensión del art. 80 CP con su plazo, responsabilidad civil), el
asunto permanece `open` con `fase: ejecucion`.

### `detach`

Escribir `Asunto activo: ninguno` en el CLAUDE.md de configuración. Los skills trabajarán a nivel
despacho (contexto general, sin carpeta de asunto).

### `status`

Mostrar:
- Asunto activo (o "ninguno — trabajo a nivel despacho")
- Posición, fase, procedimiento y órgano
- Situación personal y medidas cautelares
- **Plazo de instrucción (art. 324):** vencimiento, días restantes, nº de prórrogas y estado del
  324.3
- Prescripción del delito (art. 131 CP): fecha estimada
- Cross-matter context (`on` / `off`)
- Carpeta del asunto activo: `matters/<slug>/`
- Última actualización
- Próximo plazo crítico con su concepto y su norma

## Cuando un skill pregunta

Si un skill de trabajo (`/escrito-defensa-calificacion`, `/briefing-asunto`, `/cronologia`,
`/solicitud-diligencias-instruccion-catalogo`, etc.) necesita asunto y no hay ninguno activo:

> "Workspaces de asunto están habilitados. ¿Qué asunto? Opciones:
> 1. Trabajar en uno existente: [primeros 5 slugs con nombre y fase]
> 2. Crear nuevo: dime el tipo de asunto y disparo `/asunto-intake`
> 3. Trabajar a nivel despacho (sin asunto): responde 'sin asunto'."

## Reglas

1. **Asunto activo es único.** No hay multi-activo.
2. **Cross-matter context off por defecto.** Un skill en el asunto A no lee archivos del B. En penal
   esto no es higiene: es **secreto profesional** y **art. 10 RGPD**. Y en asuntos con coinvestigados
   defendidos por distintos letrados, el cruce puede además comprometer la estrategia.
3. **Detach no borra nada.** Solo desactiva el contexto.
4. **`Asunto activo: ninguno`** no equivale a "ningún asunto en cartera". Solo significa que el
   contexto activo es general.
5. **Directorio propio del plugin penal.** Todas las rutas cuelgan de
   `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`. Nunca del directorio del
   plugin civil: colisiona y mezcla dos carteras de clientes.
6. **⚠️ Todo `list` y todo `switch` muestran el estado del art. 324.** Es el plazo que manda y el que
   se pierde en silencio. Si un asunto en instrucción no tiene `fecha_incoacion`, marcarlo como
   pendiente de averiguar, no como "—".
7. **Los slugs y el `_log.yaml` no llevan nombres, DNI, domicilios ni antecedentes.** Art. 10 RGPD.
   Si el usuario pide localizar un asunto "el de [nombre]", responder por slug tras consultar
   `matter.md`, sin volcar el nombre al log ni a la tabla.
