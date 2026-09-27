---
name: procedimiento-sancionador-ca
description: >-
  Catálogo (sin plantilla). Defensa en la fase ADMINISTRATIVA del procedimiento sancionador (arts. 25-31 Ley 40/2015 y arts. 53, 64, 77, 85, 89-90, 95-96 LPAC), antes de llegar al juzgado. Cubre caducidad, prescripción de infracciones y sanciones, atipicidad, culpabilidad, presunción de veracidad de las actas, defectos de notificación, pago voluntario con reducción y el recorrido alzada/reposición → contencioso. Activar con "expediente sancionador", "pliego de cargos", "alegaciones a la denuncia", "propuesta de resolución", "caducidad del expediente", "prescripción de la infracción", "boletín de denuncia", "me han multado", "denuncia de un agente", "pago con reducción", "pronto pago", "todavía estoy en vía administrativa". Requisito previo: la sanción sigue en tramitación administrativa o cabe recurso administrativo. Una vez agotada la vía y ya en sede judicial, el cauce es /procedimiento-abreviado-ca.
---

# Procedimiento sancionador y su impugnación contenciosa — catálogo (sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Principios de la potestad sancionadora** → `buscar_articulo` (`ley="LRJSP"`, artículos 25 a 31).
- **Caducidad, notificación y trámites** → `buscar_articulo` (`ley="LPAC"`, artículos 21, 25, 40 a 44, 64, 77, 85, 89, 90, 95 y 96).
- **Tipo previsto en una ordenanza** (terrazas, ruido, ZBE, residuos, animales) → `buscar_ordenanzas` + `leer_ordenanza` con `articulo` del precepto aplicado.
- **Régimen propio de tráfico** → `buscar_articulo` (`ley="Ley de Tráfico"` —RDL 6/2015—, artículos 94, 95 y 112).
- **Notificación edictal en el BOE (art. 44 LPAC)** → `novedades_boe` (órgano y referencia del expediente; periodo de hasta 31 días) + `leer_boe`.
- **Doctrina sobre tipicidad, presunción de veracidad de las actas y alcance del pago con reducción** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Alegaciones o recurso antes de presentar** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

Asiste en la defensa desde el acuerdo de iniciación hasta el recurso contencioso. **Verifica con
`buscar_articulo` todo precepto antes de citarlo**; los plazos de este documento están verificados
contra el BOE el **2026-07-17**, pero el régimen sectorial puede desplazarlos (ver § 7).

> ⛔ **Nada de MASC.** Es requisito del orden civil (LO 1/2025). Aquí el equivalente funcional es el
> **agotamiento de la vía administrativa** (art. 25.1 LJCA). No lo exijas ni bloquees escritos por él.

---

## 1. Los dos ejes de la defensa — comprobar SIEMPRE antes que el fondo

Antes de discutir si el cliente cometió o no la infracción, comprueba estas dos. Ganan más asuntos
que todos los motivos de fondo juntos y no exigen prueba, solo fechas del expediente.

### 1.1 Caducidad del procedimiento (art. 25.1.b) LPAC, con efectos del art. 95)

- El sancionador se inicia **de oficio** y es de gravamen: vencido el plazo máximo sin resolución
  **notificada**, **se produce la CADUCIDAD** — nunca silencio positivo (art. 25.1.b) LPAC).
- **Plazo máximo:** el que fije la norma reguladora (art. 21.2), que **no puede exceder de 6 meses**
  salvo norma con rango de ley o Derecho de la UE. **Si la norma sectorial no fija plazo: 3 meses**
  (art. 21.3). Se cuenta **desde la fecha del acuerdo de iniciación** (art. 21.3.a)).
- **A efectos de cumplir el plazo basta el intento de notificación debidamente acreditado**, si
  contiene el texto íntegro de la resolución (art. 40.4 LPAC). No regales caducidades que no lo son.
- **Se interrumpe** el cómputo si el procedimiento se paraliza por causa imputable al interesado
  (art. 25.2 LPAC). Revisa si la Administración imputa al cliente alguna paralización.
- **Efecto decisivo (art. 95.3 LPAC):** la caducidad no produce por sí sola la prescripción, **pero
  los procedimientos caducados NO interrumpen el plazo de prescripción**. Por eso las dos se
  alegan juntas y en este orden: caducado el expediente, la interrupción del art. 30.2 desaparece
  retroactivamente y la infracción suele resultar **prescrita**. Ésta es la jugada.
- La Administración puede reiniciar un procedimiento nuevo si la infracción no ha prescrito, e
  incorporar actos cuyo contenido se hubiera mantenido igual, pero **debe repetir alegaciones,
  proposición de prueba y audiencia** (art. 95.3, párr. 2.º).
- La caducidad **se declara de oficio o a solicitud de cualquier interesado**; pídela expresamente.

### 1.2 Prescripción de la infracción y de la sanción (art. 30 Ley 40/2015)

**Plazos supletorios — solo si la ley sectorial no fija los suyos (art. 30.1):**

| | Infracciones | Sanciones |
|---|---|---|
| Muy graves | **3 años** | **3 años** |
| Graves | **2 años** | **2 años** |
| Leves | **6 meses** | **1 año** |

> ⚠️ No son simétricos: la sanción **leve** prescribe al **año**, la infracción leve a los **6 meses**.
> Error frecuente. Y son **supletorios**: la ley sectorial gana (§ 7).

**Cómputo e interrupción — infracciones (art. 30.2):**
- Desde **el día en que la infracción se hubiera cometido**. En infracciones **continuadas o
  permanentes**, desde que **finalizó la conducta infractora**.
- Interrumpe la prescripción **la iniciación, con conocimiento del interesado**, de un procedimiento
  sancionador. Sin conocimiento del interesado no hay interrupción → conecta con § 4 (notificación).
- **Se REINICIA** (no se reanuda: vuelve a empezar de cero) el plazo si el expediente está
  **paralizado más de un mes** por causa no imputable al presunto responsable. Peina el expediente
  buscando huecos de más de un mes entre actuaciones.

**Cómputo e interrupción — sanciones (art. 30.3):**
- Desde **el día siguiente a aquel en que sea ejecutable la resolución** que impone la sanción **o
  haya transcurrido el plazo para recurrirla**.
- Interrumpe la iniciación, con conocimiento del interesado, del **procedimiento de ejecución**;
  vuelve a transcurrir si éste se paraliza más de un mes por causa no imputable al infractor.
- **Desestimación presunta de la alzada:** el plazo de prescripción de la sanción corre **desde el
  día siguiente a aquel en que finalice el plazo legal para resolver dicho recurso**. Regla muy
  rentable en expedientes dormidos: no espera a la resolución tardía.

**Cómo trabajarlo:** construye una tabla de fechas del expediente (comisión → iniciación →
notificación → cada actuación → propuesta → resolución → notificación) y marca (a) el día 0 de cada
plazo, (b) cada interrupción y si el interesado la conoció, (c) cada paralización > 1 mes. Usa la
skill `cronologia` si el expediente es voluminoso.

---

## 2. Motivos de fondo

Ordénalos por rendimiento, no por sistemática. Cada uno debe anclarse al folio del expediente.

- **Atipicidad (art. 27).** Solo son infracciones las previstas **por una Ley** (entidades locales:
  Título XI de la Ley 7/1985). El reglamento solo **especifica o gradúa**, sin crear infracciones ni
  sanciones nuevas ni alterar su naturaleza o límites (27.3). **No cabe aplicación analógica** (27.4):
  si la conducta no encaja **literalmente** en el tipo, no hay infracción.
- **Irretroactividad y retroactividad favorable (art. 26).** Rige la norma vigente al cometerse los
  hechos; la posterior **más favorable retroactúa** en tipificación, sanción **y plazos de
  prescripción**, incluso sobre sanciones **pendientes de cumplimiento**. Comprueba siempre si hubo
  reforma posterior favorable.
- **Ausencia de culpabilidad (art. 28.1).** Solo se sanciona a quien sea responsable **a título de
  dolo o culpa**: **no hay responsabilidad objetiva**. Trabaja diligencia empleada, error e
  imposibilidad de conocer el deber.
- **Error en la identificación del responsable (art. 28).** Sancionables: personas físicas y jurídicas
  y, cuando una ley les reconozca capacidad de obrar, grupos de afectados, uniones y entidades sin
  personalidad y patrimonios independientes. Solidaridad **solo** si la obligación legal corresponde
  **conjuntamente** a varios (28.3), individualizando la multa por grado de participación si es posible.
- **Falta de motivación (art. 35.1 LPAC).** Deben motivarse la **propuesta y la resolución**
  sancionadoras (35.1.h)), los actos que **rechazan pruebas** (35.1.f)) y los discrecionales (35.1.i)).
- **Desproporción (art. 29).** Idoneidad, necesidad y adecuación a la gravedad. Graduación (29.3):
  a) culpabilidad o intencionalidad; b) continuidad o persistencia; c) naturaleza de los perjuicios;
  d) **reincidencia** — más de una infracción de la misma naturaleza en el término de **un año**
  **declarada por resolución firme en vía administrativa** (sin firmeza no hay reincidencia: motivo
  puro). Pide el **grado inferior** (29.4). Si de una infracción deriva necesariamente otra, solo se
  impone la de la **más grave** (29.5).
- **Non bis in idem (art. 31.1).** No cabe sancionar hechos ya sancionados penal o administrativamente
  con **identidad de sujeto, hecho y fundamento**. Los **hechos probados por sentencia penal firme
  vinculan** a la Administración (art. 77.4 LPAC).
- **Presunción de inocencia y prueba insuficiente** (§ 3). **Defectos de notificación** (§ 4).

> **Derechos del presunto responsable — precisión.** El art. 53.2 LPAC reconoce **solo dos**:
> a) ser notificado de los hechos imputados, de las infracciones que puedan constituir, de las
> sanciones posibles, y de la identidad del instructor, de la autoridad competente para sancionar y
> de la norma que le atribuye la competencia; b) **presunción de no existencia de responsabilidad
> administrativa mientras no se demuestre lo contrario**. El **derecho a no declarar contra sí mismo**
> **no** figura en el art. 53.2 LPAC: invócalo por el **art. 24.2 CE** y la doctrina constitucional
> sobre su aplicación matizada al Derecho administrativo sancionador — **no lo cites como LPAC**.

---

## 3. Prueba y valor de las actas y denuncias de los agentes

- **Medios (art. 77.1):** cualquier medio admisible en Derecho; valoración conforme a la LEC.
  **Período de prueba (77.2):** **no superior a 30 días ni inferior a 10**; extraordinario a petición
  del interesado, **hasta 10 días**.
- **Rechazo de prueba (77.3):** solo si es **manifiestamente improcedente o innecesaria** y **mediante
  resolución motivada**. Un rechazo inmotivado o genérico es motivo de nulidad por indefensión: propón
  prueba SIEMPRE por escrito, aunque parezca inútil, para construir el motivo.
- **⚠️ Presunción de veracidad — art. 77.5 LPAC (éste es el apartado, no otro):** los documentos
  formalizados por **funcionarios a los que se reconoce la condición de autoridad**, en los que,
  **observándose los requisitos legales correspondientes**, se recojan **los hechos constatados** por
  aquéllos, **hacen prueba de éstos «salvo que se acredite lo contrario»**. Alcance real y ataques:
  1. Es **iuris tantum** — el propio texto admite prueba en contrario.
  2. Cubre **hechos constatados personalmente** por el agente, **no juicios de valor, deducciones,
     apreciaciones subjetivas ni calificaciones jurídicas**.
  3. Exige que se hayan **observado los requisitos legales** del documento: si al acta le falta un
     requisito reglamentario (identificación del agente, fecha, lugar, descripción del hecho, motivo
     de no entrega en el acto), **decae la presunción** y el hecho queda sin prueba.
  4. Exige la **condición de autoridad** del funcionario: compruébala; no todo denunciante la tiene
     (personal de control, vigilantes, empleados de concesionarias).
  5. No cubre lo que el agente **no pudo percibir directamente** ni lo que recoge por referencia.
- **Aparatos de medición** (cinemómetros, sonómetros, etilómetros): la presunción no sustituye la
  acreditación de **verificación/calibración vigente** conforme a su normativa metrológica. Pide el
  certificado en el expediente y alega su ausencia. **Verifica la norma metrológica aplicable con el
  usuario** — es en buena parte reglamentaria y sectorial.

---

## 4. Notificación — el punto débil habitual de la Administración

Determina el *dies a quo*, la interrupción de la prescripción y la caducidad. Audítala siempre.

- **Contenido y plazo (art. 40.2):** cursada en **10 días** desde que se dictó el acto; **texto
  íntegro**, si pone fin a la vía administrativa, **recursos** procedentes (administrativos y
  judiciales), órgano ante el que presentarlos y **plazo**.
- **⚠️ Notificación defectuosa (art. 40.3):** si contiene el texto íntegro pero omite los demás
  requisitos del 40.2, **surte efecto solo desde que el interesado realiza actuaciones que supongan
  el conocimiento del contenido y alcance del acto, o interpone cualquier recurso**. Una notificación
  **sin pie de recurso no abre el plazo** hasta ese momento: argumento central frente a la
  extemporaneidad. (A efectos de **caducidad**, en cambio, basta el intento acreditado con texto
  íntegro — art. 40.4.)
- **Papel (art. 42.2):** si no hay nadie, se hace constar día y hora y **se repite por una sola vez
  en hora distinta dentro de los 3 días siguientes**; si el 1.º fue **antes de las 15:00**, el 2.º
  **después de las 15:00** y viceversa, con **al menos 3 horas de diferencia**; si falla → art. 44.
  Puede recibirla cualquier persona **mayor de 14 años** que haga constar su identidad. **Comprueba
  las horas de ambos intentos en el acuse: incumplir la regla de las 15:00 / 3 horas invalida el
  edicto posterior.**
- **Electrónica (art. 43.2):** practicada **al acceder** a su contenido; si es obligatoria o elegida,
  se entiende **rechazada a los 10 días naturales** desde la puesta a disposición sin acceso. El
  **aviso** al móvil o correo **no invalida la notificación si falta** (art. 41.6) — no construyas
  ahí el motivo principal.
- **Edictal (art. 44):** desconocido, lugar ignorado o intento infructuoso → anuncio en el **BOE**
  (boletín autonómico, BOP o tablón son **facultativos y previos**, no sustituyen al BOE). Atácalo
  cuando la Administración **no agotó las averiguaciones razonables** de domicilio pudiendo hacerlo
  (art. 41.4: puede consultar el Padrón vía INE).
- **Rechazo expreso (art. 41.5):** se hace constar y el trámite se da por efectuado. **Doble cauce
  (art. 41.7):** vale la fecha de la notificación **producida en primer lugar**.

---

## 5. Recorrido procedimental y calendario

1. **Acuerdo de iniciación (art. 64 LPAC).** Contenido mínimo (art. 64.2): a) presuntos responsables;
   b) hechos, posible calificación y sanciones que pudieran corresponder; c) instructor y, en su
   caso, secretario, **con indicación del régimen de recusación**; d) órgano competente para resolver
   y norma que le atribuye la competencia, **con indicación de la posibilidad de reconocimiento
   voluntario de responsabilidad (art. 85)**; e) medidas provisionales; f) derecho a alegar y a la
   audiencia y plazos. **⚠️ Trampa del art. 64.2.f):** si **no se formulan alegaciones** en plazo, el
   acuerdo de iniciación **puede considerarse propuesta de resolución** cuando contenga un
   pronunciamiento preciso sobre la responsabilidad imputada — el expediente salta directo a la
   resolución y el cliente pierde el trámite intermedio. **Alega siempre, aunque sea someramente.**
   Si falta cualquier letra del 64.2, alégalo como indefensión.
   Excepcionalmente, sin elementos para calificar, cabe **Pliego de cargos** posterior (art. 64.3).
2. **Alegaciones y prueba** (§ 3). Propón prueba por escrito y pide expresamente el período del 77.2.
3. **Propuesta de resolución (art. 89).** Debe **notificarse**, indicar la puesta de manifiesto del
   expediente y el plazo para alegar (art. 89.2), y fijar **de forma motivada** hechos probados,
   calificación jurídica exacta, infracción, responsables, sanción propuesta, **valoración de las
   pruebas** —en especial las que fundamentan la decisión— y medidas provisionales (art. 89.3).
   **Archivo sin propuesta (art. 89.1):** el instructor debe archivar si a) los hechos no existieron;
   b) no resultan acreditados; c) no constituyen de modo manifiesto infracción; d) no hay o no se ha
   identificado responsable, o están exentos; **e) ha prescrito la infracción**. Pide el archivo por
   la letra que corresponda: es una petición reglada, no una gracia.
4. **Resolución (art. 90).** Incluye valoración de la prueba y fija hechos, responsables, infracción
   y sanción (90.1). **No puede aceptar hechos distintos** de los determinados en el procedimiento
   (90.2) — el cambio fáctico sorpresivo es motivo de nulidad. Si el órgano competente aprecia
   **mayor gravedad** que la propuesta, debe notificarlo para alegar en **15 días** (90.2).
   **Ejecutividad (90.3):** es ejecutiva cuando **no quepa contra ella recurso ordinario en vía
   administrativa**. **⚠️ Palanca infrautilizada:** siendo ejecutiva, **se suspende cautelarmente si
   el interesado manifiesta a la Administración su intención de interponer recurso
   contencioso-administrativo**; la suspensión dura hasta que transcurra el plazo sin interponerlo o
   hasta que el órgano judicial se pronuncie sobre la cautelar solicitada (y decae si al interponer
   **no se pide la suspensión cautelar** en el mismo trámite). **Presenta ese escrito y pide siempre
   la cautelar en la interposición** — ver skill `medidas-cautelares-ca`.
   Daños no cuantificados → procedimiento complementario (90.4).
5. **Tramitación simplificada (art. 96).** En sancionador **solo cabe si el órgano considera que hay
   elementos para calificar la infracción como LEVE**, y aquí el interesado **no puede oponerse**
   (art. 96.5). Plazo de resolución: **30 días** desde el siguiente a la notificación del acuerdo de
   tramitación simplificada (art. 96.6); alegaciones en **5 días** (96.6.c)); audiencia solo si la
   resolución va a ser desfavorable (96.6.d)). **Si se simplifica una infracción que no es leve,
   alega la infracción del 96.5**; y controla el plazo de 30 días para la caducidad.
6. **Recurso administrativo.** Comprueba en el pie de recurso y en la norma de competencia si la
   resolución **pone fin a la vía administrativa**:
   - **No la agota → ALZADA**, plazo **1 mes** (acto expreso). Es **preceptiva** para acceder al
     contencioso. Resolución en 3 meses; silencio **negativo**.
   - **La agota → REPOSICIÓN potestativa**, plazo **1 mes**. Resolución en 1 mes; silencio negativo.
   - Contra **acto presunto**: el recurso puede interponerse **«en cualquier momento»** (arts. 122.1
     y 124.1 Ley 39/2015). **Nunca cites el plazo de 3 meses**: era el art. 115.1 de la derogada
     Ley 30/1992. Ver `references/anclas-normativas-ca.md` § 2.4 y skill `recurso-alzada-reposicion-ca`.
7. **Recurso contencioso.** **2 meses** desde la notificación del acto expreso que pone fin a la vía;
   **6 meses** si es presunto (art. 46 LJCA). **Agosto no corre** (art. 128.2 LJCA). Casi siempre
   **procedimiento abreviado**: entra por **cuantía ≤ 30.000 €** (art. 78.1 LJCA) — ojo, **«tráfico»
   no es una materia del art. 78.1**; las multas de tráfico van por cuantía. Se inicia **por demanda**
   (skill `procedimiento-abreviado-ca`). **Advertencia al cliente:** con cuantía **≤ 30.000 €** la
   sentencia **no es apelable** (art. 81.1.a) LJCA): el abreviado es de instancia única.

---

## 6. ⚠️ Pago voluntario con reducción — explicárselo al cliente ANTES de que pague

Es la decisión irreversible más frecuente y la que más asuntos mata. **Régimen general, art. 85 LPAC:**

- **Reconocimiento de responsabilidad (85.1):** iniciado el procedimiento, si el infractor reconoce
  su responsabilidad, **se podrá resolver con la imposición de la sanción que proceda**.
- **Pago voluntario (85.2):** cuando la sanción sea **únicamente pecuniaria** —o quepa una pecuniaria
  y otra no pecuniaria pero se haya justificado la improcedencia de la segunda—, el pago **en
  cualquier momento anterior a la resolución** implica la **terminación del procedimiento**, salvo en
  lo relativo a la **reposición de la situación alterada** y a la **indemnización de daños y
  perjuicios** (que siguen exigiéndose aparte: adviértelo, el cliente cree que paga y se acabó).
- **Reducciones (85.3):** cuando la sanción sea únicamente pecuniaria, el órgano aplicará reducciones
  **de, AL MENOS, el 20 %** sobre el importe de la **sanción propuesta**, **acumulables entre sí**
  (reconocimiento + pago → mínimo 20 % + 20 %). Requisitos y efectos, literales:
  - **Deben estar determinadas en la notificación de iniciación del procedimiento.** Si el acuerdo
    de iniciación **no las informó**, la reducción aplicada o el ofrecimiento son irregulares →
    motivo de impugnación.
  - Su **efectividad está condicionada al desistimiento o renuncia de cualquier acción o recurso
    EN VÍA ADMINISTRATIVA contra la sanción**.
  - El porcentaje **puede incrementarse reglamentariamente** (por eso hay sectores con 50 %).
- **Cómo asesorar, con precisión:** el art. 85.3 condiciona la reducción, **por su literalidad**, a la
  renuncia a acciones y recursos **en vía administrativa**. **No digas al cliente que el pago cierra
  automáticamente el recurso contencioso** ni lo contrario: la cuestión del alcance de esa renuncia
  sobre la vía judicial es **jurisprudencial y debe verificarse con `buscar_sentencias`/`buscar_por_cita`
  antes de afirmar nada** `[verificar]`. Lo que sí es seguro y debe decírsele por escrito:
  1. Pagando **renuncia a los recursos administrativos** y el procedimiento **termina**;
  2. renuncia a que se practique la prueba y a discutir los hechos;
  3. la **reposición** y la **indemnización de daños** siguen siendo exigibles;
  4. la sanción **computa a efectos de reincidencia** (art. 29.3.d)) salvo regla sectorial en contra;
  5. si hay **caducidad o prescripción** apreciables (§ 1), pagar es regalar un asunto ganado —
     **comprueba § 1 antes de recomendar el pago**.
- Deja constancia de la advertencia y de la decisión del cliente. Usa marcadores `[CLIENTE]`,
  `[FECHA]`, `[IMPORTE]` en cualquier borrador o nota.

---

## 7. ⚠️ Normativa sectorial — desplaza al régimen general. NO apliques el general sin comprobarlo

Los arts. 30 Ley 40/2015 y 21 LPAC son **supletorios**. Antes de calcular un solo plazo:
**pide al usuario la norma sectorial aplicable y verifícala con `buscar_articulo`.**

**Tráfico — RDL 6/2015, texto refundido de la Ley de Tráfico (verificado 2026-07-17). Todo distinto:**

| | Régimen general | **Tráfico (RDL 6/2015)** |
|---|---|---|
| Prescripción infracción leve | 6 meses | **3 meses** (art. 112.1) |
| Prescripción infracción grave / muy grave | 2 años / 3 años | **6 meses ambas** (art. 112.1) |
| Prescripción sanción de multa | 2-3 años / 1 año leves | **4 años** (art. 112.4) |
| Prescripción suspensión del permiso (art. 80) | — | **1 año** (art. 112.4) |
| Caducidad del procedimiento | 3-6 meses (arts. 21, 25 LPAC) | **1 año** desde la iniciación (art. 112.3) |
| Reducción por pago voluntario | ≥ 20 % + 20 % (art. 85.3 LPAC) | **50 %** (art. 94.a)) |
| Plazo de alegaciones | el del acuerdo | **20 días naturales** (art. 95.1) |

- **Prescripción en tráfico (art. 112):** el plazo corre **desde el mismo día** de comisión. Interrumpe
  cualquier actuación administrativa **conocida por el denunciado** o encaminada a averiguar su
  identidad o domicilio practicada con otras administraciones u organismos, y la notificación ex
  arts. 89-91. **Se reanuda** si el procedimiento se paraliza más de **un mes** por causa no imputable
  al denunciado. Las sanciones de multa corren **desde el día siguiente a la firmeza en vía
  administrativa**; su exacción en apremio se rige por la **normativa tributaria**.
- **Caducidad en tráfico (art. 112.3):** **1 año** desde la iniciación, a instancia de cualquier
  interesado o de oficio. Se **suspende** mientras los hechos estén en la jurisdicción penal y se
  **reanuda** por el tiempo restante al ganar firmeza la resolución judicial.
- **Pago voluntario en tráfico (art. 94):** en el acto de entrega de la denuncia o en **20 días
  naturales** desde el día siguiente a su notificación → a) **reducción del 50 %**; b) **renuncia a
  formular alegaciones** (si se formulan, se tienen por no presentadas); c) terminación **sin
  resolución expresa** el día del pago; d) **agotamiento de la vía administrativa, siendo recurrible
  únicamente ante el orden contencioso-administrativo**; e) el plazo del contencioso corre **desde el
  día siguiente al pago**; f) firmeza desde el pago; g) **no computa como antecedente** en el Registro
  de Conductores e Infractores si es **grave sin pérdida de puntos**. **Diferencia clave con el
  art. 85 LPAC:** aquí la ley dice expresamente que el acto **sigue siendo recurrible en vía
  contenciosa** — pero sin alegaciones ni prueba, el recurso queda reducido a caducidad, prescripción,
  incompetencia, atipicidad manifiesta o defectos de notificación.
- **Denuncia como acto resolutorio (art. 95.4):** si el denunciado **ni alega ni paga en 20 días
  naturales**, la denuncia surte **efecto de resolución** en: a) leves siempre; b) graves sin
  detracción de puntos no notificadas en el acto; c) graves y muy graves notificadas en el acto. La
  sanción se ejecuta a los **30 días naturales** desde la notificación de la denuncia y **pone fin a
  la vía administrativa** (95.5). **El silencio del cliente le cierra la vía administrativa: avísale.**
  Si hay alegaciones con datos nuevos, se da traslado al agente para informe en **15 días naturales**
  (95.2); solo se traslada la propuesta si hay hechos o pruebas distintos de los aducidos (95.3).

**Otros sectores — instrucciones:**
- **Consumo, actividades, disciplina urbanística, medio ambiente, ruido, animales, terrazas, tributos
  locales:** son en gran medida **autonómicos y locales**.
- ⚠️ **El conector NO cubre normativa autonómica ni los BOP.** Sí cubre **BOE estatal** y
  **ordenanzas municipales** de los municipios cubiertos (`buscar_ordenanzas` / `leer_ordenanza`).
  **Pide la norma autonómica al usuario y NO la cites de memoria.** Si no la aportan, dilo y marca
  `[verificar]` cada plazo dependiente de ella. Nunca apliques el plazo supletorio del art. 30
  Ley 40/2015 sin haber comprobado que la sectorial no fija otro.
- **Régimen disciplinario del personal al servicio de las AAPP:** el capítulo sancionador de la
  Ley 40/2015 **le es extensivo** (art. 25.3), pero **no** se aplica a la potestad sancionadora
  respecto de vinculados por **contratos del sector público** ni por la **legislación patrimonial**
  (art. 25.4). Compruébalo antes de encajar el asunto.

---

## 8. Salidas y entregables

- **Escritos:** alegaciones al acuerdo de iniciación; alegaciones a la propuesta de resolución;
  solicitud de archivo por prescripción (art. 89.1.e)); solicitud de declaración de caducidad;
  recurso de alzada o reposición (skill `recurso-alzada-reposicion-ca`); escrito de manifestación de
  intención de recurrir en vía contenciosa a efectos del art. 90.3 LPAC; demanda de abreviado
  (skill `procedimiento-abreviado-ca`); solicitud de medida cautelar (skill `medidas-cautelares-ca`).
- **Estilo:** skill `estilo-escritos-judiciales`. **Entrega:** Word `.docx` maquetado (skill `docx`).
- **Jurisprudencia:** **prohibido** citar ECLI, ROJ, fecha o ponente de memoria. Verifica con
  `buscar_sentencias` / `buscar_por_cita` (Sala Tercera del TS, TSJ) antes de citar. Si no puedes
  verificar, escribe `[verificar]` y dilo abiertamente.
- **Datos personales:** cero datos reales en ejemplos y borradores. Usa `[CLIENTE]`, `[ÓRGANO]`,
  `[FECHA]`, `[IMPORTE]`, `[EXPEDIENTE]`, `[MATRÍCULA]`. **En tráfico, nunca matrículas, DNI ni
  números de permiso reales.** Ver `PROTECCION-DATOS.md`.
- **Perfil del despacho:** `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/`.
