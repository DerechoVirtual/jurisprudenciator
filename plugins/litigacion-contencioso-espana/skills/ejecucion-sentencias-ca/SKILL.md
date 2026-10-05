---
name: ejecucion-sentencias-ca
description: >-
  Asiste en la ejecución de sentencias contra la Administración obtenidas por el propio recurrente (arts. 103-113 LJCA) — requerimiento de ejecución, multas coercitivas, indemnización sustitutoria por imposibilidad legal o material, condenas dinerarias e incidente de ejecución. Activar con "ejecutar mi sentencia contra la Administración", "incidente de ejecución contencioso", "la Administración no cumple la sentencia que gané", "multas coercitivas", "art. 104 LJCA", "art. 108 LJCA", "ejecución forzosa del fallo". Requisito previo: FUISTE PARTE en el pleito y la sentencia es tuya. Si no litigaste y lo que quieres es que se te apliquen los efectos de una sentencia firme obtenida por un tercero en idéntica situación (arts. 110-111 LJCA), usar /extension-efectos-ca.
---

# Ejecución de sentencias contra la Administración (arts. 103-113 LJCA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Preceptos de la ejecución** → `buscar_articulo` (`ley="LJCA"`, artículos 103 a 113; artículos 84 y 91 para la ejecución provisional).
- **Imposibilidad, finalidad elusoria (art. 103.4) y falta de crédito** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`, `terminos="eludir su cumplimiento"`).
- **Fechar el acto o la disposición que elude la sentencia** → `buscar_boe` + `leer_boe` o `sumario_boe` (disposición estatal); `buscar_ordenanzas` + `leer_ordenanza` (ordenanza municipal).
- **Tipo del interés legal del dinero de cada año (art. 106.2)** → `buscar_boe` + `leer_boe` (Ley de Presupuestos Generales del Estado de cada ejercicio).
- **Ejecución sobre un inmueble** (demolición, reposición de la legalidad urbanística) → `consultar_catastro` (referencia catastral y construcciones afectadas).
- **Comprobación de las citas del escrito de ejecución o de extensión de efectos** → `verificar_escrito` lo pasa cada redactor sobre las frases de su sección que citan normas, y el ensamblado de `redaccion-rapida` comprueba que cada cita se leyó.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

---

Fase de ejecución en el contencioso. Plazos y cifras: `references/anclas-normativas-ca.md`. Lo no
anclado, verificarlo con `buscar_articulo` o marcarlo `[verificar]`.

> **Principio rector (art. 103, verificado):** las sentencias se ejecutan **en sus propios términos**.
> La potestad de hacer ejecutar corresponde **exclusivamente** a los juzgados y tribunales de este
> orden, y compete al que conoció en **primera o única instancia** (art. 103.1). Las partes están
> **obligadas a cumplirlas** en la forma y términos que en ellas se consignen (art. 103.2), y todas las
> personas y entidades, públicas y privadas, están obligadas a **prestar colaboración** (art. 103.3).

---

## 1. Bloque previo — cerrar ANTES de instar

1. **¿Es firme la sentencia?** La ejecución ordinaria presupone firmeza. (La **ejecución provisional**
   tiene régimen propio: **verificarlo con `buscar_articulo` — arts. 84 y 91 LJCA** — antes de afirmar
   nada.)
2. **¿Qué dice EXACTAMENTE el fallo?** La ejecución no amplía ni reinterpreta: se ejecuta **en sus
   propios términos** (art. 103.1). Transcribir el fallo literalmente y **trabajar sobre él**. Si el
   fallo es oscuro o incompleto, el cauce es la aclaración/complemento **en su momento**, no la
   ejecución. **Un fallo mal redactado es un problema de la instancia que se paga en ejecución** — al
   redactar cualquier suplico (art. 31 LJCA), pensar ya en cómo se ejecutará.
3. **¿Ante quién?** Ante el órgano de **primera o única instancia** (art. 103.1) — **no** ante la Sala
   que resolvió la apelación o la casación.
4. **¿Ha transcurrido el plazo?** Ver § 2. **⚠️ No es el mismo para condenas dinerarias.**
5. **¿Quién está legitimado?** Art. 104.2: **cualquiera de las partes Y las personas afectadas**.
   Art. 109.1 amplía: la Administración, las demás partes procesales y **las personas afectadas por el
   fallo**. No hace falta haber sido parte para promover el incidente del art. 109.
6. **¿Hay terceros en idéntica situación?** ⚠️ Comprobar **siempre** la **extensión de efectos**
   (§ 5): es la vía de mayor rendimiento del orden y se pasa por alto de forma sistemática.
7. **Agosto NO corre** (art. 128.2), salvo procedimiento de DDFF (agosto hábil).

## 2. Plazos para instar la ejecución forzosa — ⚠️ DOS reglas distintas

| Supuesto | Plazo | Norma (verificada) |
|---|---|---|
| **Regla general** | **2 meses** desde la comunicación de la sentencia al órgano obligado, **o** el plazo fijado en la propia sentencia conforme al art. 71.1.c) | **Art. 104.2** |
| **⚠️ Condena al pago de cantidad líquida** | **3 meses** desde que la sentencia firme sea **comunicada al órgano que deba cumplirla** — «**No obstante lo dispuesto en el artículo 104.2**» | **Art. 106.3** |
| Plazo inferior | La sentencia **puede fijar un plazo menor** cuando el de dos meses la haga ineficaz o cause grave perjuicio | **Art. 104.3** |

- **Art. 104.1:** firme la sentencia, el LAJ la comunica **en 10 días** al **órgano previamente
  identificado como responsable de su cumplimiento**, para que la lleve a puro y debido efecto.
- **Consecuencia práctica:** en una condena dineraria, instar la ejecución a los 2 meses es prematuro;
  esperar a los 3. En una condena no dineraria, esperar 3 meses regala un mes. **No mezclarlos.**
- **Dies a quo:** se cuenta desde la **comunicación al órgano**, no desde la notificación a la parte.
  Pedir en autos la constancia de esa fecha si no consta.

## 3. Herramientas de ejecución

### 3.1 Requerimiento e incidente (arts. 104, 109)

- **Incidente de ejecución (art. 109.1, verificado):** mientras no conste en autos la **total ejecución**,
  la Administración, las demás partes y **las personas afectadas por el fallo** pueden promover
  incidente para decidir, **sin contrariar el contenido del fallo**, cuantas cuestiones se planteen y
  **especialmente**: **a)** el **órgano** que ha de responsabilizarse de las actuaciones; **b)** el
  **plazo máximo** de cumplimiento, atendidas las circunstancias; **c)** los **medios** y el
  **procedimiento** a seguir.
- **Tramitación (art. 109.2-3):** traslado a las partes por plazo común **no superior a 20 días**;
  **auto en 10 días** decidiendo la cuestión.
- ⚠️ **«Sin contrariar el contenido del fallo»** es el límite duro. Usar la ejecución para obtener lo que
  no se pidió, o para corregir un fallo insuficiente, se rechaza. **Pedir en ejecución lo que el fallo
  concede** — y pedirlo **concretado**: órgano, plazo y medios (las tres letras del art. 109.1).

### 3.2 ⚠️ Multas coercitivas y responsabilidad personal (art. 112, verificado)

Transcurridos los plazos para el **total cumplimiento** del fallo, el órgano, **previa audiencia de las
partes**, adopta las medidas necesarias para lograr la efectividad de lo mandado. **Singularmente**,
**acreditada su responsabilidad** y **previo apercibimiento del LAJ notificado personalmente** para
formular alegaciones, el Juez o la Sala podrán:

- **a) Imponer multas coercitivas de 150 a 1.500 euros** a las **autoridades, funcionarios o agentes**
  que incumplan los requerimientos, **y reiterarlas hasta la completa ejecución** del fallo, sin
  perjuicio de otras responsabilidades patrimoniales. Les es aplicable lo previsto en el **art. 48**.
- **b) Deducir el oportuno testimonio de particulares** para exigir la **responsabilidad penal** que
  pudiera corresponder.

> **Cómo se usa de verdad:** la multa se dirige **a la persona física** —autoridad, funcionario o
> agente—, **no a la Administración**. Ahí está su eficacia: el importe es modesto, pero es **personal**
> y **reiterable**. Por eso el escrito debe **identificar al responsable concreto** —lo que enlaza con
> el art. 109.1.a)— y pedir el **apercibimiento personal** del art. 112. Pedir «multas coercitivas a la
> Administración» es pedir mal.
> **Requisitos formales que no se pueden saltar:** (i) transcurso de los plazos; (ii) **audiencia de las
> partes**; (iii) **responsabilidad acreditada**; (iv) **apercibimiento previo del LAJ notificado
> personalmente**. Pedirlos expresamente en el suplico.

### 3.3 ⚠️ Nulidad de pleno derecho de los actos que eluden la sentencia (art. 103.4-5, verificado)

- **Art. 103.4:** «Serán **nulos de pleno derecho** los actos y disposiciones **contrarios a los
  pronunciamientos de las sentencias**, que se dicten **con la finalidad de eludir su cumplimiento**.»
- **Art. 103.5:** el órgano al que corresponda la ejecución **declarará, a instancia de parte**, esa
  nulidad, **por los trámites previstos en los apartados 2 y 3 del art. 109** (traslado ≤ 20 días, auto
  en 10 días), **salvo que careciese de competencia** para ello conforme a la LJCA.
- **Es un arma de primer orden y muy infrautilizada.** Cuando la Administración, en vez de cumplir,
  dicta un **acto nuevo** que reproduce el anulado con otro ropaje —o una **disposición** que neutraliza
  el fallo—, **no hay que impugnarlo en un pleito nuevo**: se pide la **declaración de nulidad en la
  propia ejecución**, ante el mismo órgano, por el trámite del art. 109.2-3. Ahorra años.
- **⚠️ El requisito crítico es la FINALIDAD ELUSORIA.** No basta con que el acto sea contrario al fallo:
  hay que **acreditar que se dictó para eludir su cumplimiento**. Se prueba con **indicios**:
  cronología (acto inmediatamente posterior a la sentencia), identidad sustancial de contenido con el
  anulado, ausencia de motivación nueva, reiteración del mismo vicio ya declarado. **Construir la
  cronología con folios** y exponerla como tal.
- Si el órgano carece de competencia (art. 103.5 *in fine*), decirlo y reconducir.

### 3.4 Imposibilidad de ejecutar e indemnización sustitutoria (art. 105, verificado)

- **Art. 105.1 — punto de partida:** «**No podrá suspenderse el cumplimiento ni declararse la inejecución
  total o parcial del fallo.**» Es una regla imperativa: la inejecución es **excepcional** y tasada.
- **Art. 105.2 — imposibilidad material o legal:** el órgano obligado **lo manifiesta a la autoridad
  judicial a través del representante procesal de la Administración**, **dentro del plazo del art. 104.2**
  (2 meses). El Juez o Tribunal, **con audiencia de las partes y de quienes considere interesados**,
  aprecia si concurren o no dichas causas, **adopta las medidas necesarias que aseguren la mayor
  efectividad de la ejecutoria** y fija, **en su caso**, la **indemnización** que proceda **por la parte
  en que no pueda ser objeto de cumplimiento pleno**.
- **⚠️ Posición de la parte (crítica):** la imposibilidad es la **vía de escape favorita** de la
  Administración. Combatirla en tres frentes, por este orden:
  1. **Extemporaneidad:** debió alegarse **dentro del plazo del art. 104.2**. Si llega después, decirlo.
  2. **Inexistencia de imposibilidad**: la imposibilidad ha de ser **material o legal**, **objetiva** y
     **sobrevenida**. **No lo son** —y hay que decirlo así— la **dificultad**, la **inconveniencia**, el
     **coste**, la **falta de consignación presupuestaria** ni la **oposición de terceros**. La
     imposibilidad **creada por la propia Administración** tras la sentencia no puede beneficiarla:
     enlazar con el **art. 103.4**.
  3. **Subsidiariamente**: si hay imposibilidad **parcial**, exigir las **medidas de mayor efectividad**
     de la ejecutoria (art. 105.2) **y** la indemnización **solo por la parte incumplible** — no aceptar
     que se convierta todo el fallo en dinero.
- **Art. 105.3 — expropiación de derechos reconocidos en sentencia firme:** causas **tasadas** de
  utilidad pública o interés social: **peligro cierto de alteración grave del libre ejercicio de los
  derechos y libertades**, **temor fundado de guerra** o **quebranto de la integridad del territorio
  nacional**. Declaración por el **Gobierno de la Nación** (o el **Consejo de Gobierno** de la CCAA solo
  en el primer supuesto y respecto de actos de esa Comunidad o de sus entidades locales), **dentro de
  los 2 meses** siguientes a la comunicación de la sentencia. El órgano judicial señala la indemnización
  por el trámite de los incidentes. Es **excepcionalísimo**: si se invoca fuera de esos tres supuestos,
  denunciarlo.

### 3.5 Condenas dinerarias (art. 106, verificado)

- **106.1:** pago con cargo al crédito correspondiente del presupuesto, que tiene **siempre** la
  consideración de **ampliable**. Si es precisa **modificación presupuestaria**, debe concluirse el
  procedimiento **dentro de los 3 meses** siguientes a la notificación de la resolución judicial.
  ⚠️ **Argumento clave:** el crédito es **ampliable** por ley — la falta de partida **no** es
  imposibilidad material ni legal (art. 105).
- **106.2:** se añade el **interés legal del dinero**, **desde la fecha de notificación de la sentencia
  dictada en única o primera instancia**. ⚠️ **Desde la de instancia**, no desde la firmeza: si el
  asunto pasó por apelación o casación, son años de intereses. **Reclamarlo expresamente y calcularlo**.
- **106.3:** transcurridos **3 meses** desde la comunicación de la sentencia firme, cabe instar la
  ejecución forzosa; y el órgano judicial, **oído el órgano encargado**, **podrá incrementar en DOS
  PUNTOS el interés legal** a devengar **si aprecia falta de diligencia** en el cumplimiento.
  ⚠️ **Pedirlo siempre que haya demora**, alegando y **acreditando** la falta de diligencia.
- **106.4:** si la Administración estima que el pago produciría **trastorno grave a su Hacienda**, lo
  pone en conocimiento del órgano con **propuesta razonada**, y, **oídas las partes**, se resuelve sobre
  el modo **menos gravoso** de ejecutar. No es una excusa para no pagar: es un modo de pago.
- **106.5:** lo anterior se aplica también a la **ejecución provisional**.
- **106.6:** cualquiera de las partes puede pedir la **compensación** con créditos que la Administración
  ostente contra el recurrente. ⚠️ Comprobarlo antes: puede convenir o perjudicar al cliente.

### 3.6 Condenas a hacer o a dar (arts. 108-109)

- **Verificar el contenido exacto del art. 108 con `buscar_articulo`** antes de citar apartados
  (ejecución subsidiaria a costa de la Administración, plazos, actuaciones materiales). No darlo por sabido.
- Concretar siempre, vía art. 109.1: **órgano** responsable, **plazo** máximo y **medios**.

---

## 4. ⚠️ EXTENSIÓN DE EFECTOS A TERCEROS (arts. 110-111) — la vía de mayor rendimiento

Permite que los efectos de una sentencia firme que reconoció una **situación jurídica individualizada**
se extiendan a **otras personas** en idéntica situación, **en ejecución de la sentencia** y **sin pleito
nuevo**. Un solo pleito ganado puede resolver decenas de situaciones.

### 4.1 Materias — ⚠️ SON TRES, no dos

Art. 110.1 (texto verificado): «**En materia tributaria, de personal al servicio de la Administración
pública y de unidad de mercado** …»

> ⚠️ **La «unidad de mercado» se olvida sistemáticamente.** La añadió la **Ley 20/2013**. Muchas fuentes
> —y versiones anteriores de este plugin— solo mencionan **personal** y **tributaria**. **Son tres.**
> Comprobarlo antes de descartar la vía.
>
> Fuera de esas tres materias, **no cabe** extensión de efectos por el art. 110.

### 4.2 Requisitos (art. 110.1, verificado) — acumulativos

- **a)** Que los interesados se encuentren en **idéntica situación jurídica** que los favorecidos por el
  fallo. ⚠️ **«Idéntica», no «análoga» ni «similar».** Es el filtro real: hay que acreditar la identidad
  **de hecho y de régimen jurídico**, punto por punto, con documentos.
- **b)** Que el juez o tribunal sentenciador **fuera también competente, por razón del territorio**, para
  conocer de sus pretensiones de reconocimiento de dicha situación individualizada.
- **c)** ⚠️ Que **soliciten la extensión en el plazo de UN AÑO desde la última notificación de la
  sentencia a quienes fueron parte** en el proceso. Si se interpuso recurso en interés de ley o de
  revisión, el año cuenta **desde la última notificación de la resolución que le ponga fin**.
  **Es un plazo fatal y sorprendente:** corre desde la **notificación a los que fueron parte**, no desde
  que el tercero conoce la sentencia. **Calendarlo el día en que la sentencia gana firmeza** y avisar de
  inmediato a todos los clientes en idéntica situación.

### 4.3 Tramitación (art. 110.2-4, 110.7)

- **110.2:** la solicitud se dirige **directamente al órgano jurisdiccional** que dictó la resolución
  cuyos efectos se pretende extender.
- **110.3:** **escrito razonado**, al que se acompañan **los documentos que acrediten la identidad de
  situaciones** o la **no concurrencia** de alguna de las circunstancias del art. 110.5.
  ⚠️ **La carga documental es del solicitante y se resuelve por escrito**: el expediente de la extensión
  **es el escrito y sus documentos**. Prepararlo con el mismo rigor que una demanda.
- **110.4:** el LAJ recaba de la Administración, **en los 20 días siguientes**, los antecedentes y **en
  todo caso un informe detallado sobre la viabilidad** de la extensión; se pone de manifiesto a las
  partes para alegar por **plazo común de 5 días**, con emplazamiento en su caso de los interesados
  directamente afectados. Evacuado el trámite, el Juez o Tribunal resuelve **por auto**, **en el que no
  podrá reconocerse una situación jurídica distinta a la definida en la sentencia firme**.
- **110.7:** el régimen de recurso del auto se ajusta a las reglas generales del **art. 80**.
  ⚠️ Y el **art. 80.2**: la apelación de los autos de los arts. 110 y 111 se rige por **el mismo régimen
  de admisión que corresponda a la sentencia cuya extensión se pretende**. Enlaza con el **art. 81.2.e)**
  —sentencias susceptibles de extensión de efectos, **siempre apelables**— añadido por el RD-ley 6/2023
  (en vigor 20-3-2024). Ver `recurso-apelacion-ca`.

### 4.4 ⚠️ Causas de desestimación «en todo caso» (art. 110.5, verificado)

El incidente **se desestimará, en todo caso**, cuando concurra alguna de estas:

- **a)** Si existiera **cosa juzgada**.
- **b)** Cuando la **doctrina determinante del fallo** cuya extensión se postula fuere **contraria a la
  jurisprudencia del Tribunal Supremo** o a la doctrina sentada por los TSJ en el recurso del **art. 99**.
- **c)** ⚠️ Si para el interesado se hubiere dictado resolución que, **habiendo causado estado en vía
  administrativa, fuere consentida y firme** por **no haber promovido recurso contencioso-administrativo**.

> **La letra c) es la trampa mortal, y es de gestión de despacho, no de argumentación.** El tercero que
> dejó firme **su propio** acto —por no recurrirlo en plazo— **no puede** aprovechar la sentencia ajena,
> por idéntica que sea su situación. **Cribar esto ANTES de prometer nada al cliente.** Y, en sentido
> inverso: cuando hay un pleito piloto en marcha en materia de personal, tributaria o de unidad de
> mercado, **hay que recurrir el acto de cada afectado para no perder la letra c)**. Es un consejo que
> se da **antes**, no después.
- **110.6:** si está pendiente un recurso de revisión o de casación en interés de la ley, la decisión del
  incidente **queda en suspenso** hasta que se resuelva.

### 4.5 Art. 111

- **Verificar su contenido con `buscar_articulo`** antes de invocarlo (supuesto de pleitos suspendidos
  por remisión de un recurso testigo). No citarlo de memoria.

---

## 5. Errores típicos que pierden el asunto

1. **Instar la ejecución de una condena dineraria a los 2 meses** (son **3**, art. 106.3) o esperar 3
   meses en una condena no dineraria (bastan **2**, art. 104.2).
2. **No reclamar el interés legal desde la sentencia de instancia** (art. 106.2) ni los **2 puntos** de
   incremento por falta de diligencia (art. 106.3).
3. **Aceptar la «falta de crédito presupuestario»** como imposibilidad: el crédito es **ampliable**
   (art. 106.1).
4. **Pedir multas coercitivas «a la Administración»** en vez de a la **autoridad, funcionario o agente**
   identificado, y sin pedir el **apercibimiento personal previo** del art. 112.
5. **Impugnar en pleito nuevo el acto que elude la sentencia**, en vez de pedir su **nulidad de pleno
   derecho en la propia ejecución** (art. 103.4-5).
6. **Alegar el art. 103.4 sin acreditar la finalidad elusoria** — no basta la contradicción con el fallo.
7. **No combatir la extemporaneidad** de la alegación de imposibilidad (art. 105.2 remite al plazo del
   art. 104.2).
8. **Pedir en ejecución lo que el fallo no concede** → se rechaza (art. 109.1: «sin contrariar el
   contenido del fallo»). El problema nació al redactar el suplico.
9. **⚠️ Perder el año del art. 110.1.c)** para la extensión de efectos: corre desde la **última
   notificación a quienes fueron parte**.
10. **Descartar la extensión de efectos por creer que solo cubre personal y tributaria** — también
    **unidad de mercado**.
11. **Prometer una extensión de efectos a quien dejó firme y consentido su propio acto** (art. 110.5.c).
12. **Confundir «idéntica» con «similar»** situación jurídica (art. 110.1.a).
13. **Dirigir la ejecución a la Sala de apelación o casación** en vez de al órgano de instancia
    (art. 103.1).

## 6. Anclaje al expediente y a los autos

- **Todo hecho afirmado va con folio.** En ejecución, **triple anclaje**: `(folio X de los autos)`,
  `(doc. núm. Y del expediente administrativo, folio Z)` y **`(folio de la pieza de ejecución)`**.
- **Transcribir el fallo literalmente** al inicio del escrito, con su folio. Todo lo que se pida debe
  poder leerse en él.
- **Cronología del incumplimiento con folios y fechas**: comunicación al órgano (art. 104.1),
  requerimientos, respuestas, silencios. Es la prueba de la falta de diligencia (art. 106.3) y del
  presupuesto del art. 112.
- Para el **art. 103.4**, la cronología **es** la prueba de la finalidad elusoria: construirla con fechas
  y folios, no con adjetivos.
- Para la **extensión de efectos**, la identidad de situaciones se acredita **documento a documento**
  (art. 110.3): tabla comparativa entre el favorecido por el fallo y `[CLIENTE]`.

## 7. Estructura del escrito y SUPLICO

**Estructura:**

1. **Encabezamiento:** órgano de **primera o única instancia** (art. 103.1); procurador y letrado; autos
   y número de ejecución si ya existe pieza.
2. **Identificación de la sentencia firme:** órgano, número, fecha, **fecha de firmeza** y **fecha de
   comunicación al órgano obligado** (art. 104.1) — de ahí se computa todo.
3. **TRANSCRIPCIÓN LITERAL DEL FALLO.**
4. **HECHOS:** cronología del incumplimiento, **con folio**; actuaciones de la Administración; actos
   dictados tras la sentencia (para el art. 103.4).
5. **FUNDAMENTOS:** art. 103 (propios términos) · art. 104.2 o 106.3 (plazo) · art. 109 (incidente y las
   tres letras) · art. 112 (multas, con responsable identificado) · art. 103.4-5 (nulidad, si procede) ·
   art. 106 (intereses e incremento) · oposición al art. 105 si se ha alegado imposibilidad.
6. **SUPLICO.**
7. **OTROSÍES:** documentos; designación electrónica; en su caso, **extensión de efectos** por escrito
   separado dirigido al órgano sentenciador (art. 110.2).

**Reparto para la redacción rápida:** encabezamiento, identificación de la sentencia firme, transcripción del fallo y cronología del incumplimiento con folios · una sección por herramienta que se pida (plazo y incidente del art. 109, multas del art. 112, nulidad del art. 103.4-5, intereses del art. 106, oposición a la imposibilidad del art. 105) · cierre con suplico y otrosíes. La extensión de efectos (art. 110) es un escrito separado: encabezamiento y tabla de identidad de situaciones, requisitos y plazo, y suplico.

**SUPLICO — ejecución (modelo):**

> **SUPLICO AL JUZGADO/A LA SALA** que, teniendo por presentado este escrito, se sirva admitirlo, tener
> por **instada la EJECUCIÓN FORZOSA** de la sentencia núm. [X], de [FECHA], firme, y, previos los
> trámites del **art. 109 LJCA**, dictar auto por el que:
>
> **1.º** **Requiera** a **[ÓRGANO]** para que lleve a puro y debido efecto el fallo **en sus propios
> términos** (art. 103.1 LJCA), realizando **[ACTUACIÓN]**.
> **2.º** **Determine**, conforme al **art. 109.1 LJCA**: **a)** el **órgano** responsable de realizar
> las actuaciones; **b)** el **plazo máximo** de cumplimiento, que se interesa sea de **[PLAZO]**;
> **c)** los **medios** y el **procedimiento** a seguir.
> **3.º** **[Condenas dinerarias]** Acuerde el pago de **[IMPORTE]**, **más el interés legal del dinero
> desde la fecha de notificación de la sentencia dictada en primera instancia** (**art. 106.2 LJCA**),
> **e incremente en DOS PUNTOS** el interés legal a devengar, al concurrir **falta de diligencia** en el
> cumplimiento (**art. 106.3 LJCA**), según resulta de la cronología del hecho [N].
> **4.º** **Aperciba personalmente**, a través del LAJ y para formulación de alegaciones, a
> **[AUTORIDAD/FUNCIONARIO RESPONSABLE]** y, acreditada su responsabilidad y previa audiencia de las
> partes, **imponga multa coercitiva** de **[150 a 1.500 €]**, **reiterable hasta la completa ejecución**
> del fallo (**art. 112.a LJCA**), sin perjuicio de deducir testimonio de particulares (**art. 112.b**).
> **5.º** **[Si hay acto elusorio]** **Declare la NULIDAD DE PLENO DERECHO** de **[ACTO]**, de **[FECHA]**,
> por ser contrario a los pronunciamientos de la sentencia y haberse dictado **con la finalidad de eludir
> su cumplimiento**, conforme al **art. 103.4 y 103.5 LJCA**, por los trámites de los apartados 2 y 3 del
> art. 109.
> **6.º** Con **imposición de costas** del incidente a la Administración ejecutada.

**SUPLICO — extensión de efectos (escrito separado, art. 110.2):**

> **SUPLICO A LA SALA/AL JUZGADO** que, teniendo por presentado este **escrito razonado** y los
> documentos que se acompañan, acreditativos de la **identidad de situación jurídica** y de la **no
> concurrencia** de las circunstancias del **art. 110.5 LJCA**, se sirva admitirlo y tener por
> **solicitada la EXTENSIÓN DE LOS EFECTOS** de la sentencia firme núm. [X], de [FECHA], a favor de
> **[CLIENTE]**, conforme al **art. 110 LJCA**, por hallarse en **idéntica situación jurídica** que
> **[FAVORECIDO POR EL FALLO]** en materia de **[tributaria / personal al servicio de la Administración
> pública / unidad de mercado]**, ser este órgano **competente por razón del territorio** y formularse la
> solicitud **dentro del plazo de un año** desde la última notificación de la sentencia a quienes fueron
> parte; y, previos los trámites del **art. 110.4 LJCA**, dictar **auto** por el que se **extiendan a
> [CLIENTE] los efectos** de dicha sentencia, **reconociéndole [SITUACIÓN JURÍDICA, en los términos
> definidos en el fallo]**, con **[IMPORTE / EFECTOS ECONÓMICOS]** e intereses, y con imposición de
> costas a la Administración.

- **Congruencia (art. 31 LJCA):** en ejecución se materializa lo que el fallo declaró — **anulación** +
  **reconocimiento de la situación jurídica individualizada** + **indemnización** cuando proceda. Si el
  fallo no reconoció la situación individualizada, la ejecución **no puede crearla** (art. 109.1;
  art. 110.4 *in fine*: no cabe reconocer una situación distinta a la definida en la sentencia).
  **Ese es el motivo por el que el suplico de la demanda debe pedir siempre el art. 31.2.**
- **Costas del incidente:** rige el **art. 139.1** (el órgano resuelve también por auto los incidentes),
  con el **tope del art. 139.4**: máximo **un tercio de la cuantía del proceso por cada favorecido**;
  cuantía indeterminada = **18.000 €** a esos solos efectos, salvo razonamiento por complejidad.
  **Nunca** al Ministerio Fiscal (art. 139.6). Exacción frente a particulares por **vía de apremio**
  (art. 139.5); tasación conforme a la **LEC** (art. 139.7).

## 8. Reglas de la casa

- **Protección de datos:** cero datos reales. Marcadores `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`,
  `[IMPORTE]`, `[TERCERO]`. ⚠️ En el art. 112 hay que **identificar a la autoridad o funcionario
  responsable**: usar `[AUTORIDAD RESPONSABLE]` en el borrador y que el usuario complete el dato real.
- **Jurisprudencia:** verificar con `buscar_sentencias` / `buscar_por_cita` antes de citar. Prohibido
  inventar ECLI/ROJ/fecha/ponente. Sin verificación → `[verificar]` y decirlo.
- **Normativa autonómica y local:** el conector no la cubre. Pedírsela al usuario; no citarla de memoria.
- **Nada de MASC:** requisito del orden civil; no existe aquí.
- **Entregable:** Word `.docx` maquetado, que genera el ensamblado de `redaccion-rapida`.
