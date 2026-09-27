---
name: requerimiento-judicial-triage
description: >-
  Triage de notificaciones y requerimientos en materia contencioso-administrativa: notificacion de resolucion administrativa, providencia de apremio, requerimiento del art. 44 LJCA entre Administraciones, requerimiento previo a la via de hecho del art. 30 LJCA, emplazamiento como interesado del art. 49 LJCA y subsanacion del art. 45.3 LJCA. Identifica que plazo arranca, si es de caducidad y cuando vence. Usar con hemos recibido una notificacion, requerimiento o providencia de apremio.
---

# Triage de notificación o requerimiento — contencioso-administrativo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo que arranca cada documento de la tabla** → `buscar_articulo` (`ley="LJCA"`, artículos 30, 44, 45, 46, 49, 79, 85, 89 y 115; `ley="LPAC"`, artículos 121 a 124).
- **Providencia de apremio: plazos de ingreso y motivos tasados** → `buscar_articulo` (`ley="LGT"`, artículos 62, 167, 223 y 235).
- **Motivo c) del art. 167.3 LGT (falta de notificación de la liquidación)** → `buscar_doctrina_teac` + `leer_resolucion_teac`.
- **Notificación edictal en el BOE** → `novedades_boe` (órgano y referencia del expediente, o NIF si el destinatario es una sociedad; periodo de hasta 31 días) + `leer_boe`.
- **Recibo de un tributo local** (IBI, plusvalía) → `buscar_ordenanzas` + `leer_ordenanza` (ordenanza fiscal) y `consultar_catastro` (referencia catastral del recibo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

> 🎯 **La pregunta central de esta skill no es "qué nos piden", sino: ¿QUÉ PLAZO ARRANCA, ES DE CADUCIDAD, Y CUÁNDO VENCE?**
>
> En contencioso-administrativo, el documento más peligroso que entra por la puerta **no es una demanda**: es una **notificación administrativa** que nadie identifica como urgente y que arranca en silencio un plazo de **caducidad de 2 meses** (art. 46.1 LJCA). Cuando vence, el acto deviene **firme y consentido** y el recurso se inadmite sin entrar en el fondo (art. 69.e LJCA). No hay reapertura posible.

> ⛔ **Aquí no hay demanda civil, ni monitorio, ni ejecución de la LEC, ni diligencias preliminares del art. 256 LEC, ni MASC.** Si el documento pertenece a otro orden jurisdiccional, decirlo y no forzar el encaje.

## Cuándo activar

- "Hemos recibido una notificación de [Administración]"
- "Nos ha llegado una providencia de apremio"
- "Requerimiento de subsanación del juzgado"
- "Nos emplazan como interesados en un recurso"
- "El Ayuntamiento requiere a la Comunidad / otra Administración"
- "Han entrado a ejecutar sin acto previo" (posible vía de hecho)
- Cualquier documento con sello de registro cuyo plazo no esté identificado

## Flujo

### 1. Clasificar el documento y localizar el plazo

| Documento recibido | Plazo que arranca | Naturaleza | Norma | Acción |
|---|---|---|---|---|
| **Notificación de resolución administrativa que PONE FIN a la vía** | **2 meses** para interponer recurso contencioso, desde el día siguiente a la notificación | **CADUCIDAD** | art. 46.1 LJCA | `/interposicion-recurso-contencioso-ca` |
| **Notificación de resolución que NO agota la vía** | **1 mes** para alzada | Caducidad del recurso administrativo | arts. 121-122 Ley 39/2015 | `/recurso-alzada-reposicion-ca` |
| **Notificación de acto que agota la vía, con reposición potestativa** | **1 mes** reposición potestativa **o** 2 meses contencioso directo | Caducidad | arts. 123-124 Ley 39/2015; art. 46.1 LJCA | Decidir vía; ver regla 3 |
| **Acto presunto (silencio)** | **6 meses** para el contencioso. El recurso administrativo puede interponerse **«en cualquier momento»** | Caducidad | art. 46.1 LJCA; arts. 122.1 y 124.1 Ley 39/2015 | `/interposicion-recurso-contencioso-ca` |
| **Tras resolución de reposición potestativa (expresa o presunta)** | **2 meses** desde la notificación o desde la desestimación presunta | **CADUCIDAD** | art. 46.4 LJCA | `/interposicion-recurso-contencioso-ca` |
| **Notificación de disposición general** | **2 meses** desde el día siguiente a la publicación | Caducidad | art. 46.1 LJCA | Valorar recurso directo o indirecto |
| **Providencia de apremio (tributaria)** | Plazos de **ingreso** del art. 62.5 LGT (según día de notificación: hasta el 20 del mes o hasta el 5 del mes siguiente). Impugnación: **1 mes** (reposición, art. 223.1 LGT; o REA, art. 235.1 LGT) | Caducidad de la impugnación | arts. 62.5, 167.3, 223.1, 235.1 LGT | Ver § 1.1 |
| **Requerimiento del art. 44 LJCA entre Administraciones** | El requerimiento debe formularse en **2 meses**; se entiende **rechazado si no se contesta en el mes siguiente** a su recepción; después, **2 meses** para el recurso | Caducidad | art. 44.2 y 44.3 LJCA; art. 46.6 LJCA | Ver § 1.2 |
| **Vía de hecho — requerimiento previo del art. 30 LJCA** | Intimación de cesación; si no se atiende en **10 días**, cabe recurso directo. Interposición: **10 días** desde el fin del plazo del art. 30 | **CADUCIDAD — brevísimo** | art. 30 LJCA; art. 46 LJCA | Ver § 1.3 |
| **Vía de hecho SIN requerimiento previo** | **20 días** desde el día en que se inició la actuación material | **CADUCIDAD — brevísimo** | art. 46 LJCA | `/interposicion-recurso-contencioso-ca` |
| **Diligencia de emplazamiento como interesado (art. 49 LJCA)** | **9 días** para personarse como **demandado** | Preclusivo | art. 49.1 LJCA | Ver § 1.4 |
| **Requerimiento judicial de subsanación (art. 45.3 LJCA)** | **10 días**; si no se subsana, el órgano se pronuncia sobre el **archivo** | Preclusivo — mortal | art. 45.3 LJCA | Ver § 1.5 |
| **Providencia o auto judicial no susceptible de apelación o casación** | **5 días** para recurso de reposición | Preclusivo | art. 79.1 y 79.3 LJCA | Reposición si procede |
| **Notificación de sentencia (apelable)** | **15 días** para interponer apelación ante el Juzgado *a quo* | **CADUCIDAD** | art. 85.1 LJCA | `/recurso-apelacion-ca` |
| **Notificación de sentencia (casable)** | **30 días** para preparar la casación ante la Sala de instancia | **CADUCIDAD** | art. 89.1 LJCA | `/preparacion-recurso-casacion-ca` |
| **Resolución en materia de derechos fundamentales** | **10 días** para interponer | **CADUCIDAD — y agosto SÍ corre** | art. 115.1 LJCA; art. 128.2 LJCA | `/proteccion-derechos-fundamentales-ca` |
| **Otros** | Variable | `[verificar]` | — | Calcular plazo + acción |

#### § 1.1 Providencia de apremio

Dos plazos distintos que se confunden constantemente — separarlos siempre:

- **Plazo para pagar** (art. 62.5 LGT): si la providencia se notifica entre el **1 y el 15** del mes, hasta el **día 20 de ese mes**; si se notifica entre el **16 y el último día** del mes, hasta el **día 5 del mes siguiente**. Si no fuera hábil, el inmediato hábil siguiente. Vencido sin pago → **embargo**.
- **Plazo para impugnar**: **1 mes** (reposición del art. 223.1 LGT o reclamación económico-administrativa del art. 235.1 LGT).

⚠️ **Motivos de oposición TASADOS** (art. 167.3 LGT) — solo estos cinco:
a) extinción total de la deuda o prescripción del derecho a exigir el pago;
b) solicitud de aplazamiento, fraccionamiento o compensación en período voluntario y otras causas de suspensión;
c) **falta de notificación de la liquidación**;
d) anulación de la liquidación;
e) error u omisión en la providencia que impida identificar al deudor o la deuda.

**No cabe discutir el fondo de la liquidación en la impugnación del apremio.** El motivo c) es el que más rendimiento da: verificar SIEMPRE cómo se notificó la liquidación de origen.

#### § 1.2 Requerimiento del art. 44 LJCA (litigios entre Administraciones)

- En los litigios entre Administraciones **no cabe recurso en vía administrativa**. El requerimiento previo es **potestativo**.
- Se dirige al órgano competente por escrito razonado, en el plazo de **2 meses** desde la publicación de la norma o desde que la requirente conoció o pudo conocer el acto, actuación o inactividad (art. 44.2).
- Se entiende **rechazado** si no se contesta **dentro del mes siguiente** a su recepción (art. 44.3).
- ⚠️ **Excepción de contratación pública** (art. 44.1, párrafo 2.º): las decisiones de los órganos que resuelven los **recursos especiales y reclamaciones en materia de contratación** se recurren **directamente, sin requerimiento ni recurso administrativo previo** — lo interpongan la Administración contratante, el contratista o terceros.
- Queda a salvo lo dispuesto en la legislación de régimen local (art. 44.4).

#### § 1.3 Requerimiento previo a la vía de hecho (art. 30 LJCA)

- El interesado **puede** (no debe) requerir a la Administración actuante intimando la **cesación** de la actuación material.
- Si la intimación **no se formuló** o **no fue atendida dentro de los 10 días siguientes** a la presentación del requerimiento, cabe **recurso contencioso directo**.
- **Plazos de interposición — los más cortos del orden, y se confunden:**
  - **Con** requerimiento previo: **10 días** desde el día siguiente al fin del plazo del art. 30.
  - **Sin** requerimiento previo: **20 días** desde el día en que se inició la actuación material.
- Valorar **medidas cautelares** de inmediato (`/medidas-cautelares-ca`): en vía de hecho el daño suele estar consumándose.

#### § 1.4 Emplazamiento como interesado (art. 49 LJCA)

- Nuestro cliente **no es el recurrente**: aparece como interesado en el expediente y se le emplaza para personarse **como demandado** en **9 días**.
- La resolución que acuerda remitir el expediente se notifica a los interesados en los **5 días siguientes** a su adopción (art. 49.1).
- **Decisión estratégica, no automática:** personarse tiene coste y expone; no personarse deja que el recurso siga sin nuestra defensa y la sentencia puede afectarle igualmente. Analizar el interés real del cliente en que el acto **se mantenga**.
- Si el emplazamiento se hizo **por edictos** (art. 49.4, Tablón Edictal Judicial Único), los emplazados pueden personarse **hasta el momento en que hubiere de dárseles traslado para contestar a la demanda**.
- Si el emplazamiento fue **defectuoso o no se practicó** pese a ser el cliente identificable, hay munición: el LAJ debe ordenar que se practiquen los necesarios para asegurar la defensa de los interesados identificables (art. 49.3).

#### § 1.5 Requerimiento de subsanación (art. 45.3 LJCA)

- Plazo: **10 días**. Si no se subsana, el órgano **se pronuncia sobre el archivo**.
- Causa más frecuente y evitable: **art. 45.2.d)** — personas jurídicas que no acreditan el **cumplimiento de los requisitos para entablar acciones** conforme a sus estatutos (el «acuerdo corporativo»). **El poder no basta.**
- Otras: representación (a), legitimación derivada de transmisión (b), copia del acto impugnado o indicación del expediente (c), y **sindicatos** ex art. 19.1.k) — afiliación, comunicación al afiliado y **autorización expresa** (art. 45.2.e), añadido por la LO 1/2025).
- **Tratar como máxima urgencia.** Es un plazo corto que mata el recurso entero por un defecto formal subsanable.

### 2. Extraer datos

- **Órgano emisor** — distinguir si es **administrativo** (Ayuntamiento, Consejería, AEAT, TEAR/TEAL, jurado de expropiación) o **judicial** (Juzgado de lo CA nº [X] de [LUGAR], Sala de lo CA del TSJ de [CCAA], Audiencia Nacional, TS Sala Tercera)
- **Expediente administrativo** nº / **procedimiento judicial** nº
- **Partes / interesados** — ¿es nuestro cliente el destinatario? ¿un interesado? ¿un tercero?
- **¿Agota la vía administrativa?** — buscarlo en el **pie de recurso** de la resolución
- ⚠️ **FECHA DE NOTIFICACIÓN** — el dato más importante del documento. **No la fecha de la resolución, no la fecha de la firma: la fecha del ACUSE DE RECIBO.** Exigir el justificante. Si la notificación fue electrónica, la fecha de **puesta a disposición** y la de **acceso** (o el transcurso del plazo de rechazo automático). Si el cliente dice "me llegó hace unas semanas", **parar y documentarlo**: sin fecha cierta no hay cómputo fiable.
- **Pie de recurso** — qué recurso anuncia, ante quién y en qué plazo. **Advertencia: un pie de recurso erróneo no vincula, pero puede fundar la no preclusión** `[verificar el efecto concreto en el caso]`.
- **Documentos adjuntos** y si el expediente está completo

### 3. Calcular el plazo — y hacerlo dos veces

1. Determinar el **dies a quo**: día siguiente a la notificación (o a la publicación, o al vencimiento del plazo del art. 29, o al inicio de la actuación material en vía de hecho).
2. Aplicar el plazo de la tabla, contrastado con `references/anclas-normativas-ca.md` § 2.
3. ⚠️ **Agosto — art. 128.2 LJCA, regla propia de esta jurisdicción, distinta de la civil:** durante agosto **no corre** el plazo para interponer el recurso contencioso **ni ningún otro plazo de la LJCA**, **SALVO en el procedimiento de protección de derechos fundamentales, en el que agosto tiene carácter de HÁBIL**. Es la trampa clásica: el plazo de 10 días del art. 115.1 **sí corre en agosto**.
   > Ojo: los plazos de la **vía administrativa** (alzada, reposición) y los **tributarios** se rigen por sus propias normas, **no** por el art. 128.2 LJCA. No aplicar la regla de agosto de la LJCA a un plazo de la Ley 39/2015 o de la LGT `[verificar el cómputo concreto]`.
4. **Doble control:** recalcular el vencimiento en una segunda lectura antes de cerrar la ficha, conforme a la regla de la casa del perfil.
5. Aplicar el **margen de seguridad interno** del despacho (DEFAULT: presentar con 7 días naturales de antelación).

### 4. Cross-check cartera

Buscar en `_log.yaml`:
- ¿Hay asunto abierto coincidente (mismo expediente, mismo acto, misma Administración)?
- ¿Es un acto **confirmatorio** de otro ya firme y consentido? → art. 69.c LJCA: inadmisible. **No abrir falsas esperanzas al cliente.**
- ¿Es acto de trámite? → solo recurrible si es **cualificado** (decide el fondo directa o indirectamente, impide continuar el procedimiento, produce indefensión o perjuicio irreparable — art. 25.1 LJCA).

### 5. Análisis de respuesta

**Si el destinatario es nuestro cliente:**
- ¿Qué vía procede: recurso administrativo (alzada / reposición / REA) o contencioso directo?
- ¿La vía está agotada? (art. 25.1 LJCA)
- ¿Concurre alguna causa de **inadmisibilidad** del art. 69 LJCA que debamos anticipar? (jurisdicción, legitimación, acto no impugnable, cosa juzgada, extemporaneidad)
- ¿Procede pedir la **suspensión** del acto en vía administrativa o **medidas cautelares** en vía judicial? (arts. 129-136 LJCA — el criterio es que la ejecución pueda hacer **perder su finalidad legítima al recurso**, art. 130.1)
- ¿Procede **cautelarísima** inaudita parte por especial urgencia? (art. 135 LJCA)

**Si somos interesados emplazados (art. 49 LJCA):** ver § 1.4.

**Si el requerimiento pide documentación:**
- **Secreto profesional como límite** (art. 542.3 LOPJ): si se pide documentación cubierta, oposición motivada **antes** de entregar. Pasar por `/revision-secreto-profesional`.
- **Datos de terceros**: no aportar datos de terceros ajenos al cliente sin base jurídica.

### 6. Output

`inbound/<slug>/triage.md`:

```markdown
# Triage — [slug]

**Tipo de documento:** [...]
**Órgano:** [administrativo / judicial — cuál]
**Expediente / procedimiento:** [...]
**¿Agota la vía administrativa?:** [sí / no / potestativa reposición / presunto]

## ⏱️ PLAZO — lo primero
**Fecha de notificación (acuse):** [...]
**Dies a quo:** [...]
**Plazo:** [...] — **Naturaleza: [CADUCIDAD / preclusivo / plazo de pago]**
**Agosto:** [no corre — art. 128.2 LJCA / SÍ corre (DDFF) / régimen propio: verificar]
**VENCE:** [...]
**Fecha objetivo de presentación (margen de seguridad):** [...]
**Doble control realizado:** [sí — segunda lectura el [fecha]]

## Petición o contenido concreto
[...]

## Análisis
- ¿Destinatario es nuestro cliente? [sí / no — interesado / tercero]
- ¿Asunto abierto en cartera? [sí: slug / no]
- ¿Acto impugnable? [sí / trámite cualificado / confirmatorio de acto firme → art. 69.c]
- ¿Vía procedente? [alzada / reposición / REA / contencioso directo]
- ¿Causas de inadmisibilidad a anticipar (art. 69 LJCA)? [...]
- ¿Procede suspensión o medida cautelar? [sí: motivo / no]
- ¿Documentación cubierta por secreto profesional? [sí → revisión / no]

## Plan de actuación
[Pasos concretos con responsable y fecha]
```

### 7. Decision tree

> **¿Qué hago ahora?**
> 1. **Confirmar la fecha de notificación** con el acuse — antes que nada
> 2. **Abrir asunto** — `/asunto-intake` si no existe
> 3. **Anotar el vencimiento** — `/actualizar-asunto`
> 4. **Recurso administrativo previo** — `/recurso-alzada-reposicion-ca`
> 5. **Interponer el contencioso** — `/interposicion-recurso-contencioso-ca`
> 6. **Medidas cautelares** — `/medidas-cautelares-ca` si el acto se ejecuta
> 7. **Reposición judicial (5 días, art. 79 LJCA)** si es providencia o auto no apelable
> 8. **Comunicar al cliente** — borrador con el plazo y la fecha de vencimiento **en el asunto del correo**

## Reglas

1. **El plazo, primero.** Antes de cualquier análisis de fondo, fijar dies a quo, naturaleza y vencimiento. Si el análisis de fondo se alarga, el plazo ya está anotado.
2. **Plazo desde la NOTIFICACIÓN**, no desde la fecha de la resolución ni desde la firma. Exigir el acuse. Sin fecha cierta documentada, **no afirmar un vencimiento**: decir que no se puede computar y pedir el justificante.
3. **Caducidad, no prescripción.** No se interrumpe con burofax, reclamación extrajudicial, escrito de queja ni conversaciones con el funcionario. **Un burofax no conserva la acción contenciosa.** Si el cliente cree que "ya reclamó", desengañarle de inmediato.
4. **Agosto — art. 128.2 LJCA.** No corre ningún plazo de la LJCA **salvo derechos fundamentales**, donde agosto **sí es hábil**. No extender esta regla a los plazos de la Ley 39/2015 ni de la LGT.
5. **Vía de hecho: 10 o 20 días.** Son los plazos más cortos del orden y el error más caro. Si se sospecha vía de hecho, tratar como emergencia el mismo día.
6. **Un pie de recurso no es la ley.** Contrastar siempre lo que dice el pie de recurso con la norma; si divergen, marcar la discrepancia y `[verificar]` el efecto.
7. **Secreto profesional como límite** (art. 542.3 LOPJ). Oposición motivada antes de entregar documentación cubierta.
8. **Protección de datos.** El triage se archiva por **slug**, no por nombre del cliente. No volcar en la ficha datos personales innecesarios ni datos de **terceros** que figuren en el documento (otros interesados, denunciantes).
9. **No inventar plazos.** Todos los de la tabla están verificados en `references/anclas-normativas-ca.md` o con `buscar_articulo`. Cualquier plazo que no esté ahí: verificar en el momento o marcar `[verificar]`.
