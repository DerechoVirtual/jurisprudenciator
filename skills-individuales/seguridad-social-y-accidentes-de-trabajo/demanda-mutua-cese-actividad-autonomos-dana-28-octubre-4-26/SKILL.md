---
name: demanda-mutua-cese-actividad-autonomos-dana-28-octubre-4-26
description: "Redacta el escrito «Demanda a la Mutua por cese de actividad de autónomos por la DANA (28 octubre a 4 noviembre de 2024)» (formulario 26 de seguridad social y accidentes de trabajo, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Demanda a la Mutua por cese de actividad de autónomos por la DANA (28 octubre a 4 noviembre de 2024)

> Formulario 0026 del plugin **Seguridad Social y accidentes de trabajo** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Antes de usarlo: avisos de la revisión

El planteamiento del formulario está desfasado en algo. Corrígelo antes de redactar:

- Art. 24.4 RDL 6/2024: la prestación extraordinaria podía extenderse hasta el 31-1-2025; después, la ordinaria del art. 331.1.b).
- Cese de actividad: la reclamación previa ante el órgano gestor es potestativa (art. 350.1 LGSS); si resolvió una mutua, informa una comisión paritaria (art. 350.2).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] SEDE
- [ ] NOMBRE Y APELLIDOS (2 veces)
- [ ] DNI/NIE
- [ ] LOCALIDAD (2 veces)
- [ ] TELÉFONO
- [ ] ACTO O RESOLUCIÓN (2 veces)
- [ ] NÚMERO (2 veces)
- [ ] FECHA (8 veces)
- [ ] IMPORTE (3 veces)
- [ ] Nº DE EXPEDIENTE
- [ ] LUGAR
- [ ] Otros 14 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…, asistido/a por el/la Letrado/a»; «…zco y como mejor proceda en Derecho DIGO»; «…Que he estado realizando la actividad de»; «…desde»; «…desde [COMPLETAR] hasta»; «…como consecuencia de la DANA acaecida en»; «…los días»; «…solicité a la Mutua»; «…, notificada el»; «… Niveles Altos (DANA) en el municipio de»; «…de»; «…e de mi actividad por fuerza mayor desde»; …

## Elecciones que hay que hacer

- parcialmente / totalmente
- temporal / definitiva
- Resolución / Acuerdo

## Párrafos opcionales (4)

Inclúyelos solo si encajan en los hechos:

- que no he acreditado la imposibilidad para desarrollar la actividad…
- que no he acreditado el período mínimo de cotización establecido en el art. 338 de la LGSS…
- no es necesaria la aportación de documentos que acrediten la existencia de fuerza mayor…
- en estos casos se considerará cumplido el requisito de período mínimo de cotización de doce meses comprendidos…

## Correcciones de la revisión (3)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- art. 2.o) de la LJS
- arts. 327 a 350 de la LGSS
- art. 331.1.b) de la LGSS
- art. 338 de la LGSS
- artículos 1, 2, 6 y 10 de la Ley 36/2011
- Ley 6/2024
- Real Decreto-ley 6/2024

## Flujo

1. **Paso 0**: comprueba Jurisprudenciator (arriba).
2. Lee `formulario.md` entero, con su cabecera, y la parte de `marco.md` que afecte al caso (plazos, órgano, procedimiento, conciliación o mediación previa, reclamación previa o vía administrativa, según el caso).
3. Pide los datos de la lista. Lo que el usuario no sepa se queda como hueco visible.
4. Decide las elecciones y los párrafos opcionales según los hechos. Redacta las partes que el original no traía.
5. Aplica los avisos y las notas de revisión. Comprueba con `buscar_articulo` cada norma citada y, si citas jurisprudencia, localízala con `buscar_sentencias` o `buscar_por_cita` y léela con `leer_sentencias`.
6. Indica el plazo y el cauce: desde cuándo cuenta, cuándo vence y ante qué órgano se presenta.
7. Antes de entregarlo, pasa `verificar_escrito` con las frases del escrito que citan normas o sentencias y corrige lo que señale.
8. Entrega el escrito en **Word (.docx)** con formato de escrito (usa la skill de Word disponible) y, si es corto, también en el chat.
9. Cierra con: datos pendientes, partes redactadas por ti, normas y sentencias comprobadas con Jurisprudenciator y, si algún dato sale de internet, cuál es y su enlace.
