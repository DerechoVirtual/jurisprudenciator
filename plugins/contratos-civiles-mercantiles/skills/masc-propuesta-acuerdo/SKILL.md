---
name: masc-propuesta-acuerdo
description: >-
  Prepara el intento de negociación previo a la demanda civil que exige la LO 1/2025 en conflictos
  contractuales: elige el medio (negociación directa, oferta vinculante confidencial, mediación, conciliación,
  opinión de experto), redacta en Word la solicitud o propuesta de acuerdo, la oferta vinculante o el documento
  que acredita el intento, y una nota con plazos, efectos sobre la prescripción y la caducidad y costas. Úsala
  cuando el abogado diga «MASC», «requisito de procedibilidad», «oferta vinculante confidencial», «negociar
  antes de demandar», «me inadmitieron la demanda por no negociar» o «me han hecho una oferta vinculante».
  Si solo hay que exigir el pago o constituir en mora, usa requerimiento-cumplimiento; para liquidar la deuda
  y pedir el monitorio, reclamacion-deuda-monitorio; para resolver el contrato, resolucion-por-incumplimiento.
---

# Intento de negociación previo a la demanda (MASC)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Concepto, ámbito, materias y requisito de procedibilidad** → `buscar_articulo` (`ley="LO 1/2025"`, artículos `"2"`, `"3"`, `"4"` y `"5"`).
- **Medios y su régimen** → `buscar_articulo` (`ley="LO 1/2025"`, artículos `"6"`, `"8"`, `"11"`, `"14"`, `"15"`, `"16"`, `"17"`, `"18"` y `"19"`); mediación, (`ley="BOE-A-2012-9112"`, artículos `"4"`, `"23"` y `"25"`).
- **Plazos, confidencialidad, acreditación y acuerdo** → `buscar_articulo` (`ley="LO 1/2025"`, artículos `"7"`, `"9"`, `"10"`, `"12"` y `"13"`) y (`ley="LEC"`, `articulo="517"`).
- **Demanda y costas** → `buscar_articulo` (`ley="LEC"`, artículos `"264"`, `"399"`, `"403"`, `"394"`, `"395"`, `"245"` y `"245 bis"`).
- **Plazo de la acción que se va a ejercitar** → `buscar_articulo` (`ley="CC"`, artículos `"1964"`, `"1969"` y `"1973"`, y el especial que corresponda, p. ej. `"1490"`).
- **Doctrina de las Audiencias** (medio válido, oferta vinculante, identidad de objeto, plazos, inadmisión y subsanación, acuerdos de unificación de criterios de la plaza) → `buscar_sentencias` (`base="AN"`, `jurisdiccion="CIVIL"`, `tipo_organo="AP"`, `fecha_desde="03/04/2025"` y `provincia` de la plaza) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Contraparte que es sociedad** → `buscar_empresa_mercantil` (domicilio social vigente y administradores: a quién se dirige la solicitud y quién puede aceptar).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo de cada documento, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal, dato registral...). El conector devuelve los artículos 2 a 19 de la LO 1/2025 (título de los medios adecuados), pero no sus disposiciones adicionales, transitorias ni finales, y `leer_boe` (`identificador="BOE-A-2025-76"`) se corta en el preámbulo: cuando las necesites (régimen de los consumidores, entrada en vigor), aplica el punto 3 de la puerta.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que aplicar, la jurisprudencia que exige el apartado 8 de `references/formato-y-entrega-contratos.md`, el dato registral o catastral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-contratos.md` (cómo pedir cada norma) y `references/formato-y-entrega-contratos.md` (entregables, maquetación, nota, citas, datos y resumen). Léelas antes de redactar.

## Cuándo usarla

- Antes de presentar una demanda civil o mercantil por un conflicto contractual (cumplimiento, resolución, reclamación de cantidad, monitorio, saneamiento, daños), para que la demanda sea admisible.
- Para formular una propuesta que, si se rechaza, pese en las costas del pleito posterior.
- Cuando el cliente **recibe** una solicitud de negociación o una oferta vinculante confidencial y hay que responder.
- Cuando la demanda se inadmitió por falta del requisito y hay que rehacer el intento o recurrir.

| Situación | Skill |
|---|---|
| Solo hace falta el requerimiento de pago o de cumplimiento (puede servir también de solicitud de negociación) | `requerimiento-cumplimiento` |
| Liquidar la deuda y pedir el monitorio | `reclamacion-deuda-monitorio` |
| Decidir si se resuelve el contrato y con qué efectos | `resolucion-por-incumplimiento` |
| Defectos de la cosa con plazo de caducidad corriendo | `vicios-ocultos-saneamiento` (y esta skill para suspender la caducidad) |
| El acuerdo alcanzado modifica o extingue el contrato | `modificacion-novacion-cesion` |

## Datos que hay que reunir antes de redactar

Pregunta en este orden. No redactes al primer disparo: si falta un dato imprescindible (★), pídelo.

1. ★ A quién defiende el abogado: a quien propone o a quien recibe la solicitud u oferta.
2. ★ **Objeto de la futura demanda**: pretensiones, contrato, hechos y cuantía. La negociación debe versar sobre ese mismo objeto.
3. ★ Plazos que corren: prescripción o caducidad de la acción, con su fecha inicial; urgencia de medidas cautelares.
4. ★ Contraparte: identidad, domicilio personal o lugar de trabajo, y el medio electrónico usado en las relaciones previas; si es consumidor, empresa o entidad del sector público.
5. ★ Comunicaciones anteriores y si ya hubo algún intento de negociación (fecha, medio, prueba de recepción, respuesta).
6. ★ Margen real del cliente: qué aceptaría y qué ofrece (dato confidencial, solo para la nota y la propuesta).
7. Cláusulas del contrato sobre mediación, arbitraje, negociación previa o notificaciones.
8. Si el cliente quiere un tercero neutral (mediador, conciliador, experto) y quién paga sus honorarios.
9. Cuantía: si no supera 2.000 euros (asistencia letrada en la oferta vinculante) o 600 euros (negociación telemática preferente).

## Régimen jurídico y comprobaciones

Lee cada artículo con `buscar_articulo` en esta conversación antes de afirmarlo.

### 1. ¿Es exigible?

- Se exige en el orden civil para todos los procesos declarativos del libro II y los especiales del libro IV de la LEC (art. 5.2 LO 1/2025), salvo las materias de sus letras a) a h) (entre ellas, la tutela sumaria de la posesión y el juicio cambiario). No hace falta para la demanda ejecutiva, las medidas cautelares previas, las diligencias preliminares, la mayoría de expedientes de jurisdicción voluntaria, el monitorio europeo y el proceso europeo de escasa cuantía (art. 5.3). El monitorio no figura entre las excepciones: varias Audiencias lo exigen.
- Excluidos del título: materias laboral, penal y concursal, y asuntos en que una parte sea entidad del sector público (art. 3.2); materias no disponibles (art. 4).
- **Entrada en vigor**: las Audiencias no lo exigen a las demandas presentadas antes del 3 de abril de 2025 (hay acuerdos de unificación de criterios que lo recogen). Si el caso depende de ello, lee la disposición final de la LO 1/2025 en internet (BOE) y cítala con enlace.
- **Consumidor demandante**: las Audiencias aplican una disposición adicional de la LO 1/2025 según la cual basta la reclamación extrajudicial previa al empresario sin respuesta en plazo o con respuesta no satisfactoria. El conector no la devuelve: léela en internet en el BOE, cítala con enlace y fecha de consulta y apóyala con el auto de Audiencia que la aplique, leído con `leer_sentencias`.

### 2. Qué medio elegir

| Medio | Base | Cómo se acredita | Cuándo se entiende terminado sin acuerdo | Conviene si… |
|---|---|---|---|---|
| Negociación directa o entre abogados | arts. 5.1 y 14.1 | Documento firmado por ambas partes con el contenido del art. 10.2; en su defecto, prueba de que la otra parte recibió la solicitud o la propuesta, la fecha y que pudo acceder a su contenido íntegro (art. 10.2) | Treinta días naturales desde la recepción de la solicitud sin reunión ni respuesta escrita; treinta días desde una propuesta concreta sin acuerdo ni respuesta; tres meses desde la primera reunión; o escrito que da por terminadas las negociaciones (art. 10.4) | Es el más rápido y barato; sirve el requerimiento que invite a negociar |
| Oferta vinculante confidencial | art. 17 | Manifestación expresa en la demanda y justificantes de envío y recepción, sin mencionar el contenido (art. 17.4) | Rechazo, o falta de aceptación expresa en un mes o en el plazo mayor fijado (art. 17.4) | El cliente tiene una propuesta cerrada y quiere presión en costas; exige abogado salvo cuantía no superior a 2.000 euros (art. 6.2) |
| Mediación | Ley 5/2012; art. 14.2 | Documento del mediador (art. 10.3) | Según la Ley 5/2012 y el art. 10 | Relación que se quiere conservar o conflicto complejo |
| Conciliación privada | arts. 15 y 16 | Certificación del conciliador de que se intentó sin efecto o de que la otra parte rehusó (art. 16, letras j y k) | Plazos del art. 7.2.b y del art. 10 | Se quiere un tercero colegiado que proponga soluciones |
| Conciliación ante notario, registrador, letrado de la Administración de Justicia o juez de paz | art. 14.3 a 14.6 | Documento del órgano que interviene | Según su norma | Se busca un título con fe pública |
| Opinión de experto independiente | art. 18 | Certificación del experto (art. 18.5) | Tras el dictamen no aceptado | Discusión técnica (defectos, mediciones, valoración); exige designación de mutuo acuerdo |
| Derecho colaborativo | art. 19 | Acta final de los abogados (art. 19.3) | Acta final | Ambas partes con abogados acreditados en Derecho colaborativo, que renuncian a llevar el pleito si fracasa |

### 3. Requisitos de la solicitud o propuesta

- **Identidad de objeto** entre la negociación y el litigio, aunque las pretensiones puedan variar (art. 5.1): describe el contrato, los hechos, lo que se reclama y su cuantía con la misma extensión que tendrá la demanda. Un objeto genérico abre la puerta a la inadmisión.
- **Buena fe** y finalidad de solución extrajudicial (art. 2): propón un cauce concreto (reunión presencial o por videoconferencia, intercambio de propuestas) con fechas.
- **Destino y medio**: domicilio personal o lugar de trabajo del destinatario, o el medio electrónico usado en sus relaciones previas (art. 7.1), con prueba de recepción, fecha y contenido (arts. 10.2 y 17.2). Las Audiencias aceptan el medio electrónico si el destinatario acusa recibo o si era el canal habitual: busca el criterio de la plaza. Si no se conoce ningún domicilio ni medio, la demanda llevará la declaración responsable del art. 264.4 LEC.
- **Asistencia letrada**: voluntaria salvo en la oferta vinculante (art. 6.2); si una parte quiere valerse de abogado cuando no es preceptivo, lo dice en el requerimiento o en los tres días siguientes a recibirlo (art. 6.3).
- **Reclamaciones hasta 600 euros**: preferentemente por medios telemáticos (art. 8.2).
- **Tercero neutral propuesto por una sola parte**: si la otra no lo acepta, paga íntegramente sus honorarios devengados quien lo propuso (art. 11.2).

### 4. Oferta vinculante confidencial (art. 17)

- Quien la formula queda obligado en cuanto el destinatario la acepta expresamente; la aceptación es irrevocable (art. 17.1). Redáctala como una oferta completa y ejecutable: obligación concreta, importe, plazos y forma de pago o de cumplimiento, qué se renuncia a reclamar, gastos, plazo de aceptación (un mes como mínimo) y forma de la aceptación.
- La remisión de la oferta y de la aceptación debe dejar constancia de la identidad del oferente, de la recepción efectiva, de su fecha y del contenido (art. 17.2).
- Es confidencial en todo caso (arts. 17.3 y 9): en la demanda solo se manifiesta que se envió y se acompañan los justificantes, sin mencionar su contenido (art. 17.4).
- **No presentes la demanda antes de que venza el mes** (o el plazo mayor fijado) desde la recepción: hay Audiencias que inadmiten la demanda prematura.

### 5. Plazos y efectos sobre la prescripción y la caducidad

Calcula y entrega una tabla con: fecha de envío e intento de comunicación, fecha de recepción, fecha de terminación sin acuerdo (arts. 10.4 o 17.4), fecha límite para demandar (un año desde la recepción de la solicitud o desde la terminación, art. 7.3) y fecha de prescripción o caducidad de la acción recalculada.

- La solicitud que defina adecuadamente el objeto interrumpe la prescripción o suspende la caducidad desde que consta el intento de comunicación en el domicilio o por el medio electrónico habitual (art. 7.1). El cómputo se reinicia o se reanuda si no hay primera reunión ni respuesta escrita en treinta días naturales, o si una propuesta concreta queda sin respuesta treinta días (art. 7.1).
- Con tercero neutral rigen reglas propias: mediador, art. 4 de la Ley 5/2012 (quince días); conciliador, art. 7.2.b; experto, art. 7.2.c; letrado de la Administración de Justicia, notario o registrador, art. 7.2.d.
- Si se acordaron medidas cautelares durante la negociación, la demanda va ante el mismo tribunal en veinte días desde la terminación sin acuerdo (art. 7.3).
- Con un plazo de caducidad corriendo, calcula la fecha final sin contar la suspensión (supuesto más desfavorable) y, aparte, con ella; si el margen es escaso, envía la solicitud cuanto antes, presenta la demanda en cuanto el requisito esté cumplido (treinta días o un mes, según el medio) y explica el riesgo al abogado.

### 6. Confidencialidad (art. 9)

El proceso y su documentación son confidenciales salvo si las partes acudieron o no y el objeto de la controversia. No pueden aportarse como prueba salvo dispensa escrita de todas las partes, impugnación de la tasación de costas y solicitud de exoneración o moderación del art. 245 LEC, requerimiento del juez penal o razones de orden público (art. 9.2); lo aportado indebidamente se inadmite (art. 9.3). Consecuencia práctica: separa el requerimiento o la solicitud (no confidencial en cuanto a su existencia y objeto) de las propuestas con cifras, y conserva íntegras y fechadas todas las propuestas para una eventual solicitud del art. 245.5 LEC.

### 7. Acreditación ante el juzgado

- Con la demanda: el documento que acredite el intento (art. 264.4 LEC y art. 10 LO 1/2025) o la declaración responsable de imposibilidad por desconocer el domicilio o el medio para requerir; en la demanda, la descripción del proceso negociador (art. 399.3 LEC). Sin ello, inadmisión (art. 403.2 LEC).
- Busca si la Audiencia de la plaza permite subsanar antes de inadmitir y qué intentos de contacto considera suficientes cuando la comunicación no llega.

### 8. Costas

- No hay condena en costas a favor de quien rehusó sin justa causa participar en un medio preceptivo al que fue efectivamente convocado (art. 394.1, párrafo tercero, LEC); quien no acudió sin causa puede ser condenado aunque la estimación sea parcial (art. 394.2); si la parte requerida rehusó intervenir, el requirente queda exento de costas salvo abuso del servicio público de Justicia (art. 394.4).
- Allanamiento: hay mala fe si el demandado rechazó el acuerdo ofrecido o el medio adecuado (art. 395.1), y costas si no acudió sin causa y luego se allana (art. 395.3).
- Exoneración o moderación: la parte condenada en costas que hizo una propuesta no aceptada puede pedirla si la resolución final es sustancialmente coincidente con su propuesta, aportando la documentación íntegra (arts. 245.5 y 245 bis LEC). Los tribunales valoran la colaboración y el abuso del servicio público de Justicia (art. 7.4 LO 1/2025).

### 9. Si hay acuerdo

- Puede ser total o parcial; si es parcial, se demanda solo lo no acordado (art. 4.1). Contenido y firma: art. 12. Es vinculante y solo impugnable por las causas de invalidez de los contratos (art. 13.1).
- Para que sea título ejecutivo, debe elevarse a escritura pública u homologarse cuando proceda (art. 13.2 y art. 517.2.2.º LEC); cualquiera de las partes puede compeler a la otra a elevarlo a escritura (art. 12.3). Si el acuerdo cambia el contrato, redacta la adenda con `modificacion-novacion-cesion`.

### 10. Si defiendes a quien recibe la solicitud u oferta

- Responde por escrito dentro de los treinta días y participa de buena fe: rehusar sin causa pesa en costas (arts. 394 y 395 LEC).
- Una aceptación de la oferta vinculante es irrevocable: no la aceptes con condiciones (sería una contraoferta) y contrasta antes su contenido con la posición del cliente en un eventual juicio.
- Si la rechazas, deja constancia razonada y calcula el riesgo del art. 245.5 LEC si la sentencia acaba coincidiendo con la oferta.
- Comprueba si la solicitud recibida define el objeto con la precisión del art. 7.1: de ello depende que haya interrumpido la prescripción de la acción de la otra parte.

## Jurisprudencia: qué buscar

Imprescindible para la nota (apartado 8 del formato). Todas con `base="AN"`, `jurisdiccion="CIVIL"`, `tipo_organo="AP"`, `fecha_desde="03/04/2025"` y, si se sabe, `provincia` de la plaza; reformula como máximo dos veces:

- Oferta vinculante: `consulta="oferta vinculante confidencial requisito de procedibilidad"`.
- Inadmisión y subsanación: `consulta="requisito de procedibilidad medios adecuados de solución de controversias inadmisión demanda subsanación"`.
- Identidad de objeto: `consulta="identidad entre el objeto de la negociación y el objeto del litigio requisito de procedibilidad"`.
- Requerimiento como intento suficiente: `consulta="requerimiento de pago solicitud de negociación intento suficiente requisito de procedibilidad"`.
- Criterios de la plaza: `consulta="acuerdos de unificación de criterios medios adecuados de solución de controversias"`.
- Domicilio desconocido: `consulta="declaración responsable imposibilidad actividad negociadora domicilio desconocido"`.
- Prescripción y caducidad: `consulta="medio adecuado de solución de controversias suspensión de la caducidad solicitud de negociación"`.
- Consumidores: `consulta="disposición adicional séptima consumidores reclamación extrajudicial requisito de procedibilidad"`.
- Costas: `consulta="exoneración moderación costas propuesta sustancialmente coincidente"`. La doctrina sobre estas reglas aún es escasa: si no hay resolución aplicable, la nota se apoya en el texto de los arts. 394, 395 y 245 LEC y lo dice.

Lee con `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión) solo lo que vayas a citar en la nota; comprueba que el párrafo es razonamiento de la Sala (en estos autos abundan las transcripciones de la ley y de las alegaciones del apelante). Di que es doctrina de Audiencia y de qué plaza.

## Documentos que se entregan

En todos los documentos, nombra las normas como pide el apartado 6 del formato («artículo 17 de la Ley Orgánica 1/2025, de 2 de enero», «artículo 4 de la Ley 5/2012, de 6 de julio, de mediación en asuntos civiles y mercantiles», «artículo 394 de la Ley de Enjuiciamiento Civil»); para un apartado, «apartado 4 del artículo 17 de la Ley Orgánica 1/2025, de 2 de enero»: así los reconoce `verificar_escrito`.

1. **Solicitud de negociación o propuesta de acuerdo** (`propuesta-masc-<destinatario>-<AAAAMMDD>.docx`): partes y domicilios; objeto de la controversia con la misma extensión que la futura demanda; invitación a negociar de buena fe con cauce, fechas y plazo de respuesta; indicación de si el remitente actúa asistido de abogado (art. 6.3); advertencia de confidencialidad (art. 9); y, en documento separado o anexo confidencial, la propuesta concreta.
2. **Oferta vinculante confidencial** (`oferta-vinculante-<destinatario>-<AAAAMMDD>.docx`): encabezado «OFERTA VINCULANTE CONFIDENCIAL (artículo 17 de la Ley Orgánica 1/2025, de 2 de enero)»; oferente y destinatario; objeto; obligación que se asume con importe, plazos y forma; renuncias y gastos; plazo y forma de aceptación expresa; confidencialidad; firma del oferente y del abogado (salvo cuantía no superior a 2.000 euros).
3. **Documento de acreditación** (`acta-negociacion-<partes>-<AAAAMMDD>.docx`), para firmar ambas partes al terminar: identidad de las partes y de sus asesores, fecha, objeto, reuniones mantenidas y declaración responsable de haber intervenido de buena fe (art. 10.2). Si hay acuerdo, **acuerdo** (`acuerdo-masc-<partes>-<AAAAMMDD>.docx`) con el contenido del art. 12.
4. **Nota para el abogado** (`nota-masc-<parte-principal>-<AAAAMMDD>.docx`, 2-4 páginas): por qué se elige ese medio; tabla de fechas (apartado 5); qué se aporta con la demanda y cómo se describe (arts. 264.4 y 399.3 LEC); riesgos de costas en ambos sentidos; criterio de la Audiencia de la plaza con párrafo literal, órgano, fecha y ECLI; datos de internet con enlace; próximo paso.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió; lo que el conector no devuelve (disposiciones de la LO 1/2025) se leyó en el BOE en internet con enlace y fecha, y se señala en el resumen.
- [ ] Leídos con `buscar_articulo` en esta conversación los arts. 2, 3, 5, 6, 7, 9, 10 y 17 de la LO 1/2025 (y 12, 13, 14-19 o el art. 4 de la Ley 5/2012 según el medio); LEC 264, 394, 395, 399, 403 y 245; plazo de la acción.
- [ ] Exigibilidad comprobada (materia, proceso, excepciones, consumidor, sector público).
- [ ] Objeto de la negociación idéntico al de la futura demanda y definido con precisión.
- [ ] Medio de envío con prueba de identidad, recepción, fecha y contenido; destino conforme al art. 7.1.
- [ ] Tabla de fechas completa: terminación sin acuerdo, un año para demandar, prescripción o caducidad recalculada en el supuesto más desfavorable; en oferta vinculante, fecha antes de la cual no se puede demandar.
- [ ] Propuestas con cifras separadas de lo que se aportará con la demanda; nada confidencial en la demanda.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre cada documento; avisos de «posible disonancia» contrastados con el texto leído.
- [ ] Marcadores (`[NOMBRE Y APELLIDOS]`, `[DENOMINACIÓN SOCIAL]`, `[CIF]`, `[DOMICILIO]`, `[IMPORTE]`) en lugar de datos inventados; importes y fechas coherentes.
- [ ] Resumen para el abogado según el apartado 10 del formato: medio elegido y por qué, fechas clave con su precepto, qué aportar con la demanda, riesgos de costas, tabla de jurisprudencia, datos obtenidos de internet y próximo paso.
