---
name: alegaciones-acta-infraccion-trabajadores-289
description: "Redacta el escrito «Alegaciones al acta de infracción de trabajadores» (formulario 289 de inspección de trabajo y sanciones, revisado el 17-11-2026): pide los datos, decide las opciones, aplica las correcciones y comprueba las normas en el BOE. Requiere Jurisprudenciator."
---

# Alegaciones al acta de infracción de trabajadores

> Formulario 0289 del plugin **Inspección de Trabajo y sanciones** · revisado el 17-11-2026. Uso interno.

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

- Alegaciones: 15 días hábiles ante el órgano instructor (art. 17.1 RD 928/1998; art. 52.1.b LISOS). Si la sanción es solo pecuniaria, en el mismo plazo cabe pagar con reducción del 40 % renunciando a recursos (arts. 14.6 y 17.1). El expediente caduca a los 6 meses desde la fecha del acta hasta la notificación de la resolución (art. 20.3).
- Las infracciones del art. 17 LISOS (red. Ley 3/2023) se sancionan con suspensión de derechos del demandante 1/3/6 meses o exclusión de ayudas y formación (art. 47.2), no con multa; leves y graves corresponden al servicio público de empleo (art. 48.4).

## Qué tienes en esta carpeta

- `formulario.md`: el texto del formulario revisado, con las marcas de la revisión.
- `marco.md`: guía del tema con las reglas y plazos vigentes comprobados en el BOE.

## Datos que hay que pedir al usuario

Pídelos en una sola tanda. Si un dato aparece varias veces, aclara a qué persona o acto corresponde cada vez.

- [ ] ÓRGANO AL QUE SE DIRIGE
- [ ] NOMBRE Y APELLIDOS (2 veces)
- [ ] DNI/NIE
- [ ] DOMICILIO A EFECTOS DE NOTIFICACIONES
- [ ] FECHA (3 veces)
- [ ] NÚMERO
- [ ] IMPORTE (2 veces)
- [ ] DESCRIBIR
- [ ] Otros 8 datos sin etiqueta, marcados `[COMPLETAR]`. Su contexto en el formulario: «…LEVE por:»; «…ias del acuerdo de actividad. GRAVE por:»; «…al y como sucedieron son los siguientes:»; «…nfracción no son ciertos, por cuanto que»; «…n califica genéricamente los hechos como»; «…consistente en que se tome declaración a»; «…s escritos que se acompañan como números»; «… procedentes. Es de Justicia que pide en»

## Elecciones que hay que hacer

- en su propio nombre / en nombre de ..., cuya representación acredita conforme a la escritura de poder cuya copia acompaña
- 1 / 2 / 3
- personas trabajadoras / clientes

## Partes que tienes que redactar tú

El original solo traía los rótulos de estas opciones o varias alternativas seguidas. Redacta la que corresponda con la norma vigente y los hechos, y avísalo al entregar:

- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS
- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS
- ELEGIR UNA DE LAS ALTERNATIVAS QUE SIGUEN Y SUPRIMIR LAS DEMÁS
- ELEGIR UNA OPCIÓN Y REDACTARLA: No comparecer ante los servicios públicos de empleo o las agencias de colocación / No devolver el justificante de haber comparecido para cubrir las ofertas de empleo / No cumplir las exigencias del acuerdo de actividad / Rechazar una oferta de colocación adecuada / Negarse a participar en actividades para la mejora de la empleabilidad propuestas en el itinerario o p

## Párrafos opcionales (4)

Inclúyelos solo si encajan en los hechos:

- (Si no se refleja el nombre de los trabajadores en el acta)…
- (Si el acta se limita a calificar los hechos de forma genérica)…
- Testifical, consistente en que se tome declaración a [COMPLETAR], en cuanto [ELEGIR: personas trabajadoras / c…
- Documental, consistente en los escritos que se acompañan como números [COMPLETAR], consistentes en [DESCRIBIR]…

## Correcciones de la revisión (1)

El formulario lleva notas de revisión. Aplica lo que dicen y **quítalas** del escrito final.

## Normas que cita el formulario

Compruébalas **todas** con `buscar_articulo` antes de dejarlas en el escrito. Si una ha cambiado, usa la redacción vigente y dilo:

- artículo 17 de la LISOS
- art. 17 LISOS
- artículo 52.1.b) del Real Decreto Legislativo 5/2000
- artículo 17.1 del Real Decreto 928/1998
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
