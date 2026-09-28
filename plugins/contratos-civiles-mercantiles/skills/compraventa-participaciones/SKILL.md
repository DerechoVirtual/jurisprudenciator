---
name: compraventa-participaciones
description: >-
  Redacta la compraventa de participaciones (SL) o acciones (SA), con minuta del documento público y nota para
  el abogado: régimen legal y estatutario de transmisión, forma, precio fijo o con ajustes (deuda neta, capital
  circulante, earn-out), manifestaciones y garantías del vendedor y su régimen de responsabilidad (umbral,
  franquicia, plazo, tope), retención o depósito, condiciones suspensivas, gestión interina, no competencia del
  vendedor y comprobación registral de la sociedad. Úsala cuando el abogado diga «vender la empresa»,
  «compraventa de participaciones», «compra de acciones», «SPA», «share deal», «manifestaciones y garantías» o
  «earn-out». Para el pacto con los socios que quedan, usa pacto-de-socios; para vender solo un inmueble,
  compraventa-inmueble; para revisar el borrador de la otra parte, revision-contrato-semaforo.
---

# Compraventa de participaciones o acciones

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Régimen de transmisión y forma** → `buscar_articulo` (`ley="LSC"`, artículos `"104"`, `"106"`, `"107"`, `"108"`, `"111"`, `"112"` y `"190"` para la SL; `"116"`, `"118"`, `"120"`, `"122"` y `"123"` para la SA; `"88"`, `"126"`, `"127"` y `"160"` si hay prestaciones accesorias, cotitularidad, usufructo o venta de un activo esencial) y el Reglamento del Registro Mercantil (`ley="BOE-A-1996-17533"`, artículos `"188"` y `"123"`) para leer las cláusulas estatutarias.
- **Compraventa, saneamiento, vicios del consentimiento e incumplimiento** → `buscar_articulo` (`ley="CC"`, artículos `"1445"`, `"1447"`, `"1449"`, `"1450"`, `"1474"`, `"1484"`, `"1486"`, `"1490"`, `"1529"`, `"1532"`, `"1266"`, `"1269"`, `"1270"`, `"1301"`, `"1101"`, `"1102"`, `"1106"`, `"1107"`, `"1124"` y `"1964"`) y, si la venta es mercantil, (`ley="CCom"`, artículos `"325"`, `"342"` y `"345"`).
- **Condiciones, precio variable y cláusula penal** → `buscar_articulo` (`ley="CC"`, artículos `"1113"`, `"1115"`, `"1119"`, `"1120"`, `"1256"`, `"1152"`, `"1153"` y `"1154"`).
- **Pago con fondos o garantías de la sociedad y autocartera** → `buscar_articulo` (`ley="LSC"`, artículos `"140"`, `"143"`, `"146"` y `"150"`).
- **Autorizaciones y riesgos externos** → concentraciones (`ley="Ley 15/2007"`, artículos `"7"`, `"8"` y `"9"`); inversiones extranjeras (`ley="BOE-A-2003-13471"`, `articulo="7 bis"`); rescisión concursal si el vendedor es insolvente (`ley="TRLC"`, artículos `"226"` y `"227"`); tributación de la transmisión de valores (`ley="BOE-A-2023-7053"`, `articulo="338"`); pagos en efectivo (`ley="BOE-A-2012-13416"`, `articulo="7"`).
- **Doctrina sobre manifestaciones y garantías, saneamiento en la venta de acciones, ajustes de precio y no competencia** → `buscar_sentencias` (`jurisdiccion="CIVIL"`, `base="TS"`; Audiencias con `base="AN"` y `tipo_organo="AP"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **La sociedad objeto y las partes que son sociedades** → `buscar_empresa_mercantil` (denominación o CIF): existencia, estado, administradores y apoderados vigentes, últimos actos (disolución, concurso, ampliaciones y reducciones de capital, cambios de administradores).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...).

Dos trampas comprobadas con `verificar_escrito`: la Ley 19/2003 la toma por la ley autonómica del taxi aunque se escriba su título completo (cita el art. 7 bis como «artículo 7 bis de la Ley 19/2003, de 4 de julio, sobre régimen jurídico de los movimientos de capitales», compruébalo con `buscar_articulo` y el identificador `BOE-A-2003-13471` e ignora el veredicto del verificador sobre él); y el Reglamento del Registro Mercantil solo lo reconoce como «Real Decreto 1784/1996, de 19 de julio».

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Venta de la totalidad o de parte del capital de una SL o una SA no cotizada, con firma y cierre simultáneos o diferidos.
- Entrada de un socio comprando participaciones existentes (si entra suscribiendo una ampliación, el acuerdo de inversión sigue esta misma lógica de manifestaciones y garantías, pero la operación societaria la decide el abogado).
- Contrato privado previo a la escritura o póliza, o minuta completa para el notario.

| Situación | Skill |
|---|---|
| Reglas entre el comprador y los socios que siguen | `pacto-de-socios` (como anexo o documento aparte) |
| Se vende un inmueble y no la sociedad | `compraventa-inmueble` |
| Se transmite el negocio como conjunto de activos (compraventa de empresa por activos) | Esta skill no cubre la transmisión de activos y pasivos uno a uno: díselo al abogado |
| Carta de intenciones o confidencialidad previa a la due diligence | `confidencialidad-nda` |
| Informe de riesgos sobre el borrador del otro lado, o contrapropuesta | `revision-contrato-semaforo`, `negociacion-contrapropuesta` |
| El comprador reclama por una manifestación falsa o un pasivo oculto | `requerimiento-cumplimiento`, `resolucion-por-incumplimiento`, `vicios-ocultos-saneamiento` |
| Precio aplazado documentado como préstamo o reconocimiento de deuda | `prestamo-reconocimiento-deuda` |
| Poderes, capacidad o concurso de quien firma | `verificacion-partes-contrato` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ **A quién defiende el abogado**: vendedor o comprador. Si hay varios vendedores, si responden de forma solidaria o mancomunada y en qué proporción.
2. ★ **Sociedad objeto**: denominación, CIF, tipo social. Consulta `buscar_empresa_mercantil` y anota estado, administradores y actos recientes; si aparece disolución, concurso o una reducción de capital reciente, díselo al abogado antes de seguir. Pide los **estatutos vigentes**, el libro registro de socios o de acciones nominativas y el título de adquisición de cada vendedor.
3. ★ **Objeto**: número, numeración y clase de participaciones o acciones, porcentaje del capital, si están representadas por títulos o anotaciones en cuenta, y cargas (prenda, usufructo, embargo, opciones).
4. ★ **Vendedores y compradores**: si son personas físicas, régimen económico matrimonial (si las participaciones son gananciales, la venta exige el consentimiento de ambos cónyuges, art. 1377 CC) y vecindad civil (si es foral, busca la norma con `buscar_boe`; si no aparece, léela en internet en el texto consolidado oficial, como dice el punto 3 de la puerta); si son sociedades, quién firma y con qué poder, y si lo vendido o comprado es un activo esencial (art. 160.f LSC: acuerdo de junta). Si el comprador es de fuera de la UE o de la AELC, o tiene un titular real de fuera de ese ámbito, anótalo para el art. 7 bis de la Ley 19/2003.
5. ★ **Precio**: fijo con fecha de referencia (caja cerrada) o con ajuste al cierre (deuda neta, capital circulante), parte aplazada, earn-out (métrica, periodo, fórmula), forma de pago y garantías del pago.
6. ★ **Calendario**: firma y cierre simultáneos o diferidos; condiciones suspensivas (autorización de competencia o de inversiones exteriores, renuncia a la adquisición preferente, consentimientos de terceros por cambio de control, financiación) y fecha límite.
7. ★ **Due diligence**: si se ha hecho, sobre qué áreas, qué contingencias salieron y si hay sala de datos y carta de revelación.
8. **Manifestaciones y garantías** que el comprador exige y las que el vendedor acepta; indemnidades específicas por contingencias conocidas.
9. **Límites de responsabilidad**: umbral por reclamación, franquicia (deducible o de primer euro), tope, plazos; retención o depósito del precio.
10. **Vendedor tras el cierre**: si sigue como directivo o consultor; no competencia y no captación (ámbito y duración).
11. Gastos, ley aplicable, tribunales o arbitraje.

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo y anota la línea de vigencia.

**1. Transmisión de participaciones (SL).** Compara los estatutos con el art. 107 LSC:
- Salvo que los estatutos digan otra cosa, es libre entre socios y a favor del cónyuge, ascendientes, descendientes y sociedades del grupo.
- En los demás casos rigen los estatutos y, en su defecto, el régimen supletorio del art. 107.2: comunicación a los administradores, consentimiento de la junta, derecho de la sociedad a presentar adquirentes de la totalidad y libre transmisión si pasan tres meses sin respuesta.
- El régimen aplicable es el vigente al comunicar el propósito de transmitir (art. 111); la transmisión que no se ajuste a la ley o a los estatutos no produce efecto frente a la sociedad (art. 112).
- Si hay prestaciones accesorias, hace falta autorización de la sociedad (art. 88); si hay usufructo o cotitularidad, lee los arts. 126 y 127.
- Conflicto de intereses: el socio no puede votar el acuerdo que le autoriza a transmitir participaciones sujetas a una restricción legal o estatutaria, y sus participaciones se deducen para calcular la mayoría (art. 190.1.a y 190.2 LSC). Si venden varios socios, el consentimiento de la junta se adopta con un acuerdo por cada transmitente, sin su voto; no redactes «con el voto de todos los vendedores».
- Consecuencia: prevé en el contrato la comunicación estatutaria, la renuncia expresa de los demás socios a su adquisición preferente o el acuerdo de junta (con la regla anterior), y conviértelo en condición del cierre.

**2. Forma.** La transmisión de participaciones y la prenda sobre ellas deben constar en documento público (art. 106.1 LSC); el adquirente ejerce los derechos de socio desde que la sociedad conoce la transmisión (art. 106.2) y la sociedad solo reputa socio a quien figura en el libro registro (art. 104). Redacta el contrato privado como compraventa perfecta (art. 1450 CC) con obligación de otorgar el documento público en el cierre, y entrega la minuta. Busca doctrina sobre el valor del documento privado si el abogado lo necesita (`consulta="transmisión de participaciones sociales documento privado eficacia entre las partes documento público"`, `base="TS"`); si no aparece nada aplicable, redacta sobre el texto del art. 106 y dilo en la nota.

**3. Transmisión de acciones (SA).** Sin títulos impresos, las acciones se transmiten conforme a la cesión de créditos; con títulos, por endoso las nominativas y conforme al art. 545 del Código de Comercio las al portador; los administradores inscriben la transmisión en el libro-registro (arts. 116 y 120 LSC). Si están representadas por anotaciones en cuenta, se transmiten por transferencia contable (lee el art. 118 LSC y díselo al abogado). Restricciones estatutarias: art. 123 LSC y art. 123 del Real Decreto 1784/1996.

**4. Saneamiento, manifestaciones y garantías.** El régimen legal no protege bien al comprador de una sociedad: la acción por vicios ocultos se extingue a los seis meses de la entrega (art. 1490 CC), la venta mercantil tiene su propio plazo de denuncia (art. 342 CCom) y quien vende en globo un conjunto de derechos responde de la legitimidad del todo, no de cada parte (art. 1532 CC). Busca y lee la doctrina antes de redactar (imprescindible):
- `consulta="compraventa de empresa manifestaciones y garantías del vendedor cláusula de indemnización no saneamiento vicios ocultos"` (`base="TS"`) y `consulta="garantía de pasivos ocultos compraventa de acciones"` (`base="TS"`);
- `consulta="garantía de pasivos ocultos contingencias compraventa de participaciones reclamación vendedor"` (`base="AN"`, `tipo_organo="AP"`, `anios=6`) y `consulta="manifestaciones y garantías compraventa de participaciones plazo caducidad 1490"` (`base="AN"`, `tipo_organo="AP"`).
En las pruebas, la Sala Primera distingue: cuando se compran acciones, los defectos del patrimonio social no convierten por sí solos lo entregado en cosa distinta de la pactada; cuando el contrato configura como objeto la empresa y el vendedor garantiza su situación financiera, la información falsa es incumplimiento contractual indemnizable conforme al art. 1101 CC, sin que la indemnización quede limitada por el precio. Consecuencias de redacción:
- Si defiendes al comprador, deja escrito en el expositivo y en el objeto que se adquiere la sociedad y su negocio, y que el precio se ha fijado sobre la veracidad de las manifestaciones; si defiendes al vendedor, que el objeto son las participaciones.
- Configura las manifestaciones y garantías como obligación autónoma de indemnizar, al amparo del art. 1255 CC.
- Excluye expresamente el saneamiento legal y sus plazos (arts. 1484 a 1490 CC y 342 CCom) y fija plazos propios.
- Deja claro que el remedio pactado es el exclusivo, salvo dolo: la responsabilidad por dolo no se puede renunciar (art. 1102 CC).
- Recuerda al abogado que el comprador engañado puede pedir además la nulidad por error o dolo (arts. 1266, 1269 y 1270 CC; caducidad de cuatro años desde la consumación, art. 1301) y que la acción personal sin plazo especial prescribe a los cinco años (art. 1964.2 CC): si se pactan plazos más cortos para reclamar, dilo en la nota.

**5. Precio.**
- Debe ser cierto: vale la referencia a otra cosa cierta o el señalamiento por persona determinada (art. 1447 CC), nunca el arbitrio de una de las partes (arts. 1449 y 1256 CC). Por eso el ajuste y el earn-out se definen con reglas contables cerradas, estados de referencia, plazo de revisión y un experto independiente que resuelve las discrepancias. Si el experto no puede o no quiere señalarlo, el art. 1447 deja el contrato ineficaz: prevé un sustituto y quién lo designa.
- En el earn-out, si el comprador impide el hito voluntariamente, la condición se tiene por cumplida (art. 1119 CC): el vendedor debe pedir reglas de gestión del negocio durante el periodo; el comprador, libertad de gestión con un límite de buena fe.
- Busca doctrina sobre ajustes: `consulta="compraventa de participaciones sociales saneamiento vicios ocultos patrimonio de la sociedad"` (`base="TS"`; en las pruebas localizó un litigio por no practicar los ajustes contables que fijaban el precio definitivo) y `consulta="earn-out precio variable compraventa de participaciones resultados"` (`base="AN"`, `tipo_organo="AP"`).

**6. Pago con fondos o garantías de la sociedad.** La SL no puede anticipar fondos, prestar ni garantizar para la adquisición de sus propias participaciones (art. 143.2 LSC); la SA tampoco, con las excepciones del art. 150. No admitas que el precio aplazado se garantice con bienes de la sociedad objeto ni que se pague con su tesorería antes del cierre sin analizarlo; la compra por la propia sociedad solo cabe en los casos del art. 140 (SL) o del art. 146 (SA).

**7. Condiciones suspensivas y fecha límite.** Arts. 1113, 1115 (una condición que dependa de la sola voluntad del deudor anula la obligación), 1119 y 1120 CC. Revisa siempre:
- Concentraciones: si la operación da control (art. 7 de la Ley 15/2007) y supera los umbrales del art. 8, debe notificarse y no puede ejecutarse antes de la autorización (art. 9). La gestión interina no puede dar al comprador el control antes de tiempo.
- Inversiones exteriores: si el comprador encaja en el art. 7 bis.1 de la Ley 19/2003 y la sociedad opera en los sectores de su apartado 2 o concurre su apartado 3, la operación necesita autorización previa y sin ella carece de validez y efectos (art. 7 bis.5). No lo descartes sin leer el artículo con los datos del caso.
- Adquisición preferente, consentimiento de la sociedad y consentimientos de terceros por cambio de control en contratos clave.

**8. Situación del vendedor y de la sociedad.** Con `buscar_empresa_mercantil`, busca concurso, disolución y ceses recientes. Si el vendedor está en dificultades, la venta puede rescindirse si se declara su concurso en los dos años siguientes y la operación perjudica a la masa (arts. 226 y 227 TRLC): pide al abogado información sobre su solvencia y recomienda precio de mercado justificado y pago al contado.

**9. Tributación y pago.** Lee el art. 338 de la Ley 6/2023 (exención de la transmisión de valores y sus excepciones cuando se adquiere el control de sociedades cuyo activo es mayoritariamente inmobiliario) y díselo al abogado si la sociedad tiene inmuebles; no des tipos ni importes. Para la ganancia patrimonial del vendedor o el impuesto del comprador, remite a `buscar_consultas_hacienda`. Lee el art. 7 de la Ley 7/2012 antes de admitir pagos en efectivo.

## Cláusulas clave y jurisprudencia

Para cada cláusula: redacción según a quién defiendas, riesgo y búsqueda. La jurisprudencia es **imprescindible** (apartado 8 del formato) para las manifestaciones y garantías y su régimen de responsabilidad, la no competencia del vendedor y la cláusula penal.

1. **Objeto y titularidad.** Participaciones identificadas por numeración, libres de cargas y con todos sus derechos económicos desde el cierre; quién cobra los dividendos acordados antes. Comprador: manifestación de titularidad plena y ausencia de opciones. Vendedor: nada más allá de lo que conste en el libro registro.
2. **Precio y ajustes.** Comprador: ajuste por deuda neta y capital circulante sobre cuentas de cierre preparadas por él, con experto en caso de discrepancia. Vendedor: caja cerrada con fecha de referencia y prohibición de fugas de valor definida («fuga permitida» cerrada), sin ajuste posterior. En los dos casos, definiciones contables en un anexo y un ejemplo numérico.
3. **Earn-out.** Vendedor: métrica objetiva (ventas o EBITDA con reglas fijadas), información mensual, prohibición de actos que lo frustren, aceleración si el comprador vende o integra la sociedad. Comprador: tope, periodo corto, compensación con reclamaciones por garantías.
4. **Pago y garantías del pago.** Vendedor: todo al cierre; si hay aplazado, aval a primer requerimiento o prenda sobre las participaciones vendidas en documento público (art. 106.1 LSC). Comprador: retención de una parte o depósito (notarial o bancario) para cubrir reclamaciones, con reglas de liberación por tramos. No des aranceles ni comisiones de memoria: las comisiones las fija la entidad; los aranceles notariales, si el abogado los pide, búscalos en internet en su norma oficial (BOE) y cítalos con enlace y fecha de consulta.
5. **Condiciones suspensivas y fecha límite.** Quién hace cada gestión, plazo, renuncia solo por la parte a quien beneficia, y efecto si no se cumplen (el contrato queda sin efecto sin indemnización, salvo incumplimiento del deber de colaborar).
6. **Gestión interina.** Entre firma y cierre, la sociedad sigue su curso ordinario; lista de actos que requieren consentimiento del comprador (endeudamiento, contratación, dividendos, venta de activos). Límite: sin que el comprador asuma el control antes de la autorización de competencia.
7. **Cierre.** Entregables: escritura o póliza, renuncias o acuerdo de junta, certificación del libro registro, dimisiones y nombramientos de administradores, pago y liberación de garantías personales del vendedor.
8. **Manifestaciones y garantías.** Por áreas: capacidad y titularidad; sociedad y capital; cuentas; ausencia de pasivos no contabilizados; fiscal; laboral y Seguridad Social; contratos relevantes y cambio de control; litigios; propiedad intelectual e industrial; protección de datos; cumplimiento normativo; inmuebles y medio ambiente. Comprador: a la firma y repetidas al cierre, sin cualificación de conocimiento, y con cláusula de que su conocimiento o la due diligence no excluyen la reclamación. Vendedor: cualificación «a su leal saber», información revelada en la sala de datos y en la carta de revelación excluida, solo a la firma. Busca: `consulta="conocimiento del comprador due diligence manifestaciones y garantías vendedor responsabilidad"` (`base="AN"`, `tipo_organo="AP"`).
9. **Régimen de indemnización.** Indemnización euro por euro de los daños de la sociedad o del comprador (define «Daño» y si se reduce por el porcentaje adquirido); umbral por reclamación y franquicia (deducible o de primer euro); tope en porcentaje del precio; plazos (general más corto; fiscal, laboral y de Seguridad Social ligados a la prescripción del tributo o de la deuda, que el abogado debe comprobar); procedimiento de reclamaciones de terceros con dirección de la defensa; deber de mitigar; sin duplicidades con los ajustes de precio; exclusión expresa de los arts. 1484 a 1490 CC y del art. 342 CCom; ninguna limitación se aplica al dolo (art. 1102 CC). Vendedor: todos los límites y remedio exclusivo. Comprador: sin franquicia para titularidad y fiscal, tope alto, retención.
10. **Indemnidades específicas.** Para cada contingencia conocida en la due diligence, indemnidad concreta sin umbral ni franquicia y con su propio plazo, en vez de ajustar el precio.
11. **No competencia y no captación del vendedor.** Imprescindible: `consulta="obligación de no competencia del vendedor de participaciones sociales duración"` (`base="TS"`) y `consulta="compraventa de participaciones pacto de no competencia del vendedor restricción accesoria duración"` (`base="AN"`, `tipo_organo="AP"`). Comprador: ámbito material y territorial de la actividad de la sociedad, duración suficiente para proteger el fondo de comercio adquirido. Vendedor: duración corta, actividad concreta, sin incluir inversiones financieras. Si el vendedor sigue como trabajador, coordina con el art. 21.2 del Estatuto de los Trabajadores (`ley="ET"`).
12. **Cláusula penal.** Si se pacta por incumplir la no competencia o el cierre, di si es sustitutiva o cumulativa (arts. 1152 y 1153 CC). Imprescindible: `consulta="cláusula penal moderación improcedente cuando el incumplimiento es el previsto"` (`base="TS"`).
13. **Resolución.** Antes del cierre, por incumplimiento esencial o falsedad grave de las manifestaciones; después del cierre, solo indemnización (evita deshacer la operación). Base: art. 1124 CC.
14. **Confidencialidad, anuncios, gastos e impuestos, notificaciones, cesión, ley y tribunales o arbitraje.**

## Documentos que se entregan

Según `references/formato-y-entrega-contratos.md`, dos documentos:

1. `contrato-compraventa-participaciones-<sociedad>-<AAAAMMDD>.docx` (o `compraventa-acciones`):
   - Título, lugar y fecha; REUNIDOS e INTERVIENEN (con poderes y, si procede, consentimiento del cónyuge).
   - EXPONEN: sociedad, capital, titularidad de cada vendedor, due diligence realizada y régimen estatutario de transmisión.
   - ESTIPULACIONES, en este orden: definiciones; objeto; precio y ajustes; earn-out; pago y garantías del pago; condiciones suspensivas y fecha límite; gestión interina; cierre; manifestaciones y garantías del vendedor y del comprador; régimen de indemnización; indemnidades específicas; no competencia y no captación; resolución; cláusula penal; confidencialidad y anuncios; gastos e impuestos; notificaciones; cesión; ley y tribunales o arbitraje; integridad.
   - Anexos: participaciones vendidas y titulares; manifestaciones y garantías; carta de revelación; reglas contables y ejemplo numérico de ajuste; entregables del cierre; **minuta del documento público de compraventa** con la comparecencia, la manifestación de cumplimiento del régimen estatutario (renuncias o acuerdo de junta) y el pago.
2. `nota-compraventa-participaciones-<sociedad>-<AAAAMMDD>.docx`:
   - Régimen aplicable con los artículos leídos: qué es imperativo (forma, régimen estatutario, asistencia financiera, dolo) y qué pactable.
   - Estado registral de la sociedad según `buscar_empresa_mercantil` (informativo, sin fe pública: recomienda nota del Registro Mercantil).
   - Por cada cláusula crítica, qué dice, por qué y su base: artículo y, cuando proceda, párrafo literal con órgano, fecha y ECLI.
   - Autorizaciones que pueden hacer falta (competencia, inversiones exteriores) y por qué.
   - Riesgos fiscales a comprobar, sin cifras; datos y documentos pendientes.

Marcadores para lo que falte: `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[DATOS REGISTRALES]`, `[NÚMEROS DE LAS PARTICIPACIONES]`, `[NOMBRE Y APELLIDOS]`, `[DNI/NIE]`, `[DOMICILIO]`, `[IMPORTE]`, `[IBAN]`, `[FECHA DE REFERENCIA]`.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Sociedad objeto y partes sociedad comprobadas con `buscar_empresa_mercantil`; concurso, disolución o firmantes sin cargo vigente, dichos en la nota.
- [ ] Estatutos cotejados con los arts. 107 y 108 LSC (o 123 en la SA); la renuncia a la adquisición preferente o el acuerdo de junta figura como condición del cierre.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos usados del CC, la LSC, el CCom y, si proceden, la Ley 15/2007, el art. 7 bis de la Ley 19/2003 (por `BOE-A-2003-13471`), el TRLC y la Ley 6/2023.
- [ ] Doctrina sobre manifestaciones y garantías, no competencia y cláusula penal leída con `leer_sentencias` (párrafo de fundamentos); cada ECLI citado, leído o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el contrato, la minuta y la nota; corregido lo que señale y anotado el falso aviso sobre la Ley 19/2003.
- [ ] Precio, ajustes, umbral, franquicia, tope y plazos coherentes entre cláusulas y anexos; definiciones únicas; marcadores en lugar de datos inventados.
- [ ] Resumen para el abogado según el apartado 10 del formato: qué se ha preparado y para quién, cláusulas críticas y cómo se resolvieron, autorizaciones y condiciones, documentos que faltan (estatutos, libro registro, títulos, poderes, consentimiento del cónyuge), tabla de jurisprudencia, plazos de reclamación pactados y próximo paso (renuncias, firma, notaría).
