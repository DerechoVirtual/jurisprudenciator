---
name: ejecucion-laboral
description: Redaccion de escritos de ejecucion de sentencias laborales, tanto dineraria general como la especifica de sentencias de despido (readmision/indemnizacion, salarios de tramitacion, incidente de no readmision) y ejecucion provisional. Usar con "ejecucion laboral", "ejecutar sentencia despido", "incidente no readmision", "ejecucion provisional".
---

# Ejecución laboral

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Situación registral de la empresa ejecutada** (estado, domicilio, administradores, disolución o liquidación) → `buscar_empresa_mercantil`; actos inscritos recientes con `sumario_borme` → `leer_boe`.
- **Concurso, insolvencia o subastas que afectan a la ejecución** → `novedades_boe` (nombre o NIF de la ejecutada, periodo de hasta 31 días) → `leer_boe`.
- **Arts. 237-302 LRJS y art. 33 ET (prestaciones y topes del FOGASA) en su redacción vigente** → `buscar_articulo`.
- **Salario mínimo interprofesional del año, referencia de los topes del FOGASA** → `buscar_boe` → `leer_boe`.
- **Doctrina sobre el incidente de no readmisión, la readmisión irregular y los salarios dejados de percibir** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Inmueble conocido del ejecutado que se quiere señalar para el embargo** → `consultar_catastro` (dirección o referencia catastral); no da el titular, que se acredita con el Registro de la Propiedad.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Marco normativo

- **Títulos ejecutivos**: sentencia firme, pero también el acuerdo de conciliación SMAC (art. 68 LRJS), la conciliación judicial y los laudos arbitrales firmes (art. 237 LRJS).
- **Plazo para instar la ejecución** (art. 243 LRJS): igual al fijado en las leyes sustantivas para el ejercicio de la acción — regla general 1 año en cantidad (art. 59.2 ET).
- **Ejecución dineraria general**: arts. 237-277 LRJS (despacho de ejecución, embargo, subasta — remisión supletoria a la LEC en lo no regulado). Contra el auto que resuelve la solicitud de ejecución cabe reposición (art. 239.4 LRJS; plazo de 3 días, art. 187).
- **Insolvencia empresarial**: audiencia al FOGASA antes de la declaración de insolvencia (art. 276 LRJS); la declaración abre la vía de las prestaciones de garantía salarial del art. 33 ET — informar al cliente.
- **Ejecución específica de sentencias de despido**: arts. 278-286 LRJS. Si el empresario opta por la readmisión y no la cumple o la cumple irregularmente, cabe instar el **incidente de no readmisión**: solicitud dentro de los **20 días** siguientes según el supuesto (art. 279.1) y, en todo caso, dentro de los **3 meses** desde la firmeza de la sentencia (art. 279.2 — plazos de prescripción). Tras la comparecencia (art. 280), el auto puede declarar **extinguida la relación laboral** con la indemnización del art. 56 ET —eventualmente incrementada (art. 281.2.c)— y los salarios dejados de percibir.
- **Ejecución provisional de sentencias de despido recurridas** (arts. 297-302 LRJS): mientras se resuelve la suplicación/casación, el trabajador tiene derecho a percibir la misma retribución siguiendo a disposición del empresario (o a que se le mantenga en ocupación efectiva), a elección del empresario.
- Los plazos de ejecución de despido son modalidad urgente: **agosto es hábil** (art. 43.4 LRJS, incluida ejecución).

## Fase 1 — Datos a recabar

- Sentencia o auto firme que se pretende ejecutar (o sentencia recurrida, si es ejecución provisional).
- Si es ejecución dineraria: importe líquido reclamado, si hay bienes conocidos del ejecutado.
- Si es ejecución de despido: opción ejercitada por la empresa (readmisión/indemnización), si se ha cumplido o no, fecha en que debía producirse la readmisión.

## Fase 2 — Batería de preguntas

- ¿Qué tipo de título? sentencia firme / avenencia SMAC incumplida / conciliación judicial.
- ¿Qué tipo de ejecución? dineraria / despido (readmisión incumplida) / provisional.
- Si es incidente de no readmisión: ¿se ha producido readmisión irregular (distintas condiciones) o ausencia total de readmisión? ¿Estamos dentro de los 20 días / 3 meses del art. 279?
- Cuantía exacta si es dineraria, y si se conocen bienes del ejecutado.
- ¿Riesgo de insolvencia? — anticipar al cliente la vía FOGASA (art. 33 ET) y sus topes.

## Fase 3 — Estructura del escrito

1. Encabezamiento: Juzgado de lo Social / Sección de lo Social del Tribunal de Instancia que dictó la resolución (art. 237.2 LRJS: la ejecución corresponde al órgano que conoció del asunto en instancia), identificación de las partes (marcadores genéricos).
2. Exposición del título ejecutivo (sentencia firme / acta de conciliación, fecha) y, si aplica, incumplimiento concreto de la readmisión.
3. Fundamento: artículos LRJS aplicables según el tipo de ejecución (dineraria: 239 ss.; despido: 278 ss.; provisional: 297 ss.).
4. **SUPLICO**: despachar ejecución por la cantidad líquida (principal + 10% de interés de mora del art. 29.3 ET si es salarial + presupuesto para intereses y costas) / convocar la comparecencia del art. 280 y declarar extinguida la relación laboral con condena a indemnización y salarios dejados de percibir, según proceda.

## Fase 4 — Entrega

Word (.docx). Pulir con `/estilo-escritos-judiciales`.
