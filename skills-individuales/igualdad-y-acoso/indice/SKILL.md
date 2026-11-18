---
name: indice
description: "Índice de los 35 formularios de igualdad y acoso laboral (plan de igualdad, comisión negociadora, protocolo de acoso, LGTBI, canal de denuncias). Úsala cuando el usuario pida un escrito de esta materia y no esté claro qué formulario usar: elige la skill del formulario adecuado. Requiere Jurisprudenciator."
---

# Igualdad y acoso laboral: índice de formularios

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

## Cómo elegir

Busca por tipo de documento y título. Cada formulario es una skill de este plugin (`/igualdad-y-acoso:<skill>`). Si dudas entre dos, elige el más reciente o el que mejor encaje con los hechos y dilo; si la petición es ambigua, propón al usuario los dos o tres formularios que mejor encajan y pregúntale cuál quiere. Las reglas del tema están en `marco.md`.

## Cómo usar el formulario elegido

Invoca su skill. Si esa skill no aparece en tu lista de skills disponibles (puede pasar cuando hay muchas skills instaladas), lee directamente su fichero `SKILL.md`: está en `skills/<skill>/SKILL.md` dentro de este plugin, en la carpeta hermana de la de esta skill `indice` (`../<skill>/SKILL.md`). Síguelo igual que si la hubieras invocado, con su `formulario.md` y su `marco.md`.

## Contratos, cláusulas y anexos (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 219 | Compromiso con el plan de igualdad en el convenio colectivo: cláusula | 2019 | `compromiso-plan-igualdad-convenio-colectivo-clausula-219` |

## Cartas y comunicaciones a la plantilla (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 95 | Aviso a la plantilla de la implantación del canal de denuncias | 2023 | `aviso-plantilla-implantacion-canal-denuncias-95` |
| 161 | Carta para constituir la comisión negociadora del plan de igualdad | 2021 | `carta-constituir-comision-negociadora-plan-igualdad-161` |
| 206 | Criterios de selección de la empresa usuaria: comunicación a la empresa externa | 2019 | `criterios-seleccion-empresa-usuaria-comunicacion-empresa-206` |
| 212 | Reunión con perspectiva de igualdad: convocatoria | 2019 | `reunion-perspectiva-igualdad-convocatoria-212` |
| 213 | Aviso a la plantilla del inicio del Plan de Igualdad | 2019 | `aviso-plantilla-inicio-plan-igualdad-213` |
| 214 | Compromiso de la empresa con la igualdad: carta | 2019 | `compromiso-empresa-igualdad-carta-214` |
| 316 | Sanción por acoso: carta | 2017 | `sancion-acoso-carta-316` |

## Demandas, papeletas y reclamaciones previas (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 162 | Acoso laboral (mobbing): demanda por infracción de la normativa de prevención | 2021 | `acoso-laboral-mobbing-demanda-infraccion-normativa-162` |

## Escritos y solicitudes (2)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 165 | Autorizar los trámites de inscripción del plan de igualdad o del protocolo de acoso | 2021 | `autorizar-tramites-inscripcion-plan-igualdad-protocolo-165` |
| 217 | Denuncia de acoso sexual o por razón de sexo | 2019 | `denuncia-acoso-sexual-razon-sexo-217` |

## Expediente disciplinario (1)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 326 | Cargos por acoso sexual: pliego | 2017 | `cargos-acoso-sexual-pliego-326` |

## Actas, acuerdos, planes y protocolos (16)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 54 | Impulso por la empresa de la negociación del plan de igualdad o del plan LGTBI | 2023 | `impulso-empresa-negociacion-plan-igualdad-plan-lgtbi-54` |
| 108 | Protocolo contra el acoso y la violencia hacia personas LGTBI | 2023 | `protocolo-contra-acoso-violencia-hacia-personas-lgtbi-108` |
| 118 | Acuerdo con la representación de los trabajadores sobre medidas de igualdad LGTBI | 2023 | `acuerdo-representacion-trabajadores-sobre-medidas-118` |
| 136 | Reglamento de la Comisión de seguimiento y evaluación | 2022 | `reglamento-comision-seguimiento-evaluacion-136` |
| 141 | Acta de reunión de la Comisión de seguimiento del Plan de Igualdad | 2022 | `acta-reunion-comision-seguimiento-plan-igualdad-141` |
| 146 | Acta de constitución de la Comisión de seguimiento del plan de igualdad o plan LGTBI | 2022 | `acta-constitucion-comision-seguimiento-plan-igualdad-146` |
| 158 | Acta de aprobación del protocolo contra el acoso sexual o por razón de sexo | 2021 | `acta-aprobacion-protocolo-contra-acoso-sexual-razon-sexo-158` |
| 160 | Diagnóstico del Plan de Igualdad: acta de aprobación | 2021 | `diagnostico-plan-igualdad-acta-aprobacion-160` |
| 164 | Acta de aprobación del plan de igualdad o del plan LGTBI | 2021 | `acta-aprobacion-plan-igualdad-plan-lgtbi-164` |
| 177 | Impulso por la representación de los trabajadores de la negociación del plan de igualdad | 2020 | `impulso-representacion-trabajadores-negociacion-plan-177` |
| 208 | Compromisos de la organización en selección y promoción | 2019 | `compromisos-organizacion-seleccion-promocion-208` |
| 209 | Comisión negociadora del plan de igualdad: acta de reunión | 2019 | `comision-negociadora-plan-igualdad-acta-reunion-209` |
| 211 | Acta de constitución de la comisión negociadora del plan de igualdad o plan LGTBI | 2019 | `acta-constitucion-comision-negociadora-plan-igualdad-211` |
| 215 | Compromiso de la organización contra el acoso sexual y por razón de sexo | 2019 | `compromiso-organizacion-contra-acoso-sexual-razon-sexo-215` |
| 216 | Protocolo contra el acoso sexual y por razón de sexo en el trabajo | 2019 | `protocolo-contra-acoso-sexual-razon-sexo-trabajo-216` |
| 220 | Confidencialidad en la tramitación de denuncias de acoso: compromiso | 2019 | `confidencialidad-tramitacion-denuncias-acoso-compromiso-220` |

## Documentos, certificados y modelos oficiales (7)

| Nº | Formulario | Año | Skill |
|---|---|---|---|
| 50 | Evaluación del Plan de Igualdad: informe |  | `evaluacion-plan-igualdad-informe-50` |
| 51 | Evaluación para la comisión de seguimiento: cuestionario | 2023 | `evaluacion-comision-seguimiento-cuestionario-51` |
| 52 | Cuestionario de evaluación del plan dirigido a la plantilla | 2023 | `cuestionario-evaluacion-plan-dirigido-plantilla-52` |
| 53 | Cuestionario de evaluación dirigido a la dirección | 2023 | `cuestionario-evaluacion-dirigido-direccion-53` |
| 169 | Plan de igualdad: hoja estadística | 2021 | `plan-igualdad-hoja-estadistica-169` |
| 203 | Cuestionario de igualdad para la plantilla | 2020 | `cuestionario-igualdad-plantilla-203` |
| 205 | Cuestionario de igualdad para la dirección | 2019 | `cuestionario-igualdad-direccion-205` |
