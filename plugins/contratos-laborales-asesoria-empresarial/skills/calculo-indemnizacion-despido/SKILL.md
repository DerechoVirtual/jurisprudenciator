---
name: calculo-indemnizacion-despido
description: >-
  Calcula en una hoja de Word, con cada operación a la vista, las indemnizaciones por extinción del
  contrato: despido improcedente (art. 56 ET y, para contratos anteriores al 12/02/2012, los dos tramos y
  topes de la disposición transitoria undécima), objetivo y colectivo (art. 53), fin de contrato temporal
  (art. 49.1.c), extinción del art. 50, traslado y modificación sustancial, salarios de tramitación con
  sus descuentos y la parte a cargo del Estado, y readmisión irregular (arts. 279-281 LRJS). Úsala
  cuando digan «¿cuánto le corresponde?», «calcula la indemnización», «¿33 o 45 días?», «salario
  regulador», «salarios de tramitación» u «oferta para la conciliación». Sirve a empresa y trabajador.
  La liquidación de haberes (vacaciones, pagas, salario del mes) va en finiquito-liquidacion.
---

# Cálculo de indemnizaciones por despido y extinción

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Módulos, topes y fecha final del cómputo** → `buscar_articulo` (`ley="ET"`, artículos `"56"`, `"53"`, `"49"`, `"50"`, `"51"`, `"40"`, `"41"`, `"43"` y `"55"`) y (`ley="LRJS"`, artículos `"110"`, `"122"` y `"123"`): los de los escenarios que calcules. En contratos temporales encadenados, además `"15"` (su apartado 5: fijeza por encadenamiento).
- **Tramo anterior al 12/02/2012** → `buscar_articulo` no devuelve la disposición transitoria undécima del ET (ni sus disposiciones adicionales): léela en internet en el texto consolidado del Estatuto de los Trabajadores en el BOE y cítala con su enlace (https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#dtundecima) y la fecha de consulta. La página completa del Estatuto es demasiado larga para leerla de una vez: pide solo el bloque a la API de datos abiertos del BOE (https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2015-11430/texto/bloque/dtundecima; la disposición adicional decimonovena, con `.../texto/bloque/dadecimonovena`). La doctrina sobre sus topes, en la Sala Cuarta: `buscar_sentencias` (`consulta="disposición transitoria undécima indemnización despido improcedente 45 días 720 días 42 mensualidades"`, `base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias` (`parrafos=3`, `terminos="720 días 12 de febrero de 2012 42 mensualidades"`); su párrafo transcribe además la disposición.
- **Salarios de tramitación, recurso y readmisión irregular** → `buscar_articulo` (`ley="LRJS"`, artículos `"111"`, `"113"`, `"116"`, `"119"`, `"279"`, `"281"` y `"286"`) y (`ley="LGSS"`, artículos `"267"` y `"268"`).
- **Salario regulador y antigüedad computable** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="SOCIAL"`) + `leer_sentencias`, con las consultas de «Estrategia y jurisprudencia».
- **Relaciones especiales, FOGASA y fiscalidad** → `buscar_articulo` (`ley="BOE-A-2011-17975"`, `articulo="11"`, hogar familiar), (`ley="BOE-A-1985-17006"`, `articulo="11"`, alta dirección), (`ley="ET"`, `articulo="33"`) y (`ley="LIRPF"`, `articulo="7"`); el salario mínimo del año, si hace falta para el FOGASA, con `buscar_boe` y `leer_boe`.
- **Convenio aplicable y sus mejoras** → `buscar_convenio` + `leer_convenio` (`buscar_en="indemnización"` y `"despido"`) + `vigencia_convenio`.
- **Empresa** → `buscar_empresa_mercantil` (disolución o concurso: FOGASA y administración concursal).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, artículo del convenio con su código, ECLI o ROJ con su párrafo literal, dato registral...). Lo que Jurisprudenciator no tenga se cita de la fuente oficial de internet, con su enlace y la fecha de consulta, como dice el punto 3 de la puerta.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, el convenio, la jurisprudencia que exige el apartado 8 de `references/formato-y-organos-laboral.md` o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-laboral.md` (cómo pedir cada norma y el convenio) y `references/formato-y-organos-laboral.md` (entregables, órganos, citas, plazos, cálculos y resumen). Léelas antes de redactar.

## Cuándo usarla

Pregunta primero **a quién defiende el despacho y para qué es la cifra**:

- **Empresa**: indemnización que hay que poner a disposición con la carta (objetivo, colectivo), oferta para la conciliación, provisión contable o decisión de optar entre readmitir e indemnizar tras la sentencia. La empresa necesita una cifra que no sea impugnable por insuficiente.
- **Trabajador**: comprobar lo puesto a disposición u ofrecido, cuantificar la demanda o la ejecución, o valorar una oferta. El trabajador necesita saber qué conceptos y qué antigüedad se han dejado fuera.

| Si lo que se necesita es… | Skill |
|---|---|
| Liquidar salario pendiente, vacaciones, pagas; hacer o revisar el finiquito | `finiquito-liquidacion` |
| Redactar la carta con la indemnización | `carta-despido-objetivo` o `carta-despido-disciplinario` |
| Papeleta o demanda con la cifra | `papeleta-conciliacion`, `redactar-demanda-despido`, `extincion-contrato-trabajador` |
| Despido colectivo (umbrales, consultas) | `despido-colectivo-empresa` |
| Alto directivo | `alta-direccion` (esta skill solo aplica el art. 11 del Real Decreto 1382/1985 si ya se sabe que es alta dirección) |
| Saber qué convenio rige | `convenio-aplicable` |

## Datos que hay que reunir antes de redactar

No calcules al primer disparo. Si falta un dato imprescindible (★), pídelo o deja el escenario sin cifra con su marcador.

1. ★ Finalidad de la cifra y escenarios que hay que calcular (por ejemplo: objetivo procedente, improcedente y, si se alega, nulo).
2. ★ Fecha de inicio de la relación y **todos los contratos anteriores** con la misma empresa, su grupo o sus antecesoras: fechas de alta y baja, huecos entre contratos, subrogaciones, cesiones, finiquitos firmados en cada cambio, antigüedad reconocida en nómina o en pacto.
3. ★ Fecha de efectos del despido o del cese efectivo.
4. ★ Nóminas de los doce meses anteriores al despido, con todos sus conceptos; si en ese año hubo incapacidad temporal, ERTE u otra suspensión, las de los meses previos a la suspensión.
5. ★ Pagas extraordinarias: número, importe y si están prorrateadas. Retribución variable (comisiones, incentivos, bonus), horas extraordinarias habituales y retribución en especie (vehículo, vivienda, seguros, acciones), con su valor.
6. ★ Jornada: completa, parcial o **reducida por guarda legal** o cuidado de familiar, y desde cuándo.
7. ★ Convenio aplicable (para las mejoras de la indemnización y las categorías).
8. Si el trabajador es o fue representante legal o delegado sindical (la opción es suya).
9. Para salarios de tramitación: fecha de presentación de la demanda, fecha de la sentencia de instancia y de su notificación, nuevo empleo del trabajador (fecha e ingresos) y prestaciones por desempleo percibidas.
10. Indemnización ya puesta a disposición o cobrada, con fecha e importe.
11. Situación de la empresa (concurso, cierre, insolvencia).

## Régimen jurídico y comprobaciones

Lee cada precepto con `buscar_articulo` en esta conversación y comprueba cada módulo y cada tope en su texto antes de usarlo.

### 1. Salario regulador

- **Real** en el momento del despido (apartado 7 del formato): suma anual de todas las percepciones salariales (art. 26.1 ET) de las nóminas: salario base, complementos, pagas extraordinarias, especie y el promedio anual de lo variable. Los conceptos fijos se anualizan con su importe al tiempo del despido. Si las pagas vienen **prorrateadas** en la nómina, ya están dentro del importe mensual: no las sumes otra vez (es el error más frecuente de las gestorías); si no lo están, suma su importe anual. Excluye lo que no es salario (art. 26.2 ET): indemnizaciones y suplidos por gastos, prestaciones de la Seguridad Social, indemnizaciones por traslados, suspensiones o despidos.
- **Salario diario = salario anual ÷ 365**. **Mensualidad = salario anual ÷ 12** (para los topes expresados en mensualidades). Declara estos divisores en la hoja: si la otra parte usa otros, la diferencia se ve.
- **Suspensiones en el año anterior** (incapacidad temporal, ERTE): la Sala Cuarta excluye el periodo de suspensión del promedio de los conceptos variables (media de los meses con actividad × 12); léelo y aplícalo (consulta abajo). Las vacaciones no son suspensión: esos meses sí entran.
- **Días sin contrato en el año anterior** (contratos encadenados): el salario regulador es el de la prestación de servicios anualizado, no la suma de lo cobrado en el año, que contaría como cero los días en blanco.
- **Reducción de jornada por guarda o cuidado**: una disposición adicional del ET regula el salario con el que se calculan las indemnizaciones en esos casos, y el conector no devuelve las disposiciones adicionales del ET. Léela en internet en el texto consolidado del ET en el BOE, cítala con su enlace y la fecha de consulta, y busca la doctrina que la aplica (consulta abajo). Si no aparece ni en Jurisprudenciator ni en internet, no calcules ese escenario y dilo (punto 3 de la puerta).
- **Salario real inferior al de convenio**: calcula con el real y, si el trabajador reclama el debido, añade un escenario con el de convenio, solo con la tabla salarial publicada del año, localizada en internet con su enlace o aportada por el abogado (apartado 3 de las anclas).
- Especie, vehículo, vivienda o acciones: su cómputo depende de su naturaleza salarial; busca la doctrina antes de incluirlos o excluirlos, y explica en la hoja la decisión.

### 2. Antigüedad computable

- Desde el inicio de la relación hasta la fecha final que marque el precepto: cese efectivo (art. 56.1 ET), fecha de la sentencia si se tiene por hecha la opción en ella (art. 110.1.b) LRJS) o fecha del auto en la readmisión irregular (art. 281.2 LRJS). En el art. 50 ET, la fecha en que se extinga la relación: si calculas para la demanda, hazlo a la fecha de presentación y advierte de que la cifra se actualizará.
- **Prorrateo por meses** de los periodos inferiores al año (arts. 56.1, 53.1.b), 40.1 y 41.3 ET): la doctrina de la Sala Cuarta computa la fracción de mes como mes completo; léela y aplícala. En la hoja: años completos + meses (la fracción, como mes) ÷ 12.
- **Contratos anteriores**: se suma el tiempo de los contratos previos cuando hay unidad esencial del vínculo. La doctrina actual no fija un número de días de interrupción: pondera si el hueco es significativo en el conjunto de la relación y distingue si la contratación temporal fue fraudulenta. Lee la doctrina más reciente y justifica la decisión con el porcentaje que suponen los huecos: sobre el total y, para el hueco más largo, sobre el tiempo transcurrido desde el contrato anterior al paréntesis hasta el cese (así lo mide la Sala Cuarta). Con unidad esencial, la Sala fija la antigüedad en la fecha del primer contrato: ese es el escenario principal. Calcula además, como variantes, el de los días efectivamente trabajados (la tesis que suele oponer la empresa) y el de la cadena rota en el hueco más largo.
- **Cadena de contratos temporales que termina en un «fin de contrato»**: comprueba si el cese es en realidad un despido: fraude en la causa o, en contratos por circunstancias de la producción posteriores a la reforma de 2021, más de dieciocho meses en veinticuatro con dos o más contratos (apartado 5 del art. 15 ET: fijeza). Si lo es, calcula el despido improcedente junto a lo pagado como fin de contrato. **Indemnizaciones ya cobradas**: se descuenta la de la extinción que se impugna; las de los ceses anteriores de una cadena fraudulenta no son compensables según el criterio del Pleno de la Sala Cuarta que aplican los TSJ (consulta abajo). Muestra, como riesgo, la cifra que resultaría si se descontaran.
- **Sucesión de empresa**: el cesionario se subroga en los derechos del anterior (art. 44.1 ET). **Cesión ilegal**: en la cesionaria, la antigüedad se computa desde el inicio de la cesión ilegal (art. 43.4 ET). **Antigüedad reconocida** en contrato o nómina: busca doctrina sobre su alcance a efectos indemnizatorios antes de usarla o descartarla.

### 3. Módulos y topes

| Extinción | Módulo | Tope | Precepto |
|---|---|---|---|
| Despido improcedente (relación iniciada desde el 12/02/2012) | 33 días por año | 24 mensualidades | art. 56.1 ET |
| Despido improcedente con contrato anterior al 12/02/2012 | 45 días por año hasta esa fecha y 33 después | 720 días, salvo que el tramo anterior ya dé más: entonces ese es el máximo, sin superar 42 mensualidades | disposición transitoria undécima ET (texto del BOE consolidado; topes según la Sala Cuarta) |
| Extinción por voluntad del trabajador | la del despido improcedente | la del improcedente | art. 50.2 ET |
| Despido objetivo; despido colectivo (salvo mejora pactada) | 20 días por año | 12 mensualidades | art. 53.1.b) ET; el art. 51.4 ET remite al art. 53.1 |
| Traslado con opción por extinguir | 20 días por año | 12 mensualidades | art. 40.1 ET |
| Modificación sustancial (letras a, b, c, d y f del art. 41.1) | 20 días por año | 9 meses | art. 41.3 ET |
| Fin de contrato temporal (no formativos ni sustitución) | parte proporcional de 12 días por año (declara si prorrateas por días, días del contrato ÷ 365, o por meses, y cuadra la cifra con la del finiquito) | — | art. 49.1.c) ET |
| Muerte, jubilación o incapacidad del empresario | un mes de salario | — | art. 49.1.g) ET |
| Hogar familiar (desistimiento) y alta dirección | los del art. 11 de cada real decreto | los de ese artículo | Real Decreto 1620/2011 y Real Decreto 1382/1985 |

Si el convenio mejora la indemnización, cita el artículo leído con `leer_convenio` y calcula las dos cifras (legal y convencional).

**Cómo aplicar la disposición transitoria undécima** (con su texto y el párrafo de la Sala Cuarta a la vista):

1. Solo si el contrato se formalizó antes del 12/02/2012; con unidad esencial del vínculo, el cómputo arranca en el primer contrato.
2. Tramo 1: 45 días × tiempo anterior al 12/02/2012, prorrateado por meses. Tramo 2: 33 días × tiempo posterior, prorrateado por meses. Si febrero de 2012 queda partido entre los dos tramos, di cómo lo has computado.
3. Si el tramo 1 no llega a 720 días: suma ambos tramos con el tope de 720 días.
4. Si el tramo 1 supera 720 días: la indemnización es la del tramo 1 (el tiempo posterior no suma), con el máximo de 42 mensualidades.
5. Deja escritas en la hoja las dos cifras intermedias y la regla que decide.

### 4. Despido objetivo: puesta a disposición y efectos

- La indemnización se pone a disposición a la vez que se entrega la carta (art. 53.1.b) ET); por causa económica que lo impida, puede no hacerse si la carta lo hace constar. Preaviso de quince días o los salarios de ese periodo (art. 53.1.c) ET).
- El **error excusable** en el cálculo y la falta de preaviso no hacen improcedente el despido, pero obligan a pagar la diferencia o los salarios (art. 53.4 ET, último párrafo, y art. 122.3 LRJS); un error inexcusable sí lo hace improcedente. Busca doctrina con la causa concreta del error.
- Si se declara improcedente y se readmite, el trabajador devuelve lo cobrado; si se indemniza, se descuenta (art. 53.5.b) ET y art. 123 LRJS). Los salarios de tramitación no se deducen de los del preaviso (art. 123.2 LRJS).

### 5. Salarios de tramitación

- **Cuándo**: despido nulo, con readmisión inmediata y los salarios dejados de percibir (art. 55.6 ET y art. 113 LRJS); improcedente con opción por la readmisión (art. 56.2 ET); representante legal o delegado sindical, opte por lo que opte (art. 56.4 ET). Con opción por la indemnización, no hay salarios de tramitación salvo en ese último caso.
- **Periodo**: desde el despido hasta la notificación de la sentencia que declara la improcedencia, o hasta el nuevo empleo si es anterior (art. 56.2 ET). Importe: días naturales del periodo × salario diario del regulador; ajústalo si el abogado acredita variaciones salariales en ese periodo.
- **Descuentos**: lo percibido en el nuevo empleo, si el empresario lo prueba (art. 56.2 ET); con readmisión, las prestaciones por desempleo cobradas pasan a ser indebidas y el empresario las ingresa en la entidad gestora descontándolas de los salarios, con el límite que fija el art. 268.5.b) LGSS; el periodo se cotiza como ocupación (art. 268.6 LGSS).
- **Parte a cargo del Estado**: lo que exceda de noventa días hábiles desde la presentación de la demanda hasta la primera sentencia que declare la improcedencia (art. 56.5 ET y art. 116.1 LRJS), con los periodos excluidos del art. 119 LRJS (su texto aún dice «sesenta»: la nota del conector remite a los noventa del art. 116). Si la cifra depende de qué días cuentan, busca la doctrina. Con insolvencia provisional, el trabajador reclama directamente al Estado (art. 116.2 LRJS).
- **Recurso**: con opción por la readmisión, readmisión provisional; con opción por la indemnización, situación legal de desempleo mientras se resuelve, y posible cambio de opción si el recurso del trabajador eleva la indemnización (art. 111 LRJS). Léelo si hay recurso.

### 6. No readmisión o readmisión irregular

Tras la sentencia, si la empresa no readmite o readmite mal (plazos del art. 279 LRJS), el auto que resuelve el incidente (art. 281.2 LRJS): extingue la relación en su fecha; condena a las percepciones de los apartados 1 y 2 del art. 56 ET computando como tiempo de servicio el transcurrido hasta el auto; puede añadir una indemnización adicional de hasta quince días por año con un máximo de doce mensualidades; y condena a los salarios desde la notificación de la primera sentencia de improcedencia hasta el auto. La imposibilidad de readmitir (cierre, cese) sigue las mismas reglas (art. 286.1 LRJS); en la nulidad por acoso, la víctima puede optar por extinguir (art. 286.2 LRJS). Calcula la adicional en su tramo mínimo y máximo.

### 7. Lo que la hoja no debe prometer

- **Indemnización adicional a la tasada** por despido improcedente (Carta Social Europea, Convenio 158 de la OIT): la Sala Cuarta la ha rechazado. Lee el párrafo de la **mayoría**: en esa búsqueda, `leer_sentencias` puede devolver pasajes del voto particular, que no es doctrina. La indemnización por vulneración de derechos fundamentales (art. 183 LRJS) es otra cosa: va en la demanda.
- **Fiscalidad**: la indemnización está exenta en la cuantía obligatoria del ET y con el límite que fija el art. 7.e) LIRPF (léelo; no escribas la cifra de memoria); la acordada en la conciliación administrativa no se considera pactada, pero tampoco está exenta más allá de esa cuantía obligatoria. En la hoja, separa de forma orientativa parte exenta y parte sujeta y di que la retención la practica la empresa.
- **FOGASA**: responde con los límites del art. 33.2 ET (léelos y, para la base, el salario mínimo del año con `buscar_boe` y `leer_boe`). Muestra la cifra garantizada si la empresa es insolvente.

## Estrategia y jurisprudencia

- **Empresa**: calcula con el salario y la antigüedad más altos que razonablemente pueda sostener el trabajador. En el objetivo, un error inexcusable convierte el despido en improcedente: la diferencia de unos céntimos no compensa ese riesgo. En la oferta de conciliación, muestra la horquilla (objetivo, improcedente, salarios de tramitación si se readmite) para decidir.
- **Trabajador**: revisa por este orden: conceptos salariales omitidos (variable, especie, pagas no prorrateadas), periodos de suspensión metidos en el promedio, reducción de jornada, contratos anteriores, tramo anterior al 12/02/2012 y prorrateo de la fracción de mes. Cada omisión es una línea en la tabla de diferencias.
- **Consultas** (reformula como máximo dos veces; `base="TS"`, `jurisdiccion="SOCIAL"` salvo que se diga otra cosa):
  - Tramo anterior a 2012: `consulta="disposición transitoria undécima indemnización despido improcedente 45 días 720 días 42 mensualidades"`.
  - Salario regulador con suspensiones: `consulta="salario regulador indemnización despido retribución variable promedio doce meses"`.
  - Especie: `consulta="salario en especie computable indemnización despido vehículo seguro médico"`; si el Supremo no tiene nada sobre el concepto concreto, en el TSJ: `consulta="seguro de salud abonado por la empresa salario en especie cómputo indemnización despido"`, `base="AN"`, `tipo_organo="TSJ"` y `provincia` con la sede de la Sala.
  - Contratos anteriores: `consulta="unidad esencial del vínculo cómputo antigüedad indemnización despido interrupciones entre contratos"`, con `fecha_desde="01/01/2016"`.
  - Indemnizaciones de fin de contrato ya cobradas: `consulta="compensación indemnización fin de contrato temporal percibida con indemnización despido improcedente contratación fraudulenta"`, `base="AN"`, `tipo_organo="TSJ"`, `provincia` con la sede de la Sala y `anios=5`.
  - Fracción de mes: `consulta="prorrateo por meses fracción de mes cómputo antigüedad indemnización despido"`.
  - Error en la puesta a disposición: `consulta="error excusable puesta a disposición indemnización despido objetivo antigüedad que figuraba en nómina"`.
  - Jornada reducida por guarda: `consulta="disposición adicional decimonovena Estatuto de los Trabajadores reducción de jornada indemnización despido salario jornada completa"`, `base="AN"`, `tipo_organo="TSJ"`, `anios=4`.
  - Indemnización adicional: `consulta="indemnización adicional despido improcedente Carta Social Europea artículo 24 reparación adecuada"`.
  - Salarios a cargo del Estado: `consulta="salarios de tramitación a cargo del Estado noventa días hábiles cómputo"`.
- La doctrina es **imprescindible** (apartado 8 del formato) cuando decide la cifra: antigüedad con contratos anteriores, salario regulador con suspensiones o especie, tramo anterior a 2012 y error excusable. Lee con `leer_sentencias` (`parrafos=3`, `terminos` de la cuestión) solo lo que vayas a citar y comprueba que el párrafo es razonamiento de la Sala.

## Documento que se entrega

Hoja de cálculo en Word según `references/formato-y-organos-laboral.md`: `calculo-indemnizacion-<apellido-trabajador>-<AAAAMMDD>.docx`. Cada operación en su línea, con la fórmula y el resultado redondeado a céntimos, en este formato: «[días por año] × [años + meses ÷ 12] = [días de indemnización]; [días de indemnización] × [salario diario] = [importe]». Redondea el salario diario a céntimos y usa ese mismo valor en toda la hoja. Cuando los días no sean exactos, escríbelos con cuatro decimales o como fracción (20 × 113 ÷ 12 = 188,3333): con dos decimales la operación escrita ya no da el importe al céntimo.

Si defiendes al trabajador y el cese ya se ha producido, la hoja y el resumen empiezan por la **fecha de caducidad** de la acción (art. 103 LRJS y apartado 6 del formato): días hábiles sin sábados, domingos ni festivos de la sede del órgano; el calendario de fiestas del año (boletín de la comunidad autónoma y fiestas locales del municipio) se busca en internet y se cita con su enlace.

1. **Datos de partida** (tabla): dato · valor · fuente (nómina, contrato, vida laboral, sentencia) · marcador si falta.
2. **Salario regulador** (tabla): concepto · importe anual · ¿salarial? (art. 26 ET) · fuente; total anual, salario diario (÷ 365) y mensualidad (÷ 12).
3. **Antigüedad** (tabla): periodo · desde · hasta · años · meses (fracción como mes) · tramo (anterior o posterior al 12/02/2012) · por qué computa.
4. **Indemnización por escenario** (tabla): escenario · precepto · operación · días · importe · tope aplicable · importe final.
5. **Topes**: tope en mensualidades × mensualidad, o en días × salario diario, y cuál se aplica.
6. **Salarios de tramitación** (si proceden): periodo · días · importe bruto · descuentos (nuevo empleo, desempleo) · parte de la empresa · parte reclamable al Estado.
7. **Readmisión irregular** (si procede): indemnización a la fecha del auto, adicional mínima y máxima, salarios.
8. **Comparativa para decidir**: escenarios en columnas; parte orientativamente exenta y sujeta (art. 7.e) LIRPF); garantía del FOGASA si hay insolvencia.
9. **Notas**: criterios adoptados (divisores, mensualidad, mes partido de 2012, conceptos incluidos y excluidos), doctrina con párrafo literal y ECLI, riesgos y datos pendientes. Indica que las retenciones y cotizaciones las aplica la nómina de liquidación.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos de cada escenario (ET, LRJS, LGSS y, si se usan, LIRPF, art. 33 ET y reales decretos de relaciones especiales), con su vigencia anotada.
- [ ] Disposición transitoria undécima: texto leído en el BOE consolidado (enlace y fecha de consulta) o en el párrafo literal de la Sala Cuarta que la transcribe, citado con su ECLI; `verificar_escrito` no comprueba esa disposición.
- [ ] Todo dato que no salga de Jurisprudenciator (disposiciones del ET que el conector no devuelve, tabla salarial) citado con enlace y fecha de consulta y señalado en el resumen.
- [ ] Salario regulador con todas las partidas salariales, sin las no salariales, y con la decisión sobre suspensiones, especie y jornada reducida explicada.
- [ ] Antigüedad con cada contrato anterior valorado y la fracción de mes tratada según la doctrina leída; en cadenas de temporales, huecos con su porcentaje, variantes calculadas y decisión sobre qué indemnizaciones cobradas se descuentan.
- [ ] Pagas prorrateadas sumadas una sola vez; meses de suspensión fuera del promedio de lo variable.
- [ ] Si se defiende al trabajador y ya hay cese: fecha de caducidad calculada con el calendario de festivos de la sede.
- [ ] Cada operación visible, con divisores declarados y redondeo a céntimos; topes comprobados en el texto de su artículo.
- [ ] Ninguna cifra de límite (salario mínimo, límite de exención, garantía del FOGASA) escrita sin haberla leído en esta conversación.
- [ ] Mejoras del convenio leídas con `leer_convenio` y su vigencia comprobada, o constancia de que no las hay.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`; en la indemnización adicional, párrafo de la mayoría.
- [ ] `verificar_escrito` pasado sobre las notas de la hoja; los avisos de «posible disonancia» contrastados con el apartado leído (salta cuando una frase mezcla varias materias: cita un artículo por frase).
- [ ] Marcadores (`[SALARIO BRUTO ANUAL]`, `[FECHA DE ANTIGÜEDAD]`) donde falte un dato; ningún importe inventado.
- [ ] Resumen para el abogado según el apartado 9 del formato: qué se ha calculado y para quién, cifras clave y de dónde sale cada una, plazos si los hay, datos que faltan, riesgos, jurisprudencia citada y próximo paso.
