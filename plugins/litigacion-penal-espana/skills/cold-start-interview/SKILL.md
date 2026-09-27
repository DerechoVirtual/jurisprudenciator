---
name: cold-start-interview
description: Configurar el perfil de despacho de litigacion PENAL España. Captura areas penales, partido judicial, turno de oficio y guardia, posicion procesal, colaboradores, peritos y estilo de la casa. Usar con configurar plugin, cold-start, setup, redo.
---

# Cold-start del plugin de litigación penal España

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Comprobar que el conector responde** (bloque 12) → `estado`; registra el resultado en `## Integraciones disponibles`. Si pide iniciar sesión, se hace con la cuenta de Jurisprudenciator.
- **Prueba real de legislación** → `buscar_articulo` (`ley="LECrim"`, `articulo="324"`).
- **Prueba real de jurisprudencia en el partido judicial del despacho** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="AP"`, `provincia` de actuación).
- **Reglas fijas de plazos que se anotan en el perfil** (arts. 183 LOPJ, 201 y 324 LECrim) → `buscar_articulo` antes de escribirlas.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

> 📐 **Cifras: `references/anclas-normativas-penal.md`.** Ningún plazo, pena ni requisito se afirma sin estar ahí o sin verificarlo en el momento con `buscar_articulo`.

Esta skill escribe `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md` con el perfil de práctica. Sin completar este paso, las demás skills paran y piden ejecutarlo.

**La entrevista rellena EXACTAMENTE la plantilla `CLAUDE.md` de la raíz del plugin.** Cada bloque de abajo corresponde a una sección de esa plantilla. No inventar secciones nuevas ni omitir las existentes.

## Cuándo activar

- Primera instalación del plugin (el `CLAUDE.md` de config no existe o está con marcadores `[PLACEHOLDER]`/`[PENDIENTE]`)
- Petición explícita: "configura el plugin", "cold-start", "setup", "vuelve a preguntarme el perfil"
- Flag `--redo` o `--check-integrations`

## Flujo de la entrevista

### Bloque 0: Comprobación previa

1. Leer `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md` si existe.
2. Si existe y NO tiene marcadores, preguntar: "Ya tienes configuración previa. ¿(a) re-correr todo desde cero, (b) editar un campo con `/customize`, o (c) solo comprobar integraciones?"
3. Si no existe o tiene marcadores, seguir el flujo.

### Bloque 1: Identidad del despacho

Vía `AskUserQuestion` (bloques de 2-4 preguntas):

- Nombre del letrado / despacho
- Forma jurídica: abogado ejerciente individual / SLP / SCP / multiprofesional
- Colegio profesional (ICAM / ICAB / ICAV / otro) + nº de colegiado
- Provincia y **partido judicial** de actuación habitual
- Años ejerciendo
- Correo y teléfono

### Bloque 2: Turno de oficio y guardia — ⭐ pregunta crítica

**No omitir nunca.** Condiciona el protocolo de asistencia al detenido y la disponibilidad del despacho.

- ¿Está adscrito al **turno de oficio**? No / Sí
- Si sí, ¿a qué turnos?: **penal general**, **violencia de género**, **menores**, **extranjería**, otros
- ¿Hace **guardias**? Cadencia (semanal / quincenal / mensual) y ámbito (juzgado de guardia, detenidos en dependencias policiales, ambos)
- ¿Tiene protocolo propio de asistencia al detenido? ¿Quién cubre si está fuera?

> ⚠️ Al registrar la respuesta, dejar anotado en el perfil el **plazo de 3 horas del art. 520.5 LECrim**: el abogado designado debe acudir al centro de detención con la máxima premura y **siempre dentro de un máximo de 3 horas** desde la recepción del encargo; si no comparece, el Colegio designa otro, sin perjuicio de responsabilidad disciplinaria.

### Bloque 3: Áreas de práctica penal

Matriz de frecuencia (habitual / ocasional / nunca) sobre la lista de la plantilla:

- **Patrimoniales y socioeconómicos** (hurto, robo, estafa, apropiación indebida, daños)
- **Económico y societario** (administración desleal, insolvencias punibles, blanqueo)
- **Seguridad vial** (arts. 379-385 CP)
- **Lesiones y contra la vida**
- **Violencia de género y doméstica** (LO 1/2004 — competencia de las **Secciones de Violencia sobre
  la Mujer**, art. 89 LOPJ y art. 14.5 LECrim)
- **Libertad sexual** (LO 10/2022)
- **Salud pública / drogas** (arts. 368 y ss.)
- **Siniestralidad laboral** (arts. 316-318 CP)
- **Delitos contra la Administración pública**
- **Responsabilidad penal de personas jurídicas** (art. 31 bis CP) y compliance
- **Menores** (LO 5/2000)
- **Extranjería penal** (art. 89 CP)
- Otros

Preguntar además: **asuntos más frecuentes** en texto libre (p. ej. juicios rápidos de seguridad vial, estafas, lesiones, violencia de género).

### Bloque 4: Clientes

- Perfil típico: particulares / pymes / empresas / aseguradoras

### Bloque 5: Rol y posición procesal

- **Posición por defecto**: **defensa** (lo habitual) / acusación particular / acusación popular / actor civil / responsable civil subsidiario
- Si es mixta, porcentaje aproximado (solo para calibración)
- ¿**Ejerce acusación popular**? No / Sí → anotar que la acción popular exige **fianza (art. 280 LECrim**, con las excepciones del art. 281 — *verificar antes de cuantificar*) y que se ejercita al amparo de los arts. 101 y 270 LECrim y 125 CE
- ⭐ ¿**Defiende a personas jurídicas** (art. 31 bis CP)? No / Sí

> ⚠️ **Conflicto estructural — advertir siempre que la respuesta sea «Sí».**
> Defender simultáneamente a la **persona jurídica** y a la **persona física** investigada por los mismos hechos genera un conflicto de interés estructural: la defensa natural de la persona jurídica pasa a menudo por acreditar que el hecho fue obra individual del directivo eludiendo los controles de compliance, mientras que la de la persona física suele pasar por acreditar que actuó conforme a la organización. Son estrategias incompatibles.
> Añadir que el **art. 467.1 CP** *(verificado 2026-07-17)* castiga con **multa de 6 a 12 meses e inhabilitación especial de 2 a 4 años** al abogado que, habiendo asesorado o tomado la defensa de una persona, **sin su consentimiento** defienda en el mismo asunto a quien tenga intereses contrarios. No es solo deontología: es tipo penal.
> Anotar también que la conformidad de la persona jurídica la presta su **representante especialmente designado con poder especial**, es independiente de la de los demás acusados y **no les vincula** (art. 785.11 LECrim).

### Bloque 6: Órganos judiciales habituales

Rellenar la tabla de la plantilla. **No preguntar por Tribunales de Instancia civiles ni por Audiencia Provincial civil.**

> ⚠️ **Nomenclatura vigente (art. 14 LECrim, desde el 3-10-2025).** Ya no son «Juzgados»: son
> **Secciones de los Tribunales de Instancia**. El calendario de implantación de la DT 1.ª de la
> LO 1/2025 **concluyó el 31-12-2025**. Al preguntar, **anotar la denominación tal y como la use el
> despacho y como figure en sus resoluciones** — es la que después se copia en los encabezamientos.

| Órgano | Qué preguntar |
|---|---|
| **Secciones de Instrucción** del Tribunal de Instancia | nº y localidad — instrucción, juicios rápidos, delitos leves |
| **Secciones de Violencia sobre la Mujer** | nº y localidad (si trabaja LO 1/2004) |
| ⭐ **Secciones de Violencia contra la Infancia y la Adolescencia** | nº y localidad — **órgano NUEVO** (art. 14.6): víctimas niños, niñas y adolescentes. **Art. 14.7:** si concurre con violencia sobre la mujer, la competencia es **en todo caso** de esta última |
| **Secciones de lo Penal** del Tribunal de Instancia | nº y localidad — enjuiciamiento abreviado |
| **Audiencia Provincial** | provincia + sección — apelación, sumario, jurado |
| **Tribunal Superior de Justicia** | CCAA — apelación del jurado, aforados |
| **Audiencia Nacional** | si procede (art. 65 LOPJ) |
| **Tribunal Supremo, Sala Segunda** | casación |
| 🚨 **Sección de Vigilancia Penitenciaria** del Tribunal de Instancia | nº — ejecución penitenciaria. **También es Sección** (art. 84.2.g y **92 LOPJ**), no un Juzgado aparte |
| 🚨 **Sección de Menores** del Tribunal de Instancia | nº — si trabaja LO 5/2000 (art. 84.2.f y **91 LOPJ**) |

> ⛔ **No preguntar por Derecho civil foral.** No tiene encaje en el orden penal.

### Bloque 7: Colaboradores clave

Preguntar uno a uno; permitir "no aplica":

- **Procurador de cabecera** (nombre + colegio + provincia) — recordar que la representación exige **procurador con poder especial** para querella
- Procurador de territorio secundario (si actúa fuera de su provincia)
- **Médico forense de parte** — lesiones, sanidad, secuelas, imputabilidad
- **Calígrafo** — falsedad documental
- **Informático forense** — prueba digital, cadena de custodia, volcados
- **Tasador** — valoración de lo sustraído o defraudado (decisivo en los umbrales de 400 € y 50.000 € de hurto y estafa)
- **Criminólogo**
- **Detective privado**
- Perito de reconstrucción de accidentes (seguridad vial)
- Abogado colaborador para el ramo civil derivado, si lo deriva

> ⛔ **No preguntar por mediador ni experto MASC.** El MASC es del orden civil.

### Bloque 8: Herramientas y organización documental

- Carpeta raíz de asuntos
- Dónde guarda los documentos: carpeta local, OneDrive, Google Drive o Dropbox (si lo tiene conectado)
- Correo / LexNET / Word / otras bases jurídicas que use / CRM o gestor de expedientes
- Patrón de slug: **DEFAULT `descriptor-delito-año`**

> ⚠️ **Nunca** construir el slug con el nombre del cliente. En penal, un listado de carpetas que revele quién está investigado es un riesgo reputacional grave para el cliente y una brecha de datos de **categoría especial** (**art. 10 RGPD**: datos relativos a infracciones y condenas penales). Confirmar el patrón con el usuario y advertirlo aquí.

### Bloque 9: Conflictos

- Método: base personal / colaboradores / informal / formal-colegio
- Qué se chequea: cliente actual, ex-cliente, **coinvestigados en la misma causa**, víctima o testigo de otro asunto del despacho
- ¿Bloquea el intake antes de aceptar? sí / no / soft

### Bloque 10: Estilo de la casa

- Voz redaccional: por defecto pluma de la casa (`estilo-escritos-judiciales`). Confirmar o pedir variantes.
- Briefing al cliente: formato + tono + cadencia
- Comunicación con procurador: formato + postura presupuestaria
- Anclaje probatorio: por defecto, **toda afirmación de hecho se ancla al folio de las actuaciones**. Confirmar.

> ⛔ **No preguntar por «postura por defecto ante MASC»**. En penal no existe intento previo de MASC ni burofax como requisito de procedibilidad. Lo más próximo, y solo en supuestos tasados, son la **querella** o la **denuncia del ofendido** en delitos privados y semipúblicos, y el **acto de conciliación del art. 804 LECrim** en injurias y calumnias.

### Bloque 11: Reglas de la casa — plazos y criterio

- Margen de seguridad interno (DEFAULT: presentar con **2 días hábiles** de antelación al vencimiento)
- Criterio de la casa sobre **conformidades**: ¿postura general del despacho? (dejar claro en el perfil que **la conformidad la decide siempre el cliente**, no el letrado)
- Apetito al riesgo y **cobertura RC profesional**: aseguradora, límite por siniestro, franquicia
- Umbral de comunicación urgente al cliente

Anotar en el perfil, sin preguntarlo (son reglas fijas del orden penal):

- **Ley penal en el tiempo**: identificar siempre la redacción vigente **a la fecha de los hechos** (art. 2 CP) y comprobar si la posterior es **más favorable** (art. 2.2 CP). Con las reformas de 2025 y 2026 esto ya no es teórico.
- **Plazo de instrucción**: 12 meses desde la incoación, prorrogable (art. 324 LECrim). **Vigilar cada prórroga**: sin auto dictado antes del vencimiento, las diligencias posteriores no son válidas (art. 324.3).
- **Agosto**: inhábil con carácter general, pero las actuaciones de instrucción y las urgentes son hábiles (art. 183 LOPJ — *verificar antes de aplicar*).

### Bloque 12: Integraciones (`--check-integrations`)

Comprobar disponibilidad real (no solo configuración):

- Conector `jurisprudenciator` (viene con el plugin) → **única** vía de jurisprudencia y de verificación normativa. Llamar a `estado`; si responde, marcar ✓. Si pide iniciar sesión, hacerlo con la cuenta de Jurisprudenciator.
- Gestor documental (opcional) → si el abogado tiene conectado OneDrive, Google Drive o Dropbox, comprobar que responde; si trabaja con carpeta local, anotar la ruta. El plugin no incluye ninguno.
- Scheduled-tasks MCP → comprobar

Registrar en la tabla `## Integraciones disponibles` del CLAUDE.md.

### Bloque 13: Documentos semilla (opcional)

Preguntar si tiene plantillas propias que pueda apuntar (modelos de escrito de defensa, querella, hoja de encargo, minuta, política RGPD). Solo apuntadores; no se copia contenido.

## Salida

Escribir a `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md`. Si el directorio padre no existe, crearlo. Usar como esqueleto la **plantilla `CLAUDE.md` de la raíz del plugin**, reemplazando los marcadores por las respuestas y **conservando íntegras** las secciones fijas: `## Ámbito del plugin`, los avisos de MASC y de fiscal instructor, y el bloque de Jurisprudenciator.

Para campos con multi-elección (áreas de práctica, órganos, integraciones), mantener la estructura de tabla o de checklist.

Después de escribir, mostrar al usuario:

- "✅ Configurado. Tu perfil está en `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/CLAUDE.md`."
- Próximos pasos: "Documenta tu primer encargo con `/hoja-encargo`."
- Si el conector salió ✗: "jurisprudenciator no respondió — no se podrá buscar jurisprudencia ni verificar artículos, y las citas se marcarán `[verificar]`. Activa el conector en el chat o el proyecto e inicia sesión con la cuenta de Jurisprudenciator."
- Si marcó turno de oficio o guardia: recordar el **plazo de 3 horas del art. 520.5 LECrim**.
- Si marcó que defiende personas jurídicas: recordar el **conflicto estructural** y el art. 467.1 CP.

## Variantes

- `--redo`: ignora el archivo existente; sobrescribe.
- `--check-integrations`: NO re-pregunta; solo actualiza la tabla `## Integraciones disponibles`.
- `--quick`: versión 2 minutos con solo: despacho, partido judicial, **turno de oficio/guardia**, áreas penales principales y posición procesal por defecto. Pone defaults razonables en lo demás y marca esos campos con `# DEFAULT — editar después con /customize`.

## Reglas

1. **NUNCA escribir datos del usuario en el `CLAUDE.md` que viaja con el plugin.** Siempre en la ruta de config (`~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`). Ver `PROTECCION-DATOS.md`.
2. **NUNCA continuar con campos `[PLACEHOLDER]`** cuando una skill de trabajo los pida. Detenerse y pedir al usuario que complete con cold-start o customize.
3. El cold-start es **FORMAL**: no asumir respuestas, preguntar todo. Solo `--quick` y `--check-integrations` permiten defaults.
4. **Turno de oficio y guardia es pregunta obligatoria**, incluso en `--quick`.
5. ⛔ **No existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. La reforma está en tramitación (prevista 1-1-2028): no describirla como Derecho vigente ni reflejarla en el perfil.
6. ⛔ **Prohibido inventar** penas, plazos o artículos. Verificar con `buscar_articulo` o marcar `[verificar]`.
7. **Cero datos personales inventados.** Todo entre corchetes hasta que el usuario los aporte.
