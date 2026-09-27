---
name: delitos-leves
description: Juicio sobre delitos leves (arts. 962-977 LECrim) — juicio inmediato ante la Sección de Instrucción en funciones de guardia, juicio ordinario por delito leve, citación, celebración sin abogado, incomparecencia, sentencia y apelación en 5 días. Incluye el sobreseimiento por falta de interés público (art. 963.1.1.ª, que debe pedir el Fiscal), la prescripción de un año y la conversión de hurtos y estafas leves en menos graves por multirreincidencia (LO 1/2026). Actívala ante "delito leve", "juicio de faltas", "juicio inmediato", "hurto de menos de 400 euros", "me han citado por un delito leve", "juicio sin abogado", "sobreseimiento por escasa gravedad", "prescripción del delito leve", "multirreincidencia".
---

# Juicio sobre delitos leves — arts. 962 a 977 LECrim

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Procedimiento y plazos** (arts. 962-977 LECrim, apelación en 5 días) → `buscar_articulo` (`ley="LECrim"`).
- **Prescripción de un año y tipos reformados por la LO 1/2026** (arts. 131.1, 234.2 y 248 CP) → `buscar_articulo` (`ley="CP"`): indica la norma que dio la redacción vigente.
- **Criterio de la Audiencia que resolverá la apelación** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="AN"`, `tipo_organo="AP"`, `provincia` de la causa) + `leer_sentencias` con `parrafos=3`.
- **Multirreincidencia y ley más favorable** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`, `fecha_desde="10/04/2026"`).
- **Resoluciones que invoque el denunciante o el Fiscal** → `buscar_por_cita`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Procedimiento mínimo, plazos mínimos, atención mínima. **Es justo donde se pierden asuntos ganables**:
por prescripción no alegada, por sobreseimientos no pedidos, por acudir sin abogado y —desde el
**10-4-2026**— por no mirar los antecedentes antes de asumir que un hurto es leve.

> **Verifica cada precepto con `buscar_articulo` antes de citarlo.** Aquí va la *regla*, no el BOE.
> Anclas: `references/anclas-normativas-penal.md` §§ 3.3, 7 y 11 bis. Verificado el 2026-07-17.

> ⚠️ **Nomenclatura (art. 14 LECrim, vigente 3-10-2025).** El **conocimiento y fallo** de los delitos
> leves corresponde a la **Sección de Instrucción del Tribunal de Instancia** (**art. 14.1**), salvo que
> competa a las **Secciones de Violencia sobre la Mujer** (14.5.d) o **de Violencia contra la Infancia y
> la Adolescencia** (14.6) — § 6. Los arts. 962-977 **no fueron actualizados** y siguen diciendo
> «Juzgado de guardia»: al transcribirlos, reproduce el literal; en encabezamientos, usa la denominación
> vigente.

---

## 0. Las tres comprobaciones de apertura — en este orden

1. **¿PRESCRIBIÓ?** → § 4. **Un año.** Es la primera pregunta, siempre.
2. **¿SIGUE SIENDO LEVE?** → § 5. Desde el 10-4-2026 la multirreincidencia convierte hurtos y estafas
   leves en **menos graves**. **Pide los antecedentes antes de calificar nada.**
3. **¿CABE EL SOBRESEIMIENTO del 963.1.1.ª?** → § 3. La salida más eficiente y la menos usada.

Solo después discutas el fondo.

## 1. Qué es un delito leve

- **Art. 13.3 CP:** infracciones que la ley castiga con **pena leve**.
- **Art. 13.4 CP:** si la pena, por su extensión, puede considerarse **leve y menos grave**, el delito se
  considera **en todo caso LEVE**. *(Regla de arrastre favorable — verifícala en cada tipo.)*
- Sustituyeron a las **faltas** (suprimidas por la LO 1/2015, 1-7-2015). ⚠️ **«Juicio de faltas» es
  terminología derogada.** El cliente lo llamará así; el escrito, no.

---

## 2. Los dos cauces

> ### 📌 Nomenclatura en este bloque — leer antes de copiar nada
>
> Los **arts. 962 a 965 LECrim** conservan en su redacción **vigente** (LO 1/2015) los rótulos
> «**Juzgado de Instrucción**», «**Juzgado de Violencia sobre la Mujer**» y «**Juzgado de guardia**».
> La LO 1/2025 reformó el **art. 14** LECrim, pero **no tocó estos preceptos**. *(Verificado
> literalmente el 2026-07-17.)*
>
> - **Al citar o parafrasear los arts. 962-965 se transcriben tal cual.** No se reescribe la ley.
> - **Al encabezar un escrito**, en cambio, se usa la denominación **vigente**: **Sección de
>   Instrucción del Tribunal de Instancia** (art. 14.1 y 14.2) — y **mejor aún, la que figure en la
>   citación o en la carátula del procedimiento**.
> - La **DA 1.ª de la LO 1/2025** cierra el círculo: las referencias legales a los «Juzgados de
>   Instrucción / de Violencia sobre la Mujer» **se entienden hechas a las Secciones** de los
>   Tribunales de Instancia. No hay contradicción: hay dos registros distintos.

### Cauce A — JUICIO INMEDIATO ante el juzgado de guardia (arts. 962-964)

**Art. 962.1 — supuesto tasado.** Cuando la Policía Judicial tenga noticia de un delito leve de
**lesiones o maltrato de obra, hurto flagrante, amenazas, coacciones o injurias**, y el enjuiciamiento
corresponda al juzgado al que se entrega el atestado o a otro del mismo partido, **cita de forma
inmediata** ante el Juzgado de Guardia a ofendidos y perjudicados, denunciante, denunciado y testigos,
**apercibiéndoles** de las consecuencias de no comparecer, de que **el juicio puede celebrarse aunque no
comparezcan**, y de que han de **comparecer con los medios de prueba**. Se informa de derechos (arts. 109,
110 y 967) y se piden correo y teléfono.

- **962.2:** al denunciado se le informa **sucintamente de los hechos** y del **derecho a comparecer
  asistido de abogado**. ⭐ **«Dicha información se practicará en todo caso POR ESCRITO.»** *(Si no consta
  por escrito en el atestado, hazlo constar y alega lo que proceda.)*
- **962.5:** si la competencia es de la **Sección de Violencia sobre la Mujer**, las citaciones se hacen
  ante **ese órgano** y en el **día hábil más próximo** (§ 6).

**Art. 964 — supuestos NO contemplados por el 962.** La Policía forma atestado inmediato y lo remite sin
dilación (salvo los exceptuados del **art. 284**), con el **ofrecimiento de acciones**. Recibido — **y en
todos los casos iniciados por denuncia presentada directamente por el ofendido ante el órgano judicial**
— el juez puede: **a)** **sobreseer** conforme al **963.1.1.ª** (§ 3); o **b)** **celebrar el juicio de
forma inmediata** si el denunciado está identificado, cabe citar a todos **mientras dure la guardia** y
concurren los requisitos del 963. **964.3:** se cita al **Fiscal** —**salvo delito leve perseguible solo a
instancia de parte**—, al denunciante, al denunciado y a testigos y peritos.

**Art. 963 — resolución:** **963.1.2.ª** celebración inmediata si comparecieron los citados, o aunque
alguno falte si reputa **innecesaria su presencia**, teniendo en cuenta si resultará **imposible practicar
algún medio de prueba imprescindible**. **963.2:** el asunto debe corresponder al juzgado de guardia por
**competencia y reparto**.

### Cauce B — JUICIO ORDINARIO por delito leve (arts. 965-971)

**Art. 965.1:** si **no es posible** celebrar durante la guardia: **1.ª** si la competencia es del propio
juzgado **y no procede el sobreseimiento del 963.1.1.ª**, el LAJ señala y cita para el **día hábil más
próximo posible** y **en cualquier caso en plazo no superior a 7 días**; **2.ª** si es de otro juzgado, le
remite lo actuado para que señale igual.

> ⭐ **Nótese el inciso del 965.1.1.ª: el legislador obliga al juez a plantearse el sobreseimiento del
> 963.1.1.ª ANTES de señalar.** Es la palanca para pedirlo por escrito al recibir la citación.

---

## 3. ⭐ Art. 963.1.1.ª — sobreseimiento por falta de interés público

**La salida más eficiente, y la más desaprovechada.** El juez **acordará el sobreseimiento y el archivo
cuando lo solicite el Ministerio Fiscal** a la vista de:
- **a)** que el delito leve resulte **de muy escasa gravedad** a la vista de la **naturaleza del hecho**,
  **sus circunstancias** y **las personales del autor**; **y**
- **b)** que **no exista interés público relevante** en la persecución.
  - ⭐ **En delitos leves PATRIMONIALES** se entiende que **no existe interés público relevante** cuando
    **se hubiere procedido a la reparación del daño** **y** **no exista denuncia del perjudicado**.

Se comunica **inmediatamente la suspensión del juicio** a todos los citados y se **notifica a los
ofendidos**.

> 🚨 **El requisito que casi todos pasan por alto: «cuando lo SOLICITE el Ministerio Fiscal».** El juez
> **no puede acordarlo de oficio** por esta vía. **Tu interlocutor es el Fiscal, no el juez.** Un escrito
> dirigido solo al juzgado está mal dirigido y se desestimará.

**Estrategia de la defensa, en orden:**
1. **Repara el daño ANTES** y documéntalo (transferencia, recibo, acta de entrega). En patrimoniales es
   la mitad del requisito b) y **es lo único que controlas**.
2. **Consigue que el perjudicado no denuncie** o retire la denuncia: la ley exige que **no exista
   denuncia del perjudicado**. *(Nada de MASC: es del orden civil. Aquí es reparación voluntaria y
   acreditada.)*
3. **Dirige la petición al Fiscal**, motivando **a) muy escasa gravedad** —naturaleza, circunstancias y
   **circunstancias personales del autor**— **y b) ausencia de interés público**, con la reparación como
   argumento nuclear.
4. **Preséntalo al recibir la citación, no el día del juicio** (art. 965.1.1.ª).
5. Cauces: **963.1.1.ª** (guardia) y **964.2.a)** (atestado recibido o denuncia directa del ofendido).

> **Dato conexo — art. 969.2:** el FGE imparte instrucciones sobre los supuestos en que, **en atención al
> interés público**, los fiscales **pueden dejar de asistir al juicio y de emitir los informes de los
> arts. 963.1 y 964.2** cuando la persecución exija denuncia del ofendido. Consulta la instrucción de la
> FGE aplicable `[verificar]` antes de construir la expectativa del cliente.

---

## 4. ⭐ Prescripción: UN AÑO — art. 131.1 CP

> «A los cinco, los demás delitos, **excepto los delitos leves y los delitos de injurias y calumnias, que
> prescriben al año**.»

**Es cortísima y decide muchos asuntos.** Con un procedimiento que se señala «en el día hábil más
próximo» pero que en la práctica se demora, **el año se consume solo**.

- **131.2:** pena compuesta → la que exija **mayor** tiempo. **131.4:** concurso o infracciones conexas →
  plazo del **delito más grave**. ← **Cuidado:** un delito leve conexo con uno menos grave **no prescribe
  al año**.
- **Operativo:** calcula la prescripción **el día que abres el asunto**. Cuenta desde **la fecha de los
  hechos** (no la de la denuncia) y comprueba **cada acto de interrupción** `[verificar el art. 132 CP con
  buscar_articulo antes de aplicarlo — tiene reglas propias que esta skill no da por supuestas; ver
  también anclas sobre la denuncia, que NO interrumpe por sí sola]`.
- **Acusación:** si el plazo aprieta, **impulsa**. **Defensa:** cuenta, espera y alega como cuestión
  previa y en informe.
- ⚠️ **Interacción con el § 5:** si la multirreincidencia convierte el hurto leve en **menos grave**, la
  prescripción **pasa de 1 año a 5** (131.1, «los demás delitos»). **El cambio de calificación arrastra el
  plazo.**

---

## 5. ⭐ LO 1/2026 (vigente 10-4-2026) — la multirreincidencia convierte delitos leves en MENOS GRAVES

**El cambio más importante de la materia en años.**

### 5.1 Hurto — art. 234.2 CP (literal verificado)

> «Se impondrá la pena de **multa de uno a tres meses** si la cuantía de lo sustraído **no excediese de
> 400 euros**, salvo si concurriere alguna de las circunstancias del artículo 235. **No obstante, en el
> caso de que el culpable hubiera sido condenado ejecutoriamente al menos por TRES delitos de la misma
> naturaleza, comprendidos en este Título, y siendo al menos UNO de ellos LEVE, se impondrá la pena
> prevista en el apartado 1 de este artículo.** No se tendrán en cuenta los antecedentes penales
> cancelados o que debieran serlo.»

**Pena del 234.1: prisión de 6 a 18 meses → deja de ser delito leve.** Cambian procedimiento, competencia,
prescripción y necesidad de abogado y procurador. Requisitos acumulativos: **tres** condenas
**ejecutorias**, **de la misma naturaleza**, del **mismo Título** (XIII, patrimonio), **al menos una
leve**, y antecedentes **no cancelados ni cancelables**.

### 5.2 Estafa — art. 248 párr. 3 CP

Misma regla **en el ámbito del CAPÍTULO**: ≤400 € → multa de 1 a 3 meses, salvo circunstancias del
art. 250; **no obstante**, tres condenas ejecutorias de la misma naturaleza **del capítulo**, **al menos
una leve** → **pena del párrafo segundo** (prisión de 6 meses a 3 años).

> ⚠️ **Matiz verificado:** en el hurto el perímetro es el **TÍTULO**; en la estafa, el **CAPÍTULO**. No
> son intercambiables. Comprueba dónde encajan los antecedentes concretos.

### 5.3 Los antecedentes por delitos leves ahora COMPUTAN

- **Art. 22.8.ª:** no se computan los cancelados ni los de delitos leves, **«salvo lo dispuesto para los
  tipos agravados por multirreincidencia de delitos leves»**.
- **Art. 66.2:** en delitos leves e imprudentes rige el **prudente arbitrio**, **con la misma salvedad**.
- **Art. 80.2.1.ª:** no se tienen en cuenta las condenas por delitos leves **«salvo que estos integren un
  tipo agravado por multirreincidencia»**. Ver anclas § 6.

### 5.4 ⭐ Protocolo obligatorio

> **Ante un hurto o una estafa de ≤400 €, COMPRUEBA SIEMPRE LOS ANTECEDENTES antes de asumir que es un
> delito leve.**

Si concurren tres condenas ejecutorias del Título (hurto) o del capítulo (estafa) con al menos una leve,
el asunto **ya no es un delito leve**: no va por los arts. 962 y ss. sino por **abreviado** —o **juicio
rápido**, pues el hurto está en el catálogo del 795.1.2.º b)—; **exige abogado y procurador**; la
**prescripción pasa de 1 a 5 años**; la pena pasa de **multa de 1-3 meses** a **prisión**; y el **art. 80
CP** se complica, porque esos antecedentes leves **ya computan**.

En la guardia lo detecta el **art. 797.1.1.ª** (antecedentes por el medio más rápido). **Pídelos tú
también.** Un cliente que dice «es una tontería, son 60 euros» puede estar ante prisión.

### 5.5 ⭐ Derecho transitorio — es DESFAVORABLE

- **Art. 2.1 CP:** **NO se aplica a hechos anteriores al 10-4-2026.**
- **Art. 2.2 CP:** solo retroactividad **favorable**. Convertir el leve en menos grave **no favorece** →
  **irretroactividad plena**.
- **DT de la LO 1/2026** (anclas § 7.3): los delitos cometidos **hasta** su entrada en vigor se juzgan
  conforme a la ley **del tiempo de su comisión**, salvo que la nueva sea **más favorable**.

**Operativo:**
1. **Fija la fecha de los hechos.** Decide ella, no la de la denuncia ni la del juicio.
2. **Hechos anteriores al 10-4-2026** → **redacción anterior**: el hurto de ≤400 € es **leve** aunque haya
   tres condenas previas. **Alega la irretroactividad si la acusación pretende aplicar el nuevo 234.2.**
   Motivo de recurso sólido, y va a ocurrir.
3. **Antecedentes cancelados o cancelables: NO computan nunca.** **Pide la cancelación (art. 136 CP) antes
   de que sea tarde**: es la defensa estructural frente a la multirreincidencia.
4. Si la ley aplicable es dudosa, **haz la comparación de penas por escrito** y pide la más favorable.

---

## 6. Competencia — quién falla el delito leve (art. 14 LECrim)

| Órgano | Cuándo |
|---|---|
| **Sección de Instrucción** del Tribunal de Instancia | **Regla general** (art. 14.1) |
| **Sección de Violencia sobre la Mujer** | Delitos leves que la ley le atribuya **cuando la víctima** sea de las personas del **art. 14.5.a)** (**14.5.d**). Citación en el **día hábil más próximo** (962.5) |
| ⭐ **Sección de Violencia contra la Infancia y la Adolescencia** | **ÓRGANO NUEVO** — delitos leves **cuando la víctima sea niño, niña o adolescente** (**art. 14.6**) |

> **⭐ Art. 14.7 — regla de conflicto:** si los hechos pueden ser conocidos por la Sección de Violencia
> contra la Infancia **y** por la de Violencia sobre la Mujer, la competencia es **en todo caso de la
> segunda**. **Compruébalo siempre que haya menores implicados.**

**⭐ Art. 105.3 LECrim (LO 1/2026) — acción penal de las entidades locales por HURTO.** «Las **entidades
locales podrán ejercer la acción penal** por los delitos de hurto» del capítulo I del título XIII del
libro II CP. Legitimación nueva, de rango ordinario (DF 3.ª), y directamente relevante aquí porque el
grueso del hurto es leve. **Impacto:** un ayuntamiento personado dificulta negar el **interés público
relevante** del 963.1.1.ª, y —si el asunto fuera por juicio rápido— **elimina la conformidad del art. 801**
(801.1.1.º exige que **no** haya acusación particular), dejando solo el 801.5. **Comprueba siempre quién
está personado.**

---

## 7. Citación, abogado y celebración

### ⭐ Art. 967.1 — la asistencia letrada NO es preceptiva… salvo un caso

> «…**se les informará de que pueden ser asistidos por abogado SI LO DESEAN** y de que deberán acudir al
> juicio **con los medios de prueba** de que intenten valerse. […] Sin perjuicio de lo dispuesto en el
> párrafo anterior, **para el enjuiciamiento de delitos leves que lleven aparejada pena de multa cuyo
> límite máximo sea de AL MENOS SEIS MESES, se aplicarán las reglas generales de defensa y
> representación**.»

- **Regla general:** el juicio **puede celebrarse sin abogado**. La asistencia es un **derecho**, no un
  requisito.
- **⭐ Excepción verificada:** multa con **máximo ≥ 6 meses** → **reglas generales** = **abogado y
  procurador preceptivos**. Comprueba la pena del tipo concreto.
  > Cálculo: **hurto leve** (234.2) y **estafa leve** (248 párr. 3) llevan multa de **1-3 meses** → por
  > debajo del umbral → **no preceptiva**. Pero **si la multirreincidencia los convierte en menos graves
  > (§ 5), rigen las reglas generales por la vía ordinaria.**

> 🚨 **ADVERTENCIA AL CLIENTE — dilo siempre y por escrito.** Que la ley **permita** ir sin abogado no
> significa que sea prudente:
> - El juicio **se celebra aunque no comparezca** (art. 971) y **condena en ausencia**.
> - Hay que **acudir con los medios de prueba** (967.1): quien va solo casi nunca los lleva, y **no hay
>   segunda oportunidad** —la apelación no es un juicio nuevo—.
> - La **declaración del denunciante tiene valor de acusación** aunque el Fiscal no asista (969.2).
> - Se generan **antecedentes penales** que, desde el 10-4-2026, **computan** para convertir futuros
>   hurtos o estafas leves en **menos graves** (§ 5) y afectan a la suspensión (80.2.1.ª).
> - La condena por delito leve **puede llevar prohibiciones del art. 48 CP** (**art. 57.3 CP**).
>
> **Un delito leve de hoy es la multirreincidencia de mañana.** Ese es el argumento que el cliente
> entiende.

- **967.2:** partes, testigos y peritos que **no comparezcan ni aleguen justa causa** → **multa de 200 a
  2.000 €**.
- **⭐ Art. 970:** si el **denunciado reside fuera de la demarcación**, **no tiene obligación de concurrir**:
  puede dirigir **escrito alegando lo que estime conveniente en su defensa** y **apoderar a abogado o
  procurador** para que presente en el acto las alegaciones y **las pruebas de descargo**. *(Vía útil y
  poco usada — pero el escrito debe llevar la prueba.)*

### Art. 971 — incomparecencia del acusado

> «La **ausencia injustificada del acusado NO suspenderá** la celebración ni la resolución del juicio,
> siempre que conste habérsele **citado con las formalidades prescritas** en esta Ley, **a no ser que el
> Juez, de oficio o a instancia de parte, crea necesaria la declaración de aquél**.»

- **Defensa:** la única palanca es el **defecto de citación** — el motivo de nulidad más frecuente y
  rentable aquí. Y si conviene, **pide que se declare necesaria su declaración** para forzar la suspensión.
- **Acusación:** asegura que la citación conste con **todas las formalidades**. Un defecto tumba la
  sentencia en apelación.

### Art. 969 — celebración

**969.1:** juicio **público**. Orden: lectura de querella o denuncia → **prueba de la acusación** →
**se oye al acusado** → **testigos de descargo** y demás prueba pertinente → informes orales: **Fiscal**
(si asiste), **querellante o denunciante**, y **por último el acusado**. La querella ha de reunir los
requisitos del **art. 277**, **salvo firma de abogado y procurador**.

**⭐ 969.2:** el Fiscal asiste **siempre que sea citado**, pero el FGE puede instruir que no asista cuando
la persecución exija denuncia del ofendido. **En esos casos, la declaración del denunciante afirmando los
hechos TIENE VALOR DE ACUSACIÓN, aunque no los califique ni señale pena.**
> **Defensa: no esperes que la ausencia del Fiscal deje el asunto sin acusación. No la deja.**

### Art. 973 — sentencia

**973.1:** sentencia **en el acto de finalizar el juicio** y, de no ser posible, **dentro de los 3 días**,
apreciando **según su conciencia** las pruebas. Si usa el **libre arbitrio** que el CP le otorga, **deberá
expresar si ha tomado en consideración los elementos de juicio que el precepto aplicable obligue a tener en
cuenta**.
> **Motivo de apelación:** deber de **motivación reforzada** cuando el juez usa el arbitrio del **art. 66.2
> CP**. Su omisión es alegable — y ojo: tras la LO 1/2026 ese arbitrio tiene la salvedad de los tipos
> agravados por multirreincidencia (§ 5.3).

**973.2:** se notifica a **ofendidos y perjudicados aunque no sean parte**, haciendo constar **recursos,
plazo y órgano**.

---

## 8. Recursos

**⭐ Art. 976 — apelación: CINCO DÍAS.** «La sentencia es apelable en el plazo de los **cinco días**
siguientes al de su notificación.» Durante ese período las actuaciones están **en secretaría a disposición
de las partes**. Se formaliza y tramita conforme a los **arts. 790 a 792**. La sentencia de apelación se
notifica a ofendidos y perjudicados aunque no sean parte.

> 🚨 **NO son los 10 días del art. 790.1. Son 5** — igual que en juicio rápido (803.1.1.ª) y por la misma
> razón. A la agenda el día de la notificación.

**Art. 977 — segunda instancia:** «**Contra la sentencia que se dicte en segunda instancia no habrá lugar a
recurso alguno.**»
- **No hay casación.** La apelación es **la única y última oportunidad**. Trabájala como si lo fuera,
  porque lo es.
- Queda, en su caso, el **incidente de nulidad de actuaciones** y el amparo `[verificar los requisitos del
  art. 241 LOPJ antes de intentarlo]`.

---

## Errores típicos

| Error | Corrección verificada |
|---|---|
| «Juicio de faltas» | Terminología **derogada** (LO 1/2015). Son **delitos leves** |
| «Juzgado de Instrucción» en el encabezamiento | **Sección de Instrucción** del **Tribunal de Instancia** (art. 14.1, vigente 3-10-2025) |
| Ignorar la **Sección de Violencia contra la Infancia** | **Órgano nuevo** (14.6): falla delitos leves **con víctima menor**. Si concurre con la de la Mujer, **gana esta** (**14.7**) |
| Apelar en **10 días** | **5 días** (art. 976.1). Fuera de plazo = firmeza |
| Contar con la **casación** | **No existe**: art. 977 |
| Pedir el archivo del 963.1.1.ª **al juez** | Lo **debe solicitar el Ministerio Fiscal**. Dirige la petición al **Fiscal** |
| Pedir el sobreseimiento **el día del juicio** | El **965.1.1.ª** obliga a valorarlo **antes de señalar**. Preséntalo con la citación |
| Asumir que un hurto de ≤400 € es leve | **Comprueba los antecedentes**: el **234.2** puede convertirlo en **menos grave** |
| Aplicar el nuevo 234.2 a hechos **anteriores al 10-4-2026** | **Irretroactividad**: es **desfavorable** (art. 2.1 y 2.2 CP) |
| Confundir los perímetros de la multirreincidencia | Hurto: **Título**. Estafa: **capítulo** |
| «El delito leve prescribe al año» sin más | Cierto (131.1) — **pero** el concurso o conexidad arrastra al **delito más grave** (131.4), y si pasa a menos grave, **5 años** |
| «No hace falta abogado» sin comprobar la pena | **967.1 párr. 2:** multa con máximo **≥ 6 meses** → **reglas generales** |
| Dejar ir al cliente solo «porque se puede» | Se **puede**, pero se condena en ausencia (971), sin prueba, y el antecedente **computa** desde el 10-4-2026 |
| Creer que sin Fiscal no hay acusación | **969.2:** la declaración del denunciante **tiene valor de acusación** |
| Ignorar al **ayuntamiento** personado | **Art. 105.3 LECrim**: las entidades locales pueden ejercer la acción penal por **hurto** |

## Reglas de trabajo

- **`buscar_articulo` antes de citar.** Anclas: `references/anclas-normativas-penal.md` §§ 3.3, 7 y 11 bis.
  **Prohibido inventar** penas, plazos u ordinales → `[verificar]` y dilo.
- **Jurisprudencia solo vía `jurisprudenciator`.** **Prohibido citar ECLI, ROJ, fechas o ponentes de
  memoria.**
- **Ley penal en el tiempo: aquí es el eje del asunto.** Fija la **fecha de los hechos**, identifica la
  redacción vigente entonces (art. 2 CP) y comprueba si la posterior es **más favorable** (art. 2.2 CP). La
  **LO 1/2026 es desfavorable** en multirreincidencia: **no se aplica hacia atrás**.
- **Nomenclatura:** **Secciones de los Tribunales de Instancia**, **LAJ**. Al transcribir los arts.
  962-977, reproduce el literal y advierte del desajuste.
- **Instruye el Juez de Instrucción.** **No existe el «fiscal instructor»** en Derecho vigente.
- **Nada de MASC:** requisito del orden **civil**. Aquí lo relevante es la **reparación del daño** del
  963.1.1.ª b) y la **ausencia de denuncia del perjudicado**.
- **Anonimización:** `[INVESTIGADO]`, `[DENUNCIANTE]`, `[VÍCTIMA]`, `[TESTIGO]`. Esta skill maneja
  **antecedentes penales** constantemente: **categoría especial (art. 10 RGPD)**, máxima cautela, **cero
  datos reales**. Ver `PROTECCION-DATOS.md`.
- Config del despacho: `~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.

## Entrega

Word `.docx` (skill `docx`): **escrito al Ministerio Fiscal** interesando el sobreseimiento del **963.1.1.ª**
(con la reparación acreditada); **escrito de alegaciones del art. 970**; **recurso de apelación del art. 976**
(¡5 días!); o **nota de calificación** con el protocolo del § 5 (fecha de los hechos, antecedentes, ley
aplicable y comparación de penas).
