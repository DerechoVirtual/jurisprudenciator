---
name: acuerdo-representacion-trabajadores-sobre-medidas-118
description: "Redacta el escrito «Acuerdo con la representación de los trabajadores sobre medidas de igualdad LGTBI» (formulario 118 de igualdad y acoso laboral, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Acuerdo con la representación de los trabajadores sobre medidas de igualdad LGTBI

> Formulario 0118 del plugin **Igualdad y acoso laboral** · revisado el 17-11-2026. Uso interno.

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Convenio colectivo aplicable** (salario, jornada, categorías, faltas y sanciones) → `buscar_convenio` → `leer_convenio`; si sigue vigente o está denunciado, `vigencia_convenio`.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Antes de usarlo: avisos de la revisión

El planteamiento del formulario está desfasado en algo. Corrígelo antes de redactar:

- Medidas LGTBI: obligatorias en empresas de más de 50 personas trabajadoras (art. 15 Ley 4/2023) y desarrolladas por el RD 1026/2024 (BOE-A-2024-20402); el Estatuto de la Autoridad Independiente para la Igualdad de Trato se aprobó por RD 606/2026 (BOE-A-2026-16172).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] NOMBRE Y APELLIDOS (5 veces)
- [ ] Otros 5 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…ocolo frente al acoso y la violencia. En»; «…, en su calidad de»; «…de la Empresa»; «… legales de las personas trabajadoras de»; «… de negociación, ACUERDAN Que la empresa»

## Párrafos opcionales (31)

Inclúyelos solo si encajan en los hechos:

- D./Dña. [NOMBRE Y APELLIDOS]…
- CLÁUSULAS DE IGUALDAD DE TRATO Y NO DISCRIMINACIÓN…
- ACCESO AL EMPLEO…
- Formar, capacitar y sensibilizar a los profesionales encargados de los procesos de selección…
- Planificación, diseño y ejecución de los procesos de selección garantizando la eliminación de sesgos…
- CLASIFICACIÓN Y PROMOCIÓN PROFESIONAL…
- Diseño de estrategias para la eliminación de sesgos inconscientes en la evaluación de personas para su promoci…
- Diseño de políticas de mantenimiento del empleo de las personas LGTBI…
- FORMACIÓN, SENSIBILIZACIÓN y LENGUAJE…
- OBJETIVO: Sensibilizar sobre diversidad e inclusión LGTBI…
- Encuesta anual sobre diversidad…
- Creación de un Grupo de trabajo de sensibilización y mediación…
- Conmemoración de los días significativos en relación al colectivo LGTBI…
- Código de vestimenta flexible…
- Aseos sin género…
- OBJETIVO: Formar sobre diversidad e inclusión LGTBI…
- OBJETIVO: Utilización de un lenguaje respetuoso con la diversidad…
- ENTORNOS LABORALES DIVERSOS, SEGUROS E INCLUSIVOS…
- Redacción y revisión periódica del Protocolo de actuación para la atención del acoso o la violencia contra las…
- Creación de un canal de atención específica y confidencial al colectivo…
- Asesoramiento y consulta ante situaciones de acoso o violencia contra personas LGTBI…
- ENTORNOS LABORALES DIVERSOS, SEGUROS E INCLUSIVOS…
- Incluir la LGTBIfobia como riesgo psicosocial…
- Prohibir los reconocimientos médicos que tengan carácter discriminatorio…
- PERMISOS Y BENEFICIOS SOCIALES…
- OBJETIVO: Garantizar el disfrute de permisos y beneficios sociales atendiendo a la realidad de las familias di…
- OBJETIVO: Apoyar a las personas en proceso de transición…
- Derecho a flexibilidad horaria para las personas que están en transición de género…
- Cambio de nombre de uso común de la persona trabajadora…
- RÉGIMEN DISCIPLINARIO…
- Y para que conste, firman el presente documento, por duplicado, en el lugar y fecha al inicio consignados.…

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- art. 15 de la Ley 4/2023
- artículo 15.1 de la Ley 4/2023
- artículo 15 de la Ley 4/2023
- Real Decreto 1026/2024
- Ley 3/2023

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
