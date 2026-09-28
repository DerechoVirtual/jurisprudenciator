---
name: resolucion-por-incumplimiento
description: >-
  Prepara en Word la comunicación que da por resuelto un contrato por incumplimiento (art. 1124 CC o
  cláusula resolutoria expresa) y un dictamen breve con jurisprudencia de la Sala Primera, para quien resuelve
  o para quien recibe la resolución. Úsala cuando el abogado diga «resolver el contrato», «dar por resuelto»,
  «incumplimiento esencial», «frustración del fin», «cláusula resolutoria», «devolución de lo pagado y daños»,
  «reclamar o moderar la cláusula penal» o «excepción de contrato no cumplido». Si solo se quiere exigir el
  cumplimiento o constituir en mora, usa requerimiento-cumplimiento; si el problema son defectos de la cosa
  vendida, vicios-ocultos-saneamiento; si las partes pactan la extinción, modificacion-novacion-cesion; antes
  de demandar, masc-propuesta-acuerdo.
---

# Resolución por incumplimiento

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Facultad resolutoria, mora recíproca y terceros** → `buscar_articulo` (`ley="CC"`, artículos `"1100"`, `"1124"` y `"1295"`) y, si hay inmueble inscrito, (`ley="BOE-A-1946-2453"`, `articulo="34"`).
- **Compraventa y arrendamiento** → `buscar_articulo` (`ley="CC"`, artículos `"1466"`, `"1467"`, `"1502"`, `"1504"` y `"1505"`), (`ley="CCom"`, artículos `"329"` y `"332"`) y (`ley="LAU"`, artículos `"27"` y `"35"`).
- **Daños y perjuicios** → `buscar_articulo` (`ley="CC"`, artículos `"1101"`, `"1102"`, `"1103"`, `"1105"`, `"1106"`, `"1107"` y `"1108"`).
- **Cláusula penal** → `buscar_articulo` (`ley="CC"`, artículos `"1152"`, `"1153"`, `"1154"` y `"1155"`); con consumidores, (`ley="TRLGDCU"`, artículos `"82"`, `"83"` y `"85"`).
- **Restitución y plazo de la acción** → `buscar_articulo` (`ley="CC"`, artículos `"1303"`, `"1964"` y `"1969"`).
- **Retención de pagos y compensación** → `buscar_articulo` (`ley="CC"`, `articulo="1196"`) y, si las dos partes son empresas, (`ley="BOE-A-2004-21830"`, artículos `"5"`, `"7"` y `"8"`) con el tipo del semestre (`novedades_boe` con `contiene="interés de demora"`, `desde` y `hasta` en una ventana de 31 días, y `leer_boe`).
- **Doctrina de la Sala Primera** (incumplimiento esencial y frustración del fin, resolución extrajudicial, cláusula resolutoria expresa, efectos restitutorios, moderación de la pena, excepción de contrato no cumplido, lucro cesante) → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CIVIL"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Partes que son sociedades** → `buscar_empresa_mercantil`; **inmuebles** → `consultar_catastro` (y nota simple del Registro de la Propiedad, que pide el abogado).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). Si `buscar_articulo` devuelve una nota «Téngase en cuenta…» seguida de un texto entre comillas, ese texto entrecomillado es la redacción anterior: aplica la que encabeza la respuesta.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Contrato con obligaciones recíprocas (compraventa, obra, servicios, suministro, distribución, arrendamiento, permuta) en el que una parte no cumple y la otra quiere liberarse, recuperar lo entregado y ser indemnizada.
- Contrato con cláusula resolutoria expresa o con cláusula penal que hay que activar o combatir.
- El cliente ha recibido una comunicación de resolución y hay que responderla: negar el incumplimiento, oponer la excepción de contrato no cumplido o pedir la moderación de la pena.

| Situación | Skill |
|---|---|
| Solo se quiere exigir el cumplimiento, constituir en mora o convertir el retraso en incumplimiento con un plazo | `requerimiento-cumplimiento` |
| La cosa entregada tiene defectos ocultos o no es la pactada (el plazo puede ser de caducidad) | `vicios-ocultos-saneamiento` |
| El incumplimiento se debe a un cambio imprevisible de circunstancias o hay que interpretar el contrato | `dictamen-interpretacion-contrato` |
| Las partes quieren extinguir de mutuo acuerdo | `modificacion-novacion-cesion` |
| Hay que intentar el acuerdo antes de demandar la resolución, la restitución o los daños | `masc-propuesta-acuerdo` |
| Solo queda una deuda dineraria documentada | `reclamacion-deuda-monitorio` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende el abogado: a quien quiere resolver o a quien recibe la resolución.
2. ★ Contrato íntegro con anexos: tipo, fecha, prestaciones de cada parte y sus plazos, cláusula resolutoria, cláusula penal, plazos de subsanación o preaviso, notificaciones, ley aplicable, fuero, mediación o arbitraje.
3. ★ Incumplimiento: qué obligación, cuándo debía cumplirse, qué ha pasado desde entonces, si es total, parcial, defectuoso o un retraso, y si el cumplimiento sigue siendo posible y útil para el cliente.
4. ★ Cumplimiento propio: qué ha cumplido el cliente, qué tiene pendiente y si hay reproches de la otra parte.
5. ★ Comunicaciones previas: requerimientos, respuestas, prórrogas concedidas, pagos o entregas aceptados después del vencimiento (pueden haber renunciado al término).
6. ★ Qué se ha entregado cada parte (precio, señal, bienes, obra) y en qué estado está; frutos, rentas o uso obtenidos.
7. ★ Daños: daño emergente con justificantes, lucro cesante y cómo se prueba.
8. Si es compraventa de inmueble: precio aplazado, condición resolutoria inscrita, nota simple, terceros adquirentes o acreedores hipotecarios.
9. Si una parte es consumidor y el contrato tiene condiciones generales; si aplica Derecho civil foral o autonómico (búscalo con `buscar_boe` y, si el conector no devuelve el precepto, léelo en internet en el texto consolidado oficial y cítalo con enlace).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

### 1. Presupuestos de la resolución (art. 1124 CC)

- **Obligaciones recíprocas**: la facultad de resolver está implícita en ellas; el perjudicado elige entre cumplimiento y resolución, con daños e intereses en ambos casos, y puede pasar a la resolución si el cumplimiento resulta imposible.
- **Legitimado**: quien ha cumplido o está dispuesto a cumplir; en obligaciones recíprocas nadie incurre en mora si el otro no cumple o no se allana a cumplir (art. 1100 CC, último párrafo). Si el cliente también incumple, dilo en el dictamen: la resolución puede volverse contra él.
- **Incumplimiento resolutorio**: la Sala Primera exige un incumplimiento grave o esencial, que frustre el fin del contrato o las legítimas expectativas de la otra parte; el mero retraso basta solo si el plazo era esencial o si, prolongado y sin reparación, frustra el fin. Busca la doctrina actual (consultas abajo) y aplica sus criterios al caso: entidad económica, obligación principal o accesoria, duración, reparación ofrecida.
- **Si el incumplimiento no es resolutorio** (retraso sin término esencial que no frustra el fin, defectos accesorios o subsanables, cumplimiento aprovechable en lo sustancial), dilo con claridad aunque el cliente quiera resolver: la resolución sería indebida y el cliente quedaría como incumplidor. No redactes la comunicación de resolución; el dictamen lo explica y propone la alternativa (requerimiento de subsanación con plazo, penalidad moratoria pactada, daños, pago de lo no discutido) y ofrece preparar el requerimiento con `requerimiento-cumplimiento`. Compara en una tabla los dos escenarios (resolver o la alternativa) con lo que paga, obtiene y arriesga el cliente.
- **Frustración del fin**: cuando el objeto deviene inhábil para su destino natural o pactado (licencias denegadas, cambios urbanísticos) puede resolverse aunque no haya culpa. Si en realidad es un cambio imprevisible de circunstancias, deriva a `dictamen-interpretacion-contrato`.
- **Plazo judicial**: el tribunal puede señalar plazo si hay causas justificadas (art. 1124, párrafo tercero). Esgrímelo si defiendes al incumplidor.
- **Terceros**: la resolución no perjudica a terceros adquirentes (art. 1124, último párrafo, con los arts. 1295 y 1298 CC y la Ley Hipotecaria): con inmueble inscrito, lee el art. 34 de la Ley Hipotecaria y pide nota simple.

### 2. Cómo se resuelve: extrajudicial o judicial

- La resolución puede declararse **extrajudicialmente** mediante comunicación recepticia a la otra parte, pero **a riesgo de quien resuelve**: si la otra parte la impugna, el tribunal revisa si el incumplimiento era resolutorio, y una resolución indebida convierte al que resolvió en incumplidor. Busca la doctrina y explícalo en el dictamen.
- El art. 1124 no exige un requerimiento previo con carácter general. Hazlo antes (con `requerimiento-cumplimiento`) cuando: el contrato pacte preaviso o plazo de subsanación; el incumplimiento sea un retraso que hay que convertir en definitivo; o la ley lo imponga.
- **Compraventa de inmueble por impago del precio**: aunque se pactara resolución de pleno derecho, el comprador puede pagar mientras no haya sido requerido judicialmente o por acta notarial (art. 1504 CC). El requerimiento resolutorio tiene esa forma o no vale.
- **Muebles**: resolución de pleno derecho a favor del vendedor si el comprador no se presenta a recibir o no ofrece el precio (art. 1505 CC); compraventa mercantil: arts. 329 y 332 CCom.
- **Arrendamientos urbanos**: causas de resolución de pleno derecho del art. 27.2 y 27.3 LAU (vivienda) y del art. 35 (uso distinto); por falta de pago, el cauce es el desahucio y el requerimiento del art. 22.4 LEC.
- **Cláusula resolutoria expresa**: define qué incumplimientos resuelven y cómo se comunica. No la des por automática: busca la doctrina sobre su interpretación y sobre si el tribunal sigue valorando la entidad del incumplimiento y la buena fe.
- **Antes de demandar** (declaración de resolución, restitución o daños): requisito de procedibilidad del art. 5 LO 1/2025; la comunicación de resolución no lo cumple por sí sola. Si el cliente va a litigar, ofrece incluir una invitación a negociar la liquidación o deriva a `masc-propuesta-acuerdo`.

### 3. Efectos: restitución y liquidación

- La resolución extingue el contrato y, como regla general, produce efectos retroactivos: las partes se restituyen recíprocamente lo recibido (doctrina de la Sala Primera: búscala). Cita los preceptos en que la apoye la sentencia que leas; el art. 1303 CC, escrito para la nulidad, solo si esa sentencia lo aplica. En contratos de tracto sucesivo, las prestaciones ya ejecutadas y equivalentes no se restituyen: busca la doctrina sobre eficacia retroactiva o hacia el futuro.
- Subsisten los pactos pensados para después de la extinción (confidencialidad, devolución o destrucción de información, fuero): léelos en el contrato y dilo en la comunicación.
- Liquida en una tabla: lo que cada parte debe devolver, frutos o uso, intereses desde cuándo, compensación entre créditos, y lo que queda a favor de cada una.

### 4. Daños y perjuicios

- Responde quien incumple con dolo, negligencia, morosidad o contraviniendo el contrato (art. 1101 CC). La responsabilidad por dolo no se puede renunciar (art. 1102); la de negligencia puede moderarse (art. 1103); el caso fortuito exonera salvo ley o pacto (art. 1105).
- Comprende el daño emergente y el lucro cesante (art. 1106). El deudor de buena fe responde de los daños previstos o previsibles al contratar que sean consecuencia necesaria; con dolo, de todos los que se deriven (art. 1107). En deudas de dinero, los intereses pactados o, en su defecto, el interés legal (art. 1108): si hay que cuantificarlo, toma el tipo de cada año del BOE en internet (Ley de Presupuestos Generales del Estado o su prórroga) y cítalo con enlace y fecha de consulta; nunca de memoria.
- El lucro cesante exige prueba de una ganancia probable, no meramente posible: busca la doctrina y pide al abogado la base documental o pericial.

### 5. Cláusula penal

- Sustituye a la indemnización de daños salvo pacto de acumulación (art. 1152 CC); el acreedor no puede exigir a la vez cumplimiento y pena sin facultad clara, ni el deudor liberarse pagando la pena salvo reserva expresa (art. 1153); la nulidad de la pena no anula la obligación principal (art. 1155).
- **Moderación** (art. 1154): solo cuando la obligación se cumplió en parte o irregularmente. La Sala Primera no modera si el incumplimiento producido es precisamente el que la pena preveía, y se ha mostrado dispuesta a admitir una reducción de las penas extraordinariamente excesivas desde la perspectiva de cuando se pactaron, con la carga de probarlo sobre quien se opone. Busca y cita la doctrina vigente.
- **Consumidores**: la indemnización desproporcionadamente alta impuesta al consumidor que incumple es abusiva (art. 85 TRLGDCU, apartado 6) y nula (art. 83). Si la pena es abusiva, no pidas su moderación sino que se tenga por no puesta: busca la doctrina (`consulta="cláusula penal consumidor indemnización desproporcionadamente alta abusiva"` y `consulta="cláusula abusiva consumidor no cabe moderación ni integración se tiene por no puesta"`, ambas con `base="TS"`, `jurisdiccion="CIVIL"`). Si hay condiciones generales, deriva el análisis a `condiciones-generales-consumidores`.
- Según la posición: si defiendes al acreedor, sostén que se produjo el incumplimiento previsto y que la pena era proporcionada ex ante; si defiendes al deudor, acredita el cumplimiento parcial, que el incumplimiento no es el previsto, la desproporción extraordinaria o la abusividad.

### 6. Excepción de contrato no cumplido

Quien recibe la reclamación puede negarse a cumplir mientras la otra parte no cumpla lo suyo si las prestaciones son simultáneas o la otra debía cumplir antes (art. 1100, último párrafo; en compraventa, arts. 1466, 1467 y 1502 CC). La Sala Primera exige que lo incumplido sea una obligación básica: el cumplimiento defectuoso o de prestaciones accesorias no ampara retener todo el pago (busca la doctrina y distingue en el dictamen entre incumplimiento total y cumplimiento defectuoso). En ese caso recomienda pagar lo no discutido, descontar solo lo que sea líquido y esté pactado como descontable (una penalidad, art. 1196 CC) y reclamar el resto. Si las dos partes son empresas, quien retiene un pago vencido está en mora automática con el interés de la Ley 3/2004 y los 40 euros de costes de cobro: cuantifícalo con el tipo del semestre.

### 7. Plazo de la acción

- Acción personal: cinco años desde que pudo exigirse el cumplimiento (arts. 1964.2 y 1969 CC). Si la obligación nació antes del 7 de octubre de 2015, hay régimen transitorio: búscalo con `buscar_boe` (Ley 42/2015); si el conector no lo devuelve, léelo en internet en el BOE y cítalo con enlace y fecha de consulta; nunca calcules ese tramo de memoria.
- La acción de resolución por incumplimiento no está sujeta a los plazos de caducidad del saneamiento cuando se entrega cosa distinta o inhábil (deriva a `vicios-ocultos-saneamiento` para decidir la vía).
- Da la fecha inicial, el precepto y la fecha final calculada (apartado 9 del formato).

## Jurisprudencia: qué buscar y cómo usarla

Es imprescindible (apartado 8 del formato): el dictamen no se entrega sin doctrina aplicable. Consultas, todas con `base="TS"` y `jurisdiccion="CIVIL"` salvo que se indique; reformula como máximo dos veces:

- Esencialidad: `consulta="resolución artículo 1124 incumplimiento esencial frustración del fin del contrato"`, `anios=5`; y `consulta="valoración de la gravedad del incumplimiento resolución 1124 retraso"`.
- Resolución extrajudicial: `consulta="resolución extrajudicial declaración recepticia incumplimiento resolutorio resolución indebida"`.
- Cláusula resolutoria expresa: `consulta="cláusula resolutoria expresa gravedad del incumplimiento buena fe interpretación"`.
- Venta de inmueble: `consulta="requerimiento resolutorio artículo 1504 requerimiento notarial pago posterior"`.
- Efectos: `consulta="efectos de la resolución del contrato restitución recíproca de las prestaciones retroactivos"` y `consulta="resolución contratos de tracto sucesivo efectos ex nunc prestaciones ejecutadas"`.
- Pena: `consulta="moderación cláusula penal artículo 1154 incumplimiento previsto por las partes"` y `consulta="cláusula penal reducción conservadora penalidad extraordinariamente excesiva"`.
- Excepción: `consulta="exceptio non adimpleti contractus"` y, si el otro cumplió mal, `consulta="excepción non rite adimpleti contractus cumplimiento defectuoso"` y `consulta="cumplimiento defectuoso retención del precio pendiente proporcionada a la entidad de los defectos contrato de obra"`.
- Incumplimiento no resolutorio: `consulta="retraso que no frustra el fin del contrato incumplimiento accesorio defectuoso no comporta la resolución"`.
- Lucro cesante: `consulta="lucro cesante prueba ganancias dejadas de obtener incumplimiento contractual probabilidad"`.
- Si el pleito será en una plaza concreta y la Sala Primera no resuelve el punto: las mismas consultas con `base="AN"`, `tipo_organo="AP"` y `provincia`, diciendo que es doctrina de Audiencia.

Lee con `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión) solo lo que vayas a citar. Transcribe el párrafo de fundamentos, nunca los hechos ni los nombres de aquel pleito, y comprueba que es razonamiento de la Sala y no la alegación de una parte. Prefiere lo reciente; cita una sentencia antigua solo si fija la doctrina.

## Documentos que se entregan

En la comunicación y en el dictamen, nombra las normas como pide el apartado 6 del formato («artículo 1124 del Código Civil», «artículo 329 del Código de Comercio», «artículo 27 de la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos», «artículo 85 del Real Decreto Legislativo 1/2007»), cada artículo con su norma: así los reconoce `verificar_escrito`.

**1. Comunicación de resolución** (`burofax-resolucion-<destinatario>-<AAAAMMDD>.docx`), solo si el dictamen concluye que el incumplimiento es resolutorio; sin jurisprudencia, maquetada según el apartado 5 del formato:

1. Remitente y destinatario con domicilio; lugar, fecha y medio de envío (acta notarial si es el art. 1504 CC).
2. Hechos numerados: contrato y cláusulas, obligación incumplida con fechas, requerimientos y respuestas previos, cumplimiento propio.
3. Declaración inequívoca de voluntad de resolver, con el fundamento (art. 1124 CC o la cláusula resolutoria, identificada) y la fecha de efectos.
4. Liquidación: qué debe restituir cada parte, cómo, dónde y en qué plazo; cuantía o reserva de los daños; cláusula penal si se reclama.
5. Pactos que subsisten tras la extinción.
6. Invitación a negociar la liquidación, si el cliente irá a juicio (sin cifras de transacción).
7. Reserva de acciones y firma.

Para quien recibe la resolución: **contestación** (`contestacion-resolucion-<remitente>-<AAAAMMDD>.docx`) que niega la esencialidad o el incumplimiento, opone la excepción si procede, ofrece o exige el cumplimiento, pide la moderación o niega la pena y reserva acciones por resolución indebida.

**2. Dictamen breve** (`dictamen-resolucion-<parte-principal>-<AAAAMMDD>.docx`, 3-6 páginas), que se entrega siempre y, si se desaconseja resolver, es el único documento: cuestión planteada y conclusión al principio; hechos relevantes; régimen aplicable con artículos leídos; análisis de la esencialidad con el párrafo literal, órgano, fecha y ECLI de cada resolución; vía recomendada (extrajudicial o judicial) y riesgo de resolución indebida; efectos y tabla de liquidación; daños y cláusula penal con su doctrina; plazos; datos y documentos pendientes; próximos pasos (MASC y demanda).

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió; ninguna consulta imprescindible quedó sin resultado, y lo que Jurisprudenciator no tenía se obtuvo de una fuente oficial en internet, con enlace y fecha de consulta, y se señala en el resumen.
- [ ] Leídos con `buscar_articulo` en esta conversación CC 1100, 1124, 1101, 1106, 1107 y, según el caso, 1152-1155, 1504, 1505, CCom 329, LAU 27 o 35, TRLGDCU 82, 83 y 85, Ley Hipotecaria 34 y CC 1964; anotada su línea de vigencia.
- [ ] Posición del cliente clara y cumplimiento propio comprobado antes de resolver.
- [ ] Si el incumplimiento no es resolutorio: no se ha redactado la comunicación de resolución, el dictamen lo dice al principio y propone la alternativa con sus importes.
- [ ] Incumplimiento calificado con la doctrina actual de la Sala Primera, con párrafo literal; cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] Forma de la comunicación adecuada al supuesto (acta notarial para el art. 1504 CC) y fecha de efectos expresada.
- [ ] Tabla de restitución y daños coherente con el contrato; cláusula penal analizada desde la posición del cliente.
- [ ] Plazo de la acción con fecha inicial, precepto y fecha final; régimen transitorio señalado si la obligación es anterior al 7 de octubre de 2015.
- [ ] `verificar_escrito` pasado sobre la comunicación y sobre el dictamen; avisos de «posible disonancia» contrastados con el texto leído.
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[DOMICILIO]`, `[IMPORTE]`, `[DATOS REGISTRALES]`) en lugar de datos inventados; importes, fechas y definiciones coherentes.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cómo se resuelve cada punto crítico, datos que faltan y riesgos, tabla de jurisprudencia, plazos y próximo paso.
