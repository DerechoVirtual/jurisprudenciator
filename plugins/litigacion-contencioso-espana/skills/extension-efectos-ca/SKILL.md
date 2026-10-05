---
name: extension-efectos-ca
description: >-
  Catálogo (sin plantilla). Extensión de efectos de sentencias firmes a terceros en idéntica situación jurídica (arts. 110 y 111 LJCA), en materia tributaria, de personal al servicio de las AAPP y de unidad de mercado. Permite obtener los efectos de una sentencia AJENA sin haber pleiteado. Cubre requisitos, plazo de un año, causas tasadas de desestimación, la trampa del acto firme y consentido, y la apelabilidad del art. 81.2.e) LJCA. Activar con "extensión de efectos", "art. 110 LJCA", "art. 111 LJCA", "aprovechar una sentencia de un compañero", "ya hay sentencia para otro funcionario igual", "a un compañero se lo han reconocido", "pleito suspendido por otro preferente", "recurso testigo", "me pueden aplicar esa sentencia", "extender los efectos de la sentencia". Requisito previo: NO fuiste parte en el proceso en que recayó la sentencia. Si la sentencia es tuya y la Administración no la cumple, lo que procede es su ejecución → /ejecucion-sentencias-ca.
---

# Extensión de efectos de sentencias firmes (arts. 110-111 LJCA) — catálogo (sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Texto vigente** → `buscar_articulo` (`ley="LJCA"`, artículos 37, 80, 81, 110 y 111).
- **Localizar la sentencia extensible** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"`, `tipo_organo` y `provincia` del órgano territorialmente competente, `fecha_desde="dd/mm/aaaa"` dentro del año) + `leer_sentencias` del fallo, no del resumen.
- **Sentencia que trae el cliente** → `buscar_por_cita` (ECLI o ROJ). La firmeza y la fecha de la última notificación no están en la base: se confirman en el órgano.
- **Doctrina no desautorizada por el TS (art. 110.5.b)** → `buscar_sentencias` (`base="TS"`, `fecha_desde="dd/mm/aaaa"` = fecha de la sentencia) + `leer_sentencias` (`parrafos=3`).
- **Materia tributaria: criterio que opondrá la Administración en el informe de viabilidad** → `buscar_doctrina_teac` + `leer_resolucion_teac`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

---

Institución propia del contencioso y sistemáticamente desaprovechada: un tercero **que no fue parte**
obtiene, **en ejecución** de una sentencia firme ajena, los mismos efectos, **sin interponer un
recurso propio**. Es rápida, barata y se resuelve por auto. Texto verificado contra el BOE el
**2026-07-17**; **reverifica con `buscar_articulo` antes de citar**.

> ⛔ **Nada de MASC** (orden civil). Aquí ni siquiera hay recurso: es un **incidente de ejecución**.

---

## 1. Ámbito: solo tres materias (art. 110.1) — comprobar lo primero

**En materia TRIBUTARIA, de PERSONAL al servicio de la Administración pública y de UNIDAD DE MERCADO.**

> ⚠️ **Son tres, no dos.** «Unidad de mercado» fue añadida por la **Ley 20/2013** (redacción vigente
> del art. 110 desde el **11-12-2013**). Muchas notas y manuales antiguos dicen «tributaria y de
> personal»: están incompletos.
>
> **La enumeración es CERRADA.** Fuera de esas tres materias **no cabe** la extensión de efectos del
> art. 110 — ni en sancionador, ni en responsabilidad patrimonial, ni en urbanismo, ni en extranjería,
> ni en subvenciones. Si el usuario pide extender una sentencia de otra materia, **dilo y reconduce**
> a un recurso propio en plazo (skill `interposicion-recurso-contencioso-ca`) o, si el pleito ya está
> suspendido, al **art. 111** (§ 6). No fuerces el encaje.

**Objeto:** una sentencia firme que **hubiera reconocido una situación jurídica individualizada** a
favor de una o varias personas. **No** sirve una sentencia meramente **anulatoria** que no reconozca
una situación jurídica individualizada: comprueba el fallo, no el titular del asunto.

---

## 2. Requisitos (art. 110.1, letras a-c) — los tres, acumulativos

- **a) Identidad de situación jurídica.** Que los interesados se encuentren en **idéntica situación
  jurídica** que los favorecidos por el fallo. «Idéntica», no análoga ni similar. Es el requisito que
  más solicitudes tumba: no basta la misma norma o la misma categoría profesional; hay que acreditar
  identidad en **todos** los elementos determinantes del fallo (cuerpo/escala, puesto, período,
  concepto retributivo, hecho imponible, ejercicio, régimen aplicable...).
- **b) Competencia territorial del mismo órgano.** Que el **juez o tribunal sentenciador fuera también
  competente, por razón del territorio**, para conocer de las pretensiones de reconocimiento de esa
  situación individualizada del solicitante. → **Verifica el domicilio/destino del cliente frente al
  ámbito territorial del órgano.** Una sentencia excelente de otro TSJ **no es extensible**.
- **c) Plazo (§ 3).**

**Instrucción de trabajo:** construye una **tabla comparativa** solicitante ↔ favorecido por el fallo,
elemento a elemento, con el documento del expediente que acredita cada uno. Esa tabla **es** el
escrito. Si un elemento no coincide, dilo al cliente: la extensión se desestimará y habrá perdido el
tiempo (y su propio plazo, § 5). Usa la skill `cuadro-elementos` si ayuda.

---

## 3. ⚠️ El plazo — art. 110.1.c). Es el dato decisivo

> «Que soliciten la extensión de los efectos de la sentencia **en el plazo de UN AÑO desde la última
> notificación de ésta a quienes fueron parte en el proceso**. Si se hubiere interpuesto **recurso en
> interés de ley o de revisión**, este plazo se contará **desde la última notificación de la
> resolución que ponga fin a éste**.»

Cuatro consecuencias operativas:
1. El *dies a quo* **no** es la fecha de la sentencia, **ni** la de su firmeza, **ni** la de su
   publicación: es **la última notificación a quienes fueron parte**. Es un dato **que está en los
   autos y que el cliente no tiene**. → **Averíguala**: pídela al órgano, al letrado de la parte
   favorecida o mediante consulta de las actuaciones. **No la deduzcas ni la estimes.** Si no consta,
   **dilo y márcala `[verificar]`** antes de calcular nada.
2. Si medió **recurso en interés de ley o de revisión**, el año corre desde la última notificación de
   la resolución que le puso fin.
3. **Agosto no corre** (art. 128.2 LJCA: no corre plazo alguno de la Ley, salvo derechos
   fundamentales). Compruébalo al calcular.
4. **La solicitud se dirige DIRECTAMENTE al órgano jurisdiccional** (art. 110.2), no a la
   Administración. **⚠️ Corrige la creencia extendida:** la redacción anterior a la Ley 20/2013 exigía
   una **solicitud previa a la Administración** y un plazo posterior para acudir al juzgado. **Eso ya
   NO está en el texto vigente.** Hay **un solo plazo de un año** y **un solo destinatario: el órgano
   que dictó la resolución** cuya extensión se pretende. No pierdas el año pidiéndoselo antes a la
   Administración.

---

## 4. Tramitación (art. 110.2-110.4, 110.7)

1. **110.2 — Destinatario:** el **órgano jurisdiccional competente que hubiera dictado la resolución**
   de la que se pretende extender los efectos.
2. **110.3 — Escrito:** **escrito razonado** al que **deberá acompañarse el documento o documentos que
   acrediten la identidad de situaciones o la no concurrencia de alguna de las circunstancias del
   apartado 5**. → La carga documental es del solicitante y es **constitutiva**: sin documentos, no hay
   incidente. Aporta también el documento que acredita **la ausencia de acto firme y consentido**
   (§ 5).
3. **110.4 — Instrucción:** antes de resolver, **en los 20 días siguientes**, el LAJ recaba de la
   Administración los antecedentes y, **en todo caso, un informe detallado sobre la viabilidad de la
   extensión**; se pone de manifiesto el resultado a las partes para alegar por **plazo común de
   5 días**, con emplazamiento en su caso de los interesados directamente afectados. Evacuado el
   trámite, el juez o tribunal **resuelve por AUTO**, **sin poder reconocer una situación jurídica
   distinta de la definida en la sentencia firme**. → **Prepara la réplica al informe de viabilidad:
   son 5 días y es donde se gana el incidente.** Y **no pidas más de lo que dice el fallo**: la
   petición que excede del fallo se desestima.
4. **110.6 — Suspensión:** si está pendiente un **recurso de revisión** o un **recurso de casación en
   interés de la ley**, la decisión del incidente **queda en suspenso** hasta que se resuelva.
5. **110.7 — Recursos:** el régimen de recurso del auto se ajusta a las **reglas generales del
   art. 80 LJCA**. Verifícalo con `buscar_articulo("LJCA","80")` antes de indicar el recurso concreto
   `[verificar]`.

---

## 5. Causas TASADAS de desestimación (art. 110.5) — «se desestimará EN TODO CASO cuando…»

- **a) Cosa juzgada.**
- **b) Doctrina contraria a jurisprudencia superior:** cuando la **doctrina determinante del fallo**
  cuya extensión se postula fuere **contraria a la jurisprudencia del Tribunal Supremo** o a la
  **doctrina sentada por los Tribunales Superiores de Justicia en el recurso a que se refiere el
  art. 99** LJCA. → **Antes de solicitar, comprueba con `buscar_sentencias` que la doctrina del fallo
  no ha sido desautorizada por el TS.** Una sentencia firme puede ser extensible y aun así perder por
  esta letra si el TS ya dijo lo contrario. **Prohibido afirmarlo de memoria: verifica.**
- **c) ⚠️ ACTO FIRME Y CONSENTIDO — la trampa:** si **para el interesado** se hubiere dictado
  resolución que, **habiendo causado estado en vía administrativa, fuere consentida y firme por no
  haber promovido recurso contencioso-administrativo**.

> **Explícaselo al cliente sin rodeos.** Quien recibió su propio acto y **dejó pasar los 2 meses del
> art. 46 LJCA** sin recurrir **no puede colarse después por la extensión de efectos**. La institución
> no resucita plazos perdidos: sirve a quien **todavía no tiene** acto firme y consentido en contra —
> típicamente quien nunca pidió nada, o quien pidió y su procedimiento sigue vivo o su acto aún no ha
> ganado firmeza.
>
> **Consecuencia estratégica de primer orden:** si hay una sentencia favorable pendiente o previsible
> y al cliente **ya le han notificado su propio acto desestimatorio**, **NO le aconsejes esperar a la
> extensión de efectos: hay que recurrir en plazo.** Esperar convierte su acto en firme y consentido y
> **cierra las dos puertas a la vez**. La extensión se valora **después** de tener el plazo propio a
> salvo, nunca en su lugar. Comprueba SIEMPRE, antes de recomendar la vía del 110, si el cliente tiene
> un acto propio y en qué situación de plazo está.

---

## 6. Art. 111 LJCA — pleitos suspendidos por tramitación preferente («recurso testigo»)

Supuesto distinto y más favorable. Verificado:

> Cuando se hubiere acordado **suspender la tramitación de uno o más recursos** con arreglo al
> **art. 37.2** (pluralidad de recursos con idéntico objeto: el órgano tramita uno o varios con
> carácter **preferente** y suspende los demás), una vez **declarada la firmeza** de la sentencia
> dictada en el pleito tramitado preferentemente, el **LAJ requerirá a los recurrentes afectados por
> la suspensión** para que **en el plazo de CINCO DÍAS** interesen la **extensión de los efectos** de
> la sentencia, la **continuación del pleito suspendido**, o bien **manifiesten si desisten** del
> recurso.
> Si se solicita la extensión, **el juez o tribunal LA ACORDARÁ**, salvo que concurra la circunstancia
> del **art. 110.5.b)** (doctrina contraria a la jurisprudencia del TS o a la doctrina de TSJ ex
> art. 99) o alguna de las **causas de inadmisibilidad del art. 69** LJCA.

**Diferencias capitales con el art. 110 — no las confundas:**

| | **Art. 110** | **Art. 111** |
|---|---|---|
| Quién | Tercero que **no fue parte** | Recurrente **con recurso propio suspendido** ex art. 37.2 |
| Materias | Solo tributaria, personal y unidad de mercado | **Sin limitación de materia** |
| Plazo | **1 año** desde la última notificación | **5 días** desde el requerimiento del LAJ |
| Naturaleza | Facultad, con requisitos a-c | El juez **la acordará** (imperativo) |
| Obstáculos | Todas las causas del **110.5** (incluida la del acto firme y consentido) | Solo el **110.5.b)** y el **art. 69** |

- **Plazo de 5 días: es una trampa de agenda.** El requerimiento llega sin previo aviso. **Ten
  identificados los asuntos suspendidos ex art. 37.2** y responde en plazo. Ver también art. 37.3
  LJCA: firme la sentencia, el LAJ lleva testimonio a los recursos suspendidos y la notifica a los
  recurrentes afectados para que en **5 días** interesen la extensión, la continuación o desistan.
- **Regla de decisión:** pide la **extensión** si el fallo del pleito preferente le sirve al cliente;
  pide la **continuación** si el fallo le perjudica o si su caso tiene particularidades no resueltas
  en él (la extensión no puede reconocer situación distinta de la definida en la sentencia). **Desiste
  solo con instrucción expresa y escrita del cliente.**

---

## 7. Cuándo compensa la extensión frente a un recurso propio

**Compensa cuando:** existe sentencia **firme** en una de las **tres materias**; el fallo reconoce
**situación jurídica individualizada**; hay **identidad** documentable; el órgano es **territorialmente
competente** para el cliente; **queda plazo** dentro del año; y el cliente **no tiene** acto propio
firme y consentido. Ventajas: incidente de **ejecución** (no proceso nuevo), tramitación breve,
resolución por **auto**, sin fase de demanda ni vista, coste muy inferior.

**NO compensa / no cabe cuando:** la materia está fuera de las tres; el fallo es solo anulatorio; la
identidad es discutible; el órgano no es territorialmente competente; la doctrina del fallo choca con
el TS (110.5.b)); **o el cliente ya tiene acto firme y consentido** (110.5.c)).

**Cómo localizar la sentencia extensible:**
1. Búscala con **`buscar_sentencias`** (jurisdicción `CONTENCIOSO`; acota por `tipo_organo` y
   `provincia` conforme al requisito **territorial** del art. 110.1.b); usa `fecha_desde` para no traer
   sentencias fuera del año). Léela entera con **`leer_sentencias`**: **el fallo, no el resumen**.
2. **Verifica la FIRMEZA.** El buscador **no** acredita firmeza. Sin firmeza no hay extensión: hay que
   confirmarla en el órgano. **Márcala `[verificar]` mientras no conste.**
3. **Verifica la fecha de la última notificación a las partes** (§ 3) — no está en la base de datos.
4. **Comprueba que la doctrina no ha sido desautorizada por el TS** (110.5.b)) con una búsqueda
   posterior.
5. ⛔ **Prohibido inventar o citar de memoria ECLI, ROJ, fecha o ponente.** Si no se verifica, se
   escribe `[verificar]` y se dice abiertamente.

---

## 8. ⚠️ Conexión con la apelabilidad — art. 81.2.e) LJCA (verificado, en vigor 20-3-2024)

> **«Serán SIEMPRE susceptibles de apelación las sentencias que, CON INDEPENDENCIA DE LA CUANTÍA del
> procedimiento, sean susceptibles de extensión de efectos.»** (art. 81.2.e), letra **añadida por el
> RD-ley 6/2023**, en vigor **20-3-2024**.)

- **Rompe el umbral del art. 81.1.a)** (no apelables las sentencias de cuantía ≤ 30.000 €). Un asunto
  de personal o tributario de **cuantía pequeña** —abreviado, cuantía ≤ 30.000 €, aparentemente de
  instancia única— **es apelable** si la sentencia es susceptible de extensión de efectos.
- **Úsalo en dos direcciones:**
  1. **Al recurrir en apelación** una sentencia desfavorable de cuantía ≤ 30.000 € en materia
     tributaria, de personal o de unidad de mercado: **funda la admisibilidad en el art. 81.2.e)** y
     razona por qué la sentencia es susceptible de extensión (materia + reconocimiento de situación
     jurídica individualizada). Skill `recurso-apelacion-ca`, plazo **15 días** (art. 85.1 LJCA).
  2. **Al advertir al cliente** de que una sentencia favorable suya **puede ser apelada** por la
     Administración pese a la cuantía pequeña: no le prometas firmeza inmediata.
- **Advertencia de vigencia:** la letra e) es **posterior al 20-3-2024**. Cualquier nota o precedente
  anterior a esa fecha que diga que esas sentencias no son apelables por cuantía está **obsoleto**.

---

## 9. Salidas y entregables

- **Escritos:** solicitud de extensión de efectos del art. 110 (escrito razonado + tabla de identidad
  + documentos); alegaciones de 5 días al informe de viabilidad de la Administración (art. 110.4);
  escrito de respuesta al requerimiento del art. 111 (extensión / continuación / desistimiento);
  recurso contra el auto conforme al art. 80 `[verificar]`; escrito de apelación fundado en el
  art. 81.2.e).
- **Reparto para la redacción rápida:** solicitud del art. 110 en dos secciones: encabezamiento, sentencia cuya extensión se pide, materia, competencia territorial y plazo / tabla de identidad de situaciones con sus documentos, descarte de las causas del art. 110.5 y suplico. Las alegaciones de 5 días y la respuesta del art. 111 son escritos cortos: tú solo, en un único archivo.
- **Estilo:** los redactores aplican `estilo-escritos-judiciales` al escribir. **Entrega:** Word `.docx` maquetado, que genera el ensamblado de `redaccion-rapida`.
- **Normativa autonómica y local:** el conector **no la cubre** (BOE estatal + ordenanzas de
  municipios cubiertos). En materia de personal autonómico o tributos locales, **pide la norma al
  usuario y no la cites de memoria** `[verificar]`.
- **Datos personales:** cero datos reales. Usa `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`,
  `[EXPEDIENTE]`. No reproduzcas datos de los favorecidos por el fallo ajeno más allá de lo
  imprescindible para acreditar la identidad de situación. Ver `PROTECCION-DATOS.md`.
- **Perfil del despacho:** `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/`.
- **Anclas:** `references/anclas-normativas-ca.md` § 8 (ejecución), § 3 (umbrales), § 2.2 (agosto).
