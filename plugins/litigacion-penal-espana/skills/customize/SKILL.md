---
name: customize
description: Editar un campo del perfil de despacho penal sin re-correr todo el cold-start. Cambiar partido judicial, turno de oficio, areas penales, colaboradores y peritos, organos, integraciones. Usar con cambiar mi perfil o customize.
---

# Customize — editar un campo concreto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Re-comprobar integraciones** (campo 12) → `estado` de Jurisprudenciator y, si el despacho lo tiene conectado, el gestor documental que use.
- **Cambio en las reglas de plazos** (margen interno, días inhábiles, art. 324) → `buscar_articulo` (`ley="LOPJ"`, `articulo="183"`; `ley="LECrim"`, `articulo="324"`) antes de escribir la regla.
- **Se activa la acusación popular o la defensa de personas jurídicas** → `buscar_articulo` (`ley="LECrim"`, arts. 280 y 281; `ley="CP"`, art. 467) para el aviso en cadena.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

> 📐 **Cifras: `references/anclas-normativas-penal.md`.** Verificar con `buscar_articulo` lo que no esté ahí.

## Cuándo activar

- "Cambiar mi [campo]"
- "Actualizar mi perfil"
- "Editar [sección]"
- "Añadir procurador / perito / colaborador"
- "Me he apuntado al turno de oficio de violencia de género"
- "Mi partido judicial ha cambiado a X"

## Flujo

### 1. Comprobar que hay perfil

Leer `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md`. Si no existe o tiene marcadores `[PLACEHOLDER]` masivos, derivar a `/cold-start-interview` — customize no es el camino para configurar desde cero.

### 2. Detectar qué campo

Si el usuario nombra el campo, ir directo. Si no, mostrar menú (refleja las secciones de la plantilla `CLAUDE.md`):

```
¿Qué cambiamos?
1.  Identidad del despacho (forma jurídica, colegio, colegiado, partido judicial, contacto)
2.  Turno de oficio y guardia (penal, violencia de género, menores)
3.  Áreas de práctica penal
4.  Clientes (perfil típico)
5.  Rol y posición procesal (defensa / acusación particular / popular / actor civil / responsable civil)
6.  Órganos judiciales habituales (Secciones del Tribunal de Instancia: de Instrucción, de Violencia
    sobre la Mujer, de Violencia contra la Infancia y la Adolescencia, de lo Penal, de Menores y de
    Vigilancia Penitenciaria —art. 84.2 LOPJ, estas dos últimas **también son Secciones**—;
    AP, TSJ, AN, TS Sala 2ª)
7.  Colaboradores y peritos (procurador, forense de parte, calígrafo, informático forense,
    tasador, criminólogo, detective)
8.  Herramientas y organización documental (carpeta raíz, patrón de slug)
9.  Conflictos (método)
10. Estilo de la casa (voz, briefing al cliente, anclaje probatorio)
11. Reglas de la casa (margen de plazos, criterio sobre conformidades, RC profesional)
12. Integraciones (Jurisprudenciator con `estado` y, si lo hay, el gestor documental conectado —
    re-comprobar)
13. Documentos semilla (apuntadores a plantillas)
```

### 3. Hacer el cambio

Vía `AskUserQuestion`:
- Mostrar valor actual
- Pedir nuevo valor
- Confirmar antes de escribir

### 4. Validaciones en cadena

- **Partido judicial cambia** → revisar **órganos habituales** (Secciones de Instrucción, de lo Penal y de Violencia sobre la Mujer del Tribunal de Instancia, AP) y **procurador**: preguntar si también cambian.
- **Colegio profesional cambia** → revisar nº de colegiado (no encaja en otro colegio) y **adscripción al turno de oficio** (es por colegio).
- **Se activa turno de oficio o guardia** → recordar el **plazo de 3 horas del art. 520.5 LECrim** para acudir al centro de detención desde la recepción del encargo, y preguntar quién cubre si el letrado está fuera.
- ⭐ **Se activa «defiende personas jurídicas»** → advertir del **conflicto estructural** de defender a la vez a la persona jurídica y a la persona física investigada por los mismos hechos, y del **art. 467.1 CP** *(verificado 2026-07-17: multa de 6 a 12 meses e inhabilitación especial de 2 a 4 años al abogado que, sin consentimiento, defienda en el mismo asunto a quien tenga intereses contrarios)*.
- **Se activa «ejerce acusación popular»** → recordar la **fianza del art. 280 LECrim**, con las excepciones del art. 281 *(verificar antes de cuantificar)*.
- **Se añade un área nueva** (p. ej. violencia de género, menores, personas jurídicas) → preguntar si cambian los órganos habituales y los peritos.
- **Cambia el patrón de slug** → ⚠️ advertir: **nunca** construir el slug con el nombre del cliente. Un listado de carpetas que revele quién está investigado es una brecha de datos de **categoría especial** (**art. 10 RGPD**: infracciones y condenas penales). DEFAULT: `descriptor-delito-año`.
- **Cambio masivo de perfil** → recomendar `/cold-start-interview --redo`.

### 5. Escribir

Editar `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md` modificando **solo** la línea o sección afectada. Mantener el resto idéntico, incluidas las secciones fijas (`## Ámbito del plugin`, avisos de MASC y de fiscal instructor, bloque de Jurisprudenciator).

Añadir una fila al `## Historial de cambios` con la fecha y la acción.

El perfil de este plugin es autónomo: el cambio se guarda solo en su `CLAUDE.md` y no se comparte con ningún otro plugin.

### 6. Output

```
✅ Actualizado.

**Campo:** [nombre]
**Antes:** [valor anterior]
**Ahora:** [valor nuevo]

[Si dispara otras revisiones:]
**Posibles ajustes en cadena:** [sugerencias]
```

## Reglas

1. **Un campo por sesión.** Si el usuario quiere cambiar varios, hacerlos secuencialmente uno a uno, confirmando cada uno.
2. **NUNCA borrar campos.** Si el usuario quiere "vaciar" un campo, dejar `[PENDIENTE]` con nota; no borrar la fila.
3. **NUNCA escribir datos reales en el `CLAUDE.md` que viaja con el plugin.** Solo en la ruta de config. Ver `PROTECCION-DATOS.md`.
4. ⛔ **No existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. No reflejar en el perfil la reforma en tramitación (prevista 1-1-2028).
5. ⛔ **No introducir campos del orden civil** (MASC, Derecho civil foral, órganos civiles, burofax previo). Si el usuario los pide, explicar que el plugin es exclusivamente penal.
6. ⛔ **Prohibido inventar** penas, plazos o artículos. Verificar con `buscar_articulo` o marcar `[verificar]`.
