---
name: contestacion-demanda-ca
description: Redacta la contestación a la demanda contencioso-administrativa y las alegaciones previas del art. 58 LJCA desde la posición PASIVA — defendiendo a la Administración demandada, a un codemandado (aseguradora, adjudicatario de un contrato, titular de una licencia) o a un tercero interesado emplazado ex art. 49 LJCA. Activar con "contestar la demanda contencioso", "nos demandan en el contencioso", "defender a la Administración", "somos codemandados", "alegaciones previas", "inadmisibilidad del recurso", "me han emplazado como interesado", "defendemos a la aseguradora del ayuntamiento", "oponernos al recurso".
---

# Contestación a la demanda contencioso-administrativa (arts. 54, 56 y 58 LJCA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Preceptos de la posición pasiva** → `buscar_articulo` (`ley="LJCA"`, artículos 21, 49, 54, 56, 58 a 60 y 69; `ley="LPAC"`, artículos 39 y 48).
- **Cada cita jurisprudencial del recurrente** → `buscar_por_cita` + `leer_sentencias` (`parrafos=3`, `terminos` de la tesis contraria) para detectar citas erróneas o descontextualizadas.
- **Discrecionalidad técnica, irregularidad no invalidante y motivación de la sanción** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"`) + `leer_sentencias` (`parrafos=3`).
- **Casación admitida con identidad jurídica sustancial (art. 56.5)** → `buscar_sentencias` (`base="TS"`, `tipo_resolucion="AUTO"`, `consulta` con la cuestión) para localizar el auto de admisión.
- **Recurrente persona jurídica (falta de acuerdo corporativo) o codemandado adjudicatario** → `buscar_empresa_mercantil` (órgano de administración, apoderados y últimos actos inscritos).
- **Antes de presentar** → `verificar_escrito` sobre el borrador completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

Posición **pasiva**. Plazos y cifras: `references/anclas-normativas-ca.md`. Lo que no esté allí,
verifícalo con `buscar_articulo` o márcalo `[verificar]`.

> ⚠️ **ANTES DE ACEPTAR EL ENCARGO — conflicto de interés.** Si el despacho litiga habitualmente
> **frente** a la Administración (perfil por defecto del plugin), asumir su defensa —o la de un
> codemandado alineado con ella— puede generar conflicto: contra cliente actual, contra cliente anterior
> en asunto conexo, o contra la tesis que el despacho sostiene viva en otro pleito. **Correr el chequeo
> de conflictos y obtener el visto bueno antes de redactar una línea.** Si hay duda, escalarla.

---

## 1. La baza estructural del demandado

En el contencioso **el demandado parte ganando**, y por Derecho positivo:

1. **Presunción de validez** — art. 39.1 LPAC (verificado): «Los actos de las Administraciones Públicas
   sujetos al Derecho Administrativo **se presumirán válidos y producirán efectos desde la fecha en que
   se dicten**, salvo que en ellos se disponga otra cosa.» La carga de **destruirla** es del recurrente.
   La contestación no debe demostrar que el acto es perfecto, sino que **el recurrente no lo ha
   desvirtuado**.
2. **El expediente es la prueba principal y lo aporta la propia Administración**, ordenado y foliado por
   quien defiende el acto. Cada afirmación propia se ancla a folio; cada afirmación de la demanda que
   **no** conste en el expediente se señala como **no acreditada**.

> **En redacción:** no escribir «el acto es conforme a Derecho porque...», sino «el recurrente no ha
> acreditado / no ha desvirtuado / afirma sin soporte en el expediente...», y solo después,
> subsidiariamente, la defensa positiva. Invertir el orden es asumir una carga que no corresponde.

---

## 2. Quién es parte demandada (art. 21, verificado)

**21.1:** **a)** las **Administraciones** o los órganos del art. 1.3 **contra cuya actividad se dirija
el recurso**; **b)** las **personas o entidades cuyos derechos o intereses legítimos pudieran quedar
afectados por la estimación** (adjudicatario, titular de la licencia, aspirante que obtuvo la plaza);
**c)** ⚠️ las **aseguradoras de las Administraciones**, que **«siempre serán parte codemandada junto con
la Administración a quien aseguren»** — literal: **«siempre»**, no es opcional. Nuclear en
responsabilidad patrimonial.

- **21.2** — Entes sujetos a fiscalización: demandada es el **autor** del acto si la fiscalización fue
  aprobatoria; la **fiscalizadora** si no aprobó íntegramente.
- **21.3** — Recursos contra decisiones de los **órganos de recursos contractuales**: esos órganos **NO
  son parte demandada**; lo son las personas o Administraciones **favorecidas** por el acto, o que se
  personen ex art. 49. **Error frecuente:** demandar al tribunal administrativo de contratación. Si se
  defiende al **adjudicatario**, este es el demandado y debe personarse.
- **21.4** — Si la pretensión se funda en la **ilegalidad de una disposición general**, es **también
  demandada la Administración autora de la disposición** (ver `impugnacion-disposiciones-generales-ca`).

**Codemandado ≠ coadyuvante.** La LJCA de 1998 **suprimió el coadyuvante** de la ley de 1956: quien
tiene interés legítimo afectado es **parte demandada de pleno derecho** (art. 21.1.b), con posición
**plena** — contesta, prueba, recurre y pide costas por sí. **No** supeditar su defensa a la de la
Administración: si esta se allana, desiste o defiende mal, el codemandado **conserva la suya**. Si
aparece «coadyuvante» en un escrito o resolución, es terminología histórica: no reproducirla.

---

## 3. Emplazamiento de interesados (art. 49, verificado)

| Trámite | Regla |
|---|---|
| Notificación | La resolución que acuerda **remitir el expediente** se notifica **en los 5 días siguientes** a **cuantos aparezcan como interesados** en él (49.1) |
| **Personación** | **9 días** para personarse **como demandados** (49.1) ⚠️ **Nueve, no veinte** |
| Contratación pública | Se emplaza a quienes, distintos del recurrente, comparecieron en el recurso administrativo — también **9 días** (49.1.II) |
| Control judicial | Si las notificaciones son **incompletas**, el LAJ **ordena a la Administración** practicar las necesarias para asegurar la defensa de los interesados **identificables** (49.3) |
| Edictos | **Tablón Edictal Judicial Único**; los emplazados por edictos pueden personarse **hasta el momento en que hubiere de dárseles traslado para contestar** (49.4) |
| Lesividad | Emplazamiento **personal**, **9 días** (49.6) |

> **Uso defensivo:** si el cliente **no fue emplazado** pese a ser interesado identificable en el
> expediente, hay munición de **indefensión** (49.3 impone al LAJ ordenar la subsanación).
> **Uso preventivo:** si **sí fue emplazado y dejó pasar los 9 días**, el daño puede ser irreversible.
> **Primera pregunta a quien llega con un emplazamiento: ¿qué día lo recibió?**

---

## 4. Plazo para contestar y qué pasa si no se contesta (art. 54, verificado)

- **Plazo: 20 días** desde el traslado de la demanda con entrega del expediente (54.1).
- **⚠️ El apercibimiento del art. 54.1 es OTRA cosa de lo que suele creerse.** No se refiere a las
  consecuencias de no contestar: si la demanda se formalizó **sin haberse recibido el expediente**, se
  emplaza a la Administración «**apercibiéndola de que no se admitirá la contestación si no va
  acompañada de dicho expediente**». El apercibimiento es **sobre el expediente**: contestar sin
  acompañarlo = **contestación inadmitida**. Comprobarlo en cada asunto antes de presentar.
- **Orden (54.3):** contesta **primero la Administración**; si hay otros demandados, todos ellos
  contestan **simultáneamente**, aunque no actúen bajo una misma dirección. El codemandado **no**
  contesta después: coordinar agenda.
- **Entidad local no personada (54.4):** se le da traslado igualmente para que en **20 días** designe
  representante o **comunique por escrito** por qué estima improcedente la pretensión.
- **Suspensión por parecer razonado (54.2):** si el defensor de la Administración estima que el acto
  **pudiera no ajustarse a Derecho**, puede pedir **suspensión por 20 días** para comunicar su parecer
  razonado a aquélla. Vía institucional antes de defender lo indefendible.

> ⚠️ **EL ERROR DE QUIEN VIENE DEL CIVIL — decirlo expresamente.** No contestar **NO** produce
> **allanamiento tácito**, **NO** produce **ficta confessio**, **NO** produce admisión de hechos y **NO**
> hay rebeldía con los efectos de la LEC. Lo que opera es el **art. 128.1 LJCA** (verificado): los plazos
> son improrrogables y, transcurridos, el LAJ **tendrá por caducado el derecho y por perdido el trámite**
> que se dejó de utilizar. Se pierde **el trámite, no el pleito**: el proceso sigue, el expediente sigue
> siendo prueba y el recurrente **sigue teniendo que acreditar su pretensión** frente al art. 39.1 LPAC.
> **Salvavidas del art. 128.1 in fine:** se admite el escrito presentado **dentro del día en que se
> notifique** la resolución de caducidad —salvo plazos para preparar o interponer recursos—: un día, no
> una prórroga. Nada de esto excusa no contestar: sirve para calibrar el daño y actuar el mismo día.

---

## 5. Alegaciones previas (art. 58, verificado)

**Literal del 58.1:** las demandadas podrán alegar, **«dentro de los primeros cinco días del plazo para
contestar la demanda»**, los motivos que pudieren determinar **la incompetencia del órgano
jurisdiccional** o **la inadmisibilidad del recurso con arreglo al art. 69**, «sin perjuicio de que tales
motivos, **salvo la incompetencia del órgano jurisdiccional**, puedan ser alegados en la contestación,
**incluso si hubiesen sido desestimados como alegación previa**».

1. **Plazo: los 5 PRIMEROS días de los 20.** ⚠️ No es trámite añadido: **corre dentro** del plazo de
   contestación. Perdido el día 5 no hay previas, pero **sí contestación**. Calendar **día 5** y **día 20**.
2. **Motivos:** los del **art. 69** **más** la **incompetencia del órgano jurisdiccional** — que el
   precepto menciona **separada** de las causas del 69: no confundirla con el 69.a) (**falta de
   jurisdicción**), que es cosa distinta.
3. **Doble oportunidad:** cabe oponerlos como previa **O** en la contestación, e incluso en la
   contestación **aunque ya se hubieran desestimado** como previa. **Excepción verificada: la
   incompetencia del órgano jurisdiccional**, exceptuada de esa reiteración → **si el motivo es ese, hay
   que plantearlo en los 5 primeros días**: es el único con ventana corta y única.
4. **58.2:** para usar el trámite, la Administración ha de **acompañar el expediente** si no lo remitió.

> **¿Previas o contestación?** **Previas** si el motivo es **incompetencia del órgano jurisdiccional**
> (obligado) o si es **objetivo, documental y limpio** (extemporaneidad con fecha en el expediente, falta
> de acuerdo corporativo del art. 45.2.d) y se quiere cerrar pronto sin descubrir el fondo. **En la
> contestación** si exige valoración o va entrelazado con el fondo (legitimación discutible): plantearlo
> como previa y perderlo desgasta y avisa al contrario. **Regla práctica: ante la duda, y salvo
> incompetencia, oponerlo en la contestación** — no hay preclusión, reservarlo no cuesta nada.
> Tramitación del incidente (arts. 59-60): **verificar con `buscar_articulo` antes de calendar**.

---

## 6. Causas de inadmisibilidad (art. 69, verificado)

La sentencia declarará la inadmisibilidad **del recurso o de alguna de las pretensiones** cuando:

| | Causa | Cómo se trabaja |
|---|---|---|
| **a)** | **Falta de jurisdicción** | Materia realmente civil, laboral o social; contratos privados. Distinta de la incompetencia del 58.1 |
| **b)** | **Persona incapaz, no debidamente representada o no legitimada** | La mina: **art. 45.2.d)** — falta del **acuerdo corporativo** (poder ≠ acuerdo). Comprobar SIEMPRE si el recurrente es sociedad, asociación o comunidad. También: interés legítimo inexistente |
| **c)** | **Objeto no susceptible de impugnación** | Acto de trámite **no cualificado**; **firme y consentido**; **confirmatorio** de otro firme; que no pone fin a la vía; mera respuesta informativa. Contrastar con el art. 25 |
| **d)** | **Cosa juzgada o litispendencia** | Identidad de sujeto, objeto y causa de pedir |
| **e)** | **Escrito inicial fuera de plazo** | ⚠️ La estrella. Plazos de **CADUCIDAD**: no se interrumpen por burofax ni reclamación extrajudicial. Reconstruir el cómputo con la **fecha de notificación del expediente**, acuse y folio. Ojo al art. 128.2 (**agosto no corre**, salvo DDFF) y al 46.4 (reposición potestativa): la Administración pierde muchas extemporaneidades por computar agosto mal **en su contra** |

> **Método:** la inadmisibilidad se gana **con el expediente**: acuse de recibo, sello de registro,
> acuerdo corporativo (o su ausencia), citados **por folio**. Una excepción sin fecha y folio no prospera.
> **Rigor:** no acumular excepciones por inercia — cinco inadmisibilidades endebles restan credibilidad a
> la buena. Seleccionar.

---

## 7. Oposición de fondo

1. **Presunción de validez (39.1 LPAC)** y carga del recurrente — eje transversal (§ 1).
2. **Motivación suficiente:** contestar **con folio** (informes, propuesta de resolución). Distinguir
   **motivación escueta** (válida) de **ausencia de motivación**.
3. **Corrección del procedimiento** y, frente a vicios formales menores, **anulabilidad y conservación**
   (arts. 48 y ss. LPAC: irregularidad no invalidante si no produce indefensión ni impide el fin del
   acto) — **verificar el precepto exacto con `buscar_articulo` antes de citarlo**.
4. **Proporcionalidad**, señaladamente en sancionador: graduación e individualización razonadas. Si la
   sanción se impuso en grado mínimo, decirlo.
5. **Discrecionalidad técnica** (tribunales de oposiciones, valoraciones técnicas): el control no
   sustituye el juicio técnico salvo error patente, arbitrariedad o desviación de poder. Alcance:
   **jurisprudencial** — verificar con `buscar_sentencias`.
6. **Hechos no acreditados:** listar una a una las afirmaciones de la demanda sin soporte en el
   expediente. Lo más rentable del escrito.
7. **Subsidiariedad ordenada:** inadmisión → desestimación total → y solo si procede, cuantía o alcance.

**Prueba y documentos (art. 56, verificado).** *56.3:* con la contestación se acompañan los documentos
en que **directamente se funde el derecho**; si no obran en poder de la parte, **designar** archivo,
oficina, protocolo o persona. *56.4:* **después de la contestación no se admiten más documentos** que en
los casos del proceso civil —el demandante conserva una ventana para desvirtuar alegaciones de la
contestación—. **La contestación es la última llamada documental del demandado: aportarlo todo ahora.**
*56.1:* pueden alegarse **cuantos motivos procedan, hayan sido o no planteados ante la Administración**
(con el límite de la motivación *ex post* del acto sancionador: verificar con `buscar_sentencias`).
*56.5 (RD-ley 5/2023):* si hay **casación admitida por el TS con identidad jurídica sustancial**, cabe
**suspensión** previa audiencia común de 10 días; contra el auto que la resuelve **no cabe recurso**.
Comprobarlo siempre: si la casación pendiente favorece al cliente, pedirla.

---

## 8. Estructura y SUPLICO

1. **Encabezamiento:** órgano; autos; procurador (preceptivo ante colegiados, art. 23.2); **concepto en
   que se comparece** — Administración demandada, **codemandado ex 21.1.b)**, **aseguradora ex 21.1.c)**
   o **autora de la disposición ex 21.4**.
2. **A los HECHOS de la demanda**, **ordinal por ordinal**: admitido / admitido con matices / **negado
   por no constar en el expediente**. Ningún ordinal sin respuesta.
3. **HECHOS propios** con folio (`(doc. núm. X, folio Y)`).
4. **PROCESALES — inadmisibilidades (art. 69)**, una por ordinal (§ 6). Si ya se opusieron como previas
   y se desestimaron, **reiterarlas** (el 58.1 lo permite, salvo incompetencia).
5. **FONDO** (§ 7), abriendo con presunción de validez y carga probatoria.
6. **Jurisprudencia del contrario:** verificar **cada** cita con `buscar_por_cita` — las citas erróneas o
   descontextualizadas del recurrente son munición.
7. **SUPLICO** y **OTROSÍES:** prueba con puntos de hecho; vista o conclusiones; **cuantía** si se
   discute (afecta a apelación y al tope de costas del 139.4); suspensión ex 56.5 si procede.

> **SUPLICO AL JUZGADO/A LA SALA** que, teniendo por presentado este escrito con sus documentos, se sirva
> admitirlo, tener por **contestada la demanda** en tiempo y forma por **[CLIENTE]**, en su condición de
> **[Administración demandada / parte codemandada ex art. 21.1.b) LJCA / aseguradora codemandada ex art.
> 21.1.c) LJCA]**, y dictar sentencia por la que:
> **1.º)** con carácter principal, **declare la INADMISIBILIDAD** del recurso conforme al **art. 69.[letra]
> LJCA**, por **[causa]**;
> **2.º)** subsidiariamente, **DESESTIME íntegramente** el recurso, **confirmando** el acto impugnado
> **[ACTO]**, de **[ÓRGANO]**, de **[FECHA]**, por ser conforme a Derecho;
> todo ello con **expresa imposición de costas a la recurrente** (**art. 139.1 LJCA**).
>
> **PRIMER OTROSÍ DIGO** que, a tenor del **art. 60 LJCA**, **SUPLICO** el **recibimiento del pleito a
> prueba**, sobre los siguientes puntos de hecho: **[PUNTOS]**.

- **Costas (art. 139, anclas):** en 1.ª o única instancia rige el **vencimiento objetivo**, salvo serias
  dudas **razonadas**. Pedirlas siempre. **Tope del 139.4** (1/3 de la cuantía por favorecido; 18.000 € si
  indeterminada): si el cliente espera recuperar honorarios, **advertirlo por escrito**.
- Si se defiende a un **codemandado**, el suplico es **propio y completo**, no una adhesión al de la
  Administración (§ 2).

## 9. Reglas de la casa

- **Conflicto de interés:** chequeo **previo** obligatorio (aviso de cabecera).
- **Protección de datos:** cero datos reales. `[CLIENTE]`, `[ÓRGANO]`, `[DOMICILIO]`, `[FECHA]`,
  `[IMPORTE]`. Anonimizar a los terceros del expediente.
- **Jurisprudencia:** prohibido citar ECLI/ROJ/fecha/ponente de memoria. `buscar_sentencias` y
  `buscar_por_cita` — **incluidas las citas del contrario**. Lo no verificado se marca `[verificar]`.
- **Normativa autonómica y local:** el conector no la cubre (solo BOE estatal + ordenanzas de municipios
  cubiertos, vía `buscar_ordenanzas`). **Pedírsela al usuario**; no citarla de memoria.
- **Nada de MASC:** es del orden **civil**; no existe aquí, ni como excepción oponible al recurrente.
- **Entregable:** Word `.docx` maquetado (skill `docx`).
