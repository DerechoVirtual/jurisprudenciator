---
name: ejecucion-penal-liquidacion-condena-suspension-catalogo
description: >-
  Catálogo (sin plantilla). Redacta escritos de ejecución penal: solicitud de suspensión de la ejecución de la pena privativa de libertad (art. 80 CP, reformado por la LO 1/2026), liquidación de condena, abono de la prisión provisional (art. 58 CP), refundición/acumulación (art. 988 LECrim y 76 CP), expulsión (art. 89 CP) y oposición a la revocación (art. 86 CP). Actívala ante "solicitar la suspensión de la pena", "art. 80 CP", "liquidación de condena", "abono de prisión preventiva", "refundición de condenas", "acumulación jurídica", "expulsión sustitutiva", "revocación de la suspensión", "revisión de condena por ley más favorable", o "ejecutoria penal".
---

# Ejecución penal: suspensión, liquidación y revisión (catálogo — sin plantilla)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Suspensión, revocación, abono, refundición y expulsión** → `buscar_articulo` (`ley="CP"`, arts. 58, 76, 80-86 y 89; `ley="LECrim"`, art. 988).
- **Revisión por ley más favorable tras la LO 1/2026 (art. 80.2.1.ª CP)** → `buscar_articulo` (`ley="CP"`, `articulo="80"`) y `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`, `fecha_desde="10/04/2026"`).
- **Doctrina sobre acumulación de condenas, abono de la preventiva y revocación** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"`; y `base="AN"`, `tipo_organo="AP"` para la Audiencia de la ejecutoria) + `leer_sentencias` con `parrafos=3`.
- **Expulsión sustitutiva de ciudadanos de la UE o residentes de larga duración** → `buscar_sentencias` (`base="TJUE"`).
- **Indulto concedido o requisitoria publicada en la ejecutoria** → `novedades_boe` (por órgano o número de ejecutoria, no por el nombre del penado) → `leer_boe`.
- **Revisar las citas del escrito antes de presentarlo** → `verificar_escrito` (pasa el texto completo).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Escritos de la fase de ejecución. **La LO 1/2026 (vigente 10-4-2026) reescribió el art. 80 CP**: cualquier
material anterior está obsoleto. Anclas: `references/anclas-normativas-penal.md` (§ 6). Perfil:
`~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/`.

## 1. Comprobaciones previas

1. **Órgano**: el **sentenciador** (ejecutoria nº). El **abono de prisión provisional en causa distinta** →
   **Juez de Vigilancia Penitenciaria** (58.2). La **refundición** → el que dictó la **última sentencia**
   (988). ⚠️ Encabezamientos con la nomenclatura de la **LO 1/2025** (DF 38.3, desde 3-10-2025; art. 14
   LECrim): **Sección de lo Penal del Tribunal de Instancia**, no «Juzgado de lo Penal».
2. **Firmeza** (988 párr. 1): la declara el órgano que dictó la sentencia (art. 141 LECrim). Sin firmeza no
   hay ejecución. **Momento (82.1):** el juez resuelve sobre la suspensión **en sentencia siempre que
   resulte posible**; si no, declarada la firmeza, **con la mayor urgencia y previa audiencia a las
   partes**. → **Pídela ya en el juicio** cuando quepa (en conformidad, el art. 785.9 prevé el
   pronunciamiento en el acto).
3. **Prescripción de la PENA** (art. 133 — anclas § 3.4). En ejecución prescribe **la pena**, no el delito,
   y su cómputo es **propio** (art. 134 CP — **verifícalo con `buscar_articulo`**): **no** le aplica la
   suspensión por querella o denuncia del **132.2.2.ª**, que rige la prescripción **del delito**. No los
   mezcles. Una ejecutoria dormida puede estar prescrita.
4. **Días inhábiles para recursos (art. 183 LOPJ, LO 14/2022):** **agosto** y **24-dic a 6-ene**, salvo
   actuaciones urgentes. Margen de la casa: **2 días hábiles** de antelación.
5. ⭐ **Ley penal más favorable — art. 2.2 CP (aquí es obligatorio):** efecto retroactivo **AUNQUE hubiera
   recaído sentencia firme y el sujeto estuviese cumpliendo condena**; **en caso de duda, SERÁ OÍDO EL
   REO**. Ver § 2. **Marcadores**: `[PENADO]`, `[VÍCTIMA]`, `[DATO]`.

## 2. ⭐ REVISIÓN DE CONDENAS por la LO 1/2026 (art. 2.2 CP) — hazlo por sistema

Con la **LO 1/2026 vigente desde el 10-4-2026**, **revisa toda ejecutoria con hechos anteriores** a esa
fecha. Su **disposición transitoria**: los hechos anteriores se juzgan conforme a la ley del momento de
comisión, **pero se aplica la LO 1/2026 si es más favorable** (art. 2.2 CP).

**Dónde puede haber pena menor (anclas § 7.1):** **80.2.1.ª** (nuevos supuestos que **no computan** como
antecedente → puede abrir la suspensión a quien la tenía cerrada, § 3.2); **22.8.ª y 66.2** (reincidencia
y delitos leves); **248** estafa reescrita (**prisión 6 meses-3 años**; **≤ 400 € → multa 1-3 meses**);
**234.2** hurto leve (**≤ 400 € → multa 1-3 meses**); **235.1.4.º** (**> 400 €**); **250** (umbrales
**> 50.000 €** y **> 250.000 €**).

⚠️ **Pero la LO 1/2026 también AGRAVA**: multirreincidencia de delitos leves, nuevo **235.1.10.º**
(móviles), **255.3**, **568.2**. La comparación es **global y por bloques**: se aplica **una ley entera**.
**No se pueden combinar preceptos de ambas redacciones.** **Operativo:** compara la pena de ambas
redacciones, en concreto y con números, para **este** penado. Si la vigente es más favorable → **pide la
revisión**. Si hay **duda**, invoca el 2.2 in fine: **el reo debe ser oído**. Verifica **siempre** la
redacción aplicable con `buscar_articulo`.

## 3. ⚠️ Suspensión — art. 80 CP (redacción **LO 1/2026**, vigente 10-4-2026)

### 3.1 Regla general (80.1)
Penas privativas de libertad **≤ 2 años**, por **resolución motivada**, **cuando sea razonable esperar que
la ejecución no sea necesaria para evitar la comisión futura de nuevos delitos**. Se valoran:
circunstancias del delito y personales, **antecedentes**, conducta posterior —**en particular el esfuerzo
para reparar el daño**—, circunstancias familiares y sociales, y efectos esperables de la suspensión.
> El eje es la **prognosis**: no es merecimiento, sino **necesidad preventiva**. Construye el escrito sobre
> eso, con documentos (arraigo, empleo, tratamiento, reparación).

### 3.2 Condiciones necesarias (80.2)

**1.ª Haber delinquido POR PRIMERA VEZ.** No se computan: condenas por delitos **imprudentes**; por **delitos
leves** ⭐ **salvo que integren un tipo agravado por multirreincidencia de delitos leves** (**novedad 2026**:
los leves ya no son siempre inocuos); ni antecedentes **cancelados o que debieran serlo** (art. 136). Y,
literal:

> ⭐⭐ «**Tampoco se tendrán en cuenta los antecedentes penales correspondientes a delitos que, POR SU
> NATURALEZA O CIRCUNSTANCIAS, CAREZCAN DE RELEVANCIA PARA VALORAR LA PROBABILIDAD DE COMISIÓN DE
> DELITOS FUTUROS.**»

**Cómo alegarla — la baza nueva.** Antes, un antecedente vivo por delito doloso cerraba el 80.2.1.ª casi
mecánicamente. **Ya no**: la ley introduce un **juicio material de relevancia preventiva** — el antecedente
solo cuenta **si dice algo sobre la probabilidad de que este penado reincida**.
1. **Identifica** el antecedente que opondrá el Fiscal (fecha, tipo, pena, ejecutoria).
2. **Irrelevancia por NATURALEZA**: heterogeneidad radical con el delito actual (bien jurídico, dinámica
   comisiva, motivación) — un antecedente de seguridad vial nada dice sobre un delito patrimonial. La ley
   pide relación con **delitos futuros**, no un registro.
3. **Irrelevancia por CIRCUNSTANCIAS**: antigüedad (aunque no esté cancelado), contexto superado
   (dependencia hoy tratada, precariedad resuelta), carácter aislado, cambio vital acreditado.
4. **Documenta** (hoja histórico-penal, certificado de deshabituación, contrato, informes sociales): es un
   **juicio**, y un juicio necesita prueba. **Encadénala con el 80.1** — si el antecedente carece de
   relevancia para valorar delitos futuros, **entonces** es razonable esperar que la ejecución no sea
   necesaria. Y **pide en subsidio el 80.3** (que no exige la 1.ª).
> ⚠️ Redacción **nueva**: sin cuerpo jurisprudencial consolidado. **Verifica el estado de la interpretación
> con `buscar_sentencias`** y, si no hay doctrina, **dilo**: el texto legal basta.

**2.ª** Que la pena **o la suma** **no supere 2 años**, **sin incluir la derivada del impago de multa**.

**3.ª (ampliada en 2026)** Satisfechas las **responsabilidades civiles** ⭐ **y hecho efectivo el DECOMISO**
del art. 127. **Se cumple con el COMPROMISO** de satisfacerlas **conforme a su capacidad económica** y de
**facilitar el decomiso**, si es razonable esperar cumplimiento en el **plazo prudencial** fijado. ⭐ El
juez, atendido el alcance de la responsabilidad civil y el **impacto social del delito**, **puede pedir
GARANTÍAS**.
> **Operativo:** el compromiso sigue siendo la vía del insolvente, pero **ahora alcanza al decomiso**.
> Formúlalo **por escrito, cuantificado y calendarizado**, con capacidad económica acreditada. **Ofrece tú**
> las garantías si son asumibles. Ojo al **86.1.d**: incumplirlo es causa de revocación **salvo falta de
> capacidad económica**.

### 3.3 Modalidades especiales — cuando no concurren las condiciones

| Vía | Requisitos | A cambio |
|---|---|---|
| **80.3 excepcional** | Sin las condiciones **1.ª y 2.ª**, y **siempre que NO sea reo habitual**; penas que **individualmente** no excedan de **2 años**; atendidas circunstancias personales, naturaleza del hecho, conducta y **esfuerzo reparador** | **Siempre** condicionada a **reparación efectiva** conforme a sus posibilidades, o al **acuerdo de mediación** (84.1.ª). **Y siempre** una de las medidas **84.2.ª o 3.ª**, con extensión **no inferior** a la conversión sobre **1/5 de la pena** |
| **80.4 enfermedad** | **Enfermedad muy grave con padecimientos incurables** | ⭐ **CUALQUIER pena**, **sin sujeción a requisito alguno** — salvo que al delinquir ya tuviera otra pena suspendida por el mismo motivo. Sin límite de 2 años, sin primariedad, sin responsabilidad civil |
| **80.5 dependencia** | Sin las condiciones **1.ª y 2.ª**: penas **≤ 5 AÑOS** de quien **cometió el hecho a causa de su dependencia** de las sustancias del **art. 20.2.º**, con **certificación** de centro **acreditado u homologado** de estar **deshabituado o en tratamiento** | **No abandonar el tratamiento**. ⭐ **«No se entenderán abandono las recaídas en el tratamiento si estas no evidencian un abandono definitivo.»** |

> **80.5 es la vía olvidada**: **hasta 5 años** (frente a 2) y **sin primariedad**. Si hay dependencia en el
> origen del hecho, **explórala antes de dar por perdida la suspensión**. **La regla de las recaídas** es
> munición frente a la revocación: una recaída **no es** abandono — exige que se acredite el **abandono
> definitivo**, con informe del centro que contextualice el episodio.

**80.6 — audiencia al ofendido:** en delitos **solo perseguibles previa denuncia o querella**, se **oirá al
ofendido** antes de conceder la suspensión. → Delitos privados y semipúblicos: prevé el trámite; si acusas,
**exige ser oído**; su omisión es defecto.

## 4. Plazo, reglas de conducta y prestaciones

### 4.1 Plazo — art. 81
**2 a 5 años** para penas privativas de libertad **≤ 2 años**; **3 meses a 1 año** para **penas leves**;
**3 a 5 años** si la suspensión se acordó por el **80.5** (dependencia). Se fija atendiendo a los criterios
del 80.1. **Cómputo (82.2):** desde la **resolución que la acuerda**; si se acordó **en sentencia**, desde
su **firmeza**. ⭐ **No se computa** el tiempo en **rebeldía**. **Pide el plazo mínimo**: la horquilla es
amplia y el plazo es tiempo de riesgo de revocación.

### 4.2 Prohibiciones y deberes — art. 83 (síntesis; catálogo íntegro vía `buscar_articulo`)
Condicionables **solo cuando sea necesario para evitar el peligro de comisión de nuevos delitos**, ⭐ **«sin
que puedan imponerse deberes y obligaciones que resulten excesivos y desproporcionados»** — el límite legal
a invocar frente a un catálogo desmedido. Reglas **1.ª a 9.ª**: aproximación/comunicación (1.ª); contacto
con personas o grupo (2.ª); residencia fija (3.ª); prohibición de residir o acudir (4.ª); comparecencia
periódica (5.ª); **programas formativos** y similares (6.ª); **deshabituación** (7.ª); **prohibición de
conducir sin dispositivo de control de condiciones físicas** en seguridad vial (8.ª); demás deberes
**previa conformidad del penado** (9.ª).

- ⚠️ **83.2 — IMPERATIVO:** en delitos **sobre la mujer** por cónyuge o quien esté o haya estado ligado por
  relación análoga **aun sin convivencia**, **se impondrán SIEMPRE** las reglas **1.ª, 4.ª y 6.ª**. Igual
  en **libertad sexual, matrimonio forzado, mutilación genital femenina y trata**. **No hay margen.**
- **83.3 y .4:** las reglas 1.ª-4.ª se comunican a las **FCSE**; las 6.ª, 7.ª y 8.ª las controlan los
  **servicios de gestión de penas y medidas alternativas**, con informe **trimestral** (6.ª y 8.ª) o
  **semestral** (7.ª), y **en todo caso a su conclusión**.

### 4.3 Prestaciones o medidas — art. 84
**1.ª** **acuerdo de mediación**; **2.ª** **multa**, que **no podrá exceder** de **2 cuotas por cada día de
prisión** sobre un máximo de **2/3 de su duración**; **3.ª** **trabajos en beneficio de la comunidad**,
**especialmente como reparación simbólica**, sin exceder de **1 día de trabajo por día de prisión** sobre un
máximo de **2/3**. ⚠️ **84.2:** en violencia sobre la mujer y ámbito familiar (descendientes, ascendientes,
hermanos, menores o personas con discapacidad a cargo), **la multa (2.ª) solo cabe si consta acreditado que
NO existen relaciones económicas** derivadas de relación conyugal, convivencia, filiación o descendencia
común.

## 5. Revocación — art. 86: cómo oponerse

**86.1 — el juez REVOCARÁ cuando el penado:**
- **a)** sea **condenado por delito cometido durante la suspensión** ⭐ **«y ello ponga de manifiesto que la
  expectativa en la que se fundaba la decisión de suspensión ya no puede ser mantenida»**. → **La condena no
  basta**: la ley exige el **segundo requisito valorativo**. Un delito heterogéneo, leve o ajeno a la
  prognosis **no destruye necesariamente** la expectativa. **Argumenta sobre la expectativa, no sobre el
  hecho.**
- **b) y c)** incumpla **de forma grave o reiterada** el art. 83 o las condiciones del art. 84, o **se
  sustraiga al control** de los servicios de gestión de penas.
- **d)** dé **información inexacta o insuficiente sobre bienes cuyo decomiso** se acordó; **incumpla el
  compromiso de pago** ⭐ **«salvo que careciera de capacidad económica para ello»**; o informe
  inexactamente **sobre su patrimonio** (art. 589 LEC).

**⭐ 86.2 — la alternativa:** si el incumplimiento **NO fue grave ni reiterado**, el juez **PODRÁ**: a)
imponer **nuevas** prohibiciones o **modificar** las impuestas; b) **prorrogar el plazo**, **sin exceder de
la mitad** del inicialmente fijado. → **Pídelo siempre en subsidio**: es la salida que evita el ingreso.
Enmarca el incumplimiento como **no grave ni reiterado** y **ofrece** tú la medida.

**86.3 y .4:** revocada, **los gastos de reparación (84.1) no se restituyen**, pero el juez **abonará a la
pena los pagos y trabajos** de las medidas **2.ª y 3.ª** (**reclámalo: es tiempo de prisión menos**).
Resuelve **oído el Fiscal y las demás partes**; solo **podrá** revocar con **ingreso inmediato** **cuando
resulte imprescindible** para evitar **reiteración**, **huida** o **proteger a la víctima**. Puede acordar
**diligencias** y **VISTA oral** → **pídelas**.

## 6. Liquidación de condena y abono de la prisión provisional — art. 58 CP

- **58.1:** el tiempo de privación de libertad provisional **se abona EN SU TOTALIDAD** por el sentenciador
  **en la causa en que se acordó**, **salvo** que haya coincidido con otra privación abonada o abonable en
  otra causa. ⚠️ **«En ningún caso un mismo periodo podrá ser abonado en más de una causa.»**
- **58.2:** el abono **en causa distinta** lo acuerda, **de oficio o a petición del penado** y **previa
  comprobación de que no se abonó en otra**, el **JUEZ DE VIGILANCIA PENITENCIARIA** del centro, **oído el
  Fiscal**. → **Órgano distinto: no lo pidas al sentenciador.**
- **⭐ 58.3:** solo procede el abono de prisión provisional sufrida en otra causa **cuando la medida cautelar
  sea POSTERIOR a los hechos** que motivaron la pena a la que se pretende abonar. **58.4:** igual para las
  **privaciones de derechos acordadas cautelarmente** (retirada del permiso) — **se olvidan casi siempre**.

**Control de la liquidación:** fechas **exactas** de cada período de detención y prisión provisional (con
folio; **días naturales**, extremos incluidos); que **todos** estén abonados (58.1); que **ninguno** se
abonara ya en otra causa; el **requisito de posterioridad** (58.3); las privaciones de derechos (58.4); y la
**fecha de cumplimiento** resultante, con **1/2, 2/3 y 3/4** de la condena. Si es errónea, **impúgnala**:
verifica cauce y plazo con `buscar_articulo` (**794 y ss.**, **983 y ss. LECrim**) → si no, `[verificar]`.

## 7. Refundición / acumulación — art. 988 LECrim y art. 76 CP

- **988 párr. 3:** condenado **en distintos procesos por hechos que pudieron ser objeto de uno solo** (art. 17
  LECrim) → **el órgano que dictó la ÚLTIMA sentencia**, de oficio, a instancia del **Fiscal** o **del
  condenado**, fija el **límite de cumplimiento** conforme al **art. 76 CP**. El LAJ reclama la **hoja
  histórico-penal** y testimonio de las sentencias; previo dictamen del Fiscal, **auto** con todas las penas
  y el máximo. **⭐ Recurso:** cabe **CASACIÓN por infracción de Ley** — **no es apelación**.
- **76.1:** el máximo efectivo **no excederá del TRIPLE de la más grave**, con tope de **20 años**;
  excepcionalmente **25** (algún delito con prisión de hasta 20 años), **30** (alguno superior a 20),
  **40** (dos superiores a 20, o dos o más de **terrorismo** con alguno superior a 20); con **prisión
  permanente revisable** → **92 y 78 bis**.
- **⭐ 76.2 — el criterio que decide:** la limitación se aplica **aunque las penas se hayan impuesto en
  distintos procesos**, cuando lo hayan sido **por hechos cometidos ANTES de la fecha en que fueron
  enjuiciados los que, siendo objeto de acumulación, lo hubieran sido en primer lugar**. → **Es una regla
  de fechas.** Haz una **tabla**: fecha de cada hecho / fecha de cada enjuiciamiento / pena. La
  acumulación se gana o se pierde ahí, y es de los escritos más rentables de la ejecución.

## 8. Expulsión sustitutiva — art. 89 CP

> ⚠️ **ERRATA CORREGIDA — verificado el 2026-07-17: la redacción vigente es la de la LO 1/2015, en vigor
> desde el 1-7-2015. La LO 1/2026 NO modificó este artículo.** No le atribuyas un cambio inexistente.

- **89.1 a .3:** prisión **> 1 año** a **extranjero** → **sustitución por expulsión**; excepcionalmente,
  ejecución de **parte de la pena (≤ 2/3)** y expulsión del resto. Pena **> 5 años** → ejecución de todo o
  parte en lo necesario para la defensa del orden jurídico. **En todo caso** se sustituye el resto al
  acceder al **tercer grado** o a la **libertad condicional**. Se resuelve **en sentencia siempre que sea
  posible**; si no, firme esta, **con la mayor urgencia, oídos el Fiscal y las demás partes**.
- **⭐ 89.4 — la vía de la defensa:** **no procede** cuando, a la vista de las circunstancias del hecho y
  personales, **EN PARTICULAR SU ARRAIGO EN ESPAÑA**, la expulsión resulte **DESPROPORCIONADA**. →
  **Acredita el arraigo**: años de residencia, familia (cónyuge, hijos escolarizados), trabajo, vivienda,
  integración, vínculos (o ausencia) con el país de origen. **Es el argumento central.** **Ciudadano UE:** solo
  si es **amenaza grave para el orden público o la seguridad pública**; con **10 años de residencia**, además,
  condena por delitos graves contra la vida/libertad/indemnidad sexual (pena máx. **> 5 años**) **con riesgo
  grave** de reiteración, o **terrorismo**/**organización criminal** — y rige el **89.2**.
- **89.5 a .7:** prohibición de regreso **5 a 10 años**; archivo de los expedientes de residencia o trabajo;
  **regreso anticipado** → cumple las penas sustituidas (salvo reducción excepcional), y si es **sorprendido
  en la frontera**, expulsión gubernativa y **plazo de prohibición de nuevo íntegro**.
- **89.8:** cabe **ingreso en CIE** para asegurar la expulsión. ⭐ Si **no puede llevarse a efecto**, se
  ejecuta la **pena originaria** o el resto, **o se aplica, en su caso, la SUSPENSIÓN** → si es inejecutable,
  **reclama el art. 80**. **⭐ 89.9:** **NO se sustituyen** las penas de los **arts. 177 bis (trata), 312,
  313 y 318 bis**.

## 9. Estructura del escrito

1. Encabezamiento al **órgano sentenciador** (**Sección de lo Penal del Tribunal de Instancia** /
   Audiencia), **ejecutoria nº**; o a la **Sección de Vigilancia Penitenciaria** (abono en causa
   distinta, 58.2); o el de la **última sentencia** (refundición, 988). Comparecencia del
   **[PENADO]** con procurador y letrado.
   > ⭐ **Copia la denominación exacta que figure en la resolución o en la carátula de la ejecutoria.**
   > El **art. 58.2 CP** atribuye el abono al «**Juez de Vigilancia Penitenciaria**» (así, literal,
   > redacción de 2010): esa es la **persona**; el **órgano** es la **Sección de Vigilancia
   > Penitenciaria** (art. 84.2.g y 92 LOPJ).
2. **Objeto** delimitado: (a) **suspensión** [80.2 / 80.3 / 80.4 / 80.5]; (b) **liquidación** y **abono**
   (58); (c) **refundición** (988 / 76); (d) **revisión** por ley más favorable (2.2); (e) **oposición a
   la revocación** (86); (f) **expulsión** (89) o su improcedencia por desproporción (89.4).
3. **Hechos** con **folio** y ejecutoria: firmeza, penas, períodos de privación de libertad, hoja
   histórico-penal.
4. **Fundamentos**, requisito por requisito, con **prueba documental**. En suspensión: **80.1** (prognosis)
   + cada condición del **80.2** (con la **cláusula de irrelevancia** si procede) + **subsidiariamente 80.3
   / 80.5**; **plazo** del 81 (pide el mínimo); reglas del **83** que se aceptan (invocando el límite de lo
   **excesivo y desproporcionado**); medidas del **84** que se ofrecen.
5. **SUPLICO**: suspensión por el plazo procedente / aprobación o rectificación de la liquidación / fijación
   del límite / revisión / no revocación o, subsidiariamente, **86.2**. Otrosíes: **vista** (86.4),
   diligencias, documental. Lugar, fecha y firma.

## 10. Errores típicos

- ❌ Citar el **art. 80 en su redacción anterior** (la LO 1/2026 añadió la **cláusula de irrelevancia**, el
  **decomiso** en la 3.ª y la salvedad de **multirreincidencia de delitos leves** en la 1.ª), o **no alegar
  la cláusula de irrelevancia** (80.2.1.ª) ante antecedente heterogéneo o antiguo: la novedad más rentable.
- ❌ Olvidar el **decomiso** (art. 127) en la condición 3.ª, o computar en la 2.ª la pena por **impago de
  multa** (el 80.2.2.ª la **excluye**).
- ❌ Renunciar a la suspensión por superar 2 años **sin explorar el 80.5** (**≤ 5 años**), el **80.3** ni el
  **80.4** (**cualquier pena**, sin requisitos); o tratar una **recaída** como abandono (80.5: **no lo es**
  salvo abandono definitivo).
- ❌ Pedir el **abono en causa distinta** al sentenciador (es del **Juez de Vigilancia Penitenciaria**
  —Sección de Vigilancia Penitenciaria—, 58.2), o abonar un período **ya
  abonado** (58.1) o **anterior** a los hechos (58.3).
- ❌ Ante la revocación, discutir solo el hecho y **no la expectativa** (86.1.a), no pedir
  **subsidiariamente el 86.2**, ni reclamar el **abono** del 86.3.
- ❌ En expulsión, no acreditar el **arraigo** (89.4) ni invocar el **89.9** cuando el delito está excluido;
  o atribuir a la LO 1/2026 una reforma del 89 **que no existió**.
- ❌ Olvidar la **audiencia al ofendido** (80.6) en delitos privados/semipúblicos.
- ❌ No revisar la **prescripción de la pena** (133) en ejecutorias antiguas — ni confundir su cómputo con
  el del **132.2.2.ª**, que es del delito.
- ❌ **Combinar** preceptos de dos redacciones al comparar la ley más favorable.

## 11. Reglas de trabajo

- **Jurisprudencia — verificación PREVIA y obligatoria** con `jurisprudenciator` (`buscar_sentencias`,
  `buscar_por_cita`, `leer_sentencias`). ⛔ **PROHIBIDO inventar o citar de memoria** ECLI, ROJ, fechas o
  ponentes. La cláusula de irrelevancia del 80.2.1.ª es **de 2026**: comprueba si ya hay doctrina y, si no
  la hay, **dilo** — el texto legal basta. Sin verificación → `[verificar]`.
- **Prohibido inventar** artículos, apartados, plazos o penas. Confirma con `buscar_articulo` el **apartado
  concreto** del art. 80 y los **arts. 81-84, 86, 89 y 134 CP**, y los preceptos de ejecución (**794 y
  ss.**, **983 y ss. LECrim**).
- **Ley penal en el tiempo:** identifica **siempre** la redacción vigente **a la fecha de los hechos**
  (art. 2 CP) y compárala con la vigente (2.2). Ver § 2. **Anclaje al folio** y a la **ejecutoria**:
  firmeza, liquidación y períodos de privación de libertad.
- **Marcadores:** `[PENADO]`, `[VÍCTIMA]`, `[DATO]`. **Nunca datos reales**: condenas, antecedentes y hoja
  histórico-penal son de **categoría especial** (**art. 10 RGPD**); en el 80.4 y 80.5 hay además **datos de
  salud**. Ver `PROTECCION-DATOS.md`.
- **Terminología (LO 1/2025, DF 38.3, desde 3-10-2025):** **Secciones de los Tribunales de Instancia**
  (art. 14 LECrim); 🚨 **Sección de Vigilancia Penitenciaria** —**no** «Juzgado de Vigilancia
  Penitenciaria»: el **art. 84.2.g LOPJ** la lista como Sección del Tribunal de Instancia y su sede
  propia es el **art. 92 LOPJ** *(verificado; ⚠️ el art. 94 LOPJ ya **no** es el JVP, hoy es la
  Sección de lo Social)*—; LAJ. Al **citar el texto legal**, respeta su literalidad: el **art. 58.2
  CP** y la legislación penitenciaria **no fueron actualizados** y siguen diciendo «Juez de
  Vigilancia Penitenciaria» *(la **DA 1.ª de la LO 1/2025** manda entender esa mención hecha a la
  Sección)*.
  > **⭐ Art. 92.5 LOPJ:** el juez o jueza de la Sección de Vigilancia Penitenciaria **puede
  > compatibilizar** sus funciones con las de otras Secciones penales del mismo Tribunal de
  > Instancia. Útil al anticipar quién resolverá.
- ⛔ **NO existe el «fiscal instructor».** Instruye el **Juez de Instrucción**. Reforma en tramitación
  (prevista 1-1-2028): **nunca** como Derecho vigente.
- ⛔ **Nada de MASC**: es del orden civil. (La **mediación** del art. 84.1.ª es otra cosa: medida de la
  suspensión, no requisito de procedibilidad.)

## Entrega — escrito final en **Word `.docx`** (skill `docx`), maquetado para LexNET.
