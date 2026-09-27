---
name: responsabilidad-patrimonial-ca
description: Asiste en reclamaciones de responsabilidad patrimonial de la Administración (arts. 32-37 Ley 40/2015, procedimiento de la Ley 39/2015) y en su posterior impugnación contenciosa. Cubre responsabilidad sanitaria, viaria, por funcionamiento de servicios y del Estado legislador. Activar con "responsabilidad patrimonial", "reclamación de daños a la Administración", "lex artis", "infección nosocomial", "negligencia médica hospital público", "caída en la vía pública", "reclamar al ayuntamiento por daños".
---

# Responsabilidad patrimonial de la Administración (arts. 32-37 Ley 40/2015)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Requisitos, prescripción y procedimiento** → `buscar_articulo` (`ley="LRJSP"`, artículos 32 a 35; `ley="LPAC"`, artículos 67, 81 y 91).
- **Lex artis, daño desproporcionado, pérdida de oportunidad y consentimiento informado** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`, `terminos`).
- **Estado legislador (arts. 32.4 y 32.5)** → `buscar_sentencias` (`base="TC"` o `base="TJUE"`) y `buscar_boe` + `leer_boe` para la fecha de publicación que abre el año para reclamar.
- **Daño en la vía pública** → `consultar_catastro` (dirección o coordenadas del lugar; `callejero_catastro` si la vía no casa) y `buscar_ordenanzas` + `leer_ordenanza` (ordenanza de vía pública o de conservación).
- **Actualización e intereses del art. 34.3** → `buscar_articulo` (`ley="Ley 47/2003"`).
- **Aseguradora codemandada** → `buscar_empresa_mercantil` (denominación inscrita y domicilio).
- **Antes de presentar** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

---

Reclamación en vía administrativa y su impugnación contenciosa. Plazos y cifras:
`references/anclas-normativas-ca.md`. Lo no anclado, verificarlo con `buscar_articulo` o marcarlo
`[verificar]`.

---

## 1. ⚠️ PRESCRIPCIÓN — art. 67.1 LPAC: son CUATRO reglas, no una

Texto verificado. La regla general es **1 año**, pero **el dies a quo cambia** según el supuesto:

| Supuesto | Plazo | **Cómputo desde** |
|---|---|---|
| **Regla general** | 1 año | Producido el **hecho o acto** que motive la indemnización **o se manifieste su efecto lesivo** |
| **⚠️ Daños físicos o psíquicos a las personas** | 1 año | La **CURACIÓN** o la **DETERMINACIÓN DEL ALCANCE DE LAS SECUELAS** |
| **Anulación** en vía administrativa o contencioso-administrativa de un acto o disposición general | 1 año | La **notificación de la resolución administrativa o de la sentencia definitiva** |
| **Arts. 32.4 y 32.5 Ley 40/2015** (norma inconstitucional o contraria al Derecho de la UE) | 1 año | La **publicación en el BOE o en el DOUE**, según el caso, de la sentencia que declare la inconstitucionalidad o el carácter contrario al Derecho de la UE |

> # ⚠️ LA REGLA DE LAS SECUELAS DECIDE LOS ASUNTOS SANITARIOS
>
> «En caso de daños de carácter físico o psíquico a las personas, el plazo empezará a computarse
> **desde la curación o la determinación del alcance de las secuelas**» (art. 67.1 LPAC).
>
> **Es la regla más importante de esta skill y la que más asuntos salva o pierde.** Consecuencias:
>
> - **El año NO corre desde la intervención, el diagnóstico ni el alta hospitalaria.** Corre desde la
>   **estabilización lesional**: curación o determinación del alcance de las secuelas.
> - **Un asunto aparentemente prescrito puede no estarlo.** Antes de decirle a nadie que ha perdido el
>   derecho, **buscar la fecha de estabilización**: alta médica definitiva, informe de secuelas,
>   resolución de incapacidad, dictamen del EVI, último informe de rehabilitación.
> - **Daños continuados vs. permanentes:** en los **permanentes** el año corre desde que se conoce el
>   alcance; en los **continuados**, mientras el daño se sigue produciendo, no empieza a correr.
>   ⚠️ La delimitación es **jurisprudencial**: **verificar con `buscar_sentencias` antes de sostenerla**,
>   y no citar doctrina de memoria.
> - **Acreditar la fecha de estabilización con documento y folio** en el propio escrito, de forma
>   proactiva: la Administración alegará prescripción y el escrito debe traer la respuesta hecha.
>
> **Y a la inversa:** no confiar en que la regla salvará el asunto. Si hay fecha de estabilización
> clara, **el año corre y es de prescripción** — reclamar ya. Aplicar el margen de seguridad de la casa.

- **Naturaleza:** en vía administrativa el plazo del art. 67 es de **PRESCRIPCIÓN** — **sí se
  interrumpe** por reclamación (a diferencia de los plazos de interposición del contencioso, que son de
  **caducidad**). ⚠️ **No confundir los dos regímenes**: una vez notificada la resolución (o producido
  el silencio), el plazo para acudir al contencioso **es de caducidad** y no lo interrumpe nada. Ver § 5.
- **Art. 67.1 *in fine*:** solo puede solicitarse el inicio del procedimiento **cuando no haya prescrito**
  el derecho a reclamar.

## 2. Requisitos de fondo (arts. 32 y 34 Ley 40/2015, verificados)

- **Art. 32.1:** derecho a ser indemnizado de **toda lesión en bienes y derechos**, siempre que sea
  **consecuencia del funcionamiento NORMAL O ANORMAL de los servicios públicos**, **salvo** en casos de
  **fuerza mayor** o de **daños que el particular tenga el deber jurídico de soportar de acuerdo con la
  Ley**.
  - ⚠️ **Fuerza mayor** excluye; el **caso fortuito** **no**. Es una distinción que se juega en cada
    asunto viario y sanitario: la Administración llamará «fuerza mayor» a lo que suele ser caso fortuito.
    Exigir los rasgos de la fuerza mayor: **externa, imprevisible e inevitable**.
- **⚠️ Art. 32.1, párrafo 2.º — el jarro de agua fría que hay que conocer:** «La **anulación** en vía
  administrativa o por el orden jurisdiccional contencioso administrativo de los actos o disposiciones
  administrativas **NO PRESUPONE, POR SÍ MISMA, derecho a la indemnización**.» Ganar la anulación **no**
  da automáticamente la indemnización: hay que **acreditar la lesión antijurídica y el nexo** de forma
  autónoma. Decírselo al cliente **antes** de que lo descubra al final.
- **Art. 32.2 — el daño:** ha de ser **efectivo**, **evaluable económicamente** e **individualizado** con
  relación a una persona o grupo de personas. (Daño hipotético, futuro incierto o general → fuera.)
- **Antijuridicidad (art. 32.1 + art. 34.1):** solo son indemnizables las lesiones provenientes de daños
  que el particular **no tenga el deber jurídico de soportar de acuerdo con la Ley**. **Es el requisito
  que más se descuida**: se argumentan daño y nexo y se da por supuesta la antijuridicidad. **Dedicarle
  un fundamento propio.**
- **⚠️ Art. 34.1 — riesgos del desarrollo:** «**No serán indemnizables los daños que se deriven de hechos
  o circunstancias que no se hubiesen podido prever o evitar según el ESTADO DE LOS CONOCIMIENTOS DE LA
  CIENCIA O DE LA TÉCNICA existentes en el momento** de producción de aquéllos», sin perjuicio de las
  prestaciones asistenciales o económicas que las leyes establezcan.
- **Nexo causal:** debe ser **directo**. Valorar la **concurrencia de culpas** de la víctima o de
  terceros: rara vez rompe el nexo, pero **modera** el quantum. Anticiparlo en lugar de ignorarlo.

### 2.1 ⚠️ «Lex artis» — es estándar JURISPRUDENCIAL, no literal de la ley

- **El art. 34.1 NO emplea la expresión «lex artis».** Lo que dice literalmente es lo del **estado de los
  conocimientos de la ciencia o de la técnica** (riesgos del desarrollo). La **lex artis** —y la **lex
  artis ad hoc**— son construcción **jurisprudencial**.
- **Consecuencia práctica:** no atribuir al art. 34.1 palabras que no tiene. Citarlo por lo que dice, y
  **fundar la lex artis en jurisprudencia VERIFICADA** con `buscar_sentencias` / `buscar_por_cita`.
- **Idea central del estándar sanitario:** la obligación es **de medios, no de resultado**. No se
  responde por el mal resultado, sino por la **infracción del estándar de diligencia exigible**. Un
  escrito que argumenta «el resultado fue malo, luego hay responsabilidad» **pierde**.
- **Doctrinas de alto rendimiento** —todas **jurisprudenciales**, todas a **verificar antes de citar**:
  - **Daño desproporcionado / resultado clamoroso**: desplaza la carga de explicar a la Administración.
  - **Pérdida de oportunidad**: cuando no se acredita que la actuación correcta habría evitado el daño,
    pero sí que privó de una posibilidad relevante de curación o mejoría. **Indemniza el porcentaje de
    oportunidad perdida, no el daño íntegro** — plantearlo así, y no como todo o nada.
  - **Consentimiento informado**: su ausencia o insuficiencia tiene sustantividad propia (lesiona la
    autodeterminación), **incluso sin mala praxis**. Verificar su régimen y no confundirlo con el
    formulario firmado: el consentimiento es un **proceso**, no un papel.
  - **Infección nosocomial**: valorar el estándar de asepsia y los protocolos del centro.
- ⚠️ **Prohibido citar de memoria** cualquier STS de la Sala Tercera en materia sanitaria. Verificar
  siempre; sin verificación → `[verificar]` y decirlo.

### 2.2 Estado legislador (arts. 32.3, 32.4, 32.5 y 32.6) — requisitos exigentes

- **32.4 (norma declarada inconstitucional)** y **32.5 (norma contraria al Derecho de la UE)**: procede
  la indemnización **cuando el particular haya obtenido, EN CUALQUIER INSTANCIA, SENTENCIA FIRME
  DESESTIMATORIA de un recurso contra la actuación administrativa que ocasionó el daño**, **siempre que
  se hubiera ALEGADO la inconstitucionalidad —o la infracción del Derecho de la UE— posteriormente
  declarada**.
  > ⚠️ **Doble filtro brutal y muy poco conocido:** (i) haber **recurrido y perdido** con sentencia
  > firme; (ii) **haber alegado** el vicio en aquel recurso. Quien no recurrió, o recurrió sin alegarlo,
  > **queda fuera**. Es un consejo que se da **antes**, no después: si hay una norma cuya
  > constitucionalidad o compatibilidad con la UE se discute, **recurrir y alegarlo expresamente** es lo
  > que preserva el derecho.
- **32.5** exige **además**, acumulativamente: **a)** que la norma tenga por objeto **conferir derechos a
  los particulares**; **b)** que el incumplimiento esté **suficientemente caracterizado**; **c)**
  **relación de causalidad directa**.
- **32.6:** la sentencia que declare la inconstitucionalidad o el carácter contrario al Derecho de la UE
  produce efectos **desde su publicación** en el BOE o el DOUE, salvo que ella disponga otra cosa.
- **⚠️ Art. 34.1, párrafo 2.º — límite temporal del quantum:** en los supuestos de los arts. 32.4 y 32.5
  son indemnizables **los daños producidos en los CINCO AÑOS anteriores a la fecha de publicación** de la
  sentencia, **salvo que la sentencia disponga otra cosa**. No confundir con el plazo de **1 año** para
  reclamar del art. 67.1: **son cosas distintas** — uno es el plazo para pedir, otro el período indemnizable.
- **32.7:** la responsabilidad por el funcionamiento de la **Administración de Justicia** se rige por la
  **LOPJ** — **fuera de esta skill**; no forzar el encaje.

## 3. Cuantificación (art. 34, verificado) — el apartado que decide el resultado económico

- **34.2:** cálculo con arreglo a los criterios de la legislación **fiscal**, de **expropiación forzosa**
  y demás normas aplicables, ponderando **las valoraciones predominantes en el mercado**. En **muerte o
  lesiones corporales** **se podrá tomar como referencia** el **baremo** de la normativa de **seguros
  obligatorios** y de la **Seguridad Social**.
  > ⚠️ El baremo es **referencia orientativa, NO vinculante** («se podrá tomar como referencia»). Es una
  > **oportunidad**: cabe **razonar al alza** frente al baremo cuando el caso lo justifique. Un escrito
  > que aplica el baremo como si fuera obligatorio renuncia a dinero sin saberlo. Argumentar la
  > desviación, no darla por imposible.
- **34.3:** la cuantía se calcula **con referencia al día en que la lesión efectivamente se produjo**,
  **sin perjuicio de su ACTUALIZACIÓN** a la fecha en que se ponga fin al procedimiento **con arreglo al
  Índice de Garantía de la Competitividad (IGC)** del INE, **y de los intereses** que procedan por
  **demora en el pago**, exigibles conforme a la **Ley 47/2003 General Presupuestaria** o a las normas
  presupuestarias autonómicas.
  > ⚠️ **Pedir SIEMPRE, y por separado: (i) la cuantía a fecha del daño; (ii) la ACTUALIZACIÓN por el
  > IGC; (iii) los INTERESES de demora.** Son tres conceptos distintos y los tres se olvidan. En asuntos
  > que tardan años, la actualización y los intereses son una parte sustancial de lo que se cobra.
- **34.4:** la indemnización **puede sustituirse** por **compensación en especie** o abonarse mediante
  **pagos periódicos**, cuando sea más adecuado para la reparación debida y convenga al interés público,
  **siempre que exista acuerdo con el interesado**. ⚠️ **Requiere acuerdo**: no se puede imponer.

## 4. Procedimiento en vía administrativa (Ley 39/2015, verificado)

| Trámite | Regla |
|---|---|
| **Contenido de la solicitud (art. 67.2)** | Además del art. 66, debe especificar: las **lesiones producidas**; la **presunta relación de causalidad** con el funcionamiento del servicio público; la **evaluación económica**, si fuera posible; y el **momento en que la lesión efectivamente se produjo**. Se acompaña de alegaciones, documentos e informaciones y de la **proposición de prueba**, concretando los medios. |
| **Informe del servicio (art. 81.1)** | **Preceptivo** solicitar informe **al servicio cuyo funcionamiento** ocasionó la presunta lesión; plazo de emisión **≤ 10 días**. ⚠️ Es la Administración informando sobre sí misma: **rebatirlo con pericial propia**. |
| **⚠️ Dictamen del Consejo de Estado / órgano consultivo autonómico (art. 81.2)** | **Preceptivo** cuando las indemnizaciones reclamadas sean de **cuantía IGUAL O SUPERIOR a 50.000 €** **o a la que establezca la legislación autonómica correspondiente**, así como en los casos de la LO 3/1980 del Consejo de Estado. El instructor remite propuesta de resolución en **10 días** desde el fin de la audiencia. El dictamen se emite en **2 meses** y **debe pronunciarse sobre la existencia o no de relación de causalidad** y, en su caso, sobre la **valoración del daño**, la **cuantía** y el **modo** de la indemnización. |
| **Resolución (art. 91.2)** | Debe pronunciarse **sobre el nexo causal** y, en su caso, sobre la **valoración del daño**, **cuantía** y **modo**, conforme al art. 34 LRJSP. ⚠️ Si no lo hace, es un **vicio alegable**. |
| **⚠️ Silencio (art. 91.3)** | Transcurridos **6 MESES** desde el inicio sin resolución expresa notificada (ni acuerdo formalizado), **puede entenderse que la resolución es CONTRARIA a la indemnización** — silencio **desestimatorio**. |

> ⚠️ **El umbral del dictamen (50.000 €) es una decisión estratégica al redactar.** Es *«o a la que se
> establezca en la correspondiente legislación autonómica»*: **el umbral autonómico puede ser distinto**
> (y a menudo lo es). **El conector NO cubre normativa autonómica: pedírsela al usuario y no citarla de
> memoria.** El dictamen alarga el procedimiento, pero un dictamen favorable es un activo de primer
> orden en el pleito posterior. Valorarlo con el cliente, no cuantificar a ciegas.

## 5. Impugnación contenciosa — plazos y competencia

- **Acto expreso** que pone fin a la vía administrativa: **2 meses** (art. 46.1 LJCA).
- **Silencio** (desestimación presunta a los 6 meses, art. 91.3 LPAC): **6 meses** para interponer
  (art. 46.1 LJCA), desde el día siguiente a producirse el acto presunto.
- ⚠️ **Estos plazos son de CADUCIDAD.** No los interrumpe burofax, reclamación ni requerimiento. Cambio
  de régimen respecto de la vía administrativa (§ 1): explicarlo al cliente.
- **Agosto NO corre** (art. 128.2 LJCA), salvo procedimiento de DDFF.
- **⚠️ Competencia objetiva:** los **Juzgados de lo Contencioso-administrativo** conocen de la
  responsabilidad patrimonial de las **CCAA** cuando la cuantía **no exceda de 30.050 €** (**art. 8.2.c
  LJCA**). Por encima, la **Sala del TSJ**. Comprobar antes de dirigir el escrito; y comprobar el resto
  del art. 8 con `buscar_articulo` para entidades locales y Administración del Estado.
- **Cuantía:** determina competencia, **abreviado** (≤ 30.000 €, art. 78.1 LJCA), **apelación** (excluida
  si ≤ 30.000 €, art. 81.1.a, salvo los supuestos del art. 81.2) y el **tope de costas** del art. 139.4.
  **Fijarla con criterio desde el principio**: es una decisión con cuatro consecuencias.
- **Costas:** art. 139.1 (vencimiento objetivo, salvo serias dudas de hecho o de derecho razonadas — en
  responsabilidad sanitaria se aprecian con relativa frecuencia), con el **tope del art. 139.4**: máximo
  **un tercio de la cuantía del proceso por cada favorecido**; cuantía indeterminada = **18.000 €** a
  esos solos efectos, salvo razonamiento por complejidad. **Nunca** al Ministerio Fiscal (art. 139.6).
  ⚠️ **Advertir del riesgo por escrito**: reclamar 300.000 € y perder puede significar una condena de
  hasta 100.000 € en costas por cada favorecido. **El tope se calcula sobre la cuantía que se pide** —
  razón adicional para no inflarla.
- **Codemandada aseguradora:** habitual en sanitario y viario. Comprobar si la Administración tiene
  póliza y pedir su llamada. Verificar el régimen aplicable antes de afirmarlo.

## 6. Errores típicos que pierden el asunto

1. **⚠️ Computar el año desde el hecho en daños físicos o psíquicos**, cuando corre desde la **curación o
   la determinación del alcance de las secuelas** (art. 67.1). Y su reverso: **dar por prescrito** un
   asunto sin buscar la fecha de estabilización.
2. **Confundir prescripción (vía administrativa, interrumpible) con caducidad** (plazos del contencioso,
   no interrumpibles).
3. **Creer que la anulación del acto da la indemnización** — art. 32.1, párrafo 2.º: **no la presupone**.
4. **No argumentar la ANTIJURIDICIDAD** en fundamento propio, dando por supuesto que daño + nexo bastan.
5. **Argumentar el mal resultado** en vez de la infracción del estándar (obligación de medios).
6. **Atribuir al art. 34.1 la expresión «lex artis»** — no la contiene: es jurisprudencial.
7. **Plantear la pérdida de oportunidad como todo o nada** en vez de como porcentaje.
8. **Aplicar el baremo como vinculante** (art. 34.2: «se podrá tomar como referencia»).
9. **No pedir la actualización por el IGC ni los intereses de demora** (art. 34.3): tres conceptos, tres
   peticiones.
10. **Aceptar «fuerza mayor» donde hay caso fortuito.**
11. **Reclamar por debajo de 50.000 € sin advertir la consecuencia sobre el dictamen** (art. 81.2), o
    ignorar que el **umbral autonómico** puede ser distinto.
12. **En estado legislador (arts. 32.4-32.5): reclamar sin haber recurrido y alegado** el vicio en su día.
13. **Inflar la cuantía**: eleva el **tope de costas** del art. 139.4 y el riesgo del cliente.
14. **Dirigir al Juzgado una reclamación autonómica > 30.050 €** (art. 8.2.c).
15. **Citar STS de sanitario de memoria.**

## 7. Anclaje al expediente administrativo

- **Todo hecho afirmado va con folio:** `(doc. núm. X del expediente administrativo, folio Y)`.
- **Documentos que sostienen el asunto** y que deben citarse con folio: historia clínica, informes de
  alta, **informe de secuelas y fecha de estabilización** (§ 1), consentimiento informado, protocolos del
  servicio, partes de incidencias, informes de mantenimiento, **el informe del servicio del art. 81.1** y
  **el dictamen del art. 81.2** si lo hubo.
- **El dictamen del órgano consultivo es material de primer orden:** si fue **favorable** al reclamante y
  la Administración resolvió en contra, **explotarlo** — la resolución se aparta de su propio órgano
  consultivo. Citarlo con folio y transcribir el pasaje sobre el nexo (art. 81.2 exige que se pronuncie
  sobre él).
- Si falta un documento decisivo en poder de la Administración, **decirlo y pedirlo**; el silencio
  documental de quien custodia la historia clínica no puede perjudicar al reclamante.
- **Pericial propia:** en sanitario es prácticamente imprescindible para rebatir el informe del servicio.
  Advertirlo al usuario desde el primer momento (coste y plazo).

## 8. ⚠️ Protección de datos — categoría especial del art. 9 RGPD

> **Los datos de salud son categoría especial del art. 9 RGPD.** También la ideología, afiliación
> sindical, religión, orientación sexual, datos genéticos y biométricos.
>
> - **NUNCA reproducir historiales clínicos reales** en los borradores, ni transcribir informes médicos
>   con datos identificativos.
> - **La cronología clínica se construye con MARCADORES:** `[PACIENTE]`, `[CENTRO]`, `[SERVICIO]`,
>   `[FECHA]`, `[DIAGNÓSTICO]`, `[PROFESIONAL]`, `[IMPORTE]`.
> - Trabajar con la **estructura** del caso —secuencia de actuaciones, momento de la infracción del
>   estándar, momento de la estabilización— **no con los datos personales**. El usuario completa los
>   datos reales en su entorno al firmar el escrito.
> - Anonimizar también a **terceros**: otros pacientes, profesionales identificados, familiares.
> - No incorporar datos clínicos reales a resúmenes, tablas o entregables intermedios.

## 9. Estructura del escrito

**A) Reclamación en vía administrativa (arts. 66 y 67.2 LPAC):**

1. Órgano competente; identificación del reclamante y representación.
2. **HECHOS** numerados: cronología con **marcadores** y **folios**.
3. **LESIONES PRODUCIDAS** (art. 67.2).
4. **RELACIÓN DE CAUSALIDAD** con el funcionamiento del servicio público (art. 67.2).
5. **ANTIJURIDICIDAD**: por qué no existe deber jurídico de soportar el daño (fundamento propio).
6. **EVALUACIÓN ECONÓMICA** (art. 67.2) y **MOMENTO EN QUE LA LESIÓN SE PRODUJO** — este dato es
   **doblemente crítico**: exigido por el art. 67.2 y base del cálculo del art. 34.3.
7. **PRESCRIPCIÓN**: acreditar proactivamente el dies a quo (§ 1), con documento y folio.
8. **PROPOSICIÓN DE PRUEBA**, concretando los medios (art. 67.2): documental, pericial, testifical.
9. **SUPLICO** y otrosíes.

**B) Recurso contencioso / demanda:** aplicar `interposicion-recurso-contencioso-ca` y
`demanda-contencioso-administrativa`. En la demanda, además: acreditar el **agotamiento de la vía**,
la **cuantía** (arts. 40-42 LJCA), el **recibimiento a prueba** (art. 60 LJCA), y **rebatir el informe
del art. 81.1** con pericial propia. **Nada de MASC:** es del orden civil.

## 10. SUPLICO — modelo conforme al art. 31 LJCA

> **SUPLICO AL JUZGADO/A LA SALA** que, teniendo por presentado este escrito, se sirva admitirlo, tener
> por formulada **DEMANDA** en el presente recurso contencioso-administrativo y, previos los trámites
> legales, dictar sentencia por la que, **estimando íntegramente** el recurso:
>
> **1.º** **Declare** que **[RESOLUCIÓN]** de **[ÓRGANO]**, de **[FECHA]** —[o la desestimación presunta
> por silencio, ex art. 91.3 LPAC]—, **no es conforme a Derecho**, y la **anule** (art. 31.1 LJCA).
> **2.º** **Reconozca la situación jurídica individualizada** de **[CLIENTE]**, declarando la
> **responsabilidad patrimonial** de **[ADMINISTRACIÓN]** por el funcionamiento **[normal/anormal]** del
> servicio público de **[SERVICIO]**, y **acuerde las medidas necesarias para el pleno restablecimiento**
> de dicha situación (art. 31.2 LJCA).
> **3.º** **Condene a [ADMINISTRACIÓN] [y solidariamente a [ASEGURADORA]] a indemnizar** a **[CLIENTE]**
> en la cantidad de **[IMPORTE]**, calculada con referencia al día en que la lesión efectivamente se
> produjo (**art. 34.3 LRJSP**), **[o la que se determine en ejecución de sentencia conforme a las bases
> que se fijen]**; **más su ACTUALIZACIÓN** hasta la fecha en que se ponga fin al procedimiento **con
> arreglo al Índice de Garantía de la Competitividad** del INE; **más los INTERESES** de demora que
> procedan conforme a la **Ley 47/2003, General Presupuestaria** [o normativa presupuestaria autonómica
> aplicable] (**art. 34.3 LRJSP**), y los del **art. 106.2 LJCA** desde la notificación de la sentencia.
> **4.º** Con **imposición de costas** a la Administración demandada (art. 139.1 LJCA).
>
> **OTROSÍ DIGO** que, para el caso de imposición de costas a esta parte, **SUPLICO** se haga constar el
> **límite del art. 139.4 LJCA** (un tercio de la cuantía del proceso por cada favorecido).

- ⚠️ **Los tres conceptos del punto 3.º (principal + actualización IGC + intereses) van SIEMPRE y por
  separado.** Lo no pedido no se concede.
- **No omitir el punto 2.º:** anular la resolución denegatoria sin que se reconozca la situación jurídica
  individualizada es una **victoria estéril** que devuelve el asunto a la Administración. El art. 31.2
  LJCA existe precisamente para eso — y de él depende, además, la ejecución (ver `ejecucion-sentencias-ca`).
- Si el quantum no está cerrado, pedir **bases para ejecución de sentencia** en lugar de una cifra
  aventurada — pero **fijar la cuantía del proceso** con criterio (§ 5).

## 11. Reglas de la casa

- **Protección de datos:** § 8 — **datos de salud = art. 9 RGPD**. Cero datos reales; cronología con
  marcadores.
- **Jurisprudencia:** **especialmente crítico en sanitario.** Lex artis, daño desproporcionado, pérdida
  de oportunidad y consentimiento informado son **doctrina jurisprudencial**: verificar **cada** cita con
  `buscar_sentencias` / `buscar_por_cita` **antes** de incluirla. Prohibido inventar ECLI, ROJ, fecha,
  ponente o fundamento. Sin verificación → `[verificar]` y decirlo.
- **Normativa autonómica y local:** el conector no la cubre. Afecta de lleno aquí: **umbral del dictamen
  del art. 81.2**, órgano consultivo autonómico, normas presupuestarias autonómicas del art. 34.3,
  ordenanzas en responsabilidad viaria. **Pedírsela al usuario; no citarla de memoria.**
- **Nada de MASC:** requisito del orden civil; no existe aquí. El equivalente funcional es el
  **agotamiento de la vía administrativa** (art. 25.1 LJCA).
- **Entregable:** Word `.docx` maquetado (skill `docx`).
