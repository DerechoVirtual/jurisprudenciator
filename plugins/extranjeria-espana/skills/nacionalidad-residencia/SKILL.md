---
name: nacionalidad-residencia
description: >-
  Prepara la solicitud de nacionalidad española por residencia y los recursos contra su denegación
  (reposición y recurso contencioso-administrativo) en Word. Úsala cuando el abogado diga
  «nacionalidad por residencia», «le han denegado la nacionalidad», «buena conducta cívica»,
  «antecedentes policiales y nacionalidad», «DELE y CCSE», «examen de nacionalidad», «diez años de
  residencia», «dos años iberoamericanos», «un año casado con español», «silencio en la nacionalidad»,
  «recurso de reposición nacionalidad» o «jura de nacionalidad». Comprueba el plazo de residencia, la
  buena conducta cívica, la integración, el plazo para resolver y el órgano judicial competente. Para
  nacionalidad de origen, opción, carta de naturaleza, recuperación o Ley de Memoria Democrática usa
  nacionalidad-otras-vias.
---

# Nacionalidad española por residencia: solicitud y recursos

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Plazo de residencia, requisitos sustantivos, caducidad de la concesión y requisitos comunes (jura, renuncia, inscripción)** → `buscar_articulo` (`ley="CC"`, `articulo="22"`; también `"21"`, `"23"` y `"24"`).
- **Procedimiento: solicitud, documentos, DELE y CCSE, exenciones y dispensas, informes, subsanación, plazo para resolver, silencio, eficacia y recursos** → `buscar_articulo` (`ley="Real Decreto 1004/2015"`, artículos `"4"`, `"5"`, `"6"`, `"8"`, `"10"`, `"11"`, `"12"` y `"13"`; `ley="Orden JUS/1625/2016"`, artículos `"2"`, `"7"`, `"10"`, `"11"`, `"12"` y `"13"`).
- **Inscripción constitutiva y ante quién se hacen las declaraciones** → `buscar_articulo` (`ley="Ley 20/2011"`, `articulo="68"`).
- **Recurso de reposición, plazos y documentos nuevos** → `buscar_articulo` (`ley="LPAC"`, artículos `"24"`, `"30"`, `"118"`, `"123"` y `"124"`; si la resolución se firma «por delegación», `ley="Ley 40/2015"`, `articulo="9"`); **recurso contencioso, órgano y plazo** → `buscar_articulo` (`ley="LJCA"`, artículos `"11"`, `"23"`, `"25"`, `"36"`, `"45"`, `"46"`, `"52"` y `"139"`; `ley="LOPJ"`, `articulo="66"`).
- **Doctrina sobre buena conducta cívica e integración** → `buscar_sentencias` (`consulta="nacionalidad por residencia buena conducta cívica antecedentes policiales"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde` de los dos últimos años) y la misma materia con `base="TS"` sin filtro de fecha; después `leer_sentencias` (`parrafos=3`, `terminos` del motivo de denegación).
- **Órgano judicial que resuelve hoy las denegaciones** → `buscar_sentencias` (`consulta="denegación nacionalidad española por residencia"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde` de los últimos seis meses) y lectura de una resolución para ver la Sala y el procedimiento.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar o el requisito que hay que comprobar), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- Preparar el escrito que acompaña a la solicitud de nacionalidad por residencia (memoria justificativa del plazo, de la residencia, de la buena conducta y de la integración) y la lista de documentos.
- Contestar un requerimiento de subsanación dentro del expediente.
- Recurrir en reposición una denegación expresa o presunta, un desistimiento o una declaración de ineficacia de la concesión.
- Preparar el escrito de interposición del recurso contencioso-administrativo contra la denegación, y el esquema de la demanda cuando llegue el expediente.
- Valorar si conviene recurrir o presentar una nueva solicitud cuando el defecto ya está subsanado.

Usa otra skill del plugin cuando el asunto sea:

- nacionalidad de origen, opción, carta de naturaleza, consolidación, conservación, pérdida, recuperación o Ley 20/2022 → `nacionalidad-otras-vias`;
- la autorización de residencia que sirve de base al cómputo (arraigos, `reagrupacion-familiar`, `familiares-de-espanoles`, `trabajo-cuenta-ajena`...) o su renovación;
- asilo o apatridia → `proteccion-internacional-apatridia`;
- primera consulta sin saber aún qué vía conviene → `extranjeria-intake`.

La casación ante el Supremo queda fuera: si el abogado la pide, dilo y limita la ayuda a identificar la cuestión de interés casacional con jurisprudencia.

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible, pregúntalo y espera.

1. **Qué se prepara** (imprescindible): solicitud, subsanación, reposición o recurso contencioso.
2. **Fechas** (imprescindible para recursos): fecha de notificación de la resolución o, si no hay resolución, fecha de entrada de la solicitud en el órgano instructor (de ella depende el silencio). Pregunta también si hubo **requerimientos de subsanación o de documentos** (fecha de notificación y fecha en que se atendieron) y si se abrió **trámite de audiencia o de alegaciones**: los requerimientos suspenden el plazo para resolver y, en reposición, de ello depende que se admitan documentos nuevos. Sin la fecha no calcules ningún plazo.
3. **Supuesto de plazo** (imprescindible): nacionalidad de origen del interesado y hechos del supuesto que se invoca (refugiado, nacional de país del art. 22.1, nacido en España, matrimonio con español y su fecha, viudedad, descendiente de español de origen, tutela o acogimiento, no ejercicio de la opción).
4. **Historial de residencia** (imprescindible): cada autorización con tipo y fechas de inicio y fin, renovaciones solicitadas en plazo o fuera de plazo, periodos de estancia por estudios, de solicitante de protección internacional o de irregularidad, y ausencias de España.
5. **Conducta** (imprescindible): antecedentes penales en España y en el país de origen, antecedentes policiales, diligencias abiertas, sanciones administrativas (tráfico, extranjería, tributarias) y expulsiones o prohibiciones de entrada.
6. **Integración** (imprescindible): diplomas DELE y CCSE con fechas, o la causa de dispensa (edad, discapacidad, analfabetismo, escolarización en España) y si se pidió la dispensa y cuándo.
7. **Edad y capacidad**: si el interesado es menor o precisa apoyos, quién lo representa y si hay autorización del Encargado.
8. **Resolución impugnada** (imprescindible para recursos): texto íntegro, motivo de denegación, órgano que la firma («por delegación» o no) y pie de recursos.
9. Opcionales: arraigo laboral, familiar y social, estudios, voluntariado, empadronamiento, cumplimiento tributario.

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` en el momento y cita su texto vigente. Lo que sigue es el mapa verificado; confírmalo en cada asunto.

**Plazo de residencia (`CC`, art. 22).**
- Regla general, refugiados y nacionales de origen de los países que enumera el art. 22.1, y sefardíes: lee el apartado 1 y aplica el plazo exacto que devuelva.
- Plazo de un año: supuestos del art. 22.2, letras a) a f). En el matrimonio, comprueba que el año de casados exista «al tiempo de la solicitud» y que no haya separación legal o de hecho.
- En todos los casos la residencia ha de ser «legal, continuada e inmediatamente anterior a la petición» (art. 22.3). Calcula el cómputo con las fechas de las autorizaciones y señala cada interrupción.
- Cuestiones de cómputo que se deciden con jurisprudencia, nunca de memoria: periodos como estudiante, como solicitante de protección internacional, renovaciones presentadas fuera de plazo, ausencias prolongadas. Consulta `buscar_sentencias` (`consulta="residencia legal continuada inmediatamente anterior nacionalidad"` más el supuesto concreto, `base="AN"`, `jurisdiccion="CONTENCIOSO"`) y lee los fundamentos.
- Causa típica de denegación: se invoca el plazo de un año pero el supuesto de hecho no encaja (por ejemplo, descendiente frente a no ejercicio de la opción) y se exige entonces el plazo general. Identifica el supuesto correcto en la solicitud.

**Buena conducta cívica (`CC`, art. 22.4).**
- La justifica el interesado (`Orden JUS/1625/2016`, art. 7.2, pone en él la prueba de la residencia, la conducta y la integración); la jurisprudencia reciente de la Audiencia Nacional sitúa en él la carga de la prueba y admite valorar antecedentes policiales aunque el proceso penal terminara sin condena. Compruébalo con `leer_sentencias` antes de fijar la estrategia.
- El Supremo exige que consten en el expediente el certificado de antecedentes penales en España y el informe preceptivo del Ministerio del Interior (RD 1004/2015, art. 8.2) antes de valorar la conducta. Búscalo con `consulta="buena conducta cívica certificado de antecedentes penales informe del Ministerio del Interior nacionalidad"`, `base="TS"`, y úsalo cuando falten en el expediente.
- El Ministro puede denegar «por motivos razonados de orden público o interés nacional» (`CC`, art. 21.2) y la resolución basada en informe del Centro Nacional de Inteligencia se entiende motivada (RD 1004/2015, art. 11.2). Si la denegación se apoya en ello, dilo al abogado y valora con él el margen real de éxito.
- Motivos típicos: antecedentes policiales, condenas (canceladas o no), diligencias abiertas, infracciones graves de tráfico, sanciones de extranjería, incumplimientos tributarios, ocultación de datos en la solicitud.

**Integración (`CC`, art. 22.4; RD 1004/2015, art. 6).**
- DELE de nivel A2 como mínimo y prueba CCSE, administrados por el Instituto Cervantes (RD 1004/2015, art. 6.1 y 6.2; `Orden JUS/1625/2016`, art. 10.1).
- Exención del DELE para los nacionales de los países que enumeran el art. 6.5 del RD y el art. 10.2 de la Orden: copia la lista del texto vigente, no de memoria. Si esa nacionalidad no es la principal, la Orden exige pasaporte o certificado consular (art. 10.2).
- El dominio del español puede acreditarse también con los certificados oficiales de idiomas que enumera el art. 10.3 de la Orden. El certificado CCSE tiene la vigencia que fija el art. 10.4: compruébala con la fecha de la solicitud.
- Menores de dieciocho años y personas con la capacidad modificada judicialmente: exentos de las pruebas, con certificados de centros (RD, arts. 5.2 y 6.6; Orden, art. 10.6).
- Dispensa por no saber leer ni escribir o por dificultades de aprendizaje: se pide al Ministerio **antes** de la solicitud de nacionalidad y en modelo normalizado; si se presentan a la vez, la solicitud de nacionalidad se archiva; la dispensa se resuelve en seis meses con silencio desestimatorio y su resolución pone fin a la vía administrativa (Orden, art. 10.5). Quien estuvo escolarizado en España y superó la educación secundaria obligatoria puede solicitar la nacionalidad directamente con esa documentación (art. 10.5).
- Valoración conjunta con los informes del art. 8 del RD (art. 6.8).
- La disposición final séptima de la Ley 19/2015, en la que se apoyan estas reglas, no la devuelve Jurisprudenciator: cita el RD 1004/2015 y la Orden. Si una cuestión solo se resuelve con esa disposición, aplica la puerta en ese punto.
- Criterio reciente que debes comprobar: la Audiencia Nacional ha exigido que las pruebas o la dispensa consten al tiempo de la solicitud. Busca `consulta="nacionalidad residencia integración CCSE DELE dispensa"`, `base="AN"`, y para atemperar la exigencia en mujeres migrantes `consulta="grado de integración mujer migrante nacionalidad"`, `base="TS"`. Contra la denegación de la dispensa, determina el órgano judicial con la LJCA y jurisprudencia (`consulta="dispensa pruebas DELE CCSE nacionalidad"`, `base="AN"`): no es la resolución del Ministro sobre la nacionalidad.

**Procedimiento (RD 1004/2015).**
- Solicitud en modelo normalizado por la aplicación electrónica (art. 4); los profesionales colegiados se relacionan electrónicamente (art. 3). El modelo, la tasa y la sede se comprueban en la sede oficial del Ministerio: no des importes ni códigos.
- Documentos: art. 5 (certificado de nacimiento, pasaporte, integración, tasa, documentos del supuesto, antecedentes penales del país de origen para mayores de edad) y anexo de la `Orden JUS/1625/2016` (art. 2.1). Si el conector no devuelve el anexo, pide al abogado la lista vigente de la sede oficial. Las consultas de oficio que el interesado puede autorizar en lugar de aportar certificados están en el art. 7.2 de la Orden.
- Subsanación: plazo de tres meses desde el requerimiento; si no se atiende, desistimiento (art. 10.2).
- Plazo para resolver: un año desde la entrada en el órgano instructor; transcurrido sin resolución, la solicitud se entiende desestimada (art. 11.3; `Orden JUS/1625/2016`, art. 11.3). Cita también `LPAC`, art. 24, si lo necesitas. El requerimiento de subsanación **suspende** ese plazo desde su notificación hasta su cumplimiento o hasta que pasen los tres meses concedidos (`Orden JUS/1625/2016`, art. 7.3): suma los días de suspensión antes de fijar la fecha del silencio y cuenta de fecha a fecha (`LPAC`, art. 30.4).
- Instrucción: el reglamento atribuye la instrucción a la «Dirección General de los Registros y del Notariado» (art. 1.2); hoy la resolución identifica al órgano con su denominación vigente: encabeza con la que figure en la resolución o en la sede oficial.

**Eficacia, jura e inscripción.**
- La concesión caduca a los ciento ochenta días de su notificación si no se comparece para cumplir el art. 23 (`CC`, art. 21.4; RD 1004/2015, art. 12.1).
- Requisitos comunes: jura o promesa, renuncia a la nacionalidad anterior salvo los naturales de los países del art. 24.1 y los sefardíes, e inscripción (`CC`, art. 23). La inscripción es constitutiva y la declaración puede hacerse ante el Encargado, notario o funcionario consular (`Ley 20/2011`, art. 68).
- El art. 12.1 del RD 1004/2015 tiene un inciso anulado por el Tribunal Supremo. La nota que devuelve `buscar_articulo` habla del «inciso destacado», pero el texto llega sin el destacado: identifica el inciso con `leer_boe` (`identificador="BOE-A-2024-18114"`), que transcribe el fallo, y no lo cites como requisito.

**Recursos y plazos.**
- Reposición potestativa ante el mismo órgano o recurso contencioso directo (`Orden JUS/1625/2016`, art. 13.1). Reposición: un mes si el acto es expreso; si es presunto, en cualquier momento desde que se produce el silencio (`LPAC`, art. 124). La Orden entiende desestimada la reposición no resuelta en un mes (art. 13.1).
- La resolución firmada por la Dirección General «por delegación» se considera dictada por el Ministro (`Ley 40/2015`, art. 9.4): la reposición va al Ministro, y el recurso contencioso se dirige contra un acto del Ministro.
- Documentos nuevos en reposición (auto de archivo, certificados): el art. 118.1 de la `LPAC` no los tiene en cuenta si el recurrente pudo aportarlos en el trámite de alegaciones y no lo hizo. Con la respuesta del dato 2, explica en el recurso por qué no pudieron aportarse antes (no hubo requerimiento ni audiencia sobre ese extremo) o, si se requirieron y no se atendieron, advierte al abogado de que la reposición no los salvará y valora el recurso contencioso o una nueva solicitud.
- Recurso contencioso: la resolución es del Ministro (normalmente firmada por delegación) y la Orden lo dirige a la Audiencia Nacional (art. 13.1). Cita además `LJCA`, art. 11.1.a) y `LOPJ`, art. 66.a), y confírmalo con la búsqueda de jurisprudencia reciente de la lista antes de encabezar a la Sala de lo Contencioso-Administrativo de la Audiencia Nacional. Ante órgano colegiado actúan procurador y abogado (`LJCA`, art. 23.2).
- Plazo: dos meses desde la notificación del acto expreso o de la resolución de la reposición (`LJCA`, art. 46.1 y 46.4). Contra la desestimación presunta, `LJCA`, art. 46.1 y `Orden JUS/1625/2016`, art. 13.2 mencionan seis meses: antes de decir al abogado que hay o no hay plazo, busca la doctrina constitucional (`consulta="silencio administrativo negativo plazo recurso contencioso-administrativo articulo 46.1 tutela judicial efectiva"`, `base="TC"`; la consulta equivalente con `base="TS"` devuelve asuntos ajenos), lee el fundamento de la mayoría (la lectura puede devolver párrafos del voto particular: no los cites como doctrina del Tribunal) y compara la regla que interpretó con la actual (`LPAC`, art. 24.2 y 24.3.b). Da siempre, además, la fecha final en la lectura más estricta (seis meses) y recomienda interponer sin esperar.
- Fuera de plazo, el recurso se inadmite (`LJCA`, art. 69.e). Calcula siempre la fecha final.

## Estrategia y jurisprudencia

1. **Diagnostica antes de escribir.** Clasifica el motivo de denegación: plazo o residencia; conducta; integración; orden público o interés nacional; desistimiento o caducidad. Cada uno tiene su línea de defensa y su consulta.
2. **Conducta.** Busca con el motivo exacto (`"antecedentes policiales archivo nacionalidad buena conducta"`, `"antecedentes penales cancelados nacionalidad"`, `"infracciones de tráfico buena conducta cívica"`), `base="AN"`, `jurisdiccion="CONTENCIOSO"`, `fecha_desde` de los dos últimos años; y `base="TS"` sin filtro de fecha para la doctrina general. Lee con `parrafos=3` y `terminos` del motivo. Los tribunales ponderan la proximidad o lejanía temporal de la conducta, su gravedad y los factores positivos del periodo de residencia: construye el fundamento con esos tres elementos y con prueba documental (certificados, sentencias absolutorias, autos de archivo, informes de empleo y arraigo).
3. **Integración.** Si faltaban los diplomas al solicitar, comprueba con la búsqueda si la jurisprudencia reciente confirma esas denegaciones y, si es así, díselo al abogado y valora presentar una nueva solicitud con los diplomas (o tras obtener la dispensa previa del art. 10.5 de la Orden) en lugar de litigar. Si hubo dispensa pedida y no resuelta, o pruebas adaptadas, busca esos supuestos concretos.
4. **Residencia.** Reconstruye la línea temporal de autorizaciones en una tabla; si hay un hueco, busca jurisprudencia del supuesto concreto antes de sostener que no interrumpe.
5. **Expediente incompleto.** Si falta el informe del Ministerio del Interior o el certificado de antecedentes, alega la doctrina del Supremo sobre su carácter imprescindible.
6. **Silencio.** Ante la desestimación presunta, calcula la fecha del silencio (un año más los días de suspensión por requerimientos) y elige entre reposición y recurso contencioso directo explicando al abogado ventajas (tiempo, coste, posibilidad de que la Administración resuelva) y riesgos (costas, necesidad de ampliar el recurso si llega una resolución expresa).
7. **Cuadro de trabajo por motivo de denegación** (las consultas van con `jurisdiccion="CONTENCIOSO"`; ajusta los términos al caso):

| Motivo de la resolución | Consulta en `buscar_sentencias` | Prueba que conviene aportar |
|---|---|---|
| Antecedentes policiales sin condena | `"antecedentes policiales archivo nacionalidad buena conducta cívica"`, `base="AN"`; para la doctrina del Supremo sobre el valor de los informes policiales y la ponderación temporal, `"antecedentes policiales fuerza probatoria coherencia precision corroboracion nacionalidad"` y `"proximidad o lejania temporal buena conducta civica factores positivos"`, `base="TS"` | Testimonio del auto de archivo o sobreseimiento con su firmeza (y de las diligencias relevantes: tipo de delito y calificación) o sentencia absolutoria, certificado de antecedentes penales, informes de trabajo y arraigo |
| Condena penal cancelada | `"antecedentes penales cancelados nacionalidad buena conducta"`, `base="AN"` y `base="TS"` | Resolución de cancelación, fecha de los hechos, conducta posterior |
| Falta el informe de Interior o el certificado de penales | `"buena conducta cívica certificado de antecedentes penales informe del Ministerio del Interior"`, `base="TS"` | Petición de que se complete el expediente |
| DELE o CCSE ausentes | `"nacionalidad residencia integración CCSE DELE dispensa"`, `base="AN"` | Diplomas, solicitud de dispensa y su fecha, escolarización |
| Residencia no legal o interrumpida | `"residencia legal continuada inmediatamente anterior nacionalidad"` más el supuesto, `base="AN"` | Resoluciones de concesión y renovación con fechas, justificantes de presentación en plazo |
| Plazo abreviado mal invocado | `"nacionalidad residencia plazo de un año"` más la letra del art. 22.2, `base="AN"` | Certificados que acreditan el supuesto correcto |
| Orden público o interés nacional | `"denegación nacionalidad orden público interés nacional informe reservado"`, `base="TS"` | Petición de acceso al expediente en lo no reservado |

8. **Cómo usar la doctrina en el escrito:** premisa normativa con el texto vigente, párrafo literal del fundamento jurídico con órgano, fecha y ECLI tal como los devolvió `leer_sentencias`, aplicación a los hechos del cliente y conclusión. Cita doctrina, nunca el relato de hechos ni datos de las partes de aquel pleito. Prioriza la jurisprudencia reciente de la Audiencia Nacional y la del Supremo (la doctrina del Supremo sobre buena conducta es, en su mayoría, anterior a 2012: con `base="TS"` el filtro de fecha deja fuera los hitos). Antes de citar un párrafo, comprueba que es razonamiento de la Sala y no la postura de una parte que la sentencia resume («alega», «sostiene», «suplica de la Sala»): `leer_sentencias` devuelve a menudo esos resúmenes. Si citas una sentencia desfavorable para distinguirla, dilo y explica en qué se diferencia el caso.

## Documento que se entrega

Formato, destinatarios, citas y datos: `references/formato-y-organos.md`. Todo en Word.

**A. Escrito de solicitud y memoria justificativa** (`solicitud-nacionalidad-residencia-<apellido>-<AAAAMMDD>.docx`). Acompaña al modelo normalizado; no lo sustituye.
1. Encabezamiento: órgano instructor con la denominación de la sede oficial.
2. Comparecencia: `[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[DOMICILIO]`, y representación del abogado.
3. Supuesto de plazo invocado, con el texto del art. 22 aplicable.
4. Residencia legal, continuada e inmediatamente anterior: tabla de autorizaciones (tipo, número, desde, hasta) y cómputo.
5. Buena conducta cívica: declaración de antecedentes y explicación documentada de cualquier incidencia.
6. Integración: diplomas o causa de exención con su precepto.
7. SOLICITA y relación numerada de documentos (art. 5 RD 1004/2015).

**B. Recurso de reposición** (`recurso-reposicion-nacionalidad-<apellido>-<AAAAMMDD>.docx`).
1. Encabezamiento al órgano que firmó la resolución, tal como figura en ella.
2. Comparecencia e identificación de la resolución (`[NÚMERO DE EXPEDIENTE]`, fecha de notificación).
3. Hechos numerados: solicitud, tramitación, resolución y motivo.
4. Fundamentos: procedencia, órgano y plazo del recurso con su fecha final (`LPAC`, arts. 30.4, 123 y 124; `Ley 40/2015`, art. 9.4 si se firmó por delegación); admisibilidad de los documentos nuevos (`LPAC`, art. 118.1), si se aportan; fondo por cada motivo de denegación, con doctrina.
5. SOLICITA: estimación del recurso y concesión; subsidiariamente, retroacción para completar el expediente o valorar la prueba aportada.
6. Documentos nuevos numerados.

**C. Escrito de interposición del recurso contencioso-administrativo** (`recurso-contencioso-nacionalidad-<apellido>-<AAAAMMDD>.docx`).
1. Encabezamiento a la Sala competente comprobada.
2. Comparecencia del procurador `[PROCURADOR]` en nombre del interesado, con abogado.
3. Acto impugnado y fecha de notificación; petición de que se tenga por interpuesto el recurso y se reclame el expediente (`LJCA`, art. 45).
4. Documentos: representación, resolución impugnada y, si procede, la reposición y su resolución.
5. Contra una desestimación presunta, identifica el acto por el expediente (`LJCA`, art. 45.2.c), explica por qué se recurre en plazo y anuncia en otrosí que, si la Administración resuelve durante el proceso, se pedirá la ampliación a la resolución expresa o se desistirá (`LJCA`, art. 36.4).
6. Si el abogado lo pide, añade el esquema de la demanda en un documento aparte, de uso interno (`esquema-demanda-nacionalidad-<apellido>-<AAAAMMDD>.docx`), para cuando se entregue el expediente (plazo de veinte días y caducidad, `LJCA`, art. 52): hechos, fundamentos por motivo, pretensión de anulación y reconocimiento del derecho (`LJCA`, arts. 31.2 y 71.1.b), prueba y riesgo de costas (`LJCA`, art. 139.1).

## Comprobación final

- [ ] `estado` respondió y la puerta se cumplió en todo el trabajo.
- [ ] Cada artículo citado se leyó en esta conversación con `buscar_articulo` y se cita con su texto vigente (incluida la nota del art. 12 del RD 1004/2015 si se usa).
- [ ] Si el caso dependía de una disposición final o adicional que el conector no devuelve, la tarea se detuvo en ese punto y se explicó al abogado.
- [ ] El órgano judicial se comprobó con la LJCA, la LOPJ y una resolución reciente leída.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`; solo se citan fundamentos jurídicos.
- [ ] `verificar_escrito` pasado sobre el texto completo y corregidos los avisos. No identifica las citas con letra («artículo 20.1.b)», «artículo 11.1.a)») y las marca como no localizadas: compruébalas con `buscar_articulo` y no las cambies por ese aviso.
- [ ] Marcadores entre corchetes para todo dato no facilitado; ningún dato inventado.
- [ ] Plazo con fecha inicial, precepto y fecha final; si falta la fecha de notificación, no se da plazo. En el silencio, fecha de entrada más un año y más los días de suspensión por requerimientos (`Orden JUS/1625/2016`, art. 7.3).
- [ ] Resumen para el abogado según el apartado 7 del formato: documento y órgano, plazo, documentos que faltan y riesgos (en especial si la denegación se funda en orden público o informe reservado), tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene) y próximo paso.
