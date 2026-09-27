---
name: reclamacion-cantidad
description: >-
  Redaccion de demanda de reclamacion de cantidad laboral (salarios impagados, horas extraordinarias, pagas extra, finiquito, diferencias de convenio, complementos) por el procedimiento ordinario de la LRJS, con FOGASA cuando procede, MANTENIENDO vivo el contrato. Usar con "reclamacion de cantidad", "salarios impagados", "me deben nominas", "horas extra", "finiquito", "diferencias salariales". Solo para trabajadores por cuenta ajena: si quien reclama es un autonomo economicamente dependiente, usar /reclamacion-trade. Y si los impagos son graves y continuados y el trabajador quiere ademas SALIR de la empresa con indemnizacion, valorar la extincion del art. 50.1.b) ET → /extincion-contrato-trabajador (acumulable a la cantidad).
---

# Reclamación de cantidad — procedimiento ordinario

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Tablas salariales, pluses, pagas extraordinarias y precio de la hora extra del convenio, año por año del desglose** → `buscar_convenio` (sector y territorio) + `leer_convenio` (`buscar_en="tablas salariales"`, `buscar_en="horas extraordinarias"`) y `vigencia_convenio` para saber qué texto regía en cada periodo reclamado.
- **Salario mínimo interprofesional del año, cuando el salario pactado o el de convenio queda por debajo** → `buscar_boe` → `leer_boe` (real decreto del SMI de cada año reclamado).
- **Arts. 26, 29.3, 34.9 y 59 ET; arts. 25-26, 80-85, 94.2 y 191.2.g) LRJS en su redacción vigente** → `buscar_articulo`.
- **Solvencia de la empresa y citación del FOGASA** → `buscar_empresa_mercantil` (estado, concurso, disolución) y `novedades_boe` con el nombre o el NIF de la empresa (edictos concursales recientes).
- **Doctrina de la Sala Cuarta sobre el interés por mora del art. 29.3 ET y la prueba de las horas extraordinarias sin registro horario** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Revisión del borrador** → `verificar_escrito` con el texto completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Marco normativo

- **Prescripción de 1 año** (art. 59.1-59.2 ET) desde que cada cantidad fue exigible — las nóminas prescriben mes a mes: calcular qué mensualidades siguen vivas ANTES de cuantificar.
- **Conciliación previa obligatoria** (arts. 63-65 LRJS): la papeleta **interrumpe** la prescripción (`/papeleta-conciliacion`).
- **Interés por mora salarial**: 10% anual sobre lo adeudado (art. 29.3 ET) — pedirlo siempre; la doctrina actual de la Sala IV lo aplica de forma objetiva y automática a deudas salariales (verificar cita vía jurisprudenciator).
- **Procedimiento**: ordinario (arts. 80-102 LRJS). No hay contestación escrita: la empresa se opone oralmente en el acto del juicio (art. 85 LRJS).
- **Cuantía y recurso**: si lo reclamado no excede de 3.000 €, la sentencia NO tiene suplicación (art. 191.2.g LRJS) — advertirlo al cliente (pleito a una sola instancia).
- **Acumulación**: acumulables entre sí las acciones de cantidad (art. 25 LRJS); acumulable la cantidad al despido conforme al art. 26.3 LRJS.
- **FOGASA** (art. 33 ET; art. 23 LRJS): si la empresa está en concurso o es presumiblemente insolvente, pedir su citación — la condena marcará el título para las prestaciones de garantía.
- **Carga documental de la empresa**: nóminas, registro horario (art. 34.9 ET — conservación 4 años) y registro retributivo son documentos en poder del demandado: pedir su aportación con apercibimiento del art. 94.2 LRJS.

## Regla cardinal

La reclamación de cantidad se gana con el **desglose**. Sin cuadro concepto-a-concepto (mes, concepto, devengado, percibido, diferencia), no hay demanda: el suplico exige cantidad líquida y el juez no va a hacer las cuentas del actor.

## Fase 1 — Documentación a pedir

- Contrato y nóminas del periodo reclamado (y las 12 últimas para el salario regulador si se acumula a despido).
- Convenio colectivo aplicable (tablas salariales del periodo — verificar la vigente vía BOE/boletín autonómico).
- Registro horario o, en su defecto, cuadrantes, correos, geolocalización, testigos (para horas extra).
- Comunicaciones reclamando el pago (si las hay).
- Certificado del acto de conciliación (o papeleta presentada).
- Vida laboral si hay dudas de antigüedad o de altas/bajas.

## Fase 2 — Batería de preguntas (AskUserQuestion)

- ¿Qué conceptos se reclaman? (salario base / complementos / horas extra / pagas extra / vacaciones no disfrutadas / finiquito / diferencias de convenio o categoría).
- ¿Periodo exacto de cada concepto? — aplicar el filtro de prescripción de 1 año y decir qué queda fuera.
- ¿La relación laboral sigue viva o se ha extinguido? (si hay despido en los últimos 20 días hábiles: valorar acumulación con `/redactar-demanda-despido`).
- ¿Hay riesgo de insolvencia o concurso? (citar FOGASA).
- ¿Resultado de la conciliación? fecha y estado.
- ¿La cuantía supera los 3.000 €? — informar sobre el acceso a suplicación.

## Fase 3 — Estructura del escrito

1. Encabezamiento: "AL JUZGADO DE LO SOCIAL / A LA SECCIÓN DE LO SOCIAL DEL TRIBUNAL DE INSTANCIA DE [...]", parte actora con marcadores genéricos, empresa demandada (y FOGASA si se cita).
2. **HECHOS**: relación laboral (antigüedad, categoría, convenio, salario) → conceptos y periodos adeudados, con remisión al **cuadro de desglose** (incorporado al cuerpo o como documento) → reclamaciones extrajudiciales efectuadas → conciliación previa (fecha, resultado).
3. **FUNDAMENTOS DE DERECHO**: jurisdicción y competencia (arts. 1, 2.a, 6, 10.1 LRJS) → legitimación (arts. 16-17 LRJS) → conciliación previa (arts. 63-65 LRJS) → procedimiento ordinario (arts. 80 ss. LRJS) → fondo: arts. 4.2.f, 26, 29 ET + convenio colectivo (artículo y tabla concretos) → interés del art. 29.3 ET → responsabilidad del FOGASA (art. 33 ET) si se cita.
4. **SUPLICO**: condena al pago de la cantidad total líquida [X € con desglose por conceptos], más el 10% de interés por mora del art. 29.3 ET, con la responsabilidad legal del FOGASA en su caso.
5. **OTROSÍES**: proposición de prueba — interrogatorio de la demandada con apercibimiento del art. 91.2 LRJS, documental con requerimiento de exhibición del registro horario y nóminas (arts. 90.3 y 94.2 LRJS), testifical si hay horas extra.

## Fase 4 — Verificación

- Cuadro de desglose: las sumas CUADRAN (comprobar aritmética dos veces; es el error más frecuente).
- Prescripción: ningún concepto reclamado anterior al año (salvo interrupciones acreditadas).
- Convenio: tabla salarial del AÑO correcto.
- Conciliación previa acreditada.
- Pasar por `/subsuncion-juridica` y `/estilo-escritos-judiciales`.

## Fase 5 — Entrega

Word (.docx) maquetado, listo para presentación telemática (LexNET/plataforma autonómica equivalente), con el cuadro de desglose como tabla formateada.

---

**Nota de anonimización (aplica a todas las skills basadas en plantillas reales del despacho):** cualquier nombre, DNI, colegiado, domicilio, teléfono o email de terceros presente en los documentos de origen se sustituye por un marcador genérico `[DATO]` y NUNCA se reproduce en el cuerpo de la skill ni en ejemplos.
