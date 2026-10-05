---
name: autorizacion-entrada-domicilio-ca
description: >-
  Procedimiento AUTÓNOMO de autorización judicial de entrada en domicilio y lugares de acceso restringido del art. 8.6 LJCA — oposición del afectado a la autorización pedida por la Administración (ejecución forzosa de actos, entrada de la Administración Tributaria incluso previa al inicio formal del procedimiento, inspección de la CNMC, ratificación de medidas sanitarias) e impugnación posterior de la entrada que excedió de lo autorizado. Activar con "autorización de entrada en domicilio", "art. 8.6 LJCA", "entrada de Hacienda en la empresa", "la Inspección quiere entrar", "nos han pedido autorización judicial de entrada", "oponernos a la entrada", "registro de la CNMC", "ratificación de medidas sanitarias", "van a entrar a ejecutar la demolición", "han entrado más allá de lo autorizado". Su objeto es la entrada física, no el acto que se ejecuta: si lo que se pretende es suspender la ejecutividad del acto administrativo mientras se recurre, usar /medidas-cautelares-ca.
---

# Autorización judicial de entrada en domicilio (art. 8.6 LJCA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Presupuestos legales de la entrada** → `buscar_articulo` (`ley="LJCA"`, `articulo="8"`; `ley="LPAC"`, artículos 99 y 100).
- **Entrada de la Administración Tributaria** → `buscar_articulo` (`ley="LGT"`, artículos 113 y 142) antes de citar su redacción vigente.
- **Doctrina del TS sobre entrada tributaria, autorizaciones prospectivas y domicilio de la persona jurídica** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`, `fecha_desde="dd/mm/aaaa"` posterior a la reforma de la LGT) + `leer_sentencias` (`parrafos=3`, `terminos="entrada en domicilio"`).
- **Inviolabilidad del domicilio (art. 18.2 CE)** → `buscar_sentencias` (`base="TC"`) + `leer_sentencias` (`parrafos=3`).
- **Orden de ejecución o demolición fundada en una ordenanza** → `buscar_ordenanzas` + `leer_ordenanza` con `articulo`.
- **Petición subsidiaria de acotación: qué dependencias hay** → `consultar_catastro` (referencia catastral o dirección: desglose de construcciones por planta, puerta y uso).
- **Resoluciones que cite la solicitud de la Administración** → `buscar_por_cita` sobre cada ECLI o ROJ antes de contestarlas.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

---

Anclas: `references/anclas-normativas-ca.md` (§ 10). Lo que no esté allí, verifícalo con
`buscar_articulo` o márcalo `[verificar]`.

> 🚨 **URGENCIA — leer antes que nada.** Estos procedimientos son **rapidísimos**: el escrito de
> oposición se prepara **en horas, no en días**. Cuando el cliente avisa, la solicitud suele estar ya
> presentada. **En este orden:** (1) fecha y hora exactas en que supo de la solicitud; (2) personarse
> **ya** y pedir **vista de las actuaciones** — sin ver la solicitud no cabe oposición seria; (3)
> comprobar si ya hay auto dictado y, si lo hay, cambiar de estrategia (§ 5.2). **No** gastar las
> primeras horas en doctrina: gastarlas en **conseguir el expediente y datar los hechos**.

---

## 1. Los cuatro supuestos del art. 8.6 (verificado)

Conocen los **Juzgados de lo Contencioso-administrativo** de:

| | Supuesto | Requisito específico |
|---|---|---|
| **a)** | **Entrada en domicilios y restantes lugares cuyo acceso requiera el consentimiento de su titular**, siempre que proceda para la **ejecución forzosa de actos de la Administración** | ⚠️ **Salvo** ejecución de **medidas de protección de menores** acordadas por la **Entidad Pública competente** |
| **b)** | **Autorización o ratificación de medidas sanitarias** que las autoridades sanitarias consideren **urgentes y necesarias para la salud pública** e impliquen **limitación o restricción de derechos fundamentales** | Solo si están plasmadas en **actos administrativos SINGULARES** que afecten **únicamente a uno o varios particulares concretos e identificados de manera individualizada** |
| **c)** | **Entrada e inspección** de domicilios, locales, terrenos y medios de transporte acordada por la **CNMC** | Cuando, requiriendo el acceso el consentimiento del titular, **este se oponga o exista riesgo de tal oposición** |
| **d)** | **Entrada en domicilios y otros lugares constitucionalmente protegidos** acordada por la **Administración Tributaria** en una actuación o procedimiento de aplicación de los tributos **aun con carácter previo a su inicio formal** | Cuando, requiriendo el acceso el consentimiento del titular, **este se oponga o exista riesgo de tal oposición** |

> **Detalle que se pasa por alto y es oponible:** en **c)** y **d)** la ley exige **oposición o riesgo de
> oposición**. Si no consta ninguna de las dos —p. ej. nunca se pidió el consentimiento— **falta un
> presupuesto legal** de la autorización. Alegarlo.
>
> **Ámbito objetivo:** «domicilio **y restantes lugares cuyo acceso requiera el consentimiento de su
> titular**» — no se agota en la vivienda: alcanza al **domicilio constitucionalmente protegido de las
> personas jurídicas**. Su alcance exacto y el de las distintas dependencias es **jurisprudencial**:
> verificar con `buscar_sentencias`, **no afirmarlo de memoria**.

---

## 2. Marco constitucional y sustantivo

- **Art. 18.2 CE (verificado):** «El domicilio es inviolable. **Ninguna entrada o registro podrá hacerse
  en él sin consentimiento del titular o resolución judicial**, salvo en caso de flagrante delito.» La
  autorización es **garantía de un derecho fundamental**, no un trámite: el juez **no visa, controla**.
- **Art. 99 LPAC (verificado):** las Administraciones podrán proceder, **«previo apercibimiento»**, a la
  ejecución forzosa, **salvo** cuando se **suspenda la ejecución** conforme a la Ley **o cuando la
  Constitución o la Ley exijan la intervención de un órgano judicial**. → ⚠️ **Tres excepciones
  oponibles en un solo precepto:** (1) **falta de apercibimiento previo** —requisito legal expreso, no
  formalidad—; (2) **acto suspendido** —comprobar SIEMPRE si hay cautelar concedida o suspensión en vía
  administrativa—; (3) intervención judicial exigida.
- **Art. 100 LPAC (verificado):**
  - **100.1** — la ejecución forzosa se efectuará **«respetando siempre el principio de
    proporcionalidad»**, por: a) apremio sobre el patrimonio; b) ejecución subsidiaria; c) multa
    coercitiva; d) compulsión sobre las personas. La proporcionalidad está **en el texto de la ley**.
  - **100.2** — si fueran **varios los medios admisibles**, se elegirá **el menos restrictivo de la
    libertad individual**. **Argumento de oro:** si el fin podía alcanzarse sin entrar (multa coercitiva,
    apremio, ejecución subsidiaria desde el exterior), la entrada **no es el medio menos restrictivo**.
  - **100.3** — si fuese necesario entrar en el domicilio o lugares que requieran autorización del
    titular, deberán obtener **su consentimiento o, en su defecto, la oportuna autorización judicial**.
    Es el engarce LPAC ↔ art. 8.6 LJCA.

**Qué controla el juez** (canon construido sobre esos preceptos y el art. 18.2 CE; su formulación acabada
es **jurisprudencial** — verificar con `buscar_sentencias` antes de citarla):

1. **Acto administrativo válido, ejecutivo y que precise la entrada** (salvo el supuesto tributario
   previo, § 4). 2. **Notificación previa y apercibimiento** (art. 99). 3. **Que el acto no esté
   suspendido.** 4. **Necesidad.** 5. **Idoneidad.** 6. **Proporcionalidad estricta y medio menos
   restrictivo** (100.1-100.2). 7. **Determinación del objeto:** qué inmueble, qué alcance material,
   **qué límite temporal**.

---

## 3. ⚠️ Objeto limitado — el error argumental más frecuente

**El procedimiento del art. 8.6 NO juzga la legalidad del acto de fondo.** Solo decide **si procede la
entrada**: es un juicio sobre el **medio ejecutivo**, no sobre el acto ejecutado.

- **No plantear aquí** que la sanción es injusta, la liquidación errónea o los hechos falsos. El juez de
  la entrada **no puede entrar en eso**: hacerlo **desperdicia el escrito** y delata desconocimiento del
  cauce.
- **El fondo va por su cauce:** recurso administrativo, recurso contencioso y, sobre todo, **medida
  cautelar de suspensión** (`medidas-cautelares-ca`).
- **La frontera, bien trazada:** sí cabe alegar que **no existe acto**, que **no es ejecutivo**, que **no
  fue notificado**, que **está suspendido** o que **no requiere la entrada** — no es el fondo, son
  **presupuestos de la ejecución**. La **nulidad de pleno derecho manifiesta** está en el límite:
  sostenible solo si es palmaria y **articulada como ausencia de título ejecutivo válido**, nunca como
  discrepancia de fondo. Alcance: **jurisprudencial** — verificar.

> **Operativo:** el cliente siempre querrá discutir el fondo. Explicarle la separación de cauces **por
> escrito** y abrir **en paralelo** la impugnación del acto con petición cautelar. **La cautelar
> concedida desactiva la entrada** vía art. 99 LPAC (acto suspendido): es **la jugada más eficaz**. Las
> dos vías a la vez, no una después de otra.

---

## 4. Perfil tributario (art. 8.6.d) — el más litigioso

Permite la entrada acordada por la **Administración Tributaria** «aun con carácter previo al inicio
formal» del procedimiento. Es el frente más conflictivo y donde el control debe ser **más estricto**,
precisamente porque la garantía ordinaria —un procedimiento en marcha y notificado— **puede faltar**.

- **Motivación reforzada y singularizada.** Sin procedimiento iniciado, el único contrapeso es la
  motivación de la solicitud: exigir **indicios concretos y datados** referidos a **este** obligado.
  Fórmulas de estilo, ratios sectoriales o «discrepancias con la media del sector» **no son indicios**:
  son estadística.
- **Sospechar de las autorizaciones PROSPECTIVAS o GENÉRICAS.** Atacar: entrada «para comprobar la
  situación tributaria» **sin objeto acotado** (expedición en blanco); **sin límite temporal** ni de
  ejercicios; **sin identificar** qué se busca ni por qué solo puede obtenerse entrando; la que habilita
  de hecho un rastreo indiscriminado (*fishing expedition*).
- **Necesidad real:** ¿por qué no basta un **requerimiento de información**? Si la documentación puede
  obtenerse así, la entrada **no es el medio menos restrictivo** (canon del art. 100.2 LPAC).
- **Consentimiento y sorpresa:** el precepto exige **oposición o riesgo de oposición** (§ 1). Si nunca se
  pidió el consentimiento y no se acredita **riesgo real**, falta el presupuesto. La invocación genérica
  del «factor sorpresa» **no acredita** riesgo de oposición.
- **Persona jurídica:** delimitar qué dependencias son domicilio constitucionalmente protegido; la
  autorización debe **acotarlas**.
- ⚠️ **Régimen de la LGT** (arts. 113 y 142 y su reforma por la Ley 11/2021, que afecta de lleno a la
  solicitud de entrada y su motivación): **verificar el texto vigente con `buscar_articulo("LGT","113")`
  y `buscar_articulo("LGT","142")` antes de citarlos**. No se citan aquí de memoria. La doctrina del TS
  sobre entrada tributaria es **abundante, reciente y decisiva**: localizar con `buscar_sentencias`,
  verificar con `buscar_por_cita`. **Sin verificar, no se cita.**

---

## 5. Los dos lados del despacho

### 5.1 OPONERSE a la autorización

**Antes de escribir:** vista de actuaciones y copia de la solicitud; **cronología documentada** (acto,
notificación, apercibimiento, requerimientos, recursos, **suspensiones**); comprobar si hay **cautelar**
pedida o concedida en el pleito de fondo.

**Checklist de motivos:**

1. **Falta de acto ejecutivo** que ampare la entrada, o acto **no definitivo**.
2. **Falta de notificación previa** del acto.
3. **Falta de apercibimiento previo** (**art. 99 LPAC**).
4. **Acto suspendido** — el art. 99 excluye entonces la ejecución forzosa.
5. **Ausencia de necesidad:** el fin puede alcanzarse **sin entrar**.
6. **Desproporción / medio no menos restrictivo** (100.1-100.2): existían apremio, multa coercitiva o
   ejecución subsidiaria viables.
7. **Indeterminación del objeto y del alcance temporal.**
8. **Falta de oposición o de riesgo de oposición** acreditado (supuestos c y d).
9. **Motivación insuficiente**, señaladamente en el tributario (§ 4).
10. **Falta de competencia** del órgano solicitante o del autor del acto.
11. **Terceros afectados:** si el domicilio es de un tercero (arrendatario, convivientes), su derecho del
    art. 18.2 CE es **propio** y no puede sacrificarse sin oírle.

### 5.2 IMPUGNAR lo actuado si la entrada excedió de lo autorizado

- **Documentar el exceso el mismo día:** acta, diligencias, testigos, hora de entrada y salida, relación
  de lo incautado o copiado. **La prueba se hace ese día**; después no existe.
- **Cauces posibles** según fase: recurso contra el auto (si aún cabe); **incidente ante el propio
  Juzgado** que autorizó, por extralimitación; impugnación del acto o liquidación que se apoye en lo
  obtenido, invocando la **ilicitud de la prueba** y su conexión; **amparo** ex art. 18.2 CE agotada la
  vía; y, en su caso, **responsabilidad patrimonial**.
- ⚠️ **El cauce, el órgano y el plazo de recurso frente al auto del art. 8.6 dependen del caso y NO están
  en las anclas: `[verificar]` en cada asunto** con `buscar_articulo` (arts. 79-80, régimen de recursos
  contra autos, y art. 87 para apelación) y con `buscar_sentencias`. **No dar por sabido el plazo ni el
  recurso procedente: comprobarlo el mismo día.**
- La **ilicitud probatoria** en el ámbito administrativo-tributario y su alcance (conexión de
  antijuridicidad) es **jurisprudencia viva**: verificar antes de construir el escrito sobre ella.

### 5.3 Petición subsidiaria — incluirla siempre

Aunque se pida la denegación, **pedir subsidiariamente la acotación**: es lo que más se concede y lo que
más protege en la práctica. Que el auto fije **día y franja horaria**, **dependencias concretas**,
**objeto material** de lo examinable o copiable, **presencia del titular y de su letrado** y **acta** de
lo actuado.

---

## 6. Estructura y SUPLICO

1. **Encabezamiento:** Juzgado CA (art. 8.6); autos de autorización; letrado y, en su caso, procurador
   (potestativo ante Juzgados, art. 23.1 — anclas § 4.4); **personación y petición de vista**.
2. **HECHOS** numerados, **datados** y con folio: acto, notificación, apercibimiento, recursos,
   **suspensiones**, y **qué se pide exactamente**.
3. **PROCESALES:** naturaleza del procedimiento y **su objeto limitado** (§ 3) — decirlo el despacho
   **primero** demuestra dominio del cauce y encuadra el debate donde conviene; interés legítimo del
   compareciente como titular.
4. **FONDO:** art. 18.2 CE; arts. 99 y 100 LPAC; motivos del § 5.1, **uno por ordinal**, cada uno anclado
   a documento.
5. **Jurisprudencia** — solo verificada (§ 7).
6. **SUPLICO** y **OTROSÍES:** vista de actuaciones; documentos; **urgencia**.

**Reparto para la redacción rápida:** encabezamiento, personación y hechos datados · fundamentos procesales (objeto limitado del § 3) y de fondo (art. 18.2 CE, arts. 99 y 100 LPAC y los motivos del § 5.1; una sección más si son muchos motivos) · cierre con petición subsidiaria de acotación, suplico y otrosíes. La urgencia manda: escrito corto, tres secciones como máximo.

> **SUPLICO AL JUZGADO** que, teniendo por presentado este escrito, se sirva admitirlo, tener por
> **personado y parte** a **[CLIENTE]**, **titular del domicilio** sito en **[DOMICILIO]**, tener por
> formulada **OPOSICIÓN** a la autorización de entrada solicitada por **[ÓRGANO]** y dictar auto por el que:
>
> **1.º)** **DENIEGUE la autorización de entrada**, por **[falta de acto administrativo ejecutivo / falta
> de apercibimiento previo del art. 99 LPAC / hallarse suspendida la ejecución del acto / no ser la
> entrada necesaria ni el medio menos restrictivo, ex art. 100.1 y 100.2 LPAC / indeterminación del
> objeto y del alcance temporal / insuficiente motivación de la solicitud]**;
>
> **2.º)** **subsidiariamente**, para el caso de autorizarse, **ACOTE** la autorización determinando:
> **[a) dependencias concretas; b) día y franja horaria; c) objeto material de lo examinable o copiable;
> d) presencia del titular y de su letrado durante toda la actuación; e) levantamiento de acta con
> entrega de copia]**.
>
> **PRIMER OTROSÍ DIGO** que, dada la **urgencia**, **SUPLICO** la **vista de las actuaciones** con
> carácter inmediato y previo a resolver.

## 7. Reglas de la casa

- **Protección de datos:** cero datos reales. `[CLIENTE]`, `[ÓRGANO]`, `[DOMICILIO]`, `[FECHA]`,
  `[IMPORTE]`. Aquí el escrito contiene por definición el **domicilio real**: en borradores va **siempre**
  como `[DOMICILIO]`; solo se completa en la versión final que se presenta.
- **Jurisprudencia:** **decisiva** aquí — el canon de control de la entrada, la doctrina del TS sobre
  entrada tributaria y autorizaciones prospectivas y el domicilio de las personas jurídicas son
  **construcción jurisprudencial**. **Prohibido citar ECLI/ROJ/fecha/ponente de memoria.**
  `buscar_sentencias` para localizar, `buscar_por_cita` para verificar. Lo no verificado, `[verificar]`.
- **Normativa autonómica y local:** el conector no la cubre (solo BOE estatal + ordenanzas de municipios
  cubiertos, vía `buscar_ordenanzas`). Muy relevante aquí: **órdenes de ejecución y demoliciones** son de
  normativa **urbanística autonómica y local**. **Pedírsela al usuario.**
- **Nada de MASC:** es del orden **civil**; no existe en esta jurisdicción.
- **Coordinación obligatoria:** abrir **siempre en paralelo** la impugnación del acto de fondo con
  petición de **medida cautelar** (`medidas-cautelares-ca`) — § 3.
- **Entregable:** Word `.docx` maquetado, que genera el ensamblado de `redaccion-rapida`.
