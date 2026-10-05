---
name: larga-duracion
description: >-
  Prepara en Word la solicitud de autorización de residencia de larga duración nacional o de larga duración-UE (LOEX, art. 32; arts. 175-185 del Reglamento aprobado por el Real Decreto 1155/2024), con cuadro de cómputo de los cinco años y de las ausencias, la solicitud de recuperación de una larga duración extinguida (arts. 186-189), la de residencia en España del residente de larga duración-UE de otro Estado miembro y la renovación de la tarjeta. Úsala cuando el abogado diga «ya lleva cinco años», «permiso de larga duración», «residencia permanente» de un no comunitario, «larga duración-UE», «ha estado fuera más de un año y perdió la larga duración» o «renovar la tarjeta de larga duración». Si es familiar de un ciudadano de la Unión, usa ciudadanos-ue-y-familiares; si aún no cumple los cinco años, renovacion-modificacion-extincion.
---

# Residencia de larga duración

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Base legal** → `buscar_articulo` (`ley="LOEX"`, artículos `"30 bis"` y `"32"`) y `buscar_articulo` (`ley="Directiva 2003/109/CE"`, artículos `"4"`, `"5"` y `"9"`).
- **Larga duración-UE: requisitos, procedimiento y tarjeta** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"175"`, `"176"`, `"177"` y `"178"`); medios con los criterios de la reagrupación → `articulo="67"`.
- **Larga duración nacional** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"182"`, `"183"`, `"184"` y `"185"`).
- **Movilidad del residente de larga duración-UE de otro Estado miembro y su familia** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"179"`, `"180"` y `"181"`).
- **Extinción y recuperación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"201"`, `"186"`, `"187"`, `"188"` y `"189"`); requisitos del visado de regreso → `articulo="38"`.
- **Competencia, presentación y representación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"193"` y `"197"`).
- **Doctrina sobre cómputo, ausencias, antecedentes, medios y recuperación** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`, `base="TS"` o `base="AN"`) + `leer_sentencias` (`parrafos=3`, `terminos` con la cuestión).
- **Revisión del documento** → cada redactor del equipo pasa `verificar_escrito` solo sobre sus frases con normas, y el ensamblado rechaza cualquier ECLI o ROJ que ningún redactor leyera; `buscar_por_cita` se usa solo con un ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). La letra va detrás de la norma («artículo 176 del Real Decreto 1155/2024, letra a)» o «la letra a) del artículo 176 del Real Decreto 1155/2024»), nunca pegada al número («176.a)»), y cada mención de un artículo lleva su norma; en una cita literal que nombre un artículo sin norma, añádela entre corchetes. **`verificar_escrito` no identifica las directivas:** atribuye «artículo 4.1 de la Directiva 2003/109/CE» a la última ley española citada (por ejemplo, al art. 4.1 de la LOEX). Comprueba esas citas con `buscar_articulo` (`ley="Directiva 2003/109/CE"`) y explícalo en el resumen; no las cambies por otra norma.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

**Redacción rápida (por defecto).** Este documento se redacta con la skill `redaccion-rapida` de este plugin: un equipo de subagentes escribe las secciones a la vez y el Word sale en 2-3 minutos. Cárgala y sigue sus pasos; esta skill aporta el contenido jurídico (estructura, destinatario u órgano, reglas, jurisprudencia mínima y comprobaciones). Sus fases, baterías de preguntas y pasadas de pulido se cumplen dentro de ese método —las preguntas se responden con la documentación y solo se pregunta lo que bloquea, en una única ronda—, no una detrás de otra. Si el abogado pide expresamente ir paso a paso, sigue las fases en orden.

Referencias del plugin: `references/anclas-normativas-extranjeria.md` y `references/formato-y-organos.md`. Léelas antes de redactar. Aviso: la LOEX no tiene art. 32 bis (Jurisprudenciator no lo encuentra); la larga duración está entera en el art. 32, incluido su apartado 3 bis.

## Cuándo usarla

- Residente temporal que ha cumplido, o cumplirá antes de caducar su autorización, cinco años de residencia legal y continuada.
- Supuestos de larga duración nacional sin esperar cinco años (art. 183.3): pensionistas de jubilación o incapacidad, nacidos en España con tres años de residencia al llegar a la mayoría de edad, antiguos españoles de origen, tutelados por entidad pública, apátridas y beneficiarios de protección internacional.
- Residente de larga duración-UE en otro Estado miembro que quiere residir en España, y su familia (arts. 179-181).
- Recuperación tras extinción por ausencia o por haber adquirido la larga duración-UE en otro Estado, tras seis años fuera o tras un retorno voluntario (arts. 186-189).
- Renovación de la tarjeta (arts. 178 y 185).

**Detector previo:**

| Situación | Skill |
|---|---|
| No alcanza los cinco años ni un supuesto del art. 183.3 | renovacion-modificacion-extincion (renovación de la temporal) |
| Familiar de ciudadano de la Unión que pide la residencia permanente | ciudadanos-ue-y-familiares (arts. 10 y 11 del Real Decreto 240/2007) |
| Procedimiento de extinción ya incoado contra su larga duración | renovacion-modificacion-extincion (alegaciones, arts. 201 y 202) |
| Reagrupado cuya larga duración se extinguió | No puede pedir la recuperación (arts. 186.2 y 188.2): debe reagruparlo el reagrupante (reagrupacion-familiar) |
| Nacionalidad por residencia | nacionalidad-residencia |

## Datos que hay que reunir antes de redactar

Los marcados con ★ son imprescindibles.

1. ★ Historial completo de autorizaciones: tipo, fecha de concesión y de caducidad de cada una, renovaciones y huecos entre caducidad y nueva solicitud; periodos de estancia por estudios; tiempo como solicitante y beneficiario de protección internacional; Tarjeta azul-UE en otros Estados.
2. ★ Ausencias de España en los cinco años: fechas de salida y regreso, destino y motivo (laboral, fuerza mayor, cooperación); si alguna salida fue irregular.
3. ★ Autorización vigente y su fecha de caducidad (fija el plazo de presentación).
4. ★ Para larga duración-UE: recursos fijos y regulares de la unidad familiar (origen, cuantía, estabilidad) y seguro de enfermedad.
5. ★ Antecedentes penales en España y en los países de residencia de los cinco años previos; antecedentes policiales; expulsiones.
6. Hijos a cargo en edad de escolarización obligatoria (art. 184.3.c).
7. Supuestos del art. 183.3: resolución de la pensión, partida de nacimiento, tutela, pérdida de la nacionalidad, estatuto de protección.
8. Recuperación: fecha y causa de la extinción, tiempo fuera de España o de la Unión, lugar de residencia actual, compromiso de no retorno y su plazo.
9. Renovación de tarjeta: fecha de caducidad y edad del titular.
10. Representación.

## Requisitos y comprobaciones

Lee cada artículo con `buscar_articulo` antes de afirmarlo. Si la respuesta trae una nota «Téngase en cuenta…» (nulidad declarada por el Tribunal Supremo o reforma), léela y aplícala: lo anulado no se aplica ni se cita como vigente.

**Elección entre las dos figuras.** La larga duración-UE (arts. 175-176) exige, además de los cinco años, recursos fijos y regulares y seguro de enfermedad, y da el estatuto de la Directiva 2003/109/CE (movilidad a otros Estados). La nacional (arts. 182-183) exige solo la residencia (o un supuesto del art. 183.3). El Supremo declaró, con el Reglamento anterior, que para la nacional no se exigen las condiciones propias de la de la Unión; comprueba al leer los arts. 182-184 vigentes que siguen sin exigir recursos ni seguro y cita esa doctrina advirtiendo de la norma que interpretaba. Si el cliente no acredita recursos o seguro, pide la nacional.

**Cómputo de los cinco años (arts. 176.a y 183).**

- Residencia legal y continuada durante los cinco años **anteriores a la solicitud**.
- Ausencias que no rompen la continuidad: hasta seis meses continuados y diez meses en total; por motivos laborales, seis meses continuados y dieciocho en total; salidas irregulares no se benefician. En la nacional, también fuerza mayor valorada individualmente y cooperantes (art. 183.2).
- Estancia por estudios: computa al 50 % si al solicitar está en residencia (art. 176.a); protección internacional: 100 % del tiempo desde la solicitud hasta la autorización; Tarjeta azul-UE: reglas propias del art. 176.a.
- **Cómo se combinan los topes de ausencias:** suma por separado las ausencias no laborales (tope de diez meses) y las laborales (tope de dieciocho meses), comprueba que ninguna supera seis meses continuados y da también el total de todas. La lectura prudente es que las no laborales no pasen de diez meses y el total no pase de dieciocho. Si el caso solo cumple calificando una ausencia como laboral, dilo en el resumen como riesgo principal y pide documentos del empleador (carta de desplazamiento con fechas y destino, nóminas del periodo). El art. 4.3 de la Directiva 2003/109/CE permite a los Estados tener en cuenta los traslados por motivos laborales.
- **Topes antiguos en la doctrina:** las sentencias dictadas con el art. 148 del Real Decreto 557/2011 aplican un tope de **un año** para las ausencias laborales; el vigente es de dieciocho meses. No traslades el tope antiguo y adviértelo si la Oficina lo aplica.
- Construye un **cuadro de cómputo**: una fila por periodo con título, fechas, días, porcentaje computable y documento; otra tabla con cada ausencia, su duración y el tope que respeta, y las sumas (no laborales, laborales y total). Si el total no llega, no redactes la solicitud: dile al abogado la fecha en que se cumplirá.

**Recursos y seguro (larga duración-UE, art. 176.b-c).** Recursos fijos y regulares con los términos y cuantías de la reagrupación (art. 67): pueden ser propios o de la actividad. Jurisprudenciator no devuelve la cuantía del IPREM: pídesela al abogado.

**Procedimiento (arts. 177 y 184).**

- Oficina de extranjería de la provincia de residencia; desde fuera, consulado de la demarcación.
- Plazo: en los dos meses anteriores a la caducidad de la autorización vigente (prorroga su validez) o en los tres posteriores, con posible sanción. Si la autorización está en vigor y ya se cumplen los requisitos, se puede pedir en cualquier momento (arts. 177.2 y 184.2).
- Documentos: pasaporte, tasa, recursos y seguro (UE), escolarización de menores (nacional), certificado de antecedentes de los países de residencia de cinco años cuando proceda (arts. 177.3 y 184.3). La oficina comprueba los tiempos y pide penados e informe policial.
- Denegación solo si la persona es una amenaza para el orden público o la seguridad pública (arts. 177.5 y 184.5).
- Resolución en tres meses; **transcurridos sin resolver, se entiende estimada** (arts. 177.6 y 184.6). TIE en un mes desde la notificación.

**Antecedentes penales.** El art. 184.3.e) pide un certificado «en el que no debe constar condenas», que sirve para valorar la amenaza. La doctrina del Supremo ha pasado de la denegación automática a exigir ponderación: tipo y gravedad del delito, peligro actual, duración de la residencia y vínculos. Léela antes de sostener una u otra cosa y comprueba si los antecedentes están cancelados o son cancelables.

**Tarjeta (arts. 178 y 185).** Renovación a los cinco años y cada cinco hasta los treinta años de edad, después cada diez; en los dos meses anteriores a su caducidad o en los tres posteriores. No renovarla no extingue la autorización (sí puede sancionarse); en la nacional, la oficina comprueba que se mantienen las condiciones.

**Extinción (art. 201; LOEX, art. 32.5).** Fraude; expulsión; ausencia del territorio de la **Unión** durante doce meses consecutivos (veinticuatro para quien procede de Tarjeta azul-UE y su familia; no para cooperantes); larga duración-UE adquirida en otro Estado; cese de la protección internacional; condena por los delitos de los arts. 177 bis y 318 bis del Código Penal; y, para la larga duración-UE, seis años fuera de España salvo decisión en contrario por motivos excepcionales.

**Recuperación (arts. 186-189).**

- Larga duración-UE: extinguida por ausencia de la Unión o por adquisición en otro Estado, o tras más de seis años fuera de España. Nacional: extinguida por esas mismas causas o tras cumplir el compromiso de no retorno de un retorno voluntario.
- No cabe para los reagrupados (salvo menores en la nacional): los reagrupa de nuevo el reagrupante.
- Solicitud **personal** ante la oficina de la provincia donde vaya a residir o ante el consulado; desde fuera, visado con los requisitos del art. 38 que indica el artículo; recursos y seguro en la UE.
- **Desde España, la larga duración-UE exige estar en situación regular** (art. 187.2), y la oficina comprueba los requisitos de las letras a) a e) del art. 38 (impreso, no estar irregular, no ser rechazable, pasaporte con un año de vigencia y antecedentes de los países de residencia de cinco años), salvo la tasa del visado. En la nacional, el art. 189.2 remite a esas mismas letras, entre ellas la b) (no encontrarse irregularmente en España).
- **La extinción exige resolución** (art. 201.1: «mediante resolución del órgano competente»). Si el cliente ha superado la ausencia pero la extinción no se ha declarado, sigue en situación regular: aconseja pedir ya la recuperación, con resolución simultánea de la extinción (arts. 187.7 y 189.8), porque si se declara antes la extinción ya no podrá pedirla desde España. Explícale ese riesgo al abogado. Si ya se incoó la extinción, las alegaciones van por renovacion-modificacion-extincion (art. 202).
- Resolución en tres meses; **silencio favorable** (arts. 187.5 y 189.6). TIE de cinco años. La extinción y la recuperación pueden tramitarse a la vez.
- La doctrina del Supremo sobre recuperación con antecedentes exige ponderar tipo de delito, gravedad, peligro, duración de la residencia y vínculos.

**Residente de larga duración-UE de otro Estado (arts. 179-181).** Sin visado; solicitud antes de entrar o en los tres meses siguientes; documentación según vaya a trabajar o no; resolución en dos meses con **silencio desestimatorio**; entrada en tres meses; la familia que formaba parte de la unidad en el otro Estado obtiene residencia por reagrupación. Tras la residencia en España puede acceder a la larga duración-UE española (art. 181).

**Causas típicas de denegación y respuesta.**

| Causa | Respuesta |
|---|---|
| No se completan cinco años (huecos entre autorizaciones) | Cuadro de cómputo con la prórroga de vigencia de cada renovación presentada en plazo; doctrina sobre huecos |
| Ausencias por encima de los topes | Motivo laboral (topes mayores), fuerza mayor en la nacional (art. 183.2), cooperación; documenta cada salida |
| Estancia por estudios computada entera | Solo el 50 % y solo si al pedir está en residencia (art. 176.a); recalcula antes de presentar |
| Recursos no fijos ni regulares (UE) | Pide la nacional, que no los exige, o acredita estabilidad con los criterios del art. 67 |
| Sin seguro de enfermedad (UE) | Alta en la Seguridad Social o seguro privado; o la nacional |
| Antecedentes penales | Cancelación o cancelabilidad; ponderación de gravedad, actualidad, arraigo y duración de la residencia |
| Menores sin escolarizar (nacional) | Informe de escolarización en el mes de advertencia (art. 184.4) |

## Estrategia y jurisprudencia

1. Presenta en cuanto se cumplan los cinco años si la autorización está en vigor: no hace falta esperar a su caducidad.
2. Si hay dudas sobre alguna ausencia, documenta el motivo (contratos, bajas médicas, fuerza mayor) y plantea subsidiariamente la nacional, que admite la fuerza mayor.
3. Los huecos entre una autorización caducada y la solicitud de renovación presentada en los tres meses posteriores se discuten a menudo: busca doctrina antes de computarlos.
4. Consultas (reformula como máximo dos veces):
   - Continuidad y ausencias: `buscar_sentencias` (`consulta="residencia de larga duración continuidad ausencias diez meses cinco años"`, `base="AN"`, `jurisdiccion="CONTENCIOSO"`).
   - Requisitos de la nacional frente a la UE: `consulta="residencia de larga duración requisitos cinco años residencia legal continuada"`, `base="TS"`, `jurisdiccion="CONTENCIOSO"`; elige la sentencia cuyo resumen trate de la larga duración que no es la de la Unión.
   - Antecedentes: `consulta="residencia de larga duración antecedentes penales ponderación orden público"`, `base="TS"`.
   - Recuperación: `consulta="recuperación autorización residencia larga duración antecedentes penales proporcionalidad"`, `base="TS"`; `consulta="recuperación larga duración ausencia seis años"`, `base="AN"`; y, para la ausencia de doce meses de la Unión, `consulta="recuperación residencia larga duración UE ausencia doce meses consecutivos territorio Unión Europea"`, `base="AN"`.
   - Regulación vigente: añade `fecha_desde="20/05/2025"` y, si no hay resultados, amplía.
5. Buena parte de la doctrina interpreta los arts. 147 a 166 del Real Decreto 557/2011. Úsala para cuestiones que el nuevo texto mantiene (ausencias, antecedentes, recuperación) y dilo en el escrito; ojo con los topes de ausencias laborales, que han cambiado (un año antes, dieciocho meses ahora).
6. **Comprueba que el párrafo que citas es razonamiento de la Sala.** Los «párrafos clave» de `leer_sentencias` traen a menudo alegaciones de las partes («intereso la estimación…», «la parte apelante…»), la resolución administrativa recurrida o la transcripción de la norma: eso no es doctrina y no se cita como tal. Si ninguna sentencia leída contiene razonamiento aplicable, en una solicitud redacta sin ese fundamento y explícalo en el resumen (no es causa de detención: la solicitud se apoya en el texto del artículo).

## Documento que se entrega

Word maquetado según `references/formato-y-organos.md`, que acompaña al impreso oficial vigente (no lo sustituye). Sin importes de tasas ni códigos de modelos.

En el escrito, cita el Reglamento como «artículo N del Real Decreto 1155/2024» y el resto de normas como indica el apartado 4 de `references/formato-y-organos.md`, para que `verificar_escrito` las reconozca.

Nombres: `solicitud-larga-duracion-<apellido-cliente>-<AAAAMMDD>.docx`, `solicitud-recuperacion-larga-duracion-<apellido-cliente>-<AAAAMMDD>.docx` o `solicitud-residencia-ld-ue-otro-estado-<apellido-cliente>-<AAAAMMDD>.docx`.

1. Encabezamiento: «A LA OFICINA DE EXTRANJERÍA DE [PROVINCIA] — [DELEGACIÓN / SUBDELEGACIÓN] DEL GOBIERNO» (art. 193.2) o la oficina consular si se presenta desde fuera.
2. Comparecencia: `[NOMBRE Y APELLIDOS]`, `[NIE]`, `[PASAPORTE]`, `[DOMICILIO]`; representación y su título.
3. EXPONE — HECHOS: PRIMERO, identidad y autorización vigente con su caducidad; SEGUNDO, trayectoria de residencia (remite al anexo de cómputo); TERCERO, ausencias y su motivo; CUARTO, recursos y seguro (UE) o supuesto del art. 183.3; QUINTO, antecedentes; SEXTO, en la recuperación, extinción previa y situación actual.
4. FUNDAMENTOS DE DERECHO: I, LOEX art. 32 y Directiva 2003/109/CE; II, figura elegida y por qué (UE o nacional, con subsidiariedad si procede); III, cómputo y continuidad; IV, requisitos restantes; V, doctrina con párrafo literal y ECLI; VI, plazo, silencio estimatorio y efectos.
5. SOLICITA la concesión (o recuperación) y, **subsidiariamente**, la larga duración nacional si se pidió la UE. En la recuperación, pide la resolución simultánea con la extinción (arts. 187.7 y 189.8).
6. OTROSÍ: que se tenga por prorrogada la autorización vigente hasta resolver cuando la solicitud dependa del plazo de su caducidad (no hace falta si se presenta con autorización en vigor y requisitos ya cumplidos, art. 177.2 último párrafo); que la oficina compruebe de oficio los tiempos de residencia; en la recuperación, audiencia y ponderación del art. 202 si se incoa la extinción.
7. Lugar, fecha, firma y RELACIÓN DE DOCUMENTOS numerada.
8. **ANEXO I — Cuadro de cómputo**: tabla de periodos (título, desde, hasta, días, % computable, días computados, documento) y tabla de ausencias (salida, regreso, días, motivo, tope aplicado).

**Reparto para la redacción rápida:** 01 encabezamiento, comparecencia y hechos; 02 fundamentos: figura elegida, requisitos restantes, plazo y efectos; 03 cómputo y continuidad con su doctrina; 04 solicita, otrosí, firma, relación de documentos y Anexo I. El cuadro de cómputo lo calcula el director antes del plan y lo deja en `caso.md`; la sección de cierre lo reproduce como anexo.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió y ninguna consulta imprescindible quedó sin resultado.
- [ ] Leídos con `buscar_articulo` en esta conversación LOEX 32 y los arts. 175-189 y 201 del Reglamento que se citan.
- [ ] Cuadro de cómputo cerrado a la fecha prevista de presentación; ausencias no laborales, laborales y total sumadas por separado y dentro de los topes vigentes; porcentajes aplicados con su artículo.
- [ ] En la recuperación desde España: situación regular comprobada (extinción no declarada o autorización vigente) y requisitos del art. 38 a) a e).
- [ ] Plazo de presentación con fecha y precepto; silencio estimatorio o desestimatorio del procedimiento concreto citado con su artículo.
- [ ] Cada ECLI leído con `leer_sentencias` o comprobado con `buscar_por_cita`.
- [ ] `verificar_escrito` pasado por cada redactor sobre sus frases con normas y corregido lo que señale; ninguna cita a un «art. 32 bis» de la LOEX.
- [ ] Marcadores para lo que falta; cuantías confirmadas por el abogado.
- [ ] Resumen para el abogado según el apartado 7 del formato: figura y oficina, fecha límite y precepto, documentos que faltan y riesgos, tabla de jurisprudencia y próximo paso.
