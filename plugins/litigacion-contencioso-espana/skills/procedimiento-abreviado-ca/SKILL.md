---
name: procedimiento-abreviado-ca
description: >-
  Guía y redacción del procedimiento abreviado contencioso-administrativo en sede JUDICIAL (art. 78 LJCA, redacción LO 1/2025) — ámbito por materia y por cuantía, demanda inicial directa, vista rogada y motivada, expediente electrónico y sentencia oral. Activar con "procedimiento abreviado contencioso", "art. 78 LJCA", "demanda abreviado", "llevar la multa ya firme en vía administrativa al juzgado", "recurso de personal", "extranjería", "asunto de menos de 30.000 euros". Requisito previo: vía administrativa AGOTADA. Si la sanción está todavía en tramitación administrativa (pliego de cargos, propuesta de resolución, alzada o reposición pendientes), usar antes /procedimiento-sancionador-ca; para decidir entre ordinario y abreviado hace falta conocer materia y cuantía → si el asunto no encaja en el art. 78.1 ni baja de 30.000 €, va por ordinario (/interposicion-recurso-contencioso-ca y después /demanda-contencioso-administrativa).
---

# Procedimiento abreviado (art. 78 LJCA)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Ámbito, trámites y vista** → `buscar_articulo` (`ley="LJCA"`, artículos 29, 45, 78 y 81).
- **Sanción municipal** (tráfico urbano, terrazas, ruido, ZBE) → `buscar_ordenanzas` + `leer_ordenanza` con `articulo` del tipo aplicado.
- **Sanción de tráfico** → `buscar_articulo` (`ley="Ley de Tráfico"` —RDL 6/2015—, artículos 94, 95 y 112).
- **Criterio del juzgado o de la Sala en personal y extranjería** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="AN"`, `provincia`, `tipo_organo="TSJ"`) + `leer_sentencias` (`parrafos=3`).
- **Extranjería con Derecho de la UE** → `buscar_articulo` (`ley="LOEX"`) y `buscar_sentencias` (`base="TJUE"`).
- **Antes de presentar la demanda** → `verificar_escrito`.

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

> ⛔ **ERRATAS VERIFICADAS — NO REINTRODUCIR** (BOE, 2026-07-17):
> 1. Versiones anteriores decían que el abreviado cubre **«cuestiones de tráfico»** como materia.
>    **ES FALSO.** El art. 78.1 **no menciona el tráfico**. Las sanciones de tráfico entran por
>    **CUANTÍA**, no por materia. No inventes una materia que la ley no recoge.
> 2. El umbral es **30.000 €**. Está **verificado**: no escribas «verifica el umbral vigente».
> 3. Versiones anteriores situaban las **«conclusiones orales» en el art. 78.6**. **ES FALSO.**
>    El **art. 78.6** es la **apertura de la vista** por el demandante. Ver § 5.

## 1. Ámbito — art. 78.1 (texto vigente)

Conocen los **Juzgados** de lo Contencioso-administrativo y los **Juzgados Centrales**, por este
cauce, de los asuntos de su competencia que se susciten:

**POR MATERIA** — lista **cerrada**, son solo cuatro:
1. Cuestiones de **personal al servicio de las Administraciones Públicas**.
2. **Extranjería**.
3. **Inadmisión de peticiones de asilo político**.
4. **Disciplina deportiva en materia de dopaje**.

**POR CUANTÍA:** «todas aquellas cuya cuantía **no supere los 30.000 euros**».

- ⚠️ **El tráfico NO es materia del art. 78.1.** Una multa de tráfico va al abreviado **porque su
  cuantía no supera los 30.000 €**. La diferencia importa: si un asunto de tráfico superase ese
  umbral, iría al **ordinario**. Razona siempre por la vía correcta.
- **Entrada adicional — art. 29.2:** el recurso por **no ejecución de actos firmes** (petición y
  **1 mes** sin ejecución) **se tramita por el abreviado**, con independencia de materia o cuantía.
- **Impugnación del cauce por cuantía — art. 78.9:** si el demandado impugna la adecuación del
  procedimiento por razón de la cuantía, el juez exhorta a las partes a acordar antes de la prueba o
  las conclusiones; sin acuerdo, decide él y da al proceso el curso que corresponda. **Contra esa
  decisión no cabe recurso alguno.**
- **Recuerda el doble efecto de la cuantía:** **≤ 30.000 €** también significa **sin apelación**
  (art. 81.1.a). Advierte al cliente **antes** de fijarla.

## 2. Iniciación: por DEMANDA — art. 78.2

- El recurso **se inicia por demanda**, **no** por escrito de interposición del art. 45.1. Es la
  diferencia estructural con el ordinario: aquí se argumenta el fondo **desde el primer escrito y
  sin haber visto el expediente**. Trabaja con la documentación del cliente y con lo que se pueda
  reclamar en la vista.
- Se acompañan **los documentos en que el actor funde su derecho** y **los del art. 45.2**:
  a) representación; b) legitimación por transmisión; c) copia del acto o indicación del expediente;
  **d) personas jurídicas: el ACUERDO CORPORATIVO** — documento acreditativo del cumplimiento de los
  requisitos para entablar acciones según sus normas o estatutos. **No basta el poder.** Es la causa
  de inadmisión más frecuente y evitable; **pregunta siempre por el acuerdo**;
  **e) sindicatos** ex art. 19.1.k) (**LO 1/2025**, vigente 3-4-2025): **afiliación**, **comunicación
  al afiliado** de la voluntad de iniciar el proceso y **autorización expresa** del afiliado.
- **Subsanación: 10 días** (art. 45.3).
- **Admisión (art. 78.3):** el LAJ, apreciada la **jurisdicción y competencia objetiva**, admite la
  demanda; en otro caso da cuenta al órgano.

## 3. Bloque de admisibilidad — antes de redactar

Mismo control que en el ordinario. **No redactes hasta contestarlo:**

- **Plazo (art. 46):** **2 meses** acto expreso; **6 meses** acto presunto; **2 meses** desde la
  resolución expresa o presunta de la **reposición** (art. 46.4); **vía de hecho: 10 días** si hubo
  requerimiento del art. 30, **20 días** si no lo hubo (art. 46.3); **inactividad (art. 29): 2
  meses** desde el vencimiento; **lesividad: 2 meses**. **Dies a quo = fecha de notificación**:
  pídela. Son plazos de **CADUCIDAD**: **no los interrumpe** un burofax ni una reclamación
  extrajudicial (art. 69.e).
- **Agosto — art. 128.2 LJCA:** **no corre ningún plazo de la LJCA**, **salvo en el procedimiento de
  derechos fundamentales, donde agosto SÍ es hábil**. **No cites el art. 133 LEC.**
- **Acto impugnable (art. 25):** debe **poner fin a la vía administrativa**, ser definitivo o de
  **trámite cualificado** (decide el fondo, impide continuar, produce indefensión o perjuicio
  irreparable). Inactividad (art. 29) y vía de hecho (art. 30).
- **Legitimación (art. 19)**; **agotamiento de la vía**; **competencia objetiva (arts. 8-14)** —
  aquí, Juzgados.
- **Inadmisibilidad — art. 69:** a) falta de jurisdicción; b) persona incapaz, no debidamente
  representada o **no legitimada**; c) objeto no susceptible de impugnación; d) cosa juzgada o
  litispendencia; e) **escrito inicial fuera de plazo**.
- **Postulación — art. 23 LJCA** (no art. 23 LEC): ante **Juzgados**, procurador **potestativo**,
  abogado siempre; los **funcionarios** en defensa de sus derechos estatutarios pueden comparecer
  **por sí mismos**.

## 4. La decisión clave: ¿con vista o sin vista? — art. 78.3 (reforma LO 1/2025, vigente 3-4-2025)

### 4.1 Cauce por defecto: CON vista

Admitida la demanda, el LAJ acuerda su **traslado** a la persona demandada, **cita a las partes para
la vista** con día y hora, y **requiere a la Administración demandada que remita el expediente
administrativo en SOPORTE ELECTRÓNICO, con al menos QUINCE DÍAS de antelación** al término señalado
para la vista. Señalamiento conforme al **art. 182 LEC**.

- **Diligencias de preparación de la prueba:** si las solicitas **en la demanda**, el LAJ acordará lo
  necesario para posibilitar su práctica, **sin perjuicio de lo que el juez decida sobre su admisión
  en el acto del juicio**. **Pídelas en la demanda**: es el único momento útil.
- **Art. 78.4:** recibido el expediente, el LAJ **lo entrega al actor y a los personados** para que
  puedan hacer **alegaciones en el acto de la vista**. Léelo en cuanto llegue: es tu única ventana
  antes del juicio.

### 4.2 Cauce alternativo: SIN vista ni prueba, a instancia del actor

Si **el actor pide por OTROSÍ en su demanda** que el recurso se falle **sin recibimiento a prueba ni
vista**:

1. El LAJ da **traslado a las partes demandadas para que CONTESTEN en 20 DÍAS**, con el
   apercibimiento del **art. 54.1**.
2. **Dentro de los DIEZ PRIMEROS DÍAS** de ese plazo, **las demandadas pueden solicitar que se
   celebre la vista** — pero ya **no basta con pedirla**: deben **argumentar (i) en qué HECHOS existe
   disconformidad y (ii) qué MEDIOS DE PRUEBA, distintos de los ya obrantes en actuaciones, habrían
   de practicarse para despejar esa disconformidad**. Es la novedad central de la LO 1/2025: la vista
   pasa a ser **rogada y motivada**.
3. **El juez decide por AUTO:**
   - **Auto que ACUERDA la vista:** **NO es recurrible**. Notificado, el LAJ cita a las partes.
   - **Auto que RECHAZA la vista:** dispone además que **se conteste la demanda en el plazo que
     reste** y **cabe RECURSO DE REPOSICIÓN** contra él.
4. **Contestada la demanda:**
   - Si **no** se pidió vista: el LAJ procede conforme al **art. 57**, declarando **concluso** el
     pleito, salvo que el juez use la facultad del **art. 61**.
   - Si la vista se **rechazó** por auto: presentada la contestación, **se abre un trámite de
     CONCLUSIONES por plazo de CINCO DÍAS SUCESIVOS — pero SOLO si la parte actora lo hubiese
     SOLICITADO EN SU DEMANDA**. ⚠️ **Pídelo en la demanda**: si no lo pediste, **no hay
     conclusiones**. Es un olvido silencioso y sin remedio.

### 4.3 Cómo asesorar

- **Sin vista** conviene cuando la controversia es **puramente jurídica**, el expediente ya contiene
  todo y la vista solo añade coste y demora.
- **Con vista** conviene cuando hay **disconformidad en los hechos**, prueba que practicar o
  interrogatorio útil. En **sancionador**, recuerda el **art. 60.3**: habiendo disconformidad en los
  hechos, el proceso **se recibe siempre a prueba**.
- Si pides el fallo sin vista, **pide en el mismo otrosí el trámite de conclusiones** (art. 78.3 in
  fine). Cuesta una línea y te cubre.

## 5. La vista — arts. 78.5 a 78.19

| Ap. | Qué ocurre | Qué debes hacer |
|---|---|---|
| **78.5** | **Incomparecencia**: si no comparece el actor → **desistido y condenado en costas**. Si solo comparece el actor, prosigue en ausencia del demandado. | Advertirlo al cliente **por escrito**. |
| **78.6** | **Apertura**: el **demandante** expone los fundamentos de lo que pide o **ratifica** los de la demanda. | Es la apertura, **NO** las conclusiones. |
| **78.7-78.8** | **Cuestiones procesales**: el demandado alega jurisdicción, competencia y cuanto obste al fondo. Oído el demandante, el juez resuelve. | Si manda proseguir, **hacer constar en acta la disconformidad**. Sin protesta se compromete el recurso. |
| **78.9** | **Adecuación por cuantía** (§ 1). Decide el juez; **no cabe recurso alguno**. | — |
| **78.10** | **Fijación de hechos**; sin conformidad, se proponen y **practican seguidamente** las pruebas admitidas. | Llevar los puntos de hecho ya redactados. |
| **78.11** | Conformidad de los demandados, controversia **meramente jurídica**, sin prueba o toda inadmitida, **y sin conclusiones** → **sentencia sin más dilación** si nadie se opone. | Si no interesa, **oponerse en el acto**. |
| **78.12-78.16** | Prueba como en el ordinario en lo compatible (78.12). Interrogatorio **verbal, sin pliegos** (78.13). Testifical **sin escritos de preguntas/repreguntas**; el juez puede **limitar** testigos excesivos (78.14). Testigos **NO tachables** — observaciones **solo en conclusiones** (78.15). Pericial **sin insaculación** (78.16). | Preparar la vista **sin pliegos y sin tachas**. |
| **78.17** | Denegación de prueba, o admisión de prueba denunciada como obtenida **con violación de derechos fundamentales** → recurso **en el acto**, resuelto seguidamente. | **Interponerlo siempre**: sin él no hay queja después. |
| **78.18** | Prueba relevante impracticable **sin mala fe** → **suspensión** y reanudación señalada en el acto; si el LAJ no asistió, **día hábil siguiente**. | — |
| **78.19** | Tras la prueba **y, en su caso, las conclusiones**, oídos los Letrados, **las partes** pueden exponer de palabra su defensa con la venia. | — |

> **Dónde están realmente las conclusiones en el abreviado** (ninguna es el art. 78.6):
> **(i) orales**, en la vista — arts. 78.10, 78.11, 78.15 y 78.19; **(ii) escritas**, **5 días
> sucesivos**, solo si se rechazó la vista por auto **y el actor las pidió en la demanda** —
> art. 78.3 in fine. → skill `escrito-conclusiones-ca`.

## 6. Sentencia — art. 78.20 (LO 1/2025)

- Plazo: **10 días** desde la celebración de la vista.
- **Puede dictarse ORALMENTE al concluir la vista**, con los **requisitos de forma y consecuencias
  de los apartados 3 y 4 del art. 210 LEC**, pronunciando el fallo conforme a los **arts. 68 a 71
  LJCA**. Advierte al cliente: **puede salir de la vista con sentencia**.
- **Documentación:** la vista se documenta conforme al **art. 63.3 y 4** (art. 78.21); el art. 78.22
  regula el acta cuando fallan los medios de registro.
- **Art. 78.23:** en lo no previsto, rigen las normas generales de la Ley.

## 7. Redacción de la demanda del abreviado

Como la demanda ordinaria (skill `demanda-contencioso-administrativa`), con estas diferencias:

1. **Hechos** anclados al expediente **con folio** cuando ya se disponga de él; si no, a la
   documentación del cliente, **identificando qué habrá de acreditarse con el expediente**.
2. **Fundamentos:** procesales (competencia, legitimación, plazo, cuantía y **procedencia del
   abreviado**, citando el inciso del art. 78.1 que aplica — **materia o cuantía**) y de fondo:
   **nulidad (art. 47.1 LPAC, letra exacta)**, **anulabilidad y desviación de poder (art. 48.1)**,
   **defecto de forma solo con indefensión material (art. 48.2)**.
3. **SUPLICO — art. 31 LJCA**, las tres pretensiones cuando procedan: **anulación** (31.1);
   **reconocimiento de la situación jurídica individualizada** y medidas de pleno restablecimiento
   (31.2); **indemnización** con `[IMPORTE]` cuando proceda. Y costas (art. 139).
4. **OTROSÍES — aquí se juega el procedimiento:**
   - **Cuantía** (arts. 40-42) — con la advertencia de apelabilidad.
   - **Prueba (art. 60.1):** puntos de hecho y medios, **de forma ordenada**. En **sancionador**,
     invoca el **art. 60.3** (recibimiento a prueba **siempre** si hay disconformidad en los hechos).
   - **Diligencias de preparación** de la prueba a practicar en juicio (art. 78.3).
   - **Si procede: fallo SIN vista ni prueba** (art. 78.3) **+ solicitud del trámite de
     CONCLUSIONES** en el mismo otrosí.
   - **Medidas cautelares** (art. 129): pieza separada (art. 131), **periculum in mora** (art. 130.1),
     ponderación (art. 130.2); cautelarísima del art. 135 si hay especial urgencia.

## 8. Errores que pierden el asunto

- **Decir que el abreviado cubre «tráfico» por materia.** No lo cubre: entra **por cuantía**.
- **Pedir el fallo sin vista y olvidar solicitar las conclusiones** en la demanda (art. 78.3 in fine).
- **Creer que la demandada puede pedir vista sin motivar:** desde la LO 1/2025 debe **argumentar
  hechos discutidos y medios de prueba** necesarios.
- **Recurrir el auto que ACUERDA la vista:** no es recurrible. El recurrible (reposición) es el que
  la **rechaza**.
- **No comparecer a la vista:** desistimiento **y costas** (art. 78.5).
- **Llevar pliegos de preguntas** (78.13-78.14) o intentar **tachar testigos** (78.15).
- **No formular protesta en el acto** ante la denegación de prueba (78.17) o la desestimación de
  cuestiones procesales (78.8).
- **Olvidar el acuerdo corporativo del art. 45.2.d)** o los documentos del **art. 45.2.e)**.
- **Suplicar solo la anulación** sin reconocimiento de la situación jurídica ni indemnización
  (art. 31.2).
- **Fijar la cuantía a la baja** y perder la apelación (art. 81.1.a).

## 9. Cierre

- **Jurisprudencia:** verifica **antes de citar** con `buscar_sentencias` / `buscar_por_cita`.
  Prohibido inventar ECLI, ROJ, fechas o fundamentos.
- **Normativa autonómica y local:** el conector no la cubre. **Pídesela al usuario**; no la cites de
  memoria.
- **Protección de datos:** `[CLIENTE]`, `[ÓRGANO]`, `[FECHA]`, `[IMPORTE]`, `[EXPEDIENTE]`. Nunca
  reproduzcas datos de terceros ni datos de salud (art. 9 RGPD).
- **Nada de MASC:** es del orden civil.
- **Entregable:** Word `.docx` maquetado (skill `docx`). Aplica `estilo-escritos-judiciales`.
