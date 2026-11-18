---
name: indice
description: "Índice de los 20 formularios de medidas cautelares y diligencias preliminares (embargo preventivo, anotación preventiva, caución, diligencias preliminares). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Medidas cautelares y diligencias preliminares: índice de formularios

## Paso 0: Jurisprudenciator en esta skill (obligatorio)

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del escrito sale de ellas.

- **Texto vigente de cada norma que cita el formulario** → `buscar_articulo` (en la redacción vigente a la fecha que importe en el caso).
- **Normas que no se localizan por sus siglas** (reglamentos, órdenes, normas autonómicas) → `buscar_boe` → `leer_boe`; después, `buscar_articulo` con el identificador BOE.
- **Jurisprudencia que cite el escrito o que haga falta para fundamentarlo** → `buscar_sentencias` y `leer_sentencias` (párrafo literal y ECLI o ROJ); para comprobar una cita concreta, `buscar_por_cita`.
- **Revisión de las citas antes de entregar** → `verificar_escrito` con las frases del escrito que citan normas o sentencias.
- **Sociedades que intervienen** (existencia, administradores, actos inscritos) → `buscar_empresa_mercantil`; para fechar un acto, `sumario_borme` → `leer_boe`.
- **Inmuebles** (referencia catastral, superficie, uso) → `consultar_catastro` (y `callejero_catastro` para localizar la dirección).

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ, datos registrales o catastrales, convenio…).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no rellenes el formulario y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta (en Claude Code, con `/mcp`).
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, una sentencia aplicable, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato, búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas pendientes de verificar. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Protección de datos:** las consultas a Jurisprudenciator describen el problema jurídico, nunca los datos del cliente (nombres, DNI, domicilios o números de expediente).

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/cautelares-y-diligencias-preliminares:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Contestaciones, oposiciones y alegaciones (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1399 | Oposición a diligencias preliminares de propiedad horizontal | 2013 | `oposicion-diligencias-preliminares-propiedad-horizontal-1399` |
| 1484 | Oposición a medidas cautelares acordadas por arbitraje pendiente sin audiencia del demandado | 2014 | `oposicion-medidas-cautelares-acordadas-arbitraje-1484` |

## Solicitudes y expedientes (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 187 | Devolución de la caución prestada en diligencias preliminares | 2021 | `devolucion-caucion-prestada-diligencias-preliminares-187` |
| 512 | Medida cautelar previa a la demanda: acceso a vivienda o local | 2016 | `medida-cautelar-previa-demanda-acceso-vivienda-local-512` |
| 1040 | Medidas cautelares (general) | 2013 | `medidas-cautelares-general-1040` |
| 1100 | Alzamiento de medidas cautelares por no presentar la demanda en plazo | 2013 | `alzamiento-medidas-cautelares-no-presentar-demanda-plazo-1100` |
| 1107 | Medida cautelar con el proceso iniciado (general) | 2013 | `medida-cautelar-proceso-iniciado-general-1107` |
| 1401 | Abono de gastos de diligencias preliminares de propiedad horizontal | 2013 | `abono-gastos-diligencias-preliminares-propiedad-1401` |
| 1494 | Prórroga de anotación preventiva de demanda | 2014 | `prorroga-anotacion-preventiva-demanda-1494` |

## Escritos de trámite (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 168 | Otrosí de medidas cautelares del art. 727 LEC: inventario y administrador judicial | 2021 | `otrosi-medidas-cautelares-art-727-lec-inventario-168` |
| 634 | Impugnación de la oposición a las diligencias preliminares | 2015 | `impugnacion-oposicion-diligencias-preliminares-634` |
| 1038 | Otrosí: caución | 2013 | `otrosi-caucion-1038` |

## Actos y resoluciones de la Administración o del órgano judicial (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 1373 | Diligencias preliminares de propiedad horizontal para exhibir documentos de la comunidad | 2013 | `diligencias-preliminares-propiedad-horizontal-exhibir-1373` |

## Otros (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 981 | Caución en sustitución de la medida de aseguramiento | 2013 | `caucion-sustitucion-medida-aseguramiento-981` |
| 1022 | Audiencia de las partes sobre la caución en tercería de dominio | 2013 | `audiencia-partes-sobre-caucion-terceria-dominio-1022` |
| 1054 | Caución ofrecida en sustitución de medidas (general) | 2013 | `caucion-ofrecida-sustitucion-medidas-general-1054` |
| 1106 | Medida cautelar de depósito de cosa mueble con la demanda | 2013 | `medida-cautelar-deposito-cosa-mueble-demanda-1106` |
| 1110 | Caución prestada por el demandante | 2013 | `caucion-prestada-demandante-1110` |
| 1340 | Fijación de caución en diligencias preliminares de propiedad horizontal | 2013 | `fijacion-caucion-diligencias-preliminares-propiedad-1340` |
| 1400 | Pérdida de la caución de diligencias preliminares por no presentar la demanda | 2013 | `perdida-caucion-diligencias-preliminares-no-presentar-1400` |
