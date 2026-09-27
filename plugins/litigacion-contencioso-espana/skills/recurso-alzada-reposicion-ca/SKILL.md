---
name: recurso-alzada-reposicion-ca
description: >-
  REDACTA los recursos administrativos de alzada (arts. 121-122 Ley 39/2015) y de reposición potestativa (arts. 123-124) en la vía administrativa previa, una vez decidido que ese es el escrito que procede. Activar con "redactar un recurso de alzada", "recurso de reposición administrativo", "recurrir en vía administrativa", "me han notificado una resolución y voy a recurrirla antes de ir al juzgado". Es el paso posterior al diagnóstico: para decidir ANTES si el acto agota o no la vía administrativa, si es impugnable y en qué plazo, correr primero el checklist de /admisibilidad-ca.
---

# Recurso de alzada y de reposición (vía administrativa previa)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Triaje del recurso y plazos** → `buscar_articulo` (`ley="LPAC"`, artículos 24, 30, 112, 114, 115, 117 y 121 a 124).
- **Acto municipal: ordenanza aplicada y órgano competente** → `buscar_ordenanzas` + `leer_ordenanza` con `articulo` (también el reglamento orgánico municipal).
- **Acto tributario (art. 112.4 LPAC): la vía es la económico-administrativa** → `buscar_doctrina_teac` + `leer_resolucion_teac` y `buscar_consultas_hacienda` + `leer_consulta_hacienda` para conocer el criterio vinculante.
- **Procedimiento de impugnación sustitutivo previsto en una ley sectorial (art. 112.2)** → `buscar_boe` + `leer_boe`.
- **Doctrina para los motivos de nulidad o anulabilidad** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Antes de presentar** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

Instrucciones PARA Claude. Fuente única de plazos y umbrales: `references/anclas-normativas-ca.md`.
Lo que no esté allí, verifícalo con `buscar_articulo` o márcalo `[verificar]`. **No inventes nunca**
plazos, letras de artículo ni cifras.

> ⛔ **ERRATA VERIFICADA — NO REINTRODUCIR.** Versiones anteriores de esta skill afirmaban que el
> plazo contra **acto presunto** era de **3 meses**. **ES FALSO.** Ese plazo pertenecía al **art.
> 115.1 de la derogada Ley 30/1992**. Desde la Ley 39/2015 (vigente 2-10-2016), contra acto
> presunto tanto la alzada (**art. 122.1, párr. 2**) como la reposición (**art. 124.1, párr. 2**)
> pueden interponerse **«en cualquier momento»** a partir del día siguiente a aquel en que se
> produzcan los efectos del silencio. Verificado contra el BOE el 2026-07-17. Si alguna vez lees
> «3 meses» en un borrador, es un error: corrígelo y di por qué.

## 1. Triaje: ¿qué recurso procede? (art. 112.1 LPAC)

Antes de redactar, resuelve estas cinco preguntas **en este orden**:

1. **¿El acto pone fin a la vía administrativa?** (art. 114 LPAC — consúltalo si dudas).
   - **NO** → **ALZADA**, ante el órgano superior jerárquico del que dictó el acto (art. 121.1).
     Es **obligatoria**: sin ella no se agota la vía y el contencioso se inadmite (art. 69.c LJCA).
   - **SÍ** → **REPOSICIÓN**, **potestativa**, ante el mismo órgano (art. 123.1), o recurso
     contencioso directo. Decide con el § 4.
2. **¿Es un acto de trámite?** Solo cabe recurso si es **cualificado**: decide directa o
   indirectamente el fondo, impide continuar el procedimiento, produce indefensión o perjuicio
   irreparable (art. 112.1). Contra el trámite **no** cualificado **no cabe recurso**: la oposición
   se alega para su consideración en la resolución que ponga fin al procedimiento (art. 112.1,
   párr. 2). Recurrir un trámite simple pierde tiempo y no conserva nada.
3. **¿Es una disposición general?** **No cabe recurso administrativo** contra ella (art. 112.3).
   Si el acto se recurre **únicamente** por la nulidad de una disposición general, el recurso puede
   interponerse **directamente ante el órgano que dictó la disposición** (art. 112.3, párr. 2).
4. **¿Es materia tributaria o de Seguridad Social con vía propia?** Las **reclamaciones
   económico-administrativas** se rigen por su legislación específica (art. 112.4): TEAR/TEAC, no
   alzada. No fuerces el encaje; identifica la vía y dilo.
5. **¿Una ley sectorial sustituye el recurso?** El art. 112.2 permite sustituir la alzada (y la
   reposición) por otros procedimientos de impugnación ante órganos colegiados. Comprueba la norma
   sectorial antes de dirigir el escrito.

## 2. Cuadro de plazos — verificado BOE 2026-07-17

| | **Alzada** (arts. 121-122) | **Reposición** (arts. 123-124) |
|---|---|---|
| Objeto | Actos que **NO** ponen fin a la vía | Actos que **SÍ** ponen fin a la vía |
| Órgano | Superior jerárquico | El mismo que dictó el acto |
| Naturaleza | **Obligatoria** (agota la vía) | **Potestativa** |
| Plazo — acto **expreso** | **1 mes** (art. 122.1) | **1 mes** (art. 124.1) |
| Plazo — acto **presunto** | **«En cualquier momento»** (art. 122.1) | **«En cualquier momento»** (art. 124.1) |
| Plazo para resolver | **3 meses**; silencio **negativo** (art. 122.2) | **1 mes**; silencio **negativo** (art. 124.2) |
| Recurso posterior | Ninguno en vía administrativa, salvo revisión extraordinaria (art. 122.3) | No cabe reposición contra reposición (art. 124.3) |

- **Transcurrido el mes sin recurrir el acto expreso, la resolución es firme a todos los efectos**
  (art. 122.1). En reposición, transcurrido el mes «únicamente podrá interponerse recurso
  contencioso-administrativo» (art. 124.1) — pero ojo: si el acto ya es firme, tampoco.
- **Cómputo (art. 30.4 LPAC):** los plazos por meses se cuentan desde el **día siguiente** a la
  notificación y **concluyen el mismo día del mes de vencimiento**; si no hay día equivalente,
  el último día del mes. Último día inhábil → primer día hábil siguiente (art. 30.5).
- ⚠️ **Agosto SÍ corre aquí.** El art. 128.2 **LJCA** suspende en agosto los plazos «previstos en
  **esta Ley**» — es decir, los de la LJCA. El mes de alzada/reposición es un plazo de la **Ley
  39/2015** y **no se beneficia de esa regla**. No apliques agosto inhábil a la vía administrativa.

## 3. Silencio: la trampa del doble silencio (art. 24 LPAC)

- El silencio es **desestimatorio** en los procedimientos de **impugnación de actos** (art. 24.1,
  párr. 3) y su desestimación solo produce el efecto de **permitir el siguiente recurso** (art. 24.2).
- **Excepción — doble silencio estimatorio:** si la **alzada** se interpuso contra la
  **desestimación por silencio** de una solicitud y el órgano no resuelve en plazo, la alzada
  **se entiende ESTIMADA** (art. 24.1, párr. 3, in fine).
- **Materias excluidas del doble silencio** (art. 24.1, párr. 2): derecho de petición (art. 29 CE),
  actos cuya estimación transfiera facultades sobre **dominio público** o **servicio público**,
  actividades que puedan **dañar el medio ambiente**, y **responsabilidad patrimonial**. En
  responsabilidad patrimonial **nunca** hay doble silencio estimatorio: no lo alegues.
- Si el cliente tiene un acto presunto estimatorio, dilo: es acto finalizador a todos los efectos
  (art. 24.2) y puede acreditarse por cualquier medio, incluido el certificado del art. 24.4.

## 4. Decisión estratégica: ¿reposición o contencioso directo?

Cuando el acto agota la vía, **razona la opción y explícasela al usuario** — no la des por hecha:

- **A favor de la reposición:** coste cero, puede corregir errores materiales evidentes, permite
  completar el expediente y fuerza a la Administración a motivar.
- **En contra — el riesgo real:** interpuesta la reposición, **no se puede acudir al contencioso
  hasta que se resuelva expresamente o se produzca la desestimación presunta** (art. 123.2).
  Se pierde tiempo y se han perdido asuntos por interponer el contencioso «mientras tanto».
- **Reanudación del plazo:** resuelta la reposición (expresa o presuntamente), el plazo del
  contencioso es de **2 meses** desde el día siguiente a la notificación de la resolución expresa
  o a la desestimación presunta (**art. 46.4 LJCA**).
- **Regla de la casa:** si el motivo es puramente jurídico y la Administración ya lo rechazó de
  forma motivada, la reposición rara vez añade valor. Dilo con franqueza.

## 5. Estructura del escrito (art. 115.1 LPAC)

1. **Encabezamiento** — órgano al que se dirige y su **código de identificación** (art. 115.1.d).
2. **Recurrente** — nombre e identificación personal (art. 115.1.a): `[CLIENTE]`. Representación.
3. **Acto recurrido y razón de la impugnación** (art. 115.1.b): identificación del acto,
   **`[EXPEDIENTE]`** y **fecha de notificación** (fija el dies a quo y justifica el plazo).
4. **HECHOS**, numerados, cada uno **anclado al expediente con folio**.
5. **FUNDAMENTOS DE DERECHO** — el recurso puede fundarse en **cualquier motivo de nulidad
   (art. 47) o de anulabilidad (art. 48)** (art. 112.1):
   - **Nulidad de pleno derecho (art. 47.1):** a) lesión de derechos susceptibles de amparo;
     b) órgano manifiestamente incompetente por materia o territorio; c) contenido imposible;
     d) infracción penal; e) **prescindir total y absolutamente del procedimiento** o de las reglas
     esenciales de formación de la voluntad de órganos colegiados; f) adquisición de facultades sin
     los requisitos esenciales; g) los previstos en norma de rango legal. **Cita la letra exacta.**
   - **Anulabilidad (art. 48.1):** cualquier infracción del ordenamiento, **incluida la desviación
     de poder**. El **defecto de forma** solo anula si el acto carece de requisitos formales
     indispensables para alcanzar su fin o **causa indefensión** (art. 48.2) — argumenta siempre la
     indefensión concreta, no la mera irregularidad.
6. **SUPLICO** — anulación del acto **y**, cuando proceda, reconocimiento de lo pedido en vía
   administrativa. Otrosí de **suspensión de la ejecución** si hay perjuicio (art. 117 LPAC —
   verifícalo antes de citarlo).
7. **Lugar, fecha, firma y medio de notificación** (art. 115.1.c).

**Red de seguridad (art. 115.2):** el error o la ausencia de calificación del recurso no impide su
tramitación si se deduce su verdadero carácter. Úsalo si hay duda razonable sobre qué recurso
procede, pero **no lo conviertas en estrategia**: califica bien.
**Límite (art. 115.3):** los vicios que hagan anulable un acto **no pueden ser alegados por quien
los causó**. Comprueba que el cliente no provocó el defecto que ahora invoca.

## 6. Errores que pierden el asunto

- **Dejar caducar el plazo creyendo que un burofax lo interrumpe.** No lo interrumpe. En vía
  administrativa el mes corre; en la contenciosa los plazos son de **caducidad** (art. 69.e LJCA).
- **Citar los 3 meses del acto presunto.** Errata de la Ley 30/1992 (ver banner).
- **Recurrir en alzada un acto que ya agotaba la vía** (o al revés): se pierde el plazo del
  contencioso. Verifica el art. 114 LPAC y el pie de recurso de la notificación — y si el pie de
  recurso es erróneo, dilo, porque protege al administrado.
- **Interponer el contencioso con la reposición pendiente** (art. 123.2).
- **Recurrir un acto de trámite no cualificado** (art. 112.1, párr. 2).
- **Impugnar el acto confirmatorio en lugar del originario** — el confirmatorio de un acto firme y
  consentido no es impugnable (art. 69.c LJCA).
- **Alegar doble silencio en responsabilidad patrimonial** (excluida, art. 24.1).
- **Suplicar solo la anulación** cuando además cabe pedir el reconocimiento de la situación
  jurídica: lo pedido aquí condiciona lo que podrá pedirse después (art. 31.2 LJCA).

## 7. Cierre

- **Jurisprudencia:** verifica **antes de citar** con `buscar_sentencias` / `buscar_por_cita`.
  Prohibido inventar ECLI, ROJ, fechas, ponentes o fundamentos.
- **Normativa autonómica y local:** el conector no la cubre (solo BOE estatal y ordenanzas de los
  municipios cubiertos). **Pídesela al usuario; no la cites de memoria.**
- **Protección de datos:** cero datos reales. Usa `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`,
  `[EXPEDIENTE]`. El expediente contiene datos de terceros y, en sanitario, datos de salud
  (art. 9 RGPD, categoría especial): **nunca los reproduzcas**.
- **Nada de MASC:** es del orden civil. Aquí el equivalente es el agotamiento de la vía.
- **Entregable:** Word `.docx` maquetado (skill `docx`). Aplica `estilo-escritos-judiciales`.
- **Cierra siempre con el aviso de plazo:** «Resuelto o desestimado presuntamente este recurso,
  dispone de **2 meses** para el contencioso (art. 46.4 LJCA). Plazo de **caducidad**.»
