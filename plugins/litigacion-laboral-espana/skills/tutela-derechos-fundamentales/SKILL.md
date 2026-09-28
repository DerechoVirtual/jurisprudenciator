---
name: tutela-derechos-fundamentales
description: >-
  Prepara la demanda de tutela de derechos fundamentales y libertades públicas del orden social (LRJS
  arts. 177-184) cuando la relación laboral sigue y no hay despido: acoso, discriminación (Ley 15/2022,
  LO 3/2007), garantía de indemnidad, libertad sindical, intimidad y control digital. Panorama de
  indicios e inversión de la carga (art. 181.2), indemnización por daño moral y material con el criterio
  orientativo de la LISOS (art. 183), Ministerio Fiscal y medidas cautelares (art. 180). Para el
  trabajador, la demanda; para la empresa demandada, la nota de defensa con la justificación objetiva y
  proporcionada. Úsala con «acoso en el trabajo», «me discriminan», «represalia por reclamar», «tutela de
  derechos fundamentales», «nos demandan por acoso». Si hubo despido, la nulidad va en la demanda de
  despido (art. 184): redactar-demanda-despido; si quiere irse, extincion-contrato-trabajador.
---

# Tutela de derechos fundamentales sin despido

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Modalidad procesal** → `buscar_articulo` (`ley="LRJS"`, artículos `"177"`, `"178"`, `"179"`, `"180"`, `"181"`, `"182"`, `"183"` y `"184"`), y exención de conciliación, calendario, competencia y recurso (`"64"`, `"43"`, `"10"` y `"191"`).
- **Derecho invocado** → `buscar_articulo` (`ley="CE"`, el artículo del derecho: `"14"`, `"15"`, `"18"`, `"24"`, `"28"`), (`ley="ET"`, artículos `"4"` y `"17"`) y su norma de desarrollo: igualdad y no discriminación (`ley="BOE-A-2022-11589"`, artículos `"2"`, `"4"`, `"6"`, `"9"`, `"25"`, `"26"`, `"27"` y `"30"`), sexo (`ley="BOE-A-2007-6115"`, artículos `"7"`, `"8"`, `"9"` y `"13"`), libertad sindical (`ley="LOLS"`, `articulo="12"`), intimidad digital (`ley="LOPDGDD"`, artículos `"87"` a `"90"`); en el acoso moral sin móvil discriminatorio, el deber de protección del empresario que funda su responsabilidad propia (`ley="LPRL"`, `articulo="14"`).
- **Criterio orientativo del daño moral** → `buscar_articulo` (`ley="BOE-A-2000-15060"`, `articulo="8"` para el tipo, `articulo="40"` para la escala y `articulo="39"` para los criterios de graduación), leído en el momento: no escribas importes de memoria.
- **Doctrina sobre indicios, garantía de indemnidad, acoso y cuantificación del daño** → `buscar_sentencias` (`base="TC"`; `base="TS"`, `jurisdiccion="SOCIAL"`; y `base="AN"`, `tipo_organo="TSJ"`, `provincia` = sede de la Sala) + `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión); con derecho de la Unión, `base="TJUE"`.
- **Convenio aplicable y sus artículos**, si la lesión afecta a retribución, clasificación, protocolo de acoso o derechos sindicales pactados → `buscar_convenio` + `leer_convenio` + `vigencia_convenio`. `leer_convenio` puede devolver un texto anterior: si `vigencia_convenio` registra un texto nuevo o una modificación posterior a la publicación leída, búscalo en internet en el boletín oficial (BOE, boletín autonómico o BOP; `buscar_boe` y `novedades_boe` no localizan convenios), lee su artículo de vigencia (los textos nuevos suelen entrar en vigor con efectos retroactivos al 1 de enero) y cita el texto que regía en la fecha de los hechos, con su enlace (punto 3 de la puerta). No afirmes que un texto no está publicado sin haberlo buscado en el boletín.
- **Empresa** → `buscar_empresa_mercantil` (denominación exacta, domicilio, administradores, grupo).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Esta skill también está en el plugin Contratos Laborales y Asesoría Empresarial, que añade la asesoría de empresa (convenio aplicable, cálculo de indemnizaciones, cartas de despido, finiquitos…). Si una derivación de esta skill nombra una skill que no está en este plugin, está en aquel. **Pregunta primero a quién defiende el abogado**:

- **Trabajador o sindicato**: la relación sigue y se pide que cese la conducta lesiva, que se reponga la situación y que se indemnice: acoso laboral, sexual o discriminatorio; discriminación directa, indirecta, por asociación o por error; represalias por reclamar (garantía de indemnidad); lesión de la libertad sindical o de huelga; intimidad, propia imagen o protección de datos (videovigilancia, geolocalización, dispositivos digitales).
- **Empresa demandada**: nota de defensa. Frente a indicios, a la empresa le toca probar una justificación objetiva, razonable y proporcionada (art. 181.2 LRJS): la nota ordena esa prueba, mide la exposición (daño moral, daños materiales, riesgo sancionador) y prepara la oposición a las cautelares.

**Detector de la puerta procesal (art. 184 LRJS).** Si la lesión se materializa en alguno de estos actos, la tutela va **dentro** de su modalidad, con las garantías de este capítulo (art. 178.2), y no aquí:

| Acto | Skill |
|---|---|
| Despido o cualquier otra extinción | `redactar-demanda-despido` o `extincion-contrato-trabajador` |
| Modificación sustancial, suspensión o reducción del art. 47 ET | `modificacion-sustancial-condiciones` o `erte-suspension-reduccion` |
| Movilidad geográfica | `movilidad-geografica-funcional` |
| Derechos de conciliación del art. 139 LRJS | `permisos-conciliacion-adaptacion` |
| Sanción disciplinaria | `sanciones-disciplinarias` |
| Vacaciones, materia electoral, impugnación de convenios o de estatutos sindicales | su modalidad propia (fuera de este plugin salvo las anteriores) |

**Episodio dudoso dentro de una conducta continuada.** Si uno de los episodios podría calificarse por sí solo como modificación sustancial o movilidad funcional (retirada de clientes o tareas, cambio de horario o de equipo), lee los artículos 39 y 41 del ET y explica en la demanda por qué no altera ninguna de las materias del art. 41.1 ET y se impugna como parte de la lesión. Como el juez puede reconducir la demanda a la modalidad adecuada (art. 179.4 LRJS), calcula además los veinte días hábiles de caducidad desde ese acto (art. 59.3 y 59.4 ET) y recomienda presentar antes de esa fecha; si ya ha pasado, dilo como riesgo en la nota.

Otras derivaciones: investigación interna del acoso, `protocolo-acoso-laboral`; protección del informante que denunció por el canal interno, `canal-denuncias-informantes`; diagnóstico de brecha retributiva, `plan-igualdad-registro-retributivo`.

## Datos que hay que reunir antes de redactar

No redactes al primer disparo: si falta un dato imprescindible (★), pregúntalo.

1. ★ A quién defiende el abogado; si la relación laboral sigue viva y si ha habido algún acto de los del art. 184 (en ese caso, cambia de skill).
2. ★ Derecho fundamental afectado y conducta concreta; si continúa o cesó y cuándo (condiciona el plazo del art. 179.2).
3. ★ Cronología: cada episodio con fecha, autor, testigos y soporte (correos, mensajes, grabaciones, partes médicos, denuncias internas, actas de la Inspección, comunicaciones sindicales).
4. ★ Hecho que dispara la represalia o el móvil (reclamación, denuncia, embarazo, afiliación, baja, queja por igualdad) y su fecha, para la conexión temporal.
5. ★ En discriminación: término de comparación (personas en situación comparable, retribuciones, criterios de promoción) y datos del registro retributivo si los hay.
6. ★ Contra quién: empresa, causante directo (compañero, superior), terceros vinculados (contrata, usuaria).
7. ★ Daños: moral (gravedad, duración, consecuencias, reiteración) y materiales con sus bases de cálculo (diferencias salariales, gastos médicos, pérdida de oportunidades). Datos de salud: solo los necesarios, con marcador en el borrador.
8. ★ Si se necesitan medidas urgentes (alejamiento del acosador, cambio de puesto o de centro, exoneración de prestar servicios) para pedir cautelares.
9. Si interviene un sindicato como coadyuvante o hay entidades de defensa del derecho afectado dispuestas a personarse.
10. Si defiende a la empresa: protocolo de acoso y su aplicación, investigación interna, medidas adoptadas, razones documentadas de cada decisión cuestionada.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación y anota su «vigente desde».

**Objeto, partes y acumulación.**
- Cualquier trabajador o sindicato puede pedir la tutela de la libertad sindical, la huelga y demás derechos fundamentales, incluida la prohibición de discriminación y de acoso, también frente a terceros vinculados al empresario cuando la lesión tenga conexión directa con la prestación de servicios (art. 177.1 LRJS).
- La víctima es la única legitimada, elige la tutela y puede dirigirse contra el empresario y contra el causante directo, que solo debe ser demandado si se pide su condena o puede resultar afectado (art. 177.4). Coadyuvantes: su sindicato, el más representativo y, en discriminación, las entidades de defensa (art. 177.2). **El Ministerio Fiscal es siempre parte** (art. 177.3).
- Solo se conoce de la lesión del derecho: no se acumulan acciones de otra naturaleza (art. 178.1). Si el acto está en el art. 184, se va a su modalidad con estas garantías (art. 178.2).

**Tramitación y plazo.**
- Exenta de conciliación previa (art. 64.1 LRJS). Urgente y preferente (art. 179.1); agosto y del 24 de diciembre al 6 de enero cuentan (art. 43.4).
- Plazo: el general de prescripción o caducidad de la acción prevista para las conductas o actos en que se concreta la lesión (art. 179.2). Identifica esa acción y su plazo (por ejemplo, el del art. 59 ET) y deja en la nota la fecha inicial, el precepto y la fecha límite; en conductas continuadas, explica desde cuándo se cuenta y por qué.
- Competencia territorial: la del lugar donde se produjo la lesión o al que se extienden sus efectos (art. 10.2.f LRJS). Juicio dentro de los cinco días siguientes a la admisión y sentencia en tres días (art. 181.1 y 181.3).

**Contenido de la demanda (art. 179.3 LRJS).** Hechos constitutivos de la vulneración, derecho infringido y cuantía de la indemnización con especificación de los daños; salvo el daño moral de difícil estimación, hay que dar las circunstancias relevantes (gravedad, duración y consecuencias) o las bases de cálculo. Una demanda que no deba tramitarse por esta vía puede ser rechazada o reconducida (art. 179.4).

**Carga de la prueba.** Justificados indicios de la vulneración, corresponde al demandado aportar una justificación objetiva y razonable, suficientemente probada, de las medidas y de su proporcionalidad (art. 181.2 LRJS; también art. 96.1 LRJS, art. 30 de la Ley 15/2022, de 12 de julio, y art. 13 de la Ley Orgánica 3/2007, de 22 de marzo). El indicio no es una afirmación: es un hecho con fecha y documento que hace verosímil el móvil.

**Derecho sustantivo (lee solo lo que vayas a invocar).**
- Igualdad y no discriminación: art. 14 CE; art. 4.2.c y art. 17 ET; Ley 15/2022: causas, incluida la enfermedad o condición de salud (art. 2.1), vulneraciones y definiciones de discriminación directa, indirecta, por asociación, por error, múltiple, acoso discriminatorio y represalias (arts. 4 y 6), empleo por cuenta ajena (art. 9), nulidad (art. 26), reparación, presunción del daño moral y responsabilidad del empleador que no cumplió sus deberes de prevención (arts. 25 y 27).
- Sexo: acoso sexual y por razón de sexo (art. 7), embarazo o maternidad (art. 8), indemnidad frente a represalias (art. 9) de la Ley Orgánica 3/2007.
- Integridad moral y acoso laboral: art. 15 CE y art. 4.2.d y e ET. Garantía de indemnidad: art. 24 CE; cubre también las reclamaciones extrajudiciales y los actos preparatorios (búscalo en la doctrina). Libertad sindical: art. 28 CE y art. 12 de la Ley Orgánica 11/1985, de 2 de agosto. Intimidad y control digital: art. 18 CE y arts. 87 a 90 de la Ley Orgánica 3/2018.

**Medidas cautelares (art. 180 LRJS).** Se piden en la propia demanda: suspensión de los efectos del acto y demás medidas para asegurar la efectividad de la sentencia (180.1), si la ejecución del acto haría perder su finalidad a la tutela y no causa una perturbación grave y desproporcionada (180.2; en libertad sindical, solo en los supuestos tasados de ese apartado). En acoso y en violencia de género caben además la suspensión de la relación o la exoneración de prestar servicios, el traslado de puesto o de centro, la reordenación o reducción del tiempo de trabajo y medidas que afecten al presunto acosador, que será oído (180.4). Audiencia preliminar en cuarenta y ocho horas con principio de prueba de la justificación y la proporcionalidad; en urgencia excepcional, al admitir la demanda (180.5).

**Sentencia e indemnización.**
- Si se estima: declaración de la vulneración, nulidad radical de la actuación, cese inmediato o realización de la actividad omitida, reposición de la situación anterior y reparación, incluida la indemnización (art. 182.1 LRJS). El suplico reproduce estos pronunciamientos.
- Indemnización del daño moral unido a la vulneración y de los daños adicionales; el juez la fija prudencialmente cuando la prueba del importe exacto es difícil, para resarcir y para prevenir el daño; es compatible con la de modificación o extinción del contrato (art. 183.1 a 183.3). Si se ejercitó la acción civil en un proceso penal, no puede reiterarse aquí mientras no se desista o termine sin condena (art. 183.4).
- Criterio orientativo: la Sala Cuarta admite como referencia las sanciones de la LISOS para la infracción correspondiente. Identifica el tipo del art. 8 del Real Decreto Legislativo 5/2000 (dignidad, discriminación, acoso sexual, acoso discriminatorio no evitado) y la escala de su art. 40, leídos en el momento; elige el grado razonando gravedad, duración, reiteración, consecuencias y posición de las partes, y dilo en la demanda.
- Recurso: suplicación en todo caso (art. 191.3.f LRJS).

## Estrategia y jurisprudencia

**Si defiende al trabajador.**
1. Pasa el detector del art. 184 antes de redactar: elegir mal la modalidad es el error más caro.
2. Construye el panorama indiciario en los HECHOS: indicio primero, segundo…, cada uno con fecha, documento y conexión temporal con el hecho protegido.
3. Cuantifica siempre (art. 179.3): daño moral con el criterio orientativo razonado y daños materiales con sus bases; en discriminación retributiva, busca la doctrina que admite reclamar las diferencias como daño.
4. Valora las cautelares cuando la situación sea insostenible, antes que aconsejar una baja o una salida.

**Si defiende a la empresa.**
1. Ordena la prueba de la justificación de cada decisión: razón, fecha, documento, criterio aplicado a otros trabajadores comparables, proporcionalidad.
2. Acredita el protocolo, la investigación y las medidas: sin ellos, la empresa responde del daño de la discriminación o del acoso discriminatorio producidos en su ámbito aunque no los cometa ella (art. 27.2 de la Ley 15/2022, de 12 de julio, en relación con su art. 25.1).
3. Prepara la oposición a las cautelares (perturbación desproporcionada, falta de principio de prueba) y mide la exposición: indemnización, riesgo sancionador del art. 8 LISOS y repercusión de un acta de la Inspección.

**Consultas** (reformula dos veces como máximo; lee solo lo que vayas a citar, `parrafos=3`, y transcribe fundamentos, nunca hechos ni datos de las partes, y menos aún datos de salud):
- Indicios: `consulta="prueba indiciaria vulneración derechos fundamentales inversión carga de la prueba"`, `base="TC"`.
- Indemnidad: `consulta="garantía de indemnidad represalia indicios reclamación extrajudicial actos preparatorios"`, `base="TS"`, `anios=3`.
- Daño moral: `consulta="indemnización daño moral vulneración derechos fundamentales criterio orientativo LISOS bases cuantificación"`, `base="TS"`, `anios=3`.
- Acoso: `consulta="acoso laboral tutela derechos fundamentales integridad moral indemnización"`, `base="TS"` y después `base="AN"`, `tipo_organo="TSJ"`.
- Discriminación retributiva: `consulta="tutela derechos fundamentales discriminación retributiva indemnización diferencias salariales daños materiales"`, `base="TS"`.
- Intimidad y control: `consulta="videovigilancia dispositivos digitales geolocalización intimidad trabajador proporcionalidad"`, `base="TS"` y `base="TC"`.
- Derecho de la Unión (igualdad de trato, carga de la prueba): la cuestión concreta con `base="TJUE"`.

## Documentos que se entregan

**1. Demanda** (`demanda-tutela-derechos-fundamentales-<apellido-cliente>-<AAAAMMDD>.docx`), si defiende al trabajador o al sindicato, maquetada según el apartado 2 del formato:
1. Encabezamiento al Tribunal de Instancia de `[SEDE]`, Sección de lo Social; demandante con marcadores; demandados: `[DENOMINACIÓN SOCIAL]` (`[CIF]`) y, si se pide su condena, `[NOMBRE Y APELLIDOS DEL CAUSANTE]`; **con citación del Ministerio Fiscal**. Modalidad: tutela de derechos fundamentales y libertades públicas (arts. 177 y siguientes LRJS).
2. HECHOS: relación laboral; hecho protegido y su fecha; episodios de la lesión en orden cronológico con su soporte; panorama indiciario numerado; daños con sus circunstancias y bases.
3. FUNDAMENTOS: competencia (art. 2 y art. 10.2.f LRJS); adecuación de la modalidad y exención de conciliación (arts. 64.1, 177 y 184 LRJS); plazo (art. 179.2 y el precepto de la acción); derecho vulnerado con su norma de desarrollo; indicios y carga (art. 181.2 LRJS y doctrina constitucional leída); pronunciamientos (art. 182); indemnización (art. 183, criterio orientativo razonado y doctrina leída).
4. SUPLICO: declaración de la vulneración de `[DERECHO]`; nulidad radical de `[CONDUCTA O DECISIÓN]`; cese inmediato; reposición a la situación anterior; condena solidaria o individual a pagar `[IMPORTE]` € por daño moral y `[IMPORTE]` € por daños materiales.
5. OTROSÍES: medidas cautelares concretas con su justificación (art. 180); prueba: interrogatorio con el apercibimiento del art. 91.2 LRJS, documental en poder de la empresa (expediente de acoso, registros, comunicaciones) con el del art. 94.2, testifical y pericial (psicológica, informática), y las condiciones de declaración de la víctima (art. 177.4).

**2. Tabla de cuantificación** dentro de la demanda y de la nota: concepto (daño moral / cada daño material) · base o circunstancia · fuente (artículo de la LISOS leído, documento) · importe pedido.

**3. Nota** (`nota-tutela-<empresa>-<AAAAMMDD>.docx`): puerta procesal elegida y por qué; plazo con fechas; fortaleza de cada indicio; riesgos; para la empresa, la nota de defensa con la prueba de la justificación, las medidas, la oposición a las cautelares y la exposición; jurisprudencia literal usada.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Detector del art. 184 LRJS pasado: no hay despido ni otro acto con modalidad propia; si lo hay, se ha cambiado de skill. Si un episodio podría ser modificación sustancial o movilidad funcional, la demanda explica por qué no lo es y la nota da la fecha de caducidad de veinte días hábiles desde ese acto.
- [ ] Leídos en esta conversación LRJS 177 a 184, 64, 43, 10 y 191, y cada precepto sustantivo que se invoca (CE, ET, Ley 15/2022, Ley Orgánica 3/2007, Ley Orgánica 11/1985, Ley Orgánica 3/2018).
- [ ] Ministerio Fiscal citado; causante directo demandado solo si se pide su condena o le afecta la sentencia.
- [ ] Plazo del art. 179.2 identificado con la acción de referencia, su precepto y su fecha límite.
- [ ] Panorama indiciario con fecha y documento para cada indicio.
- [ ] Indemnización cuantificada con sus bases; artículos 8 y 40 del Real Decreto Legislativo 5/2000 leídos en esta conversación si se usan como referencia; ningún importe escrito de memoria.
- [ ] Convenio con su código y vigencia, si se ha usado.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; ningún dato de salud ni de las partes de otros pleitos transcrito.
- [ ] `verificar_escrito` pasado sobre cada documento; avisos de «posible disonancia» (el art. 181 LRJS se titula «Conciliación y juicio») contrastados con el apartado leído.
- [ ] Marcadores en lugar de datos no facilitados.
- [ ] Los datos obtenidos en internet (por ejemplo, una norma de la Unión en EUR-Lex) figuran con su enlace en el documento y en el resumen.
- [ ] Resumen para el abogado según el apartado 9 del formato.
