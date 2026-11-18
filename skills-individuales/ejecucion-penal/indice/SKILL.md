---
name: indice
description: "Índice de los 16 formularios de ejecución penal (liquidación de condena, suspensión de la pena, prescripción, refundición, libertad vigilada, decomiso). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Ejecución penal: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/ejecucion-penal:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Recursos e impugnaciones (8)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 51 | Ejecutoria penal: impugnar la liquidación de condena hecha por el LAJ | 2025 | `ejecutoria-penal-impugnar-liquidacion-condena-hecha-laj-51` |
| 55 | Ejecutoria penal: súplica contra el auto que resuelve alegaciones | 2025 | `ejecutoria-penal-suplica-contra-auto-resuelve-55` |
| 56 | Ejecutoria penal: reforma y subsidiario de apelación contra el auto que resuelve alegaciones | 2025 | `ejecutoria-penal-reforma-subsidiario-apelacion-contra-56` |
| 100 | Suspensión de pena denegada: apelación pidiendo la excepcional (hasta el 2 de abril de 2025) | 2023 | `suspension-pena-denegada-apelacion-pidiendo-excepcional-100` |
| 557 | Refundición de condenas: interponer recurso de casación | 2018 | `refundicion-condenas-interponer-recurso-casacion-557` |
| 561 | Refundición de condenas: preparar la casación por infracción de ley | 2018 | `refundicion-condenas-preparar-casacion-infraccion-ley-561` |
| 755 | Decomiso autónomo: apelación del tercero contra la sentencia condenatoria | 2016 | `decomiso-autonomo-apelacion-tercero-contra-sentencia-755` |
| 760 | Decomiso en el proceso penal: apelación del tercero afectado contra la condena | 2016 | `decomiso-proceso-penal-apelacion-tercero-afectado-contra-760` |

## Escritos de defensa (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 58 | Ejecutoria penal: alegaciones de la defensa del condenado | 2025 | `ejecutoria-penal-alegaciones-defensa-condenado-58` |

## Solicitudes y escritos de trámite (6)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 142 | Pedir la revisión de la condena por retroactividad de la norma penal más favorable | 2023 | `pedir-revision-condena-retroactividad-norma-penal-mas-142` |
| 168 | Impago de multa: suspender la responsabilidad personal subsidiaria (hasta el 2 de abril de 2025) | 2022 | `impago-multa-suspender-responsabilidad-personal-168` |
| 384 | Prescripción de la pena: petición del penado (hasta el 2 de abril de 2025) | 2021 | `prescripcion-pena-peticion-penado-hasta-2-abril-2025-384` |
| 756 | Decomiso autónomo: designar bienes para decomisar | 2016 | `decomiso-autonomo-designar-bienes-decomisar-756` |
| 759 | Pedir la modificación de la libertad vigilada | 2016 | `pedir-modificacion-libertad-vigilada-759` |
| 761 | Decomiso de bienes: pedir que se llame al proceso penal al tercero afectado | 2016 | `decomiso-bienes-pedir-llame-proceso-penal-tercero-761` |

## Otros (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 762 | Decomiso: contestación a la demanda por tercero rebelde o que no pudo oponerse | 2016 | `decomiso-contestacion-demanda-tercero-rebelde-no-pudo-762` |
