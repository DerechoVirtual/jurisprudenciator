---
name: indice
description: "Índice de los 49 formularios de instrucción y procedimiento penal (competencia y declinatoria, diligencias previas, habeas corpus, declaraciones telemáticas, intérprete, aceptación por decreto). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Instrucción y procedimiento penal: índice de formularios

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

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/instruccion-y-procedimiento-penal:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Conformidad (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 52 | Procedimiento común: calificación del Fiscal y la acusación particular con conformidad del acusado | 2025 | `procedimiento-comun-calificacion-fiscal-acusacion-52` |
| 95 | Conformidad en el juicio oral con discrepancia en lo civil: calificación conjunta | 2023 | `conformidad-juicio-oral-discrepancia-lo-civil-95` |
| 697 | Procedimiento abreviado: defensa conforme con la acusación salvo en la responsabilidad civil | 2017 | `procedimiento-abreviado-defensa-conforme-acusacion-salvo-697` |

## Querellas y denuncias (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 69 | Ampliar la denuncia contra un nuevo denunciado | 2024 | `ampliar-denuncia-contra-nuevo-denunciado-69` |

## Escritos de defensa (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 433 | Administración responsable civil subsidiaria: escrito de defensa | 2020 | `administracion-responsable-civil-subsidiaria-escrito-433` |

## Medidas cautelares y protección (4)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 128 | Habeas corpus: solicitud del abogado de la persona privada de libertad | 2023 | `habeas-corpus-solicitud-abogado-persona-privada-libertad-128` |
| 166 | Cambiar la prisión provisional por internamiento en centro de deshabituación | 2022 | `cambiar-prision-provisional-internamiento-centro-166` |
| 477 | Pedir la rebaja de la fianza por responsabilidad civil | 2019 | `pedir-rebaja-fianza-responsabilidad-civil-477` |
| 478 | Pedir la rebaja de la fianza para eludir la prisión provisional | 2019 | `pedir-rebaja-fianza-eludir-prision-provisional-478` |

## Resoluciones, actas y documentos (3)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 38 | Delitos cometidos en el extranjero: auto de archivo por falta de jurisdicción | 2025 | `delitos-cometidos-extranjero-auto-archivo-falta-38` |
| 771 | Aceptación de decreto: decreto del fiscal con la propuesta de pena | 2016 | `aceptacion-decreto-decreto-fiscal-propuesta-pena-771` |
| 772 | Aceptación de decreto: comparecencia del encausado ante el juez | 2016 | `aceptacion-decreto-comparecencia-encausado-ante-juez-772` |

## Solicitudes y escritos de trámite (37)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 25 | Pedir la acumulación de procesos penales seguidos ante el mismo órgano | 2026 | `pedir-acumulacion-procesos-penales-seguidos-ante-mismo-25` |
| 62 | Abogado con discapacidad: pedir que se adapte la sala de vistas para el juicio o la actuación | 2024 | `abogado-discapacidad-pedir-adapte-sala-vistas-juicio-62` |
| 63 | Información del abogado al cliente sobre la gravedad del conflicto y estrategia (art. 6 LO 5/2024) | 2024 | `informacion-abogado-cliente-sobre-gravedad-conflicto-63` |
| 67 | Pedir que se repita una declaración en instrucción por privar al letrado de su libertad de expresión | 2024 | `pedir-repita-declaracion-instruccion-privar-letrado-67` |
| 71 | Investigado o acusado: pedir declarar por vía telemática (desde el 20 de marzo de 2024) | 2024 | `investigado-acusado-pedir-declarar-via-telematica-desde-71` |
| 72 | Testigo enfermo o lesionado: declarar por vía telemática desde casa (desde el 20 de marzo de 2024) | 2024 | `testigo-enfermo-lesionado-declarar-via-telematica-desde-72` |
| 73 | Pedir que testigo o perito declaren en persona en el juicio oral (desde el 20 de marzo de 2024) | 2024 | `pedir-testigo-perito-declaren-persona-juicio-oral-desde-73` |
| 74 | Pedir que testigo o perito declaren por vía telemática (desde el 20 de marzo de 2024) | 2024 | `pedir-testigo-perito-declaren-via-telematica-desde-20-74` |
| 75 | Acusado: pedir estar presente físicamente en los juicios (desde el 20 de marzo de 2024) | 2024 | `acusado-pedir-estar-presente-fisicamente-juicios-desde-75` |
| 76 | Pedir que el acusado declare en último lugar en la práctica de la prueba | 2024 | `pedir-acusado-declare-ultimo-lugar-practica-prueba-76` |
| 78 | Acusado: comparecencia telemática por justa causa o fuerza mayor (desde el 20 de marzo de 2024) | 2024 | `acusado-comparecencia-telematica-justa-causa-fuerza-78` |
| 116 | Abreviado: el investigado pide el sobreseimiento tras diligencias complementarias | 2023 | `abreviado-investigado-pide-sobreseimiento-tras-116` |
| 117 | Pedir la reapertura de diligencias previas archivadas | 2023 | `pedir-reapertura-diligencias-previas-archivadas-117` |
| 119 | Pedir que las diligencias previas pasen a juicio por delito leve | 2023 | `pedir-diligencias-previas-pasen-juicio-delito-leve-119` |
| 120 | Investigado: pedir diligencias de prueba en las diligencias previas | 2023 | `investigado-pedir-diligencias-prueba-diligencias-previas-120` |
| 122 | Denunciante: pedir que se notifique el auto que inadmite la denuncia | 2023 | `denunciante-pedir-notifique-auto-inadmite-denuncia-122` |
| 130 | Abogado del detenido: pedir a la policía diligencias inmediatas | 2023 | `abogado-detenido-pedir-policia-diligencias-inmediatas-130` |
| 141 | Comparecencias periódicas ante el juez: pedir su suspensión o una ampliación temporal | 2023 | `comparecencias-periodicas-ante-juez-pedir-suspension-141` |
| 230 | Declinatoria por falta de jurisdicción | 2022 | `declinatoria-falta-jurisdiccion-230` |
| 231 | Declinatoria por falta de competencia objetiva por razón de la materia | 2022 | `declinatoria-falta-competencia-objetiva-razon-materia-231` |
| 232 | Pedir que se reclamen las actuaciones al órgano jerárquicamente inferior | 2022 | `pedir-reclamen-actuaciones-organo-jerarquicamente-232` |
| 233 | Declinatoria por falta de competencia territorial | 2022 | `declinatoria-falta-competencia-territorial-233` |
| 234 | Acumular causas penales conexas y pedir la inhibición a la Sección competente | 2022 | `acumular-causas-penales-conexas-pedir-inhibicion-seccion-234` |
| 236 | Revocar la renuncia a la acción civil en el proceso penal | 2022 | `revocar-renuncia-accion-civil-proceso-penal-236` |
| 357 | Procedimiento ordinario: pedir la nulidad de actuaciones judiciales | 2021 | `procedimiento-ordinario-pedir-nulidad-actuaciones-357` |
| 420 | Abogado: intervenir por videoconferencia en el juicio penal (desde el 20 de marzo de 2024) | 2020 | `abogado-intervenir-videoconferencia-juicio-penal-desde-420` |
| 422 | Abogado: intervenir por videoconferencia en juicio penal telemático (hasta el 19 de marzo de 2024) | 2020 | `abogado-intervenir-videoconferencia-juicio-penal-422` |
| 487 | Oponerse a la prórroga de la instrucción | 2019 | `oponerse-prorroga-instruccion-487` |
| 518 | Reclamar los honorarios del letrado en un procedimiento penal (jura de cuentas) | 2019 | `reclamar-honorarios-letrado-procedimiento-penal-jura-518` |
| 741 | Repetir la declaración del investigado por no haber tenido traductor o intérprete | 2016 | `repetir-declaracion-investigado-no-haber-tenido-741` |
| 743 | Pedir traductor o intérprete para el investigado o acusado | 2016 | `pedir-traductor-interprete-investigado-acusado-743` |
| 744 | Pedir la presencia física del intérprete (defensa del investigado o acusado) | 2016 | `pedir-presencia-fisica-interprete-defensa-investigado-744` |
| 745 | Pedir que se compruebe la exactitud de la traducción o interpretación (defensa del investigado) | 2016 | `pedir-compruebe-exactitud-traduccion-interpretacion-745` |
| 746 | Renunciar al derecho a traductor e intérprete (investigado o acusado) | 2016 | `renunciar-derecho-traductor-e-interprete-investigado-746` |
| 757 | Pedir que se determine la edad del encausado extranjero | 2016 | `pedir-determine-edad-encausado-extranjero-757` |
| 758 | Pedir diligencias para determinar la edad del encausado | 2016 | `pedir-diligencias-determinar-edad-encausado-758` |
| 803 | Defensa: pedir que se tramite por el proceso por aceptación de decreto | 2016 | `defensa-pedir-tramite-proceso-aceptacion-decreto-803` |
