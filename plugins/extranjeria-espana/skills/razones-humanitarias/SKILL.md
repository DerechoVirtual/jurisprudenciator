---
name: razones-humanitarias
description: >-
  Prepara la solicitud de autorización de residencia temporal por circunstancias excepcionales por razones
  humanitarias (art. 128 del Real Decreto 1155/2024) o por colaboración con autoridades, seguridad
  nacional o interés público (arts. 129 y 142 a 147), con memoria justificativa en Word. Úsala cuando el
  abogado diga «enfermedad grave sobrevenida», «tratamiento que no existe en su país», «víctima de un
  delito de odio o contra los trabajadores», «volver a pedir el visado es peligroso», «colabora con la
  policía o con la Inspección de Trabajo», «trabajó sin papeles y hay acta» o «ha denunciado a la red». Si
  es víctima de violencia de género o sexual, usa victimas-violencia-genero-sexual; si es trata,
  victimas-trata; si pide asilo o se le denegó, proteccion-internacional-apatridia; si solo hay arraigo,
  las skills de arraigo.
---

# Razones humanitarias y colaboración con autoridades

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Base legal y supuestos** → `buscar_articulo` (`ley="LOEX"`, artículos `"31"` y `"59"`) y `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"124"`, `"128"` y `"129"`).
- **Colaboración contra redes organizadas** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"142"` a `"147"`, uno por llamada).
- **Procedimiento, órgano, representación, trabajo, duración, prórroga y modificación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"130"`, `"131"`, `"132"`, `"191"`, `"193"` y `"197"`); si hay devolución o expulsión, también `"23"` y `"244"`.
- **Normas a las que remite el art. 128** → `buscar_articulo` (`ley="Ley 12/2009"`, artículos `"37"` y `"46"`) para el apartado 1; `buscar_articulo` (`ley="CP"`, el artículo del delito sufrido: `"311"` a `"318"`, `"510"`, `"511"`, `"512"` o `"22"`) para el apartado 2; cancelación de antecedentes → `buscar_articulo` (`ley="CP"`, `articulo="136"`).
- **Doctrina sobre cada supuesto y causas de denegación** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"` para el Supremo y `base="AN"` para TSJ y juzgados; fechas siempre en formato `dd/mm/aaaa`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Reformas y nulidades posteriores** → no las busques con `buscar_boe` (con el nombre del Real Decreto y una fecha no devuelve las reformas). Mira en cada respuesta de `buscar_articulo` la línea «redacción vigente dada por» (BOE-A-2026-8284 es el Real Decreto 316/2026; BOE-A-2026-19632 y 19633, las sentencias del Supremo de julio de 2026) y las notas «Téngase en cuenta…»; si necesitas el texto de la norma modificadora, `leer_boe` con ese identificador.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

## Cuándo usarla

Persona extranjera que está en España y pide una autorización de residencia temporal por circunstancias excepcionales, sin visado (art. 31.3 LOEX), por alguno de estos supuestos:

| Supuesto | Precepto | Qué lo caracteriza |
|---|---|---|
| Víctima de delitos contra los trabajadores, de odio o discriminación, o de conductas violentas en el entorno familiar | art. 128.2 | Exige resolución judicial **finalizadora y firme** que declare la condición de víctima |
| Enfermedad grave sobrevenida en España | art. 128.3 | Asistencia especializada no accesible en el país de origen; informe clínico de la autoridad sanitaria |
| Peligro al volver al país para pedir el visado | art. 128.4 | Además debe reunir **los demás requisitos** de otra autorización de residencia o de residencia y trabajo |
| Colaboración con autoridades ajena a redes, seguridad nacional o interés público | art. 129.1 | Puede instarla la propia autoridad; resuelve la Secretaría de Estado de Seguridad o la Dirección General de Gestión Migratoria (art. 130.4) |
| Colaboración con la administración laboral o judicial por trabajo irregular | art. 129.2 | Seis meses de trabajo irregular en los dos años anteriores a la colaboración, con resolución judicial o acta de la Inspección |
| Víctima, perjudicado o testigo que colabora contra redes (tráfico, inmigración ilegal, explotación laboral o en la prostitución) | LOEX art. 59; arts. 142 a 147 | Requiere **exención de responsabilidad** declarada antes de pedir la autorización |

Detector de otra figura (léela con `buscar_articulo` antes de decírselo al abogado y no redactes esta solicitud si encaja):

| Situación | Figura y skill |
|---|---|
| Mujer víctima de violencia de género, o víctima de violencia sexual | LOEX art. 31 bis; arts. 133 a 141 → `victimas-violencia-genero-sexual` |
| Indicios de trata de seres humanos | LOEX art. 59 bis; arts. 148 a 155 → `victimas-trata` |
| Solicitante de asilo, o asilo denegado con permanencia por razones humanitarias (art. 128.1: Ley 12/2009, arts. 37.b y 46.3) o protección temporal | → `proteccion-internacional-apatridia` (la permanencia la autoriza el Ministerio del Interior en ese procedimiento) |
| Reagrupada víctima del reagrupante | residencia independiente, art. 69.2.b → `reagrupacion-familiar` |
| Menor desplazado a España para tratamiento médico | art. 162.3 → `menores-extranjeros` |
| Dos años de permanencia y vínculos, contrato o formación | → skills de arraigo |
| Orden de expulsión vigente | la resolución de expulsión archiva todo procedimiento de residencia (art. 244.3) → `expulsion-procedimiento-sancionador` |
| Desplazamiento colectivo por conflicto grave («supuestos de especial relevancia») | disposición adicional segunda del Reglamento: ver «Huecos normativos» |

## Datos que hay que reunir antes de redactar

No redactes al primer disparo. Pregunta en este orden; si falta un dato imprescindible (★), pídelo y espera.

1. ★ Supuesto que se invoca y relato breve de los hechos que lo sostienen.
2. ★ Nacionalidad y documento: pasaporte en vigor, cédula de inscripción o título de viaje válido (art. 130.1.a). Si no tiene ninguno, pregunta si ha pedido cédula de inscripción (art. 210).
3. ★ Provincia de residencia efectiva (art. 193.2) o, en el art. 129.1 y en los arts. 143-144, autoridad con la que colabora.
4. ★ Situación administrativa: autorizaciones anteriores, procedimientos en trámite, solicitud de asilo, expediente sancionador, orden de expulsión o devolución (número, fecha y estado), prohibiciones de entrada.
5. ★ Antecedentes penales en España y en los países de residencia de los cinco años anteriores a la entrada (LOEX art. 31.5; art. 130.2), fecha de firmeza y de extinción de cada condena; antecedentes policiales.
6. ★ Datos del supuesto:
   - art. 128.2: delito, órgano, número de procedimiento, resolución que declara la condición de víctima y **fecha de firmeza**;
   - art. 128.3: fecha de entrada, fecha en que la enfermedad se manifestó o exigió asistencia especializada, diagnóstico y tratamiento, informe clínico (quién lo firma y de qué servicio público), prueba de que el tratamiento no es accesible en el país de origen, riesgo si se interrumpe; si es menor, qué progenitor o tutor está con él;
   - art. 128.4: en qué consiste el peligro y con qué se prueba; qué otra autorización se reuniría (medios, contrato, actividad) y con qué documentos;
   - art. 129.1: autoridad, objeto de la colaboración e informe que la acredita;
   - art. 129.2: prueba del trabajo irregular (periodos, empleador) y resolución judicial o acta de infracción de la Inspección;
   - arts. 142-144: expediente sancionador incoado, resolución de exención (fecha y órgano), autoridad con la que colabora (policial, fiscal o judicial, o administrativa no policial) y su informe.
7. Familiares: hijos fuera de España si hay colaboración contra redes (art. 147).
8. Representación: apoderamiento notarial, apud acta en el registro electrónico de apoderamientos o colaborador inscrito (art. 197.4).

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo. Si la respuesta trae una nota «Téngase en cuenta» sobre nulidad, aplícala: lo anulado no se cita como requisito.

**Comunes a todos los supuestos**

- Sin visado (LOEX art. 31.3; art. 130.1) y solicitud personal, que cumple el representante acreditado (art. 197.4).
- Carecer de antecedentes penales por delitos existentes en el ordenamiento español (LOEX art. 31.5). En los supuestos del art. 128.3 y del art. 129.2, si es mayor de edad penal, se aporta además certificado de los países de residencia de los cinco años anteriores a la entrada, salvo cinco años continuados en España o acreditación en otra solicitud de los últimos cinco años (art. 130.2). Los antecedentes policiales no deniegan por sí solos: exigen valoración casuística (art. 130.2).
- Subsanación en el plazo que fije la oficina, no superior a quince días, con apercibimiento de desistimiento (art. 130.3).
- Concedida: un año, prorrogable (art. 132.1); habilita a trabajar por cuenta ajena y propia sin límite geográfico ni de ocupación, salvo a quien no tenga la edad mínima (art. 131); tarjeta en el plazo de un mes desde la notificación (art. 130.6).
- Prórroga: en los dos meses anteriores al vencimiento, o en los tres posteriores con posible sanción (art. 132.3). En el art. 128.3, prórrogas anuales mientras sea necesario completar el tratamiento (art. 132.1); en las concedidas por la Secretaría de Estado de Seguridad, mientras persistan las razones (art. 132.2.c).
- Modificación a residencia y trabajo: posible desde los supuestos de esta skill salvo los excluidos en el art. 191.7 (léelo: la redacción vigente procede del Real Decreto 316/2026).
- Devolución no ejecutada: se revoca si procede la autorización (art. 23.8); pídelo en otrosí.
- Plazo máximo de resolución y sentido del silencio: están en disposiciones adicionales que el conector no devuelve. No los afirmes (ver «Huecos normativos»).
- Tasa: no des importe ni modelo; remite a la sede electrónica oficial.

**Art. 128.2 (víctimas de delitos).** Comprueba con `buscar_articulo` (`ley="CP"`) que el delito sufrido está en la lista del precepto o que se apreció la agravante del art. 22.4 CP, y que la resolución judicial que declara la condición de víctima es **firme** (una sentencia recurrida no lo es). Sin firmeza no hay supuesto: dilo al abogado. Si la víctima ha colaborado con la policía, la fiscalía o el juzgado (denuncia, identificación de los autores, declaración) y no puede esperar a la firmeza, ofrécele la vía del **art. 129.1** mientras tanto (colaboración ajena a redes, con informe de la jefatura policial y, en su caso, fiscal o judicial); si no, pospón la solicitud. La lista vigente añade los arts. 316 a 318 y 510 CP respecto del Reglamento anterior.

**Art. 128.3 (enfermedad sobrevenida).** Tres requisitos acumulativos: enfermedad grave que exige asistencia especializada y cuya falta supone grave riesgo; sobrevenida en España; asistencia no accesible en el país de origen. Informe clínico expedido por la autoridad sanitaria correspondiente: un informe de la sanidad privada no cumple la letra del precepto. Extensión al progenitor o tutor del menor enfermo que esté con él cuando surge la enfermedad y se responsabilice (art. 128.3, párrafo segundo). Si el diagnóstico y la necesidad de tratamiento eran anteriores a la entrada, el supuesto no encaja según la doctrina del Supremo (ver «Estrategia»).

**Art. 128.4 (peligro para pedir el visado).** Dos elementos: peligro real para la seguridad del solicitante o de su familia por el traslado al país de origen o procedencia, y cumplimiento de los demás requisitos de otra autorización (no lucrativa, cuenta ajena, cuenta propia…). Lee los artículos de esa otra autorización con `buscar_articulo` y acredítalos uno a uno: sin ellos, el Supremo confirma la denegación.

**Art. 129.1.** En la colaboración policial, fiscal o judicial y en la seguridad nacional, la solicitud se acompaña del informe de la jefatura de las Fuerzas y Cuerpos de Seguridad y, en su caso, de la autoridad fiscal o judicial (art. 130.4.a); resuelve la Secretaría de Estado de Seguridad (colaboración policial, fiscal o judicial y seguridad nacional) o la Dirección General de Gestión Migratoria (otras autoridades e interés público) (art. 130.4). El art. 130.4 solo fija quién resuelve: la solicitud del interesado se presenta, dirigida a ese órgano, en la oficina de extranjería de su provincia (arts. 130.1 y 197.1); la autoridad con la que colabora también puede instarla directamente (art. 129.1). La prórroga dura mientras las autoridades aprecien que persisten las razones (art. 132.2.c): avisa al abogado de que, al terminar la colaboración, habrá que pasar a otra autorización.

**Art. 129.2.** Seis meses de trabajo irregular en los dos años anteriores al inicio de la colaboración, acreditados por cualquier medio; requisitos del art. 126 salvo sus letras a) y b) (léelo); se incorpora la resolución judicial o la resolución administrativa relativa al acta de infracción de la Inspección. Resuelve el Delegado o Subdelegado del Gobierno.

**Arts. 142 a 147 (colaboración contra redes, LOEX art. 59).**

- Exención de responsabilidad: la propone el instructor del sancionador a partir del informe de la autoridad con la que colabora; la declara el Delegado o Subdelegado de la provincia donde se incoó el procedimiento, que decide también la suspensión del sancionador o de la ejecución de la expulsión o devolución (art. 142). Sin exención previa no hay autorización.
- Autorización: dirigida a la Secretaría de Estado de Migraciones si colabora con autoridades administrativas no policiales, presentada ante la Delegación o Subdelegación que declaró la exención (art. 143); o a la Secretaría de Estado de Seguridad si colabora con autoridades policiales, fiscales o judiciales, presentada ante la unidad policial de extranjería (art. 144). Pasaporte (en el art. 144, con vigencia mínima de cuatro meses) o cédula de inscripción, y representación si la hay.
- Autorización provisional de residencia y trabajo si el informe es favorable; definitiva de cinco años; tarjeta en un mes, sin mención de la condición de colaborador; la denegación extingue la provisional, que no computa para larga duración ni nacionalidad (arts. 143 y 144).
- Retorno asistido a elección del interesado (art. 145; LOEX art. 59.3); menores con prevalencia del interés superior (art. 146); reagrupación de hijos que estén fuera, sin exigir medios, residencia previa ni vivienda (art. 147).

**Causas típicas de denegación**

| Causa | Respuesta |
|---|---|
| Enfermedad previa a la entrada | Acreditar cuándo se manifestó o exigió asistencia especializada en España; doctrina del Supremo de 2026 |
| Informe clínico privado o genérico | Informe de la autoridad sanitaria pública con diagnóstico, tratamiento y riesgo de interrupción |
| No se prueba la inaccesibilidad en el país de origen | Informes médicos o de organismos sobre disponibilidad real del tratamiento |
| Resolución penal no firme (art. 128.2) | Esperar firmeza y aportar diligencia de firmeza |
| Peligro no acreditado o falta de requisitos de otra autorización (art. 128.4) | Prueba objetiva del peligro y de cada requisito de la autorización de referencia |
| Colaboración sin exención previa (arts. 142-144) | Pedir primero la exención al Delegado o Subdelegado |
| Antecedentes penales | Comprueba con el art. 136 CP si están cancelados o son cancelables y busca la doctrina (consulta de antecedentes) antes de afirmar que no pueden fundar la denegación; si no lo están, pide valoración individual |

## Huecos normativos

- `buscar_articulo` no devuelve las disposiciones adicionales del Reglamento (plazos de resolución, silencio, recursos) ni su disposición adicional segunda, a la que remite el art. 124.2 para otras circunstancias excepcionales. Del apartado 3 de esa disposición (supuestos de especial relevancia) solo hay texto dentro de `leer_boe` (`identificador="BOE-A-2026-8284"`, Real Decreto 316/2026). Si el caso depende de esa disposición o de un plazo o silencio que solo esté en una disposición adicional, detén la tarea y explica al abogado qué precepto falta.
- El apartado 1 del art. 128 remite a la normativa de desarrollo de la Ley 12/2009 y de protección temporal; si el caso depende de ella, localízala con `buscar_boe` y aplica la puerta si no aparece.

## Estrategia y jurisprudencia

1. Elige un solo supuesto principal y, si concurre otro, alégalo en un fundamento separado y subsidiario; no mezcles requisitos de supuestos distintos.
2. En el art. 128.3, construye la cronología médica (entrada, primer síntoma, diagnóstico, inicio del tratamiento especializado) con documentos y ponla en los hechos: es lo que decide el caso.
3. En el art. 128.4, trata el peligro como un hecho a probar (documentación del país, denuncias, informes) y no como una alegación genérica.
4. Consultas en Jurisprudenciator (reformula como máximo dos veces; usa dos a cuatro palabras clave, el buscador pierde precisión con frases largas y mezcla sentencias de asilo):
   - Enfermedad sobrevenida: `buscar_sentencias` (`consulta="razones humanitarias enfermedad sobrevenida"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde="01/01/2026"`) y la misma con `base="AN"`. El Supremo fijó en 2026 qué es enfermedad sobrevenida (STS 859/2026, de 24 de febrero, reiterada por la STS 1761/2026, de 22 de abril): léela con `leer_sentencias` (`terminos="enfermedad sobrevenida asistencia especializada"`) antes de redactar.
   - Peligro y demás requisitos: `consulta="razones humanitarias peligro visado"`, `base="TS"`.
   - Víctimas de delitos: `consulta="razones humanitarias víctima delito"`, `base="AN"`, `anios=10`.
   - Colaboración contra redes: `consulta="colaboración redes exención"`, `base="AN"`; colaboración del art. 129.2: `consulta="colaboración Inspección Trabajo residencia"`, `base="AN"`, `anios=10`; colaboración del art. 129.1: `consulta="colaboración autoridades policiales residencia"`, `base="AN"`.
   - Antecedentes: `consulta="circunstancias excepcionales antecedentes penales"`, `base="TS"`.
   La doctrina no es imprescindible para la solicitud administrativa: si tras dos reformulaciones no aparece nada aplicable, redacta sin el fundamento de doctrina y díselo al abogado en el resumen (en el art. 129.1 no suele haber doctrina reciente). En un recurso sí lo es: aplica la puerta.
5. Antes de citar una sentencia, comprueba en su texto qué reglamento aplicó: buena parte de la doctrina, también de 2026, se dictó con el Real Decreto 557/2011, cuyos supuestos equivalentes eran: art. 126.1 (hoy 128.2, con una lista de delitos más corta), 126.2 (hoy 128.3), 126.3 (hoy 128.4), 125 (hoy 128.1), 127 (hoy 129) y la colaboración contra redes, entre otros, en su art. 135. Cítala solo para requisitos que se mantienen y dilo en el escrito («doctrina dictada bajo el art. 126.2 del Reglamento anterior, de contenido equivalente al vigente art. 128.3»).
6. Lee con `leer_sentencias` (`parrafos=3`) solo lo que vayas a citar y transcribe el párrafo de fundamentos, nunca el relato de hechos ni datos de aquel pleito. Comprueba que el párrafo es razonamiento de la Sala y no la pretensión o alegación de una parte: los que empiezan «Razona que», «A su juicio», «solicita que se fije como doctrina…» o están en los antecedentes son de parte (así ocurre en la STS 859/2026 con el «Fijar como doctrina jurisprudencial…» y en la STS 1761/2026 con «Se tratan de requisitos cumulativos»). Si solo aparecen párrafos de parte, repite la lectura con otros `terminos`.
7. Datos de salud: en el escrito, describe la enfermedad con lo imprescindible para el requisito y remite al informe clínico adjunto; no reproduzcas historiales completos.

## Documento que se entrega

Un Word maquetado según `references/formato-y-organos.md`: **solicitud de autorización de residencia temporal por circunstancias excepcionales con memoria justificativa**. Acompaña al impreso oficial vigente, que no sustituye: indica al abogado que lo descargue de la sede oficial.

Nombre: `solicitud-razones-humanitarias-<apellido-cliente>-<AAAAMMDD>.docx` (arts. 128 y 129.2) o `solicitud-colaboracion-autoridades-<apellido-cliente>-<AAAAMMDD>.docx` (arts. 129.1, 143 y 144).

Estructura:

1. **Encabezamiento** según el supuesto, comprobado con los artículos leídos: Oficina de Extranjería de la Delegación o Subdelegación del Gobierno en `[PROVINCIA]` (arts. 128 y 129.2, art. 193.2); Secretaría de Estado de Seguridad o Dirección General de Gestión Migratoria, por conducto de la oficina de extranjería de la provincia de residencia (art. 129.1, arts. 130.4 y 197.1); Secretaría de Estado de Migraciones, a través de la Delegación o Subdelegación que declaró la exención (art. 143); Secretaría de Estado de Seguridad, a través de la unidad policial de extranjería (art. 144).
2. **Comparecencia**: `[NOMBRE Y APELLIDOS]`, nacionalidad, `[PASAPORTE]`, `[NIE]` si lo tiene, `[DOMICILIO]` o domicilio del despacho a efectos de notificaciones; representación y título (art. 197.4).
3. **EXPONE — HECHOS** (ordinales): identidad y entrada (`[FECHA DE ENTRADA EN ESPAÑA]`); situación administrativa; hechos del supuesto con su prueba (cronología médica, resolución firme, peligro, colaboración y exención); requisitos de la otra autorización en el art. 128.4; ausencia de antecedentes o su cancelación.
4. **FUNDAMENTOS DE DERECHO**: I. Marco legal (LOEX arts. 31.3 y 31.5, y art. 59 si hay colaboración contra redes; arts. 124 y 128 o 129 del Reglamento). II. Competencia y procedimiento (arts. 130, 193 y 197, o 142 a 144). III. Concurrencia de cada requisito del supuesto, con su documento. IV. Doctrina aplicable, con párrafo literal, órgano, fecha y ECLI, si la hay (ver «Estrategia», punto 4). V. Efectos: duración, trabajo y prórroga (arts. 131 y 132). Si el abogado pidió otro supuesto y lo has descartado (por ejemplo, art. 128.2 sin firmeza), explícalo en un fundamento breve. Cada fundamento con su propia secuencia argumental (formato, apartado 2).
5. **SOLICITA**: que se admita y conceda la autorización por el supuesto invocado, con habilitación para trabajar; en los arts. 143 y 144, también la autorización provisional.
6. **OTROSÍES** que procedan: extensión al progenitor o tutor del menor enfermo (art. 128.3); revocación de la devolución no ejecutada (art. 23.8); reagrupación de hijos con las exenciones del art. 147; que se recaben de oficio los informes del art. 130.2.
7. Lugar, fecha y firma.
8. **RELACIÓN DE DOCUMENTOS**, numerada: impreso oficial; justificante de tasa; pasaporte completo o cédula; prueba del supuesto (informe clínico de la autoridad sanitaria, resolución firme con diligencia de firmeza, informe de la autoridad y resolución de exención, acta o resolución del art. 129.2); certificados de antecedentes cuando proceda (con la legalización y traducción que pida la oficina); documentos de la otra autorización (art. 128.4); representación.

Cita el Reglamento siempre como «artículo N del Real Decreto 1155/2024» y la LOEX como «artículo N de la Ley Orgánica 4/2000» (formato, apartado 4); nunca «del Reglamento de Extranjería» ni «del Reglamento aprobado por el Real Decreto…», que `verificar_escrito` no identifica. Nombra la norma también en las remisiones breves («artículo 130.3 del Real Decreto 1155/2024», no «(artículo 130.3)» ni «del mismo Real Decreto»): `verificar_escrito` atribuye el artículo suelto a la última norma mencionada, y en el art. 128.2 esa suele ser el Código Penal. Lo mismo hace con los artículos que llevan letra o «bis» con apartado: escribe «letra a) del artículo 130.4 del Real Decreto 1155/2024», no «artículo 130.4.a) del Real Decreto 1155/2024».

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación: LOEX 31 (y 59 si hay colaboración contra redes) y Reglamento 124, 128 o 129 (o 142 a 147), 130, 131, 132, 191, 193 y 197; y los de la norma de remisión (CP, Ley 12/2009, autorización de referencia del art. 128.4). Revisadas las notas de nulidad o reforma.
- [ ] Detector pasado; si encaja otra figura, se ha dicho al abogado.
- [ ] Ningún plazo de resolución ni sentido del silencio tomado de una disposición adicional no devuelta.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` (párrafo de fundamentos) o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el texto completo. Si marca un artículo del Reglamento como no localizado o lo atribuye a la LOEX, compruébalo con `buscar_articulo` (`ley="BOE-A-2024-24099"`) y reescribe la cita como «artículo N del Real Decreto 1155/2024».
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[DOMICILIO]`, `[FECHA DE ENTRADA EN ESPAÑA]`, `[NÚMERO DE EXPEDIENTE]`) en lugar de datos inventados; datos de salud reducidos a lo imprescindible.
- [ ] Sin importes de tasa ni códigos de modelo.
- [ ] Resumen para el abogado según el apartado 7 del formato: órgano; fechas clave con su precepto (subsanación, art. 130.3; tarjeta, art. 130.6; prórroga, art. 132.3); documentos que faltan y riesgos (firmeza pendiente, informe clínico, exención previa); tabla de jurisprudencia; próximo paso.
