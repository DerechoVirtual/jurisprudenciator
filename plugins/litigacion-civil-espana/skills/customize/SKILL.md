---
name: customize
description: Editar un campo del perfil de despacho sin re-correr todo el cold-start. Cambiar provincia, colaboradores, calibracion de riesgo, plantillas, integraciones. Usar con cambiar mi perfil o customize.
---

# Customize — editar un campo concreto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Re-comprobar integraciones (opción 9)** → `estado`.
- **Cambio de forma jurídica o de datos de la sociedad profesional del despacho (opción 1)** → `buscar_empresa_mercantil`.
- **Cambio de Derecho civil foral en el panorama (opción 5)** → `buscar_boe` (por materia) → `leer_boe`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Cambiar mi [campo]"
- "Actualizar mi perfil"
- "Editar [sección]"
- "Añadir procurador / perito / plantilla / contraparte habitual"
- "Mi provincia ha cambiado a X"

## Flujo

### 1. Comprobar que hay perfil

Leer `~/.claude/plugins/config/derecho-virtual/litigacion-civil-espana-pro/CLAUDE.md`. Si tiene `[PLACEHOLDER]` masivos, derivar a `/cold-start-interview` — customize no es el camino para configurar desde cero.

### 2. Detectar qué campo

Si el usuario nombra el campo, ir directo. Si no, mostrar menú:

```
¿Qué cambiamos?
1. Despacho (forma jurídica, colegio, provincia, colegiado)
2. Rol procesal y posición default
3. Colaboradores (procurador / perito / abogado colaborador / mediador)
4. Calibración de riesgo (apetito / bandas / autoridad para transigir / RC)
5. Panorama (Tribunales habituales, contrapartes, Derecho civil foral)
6. Estilo de la casa (voz, briefing al cliente, plantillas, MASC default)
7. Almacenamiento documental (carpeta local, OneDrive, Google Drive o Dropbox si está conectado; carpeta raíz; slug pattern)
8. Conflictos (método)
9. Integraciones (Jurisprudenciator: re-comprobar con `estado`; gestor documental conectado, si lo hay)
10. Documentos semilla (apuntadores a plantillas)
```

### 3. Hacer el cambio

Vía `AskUserQuestion`:
- Mostrar valor actual
- Pedir nuevo valor
- Confirmar antes de escribir

### 4. Validaciones

- **Provincia cambia → revisar Tribunales habituales** (preguntar si también cambian)
- **Posición procesal cambia → revisar plantillas activas** (las que se usen)
- **Colegio profesional cambia → revisar colegiado nº** (no encaja a otro colegio)
- **Cambio masivo de calibración riesgo → recomendar `/cold-start-interview --redo`**

### 5. Escribir

Editar `~/.claude/plugins/config/derecho-virtual/litigacion-civil-espana-pro/CLAUDE.md` modificando solo la línea/sección afectada. Mantener el resto idéntico.

El perfil de este plugin es autónomo del despacho; el cambio se guarda solo en su `CLAUDE.md` y no se comparte con ningún otro plugin.

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

1. **Un campo por sesión.** Si el usuario quiere cambiar varios, hacerlos secuencialmente uno a uno (confirmando cada uno).
2. **NUNCA borrar campos.** Si el usuario quiere "vaciar" un campo, dejar `[PENDIENTE]` con nota, no borrar la fila.
3. **Cambios cross-plugin:** advertir si el campo está en `## Perfil del despacho`.
