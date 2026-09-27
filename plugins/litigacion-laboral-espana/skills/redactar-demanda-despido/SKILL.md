---
name: redactar-demanda-despido
description: >-
  Redaccion de demandas por despido (disciplinario, objetivo, nulo o subsidiariamente improcedente) conforme a la LRJS y el ET. Basada en plantilla real del despacho, anonimizada. Usar con "demanda despido", "despido disciplinario", "despido nulo", "despido improcedente", "redactar demanda por despido", "me han despedido estando embarazada", "me han despedido tras denunciar acoso", "despido como represalia". Es el cauce UNICO cuando la vulneracion de derechos fundamentales se materializa en un despido: la nulidad se pide dentro de esta demanda, no mediante una tutela autonoma (/tutela-derechos-fundamentales solo si no ha habido despido y la relacion continua). Plazo de caducidad de 20 dias habiles.
---

# Redactar demanda de despido — flujo maestro

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Convenio aplicable, categoría y salario para el módulo de la indemnización y los salarios de tramitación** → `buscar_convenio` (sector y territorio del centro de trabajo) + `leer_convenio` (`articulo`, o `buscar_en="salario base"` / `buscar_en="antigüedad"`) y `vigencia_convenio` para confirmar el texto que regía en la fecha del despido.
- **Datos registrales de la empresa demandada** (denominación exacta, CIF, domicilio social, administradores y si está en concurso, para citar al FOGASA) → `buscar_empresa_mercantil`.
- **Arts. 55-56 y DT 11.ª ET, arts. 103-113, 181.2 y 183 LRJS y Ley 15/2022 en su redacción vigente** → `buscar_articulo` (`ley="ET"`, `articulo="55"`; `ley="LRJS"`, `articulo="108"`...).
- **Doctrina de la Sala Cuarta** (carta genérica, despido durante la baja médica, cuantificación del daño moral del art. 183) → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`) + `leer_sentencias` con `parrafos=3` y `terminos` del punto que se quiere acreditar.
- **Doctrina constitucional sobre indicios e inversión de la carga de la prueba** para la petición de nulidad → `buscar_sentencias` (`base="TC"`) + `leer_sentencias` (`parrafos=3`).
- **Revisión del borrador antes de presentarlo** → `verificar_escrito` con el texto completo y `buscar_por_cita` sobre cada ECLI o ROJ que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Marco normativo de referencia

- **Plazo de caducidad**: 20 días hábiles desde la efectividad del despido (art. 59.3 ET, art. 103.1 LRJS) — no se computan sábados, domingos ni festivos, y **sí corre en agosto y Navidad** (el despido es modalidad urgente exenta de la inhabilidad del art. 43.4 LRJS).
- **Conciliación previa obligatoria**: arts. 63-68 LRJS, ante el servicio de mediación/arbitraje autonómico (SMAC o equivalente). La papeleta **suspende** la caducidad; el cómputo se reanuda al día siguiente de intentada la conciliación o a los 15 días hábiles de la presentación si no se celebró (art. 65.1 LRJS). Sin acreditar el intento, la demanda se archiva si no se subsana en 15 días (art. 81.3 LRJS).
- **Órgano**: Juzgado de lo Social / Sección de lo Social del Tribunal de Instancia (nomenclatura LO 1/2025) del lugar de prestación de servicios o del domicilio del demandado, a elección del demandante (art. 10.1 LRJS).
- **Tramitación urgente** (art. 103.4 LRJS, añadido por RDL 6/2023): si la empresa no ha tramitado la baja en la TGSS, el procedimiento es urgente y preferente (vista en 5 días, sentencia en 5 días) — preguntarlo SIEMPRE.
- **Calificación del despido**: procedente / improcedente / nulo (art. 55 ET, arts. 108-113 y 120-123 LRJS). Nulo cuando vulnera derechos fundamentales o es discriminatorio (arts. 14 y 15 CE, Ley 15/2022) o en los supuestos de nulidad objetiva (embarazo, nacimiento y cuidado, reducción de jornada, víctimas de violencia de género — art. 55.5 ET).
- **Efectos**: nulidad → readmisión inmediata + salarios de tramitación (art. 55.6 ET, art. 113 LRJS). Improcedencia → opción empresarial readmisión + salarios de tramitación / indemnización (33 días/año — 45 días/año para el tiempo anterior al 12-2-2012, DT 11ª ET; art. 56 ET, art. 110 LRJS). Si el despedido es representante legal o sindical, la opción es del trabajador (art. 56.4 ET, art. 110.2 LRJS).
- **Despido objetivo** (arts. 52-53 ET, arts. 120-123 LRJS): mismos plazos y estructura, con control añadido de los requisitos formales del art. 53.1 (carta con causa, puesta a disposición SIMULTÁNEA de la indemnización de 20 días/año, preaviso de 15 días) — su incumplimiento determina la improcedencia (art. 122.3 LRJS).
- **Indemnización adicional por vulneración de derechos fundamentales**: art. 183 LRJS, se puede fijar orientativamente por analogía con las cuantías de la LISOS para infracciones muy graves cuando el daño moral es de difícil cuantificación — debe justificarse, no fijarse arbitrariamente (doctrina Sala IV: verificar cita vía jurisprudenciator).
- **FOGASA**: si la empresa está en concurso o presumiblemente insolvente, pedir su citación (art. 23.2 LRJS).

## Regla cardinal

NO redactar al primer disparo. Recorrer las fases. Sin conciliación previa acreditada, no hay demanda válida — derivar primero a `/papeleta-conciliacion`.

## Fase 1 — Documentación a pedir

- Contrato de trabajo y nóminas (antigüedad, categoría, salario diario/bruto).
- Carta de despido (causa alegada, fecha de efectos).
- Certificado del acto de conciliación (con/sin avenencia) + copia de la papeleta presentada.
- Convenio colectivo aplicable.
- Indicios de posible causa discriminatoria o de vulneración de derechos fundamentales, si los hay (bajas médicas, denuncias previas, comparativas con otros trabajadores).
- Si aplica: condición de representante legal/sindical del trabajador en el último año (afecta a garantías especiales).

## Fase 2 — Batería de preguntas (AskUserQuestion obligatorio)

- ¿Tipo de despido? disciplinario / objetivo / colectivo.
- ¿Se alega causa discriminatoria o vulneración de derecho fundamental? (determina si se pide nulidad, no solo improcedencia).
- ¿Antigüedad y salario diario exactos? (para calcular indemnización).
- ¿Resultado de la conciliación? fecha, sin avenencia/con avenencia — y recomputar la caducidad con la suspensión del art. 65.1 LRJS.
- ¿La empresa tramitó la baja en la TGSS? (si no: tramitación urgente del art. 103.4 LRJS).
- ¿Se reclama también indemnización por daños morales (art. 183 LRJS)? Si sí, pedir base de cálculo razonada (no una cifra sin justificar).
- ¿Se acumula reclamación de cantidad? (posible conforme al art. 26.3 LRJS: salarios pendientes con el despido).
- Órgano competente (lugar de prestación de servicios o domicilio del demandado, a elección del actor — art. 10.1 LRJS).
- ¿Empresa solvente? Si hay riesgo de insolvencia/concurso, citar al FOGASA (art. 23.2 LRJS).

## Fase 3 — Estructura del escrito (según plantilla del despacho)

1. Encabezamiento: "AL JUZGADO DE LO SOCIAL / A LA SECCIÓN DE LO SOCIAL DEL TRIBUNAL DE INSTANCIA DE [...]" + identificación de la parte actora (letrado/a, poderdante, domicilio a notificaciones) — **usar siempre marcadores `[NOMBRE ACTOR]`, `[DNI]`, `[DOMICILIO]`, `[LETRADO/A]`, `[Nº COLEGIADO]`, nunca datos reales de terceros ni del despacho salvo que el usuario los facilite expresamente para ese asunto**.
2. **HECHOS** numerados: relación laboral (fecha inicio, categoría, salario, convenio aplicable) → carta de despido (fecha, causa alegada) → por qué los hechos son falsos/discriminatorios/desproporcionados → normativa vulnerada → cálculo de indemnización → legitimación (no representante legal/sindical) → acreditación de conciliación previa (fecha, resultado, documentos).
3. **FUNDAMENTOS DE DERECHO**: jurisdicción y competencia (arts. 1, 2.a, 6 y 10.1 LRJS) → capacidad y legitimación (arts. 16-17 LRJS; art. 4.2.g ET) → representación y defensa (arts. 18-21 LRJS) → evitación del proceso/conciliación previa (arts. 63-65 LRJS, con las fechas de papeleta y acto) → requisitos de la demanda (art. 80 LRJS, más los específicos del art. 104 para despido) y plazo de caducidad (art. 59.3 ET; art. 103 LRJS, con el cómputo de la suspensión) → modalidad procesal de despido (arts. 103-113 LRJS; arts. 120-123 si es objetivo) → carga de la prueba de los hechos de la carta sobre el empresario y prohibición de imputaciones nuevas (art. 105 LRJS) → nulidad y sus efectos (art. 55.5-55.6 ET; arts. 108.2 y 113 LRJS; si hay indicios de vulneración de DDFF, inversión de carga del art. 181.2 LRJS — doctrina constitucional sobre indicios, verificar cita exacta vía jurisprudenciator antes de citar) → improcedencia y sus efectos (art. 56 ET; arts. 108.1, 110 LRJS; art. 122.3 si es objetivo) → indemnización por vulneración de derechos fundamentales (art. 183 LRJS) → convenio colectivo aplicable.
4. **SUPLICO**: admisión, señalamiento de conciliación y juicio, sentencia declarando nulidad (readmisión + salarios de tramitación) y subsidiariamente improcedencia (opción readmisión/indemnización), más indemnización de daños morales si procede.
5. **OTROSÍES**: designación de letrado/a a efectos de notificación (con marcador genérico, nunca datos reales salvo que el usuario los aporte para su propio asunto) — proposición de prueba (interrogatorio de la demandada **con apercibimiento de ficta confessio del art. 91.2 LRJS**, testifical, documental —requerir el registro horario o el expediente si obran en poder de la empresa, art. 90.3 LRJS—, pericial) — manifestación de subsanación de defectos (art. 81 LRJS).

## Fase 4 — Verificación

- Confirmar plazo de caducidad no transcurrido (20 días hábiles).
- Confirmar conciliación previa acreditada.
- Verificar con `buscar_por_cita` cualquier STC/STS citada y pasar el borrador por `verificar_escrito`.
- Pasar por `/estilo-escritos-judiciales` para el pulido final.

## Fase 5 — Entrega

Word (.docx) maquetado, listo para presentación telemática (LexNET/plataforma autonómica equivalente).

---

**Nota de anonimización (aplica a todas las skills basadas en plantillas reales del despacho):** cualquier nombre, DNI, colegiado, domicilio, teléfono o email de terceros (letrados, clientes, empresas) presente en los documentos de origen se sustituye por un marcador genérico `[DATO]` y NUNCA se reproduce en el cuerpo de la skill ni en ejemplos. Solo se conserva la estructura jurídica y el lenguaje procesal.
