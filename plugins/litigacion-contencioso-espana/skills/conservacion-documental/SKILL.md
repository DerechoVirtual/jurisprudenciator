---
name: conservacion-documental
description: Comunicacion al cliente sobre que documentacion debe conservar y cual hay que pedir ya en un asunto contencioso-administrativo. La prueba central es el expediente administrativo, que lo tiene la Administracion. El cliente conserva las notificaciones con su acuse (determinan el dies a quo), las alegaciones con justificante de registro, los informes periciales y, en sanitario, la historia clinica. Usar con comunicar al cliente que conserve documentacion.
---

# Conservación documental — Comunicación al cliente

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Preceptos que se citan en la comunicación al cliente** → `buscar_articulo` (`ley="LJCA"`, artículos 46 y 48; `ley="LPAC"`, artículo 53).
- **Asunto sanitario: conservación y acceso a la historia clínica** → `buscar_articulo` (`ley="Ley 41/2002"`, artículos 17 y 18).
- **Plazos legales de conservación del cliente empresario** que prevalecen sobre la liberación → `buscar_articulo` (`ley="Código de Comercio"`, `articulo="30"`).
- **No liberar con plazos vivos** → `buscar_articulo` (`ley="LJCA"`, artículos 85 y 89) antes de emitir `--liberar`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

> 🎯 **Premisa que cambia todo respecto del civil: en contencioso-administrativo la prueba central NO está en manos del cliente.**
>
> El **expediente administrativo** lo tiene la **Administración**. Se reclama de oficio al órgano autor del acto (art. 48.1 LJCA), que debe remitirlo **completo, en soporte electrónico, foliado, autentificado y con índice**, en el **plazo improrrogable de 20 días** desde que la comunicación judicial entra en su registro (art. 48.3 y 48.4 LJCA). Si no lo remite, cabe reiteración y **multas coercitivas de 300 a 1.200 €** a la autoridad o empleado responsable, reiterables cada 20 días (art. 48.7 LJCA); tras tres multas sin éxito, el órgano lo pone en conocimiento del Ministerio Fiscal (art. 48.10).
>
> Por tanto, esta skill **no es un "legal hold" civil**. Su función es doble:
> 1. **CONSERVAR** lo poco pero decisivo que sí tiene el cliente.
> 2. **PEDIR YA** lo que tienen terceros y puede perderse o tardar (historia clínica, informes).

## Cuándo activar

- Tras `/asunto-intake`, en cuanto se identifica el acto impugnado
- "El cliente puede haber tirado la notificación"
- "Necesito que el cliente no borre los correos con el Ayuntamiento"
- Antes de que venza el plazo de conservación de un tercero (historia clínica, grabaciones, registros)
- Recurso inminente y documentación en poder del cliente o de un tercero

## Marco legal

**Propio del orden contencioso:**

- **Art. 48 LJCA** — reclamación y remisión del expediente administrativo: 20 días improrrogables, completo, electrónico, foliado, autentificado y con índice; multas coercitivas si no se remite (48.7); exclusión motivada de los documentos clasificados como **secreto oficial** (48.6).
- **Art. 46 LJCA** — plazos de interposición, de **caducidad**: por eso el **acuse de la notificación** es el documento más importante del asunto.
- **Art. 53.1.a) LPAC** — derecho del **interesado** a conocer el estado del procedimiento y a **acceder y obtener copia** de los documentos contenidos en los procedimientos en que lo sea. Es el título con el que el cliente puede pedir copia de su expediente **en vía administrativa, antes del pleito**.
- **Art. 53.1.e) LPAC** — derecho a formular alegaciones y aportar documentos en cualquier fase anterior al trámite de audiencia, que **deben ser tenidos en cuenta** al redactar la propuesta de resolución. De ahí el valor del **justificante de registro**.

**Sanitario (responsabilidad patrimonial sanitaria):**

- **Art. 17.1 Ley 41/2002** — los **centros sanitarios** están obligados a conservar la documentación clínica, como **mínimo cinco años desde la fecha del alta** de cada proceso asistencial. ⚠️ **La historia clínica NO la tiene el cliente: la tiene el centro, y ese plazo corre.**
- **Art. 17.2 Ley 41/2002** — la documentación clínica se conserva también **a efectos judiciales** conforme a la legislación vigente.
- **Art. 18 Ley 41/2002** — el paciente tiene **derecho de acceso a la historia clínica y a obtener copia**, ejercitable también por representación acreditada. Límites (18.3): no puede ejercerse en perjuicio de la **confidencialidad de datos de terceros** recogidos en interés terapéutico del paciente, ni frente a la **reserva de anotaciones subjetivas** de los profesionales. Pacientes fallecidos: acceso de las personas vinculadas por razones familiares o de hecho, salvo prohibición expresa acreditada (18.4).

**Protección de datos:**

- **RGPD + LO 3/2018** — la conservación con fines de defensa se ampara en el art. 6.1.c y 6.1.f RGPD, con respeto a la **minimización** (art. 5.1.c).
- ⚠️ **Los datos de salud son CATEGORÍA ESPECIAL del art. 9 RGPD.** Su tratamiento en el asunto se ampara en el **art. 9.2.f RGPD** (formulación, ejercicio o defensa de reclamaciones) y **solo para el pleito**. Los datos de salud de **terceros** que aparezcan en la historia o el expediente: nunca sin base jurídica — ver `/revision-secreto-profesional`.

**Supletorio — decirlo siempre que se cite:**

- **LEC 217** (carga de la prueba) y **LEC 328-329** (exhibición de documentos entre partes y a terceros) **solo se aplican como Derecho supletorio**, por la **DF 1.ª LJCA**, en lo no previsto por la LJCA. **No son la norma primaria de este orden** y no deben invocarse como tal ante el cliente ni en un escrito sin advertir de su carácter supletorio. En materia de expediente, la LJCA sí prevé el régimen (art. 48): no hay laguna que colmar.
- **Plazos legales de conservación** propios del cliente empresario (mercantil: 6 años, art. 30 CCo; tributario; laboral) — prevalecen sobre cualquier liberación posterior.

## Subcomandos

### `--emitir` (default)

Generar la comunicación al cliente. **Dos bloques: lo que conserva y lo que hay que pedir ya.**

```
[Lugar y fecha]

Estimado/a [CLIENTE]:

Como sabe, estamos preparando el recurso contra la resolución de [ÓRGANO] de fecha
[FECHA] (expediente [EXPEDIENTE]). Le explico qué documentación es relevante y qué
debemos hacer con ella.

Antes de nada, una aclaración importante: el grueso de la prueba de este procedimiento
es el EXPEDIENTE ADMINISTRATIVO, que está en poder de la Administración y que el
Juzgado le reclamará de oficio. No hace falta que usted lo reconstruya. Pero hay
documentación que solo está en sus manos, o en las de un tercero, y que sí puede
perderse.

────────────────────────────────────────────────────────────
1. DOCUMENTACIÓN QUE DEBE CONSERVAR — NO LA DESTRUYA
────────────────────────────────────────────────────────────

1.1 LAS NOTIFICACIONES, CON SU ACUSE Y SU FECHA — LO MÁS IMPORTANTE

    Conserve el sobre, el aviso de correos, el acuse de recibo, el justificante de
    la notificación electrónica y cualquier documento que acredite QUÉ DÍA recibió
    usted la resolución.

    Por qué importa tanto: el plazo para recurrir es de CADUCIDAD y se cuenta desde
    el día siguiente a la notificación. Si no podemos acreditar la fecha, no podemos
    acreditar que el recurso va en plazo, y el recurso puede ser inadmitido sin
    entrar en el fondo. Este papel vale más que cualquier otro del asunto.

    - Si la notificación fue electrónica: conserve el justificante de puesta a
      disposición y el de acceso. No borre el buzón ni la carpeta de notificaciones.
    - Si le llegó por correo: conserve el sobre con el matasellos.
    - Si no está seguro de la fecha: dígamelo HOY. No lo deje pasar.

1.2 LAS ALEGACIONES QUE YA PRESENTÓ, CON SU JUSTIFICANTE DE REGISTRO

    Todo escrito que usted haya presentado ante la Administración (alegaciones,
    recursos, solicitudes, aportación de documentos), CON el sello o justificante
    de registro de entrada. El justificante acredita que se presentó y cuándo.

    Si la Administración no las incorpora al expediente que remita al Juzgado, su
    copia sellada es la única forma de probar que existieron y que debieron ser
    tenidas en cuenta.

1.3 LOS INFORMES PERICIALES Y TÉCNICOS

    Cualquier informe encargado a un profesional (médico, arquitecto, ingeniero,
    tasador), incluidos los borradores y la documentación que se le entregó para
    elaborarlo.

1.4 SU CORRESPONDENCIA CON LA ADMINISTRACIÓN

    Correos, escritos, requerimientos recibidos y respuestas. Incluidos los
    contactos informales (correos al técnico, al instructor). NO vacíe la papelera
    ni el archivo.

1.5 [SANITARIO] LA DOCUMENTACIÓN CLÍNICA QUE TENGA EN SU PODER

    Informes de alta, pruebas, recetas, partes de baja, justificantes de citas.

1.6 [OTRAS CATEGORÍAS PROPIAS DEL ASUNTO]

    [Ej.: licencias previas, proyectos, fotografías fechadas del estado de la obra,
    contratos, justificantes de pago de la subvención, nóminas]

────────────────────────────────────────────────────────────
2. DOCUMENTACIÓN QUE HAY QUE PEDIR YA — NO LA TIENE USTED
────────────────────────────────────────────────────────────

2.1 [SANITARIO] LA HISTORIA CLÍNICA COMPLETA

    La tiene el centro sanitario, no usted. Usted tiene derecho a acceder a ella y
    a obtener copia (art. 18 de la Ley 41/2002), y puede ejercerlo también a través
    de representante acreditado.

    ⚠️ URGENTE: los centros están obligados a conservar la documentación clínica un
    MÍNIMO de cinco años desde la fecha del alta de cada proceso asistencial
    (art. 17.1 de la Ley 41/2002). Ese plazo corre. Pídala ahora, por escrito y
    dejando constancia de la fecha de la solicitud.

    Pida la historia COMPLETA: no solo el informe de alta. Incluya pruebas de
    imagen, hojas de evolución, gráficas de enfermería, consentimientos informados
    y protocolos aplicados.

    Tenga en cuenta que el centro puede reservarse las anotaciones subjetivas de
    los profesionales y los datos de terceros (art. 18.3 de la misma Ley). Si le
    entregan una historia incompleta, dígamelo: se puede reclamar.

2.2 COPIA DEL EXPEDIENTE ADMINISTRATIVO EN VÍA ADMINISTRATIVA

    Como interesado, usted tiene derecho a acceder y a obtener copia de los
    documentos del procedimiento (art. 53.1.a de la Ley 39/2015). Conviene pedirla
    ANTES del pleito: nos permite preparar el recurso sin esperar a que el Juzgado
    reclame el expediente, y nos permite detectar si lo que la Administración remita
    después está incompleto.

2.3 [OTROS TERCEROS]

    [Ej.: grabaciones de videovigilancia (plazos de conservación muy cortos),
    atestados, informes de otros organismos, datos de terceros con plazo de purga]

────────────────────────────────────────────────────────────
3. INSTRUCCIONES CONCRETAS
────────────────────────────────────────────────────────────

- NO borre correos ni vacíe la papelera o el archivo
- NO destruya documentos físicos, sobres ni acuses
- Si sus sistemas borran automáticamente correos pasado cierto tiempo, deshabilite
  ese borrado para las cuentas relevantes
- Si hay empleados o familiares con acceso a esta documentación, comuníqueles este
  deber (puede reenviarles este escrito)
- Conserve los METADATOS (fechas de envío y recepción, autoría): no convierta los
  documentos a formatos que los pierdan, no los reimprima ni los reescanee
- No anote ni altere los originales

────────────────────────────────────────────────────────────
4. DURACIÓN
────────────────────────────────────────────────────────────

Hasta nueva comunicación por mi parte. El procedimiento puede durar años y la
documentación puede solicitarse en distintas fases (demanda, prueba, conclusiones,
apelación, ejecución).

────────────────────────────────────────────────────────────
5. POR QUÉ INSISTO
────────────────────────────────────────────────────────────

Si se pierde el acuse de la notificación, podemos no poder acreditar que el recurso
va en plazo. Si se pierde el justificante de registro de sus alegaciones, podemos no
poder probar que las presentó. Si caduca el plazo de conservación de la historia
clínica, la prueba desaparece y no hay forma de reconstruirla.

Además, la pérdida de documentación por quien debía custodiarla puede valorarse
judicialmente en su contra.

Cualquier duda sobre qué conservar, qué pedir o cómo, contácteme antes de tomar
ninguna decisión.

Atentamente,

[LETRADO]
Colegiado nº [Nº COLEGIADO] — [COLEGIO DE ABOGADOS]
```

### `--refrescar`

Reenviar la comunicación tras el paso del tiempo (p. ej. al recibir el expediente administrativo, al abrirse el período de prueba, tras la sentencia si hay apelación) para confirmar que el deber sigue vigente y para actualizar las categorías a la vista del expediente ya recibido.

### `--liberar`

Si el asunto se cierra o la documentación deja de ser relevante:

```
[...] el deber de conservación documental que le comuniqué en [FECHA ANTERIOR] queda
LIBERADO en cuanto a [tipo de documentación], al haberse [cerrado el asunto / ganado
firme / declarado la firmeza / vencido los plazos]. Puede aplicar a esos documentos
sus políticas habituales de conservación o destrucción, sin perjuicio de los plazos
legales generales que le sigan obligando (mercantil, tributario, laboral).
```

⚠️ **No liberar mientras quede plazo de apelación (15 días, art. 85.1 LJCA), de preparación de casación (30 días, art. 89.1 LJCA) o pendiente la ejecución** (arts. 103-113 LJCA). Comprobar antes de emitir.

### `--estado`

Mostrar tabla con los asuntos y el estado de conservación:

| Slug | Fecha emisión | Último refresh | ¿Historia clínica pedida? | ¿Expediente recibido? | Estado |
|---|---|---|---|---|---|
| .. | .. | .. | sí/no/N.A. | sí/no | activo / liberado |

## Flujo

### 1. Identificar qué tiene el cliente y qué tienen terceros

Vía `AskUserQuestion`:

- ¿Conserva la notificación de la resolución **y su acuse**? ¿Sabe la fecha exacta? **Si la respuesta es dudosa, es la máxima prioridad del asunto.**
- ¿Presentó alegaciones o recursos en vía administrativa? ¿Tiene el **justificante de registro**?
- ¿Hay informes periciales o técnicos? ¿En poder de quién?
- ¿Es un asunto **sanitario**? → historia clínica: ¿la ha pedido? ¿en qué centro? ¿fecha del alta? (para calcular el mínimo de 5 años del art. 17.1 Ley 41/2002)
- ¿Hay documentación en poder de terceros con plazo de purga corto (grabaciones, registros)?
- ¿En qué soporte está todo? ¿Quién tiene acceso?

### 2. Priorizar

1. **Acuse y fecha de la notificación** — determina el dies a quo y la viabilidad del recurso
2. **Documentación de terceros con plazo que corre** — historia clínica, grabaciones
3. **Justificantes de registro** de las alegaciones
4. Todo lo demás

### 3. Redactar la comunicación

Aplicar la plantilla con las categorías concretas del asunto. Suprimir los bloques que no apliquen (p. ej. el sanitario si no lo es); **nunca** suprimir el bloque 1.1.

### 4. Output

- Word `.docx` en `matters/<slug>/conservacion-v[N].docx`
- Actualizar `_log.yaml`: `conservacion_documental: emitida-AAAA-MM-DD`
- Apuntar el próximo refresh: al recibir el expediente administrativo, o en 90-180 días según la duración esperada

### 5. Recordatorio al cliente

Si Gmail MCP está disponible, crear un borrador con el texto y el Word adjunto, listo para que el usuario lo revise y lo envíe. **Nunca enviar automáticamente.**

## Reglas

1. **La prueba central es el expediente administrativo y lo tiene la Administración.** No pedir al cliente que reconstruya lo que el Juzgado va a reclamar de oficio (art. 48 LJCA). Enfocar en lo que solo él tiene y en lo que hay que pedir ya.
2. **El acuse de la notificación es el documento más importante del asunto.** Determina el dies a quo de un plazo de **caducidad**. Si el cliente no sabe la fecha exacta, tratarlo como urgencia del día.
3. **En sanitario, la historia clínica no la tiene el cliente: la tiene el centro**, con un mínimo legal de conservación de **5 años desde el alta** (art. 17.1 Ley 41/2002). El cliente tiene derecho a copia (art. 18). **Pedirla es más urgente que conservarla.**
4. **Datos de salud = categoría especial (art. 9 RGPD).** Tratamiento amparado en el art. 9.2.f (defensa de reclamaciones) y **solo para el pleito**. Canal seguro, minimización, y nada de datos de salud de **terceros** sin base jurídica (art. 18.3 Ley 41/2002 y `/revision-secreto-profesional`).
5. **LEC 217 y 328-329 son SUPLETORIOS** (DF 1.ª LJCA) y hay que decirlo cuando se citen. En materia de expediente la LJCA tiene régimen propio (art. 48) y no hay laguna. No presentar la carga de la prueba civil como si fuera la regla de este orden.
6. **No hay obligación legal genérica de "legal hold"** en España análoga a la anglosajona. La pérdida culposa de prueba en poder propio puede valorarse judicialmente en contra de quien debía custodiarla — enunciarlo así, **sin citar jurisprudencia concreta** y sin prometer un efecto automático.
7. **RGPD compatible.** La conservación con fines de defensa tiene base en el art. 6.1.c y 6.1.f RGPD, pero exige minimización y purga tras el litigio.
8. **Metadatos.** Críticos para la autenticidad: recordárselo siempre al cliente.
9. **Plazos legales de conservación** (mercantil, tributario, laboral) prevalecen sobre la liberación — apuntarlo en la comunicación.
10. **No liberar con plazos vivos** (apelación, casación, ejecución). Comprobar antes.
11. **Cero datos reales.** El modelo usa marcadores: `[CLIENTE]`, `[LETRADO]`, `[DOMICILIO]`, `[EXPEDIENTE]`, `[ÓRGANO]`. Los archivos se nombran por **slug**, sin el nombre del cliente.
12. **No inventar plazos ni artículos.** Lo que no esté en `references/anclas-normativas-ca.md` se verifica con `buscar_articulo` o se marca `[verificar]`.
