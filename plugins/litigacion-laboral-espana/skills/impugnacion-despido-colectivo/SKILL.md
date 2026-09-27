---
name: impugnacion-despido-colectivo
description: >-
  Impugnacion del despido colectivo (art. 124 LRJS): demanda colectiva de los representantes de los trabajadores, demanda empresarial de "jactancia" y demanda individual del trabajador afectado (art. 124.13). Plazos de caducidad de 20 dias y reglas de nulidad. Usar con "despido colectivo", "ERE", "impugnar el ERE", "demanda 124 LRJS", "nos han extinguido los contratos por el art. 51 ET". Requisito previo: hay EXTINCIONES de contratos por la via del art. 51 ET. Si la medida colectiva no comporta extinciones y solo se discute la interpretacion o aplicacion de una norma, convenio o decision empresarial (incluida una MSCT colectiva), usar /conflicto-colectivo.
---

# Impugnación del despido colectivo (art. 124 LRJS)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Doctrina muy evolutiva (grupos de empresa, documentación exigible, buena fe negociadora, despido colectivo de hecho): verifica cada criterio antes de citarlo** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"` y `base="AN"`, `fecha_desde` reciente) + `leer_sentencias` (`parrafos=3`).
- **Umbrales y cómputo de las extinciones según el derecho de la Unión** → `buscar_sentencias` (`base="TJUE"`) y `buscar_articulo` (`ley="Directiva 98/59/CE"`).
- **Art. 51 ET y art. 124 LRJS en su redacción vigente; reglamento de los procedimientos de despido colectivo (RD 1483/2012)** → `buscar_articulo` y `buscar_boe` → `leer_boe`.
- **Empresa y grupo** (sociedades vinculadas, administradores comunes, concurso que exige autorización del juez) → `buscar_empresa_mercantil`, y `sumario_borme` o `novedades_boe` para actos societarios y edictos concursales recientes.
- **Prioridades de permanencia o criterios de selección pactados en el convenio** (vía individual) → `buscar_convenio` + `leer_convenio` (`buscar_en="prioridad de permanencia"`).
- **Revisión del borrador** → `verificar_escrito` con el texto completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Las tres vías — elegir la correcta ANTES de redactar

| Vía | Quién | Plazo | Órgano |
|---|---|---|---|
| **Colectiva** (art. 124.1-124.12) | Representantes legales o sindicales de los trabajadores | **Caducidad 20 días** desde el acuerdo del periodo de consultas o la notificación de la decisión (art. 124.6) | Sala de lo Social del TSJ o de la AN según el ámbito (arts. 7-8 LRJS) |
| **Empresarial** ("jactancia", art. 124.3) | El empresario, para que se declare ajustada a derecho su decisión, si nadie la impugnó | 20 días desde que expiró el plazo de la acción colectiva | La misma Sala |
| **Individual** (art. 124.13) | Cada trabajador afectado | Caducidad de 20 días, cuyo cómputo se ABRE: a) si no hubo impugnación colectiva, al expirar el plazo de aquélla; b) si la hubo, desde la firmeza de la sentencia colectiva o la conciliación judicial | Juzgado de lo Social / Sección de lo Social (modalidad de despido, arts. 120-123 LRJS) |

## Marco normativo (vía colectiva)

- **Motivos tasados** (art. 124.2): a) no concurrencia de la causa; b) omisión del periodo de consultas o de la documentación del art. 51.2 ET o del procedimiento del 51.7; c) fraude, dolo, coacción o abuso de derecho; d) vulneración de derechos fundamentales. Las prioridades de permanencia se ventilan SOLO en la vía individual.
- **Sin conciliación previa** (art. 124.5): exenta de las formas de evitación del proceso.
- **Si hubo acuerdo en consultas**: demandar también a los firmantes (art. 124.4).
- **Tramitación**: urgente, preferencia absoluta salvo tutela DDFF (art. 124.8); la empresa aporta en 5 días la documentación y actas del periodo de consultas (art. 124.9); juicio en única convocatoria dentro de los 15 días (art. 124.10); sentencia en 5 días, recurrible en **casación ordinaria** (art. 124.11).
- **Calificaciones** (art. 124.11): ajustada a derecho / no ajustada (causa no acreditada) / **nula** (omisión de consultas o documentación, falta de autorización del juez del concurso, o vulneración de DDFF) → reincorporación (art. 123.2-3 por remisión).
- **Suspensión de acciones individuales**: la demanda colectiva (y la empresarial) suspende el plazo de caducidad de la acción individual (art. 124.3 in fine); la sentencia colectiva firme tiene eficacia de cosa juzgada sobre los procesos individuales (art. 124.13.b.2ª).

## Marco normativo (vía individual, art. 124.13)

- Se tramita por la modalidad de despido (arts. 120-123 LRJS) con especialidades:
  - Demandar también a los trabajadores beneficiados si se discuten **prioridades de permanencia**.
  - Nulidad individual: incumplimiento de consultas/documentación (si no hubo proceso colectivo), no respeto de prioridades de permanencia, o causas generales del art. 122.2.
  - Si hubo sentencia colectiva: el objeto queda limitado a las cuestiones individuales no resueltas en ella.
- Verificar SIEMPRE el estado de la impugnación colectiva antes de computar la caducidad individual — es el error de plazo más peligroso de esta materia.

## Fase 1 — Documentación a pedir

- Comunicación de inicio del periodo de consultas y memoria/documentación entregada (art. 51.2 ET: causas, número y clasificación de afectados, criterios de selección...).
- Actas del periodo de consultas y acuerdo final o decisión empresarial.
- Comunicación a la autoridad laboral y su expediente (el órgano lo recabará, pero conviene tenerlo).
- Carta individual de despido (para la vía individual) con criterios de selección aplicados.
- Datos del ámbito (centros, plantilla, número de afectados) — determina umbral del art. 51.1 ET y órgano competente.

## Fase 2 — Batería de preguntas (AskUserQuestion)

- ¿Quién es el cliente? (comité/sindicato → colectiva; trabajador → individual; empresa → jactancia o defensa).
- ¿Fechas exactas?: fin de consultas / notificación de la decisión / carta individual → computar los 20 días de la vía que toque, con las reglas de apertura del 124.13.
- ¿Hubo acuerdo en consultas? (habrá que demandar a los firmantes y el fraude será más difícil de sostener).
- ¿Se discute la causa, el procedimiento, o las prioridades de permanencia? → determina vía y motivos.
- ¿El despido alcanza los umbrales del art. 51.1 ET o se está ante un "despido colectivo de hecho" troceado? (doctrina a verificar vía jurisprudenciator).
- ¿Ámbito del despido? (un centro / varias provincias / varias CCAA) → TSJ o AN.

## Fase 3 — Estructura del escrito (vía colectiva)

1. Encabezamiento: Sala de lo Social del TSJ/AN, representación demandante con acreditación de implantación (art. 124.1), empresa demandada (+ firmantes del acuerdo en su caso).
2. **HECHOS**: plantilla y ámbito → comunicación de inicio y documentación entregada (o sus déficits, uno a uno) → desarrollo del periodo de consultas → decisión final y su notificación → cómputo del plazo.
3. **FUNDAMENTOS DE DERECHO**: competencia (arts. 7-8 LRJS) → legitimación (art. 124.1) → motivo(s) del art. 124.2 desarrollados con la doctrina verificada (documentación esencial, buena fe negociadora, causas económicas/técnicas/organizativas/productivas del art. 51.1 ET).
4. **SUPLICO**: declaración de nulidad (con reincorporación) o de no ajustada a derecho, según el motivo.
5. **OTROSÍES**: prueba (documental sobre consultas, pericial económica, interrogatorio con apercibimiento 91.2 LRJS).

## Fase 4 — Verificación y entrega

- Plazo de caducidad recomputado y documentado en `_log.yaml`.
- Motivos alineados con la calificación pedida (la causa insuficiente NO da nulidad en la colectiva: da "no ajustada a derecho").
- Verificar doctrina con `buscar_por_cita` y `leer_sentencias` de Jurisprudenciator, y el borrador con `verificar_escrito`.
- Pulir con `/estilo-escritos-judiciales`. Entregar en Word (.docx).

---

**Nota de anonimización**: cualquier dato real de empresa, comité, sindicato o trabajadores presente en la plantilla de origen se sustituye por marcador genérico.
