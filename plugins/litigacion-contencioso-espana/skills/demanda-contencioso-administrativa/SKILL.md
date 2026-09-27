---
name: demanda-contencioso-administrativa
description: >-
  Redacta la demanda contencioso-administrativa del procedimiento ordinario (arts. 52-56 LJCA), en el trámite posterior a la entrega del expediente administrativo — hechos anclados al expediente, motivos de nulidad y anulabilidad, cuantía, prueba y suplico del art. 31. Activar con "formalizar la demanda del contencioso", "ya tengo el expediente y toca demandar", "art. 56 LJCA", "redactar la demanda tras el emplazamiento". Requisito previo: el recurso YA está interpuesto y el expediente entregado. Si aún no se ha presentado nada, empezar por /interposicion-recurso-contencioso-ca. Si el asunto va por procedimiento abreviado (materias del art. 78.1 LJCA —personal, extranjería, inadmisión de asilo— o cuantía inferior a 30.000 €), la demanda es la inicial y directa de /procedimiento-abreviado-ca.
---

# Demanda contencioso-administrativa (procedimiento ordinario)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Preceptos procesales de la demanda** → `buscar_articulo` (`ley="LJCA"`, artículos 40 a 42, 52, 55, 56, 60 y 62).
- **Motivos de nulidad y anulabilidad** → `buscar_articulo` (`ley="LPAC"`, artículo 47 con su letra y artículo 48) y la norma sectorial estatal con `buscar_boe` + `leer_boe`.
- **Doctrina de cada fundamento de fondo** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`; `base="TS"`, o `base="AN"` con `tipo_organo="TSJ"` y `provincia`) + `leer_sentencias` (`parrafos=3`, `terminos` del punto a acreditar).
- **Casación admitida con identidad jurídica sustancial (art. 56.5)** → `buscar_sentencias` (`base="TS"`, `tipo_resolucion="AUTO"`).
- **Ordenanza aplicada por el acto** → `buscar_ordenanzas` + `leer_ordenanza` con `articulo`.
- **Materia tributaria** → `buscar_doctrina_teac` + `leer_resolucion_teac` (criterio del TEAC en la vía previa) y `buscar_consultas_hacienda` + `leer_consulta_hacienda`.
- **Antes de presentar** → `verificar_escrito` sobre el borrador completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

---

Instrucciones PARA Claude. Fuente única de plazos y umbrales: `references/anclas-normativas-ca.md`.
Lo que no esté allí, verifícalo con `buscar_articulo` o márcalo `[verificar]`. **No inventes nunca**
plazos, letras de artículo ni cifras.

> **Antes de nada:** si el asunto es de **personal**, **extranjería**, **inadmisión de asilo
> político**, **disciplina deportiva en dopaje** o de **cuantía ≤ 30.000 €**, el cauce es el
> **abreviado** (art. 78.1) y la demanda **inicia** el proceso → usa `procedimiento-abreviado-ca`.
> Esta skill es para el **ordinario**, donde la demanda se formaliza **tras** el expediente.

## 1. El plazo: 20 días desde la entrega del expediente (art. 52.1)

- Recibido el expediente **en soporte electrónico** y comprobados los emplazamientos, el LAJ lo
  incorpora a los autos y lo **entrega al recurrente** para deducir la demanda en **20 días**
  (art. 52.1, redacción RD-ley 6/2023, vigente 20-3-2024). La entrega es **telemática** o por el
  **punto de acceso electrónico** al expediente judicial.
- Varios recurrentes → demanda **simultánea** por todos, aunque no compartan dirección letrada.
- ⚠️ **Art. 52.2 — CADUCIDAD DEL RECURSO.** No presentada la demanda en plazo, el órgano declara
  **de oficio, por auto, la caducidad del recurso**. **Única red de seguridad:** se admite la
  demanda si se presenta **dentro del día en que se notifique ese auto**. No la conviertas en plan:
  al recibir el expediente, **anota el vencimiento y avisa** (regla de la casa: presentar con
  7 días naturales de antelación).
- **Agosto — art. 128.2 LJCA:** no corre ningún plazo de la LJCA, **salvo derechos fundamentales**,
  donde agosto **sí** es hábil. **No cites el art. 133 LEC.**
- Si el expediente llega **incompleto**, denúncialo **antes** de que corra el plazo y pide su
  completación (art. 55 — verifícalo antes de citarlo). No construyas hechos sobre un expediente
  mutilado: pide los folios que faltan.

## 2. Comprobaciones previas

1. **Relee el expediente completo** y **pagina** las citas. Toda afirmación de hecho irá anclada.
2. **Verifica la admisibilidad** aunque ya interpusieras: las causas del **art. 69** se aprecian
   hasta sentencia (jurisdicción, representación/legitimación, objeto no impugnable, cosa juzgada
   o litispendencia, extemporaneidad).
3. **Comprueba la cuantía** (§ 5): decide apelabilidad y pudo decidir el cauce.
4. **Art. 56.5** (RD-ley 5/2023): si hay un **recurso de casación admitido por el TS con identidad
   jurídica sustancial**, el órgano puede **suspender** el procedimiento, oídas las partes por
   10 días. Si detectas esa identidad, **valórala y dilo**: puede convenir o perjudicar.

## 3. Contenido de la demanda — art. 56 LJCA

**Art. 56.1:** se consignarán **con la debida separación** los **hechos**, los **fundamentos de
Derecho** y las **pretensiones**, «en justificación de las cuales podrán alegarse cuantos motivos
procedan, **hayan sido o no planteados ante la Administración**».

> ⚠️ **Distinción que decide asuntos.** **MOTIVOS** nuevos: **permitidos** aunque no se alegaran en
> vía administrativa (art. 56.1). **PRETENSIONES** nuevas, ajenas al acto impugnado: **prohibidas**
> — es la **desviación procesal**. La demanda debe moverse dentro del objeto delimitado por el acto
> recurrido en el escrito de interposición. Añadir argumentos jurídicos: sí. Pedir cosas que el acto
> no decidió: no.

**Art. 56.3:** acompaña los documentos **en que directamente fundes tu derecho**; si no obran en tu
poder, **designa el archivo, oficina, protocolo o persona** en cuyo poder se encuentren.
**Art. 56.4:** después de demanda y contestación **no se admiten más documentos** salvo los casos
del proceso civil; **excepción**: el demandante puede aportar documentos para **desvirtuar
alegaciones de la contestación** que pongan de manifiesto disconformidad en los hechos, **antes de
la citación de vista o conclusiones**. Reserva esa carta.
**Art. 56.2:** el LAJ examina de oficio la demanda y requiere subsanación en **plazo no superior a
10 días**.

### Estructura

1. **Encabezamiento** — órgano, `[CLIENTE]`, representación y postulación (**art. 23 LJCA**:
   procurador potestativo ante Juzgados, preceptivo ante Salas), nº de autos.
2. **HECHOS**, numerados y **cronológicos**. **Cada hecho anclado al expediente con folio**:
   «según consta al **folio [N]** del expediente administrativo». Sin folio, un hecho es una
   afirmación de parte. Distingue lo que consta en el expediente de lo que habrá que probar.
3. **FUNDAMENTOS DE DERECHO** — en este orden:
   - **Procesales:** jurisdicción y competencia (arts. 8-14), legitimación (art. 19), plazo
     (art. 46), procedimiento y cuantía.
   - **De fondo**, un fundamento por motivo, **del más fuerte al más débil**, encabezado con su
     tesis. Aplica `estilo-escritos-judiciales`: el porqué antes del qué.
4. **SUPLICO** (§ 4) y **OTROSÍES** (§ 6).

## 4. Motivos de fondo — nulidad, anulabilidad y desviación de poder

**Nulidad de pleno derecho — art. 47.1 LPAC** (cita **la letra exacta**; no la parafrasees):
a) actos que **lesionen derechos y libertades susceptibles de amparo constitucional**;
b) dictados por **órgano manifiestamente incompetente** por razón de **materia o territorio**;
c) de **contenido imposible**; d) constitutivos de **infracción penal** o dictados como
consecuencia de ésta; e) dictados **prescindiendo total y absolutamente del procedimiento**
legalmente establecido **o de las reglas esenciales para la formación de la voluntad de los órganos
colegiados**; f) actos expresos o presuntos **contrarios al ordenamiento por los que se adquieren
facultades o derechos careciendo de los requisitos esenciales**; g) cualquier otro **establecido
expresamente en norma con rango de Ley**.
**Art. 47.2:** disposiciones que vulneren la Constitución, las leyes o disposiciones de rango
superior, regulen materias reservadas a la Ley, o establezcan **retroactividad** de disposiciones
sancionadoras no favorables o restrictivas de derechos.

**Anulabilidad — art. 48 LPAC:**
- **48.1:** cualquier infracción del ordenamiento jurídico, **incluida la DESVIACIÓN DE PODER**
  (ejercicio de potestades para fines distintos de los fijados por el ordenamiento). Si la invocas,
  **acredita el fin desviado con datos del expediente** — no la alegues como adorno retórico.
- **48.2:** el **defecto de forma** solo anula si el acto **carece de los requisitos formales
  indispensables para alcanzar su fin** o **da lugar a indefensión**. Argumenta **la indefensión
  material concreta**: qué no pudo alegar el cliente y qué habría cambiado. La irregularidad no
  invalidante es la respuesta estándar de la Administración: anticípate.
- **48.3:** la actuación **fuera de plazo** solo anula cuando lo imponga la naturaleza del término.

**Elección estratégica:** nulidad y anulabilidad no son intercambiables. La nulidad no tiene plazo y
es apreciable de oficio; la anulabilidad sí está sujeta a plazo. Si el motivo encaja en el art. 47,
**dilo y razona la letra**. Si no encaja, **no lo fuerces**: un art. 47.1.e) mal invocado desacredita
el resto del escrito.

## 5. Cuantía — arts. 40-42 LJCA y su doble efecto

**Fíjala siempre y por otrosí. Tiene dos efectos que deciden el asunto:**
1. **Cauce:** **≤ 30.000 €** → **abreviado** (art. 78.1).
2. **Apelabilidad:** **≤ 30.000 €** → **no cabe apelación** (art. 81.1.a). Una cuantía mal fijada a
   la baja **cierra la segunda instancia**. Es un error irreversible: adviértelo al usuario.
   (Además, el tope de costas es **1/3 de la cuantía** por cada favorecido — art. 139.4.)

**Reglas — art. 42:**
- **42.1.a)** Si solo se pide la **anulación**: **contenido económico del acto**, atendiendo al
  **débito principal**, **sin** recargos, costas ni otras responsabilidades — **salvo** que alguno
  de éstos sea **de importe superior** al principal.
- **42.1.b)** Si además se pide el **reconocimiento de una situación jurídica individualizada** o el
  cumplimiento de una obligación administrativa: **valor económico total** del objeto de la
  reclamación si la Administración **denegó totalmente** en vía administrativa; **la diferencia**
  entre lo reclamado y el acto si **reconoció parcialmente**.
- **42.2 — cuantía INDETERMINADA:** impugnación **directa de disposiciones generales**, **incluidos
  los instrumentos normativos de planeamiento urbanístico**; asuntos de **funcionarios públicos**
  cuando **no versen sobre derechos o sanciones susceptibles de valoración económica**; y cuando se
  **acumulen** pretensiones evaluables y no evaluables. También, en **Seguridad Social**: inscripción
  de empresas, formalización de la protección frente a riesgos profesionales, tarifación, cobertura
  de IT, afiliación, alta, baja y variaciones de datos.

**Procedimiento — art. 40:** el LAJ fija la cuantía tras demanda y contestación; las partes exponen
su parecer **por otrosí**. Si no se hace, requerimiento de **10 días** al demandante (art. 40.2). El
demandado puede discrepar en **10 días** (art. 40.3) y el juez resuelve definitivamente en sentencia.
**Art. 40.4:** cabe **queja** por indebida determinación de la cuantía si por su causa no se tiene
por preparada la casación o no se admite la apelación.

## 6. Suplico y otrosíes

**SUPLICO — art. 31 LJCA. Pide las TRES cosas cuando procedan; pedir solo la anulación es el error
más caro del orden contencioso:**
1. **Art. 31.1** — que se declare **no conforme a Derecho** y se **anule** el acto `[EXPEDIENTE]`.
2. **Art. 31.2** — que se **reconozca la situación jurídica individualizada** de `[CLIENTE]` y se
   adopten **las medidas adecuadas para su pleno restablecimiento** (reincorporación, devolución de
   ingresos, otorgamiento de la licencia, reconocimiento del grado...). **Concrétala.** Un suplico
   que solo anula devuelve el asunto a la Administración y regala otra vuelta al procedimiento.
3. **Art. 31.2 in fine** — **indemnización de daños y perjuicios** cuando proceda, con `[IMPORTE]` y
   bases de cálculo. Si consta probada en autos, podrá pedirse pronunciamiento concreto sobre
   existencia y cuantía **también en conclusiones** (art. 65.3).
4. **Costas** (art. 139).

**OTROSÍES:**
- **PRIMERO — Cuantía** (arts. 40-42).
- **SEGUNDO — Recibimiento a prueba (art. 60).** ⚠️ **Solo puede pedirse por OTROSÍ en la demanda**
  (o contestación, o alegaciones complementarias). **Expresa de forma ordenada los PUNTOS DE HECHO**
  sobre los que verse y **los MEDIOS** que propones (art. 60.1). Omitirlo **precluye la prueba**.
  - **Art. 60.3:** se recibe a prueba cuando haya disconformidad en hechos **de trascendencia**; y
    **si el objeto es una SANCIÓN administrativa o disciplinaria, el proceso se recibirá SIEMPRE a
    prueba cuando exista disconformidad en los hechos**. En sancionador, **invoca este inciso**.
  - **Art. 60.4:** plazo de práctica **30 días**, con las normas del proceso civil.
  - **Art. 60.2:** si de la contestación resultan **hechos nuevos** de trascendencia, puedes pedir
    recibimiento a prueba en **5 días** desde el traslado.
- **TERCERO — Vista o conclusiones (art. 62).** Solicítalo **por otrosí aquí** o en 5 días desde la
  diligencia que declare concluso el período de prueba (art. 62.2). **Art. 62.3:** el LAJ provee
  según lo coincidente; en otro caso, **solo acuerda vista o conclusiones cuando lo pida el
  DEMANDANTE**, o cualquiera de las partes si se practicó prueba. **Posición privilegiada del
  demandante: úsala.** → skill `escrito-conclusiones-ca`.
- **CUARTO — Medidas cautelares (art. 129)**, si no se pidieron ya: pieza separada (art. 131),
  criterio del **periculum in mora** (art. 130.1), ponderación de intereses (art. 130.2).
- **QUINTO —** Documentos en poder de tercero (art. 56.3), acumulación, o lo que proceda.

## 7. Errores que pierden el asunto

- **Desviación procesal:** introducir **pretensiones ajenas al acto impugnado** (art. 56.1). Motivos
  nuevos sí; pretensiones nuevas no.
- **Suplicar solo la anulación** y no el **reconocimiento de la situación jurídica individualizada**
  ni la **indemnización** (art. 31.2).
- **Olvidar el otrosí de recibimiento a prueba** (art. 60.1): precluye.
- **Fijar la cuantía a la baja** y perder la apelación (art. 81.1.a).
- **Afirmar hechos sin folio del expediente.**
- **Dejar pasar los 20 días** (art. 52.2: caducidad de oficio).
- **Alegar defecto de forma sin acreditar indefensión material** (art. 48.2).
- **Confundir nulidad y anulabilidad** invocando el art. 47 sin encaje.
- **Aplicar el art. 133 LEC a agosto** en lugar del **art. 128.2 LJCA**.

## 8. Cierre

- **Jurisprudencia:** verifica **antes de citar** con `buscar_sentencias` / `buscar_por_cita`.
  Prohibido inventar ECLI, ROJ, fechas, ponentes o fundamentos.
- **Normativa autonómica y local** (urbanismo, actividades, tributos locales): **el conector no la
  cubre**. Pídesela al usuario y **no la cites de memoria**.
- **Protección de datos:** `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`, `[EXPEDIENTE]`. El
  expediente contiene datos de terceros y, en sanitario, **datos de salud** (art. 9 RGPD, categoría
  especial): **nunca los reproduzcas**.
- **Nada de MASC:** es del orden civil.
- **Entregable:** Word `.docx` maquetado (skill `docx`). Aplica `estilo-escritos-judiciales`.
