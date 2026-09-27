---
name: asunto-intake
description: Intake de un nuevo asunto laboral o de Seguridad Social. Recoge identificacion, conflictos, fuente, hechos, triage de riesgo, via de procedibilidad (SMAC o reclamacion previa) y fechas criticas de caducidad. Usar con nuevo asunto o intake este asunto.
---

# Intake de asunto — Litigación laboral España

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Empresa contraparte** (denominación exacta, CIF, domicilio social, administradores y si está en concurso), para el chequeo de conflictos del bloque 2 y para decidir si se cita al FOGASA → `buscar_empresa_mercantil`.
- **Convenio aplicable al cliente** (categoría y salario para la cuantía del bloque 5) → `buscar_convenio` + `vigencia_convenio`.
- **Plazos del bloque 10** (art. 59 ET; arts. 43, 65, 71 y 103 LRJS) → `buscar_articulo` para confirmar la redacción vigente antes de calcular.
- **Primera orientación sobre la cuestión jurídica central del bloque 12** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`): solo resúmenes; las que se vayan a usar se leen con `leer_sentencias` y se archivan en `jurisprudencia/`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Nuevo asunto", "intake", "abrir asunto", "vamos a empezar con este caso"
- Tras `/requerimiento-judicial-triage` cuando el triage escala a asunto
- Cuando llega un cliente con una carta de despido, una resolución del INSS o una citación

## Prerrequisito

`~/.claude/plugins/config/derecho-virtual/litigacion-laboral-espana/CLAUDE.md` debe estar configurado. Si no, parar y derivar a `/cold-start-interview`.

## Flujo

### Bloque 1: Identificación

Vía `AskUserQuestion`:
- Nombre corto del asunto (para el slug — apellidos cliente + tipo)
- Cliente (persona física: nombre + DNI; persona jurídica: razón social + NIF)
- Contraparte (empresa / trabajador / INSS / TGSS / mutua; "desconocida" si todavía no)
- Domicilio del cliente para notificaciones
- Tipo de asunto: despido / reclamación-cantidad / extinción-art-50 / incapacidad-permanente / contingencia / TRADE / tutela-DDFF / conflicto-colectivo / despido-colectivo / sanción / MSCT / vacaciones / otro

### Bloque 2: Conflictos

Comprobar contra el método configurado en CLAUDE.md:
- ¿Es el cliente actual o de los últimos 5 años?
- ¿Es la contraparte (empresa o trabajador) cliente actual o ex-cliente?
- ¿Hay parte adversa en otro asunto activo coincidente?
- Si cualquier conflicto: detener intake y avisar. Si soft, registrar y seguir.

### Bloque 3: Fuente

- ¿Cómo llega el cliente? (recomendación / web / oficio del turno / despacho / colaborador / sindicato)
- ¿Hoja de encargo firmada? Si no, recordar firmar antes de actos procesales.
- ¿Provisión de fondos? Cuantía + cobrada o pendiente.

### Bloque 4: Posición procesal

- Actor (habitual: trabajador/beneficiario) o demandado (habitual: empresa) en este asunto
- Si el cliente es empresa demandada: ¿le consta ya papeleta de conciliación o citación a juicio? Capturar fechas — en lo social **no hay contestación escrita a la demanda**: la oposición se formula oralmente en el acto del juicio (art. 85 LRJS), así que la preparación de la defensa arranca el día del intake.

### Bloque 5: Hechos y pretensión

Capturar en libre forma:
- Resumen de hechos en 3-5 frases (fecha de despido / hecho causante, antigüedad, salario, convenio)
- Pretensión principal (nulidad/improcedencia, cantidad, grado de incapacidad, contingencia, etc.)
- Pretensiones accesorias (intereses del art. 29.3 ET, indemnización art. 183 LRJS, recargos)
- Cuantía exacta o estimada (salario regulador incluido)

### Bloque 6: Triage de riesgo

Aplicar matriz severidad × probabilidad del CLAUDE.md:
- Severidad estimada (alta/media/baja) según las bandas configuradas
- Probabilidad estimada (alta/media/baja) según las bandas configuradas
- Etiqueta resultante (Crítico / Prioritario / Rutina / Vigilar)
- Mapping a `_log.yaml`: critico / alto / medio / bajo

### Bloque 7: Materialidad

- Cuantía: alta / media / baja relativa al cliente
- Relación con el cliente (cliente recurrente / único asunto / cliente de relación / sindicato)
- ¿Afecta a reputación del cliente?

### Bloque 8: Colaboradores y representación

- En lo social la defensa puede asumirla abogado o graduado social; el procurador es **opcional** (arts. 18-21 LRJS). Tomar el default del CLAUDE.md o preguntar.
- ¿Perito necesario? (médico en incapacidades/contingencia; económico en cantidad/despido objetivo)
- ¿Abogado colaborador? (si el asunto deriva a penal — p. ej. acoso — o a civil)

### Bloque 9: Conservación documental

- ¿Hay riesgo de pérdida de prueba? (correos, nóminas, registros horarios, cámaras, WhatsApps)
- Generar comunicación al cliente recordando deber de conservación. Marcar `legal_hold: pending` en log para que `/conservacion-documental --emitir` la genere.

### Bloque 10: Fechas críticas — LO MÁS IMPORTANTE DEL INTAKE LABORAL

Capturar y calcular:
- Fecha del despido / hecho causante / notificación de la resolución administrativa
- **Caducidad de 20 días hábiles** en despido, sanciones, MSCT y movilidad (arts. 59.3-59.4 ET; 103 LRJS) — sábados, domingos y festivos excluidos
- **Prescripción de 1 año** en reclamaciones de cantidad (art. 59.1-59.2 ET)
- **Reclamación previa SS**: 30 días para interponerla; demanda en 30 días desde su denegación expresa o por silencio —45 días— (art. 71 LRJS); en altas médicas, plazos especiales (11/7/20 días)
- La papeleta de conciliación **suspende** la caducidad e **interrumpe** la prescripción; el cómputo se reanuda al día siguiente de intentada la conciliación o a los 15 días hábiles de la presentación si no se celebró (art. 65.1 LRJS)
- Agosto y del 24-dic al 6-ene son inhábiles **salvo** en despido, extinción arts. 50-52 ET, movilidad, MSCT, conciliación de vida familiar, altas médicas, vacaciones, materia electoral, conflictos colectivos, impugnación de convenios y tutela DDFF (art. 43.4 LRJS)
- Próxima fecha límite a vigilar

### Bloque 11: Vía de procedibilidad

- Demandado privado (empresa/trabajador/TRADE) → **papeleta de conciliación** ante el SMAC (`/papeleta-conciliacion`), salvo excepciones del art. 64 LRJS
- INSS/TGSS/mutua (prestaciones) → **reclamación previa** (`/reclamacion-previa-seguridad-social`)
- AAPP empleadora → agotamiento de la vía administrativa cuando proceda (arts. 69-70 LRJS)
- Tutela DDFF, conflictos con exención del art. 64, despido colectivo del art. 124 → exentos
- Marcar en log `procedibilidad_acreditada: no` hasta tener certificación del acto o resolución

### Bloque 12: Posición inicial

- Tesis del asunto en 2-3 frases (la "historia" que vamos a contar)
- Puntos débiles ya identificados
- Cuestión jurídica central (ej. "carta de despido genérica → improcedencia", "presunción de laboralidad 156.3 LGSS para el burnout", "gravedad del impago para el art. 50 ET")

## Salida

1. Crear carpeta `~/.claude/plugins/config/derecho-virtual/litigacion-laboral-espana/matters/<slug>/`
2. Escribir `matter.md` con:
   - Cabecera `RESERVADO Y CONFIDENCIAL — SECRETO PROFESIONAL DEL ABOGADO`
   - Datos identificativos
   - Hechos y pretensión
   - Triage de riesgo
   - Tesis inicial
   - Fechas críticas (caducidad/prescripción + vía de procedibilidad)
   - Colaboradores
   - Próximos pasos
3. Crear `history.md` con primera entrada `[AAAA-MM-DD] INTAKE — asunto creado.`
4. Crear subcarpetas `escritos/`, `jurisprudencia/`
5. Añadir fila a `matters/_log.yaml`:

```yaml
- slug: garcia-perez-despido-2026
  name: García Pérez — Despido disciplinario
  status: open
  side: actor
  risk: alto
  type: despido
  cuantia: 28400  # indemnización estimada + salarios
  representacion: letrado propio (procurador no — opcional en lo social)
  tribunal: Sección de lo Social del TI de [PARTIDO JUDICIAL]
  contraparte: Construcciones Sur SL
  abogado_contraparte: pendiente
  next_deadline: 2026-06-02  # caducidad 20 días hábiles (suspendida por papeleta 2026-05-20)
  materiality: alta
  related_matters: []
  conservacion_documental: pending
  procedibilidad_acreditada: no  # papeleta SMAC presentada, acto pendiente
  opened: 2026-05-13
  last_updated: 2026-05-13
  notas: "Demanda en preparación. Acto de conciliación SMAC señalado."
```

6. Si workspaces de asunto están habilitados (default sí), preguntar: "¿Hacer este asunto el activo?" Si sí, escribir en CLAUDE.md → `## Workspaces de asuntos` → `Asunto activo: <slug>`.

## Reglas

1. **NUNCA crear asunto sin chequeo de conflictos.** Si hay conflicto duro, parar.
2. **NUNCA omitir la vía de procedibilidad.** Si el tipo de asunto exige conciliación previa o reclamación previa y `procedibilidad_acreditada: no`, toda skill de redacción de demanda parará hasta acreditarla (art. 81.3 LRJS da 15 días para subsanar, pero no se cuenta con ello).
3. **Calcular caducidad al intake**, no después. Los 20 días hábiles del despido son el dato que decide si el asunto tiene sentido aceptar — y corren aunque sea agosto (art. 43.4 LRJS).
4. **Fechas en formato AAAA-MM-DD.** Convertir relativas ("la semana que viene") a absolutas.
