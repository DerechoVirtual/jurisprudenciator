---
name: expediente-administrativo-ca
description: Gestión, auditoría y explotación estratégica del expediente administrativo — reclamación (art. 48 LJCA), ampliación de lo omitido (art. 55 LJCA), detección de huecos y vicios, foliado e índice de citas, expediente electrónico y protección de datos de terceros. Activar con "ha llegado el expediente", "el expediente está incompleto", "faltan documentos en el expediente", "reclamar el expediente", "no lo han remitido", "ampliación del expediente", "art. 55", "auditar el expediente", "citar por folio", "índice del expediente", "qué vicios tiene el procedimiento".
---

# Expediente administrativo — auditoría y explotación

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Reclamación, ampliación y concepto de expediente** → `buscar_articulo` (`ley="LJCA"`, artículos 48, 55 y 60; `ley="LPAC"`, artículo 70).
- **Norma que exige el documento ausente** → `buscar_articulo` o `buscar_boe` + `leer_boe` (norma estatal); `buscar_ordenanzas` + `leer_ordenanza` si lo exige una ordenanza.
- **Vicios candidatos** (motivación, audiencia, caducidad, notificación) → `buscar_articulo` (`ley="LPAC"`, artículos 25, 35, 40 a 44, 47 y 48).
- **Informes «internos» del art. 70.4, desviación de poder e indefensión** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Notificación del expediente practicada por edicto** → `novedades_boe` (órgano y referencia; periodo de hasta 31 días) + `leer_boe`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

**El expediente administrativo es LA prueba del contencioso.** No es documentación de contexto: es
el material probatorio del que sale la sentencia. Toda afirmación de hecho de la demanda se sostiene
en un folio del expediente, o no se sostiene.

**Concepto legal — art. 70 LPAC (verificado):** «el **conjunto ordenado de documentos y actuaciones
que sirven de antecedente y fundamento a la resolución administrativa**, así como las diligencias
encaminadas a ejecutarla» (70.1). Tiene **formato electrónico** e incluye un **índice numerado**
(70.2). **No** forma parte del expediente la información **auxiliar o de apoyo** —notas, borradores,
opiniones, resúmenes, comunicaciones e informes **internos**, juicios de valor— **salvo que se trate
de informes, preceptivos y facultativos, solicitados antes de la resolución** que puso fin al
procedimiento (70.4). ← Esta salvedad es munición: **los informes solicitados antes de resolver SÍ
son expediente, aunque la Administración los llame «internos»**.

## Cuándo activar

- Al admitirse el recurso y requerirse el expediente.
- **El día en que el expediente llega** — el índice se revisa ese día, no el día 15.
- Cuando la Administración **no remite** el expediente o lo remite **incompleto**.
- Antes de redactar demanda, contestación o conclusiones (para construir el índice de citas).
- Cuando hay que decidir si se pide la **ampliación del art. 55**.

## 1. Reclamación del expediente — art. 48 LJCA (verificado, redacción RD-ley 6/2023)

- **48.1** — El **LAJ** requiere a la Administración la remisión del expediente al admitir el
  recurso, ordenándole practicar los emplazamientos del art. 49. Se reclama **al órgano autor** del
  acto o disposición, o a aquel al que se impute la **inactividad** o la **vía de hecho**.
- **48.3** — Plazo de remisión: **20 días improrrogables**, a contar **desde que la comunicación
  judicial tenga entrada en el registro general del órgano requerido** (no desde el requerimiento).
- **48.4** — Se envía **completo, en soporte electrónico, foliado, autentificado y acompañado de un
  índice, asimismo autentificado**. La Administración **debe identificar al órgano responsable del
  cumplimiento de la resolución judicial**. Si lo reclaman varios órganos, envía copias electrónicas.
- **48.6** — Solo se excluyen, **mediante resolución motivada**, los documentos clasificados como
  **secreto oficial**, y debe **hacerse constar en el índice y en el lugar del expediente** donde
  estaban. → Una exclusión sin resolución motivada o sin constancia en el índice **es impugnable**.
- **48.7 — MULTA COERCITIVA.** Transcurrido el plazo sin recibirse **completo**, se **reitera** la
  reclamación; si no se envía en **10 días**, tras constatarse la responsabilidad y previo
  apercibimiento del LAJ notificado personalmente para alegaciones, el órgano judicial impone una
  **multa coercitiva de 300 a 1.200 €** a la **autoridad o empleado responsable**, **reiterada cada
  20 días** hasta el cumplimiento. Si no se puede individualizar al responsable, paga la
  **Administración**, sin perjuicio de repercutir.
- **48.8** — Contra los autos de imposición de multa: **recurso de reposición** (art. 79).
- **48.9** — Multas firmes no satisfechas → **vía judicial de apremio**.
- **48.10** — **Impuestas las tres primeras multas** sin lograr el expediente completo, el órgano
  pone los hechos en conocimiento del **Ministerio Fiscal**, y sigue multando. El requerimiento que
  pueda dar lugar a la **tercera** multa contiene el oportuno apercibimiento.
- **48.11** — Remisión electrónica por los **sistemas de interoperabilidad**, para integración
  automática en la gestión procesal.

> **Uso estratégico:** la multa del 48.7 es del órgano judicial, pero se **pide y se impulsa**. Si
> el expediente no llega, presentar escrito recordando el 48.3, interesando la reiteración y, en su
> caso, la multa del 48.7 con identificación del responsable ex 48.4. La escalada del 48.10 (Fiscal)
> existe y se cita.
>
> **En procedimiento ABREVIADO (art. 78.3, verificado, redacción LO 1/2025, en vigor 3-4-2025):** el
> LAJ requiere a la Administración demandada que remita el expediente **en soporte electrónico**,
> **con al menos 15 días de antelación** al término señalado para la vista. Recibido, el LAJ **lo
> entrega al actor** y a los interesados personados para alegar en la vista (art. 78.4). Aquí no hay
> plazo de demanda que suspender: el margen es el que va del expediente a la vista. **Si llega tarde
> o incompleto, denunciarlo de inmediato y pedir suspensión de la vista** — no esperar al acto.

## 2. Expediente incompleto — ampliación del art. 55 LJCA (verificado, redacción RD-ley 6/2023)

**Es el punto crítico de toda la fase intermedia. La regla, dicha bien:**

- **55.1** — Si las partes estiman que el expediente **no está completo**, pueden solicitar **dentro
  del plazo para formular la demanda o la contestación** que se reclamen los antecedentes para
  completarlo. A estos efectos, el expediente es el del **art. 70 LPAC**. ⚠️ **Los documentos que
  formen parte de un expediente administrativo DISTINTO NO pueden pedirse por esta vía** — eso es
  **prueba**, y su cauce es el **otrosí de recibimiento a prueba** del **art. 60.1 LJCA**
  (verificado: «solamente se podrá pedir el recibimiento del proceso a prueba por medio de otrosí, en
  los escritos de demanda y contestación»), no la ampliación. Confundir los dos cauces es perder los
  dos. **En sanciones el art. 60.3 juega a favor** (verificado): «si el objeto del recurso fuera una
  **sanción** administrativa o disciplinaria, el proceso **se recibirá siempre a prueba** cuando
  exista disconformidad en los hechos».
- **55.2** — La solicitud **SUSPENDE el curso del plazo** correspondiente. **Confirmado: sí,
  suspende.** Basta presentarla en plazo.
- **55.3** — El **LAJ resuelve en 3 días**. Y entonces:

| Situación | Efecto sobre el plazo de demanda / contestación |
|---|---|
| **Se acepta** y se pidió **dentro de los 10 primeros días** del plazo | El plazo se **REINICIA** una vez el expediente completo se pone a disposición de la parte solicitante |
| **Se rechaza** | El cómputo simplemente se **REANUDA** |
| Se acepta pero se pidió **pasados los 10 primeros días** | Se **REANUDA**, *salvo* que el LAJ considere oportuno reiniciarlo atendido el **volumen o la importancia para la causa** de los documentos añadidos |
| La pide la **Administración demandada** | **NUNCA se reinicia** (55.3 in fine) |

> **Regla operativa que se deriva de esto y que hay que decirle al usuario:** revisar el índice
> **el día que llega el expediente**. Pedir la ampliación **dentro de los 10 primeros días** no es
> una preferencia de estilo: es la diferencia entre **reiniciar** 20 días y **reanudar** los pocos
> que queden. Un expediente de 400 folios revisado el día 12 ya perdió el reinicio.
>
> La Administración, al remitir de nuevo el expediente, **debe indicar en el índice del art. 48.4
> los documentos añadidos** (55.3). Comprobarlo.

## 3. Auditoría del expediente — un expediente mutilado esconde el vicio

**Que el expediente esté completo es interés de la parte RECURRENTE, no de la Administración.** Lo
que falta es, casi siempre, lo que no convenía que estuviera. La ausencia de un documento preceptivo
no es un descuido: es un **motivo de impugnación**. Auditar hito por hito:

| Hito | ¿Está? | Si falta, qué significa |
|---|---|---|
| **Acuerdo de incoación** | | Sin él no hay procedimiento — art. 47.1.e LPAC. Fija además el **dies a quo de la caducidad** del procedimiento (art. 21.3.a) |
| **Nombramiento de instructor y secretario** | | Impide el control de **abstención y recusación** — **arts. 23 y 24 de la Ley 40/2015 (LRJSP)**, ⚠️ **no** de la LPAC (verificado): los motivos de abstención están en el **art. 23.2 LRJSP** |
| **Pliego de cargos / propuesta de resolución** | | En sancionador es **preceptiva y motivada** (art. 35.1.h LPAC) |
| **Trámite de audiencia Y su acuse de recibo** | | Sin audiencia acreditada → **indefensión** (art. 48.2 LPAC; y art. 47.1.e si se prescindió del todo) |
| **Informes preceptivos** (técnico, jurídico, órgano consultivo) | | Ausencia de informe **preceptivo** = vicio de procedimiento. Y ojo al **art. 70.4**: los solicitados antes de resolver **son expediente** |
| **Alegaciones del interesado y su valoración** | | Si constan las alegaciones pero la resolución no las contesta → falta de motivación |
| **Prueba practicada y acuerdos de admisión/denegación** | | El rechazo de prueba **debe motivarse** (art. 35.1.f LPAC) |
| **La resolución, con su motivación** | | Art. 35 LPAC — ver § 4 |
| **Notificación con acuse y FECHA** | | Es el dato del que depende **toda la admisibilidad**. Sin acuse fechado, la caducidad no está acreditada → `/computo-plazos-ca` |
| **Índice numerado, foliado y autentificado** | | Arts. 48.4 LJCA y 70.2-70.3 LPAC. Sin índice autentificado no hay garantía de **integridad e inmutabilidad** (art. 70.3) → denunciarlo |
| **Resolución motivada de exclusión** (si falta algo) | | Art. 48.6 LJCA — solo secreto oficial, motivado y con constancia en el índice |

**Cómo se documenta un hueco:** «El expediente carece de [documento]. Debería obrar por exigirlo el
art. [x]. Su ausencia impide [qué] y determina [qué vicio].» Un hueco sin norma que lo exija no es
un hueco: es una expectativa. Verificar la norma **antes** de denunciarlo.

## 4. Lectura estratégica — los vicios que se buscan (todos verificados)

| Vicio | Norma | Qué buscar en el expediente |
|---|---|---|
| **Falta de motivación** | **art. 35 LPAC** | Actos que limiten derechos (35.1.a); resoluciones de **recursos** (35.1.b); separación del criterio anterior o del dictamen de órganos consultivos (35.1.c); rechazo de pruebas (35.1.f); **propuestas y resoluciones sancionadoras y de responsabilidad patrimonial** (35.1.h); actos **discrecionales** (35.1.i) |
| **Prescindir total y absolutamente del procedimiento** | **art. 47.1.e LPAC** ✅ (letra verificada) | Ausencia de fases esenciales; también las reglas esenciales de formación de la voluntad de órganos colegiados |
| **Órgano manifiestamente incompetente** por materia o territorio | **art. 47.1.b LPAC** ✅ (letra verificada) | Quién firma vs. norma atributiva de competencia; delegaciones no publicadas |
| **Lesión de derechos susceptibles de amparo** | art. 47.1.a LPAC | → puerta al procedimiento de DDFF (agosto **hábil**) |
| **Omisión del trámite de audiencia** | art. 48.2 LPAC (defecto de forma → anulabilidad si causa **indefensión** o falta un requisito formal indispensable) | Ausencia del trámite o de su acuse |
| **Informes preceptivos ausentes** | art. 48.2 LPAC + norma sectorial | Contraste entre lo exigido y lo obrante |
| **Desviación de poder** | **art. 48.1 LPAC** ✅ (verificado: «Son anulables los actos… que incurran en cualquier infracción del ordenamiento jurídico, **incluso la desviación de poder**») | Fin real ≠ fin institucional. Se prueba **con el expediente**: correspondencia, cambios de criterio, cronología |
| **Caducidad del procedimiento** | **art. 25.1.b LPAC** ✅ (verificado) | En procedimientos **de oficio** sancionadores o de intervención, el vencimiento del plazo produce **caducidad** y archivo. Fecha de incoación vs. fecha de notificación de la resolución. **Motivo de primer orden — comprobarlo siempre** |
| **Notificación defectuosa** | arts. 40-44 LPAC (`[verificar]` la letra concreta antes de citar) | Sin notificación válida no corre el plazo |

> **Recurso indirecto:** si el vicio está en la **disposición general** que aplica el acto, art. 112.3
> LPAC. Ver `/admisibilidad-ca`.
>
> **Jurisprudencia:** la desviación de poder, el alcance de la indefensión y la caducidad tienen
> perfil **jurisprudencial**. **Verificar con `buscar_sentencias` / `buscar_por_cita`. Nunca citar
> ECLI, ROJ ni fecha de memoria.**

## 5. Foliado e índice de citas — la disciplina que gana el asunto

**Toda afirmación de hecho en demanda y en conclusiones se cita por FOLIO.** Sin excepción. Un hecho
sin folio es una alegación; con folio es prueba documental ya en autos.

Construir en `matters/<slug>/indice-expediente.md` una tabla **folio → hecho → fundamento**:

| Folio | Documento | Hecho que acredita | Fundamento que sostiene |
|---|---|---|---|
| f. 12 | Acuerdo de incoación, [FECHA] | Inicio del procedimiento el [FECHA] | FD 2.º — caducidad (art. 25.1.b LPAC) |
| f. 87-89 | Informe técnico de [ÓRGANO] | Reconoce [circunstancia] | FD 3.º — contradicción con la resolución |
| f. 140 | Acuse de notificación | Notificación el [FECHA] | Admisibilidad — dies a quo (art. 46.1 LJCA) |
| f. 155 | (**HUECO**) Trámite de audiencia | — | FD 4.º — indefensión (art. 48.2 LPAC) → **art. 55 LJCA** |

- **Formato de cita en el escrito:** «(f. 87 del expediente administrativo)» o «(ff. 87-89)».
- **En expediente electrónico**, el foliado es el del índice autentificado del art. 48.4 / 70.3. Si
  la paginación del PDF **no coincide** con el foliado del índice, **decirlo en el escrito** y citar
  el del índice — no el del visor.
- El índice de citas se construye **antes** de redactar, no después. Es lo que evita que la demanda
  afirme hechos que el expediente no sostiene.

## 6. ⚠️ Protección de datos — apartado obligatorio, no opcional

El expediente contiene **habitualmente datos de terceros**: denunciantes, otros interesados,
testigos, empleados públicos. En **sanitario**, contiene **datos de salud** = **categoría especial
del art. 9 RGPD**. Reglas de obligado cumplimiento:

1. **No reproducir datos de terceros** en escritos, resúmenes, cronologías ni informes. Al citar,
   usar marcadores: **`[TERCERO]`, `[PACIENTE]`, `[DENUNCIANTE]`, `[TESTIGO]`, `[DATO]`**. Se cita el
   **folio**, no el nombre. El folio identifica el documento sin difundir el dato.
2. **No subir el expediente íntegro a servicios externos** (IA, OCR, traducción, almacenamiento) sin
   **base jurídica** y sin que el tratamiento esté cubierto por el encargo y por el contrato de
   encargado de tratamiento. Con **datos de salud** o de **infracciones**, el listón sube: art. 9
   RGPD. Ante duda, **no subirlo y decirlo**.
3. **El acceso del interesado tiene límites.** El derecho de acceso a información pública del
   **art. 13.d LPAC** (verificado) remite a la **Ley 19/2013**, cuyo **art. 15** (verificado)
   somete a régimen reforzado los datos de **salud, origen racial, vida sexual, genéticos,
   biométricos e infracciones penales o administrativas** —acceso solo con **consentimiento expreso
   del afectado o amparo en norma con rango de ley**— y exige **ponderación motivada** en los demás
   casos; el **art. 15.4** salva el acceso **previa disociación**. Distinto es el derecho del
   **interesado en el procedimiento** a acceder y obtener copia de los documentos (**art. 53.1.a
   LPAC**, verificado): más amplio, pero no ilimitado frente a datos de terceros.
   **Consecuencia práctica:** que un dato esté en el expediente **no autoriza** a difundirlo.
4. **Secreto profesional — art. 542.3 LOPJ** (verificado): «Los abogados **deberán guardar secreto de
   todos los hechos o noticias de que conozcan por razón de cualquiera de las modalidades de su
   actuación profesional**, no pudiendo ser obligados a declarar sobre los mismos.» **Cubre también
   lo conocido a través del expediente**, incluidos los datos de terceros que el letrado solo conoce
   porque le entregaron el expediente. Ver `/revision-secreto-profesional`.
5. **En el repositorio del asunto:** ni el slug ni los nombres de archivo llevan datos personales.
   Ver `PROTECCION-DATOS.md` del plugin.

## 7. Salida — informe de auditoría

```
## Auditoría del expediente administrativo — [slug]

**Recepción:** [fecha] · **Folios:** [n] · **Índice autentificado:** sí/no ·
**Soporte:** electrónico/papel · **Plazo abierto:** demanda 20 días (art. 52.1) → vence [fecha]
**Día del plazo en que estamos:** [n] → [✅ dentro de los 10 primeros — cabe REINICIO /
⚠️ pasados los 10 — solo REANUDACIÓN]

### Hitos localizados
| Folio | Hito | Fecha |

### 🔴 HUECOS DETECTADOS
| Documento ausente | Norma que lo exige | Relevancia jurídica | ¿Art. 55? |

### Vicios candidatos
| Vicio | Norma | Folios de apoyo | Solidez [alta/media/exploratoria] |

### Defectos formales del envío
[Índice no autentificado (48.4) / exclusiones sin resolución motivada (48.6) / paginación ≠ foliado /
remisión incompleta → reiteración y multa (48.7)]

### Recomendación
[⑴ Pedir ampliación del art. 55 — SÍ/NO, y por qué. Si SÍ: qué documentos, con qué norma cada uno,
y ANTES DE [fecha = día 10 del plazo]. ⑵ Denunciar defectos del art. 48. ⑶ Nada, expediente completo.]
```

**Si procede la ampliación**, redactar el escrito del art. 55: identificar **uno a uno** los
documentos omitidos y **la norma que los exige**; razonar por qué integran **este** expediente ex
art. 70 LPAC (y no otro distinto); invocar el **art. 55.2** (suspensión del plazo) y, si estamos
dentro de los 10 primeros días, el **reinicio** del art. 55.3. Entregable `.docx` (skill `docx`).
Después, **`/actualizar-asunto`**: `expediente_administrativo` → `recibido` /
`incompleto-ampliación-pedida`, y el nuevo `next_deadline`.

## Reglas

1. **El índice se revisa el día que llega el expediente.** La ventana de los **10 primeros días** del
   art. 55.3 es la diferencia entre reiniciar y reanudar. Decírselo al usuario en la primera línea.
2. **Prohibido inventar** artículos, letras, plazos o cifras. Lo que no esté en
   `references/anclas-normativas-ca.md` se verifica con `buscar_articulo` en el momento. Si no se
   puede → `[verificar]` y decirlo.
3. **Un hueco se denuncia con la norma que exige el documento**, nunca solo con la intuición de que
   "debería estar".
4. **No afirmar en la demanda ningún hecho sin folio.** Si el folio no existe, el hecho necesita
   prueba propia o no se afirma.
5. **Protección de datos: `[TERCERO]` / `[PACIENTE]` siempre.** No reproducir datos de terceros ni
   subir el expediente íntegro a servicios externos sin base jurídica. En caso de duda, no.
6. **Prohibido citar jurisprudencia concreta** (ECLI/ROJ/fecha) sin `buscar_sentencias` /
   `buscar_por_cita`.
7. **Normativa autonómica y local: no se cita de memoria** — el conector no la cubre (salvo
   ordenanzas de los municipios cubiertos). Pedírsela al usuario.
8. **Nada de MASC.** No existe en esta jurisdicción.
9. Config del plugin: `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/`.
