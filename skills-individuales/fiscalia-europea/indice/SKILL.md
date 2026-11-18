---
name: indice
description: "Índice de los 31 formularios de procedimiento de la fiscalía europea (LO 9/2021, Fiscal Europeo Delegado, Juez de Garantías, diligencias, medidas cautelares, impugnación de decretos). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Procedimiento de la Fiscalía Europea: índice de formularios

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

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/fiscalia-europea:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 336 | Fiscalía Europea: el investigado pide declarar para reconocer los hechos y conformarse | 2021 | `fiscalia-europea-investigado-pide-declarar-reconocer-336` |

## Recursos e impugnaciones (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 337 | Fiscalía Europea: apelación contra resoluciones del Juez de Garantías | 2021 | `fiscalia-europea-apelacion-contra-resoluciones-juez-337` |
| 339 | Fiscalía Europea: impugnar decretos del Fiscal Europeo Delegado | 2021 | `fiscalia-europea-impugnar-decretos-fiscal-europeo-339` |
| 341 | Fiscalía Europea: oposición al recurso de apelación | 2021 | `fiscalia-europea-oposicion-recurso-apelacion-341` |

## Querellas y denuncias (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 321 | Fiscalía Europea: denuncia de un particular | 2021 | `fiscalia-europea-denuncia-particular-321` |
| 326 | Fiscalía Europea: querella de la acusación particular | 2021 | `fiscalia-europea-querella-acusacion-particular-326` |
| 328 | Fiscalía Europea: denuncia a través de abogado o procurador | 2021 | `fiscalia-europea-denuncia-traves-abogado-procurador-328` |

## Escritos de acusación (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 335 | Fiscalía Europea: escrito de acusación de la acusación particular | 2021 | `fiscalia-europea-escrito-acusacion-acusacion-particular-335` |

## Escritos de defensa (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 333 | Fiscalía Europea: escrito de defensa del responsable civil | 2021 | `fiscalia-europea-escrito-defensa-responsable-civil-333` |
| 334 | Fiscalía Europea: escrito de defensa de la persona acusada | 2021 | `fiscalia-europea-escrito-defensa-persona-acusada-334` |

## Medidas cautelares y protección (5)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 322 | Fiscalía Europea: pedir caución sustitutoria | 2021 | `fiscalia-europea-pedir-caucion-sustitutoria-322` |
| 323 | Fiscalía Europea: pedir que se amplíen las medidas cautelares reales | 2021 | `fiscalia-europea-pedir-amplien-medidas-cautelares-reales-323` |
| 349 | Fiscalía Europea: pedir medidas cautelares personales | 2021 | `fiscalia-europea-pedir-medidas-cautelares-personales-349` |
| 350 | Fiscalía Europea: pedir que se reduzcan las medidas cautelares reales | 2021 | `fiscalia-europea-pedir-reduzcan-medidas-cautelares-350` |
| 351 | Fiscalía Europea: pedir medidas cautelares reales | 2021 | `fiscalia-europea-pedir-medidas-cautelares-reales-351` |

## Solicitudes y escritos de trámite (16)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 324 | Fiscalía Europea: reclamación civil del actor civil | 2021 | `fiscalia-europea-reclamacion-civil-actor-civil-324` |
| 325 | Fiscalía Europea: pedir que se alce el secreto | 2021 | `fiscalia-europea-pedir-alce-secreto-325` |
| 327 | Fiscalía Europea: personación del actor civil | 2021 | `fiscalia-europea-personacion-actor-civil-327` |
| 329 | Fiscalía Europea: el investigado aporta elementos de descargo | 2021 | `fiscalia-europea-investigado-aporta-elementos-descargo-329` |
| 330 | Fiscalía Europea: la defensa pide asegurar fuentes de prueba | 2021 | `fiscalia-europea-defensa-pide-asegurar-fuentes-prueba-330` |
| 331 | Fiscalía Europea: la acusación particular pide asegurar con urgencia fuentes de prueba | 2021 | `fiscalia-europea-acusacion-particular-pide-asegurar-331` |
| 332 | Fiscalía Europea: la acusación particular pide asegurar fuentes de prueba | 2021 | `fiscalia-europea-acusacion-particular-pide-asegurar-332` |
| 338 | Fiscalía Europea: la acusación particular participa en los actos de investigación | 2021 | `fiscalia-europea-acusacion-particular-participa-actos-338` |
| 340 | Fiscalía Europea: el investigado participa en los actos de investigación | 2021 | `fiscalia-europea-investigado-participa-actos-340` |
| 342 | Fiscalía Europea: el investigado designa abogado | 2021 | `fiscalia-europea-investigado-designa-abogado-342` |
| 343 | Fiscalía Europea: el investigado designa procurador | 2021 | `fiscalia-europea-investigado-designa-procurador-343` |
| 344 | Fiscalía Europea: testimonios para la acusación particular o el actor civil en el juicio oral | 2021 | `fiscalia-europea-testimonios-acusacion-particular-actor-344` |
| 345 | Fiscalía Europea: testimonios para la defensa en el juicio oral | 2021 | `fiscalia-europea-testimonios-defensa-juicio-oral-345` |
| 346 | Fiscalía Europea: pedir diligencias de investigación que necesitan autorización judicial | 2021 | `fiscalia-europea-pedir-diligencias-investigacion-346` |
| 347 | Fiscalía Europea: el investigado pide diligencias de investigación | 2021 | `fiscalia-europea-investigado-pide-diligencias-347` |
| 348 | Fiscalía Europea: la acusación particular pide diligencias de investigación | 2021 | `fiscalia-europea-acusacion-particular-pide-diligencias-348` |
