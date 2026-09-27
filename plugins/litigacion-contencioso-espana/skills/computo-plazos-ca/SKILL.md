---
name: computo-plazos-ca
description: Calcula y audita los plazos del orden contencioso-administrativo — caducidad de la interposición (art. 46 LJCA), silencio administrativo, mes de agosto (art. 128.2 LJCA) y plazos internos del proceso. Activar con "cuándo vence el plazo", "cuánto tiempo tengo para recurrir", "calcula el plazo", "¿he perdido el plazo?", "estoy en plazo", "fecha de caducidad", "dies a quo", "hasta cuándo puedo interponer", "me notificaron el día X", "silencio administrativo", "cuándo se produce el acto presunto", "agosto cuenta", "plazo para la demanda", "plazo para apelar o preparar casación".
---

# Cómputo de plazos contencioso-administrativos

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Texto vigente de cada plazo de la tabla** → `buscar_articulo` (`ley="LJCA"`, artículos 46, 52, 55, 85, 89, 115 y 128; `ley="LPAC"`, artículos 30, 122 y 124).
- **Sentido del silencio y caducidad del procedimiento** → `buscar_articulo` (`ley="LPAC"`, artículos 21, 24 y 25) y la norma sectorial estatal con `buscar_boe` + `leer_boe`.
- **Dies a quo de una disposición general** → `buscar_boe` + `leer_boe` (fecha de publicación) o `sumario_boe` del día de la publicación.
- **Notificación por edicto en el BOE (art. 44 LPAC)** → `novedades_boe` (órgano y referencia del expediente, o NIF si el interesado es una sociedad; periodo de hasta 31 días) + `leer_boe` para fijar la fecha del anuncio.
- **Festivos nacionales y autonómicos del año (art. 30.6 LPAC)** → `buscar_boe` + `leer_boe` (resolución anual de fiestas laborales). Los festivos locales se piden al usuario.
- **Discusión sobre el cómputo de agosto o la resolución expresa tardía** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Lo primero, y no es negociable: son plazos de CADUCIDAD

Los plazos de interposición del recurso contencioso-administrativo son de **caducidad**, no de
prescripción. Consecuencias que hay que decirle al usuario **antes** de cualquier cálculo:

- **No se interrumpen.** Ni por burofax, ni por reclamación extrajudicial, ni por negociación con
  la Administración, ni por escritos, llamadas o reuniones. Nada de lo que se haga fuera del
  proceso conserva la acción.
- Quien viene del civil arrastra el reflejo contrario (art. 1973 CC). **Es el error conceptual más
  caro de esta jurisdicción.** Si el usuario menciona un burofax o una reclamación previa como si
  hubiera "parado el reloj", corregirlo expresamente.
- Vencido el plazo, el acto deviene **firme y consentido** y el recurso se inadmite
  (**art. 69.e LJCA**). No hay reparación posible.
- Excepción conceptual — **no confundir**: la responsabilidad patrimonial sí tiene un plazo de
  **prescripción** de 1 año en **vía administrativa** (art. 67 LPAC); ese sí se interrumpe. Pero
  una vez dictada (o presunta) la resolución, el plazo para ir al contencioso vuelve a ser de
  caducidad.

## Cuándo activar

- "¿Cuánto tiempo tengo para recurrir esto?" / "¿Estoy todavía en plazo?"
- Tras cualquier notificación administrativa o judicial (entra por `/actualizar-asunto`).
- Antes de redactar cualquier escrito inicial — **el plazo se comprueba antes que el fondo**.
- Cuando se produce o se va a producir un silencio administrativo.
- Cuando el cálculo cruza el mes de **agosto**.
- Al recibir el expediente administrativo (dispara el plazo de demanda).

## Flujo

### 1. Recabar los datos mínimos

Vía `AskUserQuestion` o input directo. **Sin estos datos no hay cálculo**, solo estimaciones que
hay que marcar como tales:

| Dato | Por qué |
|---|---|
| **(a) Fecha de notificación / publicación / acto presunto** | Fija el dies a quo. Pedir el **justificante** (acuse, sede electrónica, LexNET). Si el cliente "cree que fue por ahí", marcarlo `[ESTIMADO — pendiente de justificante]` y no cerrar el cálculo. |
| **(b) Tipo de actuación impugnada** | Expresa / presunta / vía de hecho / disposición general / inactividad (art. 29) / lesividad / litigio entre Administraciones. |
| **(c) ¿Hubo reposición potestativa?** | Cambia el dies a quo al art. 46.4. |
| **(d) ¿Es procedimiento de derechos fundamentales?** | Invierte la regla de agosto y acorta el plazo a 10 días. |
| **(e) ¿El acto agota la vía administrativa?** | Si no, el contencioso es prematuro — falta la alzada. Cruzar con `/admisibilidad-ca`. |

### 2. Fijar el dies a quo — art. 30 LPAC (verificado)

- **Plazos en meses (art. 30.4):** se computan **a partir del día siguiente** a la notificación,
  publicación o producción del silencio. **El plazo concluye el mismo día ordinal** en que se
  produjo la notificación, en el mes de vencimiento. Notificación el 15 de marzo → 2 meses →
  vence el **15 de mayo** (no el 16).
- **Si en el mes de vencimiento no hay día equivalente, expira el último día del mes** (art. 30.4
  in fine). Notificación el 31 de diciembre → 2 meses → vence el **28/29 de febrero**.
- **Plazos en días (art. 30.2 y 30.3):** hábiles salvo que la norma diga naturales; se cuentan
  desde el día siguiente. Excluidos sábados, domingos y festivos.
- **Último día inhábil → se prorroga al primer día hábil siguiente** (art. 30.5).
- **Art. 30.6:** si un día es hábil en el domicilio del interesado e inhábil en la sede del órgano,
  o a la inversa, **se considera inhábil en todo caso**. Comprobar los festivos locales y
  autonómicos de ambas sedes; nunca asumir el calendario nacional.

### 3. Tabla del art. 46 LJCA (verificada — fuente única: `references/anclas-normativas-ca.md`)

| Supuesto | Plazo | Dies a quo | Norma |
|---|---|---|---|
| Acto **expreso** que pone fin a la vía administrativa | **2 meses** | Día siguiente a la notificación | 46.1 |
| Acto **presunto** (silencio) | **6 meses** | Día siguiente a producirse el acto presunto | 46.1 |
| **Disposición general** | **2 meses** | Día siguiente a la publicación | 46.1 |
| Tras **reposición potestativa**, expresa o presunta | **2 meses** | Día siguiente a la notificación de la resolución o a la desestimación presunta | 46.4 |
| **Inactividad** (art. 29) | **2 meses** | Día siguiente al vencimiento de los plazos del art. 29 (3 meses del 29.1; 1 mes del 29.2) | 46.2 |
| **Vía de hecho CON requerimiento previo** (art. 30) | **10 días** | Día siguiente al fin del plazo de 10 días del art. 30 | 46.3 |
| **Vía de hecho SIN requerimiento** | **20 días** | Día en que se inició la actuación material | 46.3 |
| **Lesividad** | **2 meses** | Día siguiente a la declaración de lesividad | 46.5 |
| **Entre Administraciones** | **2 meses** | (Si precedió requerimiento del art. 44: desde la comunicación del acuerdo o su rechazo presunto) | 46.6 |

> **Vía de hecho: los plazos son de 10/20 días, no de meses.** Es el supuesto donde más rápido se
> pierde la acción. Si el usuario describe una actuación material sin cobertura (una demolición,
> una ocupación, una retirada), **calcular esto lo primero y avisar el mismo día**.

### 4. ⚠️ Agosto — art. 128.2 LJCA (verificado). La excepción está INVERTIDA respecto del civil

> «Durante el mes de agosto **no correrá** el plazo para interponer el recurso
> contencioso-administrativo **ni ningún otro plazo** de los previstos en esta Ley **salvo para el
> procedimiento para la protección de los derechos fundamentales en el que el mes de agosto tendrá
> carácter de hábil.»**

**Comprobarlo SIEMPRE, en todo cálculo. Sin excepción.**

- **Regla general LJCA:** agosto **no corre** — para *todos* los plazos de la Ley, no solo el de
  interposición.
- **Excepción DDFF:** en el procedimiento de derechos fundamentales agosto **SÍ es hábil**. El
  plazo de **10 días** del art. 115.1 **corre en agosto**. Es la trampa clásica: quien aplica el
  reflejo civil ("en agosto no pasa nada") pierde el recurso de amparo ordinario.
- **No citar el art. 133 LEC ni el art. 183 LOPJ como fundamento.** Son la regla civil. Aquí manda
  el art. 128.2 LJCA.
- **Regla operativa de seguridad — aplicar siempre:** cuando el cómputo atraviese agosto, calcular
  **las dos fechas** (sin descontar agosto y descontando agosto) y **presentar el escrito antes de
  la MÁS TEMPRANA**. Nunca gastar el margen que da la suspensión de agosto: es un colchón, no una
  fecha objetivo. La mecánica exacta del traslado del vencimiento es objeto de discusión y no se
  arriesga un asunto a ganar la discusión.

**Art. 128.1 (verificado):** los plazos son **improrrogables**; transcurridos, el LAJ tiene por
caducado el derecho y por perdido el trámite. Se admite el escrito presentado **dentro del día en
que se notifique la resolución** de caducidad — **salvo cuando se trate de plazos para preparar o
interponer recursos**. Es decir: esta válvula **no salva** una interposición, una apelación ni una
preparación de casación fuera de plazo. No ofrecerla nunca como red de seguridad.

**Art. 128.3 (verificado):** en casos de urgencia las partes pueden pedir la **habilitación de días
inhábiles** en el procedimiento de DDFF o en el incidente de suspensión / medidas cautelares. El
órgano oye a las partes y resuelve **por auto en 3 días**, y **debe** acordar la habilitación cuando
denegarla pudiera causar **perjuicios irreversibles**. Si el acto va a ejecutarse en agosto,
cruzar con `/medidas-cautelares-ca`.

### 5. Silencio administrativo (no hay skill propia — se trata aquí)

**Antes de afirmar el sentido del silencio en un caso concreto, verificar con
`buscar_articulo("LPAC","24")` y `("LPAC","25")` y, sobre todo, con la norma sectorial: el sentido
del silencio lo fija la norma reguladora del procedimiento, no la intuición.**

**Procedimientos iniciados a solicitud del interesado — art. 24 LPAC (verificado):**
- Regla general: **silencio positivo**, salvo que una norma con rango de ley o de Derecho de la UE
  o internacional disponga lo contrario.
- **Silencio NEGATIVo por mandato del propio art. 24.1**, párrafo 2.º: derecho de petición (art. 29
  CE); actos cuya estimación transfiriera al solicitante o a terceros facultades sobre **dominio
  público** o **servicio público**; actividades que puedan **dañar el medio ambiente**; y
  **procedimientos de responsabilidad patrimonial**.
- **Impugnación de actos y disposiciones y revisión de oficio a instancia de parte: silencio
  NEGATIVO** (art. 24.1, párrafo 3.º). Por eso los recursos administrativos se desestiman por
  silencio.
- **Contra-excepción (silencio positivo de segundo grado):** si la **alzada** se interpuso contra
  una **desestimación presunta** y la Administración tampoco resuelve la alzada en plazo, la alzada
  **se entiende ESTIMADA** — salvo que verse sobre las materias del párrafo anterior (dominio
  público, servicio público, medio ambiente, responsabilidad patrimonial, petición). Comprobarlo
  siempre: es un ángulo que casi nadie explota.
- **Art. 24.2:** el silencio **estimatorio** es un acto administrativo finalizador del
  procedimiento a todos los efectos. El **desestimatorio** tiene los **solos efectos** de permitir
  interponer el recurso procedente — es una ficción procesal, no un acto.
- **Art. 24.3:** tras el silencio, la resolución expresa tardía **solo puede ser confirmatoria** si
  el silencio fue **positivo**; si fue **negativo**, la Administración resuelve **sin vinculación
  alguna** al sentido del silencio.

**Plazos de la vía administrativa previa (verificado — LPAC arts. 121-124):**

| Recurso | Plazo si acto **expreso** | Plazo si acto **presunto** | Plazo de resolución / silencio |
|---|---|---|---|
| **Alzada** | **1 mes** (art. 122.1) — transcurrido, **la resolución es firme a todos los efectos** | **En cualquier momento** desde el día siguiente a los efectos del silencio (art. 122.1, párr. 2.º) | **3 meses**; transcurridos, se entiende **desestimado** salvo el supuesto del art. 24.1, párr. 3.º (art. 122.2) |
| **Reposición** (potestativo) | **1 mes** (art. 124.1) — transcurrido, **solo cabe ya el contencioso** | **En cualquier momento** desde el día siguiente al acto presunto (art. 124.1, párr. 2.º) | **1 mes** (art. 124.2); sentido **desestimatorio** ex art. 24.1, párr. 3.º |

> ⚠️ **ERRATA A EVITAR — decirlo expresamente si el usuario la trae.** El plazo de **3 meses** para
> recurrir en alzada un **acto presunto** era el **art. 115.1 de la derogada Ley 30/1992**. Desde la
> **Ley 39/2015** (2-10-2016) el recurso contra acto presunto se interpone **«en cualquier
> momento»** (arts. 122.1 y 124.1). Está en manuales, plantillas y modelos antiguos que siguen
> circulando. **No citar nunca ese plazo de 3 meses.**

**Puntos clave que la skill debe advertir siempre en silencio negativo:**
1. El plazo contencioso frente al silencio negativo es de **6 meses** (art. 46.1), no de 2.
2. El acto presunto **no cierra la puerta a una resolución expresa tardía**: la Administración
   **conserva el deber de resolver** (**art. 21.1 LPAC**, verificado — obligación de dictar
   resolución expresa y notificarla en *todos* los procedimientos). Si llega resolución expresa
   después, **abre un plazo nuevo de 2 meses** desde su notificación. No dar por perdido el asunto
   sin comprobar si hubo resolución tardía.
3. **Acreditar el silencio** (art. 24.4): produce efectos desde el vencimiento del plazo máximo;
   puede probarse por cualquier medio, incluido el **certificado acreditativo del silencio**, que
   se expide de oficio en 15 días y que el interesado puede pedir en cualquier momento.
4. **Sancionador y demás procedimientos de gravamen: no hay silencio, hay CADUCIDAD** (art. 25.1.b
   LPAC, verificado). Si el procedimiento se inició de oficio y era sancionador o de intervención,
   el vencimiento del plazo produce la **caducidad** y el archivo — no un acto presunto que
   recurrir. **Es un motivo de fondo de primer orden: comprobarlo antes de calcular nada.**
   Si el procedimiento de oficio podía reconocer derechos, el silencio es **desestimatorio**
   (art. 25.1.a).

### 6. Plazos internos del proceso (verificados)

| Trámite | Plazo | Norma |
|---|---|---|
| **Demanda** desde la entrega del expediente | 20 días | art. 52.1 LJCA |
| **Contestación** a la demanda | 20 días | art. 54.1 LJCA |
| **Subsanación** de los documentos del art. 45.2 | 10 días | art. 45.3 LJCA |
| **Conclusiones** | 10 días | art. 64.1 LJCA |
| **Apelación** (interposición ante el Juzgado a quo) | 15 días | art. 85.1 LJCA |
| **Preparación de casación** (ante la Sala de instancia) | **30 días** | art. 89.1 LJCA |
| **Emplazamiento ante el TS** tras tenerse por preparada | **15 días** | art. 89.5 (RD-ley 5/2023) |
| **DDFF** — interposición | 10 días | art. 115.1 LJCA (**agosto hábil**) |

> Estos plazos son **de la LJCA** → agosto **no corre** en ellos (salvo DDFF). Y son plazos de
> **días hábiles procesales**.
>
> **Ampliación del expediente incompleto (art. 55 LJCA): SUSPENDE el plazo de demanda o
> contestación.** Pedirla dentro de los **10 primeros días** del plazo y que se acepte → el plazo
> se **reinicia**. Después de esos 10 días, o si se rechaza → simplemente se **reanuda**. Ver
> `/expediente-administrativo-ca`. Por eso el índice del expediente se revisa **el día que llega**.

### 7. Salida

```
## Cómputo de plazos — [slug del asunto]

| Concepto | Valor |
|---|---|
| Acto impugnado | [tipo — expreso / presunto / vía de hecho / disposición] |
| Fecha de notificación / acto presunto | AAAA-MM-DD [✅ acreditada con [justificante] / ⚠️ ESTIMADA] |
| Dies a quo | AAAA-MM-DD (día siguiente — art. 30.4 LPAC) |
| Plazo aplicable | [2 meses / 6 meses / 10 días / 20 días] |
| Norma | art. 46.[x] LJCA |
| ¿Atraviesa agosto? | [No / Sí — art. 128.2 LJCA: agosto no corre / Sí — DDFF: agosto HÁBIL] |
| **Fecha de caducidad** | **AAAA-MM-DD** |
| Fecha de caducidad sin descontar agosto (control) | AAAA-MM-DD |
| **Fecha de presentación recomendada** | **AAAA-MM-DD** (margen del perfil — DEFAULT 7 días naturales) |
| Días restantes desde hoy | [n] |
| Estado | ✅ En plazo / ⚠️ Margen crítico (< margen del perfil) / 🔴 VENCIDO / ❓ INDETERMINADO |

**Cómputo razonado:** [2-4 líneas explicando el recorrido: dies a quo → regla de meses →
agosto → último día inhábil.]

**Advertencias:** [caducidad no interrumpible; datos sin acreditar; resolución tardía posible;
festivo local a comprobar; etc.]
```

Después, **escribir el resultado en el asunto** (vía `/actualizar-asunto`, no editando a mano):
- `matters/<slug>/matter.md` y `matters/_log.yaml` → `fecha_notificacion`,
  **`fecha_caducidad_interposicion`**, `next_deadline`.
- Entrada en `history.md` con el cómputo razonado y la norma aplicada.

## Reglas

1. **Regla de oro.** Ante **cualquier** duda sobre si un plazo venció o sobre la fecha de
   notificación, **decirlo con claridad y recomendar verificación humana inmediata**. Estado
   `❓ INDETERMINADO`, nunca `✅`. **Jamás tranquilizar al usuario con un cálculo dudoso.** El coste
   de un falso negativo es la pérdida irreversible de la acción; el de un falso positivo, una
   comprobación de diez minutos. La asimetría es total.
2. **🔴 VENCIDO → parar.** Decirlo el primero, antes de nada. No redactar el escrito. Explicar el
   art. 69.e LJCA. Explorar solo lo que quede: ¿hubo resolución expresa tardía que reabra el plazo
   (art. 21.1 LPAC)? ¿la notificación fue defectuosa y por tanto no desplegó efectos? ¿incurre el
   acto en alguna causa de **nulidad de pleno derecho del art. 47.1 LPAC**? — porque la **revisión
   de oficio del art. 106.1 LPAC** (verificado) procede **«en cualquier momento»**, también a
   solicitud del interesado, precisamente sobre actos **«que no hayan sido recurridos en plazo»**,
   previo **dictamen favorable** del Consejo de Estado u órgano consultivo autonómico. Es estrecha
   (solo art. 47.1, y el órgano puede inadmitir a trámite ex art. 106.3), pero es la única puerta
   que queda y hay que valorarla expresamente, no mencionarla de pasada. Y
   advertir de la posible **responsabilidad civil profesional**: es una conversación que hay que
   tener, no que evitar.
3. **Prohibido inventar plazos, artículos o letras.** Lo que no esté en
   `references/anclas-normativas-ca.md` se verifica con `buscar_articulo` **en el momento**. Si no
   se puede verificar → `[verificar]` y decirlo.
4. **Doble control.** Todo plazo de caducidad se recalcula una segunda vez, por separado, antes de
   cerrarlo en agenda. Es la regla de la casa (ver `CLAUDE.md`).
5. **Agosto se comprueba siempre**, aunque el cálculo parezca no rozarlo.
6. **Fechas absolutas.** Nunca "en dos meses" ni "el mes que viene": AAAA-MM-DD.
7. **La fecha de notificación no se estima.** Depende de ella la admisibilidad. Pedir el acuse.
8. **Nada de MASC.** No existe en esta jurisdicción y no suspende ni interrumpe nada. Si el usuario
   lo menciona, corregirlo: aquí el equivalente funcional es el **agotamiento de la vía
   administrativa** (art. 25.1 LJCA).
9. **Cero datos personales** en los ejemplos y en los cuadros: `[INTERESADO]`, `[ADMINISTRACIÓN]`.
10. **Prohibido citar jurisprudencia concreta** (ECLI/ROJ/fecha) sin verificarla con
    `buscar_sentencias` / `buscar_por_cita`.
