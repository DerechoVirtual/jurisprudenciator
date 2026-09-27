---
name: recurso-casacion-unificacion-doctrina
description: >-
  Redaccion del recurso de casacion para la unificacion de doctrina CONTRA sentencias de suplicacion del TSJ, ante la Sala de lo Social del Tribunal Supremo, incluida la relacion precisa de contradicciones entre sentencias. Basada en plantilla real del despacho, anonimizada. Usar con "casacion unificacion doctrina", "RCUD", "recurso contra la sentencia de suplicacion del TSJ", "contradiccion de sentencias", "sentencia de contraste". Requisito previo: existe sentencia del TSJ dictada EN SUPLICACION y una sentencia de contraste firme (art. 219 LRJS). Si la sentencia que se quiere recurrir es la del Juzgado de lo Social, usar /recurso-suplicacion.
---

# Recurso de casación para la unificación de doctrina (RCUD)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Localizar la sentencia de contraste** (Sala Cuarta u otra Sala de lo Social de TSJ, misma materia, fallo contradictorio; una por punto de contradicción) → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`, o `base="AN"` con `tipo_organo="TSJ"`), afinando con `opciones_busqueda`.
- **Comparar hechos, fundamentos y pretensiones de la recurrida y de la de contraste** → `leer_sentencias` (texto íntegro, o `parrafos=3` con `terminos`) y `continuar_lectura` si la lectura queda a medias.
- **Verificar cada sentencia de contraste antes de citarla** (ECLI o ROJ, órgano, fecha y número exactos) → `buscar_por_cita`; su firmeza a la fecha de fin del plazo de interposición se acredita además con certificación.
- **Arts. 218-228 LRJS en su redacción vigente, con el interés casacional objetivo del art. 221.2.c) introducido por la LO 1/2025** → `buscar_articulo` (`ley="LRJS"`, `articulo="221"`).
- **Revisión del escrito** → `verificar_escrito` con el texto completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Marco normativo

- Regulado en los arts. 218-228 LRJS (disposiciones comunes: arts. 229-235). Competencia: Sala de lo Social (Sala IV) del Tribunal Supremo.
- **Trámite y plazos verificados**: **preparación en 10 días** desde la notificación de la sentencia del TSJ, mediante escrito dirigido a la propia Sala de suplicación (art. 220.1); **interposición en el plazo común de 15 días** desde la notificación de la puesta a disposición de los autos, ante la misma Sala de suplicación (art. 223.1); emplazamiento de las demás partes para personarse ante el TS en 10 días (art. 223.4).
- **⚠️ Reforma LO 1/2025 (en vigor desde el 3-4-2025)**: el escrito de preparación debe exponer, además del núcleo de la contradicción y los datos de las sentencias de contraste, **las razones por las que la cuestión posee interés casacional objetivo** (art. 221.2.c LRJS). No incluirlo es causa de inadmisión. Verificar la redacción vigente de los arts. 220-224 vía `buscar_articulo` antes de redactar.
- **Presupuesto sustantivo — contradicción** (art. 219 LRJS): exige acreditar que, ante hechos, fundamentos y pretensiones sustancialmente iguales, la sentencia recurrida llegó a un pronunciamiento distinto al de la sentencia de contraste. Solo cabe invocar **una sentencia de contraste por punto de contradicción**, y las no mencionadas en la preparación no pueden invocarse después (art. 221.4).
- **Firmeza de la sentencia de contraste** (art. 221.3 LRJS): debe haber ganado firmeza **a la fecha de finalización del plazo de interposición**.
- **Depósito si recurre quien no goza de justicia gratuita** (art. 229.1.b LRJS): 600 €, más la consignación de la condena en su caso (art. 230).
- **Escrito de interposición** (art. 224 LRJS): relación precisa y circunstanciada de la contradicción + fundamentación de la infracción legal cometida y del quebranto producido en la unificación de doctrina.
- **Otrosíes habituales**: designación de domicilio en la sede de la Sala de lo Social del TS (art. 221.1) y aportación de certificación de la sentencia de contraste con expresión de su firmeza.

## Fase 1 — Documentación a pedir

- Sentencia recurrida (TSJ) y datos del procedimiento (autos, rollo de suplicación).
- Sentencia de contraste propuesta por el usuario, o pedirle que indique la materia exacta para que Claude la busque vía `jurisprudenciator`.
- Diligencia/providencia que tuvo por preparado el recurso.
- Certificado de firmeza de la sentencia de contraste (documento habitual a aportar con el recurso).

## Fase 2 — Batería de preguntas

- ¿En qué fase estamos? preparación (10 días) / interposición (15 días) — el contenido exigido es distinto.
- Materia exacta sobre la que se alega contradicción (para poder localizar sentencias de contraste válidas).
- ¿El usuario ya tiene identificada una sentencia de contraste, o hay que buscarla? Si hay que buscarla: usar `buscar_sentencias` de jurisprudenciator y filtrar por Sala IV/Social, verificando firmeza con `buscar_por_cita`. Recordar: UNA sentencia por punto de contradicción.
- ¿Cuál es el **interés casacional objetivo** de la cuestión (art. 221.2.c LRJS)? — prepararlo como argumento autónomo, no como coletilla.
- Norma o doctrina cuya infracción se alega en la sentencia recurrida.
- ¿Quién recurre? Si no goza de justicia gratuita: depósito de 600 € (art. 229.1.b) y consignación en su caso.

## Fase 3 — Estructura del escrito

1. Encabezamiento: datos del procedimiento (autos de origen, rollo de suplicación, sentencia y fecha), Sala de lo Social del TSJ ante la que formalmente se presenta (que lo eleva al TS), identificación de quien recurre (marcador genérico).
2. Cumplimiento de requisitos formales (preparación en plazo, emplazamiento).
3. **Relación precisa y circunstanciada de la contradicción**: exponer hechos, fundamentos y pretensiones de la sentencia recurrida y de la sentencia de contraste, subrayando la identidad sustancial y el signo contradictorio de los fallos (art. 219 LRJS).
4. **FUNDAMENTOS DE DERECHO**: competencia (art. 9.b, 218 LRJS) → desarrollo de la infracción legal cometida y del quebranto en la unificación de doctrina.
5. **SUPLICO**: que se admita el recurso, se case y anule la sentencia recurrida, y se resuelva el debate en los términos pedidos.
6. **OTROSÍES**: designación de domicilio profesional a efectos de notificaciones (art. 221.1 LRJS, marcador genérico) y constancia de firmeza de la sentencia de contraste (art. 221.3 LRJS).

## Fase 4 — Verificación y entrega

Verificación obligatoria y explícita de la firmeza y contenido exacto de la sentencia de contraste antes de entregar el escrito — sin esa verificación, el recurso es inadmisible. Pulir con `/estilo-escritos-judiciales`. Entregar en Word (.docx).

---

**Nota de anonimización**: cualquier dato real de letrado/a, colegiado o partes presente en la plantilla de origen se sustituye por marcador genérico.
