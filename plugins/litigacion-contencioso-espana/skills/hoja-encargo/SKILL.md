---
name: hoja-encargo
description: Hoja de encargo profesional para asuntos contencioso-administrativos conforme al EGA, Ley 10/2010 PBC y RGPD. Genera Word maquetado con datos del letrado, objeto del encargo en terminos contenciosos (recurso contra resolucion administrativa), honorarios, advertencia de costas del art. 139 LJCA con el tope del tercio, advertencia de plazos de caducidad, clausula RGPD y secreto profesional. Usar con redactar hoja de encargo, contrato de servicios juridicos, aceptar nuevo asunto o documentar el encargo del cliente.
---

# Hoja de encargo profesional — contencioso-administrativo

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Advertencias obligatorias** (caducidad, vía previa, costas y jura de cuentas) → `buscar_articulo` (`ley="LJCA"`, artículos 25, 46 y 139; `ley="LEC"`, `articulo="35"`).
- **Deberes de información y honorarios del Estatuto General de la Abogacía** → `buscar_boe` + `leer_boe` (RD 135/2021) antes de citar sus artículos.
- **Cliente persona jurídica** → `buscar_empresa_mercantil` (denominación o CIF: domicilio, administradores y apoderados inscritos) para completar el representante y anticipar el acuerdo corporativo del art. 45.2.d) LJCA.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

---

Documento contractual entre letrado y cliente que formaliza el encargo y blinda al despacho frente a impagos, reclamaciones por costas inesperadas o impugnaciones de minuta.

> ⚠️ **El objeto del encargo es siempre contencioso-administrativo.** No describir el encargo como demanda civil, reclamación de cantidad, desahucio ni monitorio. El contrato en sí (arrendamiento de servicios entre letrado y cliente) es de naturaleza civil — de ahí que sigan aplicándose LEC 35 y la cláusula de jurisdicción —, pero **el asunto encargado es un recurso contencioso-administrativo**.

## Marco legal

- **Estatuto General de la Abogacía (RD 135/2021)**
  - **art. 27** — encargo profesional: antes de iniciar la actuación se informa al cliente conforme al art. 48, **preferentemente mediante hoja de encargo**.
  - **art. 48.3** — deber de informar sobre la **viabilidad** del asunto y de disuadir de acciones sin fundamento.
  - **art. 48.4** — deber de informar sobre honorarios y costes **y de hacer saber las consecuencias que puede tener una condena en costas y su cuantía aproximada**. Es la base directa del bloque de advertencias.
  - **art. 25** — derecho a contraprestación y al reintegro de gastos.
  - **art. 26** — **libre fijación de honorarios**, convenidos libremente entre cliente y letrado con respeto a las normas deontológicas y de defensa de la competencia.
  - **art. 28** — obligación de entregar **factura** detallada por conceptos y gastos.
- **LEC 35** — reclamación de honorarios al cliente (jura de cuentas). Aplica al abogado con independencia del orden en que se devengaran; en contencioso, por la vía supletoria de la **DF 1.ª LJCA**.
  - **LEC 35.4** — si la reclamación se dirige contra una **persona física**, el abogado **debe aportar el contrato suscrito con el cliente**, y el juez examina **de oficio** el posible carácter **abusivo** de las cláusulas. **Sin hoja de encargo firmada, la jura de cuentas contra un particular se debilita gravemente.**
- **Art. 139 LJCA** — régimen de costas del orden contencioso, con el **tope del tercio** del art. 139.4 (redacción del RD-ley 6/2023).
- **Art. 46 LJCA** — plazos de interposición, de naturaleza de **caducidad**.
- **Art. 25.1 LJCA** — objeto del recurso: actos que **ponen fin a la vía administrativa** (agotamiento de la vía).
- **Art. 542.3 LOPJ** — secreto profesional.
- **Ley 10/2010** de prevención del blanqueo de capitales — sujeción del abogado en determinadas actividades; información obligatoria al cliente.
- **Reglamento (UE) 2016/679 (RGPD) + LO 3/2018 (LOPDGDD)** — base jurídica del tratamiento, plazos de conservación, derechos del interesado.
- **Código Deontológico de la Abogacía** — información previa, honorarios, conflicto de intereses.

> ⛔ **NO existe requisito de MASC en este encargo.** El intento de MASC de la LO 1/2025 es requisito de procedibilidad del orden **civil** (LEC) y **no se aplica** en contencioso-administrativo. **No incluir ninguna cláusula, advertencia ni casilla de MASC.** Lo que sí debe advertirse es el **agotamiento de la vía administrativa** y los **plazos de caducidad** (ver § 5).

## Cuándo activar

- "Redacta una hoja de encargo para [CLIENTE]"
- "Saca contrato de servicios para el asunto [X]"
- "Documento de aceptación del encargo"
- Tras intake del asunto (`asunto-intake`), antes de iniciar trabajo facturable
- Cuando se acepta un asunto nuevo sin documento previo de provisión o presupuesto cerrado

## Flujo — siete fases

### 1. Datos del despacho (auto-rellenar desde el perfil)

Leer de `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/CLAUDE.md`, sección `## Identidad del despacho`:

- Nombre del letrado / despacho → `[LETRADO]`
- Colegio profesional + nº de colegiado
- Domicilio profesional
- Correo y teléfono de contacto
- NIF del despacho (exigido por el art. 48.1 EGA)
- Logo: `[logo del despacho, si se aporta]`

Si algún campo aparece como `[PLACEHOLDER]` o `[PENDIENTE]`, parar y pedir **solo ese dato** (no re-lanzar el cold-start completo).

### 2. Datos del cliente — batería mínima

Mediante `AskUserQuestion` (datos que NO se inventan). En el documento se vuelcan como marcadores hasta que el usuario los facilite:

- Nombre completo o razón social → `[CLIENTE]`
- DNI / NIE / CIF → `[DNI]`
- Domicilio → `[DOMICILIO]`
- Teléfono y correo → `[TELEFONO]`, `[EMAIL]`
- Si es persona jurídica: representante legal y cargo → `[REPRESENTANTE]`, `[CARGO]`
- Titularidad: por sí mismo / como representante / como administrador

> ⚠️ **Persona jurídica — comprobación crítica.** Si el cliente es persona jurídica, advertir ya en el encargo de que el art. 45.2.d) LJCA exige aportar el **documento que acredite el cumplimiento de los requisitos para entablar acciones** según sus estatutos (el «acuerdo corporativo»), **además** del poder. Es la causa de inadmisión más frecuente y evitable. Dejar constancia de quién lo aporta y cuándo.

### 3. Objeto del encargo — en términos contenciosos

Batería de preguntas:

- **Acto o disposición que se impugna:** órgano autor, fecha de la resolución, nº de expediente administrativo, fecha de **notificación** (¡es el dies a quo!)
- **Vía administrativa:** ¿está agotada? ¿queda alzada o reposición pendiente? ¿es acto expreso o presunto?
- **Órgano judicial competente**
- **Alcance del encargo** — marcar expresamente lo que se incluye y lo que no:
  - Vía administrativa previa (recurso de alzada o de reposición)
  - Interposición del recurso contencioso-administrativo y demanda — **primera o única instancia**
  - Pieza de **medidas cautelares** (arts. 129-136 LJCA)
  - **Recurso de apelación** (art. 85 LJCA)
  - **Recurso de casación** (arts. 88-89 LJCA)
  - **Ejecución** de sentencia (arts. 103-113 LJCA)
  - Solo asesoramiento / dictamen de viabilidad

Fórmula de redacción del objeto en el documento:

```
OBJETO DEL ENCARGO

El cliente encarga a [LETRADO] la dirección letrada del recurso
contencioso-administrativo contra la resolución de [ÓRGANO] de fecha [FECHA],
dictada en el expediente administrativo nº [EXPEDIENTE] y notificada al cliente el
[FECHA NOTIFICACIÓN], ante el Juzgado de lo Contencioso-Administrativo nº [X] de
[LUGAR].

Alcance: [primera o única instancia] / [incluye pieza de medidas cautelares] /
[incluye recurso de apelación] / [incluye ejecución].

Queda EXPRESAMENTE EXCLUIDO del presente encargo: [fases no incluidas]. Su eventual
tramitación requerirá nuevo encargo y devengará honorarios independientes.
```

Variantes del órgano según el asunto: `Sala de lo Contencioso-Administrativo del Tribunal Superior de Justicia de [CCAA]`, `Audiencia Nacional, Sala de lo Contencioso-Administrativo`, `Tribunal Supremo, Sala Tercera`.

> Si el alcance no incluye una fase posterior, dejarlo explícito. Evita la discusión futura sobre la extensión del encargo, que en contencioso es especialmente frecuente porque la apelación y la casación tienen plazos propios y muy cortos.

### 4. Honorarios — modalidad

`AskUserQuestion` con las modalidades:

1. **Presupuesto cerrado** — cantidad fija acordada
2. **Por hora** — tarifa horaria con estimación
3. **Criterios orientadores del Colegio** — minuta conforme a los criterios del colegio correspondiente
4. **Con componente de éxito** — los honorarios se fijan **libremente** entre cliente y letrado (**art. 26 EGA**), con respeto a las normas deontológicas y de defensa de la competencia. Si se pacta un componente variable por resultado, **documentarlo con precisión**: base de cálculo, hecho que lo devenga y momento de pago. `[verificar]` los límites deontológicos concretos que aplique el colegio del letrado antes de cerrar la cláusula.

Para cada modalidad, capturar:

- Cantidad o tarifa
- IVA (21% salvo exención aplicable)
- Provisión de fondos (si procede): cuantía, momento, justificación
- Forma de pago: transferencia bancaria al IBAN del despacho → **`[IBAN]`** (marcador; sustituir solo cuando el letrado facilite el número — **no inventar**)
- Devengos parciales: qué se cobra si el cliente incumple, **desiste** (art. 74 LJCA) o el recurso termina por **satisfacción extraprocesal** (art. 76 LJCA) o **allanamiento** de la Administración (art. 75 LJCA)
- **Honorarios del procurador** — no incluidos en los del abogado, cobertura aparte. Explicar en el documento que el procurador es **potestativo ante los Juzgados de lo Contencioso-Administrativo** y **preceptivo ante las Salas** (TSJ, Audiencia Nacional y Tribunal Supremo) — **art. 23 LJCA**. Si el asunto puede llegar a apelación o casación, el coste de procurador aparecerá aunque en primera instancia no lo hubiera.
- Periciales (médico, arquitecto/urbanista, tasador), tasas, gastos de copias del expediente: a cargo del cliente

### 5. Advertencias obligatorias

Bloque destacado en el documento. NO se elimina ni se suaviza:

1. **Plazos de caducidad — advertencia PRIMERA y más importante.**
   > Los plazos para recurrir en vía contencioso-administrativa son de **CADUCIDAD**, no de prescripción: **no se interrumpen** por reclamaciones extrajudiciales, burofaxes, requerimientos ni negociaciones con la Administración. Transcurrido el plazo, el acto deviene **firme y consentido** y el recurso será **inadmitido** (art. 69.e LJCA), sin entrar en el fondo.
   >
   > **La firma tardía de esta hoja de encargo puede hacer perder la acción.** El cliente reconoce haber sido informado de que el plazo corre desde la notificación del acto y de que el letrado **no puede garantizar la viabilidad del recurso si el encargo se formaliza con el plazo próximo a vencer o ya vencido**. Se hace constar la fecha de notificación declarada por el cliente: **[FECHA NOTIFICACIÓN]**, y la fecha límite calculada: **[FECHA LÍMITE]**.

   Al rellenar, apoyarse en `references/anclas-normativas-ca.md` § 2 y recordar el art. 128.2 LJCA: **agosto no corre** para los plazos de la LJCA, **salvo en el procedimiento de derechos fundamentales**, donde agosto **sí es hábil**.

2. **Agotamiento de la vía administrativa.**
   > Solo son recurribles ante la jurisdicción contencioso-administrativa los actos que **ponen fin a la vía administrativa** (art. 25.1 LJCA). Si el acto no la agota, deberá interponerse previamente el recurso administrativo procedente (alzada o reposición), **cuya tramitación forma o no parte del presente encargo según el alcance pactado en la cláusula de Objeto**. El cliente queda informado de que interponer el recurso contencioso sin agotar la vía puede determinar su inadmisión.

3. **Costas procesales — art. 139 LJCA** (advertencia exigida por el art. 48.4 EGA):
   > En **primera o única instancia** rige el criterio de **vencimiento objetivo**: se imponen las costas a la parte que vea **rechazadas todas** sus pretensiones, salvo que el órgano aprecie **y razone** que el caso presentaba serias dudas de hecho o de derecho. Si la estimación o desestimación es **parcial**, cada parte abona las suyas y las comunes por mitad, salvo temeridad o mala fe razonada. En **recursos**, se imponen al recurrente si se desestima **totalmente**.
   >
   > **Límite legal (art. 139.4 LJCA, redacción del RD-ley 6/2023):** la parte condenada en costas en primera o única instancia **no abonará más de un tercio (1/3) de la cuantía del proceso por cada uno de los favorecidos por la condena**. A estos **solos efectos**, los pleitos de **cuantía indeterminada se valoran en 18.000 €**, salvo que el órgano razone otra cosa atendiendo a la complejidad del asunto. En los recursos, la imposición puede ser total, parcial o hasta una cifra máxima.
   >
   > Estimación aproximada de la exposición del cliente en este asunto: cuantía del proceso **[CUANTÍA]** → tope orientativo **[CUANTÍA ÷ 3]** por cada favorecido. **Es una estimación, no una garantía.**
   >
   > Las costas del propio cliente corren a su cargo hasta la tasación. La tasación se practica conforme a la **LEC** (art. 139.7 LJCA). Frente a particulares, las costas se exigen por **vía de apremio** (art. 139.5 LJCA).

4. **Resultado incierto.** La acción puede resultar infructuosa por razones ajenas a la diligencia del letrado (criterio jurisprudencial, prueba practicada, valoración judicial, contenido del expediente administrativo). Conforme al art. 48.3 EGA, el letrado ha informado al cliente sobre la viabilidad del asunto.

5. **El expediente administrativo lo tiene la Administración.** El cliente queda informado de que la prueba central del proceso es el **expediente administrativo**, que se reclama de oficio a la Administración demandada (art. 48 LJCA) y que el despacho **no controla ni su contenido ni su plazo de remisión**. La estrategia puede variar sustancialmente al recibirlo.

6. **Ley 10/2010 PBC.** Obligación del letrado de comunicar al SEPBLAC operaciones sospechosas en los supuestos legalmente previstos; información al cliente sobre el tratamiento de datos a estos efectos.

7. **Delegación en colaboradores.** Posibilidad de que el letrado se apoye en otros profesionales del despacho o colaboradores externos (procurador, peritos) sin incremento de honorarios del abogado para el cliente.

8. **Renuncia y revocación.** Derecho del cliente a revocar el encargo en cualquier momento; los honorarios devengados hasta la revocación siguen siendo exigibles. Derecho del letrado a cesar en la defensa conforme a las normas deontológicas aplicables `[verificar artículo concreto del EGA / Código Deontológico antes de citarlo]`, con **preaviso suficiente para no causar indefensión**, lo que en contencioso es especialmente crítico por la brevedad de los plazos.

### 6. Protección de datos — cláusula RGPD + LO 3/2018 (obligatoria)

Bloque RGPD, no suprimible:

- **Responsable:** `[LETRADO]` / `[DESPACHO]`, NIF `[NIF]`, domicilio `[DOMICILIO PROFESIONAL]`, contacto `[EMAIL]`
- **Finalidad:** prestación de los servicios jurídicos contratados y su facturación
- **Base jurídica:** ejecución del contrato (art. 6.1.b RGPD) + cumplimiento de obligaciones legales (art. 6.1.c: EGA, Ley 10/2010, normativa fiscal) + interés legítimo en la defensa de los propios derechos (art. 6.1.f)
- **Categorías especiales (art. 9 RGPD):** si el asunto implica **datos de salud** (responsabilidad patrimonial sanitaria, incapacidades, historia clínica), datos de infracciones o cualquier otra categoría especial, hacerlo constar y fundar el tratamiento en el **art. 9.2.f RGPD** (formulación, ejercicio o defensa de reclamaciones). **Recabar consentimiento explícito para la historia clínica cuando proceda.**
- **Plazo de conservación:** durante la relación profesional y, después, durante los plazos legales de conservación aplicables (fiscal, y los reforzados de la Ley 10/2010 en su caso)
- **Cesiones:** al órgano judicial, a la Administración demandada, al procurador y a los peritos, en el marco estricto del procedimiento. **Cesión a un tercero fuera de ese marco: nunca sin base jurídica.**
- **Datos de terceros:** si el cliente aporta datos de terceras personas, garantiza que está legitimado para comunicarlos. El expediente administrativo puede contener datos de otros interesados: ver `/revision-secreto-profesional`.
- **Derechos:** acceso, rectificación, supresión, oposición, limitación y portabilidad, ejercitables ante el despacho, y derecho a reclamar ante la **AEPD**

### 7. Secreto profesional — cláusula (obligatoria)

> **Art. 542.3 LOPJ.** El letrado guardará secreto de todos los hechos o noticias que conozca por razón de cualquiera de las modalidades de su actuación profesional, y **no podrá ser obligado a declarar sobre ellos**. El deber persiste tras la finalización del encargo y no decae por la revocación. Las únicas excepciones son las legalmente tasadas (Ley 10/2010 PBC/FT y autorización judicial específica en los supuestos previstos).
>
> **El secreto pertenece al cliente**: solo él puede relevar de él al letrado, y el letrado no puede renunciar a él por su cuenta.

### 8. Jurisdicción y firma

- Sometimiento a los **Tribunales del orden civil** del domicilio del despacho para cualquier controversia **derivada del propio contrato de encargo** (no del asunto encargado, que es contencioso-administrativo). Cláusula válida entre empresarios; si el cliente es **consumidor** (persona física no profesional), **manda el fuero del domicilio del consumidor** y la cláusula no puede privarle de él.
- Doble firma: letrado + cliente, con DNI debajo → `[LETRADO]` / `[DNI LETRADO]` y `[CLIENTE]` / `[DNI]`
- Fecha y lugar

## Maquetación del Word

**Diseño corporativo del despacho:**

- Logo: `[logo del despacho]` (cabecera, columna izquierda) — opcional, si se aporta
- Paleta (DEFAULT — ajustar a los colores de marca del despacho cuando se definan):
  - Color de títulos `#B8860B`
  - Fondo suave `#F5EBD7`
  - Gris oscuro texto `#333333`
  - Gris medio secundario `#666666`
- Fuente: Arial 11 cuerpo, 12 títulos
- Página: A4, márgenes 2 cm
- Cabecera: tabla de 2 columnas sin bordes (logo + título "HOJA DE ENCARGO PROFESIONAL")
- Campos: tablas con borde gris claro 1 pt
- **Bloque de advertencias:** cuadro con fondo dorado claro y borde dorado a la izquierda de 3 pt. La advertencia de **plazos de caducidad** va la primera y en **negrita**.
- Firmas: tabla de 2 columnas, altura fija 5 cm para la firma manuscrita
- Pie: nº de página + dominio del despacho

**Generación:**

- Librería: `docx` (Node.js) o `python-docx` (Python)
- Logo cargado desde `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/brand/logo-despacho.jpg` (si se aporta)
- Si el logo no existe en esa ruta, fallback a cabecera de texto plano y flag en la nota del revisor

## Salida

- `matters/<slug-asunto>/hoja-encargo/hoja-encargo-v1.docx` cuando el workspace de asunto esté habilitado
- En su defecto, `outputs/hoja-encargo-[slug-asunto]-[YYYY-MM-DD].docx`
- **El slug NO debe contener el nombre del cliente** si el repositorio se comparte o sincroniza. Usar `descriptor-materia-año`.
- La cabecera interna RESERVADO Y CONFIDENCIAL **no** se aplica: la hoja de encargo es un documento que sale al cliente, no interno
- Nota del revisor en mensaje separado con el checklist pre-firma:
  - [ ] Fecha de notificación del acto confirmada documentalmente (acuse, sello de registro), no solo de memoria del cliente
  - [ ] Fecha límite de interposición calculada y contrastada con `references/anclas-normativas-ca.md`
  - [ ] ¿Está agotada la vía administrativa? Si no, ¿el alcance cubre el recurso previo?
  - [ ] Si el cliente es persona jurídica: acuerdo corporativo del art. 45.2.d) LJCA identificado
  - [ ] Órgano judicial competente confirmado (art. 8 LJCA)
  - [ ] ¿Requiere procurador? (preceptivo solo ante Salas — art. 23 LJCA)
  - [ ] Cuantía del proceso fijada y tope de costas del tercio calculado
  - [ ] `[IBAN]` sustituido por el real antes de enviar
  - [ ] Todos los marcadores `[...]` sustituidos

## Reglas

1. **Sin hoja de encargo firmada no se inicia trabajo facturable.** Excepción real y frecuente en contencioso: si el plazo de caducidad está a punto de vencer, **el plazo manda**. Dejar constancia por correo del encargo verbal, presentar en plazo y formalizar la firma en paralelo — pero nunca dejar caducar la acción esperando una firma.
2. **Cero datos reales en el modelo.** Todo dato personal va como marcador: `[CLIENTE]`, `[DNI]`, `[DOMICILIO]`, `[IBAN]`, `[LETRADO]`. El modelo que vive en la skill **jamás** contiene datos reales; se sustituyen solo en el `.docx` generado para ese asunto.
3. **Honorarios libremente convenidos** (art. 26 EGA), con respeto a las normas deontológicas y de competencia. No afirmar prohibiciones deontológicas concretas sin verificarlas: marcar `[verificar]`.
4. **Consumidor vs empresario.** Si el cliente es persona física no profesional, la cláusula de jurisdicción no puede privarle de su fuero natural. Recordar además el control de oficio de abusividad del **art. 35.4 LEC** en una eventual jura de cuentas: una cláusula desequilibrada puede tumbar el cobro.
5. **Provisión de fondos en blanqueo.** Si el asunto cae en un supuesto de la Ley 10/2010, provisión obligatoria con identificación reforzada del cliente.
6. **NUNCA incluir MASC.** Si una plantilla heredada o el usuario lo mencionan, explicar que es requisito del orden civil y que no aplica aquí; sustituir por el bloque de agotamiento de la vía administrativa.
7. **NUNCA prometer resultado ni plazo de resolución.** El expediente y los tiempos de la Administración no dependen del despacho.
8. **Asunto en cartera.** Tras generar la hoja, ofrecer `/asunto-intake` si no se ha hecho — la hoja firmada es el detonante natural de creación de asunto.
9. **Aplicar el estilo de la casa.** Pasada final con `estilo-escritos-judiciales` para el lenguaje (no para la estructura, que es la del modelo).
10. **Plazos y cifras:** ninguno que no esté en `references/anclas-normativas-ca.md` o verificado en el momento con `buscar_articulo`. En su defecto, `[verificar]`.

## Handoffs

- Tras la firma, si el workspace de asunto no se ha creado: ofrecer `/asunto-intake`
- Si la vía administrativa no está agotada y el alcance la cubre: `/recurso-alzada-reposicion-ca`
- Si la vía está agotada y el plazo corre: `/interposicion-recurso-contencioso-ca` — **prioridad sobre todo lo demás**
- Si hay riesgo de ejecución del acto durante el proceso: `/medidas-cautelares-ca`
- Si el cliente impaga: el documento firmado es la base de la jura de cuentas del art. 35 LEC — y con persona física, **es requisito de aportación** (art. 35.4 LEC)
- Si el asunto avanza a una fase excluida del alcance (apelación, casación, ejecución): confirmar por correo la ampliación del encargo **antes** de que corra el plazo de esa fase, que es breve (15 días apelación, art. 85.1 LJCA; 30 días preparación de casación, art. 89.1 LJCA)
