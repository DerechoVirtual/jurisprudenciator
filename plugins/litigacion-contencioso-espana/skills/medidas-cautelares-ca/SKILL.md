---
name: medidas-cautelares-ca
description: >-
  Redacta solicitudes de medidas cautelares y de suspensión del ACTO administrativo impugnado en el orden contencioso-administrativo (arts. 129-136 LJCA), incluida la cautelarísima inaudita parte del art. 135. Activar con "suspensión del acto", "medida cautelar contencioso", "pieza separada de medidas cautelares", "cautelarísima", "suspender la ejecución de la sanción", "que no me ejecuten mientras dure el recurso". Su objeto es paralizar la eficacia del acto dentro de un recurso contencioso ya interpuesto o que se interpone a la vez. Si lo que está en juego es la ENTRADA física en un domicilio o local para ejecutar el acto, ese es un procedimiento autónomo distinto → /autorizacion-entrada-domicilio-ca.
---

# Medidas cautelares en el contencioso-administrativo (arts. 129-136 LJCA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Preceptos del incidente cautelar** → `buscar_articulo` (`ley="LJCA"`, artículos 128 a 136; `ley="LPAC"`, artículos 39, 90 y 117).
- **Criterio de la Sala sobre periculum y ponderación (art. 130)** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `tipo_resolucion="AUTO"`; `base="AN"` con `tipo_organo="TSJ"` y `provincia`, o `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Fumus palmario: acto idéntico ya anulado o norma anulada** → `buscar_por_cita` + `leer_sentencias` sobre la sentencia anulatoria; `buscar_boe` + `leer_boe` para la publicación del fallo (art. 72.2 LJCA).
- **Suspensión de la vigencia de una ordenanza (art. 129.2)** → `buscar_ordenanzas` + `leer_ordenanza` con `articulo`.
- **Demolición o clausura inminente** → `consultar_catastro` (referencia catastral y construcciones afectadas) para identificar con precisión lo que se quiere preservar.
- **Antes de presentar** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

Redacta la solicitud de medida cautelar en pieza separada. Plazos y cifras: `references/anclas-normativas-ca.md`.
Lo que no esté allí, verifícalo con `buscar_articulo` antes de escribirlo o márcalo `[verificar]`.

> ⚠️ **El error conceptual que arruina estos escritos:** importar el esquema cautelar civil
> (fumus + periculum + caución como tres patas equivalentes). **En el contencioso no es así.**
> El eje es el **periculum**; el fumus tiene juego **muy restrictivo**. Ver § 3.

---

## 1. Bloque previo — comprobar antes de redactar

Recorrer en orden y **no seguir** hasta cerrar cada punto:

1. **¿Hay recurso contencioso interpuesto o se interpone a la vez?** La cautelar es accesoria: no
   existe medida cautelar autónoma sin proceso. Si aún no hay recurso, se pide en el escrito de
   interposición o después.
2. **¿En qué momento se pide?** Regla general: **en cualquier estado del proceso** (art. 129.1).
3. **⚠️ EXCEPCIÓN — impugnación de disposición general** (art. 129.2, verificado): si se impugna una
   disposición general **y se pide la suspensión de la vigencia de los preceptos impugnados**, la
   petición **debe** efectuarse **en el escrito de interposición o en el de demanda**. Fuera de esos
   dos momentos, precluye. Comprobar siempre si el objeto es una disposición general antes de
   calendar la cautelar.
4. **¿Cuál es exactamente el acto/disposición/vía de hecho cuya ejecución se quiere paralizar?**
   Identificarlo con órgano, fecha y folio del expediente. No caben cautelares contra objetos difusos.
5. **¿Qué se pide en realidad?** El art. 129.1 admite «cuantas medidas aseguren la efectividad de la
   sentencia», no solo la suspensión. Si la pretensión de fondo es positiva (obtener una licencia,
   un pago, un reingreso), la mera suspensión **no sirve**: hay que pedir una medida positiva o de
   regulación provisional coherente con el art. 31 LJCA.
6. **¿Ya se pidió y se denegó la suspensión en vía administrativa?** No impide pedirla en sede
   judicial, pero el razonamiento denegatorio de la Administración estará en el expediente: hay que
   rebatirlo con folio.
7. **Agosto** (art. 128.2): los plazos de la LJCA **no corren** en agosto, salvo en el procedimiento
   de derechos fundamentales. Pero el incidente cautelar admite **habilitación de días inhábiles**
   (art. 128.3): ver § 5.

---

## 2. Criterio central — periculum in mora (art. 130.1)

Texto verificado: la medida podrá acordarse **únicamente** cuando la ejecución del acto o la
aplicación de la disposición **pudieran hacer perder su finalidad legítima al recurso**, previa
**valoración circunstanciada de todos los intereses en conflicto**.

Cómo se argumenta bien (y cómo se argumenta mal):

- **Mal:** «la ejecución causaría un grave perjuicio a mi mandante». Genérico → denegación.
- **Bien:** demostrar que, cuando llegue la sentencia estimatoria, **ya no habrá nada que restablecer**.
  Es un juicio sobre la **irreversibilidad**, no sobre la molestia.
- Trabajar la **reversibilidad económica**: si el daño es puro dinero y la Administración es solvente,
  el recurso no pierde su finalidad (se devuelve con intereses) → la cautelar decae. Por eso, en actos
  de contenido económico hay que acreditar algo más: **quebranto de la viabilidad de la actividad**,
  cierre, insolvencia sobrevenida, pérdida de la clientela o del puesto — con prueba, no con adjetivos.
- Daños típicamente **irreversibles**: demolición, clausura de actividad, expulsión, pérdida de plazo
  o de convocatoria, ejecución sobre bien único, medidas que agotan su efecto por transcurso del tiempo.
- Anclar cada perjuicio en un documento: informe pericial, cuentas, contratos, folio del expediente.

## 3. Fumus boni iuris — juego RESTRICTIVO (no es la segunda pata)

⚠️ **Instrucción de estilo y de fondo:** no presentar el fumus como criterio autónomo equiparable al
periculum, ni construir el escrito alrededor de él.

- El art. 130 **no menciona** la apariencia de buen derecho. Su sede es jurisprudencial y su juego es
  estrecho, porque choca de frente con la **presunción de validez del acto administrativo**
  (art. 39.1 LPAC, verificado: los actos se presumen válidos y producen efectos desde que se dictan).
- Admitir un fumus amplio equivaldría a prejuzgar el fondo en un incidente sumario. Los tribunales lo
  reservan a supuestos de ilegalidad **palmaria**: acto dictado en aplicación de una norma ya anulada,
  reproducción de un acto idéntico ya anulado por sentencia firme, nulidad de pleno derecho manifiesta,
  vía de hecho pura.
- **Cómo usarlo:** invocarlo **subsidiariamente** y solo si el caso es de los anteriores, en un apartado
  breve al final del fundamento, nunca como eje. Si el caso no es palmario, **omitirlo**: un fumus
  forzado debilita el escrito y da al juez el argumento para decir que se pretende anticipar el fondo.
- **Nunca** citar jurisprudencia sobre fumus de memoria: verificar con `buscar_sentencias` /
  `buscar_por_cita`. Si no se verifica, no se cita.

## 4. Ponderación y contrapeso (art. 130.2)

La medida **podrá denegarse** cuando de ella pudiera seguirse **perturbación grave de los intereses
generales o de tercero**, que el órgano ponderará de forma circunstanciada.

- Es la vía por la que se pierden la mayoría de estas piezas. **Anticiparla**: identificar qué interés
  general invocará la Administración (recaudatorio, sanitario, urbanístico, seguridad) y desactivarlo.
- El interés **recaudatorio genérico** o la mera invocación del interés público **no bastan**: exigir
  que se concrete y razone. Argumentar que el interés general también se sirve con la legalidad.
- Si hay **terceros** afectados (adjudicatario de un contrato, vecino, aspirante de una lista), hay que
  nombrarlos como `[TERCERO]` y valorar su perjuicio: ocultarlo es contraproducente.
- Ofrecer **contrapesos**: caución, medida parcial, medida sujeta a condición o plazo. Una cautelar
  bien calibrada y modesta se concede; una maximalista se deniega entera.

## 5. Tramitación, urgencia y caución

| Trámite | Regla verificada |
|---|---|
| Pieza separada | Art. 131: audiencia a la parte contraria por plazo **no superior a 10 días**; auto en los **5 días** siguientes. Si la Administración no ha comparecido, la audiencia se entiende con el **órgano autor** de la actividad impugnada. |
| **Cautelarísima** (art. 135.1) | Alegando **especial urgencia**, el órgano, **sin oír** a la contraria, resuelve por auto **en 2 días**: a) aprecia la urgencia y adopta o deniega la medida conforme al art. 130 — **contra ese auto no cabe recurso alguno** —, y en la misma resolución da audiencia de **3 días** o convoca comparecencia dentro de los **3 días** siguientes; después dicta auto sobre levantamiento, mantenimiento o modificación, este **sí recurrible**. b) **No** aprecia la urgencia y ordena tramitar el incidente por el art. 131 — y entonces **ya no se podrá volver a pedir** medida al amparo del art. 135. |
| Extranjería/asilo con menor | Art. 135.2: si la actuación implica **retorno** y el afectado es **menor de edad**, se oye al **Ministerio Fiscal** antes del auto. |
| **Habilitación de días inhábiles** | Art. 128.3: en el incidente cautelar (y en DDFF) cabe pedirla; el órgano oye a las partes y resuelve por auto en **3 días**, y **debe** acordarla cuando denegarla pudiera causar **perjuicios irreversibles**. Útil en agosto. |
| **Caución** (art. 133) | Si de la medida pudieran derivarse perjuicios, cabe acordar medidas para evitarlos o paliarlos y **exigir caución o garantía**. La medida **no se lleva a efecto** hasta que la caución esté constituida y acreditada en autos (art. 133.2). Levantada la medida, quien pretenda indemnización debe pedirla por el trámite de los incidentes **dentro del año siguiente al alzamiento**; si no, se cancela la garantía (art. 133.3). |

> **Cálculo táctico del art. 135.b):** pedir la cautelarísima sin urgencia real **quema el cartucho**.
> Solo invocarla cuando la ejecución sea inminente y datable (fecha de demolición, de clausura, de
> expulsión). Acreditar la inminencia con documento; si no hay fecha cierta, ir por el art. 131.

## 6. Errores típicos que pierden la pieza

1. **Pedir suspensión cuando la pretensión es positiva.** Suspender una denegación no otorga lo denegado.
2. **Dejar pasar el momento del art. 129.2** en impugnación de disposición general.
3. **Construir el escrito sobre el fumus** → se responde que no cabe prejuzgar el fondo.
4. **Perjuicio genérico y no acreditado** («daños de difícil reparación», sin cifra ni documento).
5. **Perjuicio puramente económico y reversible** presentado como irreversible, sin acreditar quebranto.
6. **No anticipar el art. 130.2**: el auto se apoya en el interés general que nadie rebatió.
7. **No ofrecer caución** cuando la medida afecta a un tercero o a la Hacienda: el ofrecimiento
   proactivo de caución (art. 133) reequilibra la ponderación.
8. **Quemar el art. 135** sin urgencia acreditada, y quedar además impedido de volver a pedirlo.
9. **Olvidar que el auto del art. 135.1.a) no es recurrible** y planificar el asunto contando con recurrirlo.
10. **Confundir el régimen con el civil** (LEC): aquí no hay caución como requisito general de la
    solicitud ni medida cautelar previa autónoma.

## 7. Anclaje al expediente administrativo

- **Todo hecho afirmado va con folio.** Formato: `(doc. núm. X del expediente, folio Y)`.
- Si el expediente aún no ha sido remitido (frecuente cuando la cautelar se pide con la interposición),
  citar la documentación propia aportada como anexo y **advertirlo expresamente** al órgano, pidiendo
  que se valore a resultas del expediente.
- Si falta un documento decisivo que está en poder de la Administración, **decirlo y pedir su aporte**:
  la carga de remitir el expediente es de ella.
- Cronología de la ejecución inminente: fechas, requerimientos, providencias de apremio — todo con folio.

## 8. Estructura del escrito

1. **Encabezamiento.** Órgano; procurador (preceptivo solo ante órganos colegiados, art. 23.2 LJCA) y
   letrado; autos y número de recurso; **«OTROSÍ DIGO» o escrito autónomo** según el momento.
2. **Identificación del acto/disposición/vía de hecho** cuya ejecución se pretende paralizar y de la
   pretensión de fondo del recurso (art. 31 LJCA) — la cautelar debe ser **congruente** con ella.
3. **HECHOS**, numerados y **con folio**, centrados en la inminencia y en la irreversibilidad.
4. **FUNDAMENTOS JURÍDICO-PROCESALES:** competencia, momento (art. 129), pieza separada (art. 131).
5. **FUNDAMENTOS DE FONDO:**
   - **Periculum in mora** (art. 130.1) — el bloque largo del escrito.
   - **Ponderación de intereses** (art. 130.2) — anticipar y desactivar el interés general/de tercero.
   - **Fumus** — solo si es palmario, subsidiario y breve (§ 3).
   - **Ofrecimiento de caución** (art. 133), si procede.
6. **Especial urgencia** (art. 135), si se invoca: apartado propio, con la fecha cierta de ejecución.
7. **SUPLICO.**
8. **OTROSÍES:** habilitación de días inhábiles (art. 128.3); designación electrónica; documentos.

## 9. SUPLICO — modelo de redacción

> **SUPLICO A LA SALA/AL JUZGADO** que, teniendo por presentado este escrito, se sirva admitirlo,
> tener por solicitada la adopción de medida cautelar, ordenar la formación de **pieza separada**
> conforme al art. 131 LJCA y, previos los trámites legales, dictar auto por el que se acuerde
> **[la suspensión de la ejecución de [ACTO], dictado por [ÓRGANO] con fecha [FECHA] / la medida
> cautelar positiva consistente en [MEDIDA]]**, con mantenimiento de la misma hasta que recaiga
> sentencia firme, **[sin caución / previa constitución de caución por importe de [IMPORTE], que
> desde ahora se ofrece]**.
>
> **PRIMER OTROSÍ DIGO** que, concurriendo circunstancias de **especial urgencia** consistentes en
> [HECHO DATADO], **SUPLICO** que, conforme al **art. 135.1 LJCA**, se acuerde la medida **inaudita
> parte** en el plazo de dos días.
>
> **SEGUNDO OTROSÍ DIGO** que, conforme al **art. 128.3 LJCA**, **SUPLICO** la **habilitación de días
> inhábiles**, por cuanto su denegación causaría perjuicios irreversibles [RAZÓN].

- Ajustar el suplico a la **pretensión del art. 31 LJCA**: si el fondo pide reconocimiento de situación
  jurídica individualizada, la cautelar debe asegurarlo, no limitarse a suspender.
- Nunca pedir en cautelar lo que agotaría el fondo de forma irreversible: se deniega por identidad con
  la pretensión principal. Calibrar.

## 10. Reglas de la casa

- **Protección de datos:** cero datos reales. Marcadores `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`,
  `[IMPORTE]`, `[TERCERO]`. Anonimizar a terceros del expediente.
- **Jurisprudencia:** prohibido citar ECLI/ROJ/fecha/ponente de memoria. Verificar con
  `buscar_sentencias` / `buscar_por_cita`. Si no se verifica, se marca `[verificar]` y se dice.
- **Normativa autonómica y local:** el conector no la cubre (solo BOE estatal + ordenanzas de los
  municipios cubiertos). **Pedírsela al usuario**; no citarla de memoria.
- **Nada de MASC:** es requisito del orden **civil**. No existe en esta jurisdicción.
- **Entregable:** Word `.docx` maquetado (skill `docx`).
