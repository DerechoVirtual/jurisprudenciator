---
name: conservacion-documental
description: Comunicacion al cliente sobre conservacion de documentacion exculpatoria en un procedimiento penal. Incluye la advertencia critica de que el abogado NUNCA puede aconsejar destruir, alterar u ocultar prueba (arts. 451, 464, 465 CP). Usar con comunicar al cliente que conserve documentacion o que documentacion guarda el cliente.
---

# Conservación documental — comunicación al cliente (penal)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Texto vigente de los tipos que marcan la frontera** (arts. 451, 464, 465, 466 y 467 CP) → `buscar_articulo` (`ley="CP"`) antes de incluirlos en la comunicación.
- **Hasta cuándo conservar** → `buscar_articulo` (`ley="CP"`, `articulo="131"` y `"133"`): prescripción del delito y de la pena.
- **Cliente persona jurídica: quién custodia y desde cuándo** → `buscar_empresa_mercantil` (administradores, apoderados y fechas de nombramiento o cese) para delimitar destinatarios y periodos.
- **Criterio de la Sala Segunda sobre la destrucción de documentos del proceso por el abogado (art. 465 CP)** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

> 📐 **Cifras: `references/anclas-normativas-penal.md`**; lo que no esté ahí se verifica con `buscar_articulo` **antes** de afirmarlo.

---

## ⛔ ADVERTENCIA CRÍTICA — leer antes de usar esta skill

**El abogado NO puede aconsejar destruir, alterar ni ocultar nada. Nunca. En ningún caso.**

Aconsejar al cliente sobre qué conservar es legítimo y necesario. Pero la frontera con la **destrucción u ocultación de pruebas**, el **encubrimiento** y la **obstrucción a la Justicia** es estrecha, y cruzarla es delito **del abogado**, no solo del cliente. Artículos **verificados literalmente con `buscar_articulo` el 2026-07-17**:

| Norma | Conducta | Pena |
|---|---|---|
| **Art. 451.2º CP** — encubrimiento | «**Ocultando, alterando o inutilizando el cuerpo, los efectos o los instrumentos de un delito, para impedir su descubrimiento**», con conocimiento de su comisión y **sin haber intervenido en él como autor o cómplice**, interviniendo con posterioridad a su ejecución | **Prisión de 6 meses a 3 años** |
| **Art. 451.3º CP** — encubrimiento | Ayudar a los presuntos responsables a **eludir la investigación** de la autoridad o a sustraerse a su busca o captura, en los supuestos tasados de la letra a), o **con abuso de funciones públicas** (letra b) | **Prisión de 6 meses a 3 años** (+ inhabilitación en el caso b) |
| **⭐ Art. 465.1 CP** — obstrucción a la Justicia y deslealtad profesional | «**El que, interviniendo en un proceso como abogado o procurador, con abuso de su función, destruyere, inutilizare u ocultare documentos o actuaciones de los que haya recibido traslado en aquella calidad**» | **Prisión de 6 meses a 2 años, multa de 7 a 12 meses e inhabilitación especial para su profesión de 3 a 6 años** |
| **Art. 464.1 CP** — obstrucción a la Justicia | Intentar influir **con violencia o intimidación**, directa o indirectamente, en denunciante, parte, investigado, abogado, procurador, perito, intérprete o **testigo**, para que modifique su actuación procesal | **Prisión de 1 a 4 años y multa de 6 a 24 meses** (mitad superior si se alcanza el objetivo) |
| **Art. 463.1 CP** — obstrucción a la Justicia | Dejar voluntariamente de comparecer, sin justa causa, citado en legal forma, en proceso criminal con reo en prisión provisional, provocando la suspensión del juicio oral | Prisión de 3 a 6 meses o multa de 6 a 24 meses |
| **Art. 463.2 CP** | **Si el responsable es abogado o procurador** en actuación profesional | **Pena en su mitad superior + inhabilitación especial de 2 a 4 años** |
| **Art. 467.2 CP** — deslealtad profesional | Abogado que, por acción u omisión, **perjudique de forma manifiesta** los intereses que le fueren encomendados | Multa de 12 a 24 meses e inhabilitación especial de 1 a 4 años (menor si es por imprudencia grave) |

### Cómo se traduce esto en la práctica

1. **El art. 465.1 CP apunta directamente al abogado.** Destruir, inutilizar u ocultar documentos o actuaciones **de los que se ha recibido traslado** en calidad de abogado es un tipo penal propio, con inhabilitación de hasta 6 años. Las actuaciones que el juzgado nos traslada no son nuestras: son del proceso.
2. **El art. 451 CP alcanza a quien no es autor del delito investigado.** El propio investigado que oculta la prueba de su propio delito no comete encubrimiento (el tipo exige «sin haber intervenido en el mismo como autor o cómplice»). **Pero el abogado sí ha de tener presente que él no es el autor del delito investigado**: si interviene ocultando, alterando o inutilizando el cuerpo, los efectos o los instrumentos del delito para impedir su descubrimiento, **el tipo del art. 451.2º le es plenamente aplicable**. Que el cliente pueda no delinquir haciéndolo él mismo **no significa que el abogado pueda aconsejárselo, ni hacerlo por él, ni ayudarle a hacerlo.**
3. **Nunca sugerir al cliente que "haga desaparecer", "limpie", "revise el móvil", "borre el chat" ni nada equivalente**, ni siquiera de forma implícita, ambigua o en clave de hipótesis. Si el cliente lo plantea, **la respuesta es no, y se le explica por qué**.
4. **No influir sobre testigos.** Sugerir a un testigo qué debe decir, o hacérselo sugerir por el cliente, roza el art. 464 CP si media violencia o intimidación, y en todo caso compromete al letrado deontológicamente. Preparar a un testigo sobre el procedimiento es legítimo; dictarle el contenido de su declaración, no.
5. **Si el cliente comunica que ya ha destruido algo**, eso es un hecho pasado que entra en el ámbito del **secreto profesional** (art. 542.3 LOPJ). Distinto es que anuncie la **intención de destruir en el futuro**: ahí el letrado debe disuadirle expresamente y dejar constancia del consejo dado.
6. **Ante la duda, no se toca nada.** El consejo por defecto es **conservar**, nunca eliminar.

> **En caso de duda sobre si un consejo concreto cruza la línea: no darlo, y consultar al Colegio.** Esta skill no sustituye ese juicio.

---

## ⭐ Cambio de fondo respecto del civil: NO hay carga de la prueba para el defendido

**Esto no es un legal hold civil.** En el proceso civil, quien afirma debe probar, y la pérdida culposa de prueba en poder de quien debía custodiarla puede volverse contra él. **En penal el esquema es el contrario:**

- **Art. 24.2 CE** *(literal verificado)* — todos tienen derecho «a no declarar contra sí mismos, a no confesarse culpables y a la **presunción de inocencia**».
- **La carga de la prueba corresponde íntegramente a la ACUSACIÓN.** El investigado no tiene que probar su inocencia, ni acreditar nada, ni aportar nada en su contra.
- **Art. 118.1.g) y h) LECrim** — el investigado tiene derecho a **guardar silencio** y a **no declarar contra sí mismo**.
- → **De la falta de prueba de descargo NO puede derivarse una presunción en contra del defendido.** No existe en penal el reproche procesal por no aportar.

> ⛔ **No trasladar los arts. 217 ni 328-329 LEC.** El art. 217 LEC (carga de la prueba) y la exhibición documental entre partes de los arts. 328-329 LEC son del orden civil y **no rigen aquí**. Si en el asunto hay una **pieza de responsabilidad civil** derivada del delito, esas normas podrían operar de forma **supletoria y solo en ese ámbito acotado** — y aun así, **verificar antes de invocarlas** y nunca extenderlas al enjuiciamiento de la responsabilidad penal.

**Consecuencia práctica:** la conservación en penal no es una carga, es una **oportunidad**. Se conserva lo **exculpatorio** porque conviene a la defensa, no porque exista un deber de aportarlo.

---

## ⭐ Qué conserva el cliente y qué no

**El sumario y las actuaciones las tiene el JUZGADO, no el cliente.** El cliente no custodia el expediente; accede a él a través de su letrado (art. 118.1.b LECrim). Por tanto, esta skill **no** versa sobre "conservar el expediente".

**Lo que sí está en manos del cliente y conviene conservar:**

| Categoría | Ejemplos |
|---|---|
| **Documentación exculpatoria** | Justificantes de que estaba en otro lugar, contratos, autorizaciones, licencias, albaranes, partes de trabajo, registros de acceso |
| **Comunicaciones** | Correos, mensajería y cartas con la contraparte, la víctima, testigos o terceros, **con sus metadatos** |
| **Justificantes** | Transferencias, pagos, facturas, tickets, extractos — decisivos en patrimoniales y económicos |
| **Informes periciales de parte** | Forense de parte, calígrafo, informático forense, tasador |
| **Documentación de reparación del daño** | Justificantes de consignación, pago o reparación → relevantes para el **art. 21.5ª CP** *(atenuante de reparación — verificar antes de citar)* y para la **suspensión del art. 80 CP**, cuyo apdo. 1 valora expresamente el **esfuerzo por reparar el daño** |
| **Persona jurídica** | Modelo de organización y gestión, actas, evidencias de funcionamiento del compliance (art. 31 bis CP) |
| **Historial médico / laboral** | Cuando sea relevante a la imputabilidad, a las lesiones o a las circunstancias personales |

**Lo que NO se pide al cliente:** el expediente judicial, atestados, declaraciones sumariales — están en las actuaciones.

---

## Cuándo activar

- Tras el intake, cuando haya documentación en poder del cliente relevante para su defensa
- "¿Qué documentación tiene que guardar el cliente?"
- "El cliente pregunta si puede borrar los correos" → ⚠️ ver la advertencia crítica
- Antes de una declaración o de la audiencia preliminar, para localizar descargo

## Subcomandos

### `--emitir` (default)

Generar comunicación al cliente. **Redactada en clave de conservación de descargo, nunca de carga probatoria:**

```
[Lugar y fecha]

Estimado/a [CLIENTE],

En relación con [las Diligencias Previas nº [X] seguidas ante la Sección de Instrucción
nº [X] del Tribunal de Instancia de [LUGAR] / referencia interna [REF]], le traslado
formalmente la siguiente
recomendación sobre la documentación que obra en su poder.

1. CONSERVE TODA LA DOCUMENTACIÓN RELACIONADA CON LOS HECHOS

No elimine, altere, modifique ni destruya ningún documento, archivo, mensaje o soporte
relacionado con los hechos investigados, con independencia de que a usted le parezca
favorable, desfavorable o irrelevante. Esa valoración me corresponde a mí como su
letrado, y para hacerla necesito verlo todo.

2. DOCUMENTACIÓN QUE INTERESA CONSERVAR

  1. [Categoría 1: ej. comunicaciones con [tercero] desde [fecha]]
  2. [Categoría 2: ej. justificantes de pago / transferencias del periodo [fechas]]
  3. [Categoría 3: ej. contratos, autorizaciones o licencias relativos a [objeto]]
  4. [Categoría 4: ej. informes médicos, partes de trabajo]
  5. [Etc.]

3. INSTRUCCIONES CONCRETAS

  - No borre correos ni mensajes, ni vacíe papeleras o archivos
  - No destruya documentos en papel
  - Conserve las copias de seguridad existentes a día de hoy
  - Si sus sistemas borran automáticamente mensajes pasado cierto tiempo, deshabilite
    ese borrado para las cuentas relevantes
  - Conserve los METADATOS (fechas de envío y recepción, autoría, geolocalización si
    la hubiera): no convierta los documentos a formatos que los pierdan, ni reenvíe
    capturas de pantalla en lugar del original
  - No manipule dispositivos (móvil, ordenador) tratando de "ordenarlos" o "limpiarlos"
  - Si algún soporte está en poder de un tercero, comuníquemelo antes de solicitárselo

4. ADVERTENCIA IMPORTANTE

Debo advertirle con claridad de que NO PUEDO ACONSEJARLE, NI LE ACONSEJO, DESTRUIR,
ALTERAR NI OCULTAR NINGÚN DOCUMENTO, ARCHIVO O EFECTO, ni antes ni durante ni después
del procedimiento. La ocultación, alteración o inutilización del cuerpo, los efectos o
los instrumentos de un delito para impedir su descubrimiento está tipificada en el
artículo 451 del Código Penal, y la obstrucción a la Justicia en los artículos 463 y
siguientes. Tampoco debe usted dirigirse a testigos para influir en lo que vayan a
declarar.

Si alguien le sugiere lo contrario, no lo haga y llámeme antes.

5. LO QUE NO DEBE PREOCUPARLE

Conviene que sepa que en el proceso penal USTED NO TIENE QUE PROBAR SU INOCENCIA. Rige
la presunción de inocencia del artículo 24.2 de la Constitución y la carga de la prueba
corresponde íntegramente a la acusación. Le pido que conserve esta documentación porque
puede resultarle FAVORABLE y quiero poder usarla, no porque exista obligación alguna de
aportar nada en su contra. Usted tiene además derecho a guardar silencio y a no declarar
contra sí mismo.

6. DURACIÓN

Hasta nueva comunicación por mi parte. El procedimiento puede prolongarse durante años
y atravesar varias fases —instrucción, juicio oral, recursos y ejecutoria—, y la
documentación puede resultar necesaria en cualquiera de ellas.

Cualquier duda sobre qué conservar o cómo, consúltemela ANTES de tomar ninguna decisión.

Atentamente,

[LETRADO]
Colegiado nº [Nº] — [COLEGIO DE ABOGADOS]
```

### `--refrescar`

Reenviar tras el paso del tiempo o al cambiar de fase (transformación en abreviado, apertura de juicio oral, señalamiento) para confirmar que el deber sigue vigente.

### `--liberar`

Solo cuando el asunto esté **firme y ejecutado**, o la documentación haya dejado de ser relevante. **Ser conservador con este subcomando.**

```
[...] la recomendación de conservación documental que le trasladé en [fecha] queda sin
efecto en cuanto a [tipo de documentación], al haber [ganado firmeza la resolución /
concluido la ejecutoria / ...]. Puede aplicar a esos documentos sus políticas habituales
de conservación, sin perjuicio de los plazos legales que le sean aplicables por otras
razones.
```

> ⚠️ **No liberar mientras quepa recurso, quede ejecutoria pendiente, esté viva la responsabilidad civil o no haya transcurrido la prescripción de la pena (art. 133 CP).** Ante la duda, no liberar. Una liberación prematura seguida de una destrucción es exactamente el escenario que esta skill existe para evitar.

### `--estado`

| Slug | Fecha emisión | Último refresh | Fase procesal | Estado |
|---|---|---|---|---|
| .. | .. | .. | .. | activo / liberado |

## Flujo

### 1. Identificar categorías

Vía `AskUserQuestion`:
- ¿Qué documentación en poder del cliente puede ser **exculpatoria** o relevante?
- ¿En qué soporte? (correo, mensajería, papel, dispositivos, sistemas internos)
- ¿Quién tiene acceso? (solo el cliente / empleados / terceros)
- ¿Hay **reparación del daño** documentable? (relevante para el art. 80 CP y la atenuante del art. 21.5ª CP)
- Si es persona jurídica: ¿hay modelo de organización y gestión y evidencias de su funcionamiento?

### 2. Redactar

Aplicar la plantilla con las categorías concretas. **Los apartados 4 y 5 no se eliminan nunca.**

### 3. Output

- Word `.docx` en `matters/<slug>/conservacion-v[N].docx`

> ⚠️ **Slug `descriptor-delito-año`. Nunca el nombre del cliente** en la ruta ni en el archivo (art. 10 RGPD: datos de infracciones y condenas penales).

- Actualizar `_log.yaml`: `conservacion_documental: emitida-AAAA-MM-DD`
- Apuntar el próximo refresh según la fase

### 4. Envío

Si hay conector de correo disponible, crear **borrador** con el texto y el Word adjunto, listo para que el letrado lo revise y lo envíe. **Nunca enviar automáticamente.**

## Reglas

1. ⛔ **El abogado no puede aconsejar destruir, alterar u ocultar nada.** Arts. 451, 463-465 y 467 CP. Si el usuario pide redactar algo que sugiera lo contrario —aunque sea de forma velada, hipotética o "solo para valorar"— **negarse y explicar por qué**.
2. ⭐ **No hay carga de la prueba para el defendido.** Presunción de inocencia (art. 24.2 CE); la carga es de la acusación. No redactar nunca la comunicación en términos de "tiene que poder probar".
3. ⛔ **No invocar los arts. 217 ni 328-329 LEC** como fundamento. Son civiles. Como mucho, supletorios y solo en la pieza de responsabilidad civil — **verificar antes**.
4. **El consejo por defecto es conservar.** Ante la duda, no se toca nada.
5. **Metadatos**: críticos para la autenticidad y para la cadena de custodia de la prueba digital. Recordarlo siempre.
6. **El sumario lo tiene el juzgado.** No pedir al cliente que conserve actuaciones.
7. **No influir sobre testigos** ni pedir al cliente que lo haga (art. 464 CP).
8. **Verificar cada artículo con `buscar_articulo`** antes de citarlo al cliente. Los de la tabla de la advertencia crítica están verificados el 2026-07-17.
9. ⛔ **Prohibido citar jurisprudencia concreta** (ECLI/ROJ/fecha).
10. **Cero datos reales**: `[CLIENTE]`, `[LETRADO]`, `[LUGAR]`, `[X]`.

## Handoffs

- Si llega un oficio pidiendo documentación del despacho: `/revision-secreto-profesional` **antes** de entregar nada
- Si hay que triar una citación o resolución: `/requerimiento-judicial-triage`
- Si la reparación del daño está documentada: llevarla al escrito de defensa y a la petición de suspensión (art. 80 CP)
