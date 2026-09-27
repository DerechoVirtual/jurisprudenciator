---
name: extincion-contrato-trabajador
description: >-
  Redaccion de demanda de extincion del contrato de trabajo a instancia del trabajador por incumplimiento grave del empresario (art. 50 ET), incluidos supuestos de acoso laboral/mobbing con vulneracion de derechos fundamentales. Basada en plantilla real del despacho, anonimizada. Usar con "extincion de contrato", "articulo 50 ET", "quiero irme de la empresa con indemnizacion", "acoso laboral que me obliga a salir", "mobbing", "resolucion indemnizada del contrato", "impagos continuados y quiero extinguir". El objetivo es SALIR de la empresa con la indemnizacion del despido improcedente. Si el trabajador quiere seguir en su puesto y lo que pide es que cese el acoso o la discriminacion, usar /tutela-derechos-fundamentales; si solo quiere cobrar lo debido sin romper el contrato, /reclamacion-cantidad.
---

# Extinción del contrato a instancia del trabajador (art. 50 ET) — flujo maestro

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Estado actual de la doctrina sobre la gravedad del incumplimiento y sobre mantener el contrato vivo al demandar** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`, `fecha_desde` reciente) + `leer_sentencias` (`parrafos=3`, `terminos` del incumplimiento concreto, p. ej. `"retrasos continuados"`).
- **Acoso laboral y lesión de la dignidad o de la integridad moral (arts. 10 y 15 CE)** → `buscar_sentencias` (`base="TC"`) y, para el criterio de la Sala de suplicación, `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="AN"`, `tipo_organo="TSJ"`, `provincia`).
- **Arts. 50 y 56 y DT 11.ª ET; arts. 26.5, 32, 103.5 y 177-183 LRJS en su redacción vigente** → `buscar_articulo`.
- **Salario regulador y retribuciones del convenio (variables, salario en especie)** → `buscar_convenio` + `leer_convenio` (`buscar_en="salario"`) y `vigencia_convenio`.
- **Datos registrales de la empresa demandada** (denominación exacta, CIF, domicilio social, administradores) → `buscar_empresa_mercantil`.
- **Revisión del borrador** → `verificar_escrito` con el texto completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Marco normativo

- **Art. 50.1 ET**: causas justas para que el trabajador solicite la extinción con derecho a indemnización como despido improcedente: a) modificaciones sustanciales que redunden en perjuicio de su formación/dignidad; b) falta de pago o retrasos continuados en el salario; c) cualquier otro incumplimiento grave de las obligaciones empresariales, incluida la negativa a reintegrar al trabajador tras suspensión, y **el acoso laboral (mobbing)** cuando implica vulneración de derechos fundamentales del trabajador (dignidad, integridad moral, art. 10 y 15 CE).
- **Efectos**: indemnización equivalente a la del despido improcedente (33 días/año; 45 días/año para el periodo anterior al 12-2-2012, DT 11ª ET; art. 56 ET). Si además hay vulneración de derechos fundamentales, cabe indemnización adicional por daños y perjuicios (art. 183 LRJS) e intervención del Ministerio Fiscal (art. 177.3 LRJS) cuando se acumula tutela de derechos fundamentales a la extinción (acumulación permitida por el art. 26.5 LRJS).
- **Tramitación urgente si la causa es el impago (art. 50.1.b ET)**: el art. 103.5 LRJS (RDL 6/2023) da a estas demandas la tramitación urgente y preferente del despido (vista en 5 días, sentencia en 5 días).
- **Regla de oro**: el contrato debe estar **vivo** al ejercitar la acción — la doctrina de la Sala IV exige mantener la prestación de servicios salvo situaciones insoportables o de riesgo (verificar el estado actual de esta doctrina vía jurisprudenciator antes de aconsejar abandonar el puesto).
- **Plazo**: la acción está sujeta a la prescripción del art. 59.1-59.2 ET (1 año) mientras subsista el incumplimiento; los atrasos salariales reclamables se limitan al año anterior.
- No exige agotar previamente ningún requerimiento al empresario (a diferencia del despido, aquí es el trabajador quien insta la ruptura), pero sí la conciliación/mediación previa salvo excepción (arts. 63-64 LRJS).
- **Acumulación con despido** (art. 32 LRJS): si mientras se tramita el art. 50 la empresa despide, las demandas se acumulan y el órgano resuelve ambas — avisar al cliente de este escenario.

## Fase 1 — Documentación a pedir

- Contrato, nóminas, antigüedad, categoría y salario.
- Relato cronológico de los hechos constitutivos de incumplimiento/acoso (fechas, testigos, correos, partes médicos, denuncias internas o ante inspección de trabajo).
- Informes médicos o psicológicos si hay afectación a la salud.
- Certificado del acto de conciliación.
- Si hay coacusados individuales (p. ej. un superior jerárquico concreto), sus datos identificativos y relación con los hechos.

## Fase 2 — Batería de preguntas

- ¿La causa es exclusivamente económica/de modificación de condiciones, o hay componente de acoso/vulneración de derechos fundamentales? (determina si se cita el art. 177 LRJS y se emplaza al Ministerio Fiscal).
- ¿Hay salario en especie o retribuciones variables a incluir en el cálculo del salario regulador?
- ¿Existen otros trabajadores/testigos de los hechos de acoso?
- ¿Se solicita indemnización adicional por daños morales? Pedir criterio de cálculo razonado (no cifra arbitraria).
- Fecha y resultado de la conciliación previa.

## Fase 3 — Estructura del escrito

1. Encabezamiento: Juzgado de lo Social competente, parte actora (con marcadores genéricos para datos identificativos), parte(s) demandada(s) — empresa y, si procede, persona física señalada como acosadora — y mención de emplazamiento al Ministerio Fiscal si se invoca vulneración de derechos fundamentales (art. 177.3 LRJS).
2. **HECHOS**: antigüedad, categoría y salario → descripción cronológica de los incumplimientos/conducta de acoso, con hechos concretos, no valoraciones genéricas → gravedad y reiteración → afectación a la salud/dignidad si la hay → acreditación de la conciliación previa.
3. **FUNDAMENTOS DE DERECHO**: jurisdicción y competencia (arts. 1, 2, 6, 10.1 LRJS) → legitimación (arts. 16-17 LRJS) → representación (arts. 18, 21 LRJS) → evitación del proceso (art. 63 LRJS) → causa de extinción del art. 50.1 ET aplicable, razonando por qué el incumplimiento es "grave" (doctrina jurisprudencial sobre gravedad y culpabilidad, verificar citas vía jurisprudenciator) → si hay acoso: vulneración de arts. 10, 14, 15 CE y normativa de igualdad/prevención de riesgos laborales aplicable → efectos indemnizatorios (art. 50.2, 56 ET) → indemnización adicional por daños (art. 183 LRJS).
4. **SUPLICO**: declarar extinguida la relación laboral por causa imputable al empresario, condena a la indemnización equivalente al despido improcedente más, en su caso, indemnización adicional por vulneración de derechos fundamentales.
5. **OTROSÍES**: asistencia letrada, proposición de prueba (documental, testifical, pericial médica/psicológica, interrogatorio de la empresa y, si procede, de la persona física señalada), subsanación de defectos.

## Fase 4 — Verificación y entrega

Verificar la jurisprudencia citada con `buscar_por_cita` y las citas legales con `verificar_escrito`, pulir con `/estilo-escritos-judiciales`, entregar en Word (.docx).

---

**Nota de anonimización**: cualquier dato identificativo real de terceros (nombre de letrado/a, colegiado, domicilio, empresa, persona física señalada) presente en documentos de origen se sustituye por marcador genérico y nunca se reproduce.
