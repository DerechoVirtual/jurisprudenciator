---
name: ciudadanos-ue-y-familiares
description: >-
  Prepara en Word las solicitudes del régimen de libre circulación (Real Decreto 240/2007 y Directiva 2004/38/CE): certificado de registro del ciudadano de la UE, del EEE o de Suiza, tarjeta de residencia de familiar de ciudadano de la Unión, tarjeta de residencia permanente, familiares extensos y pareja estable (art. 2 bis) y conservación del derecho tras fallecimiento, divorcio o salida. Úsala cuando el abogado diga «certificado de registro», «NIE verde», «tarjeta comunitaria», «casado con una italiana», «me la denegaron por falta de medios» o «por el seguro médico», «residencia permanente comunitaria». Si el familiar lo es de un español que nunca ha residido con él en otro Estado miembro y la solicitud es posterior al 20/05/2025, usa familiares-de-espanoles.
---

# Ciudadanos de la Unión y sus familiares

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Beneficiarios y derechos** → `buscar_articulo` (`ley="Real Decreto 240/2007"`, artículos `"1"`, `"2"`, `"2 bis"` y `"3"`) y `buscar_articulo` (`ley="Directiva 2004/38/CE"`, artículos `"2"` y `"3"`).
- **Expresiones anuladas del Real Decreto 240/2007 que el texto devuelto todavía muestra** → `leer_boe` (`identificador="BOE-A-2010-16822"`).
- **Residencia de más de tres meses, medios y seguro** → `buscar_articulo` (`ley="Real Decreto 240/2007"`, `articulo="7"`), `buscar_articulo` (`ley="BOE-A-2012-9218"`, artículos `"3"` y `"4"`: Orden PRE/1490/2012) y `buscar_articulo` (`ley="Directiva 2004/38/CE"`, `articulo="7"`).
- **Tarjeta de familiar, conservación, permanente, renovación y vigencia** → `buscar_articulo` (`ley="Real Decreto 240/2007"`, artículos `"8"`, `"9"`, `"9 bis"`, `"10"`, `"11"`, `"12"`, `"13"` y `"14"`) y `buscar_articulo` (`ley="Directiva 2004/38/CE"`, artículos `"12"`, `"13"`, `"16"` y `"17"`).
- **Orden público, seguridad y salud pública** → `buscar_articulo` (`ley="Real Decreto 240/2007"`, `articulo="15"`) y `buscar_articulo` (`ley="Directiva 2004/38/CE"`, artículos `"27"`, `"28"`, `"30"` y `"31"`).
- **Frontera con el régimen de familiares de españoles** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"93"` y `"94"`) y `leer_boe` (`identificador="BOE-A-2024-24099"`, disposición transitoria segunda).
- **Doctrina sobre medios, seguro, «a cargo», residencia permanente, silencio y orden público** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"` o `base="AN"`; `base="TJUE"` para el Tribunal de Justicia) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar.

## Cuándo usarla

- Ciudadano de otro Estado de la UE, del EEE o de Suiza que va a residir más de tres meses en España: **certificado de registro** (art. 7).
- Familiar no comunitario que acompaña o se reúne con ese ciudadano: **tarjeta de residencia de familiar de ciudadano de la Unión** (art. 8), también para familiares extensos y pareja estable (art. 2 bis).
- **Residencia permanente** tras cinco años o por los supuestos anticipados (arts. 10 y 11); **renovación** (art. 13).
- **Conservación a título personal** del derecho tras fallecimiento, salida, nulidad, divorcio o cancelación de la pareja (art. 9).
- Español que regresa tras residir de forma efectiva con su familiar en otro Estado miembro, y solicitudes de familiares de españoles presentadas antes del 20/05/2025.
- Nueva solicitud tras una denegación por medios, seguro o vínculo, o revisión de una preparada.

**Detector previo.** Si encaja otra figura, dilo al abogado con el precepto leído y no sigas con esta:

| Situación | Skill |
|---|---|
| Familiar de español que nunca ha residido con él en otro Estado miembro, solicitud desde el 20/05/2025 | familiares-de-espanoles (arts. 93-99 del Reglamento) |
| Progenitor de un menor de otro Estado de la Unión cuando el ciudadano no cumple el art. 7 | arraigo-familiar (art. 127.e del Reglamento) |
| Expulsión o prohibición de entrada de un ciudadano de la Unión o su familiar | expulsion-procedimiento-sancionador (art. 15 del Real Decreto 240/2007) |
| Recurso contra una denegación ya notificada | recurso-administrativo-extranjeria o recurso-contencioso-extranjeria; visado denegado, visados-denegacion |
| Nacionalidad española por residencia | nacionalidad-residencia |

## Datos que hay que reunir antes de redactar

Los marcados con ★ son imprescindibles: si faltan, pregúntalos y no redactes.

1. ★ Ciudadano de la Unión: nacionalidad, documento, fecha de entrada, certificado de registro (fecha) y situación que funda su derecho: trabajo por cuenta ajena o propia, medios y seguro, estudios, o conservación de la condición de trabajador (art. 7.3).
2. ★ Si es español: si residió de forma efectiva con el familiar en otro Estado miembro (dónde, cuánto tiempo, con qué título) y la fecha de la solicitud.
3. ★ Familiar: nacionalidad, pasaporte, fecha y forma de entrada (visado o tarjeta de otro Estado miembro), parentesco y documento que lo prueba, traducido y legalizado o apostillado.
4. ★ Para descendientes de 21 años o más, ascendientes y familiares extensos: prueba de estar a cargo o de convivencia en el país de procedencia; para la pareja estable, tiempo de convivencia o hijos comunes.
5. ★ Medios y seguro de la unidad familiar: ingresos o patrimonio de **cualquiera** de sus miembros, cuantía, estabilidad; tipo de cobertura sanitaria (Sistema Nacional de Salud, pública autonómica, privada con o sin copagos).
6. ★ Historial: tarjetas anteriores, ausencias de España (duración y motivo), antecedentes penales, expulsiones.
7. Residencia permanente: cinco años de residencia legal continuada con el ciudadano o supuesto anticipado (jubilación, incapacidad, trabajo transfronterizo, fallecimiento).
8. Conservación: hecho causante y fecha, duración del matrimonio o pareja y años en España, custodia, régimen de visitas, violencia de género o trata.
9. Representación del solicitante.

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` antes de afirmarlo. Si la respuesta trae una nota «Téngase en cuenta…» (nulidad declarada por el Tribunal Supremo o reforma), léela y aplícala: lo anulado no se aplica ni se cita como vigente. **Aviso crítico**: el texto del Real Decreto 240/2007 que devuelve el conector conserva expresiones que el Tribunal Supremo anuló y que en el BOE solo aparecen destacadas. Lee el fallo con `leer_boe` (`identificador="BOE-A-2010-16822"`) y no las cites: entre ellas, «otro Estado miembro» del art. 2, «separación legal» de los arts. 2 y 9, la exigencia de que el registro de pareja impida dos registros simultáneos y las excepciones al derecho a trabajar del art. 3.2.

**Beneficiarios (arts. 2 y 2 bis).**

- Familiares del art. 2: cónyuge; pareja inscrita en un registro público de un Estado de la UE o del EEE; descendientes directos y del cónyuge o pareja menores de veintiún años, mayores a cargo o incapaces; ascendientes a cargo. Matrimonio y pareja registrada son incompatibles.
- Otros familiares (art. 2 bis): los que en el país de procedencia estén a cargo o vivan con el ciudadano, o cuyo cuidado personal sea estrictamente necesario por salud o discapacidad, y la pareja con relación estable debidamente probada. No es un derecho automático: la Administración valora individualmente y motiva (art. 2 bis.4). Comprueba en el texto leído el criterio de convivencia continuada en el país de procedencia y el de la pareja estable.

**Derecho de residencia de más de tres meses (art. 7).**

- El ciudadano: trabajador por cuenta ajena o propia; o recursos suficientes y seguro de enfermedad que cubra todos los riesgos; o estudiante matriculado con seguro y declaración de recursos; o familiar de quien cumpla alguno de esos supuestos.
- El familiar no comunitario tiene derecho si el ciudadano cumple una de las letras a), b) o c) (art. 7.2); del estudiante solo cónyuge, pareja e hijos a cargo (art. 7.4).
- Medios: sin importe fijo, valorando la situación personal (art. 7.7). La Orden PRE/1490/2012 (art. 3.2.c) considera suficientes los que superen el importe fijado cada año para la prestación no contributiva y exige valoración individualizada; seguro público o privado con cobertura equivalente a la del Sistema Nacional de Salud. Jurisprudenciator no devuelve la cuantía anual: pídesela al abogado de la fuente oficial.
- Inscripción del ciudadano en el Registro Central de Extranjeros en tres meses desde la entrada; el certificado se expide de inmediato (art. 7.5). Si la solicitud es incompleta, requerimiento de diez días y, si no se subsana, desistimiento recurrible en alzada (Orden, art. 2.3).

**Tarjeta de familiar (art. 8).** Solicitud en tres meses desde la entrada, ante la oficina de extranjería de la provincia o la comisaría; resguardo inmediato que acredita la estancia legal; documentación del art. 8.3; expedición en tres meses con efectos retroactivos a la entrada; validez de cinco años o del periodo previsto de residencia del ciudadano. La tramitación no impide la permanencia provisional (art. 12.2). Los ascendientes y descendientes no vuelven a acreditar el vínculo al renovar (art. 13).

**Conservación a título personal (art. 9).** Fallecimiento (familiar que residía en España antes), salida o fallecimiento con hijos escolarizados en España y progenitor custodio, y nulidad, divorcio o cancelación de la pareja: tres años de vínculo hasta el inicio del proceso judicial con uno en España, custodia, violencia de género o trata, o régimen de visitas vigente de un menor que reside en España. Obligación de comunicar el cambio.

**Residencia permanente (arts. 10, 11 y 14).** Cinco años de residencia legal continuada; supuestos anticipados del art. 10.2 y familiares del art. 10.3 y 10.5. La tarjeta permanente del familiar se pide en el mes anterior a la caducidad de la temporal o en los tres meses posteriores, con posible sanción; se renueva cada diez años (art. 11). Se pierde por ausencia de más de dos años consecutivos (art. 10.7). La tarjeta temporal caduca por ausencias superiores a seis meses al año, salvo las excepciones del art. 14.3.

**Orden público (art. 15).** Solo por conducta personal que constituya una amenaza real, actual y suficientemente grave; las condenas previas no bastan por sí solas; ni fines económicos ni caducidad de documentos. Las enfermedades que lo justifican son las del art. 15.9.

**Silencio.** El Real Decreto 240/2007 no dice qué ocurre si no se resuelve en tres meses, y `buscar_articulo` no devuelve la disposición adicional primera de la LOEX, a la que remite la doctrina. Obtén el criterio del Supremo con `buscar_sentencias` (`consulta="silencio administrativo tarjeta de residencia de familiar de ciudadano de la Unión"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`) y cítalo con su párrafo literal; distingue tarjeta temporal y permanente. Si no lo obtienes, no afirmes el sentido del silencio.

**Documentos por trámite (compruébalos en el artículo leído).**

- Certificado de registro: pasaporte o documento de identidad y la prueba de la situación del art. 7 que corresponda según el art. 3.2 de la Orden PRE/1490/2012 (contrato o alta, actividad por cuenta propia, seguro y recursos, o matrícula, seguro y declaración responsable).
- Tarjeta de familiar: la lista del art. 8.3 y, para los del art. 2 bis, la de su apartado 3.
- Tarjeta permanente: pasaporte, prueba del supuesto que da derecho y fotografías (art. 11.2).
- Conservación: prueba del hecho causante y del supuesto del art. 9 alegado.

**Plazos que debes calcular y escribir con su fecha.** Inscripción del ciudadano y solicitud de tarjeta del familiar: tres meses desde la entrada (arts. 7.5 y 8.2). Tarjeta permanente: mes anterior a la caducidad de la temporal o tres meses posteriores (art. 11.1). Comunicación de cambios de nacionalidad, estado civil o domicilio (art. 14.2, que no fija plazo: no inventes uno). Expedición de la tarjeta de familiar en los tres meses siguientes a la presentación (art. 8.4). Si no consta la fecha de entrada o de caducidad, pídela; sin ella no des un plazo.

**Causas típicas de denegación y respuesta.**

| Causa | Respuesta |
|---|---|
| Medios insuficientes del ciudadano | Sumar los del familiar no comunitario y de la unidad; valoración individual (art. 7.7 y Orden, art. 3.2.c); doctrina del Supremo y del TJUE sobre la procedencia de los recursos |
| Seguro no válido | Cobertura del Sistema Nacional de Salud o privada equivalente; doctrina del Supremo sobre la cobertura pública autonómica |
| No acredita estar a cargo | Situación de hecho de dependencia en el país de procedencia; envíos y gastos acreditados |
| Pareja estable no probada | Vínculo duradero y tiempo de convivencia (art. 2 bis.4.b) |
| Ausencias largas | Excepciones del art. 14.3 y del art. 16.3 de la Directiva |
| Antecedentes penales | Art. 15.5.d: condena no basta; exigir motivación sobre la amenaza actual |

## Estrategia y jurisprudencia

1. Fija primero qué persona funda el derecho y en qué letra del art. 7 encaja; toda la solicitud del familiar depende de ello.
2. Si el ciudadano es español, justifica en el escrito por qué se aplica este régimen (regreso tras residencia efectiva en otro Estado miembro o solicitud anterior al 20/05/2025) con la doctrina leída.
3. Consultas (reformula como máximo dos veces):
   - Medios: `buscar_sentencias` (`consulta="artículo 7 Real Decreto 240/2007 recursos suficientes procedencia cónyuge nacional de tercer país"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`) y `consulta="recursos suficientes procedentes del miembro de la familia nacional de un tercer país"`, `base="TJUE"`.
   - Medios del propio ciudadano sin actividad económica (ahorros, patrimonio, sin ingresos periódicos): `consulta="recursos suficientes derecho de residencia ciudadano de la Unión que no ejerce actividad económica carga para la asistencia social"`, `base="TJUE"` (sale la doctrina sobre el importe de referencia y el examen individual del art. 8.4 de la Directiva, que incorpora el art. 7.7). La Administración puede objetar que se acredita solo un «saldo puntual»: prueba la estabilidad del patrimonio con extractos de varios meses.
   - Seguro: `consulta="seguro de enfermedad artículo 7 Real Decreto 240/2007 Sistema Nacional de Salud"`, `base="TS"`.
   - A cargo y familiares extensos: `consulta="artículo 2 bis Real Decreto 240/2007 a cargo país de procedencia"`, `base="AN"`, y `consulta="otros miembros de la familia facilitar entrada y residencia examen detenido de las circunstancias personales"`, `base="TJUE"`.
   - Pareja estable no registrada: `consulta="pareja de hecho no registrada relación estable debidamente probada artículo 2 bis Real Decreto 240/2007 convivencia tarjeta de familiar"`, `base="AN"`. Lo que devuelve la búsqueda en el TJUE con la consulta anterior trata sobre todo del ciudadano que regresa a su Estado (art. 21 TFUE): si el ciudadano reside en España desde otro Estado miembro, basta el art. 3.2 de la Directiva leído.
   - Regreso del ciudadano: `consulta="ciudadano de la Unión que regresa a su Estado miembro de origen familiar nacional de tercer país residencia efectiva"`, `base="TJUE"`.
   - Residencia permanente: `consulta="residencia permanente familiar ciudadano de la Unión residencia legal artículos 7 y 10 Real Decreto 240/2007"`, `base="TS"`.
   - Orden público: `consulta="familiar ciudadano de la Unión orden público amenaza real actual suficientemente grave"`, `base="TS"`.
4. Usa `fecha_desde` para priorizar lo reciente y amplía solo si no hay resultados; lee con `leer_sentencias` solo lo que vayas a citar y copia el párrafo de fundamentos, nunca hechos ni datos de las partes.

## Documento que se entrega

Word maquetado según `references/formato-y-organos.md`, que acompaña al impreso oficial vigente (no lo sustituye; el abogado lo descarga de la sede oficial). Sin importes de tasas ni códigos de modelos.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» y el resto de normas como indica el apartado 4 de `references/formato-y-organos.md`, para que `verificar_escrito` las reconozca. Cita la Orden como «artículo N de la Orden PRE/1490/2012, de 9 de julio»: `verificar_escrito` puede atribuir ese número al Real Decreto 240/2007 citado en el mismo párrafo; si lo hace, comprueba el artículo con `buscar_articulo` (`ley="BOE-A-2012-9218"`) y no cambies la cita. `verificar_escrito` tampoco reconoce la Directiva 2004/38/CE: atribuye sus artículos a la última norma nombrada (y los da por existentes); comprueba los de la Directiva con `buscar_articulo`.

Nombre según el trámite: `solicitud-certificado-registro-<apellido-cliente>-<AAAAMMDD>.docx`, `solicitud-tarjeta-familiar-ue-<apellido-cliente>-<AAAAMMDD>.docx`, `solicitud-tarjeta-permanente-ue-<apellido-cliente>-<AAAAMMDD>.docx` o `solicitud-conservacion-residencia-ue-<apellido-cliente>-<AAAAMMDD>.docx`.

1. Encabezamiento: «A LA OFICINA DE EXTRANJERÍA DE [PROVINCIA]» o, en su defecto, la comisaría correspondiente (arts. 7.5 y 8.2 leídos).
2. Comparecencia del solicitante (`[NOMBRE Y APELLIDOS]`, `[PASAPORTE]`, `[NIE]`, `[DOMICILIO]`). El certificado de registro y las tarjetas se solicitan **personalmente** (arts. 7.5 y 12.1 leídos; Orden PRE/1490/2012, art. 2.2): el solicitante comparece él mismo y el abogado le asiste; díselo al abogado para que el cliente acuda a la cita.
3. EXPONE — HECHOS: PRIMERO, ciudadano de la Unión y su situación del art. 7; SEGUNDO, familiar y vínculo; TERCERO, entrada y fecha; CUARTO, medios y seguro de la unidad; QUINTO, dependencia, convivencia o pareja estable, si procede; SEXTO, historial (ausencias, antecedentes, tarjetas previas). En el certificado de registro de un ciudadano que solicita solo, suprime los hechos del familiar y ordena los demás (identidad, entrada, situación del art. 7, medios, seguro, historial). En la tarjeta de un trabajador por cuenta ajena o propia, no hace falta acreditar medios ni seguro (art. 7.2 leído).
4. FUNDAMENTOS DE DERECHO: I, régimen aplicable y, si el ciudadano es español, por qué; II, beneficiario (art. 2 o 2 bis y Directiva, arts. 2 y 3); III, derecho de residencia (art. 7 y Orden PRE/1490/2012); IV, el trámite pedido (arts. 8, 9, 10-11 o 13); V, doctrina con párrafo literal y ECLI; VI, en su caso, art. 15 y garantías.
5. SOLICITA: la expedición del certificado o de la tarjeta, con efectos desde la entrada cuando proceda (art. 8.4).
6. OTROSÍ: en las tarjetas, que se tenga por acreditada la estancia legal con el resguardo (art. 8.2); en todo trámite, que si se detecta alguna carencia se requiera su subsanación antes de resolver (en el certificado de registro, plazo de diez días de la Orden PRE/1490/2012, art. 2.3).
7. Lugar, fecha, firma y RELACIÓN DE DOCUMENTOS numerada.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Detector resuelto; si el ciudadano es español, justificado por qué va por este régimen.
- [ ] Leídos con `buscar_articulo` en esta conversación los artículos del Real Decreto 240/2007, de la Orden PRE/1490/2012 y de la Directiva que se citan; leído el fallo anulatorio y ninguna expresión anulada citada como vigente.
- [ ] Plazos con fecha y precepto: registro y tarjeta en tres meses desde la entrada, tarjeta permanente en el mes anterior o los tres posteriores a la caducidad, expedición de la tarjeta (art. 8.4); para la conservación y la comunicación de cambios, di que el precepto no fija plazo si así es en el texto leído.
- [ ] Sentido del silencio afirmado solo si se obtuvo la doctrina con Jurisprudenciator.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado sobre el texto completo y corregido lo que señale.
- [ ] Marcadores para lo que falta; sin cuantías de medios ni importes no confirmados por el abogado.
- [ ] Resumen para el abogado según el apartado 7 del formato: trámite y oficina, plazos con su precepto, documentos que faltan y riesgos, tabla de jurisprudencia y próximo paso.
