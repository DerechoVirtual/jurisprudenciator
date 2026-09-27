---
name: informe-viabilidad-extranjeria
description: >-
  Estudio de viabilidad de las vías de extranjería de un cliente: qué autorización puede pedir hoy y
  cuál le conviene, requisito por requisito (cumple, no cumple, dudoso) con el artículo vigente del
  Reglamento aprobado por el Real Decreto 1155/2024, de la LOEX o de la Ley 14/2013, riesgos
  (expediente de expulsión, denegación, incompatibilidades), calendario y coste de oportunidad, y
  jurisprudencia de TSJ con párrafo literal sobre los requisitos dudosos. Entrega un informe en Word
  para el cliente o para el despacho. Úsala con «qué vía le conviene», «puede pedir arraigo», «estudio
  de viabilidad», «informe para el cliente», «qué opciones tiene». Para la primera toma de datos usa
  extranjeria-intake; para preparar la solicitud de una vía ya elegida, la skill de esa vía.
---

# Informe de viabilidad de extranjería

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Requisitos de cada vía candidata** → `buscar_articulo` (`ley="BOE-A-2024-24099"`: `"126"` y `"127"` arraigos, `"128"` razones humanitarias, `"61"` y `"62"` no lucrativa, `"66"` y `"67"` reagrupación, `"74"` y `"75"` cuenta ajena, `"84"` cuenta propia, `"94"` a `"98"` familiares de españoles, `"176"` y `"183"` larga duración, `"190"` y `"191"` modificaciones; `ley="LOEX"`: `"31"`, `"31 bis"` y `"32"`; `ley="BOE-A-2013-10074"`: `"62"` para la Ley 14/2013).
- **Antecedentes y orden público** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, `articulo="126"` y `articulo="130"`; `ley="LOEX"`, `articulo="31"`; `ley="CP"`, `articulo="136"` para la cancelación).
- **Efectos de cada vía** (duración, trabajo, prórroga, modificación posterior) → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"125"`, `"130"`, `"131"`, `"132"`, `"95"`, `"97"`, `"191"` y `"200"`).
- **Reglamento aplicable a una solicitud ya presentada** → `leer_boe` (`identificador="BOE-A-2024-24099"`), disposiciones transitorias primera y segunda del Real Decreto.
- **Jurisprudencia de TSJ sobre cada requisito dudoso** → `buscar_sentencias` (`base="AN"`, `jurisdiccion="CONTENCIOSO"`, `tipo_organo="TSJ"`, `provincia` del cliente y, para requisitos nuevos, `fecha_desde="20/05/2025"`) + `leer_sentencias` (`parrafos=3`, `terminos` del requisito). En `provincia` va la sede de la Sala del TSJ que conoce de la provincia del cliente, no la provincia misma cuando no coinciden (por ejemplo, para Almería, «Granada»; ocurre en las comunidades con varias sedes de Sala, como Andalucía, Canarias o Castilla y León): si la respuesta dice «Sin resultados en [provincia]», repite con la sede antes de caer al Supremo.
- **Doctrina del Supremo sobre antecedentes y sobre la sanción de la estancia irregular** → `buscar_sentencias` (`base="TS"`, `jurisdiccion="CONTENCIOSO"`) + `leer_sentencias`.
- **Qué inciso anuló exactamente el Tribunal Supremo** → `leer_boe` (`identificador="BOE-A-2026-19632"`): devuelve el fallo de la sentencia de 8 de julio de 2026 y el auto de rectificación de 1 de septiembre de 2026 con el texto literal de cada inciso anulado. Úsalo siempre que `buscar_articulo` traiga una nota de nulidad de un «inciso destacado»: el conector no conserva el resaltado y, sin el fallo, no se sabe qué palabras se anularon.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Las letras y los apartados de un artículo «bis» se escriben delante: «letra a) del artículo 53.1 de la Ley Orgánica 4/2000», «apartado 2 del artículo 63 bis de la Ley Orgánica 4/2000», nunca «artículo 53.1.a» ni «63 bis.2»: con la letra pegada al número, `verificar_escrito` no enlaza la norma que sigue y comprueba el artículo en la norma citada antes (da por buena una cita equivocada o por inexistente una correcta).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (el artículo que hay que citar, el requisito que hay que comprobar o la jurisprudencia que exige el apartado 8 de `references/formato-y-organos.md`), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- Después de la ficha de `extranjeria-intake`, cuando hay dos o más vías posibles o hay que decidir cuándo presentar.
- El cliente pregunta si puede pedir una autorización concreta y no está claro que cumpla algún requisito.
- Antes de presentar, para contrastar un requisito dudoso con la doctrina del TSJ del cliente.
- El despacho necesita un informe escrito para el cliente (presupuesto, expectativas, riesgos) o para el expediente interno.
- No la uses para redactar la solicitud de la vía elegida (usa la skill de esa vía), para la lista de documentos (`documentacion-expediente`), para recurrir (`recurso-administrativo-extranjeria` o `recurso-contencioso-extranjeria`) ni cuando hay una urgencia abierta (primero `extranjeria-intake` y su semáforo).

## Datos que hay que reunir antes de redactar

Si existe ficha del caso, léela y pregunta solo lo que falte. Los datos con ★ son imprescindibles.

1. ★ **Destinatario del informe**: cliente (lenguaje claro) o despacho (técnico). Cambia el registro, no el análisis.
2. ★ **Objetivo del cliente** y horizonte: trabajar cuanto antes, traer a la familia, estabilidad a largo plazo, nacionalidad.
3. ★ **Provincia de residencia**: fija el órgano competente (`buscar_articulo`, `ley="BOE-A-2024-24099"`, `articulo="193"`) y el TSJ cuya doctrina se busca.
4. ★ **Fecha exacta de entrada** y todas las salidas posteriores, con la prueba de cada una: sin ellas no se computa permanencia ni continuidad.
5. ★ **Situación administrativa y solicitudes en trámite** (tipo y fecha de presentación), incluida la protección internacional.
6. ★ **Antecedentes**: penales en España y en los países de residencia de los cinco años anteriores a la entrada, policiales, causas abiertas; fechas de extinción de las penas.
7. ★ **Vínculos**: familiares en España con su nacionalidad y situación; contratos u ofertas (jornada, salario, empleador); matrícula o formación.
8. Pruebas disponibles de cada hecho: empadronamiento histórico, informes sociales, historial médico, nóminas, contratos, certificados de estudios.
9. Si el cliente está dispuesto a salir de España para tramitar un visado (vías consulares).

## Requisitos y comprobaciones

### Paso 1. Filtra las vías candidatas

Parte de los hechos, no de las vías. Para cada hecho de la izquierda, lee los preceptos de la derecha y descarta o conserva la vía con una línea de motivo.

| Hecho del cliente | Vías que se estudian | Preceptos que se leen |
|---|---|---|
| En España sin autorización, dos años o más de permanencia | Arraigos social, sociolaboral, socioformativo, segunda oportunidad | Reglamento 125, 126 y 127 |
| En España sin autorización, menos de dos años | Arraigo familiar (sin permanencia mínima), familiar de español, razones humanitarias, víctimas | Reglamento 126.b, 127.e, 94, 97, 128; LOEX 31 bis y 59 bis |
| Cónyuge, pareja, hijo, ascendiente o progenitor de español | Autorización de familiar de persona con nacionalidad española (no el arraigo familiar) | Reglamento 94 a 98 |
| Familiar de ciudadano de otro Estado de la Unión | Régimen de la Unión | `ley="Real Decreto 240/2007"`, arts. 2, 2 bis, 7 y 8 |
| Titular de una autorización | Modificación, renovación, larga duración, reagrupar a su familia | Reglamento 191, 176, 183, 66 y 67 |
| Estancia por estudios | Paso a residencia y trabajo | Reglamento 190 |
| Fuera de España | Visado de residencia de la vía que proceda, Ley 14/2013 | Reglamento 38; `ley="BOE-A-2013-10074"`, art. 62 |

En el Reglamento vigente el arraigo familiar solo cubre al progenitor o tutor de un menor de otro Estado de la Unión, del EEE o de Suiza y a quien presta apoyo a una persona con discapacidad de esa nacionalidad (art. 127.e): los familiares de españoles van por los arts. 94 a 98. Compruébalo con `buscar_articulo` en cada informe.

### Paso 2. Requisito por requisito

Para cada vía conservada, construye una tabla con estas columnas: requisito (copiado del texto que devuelve `buscar_articulo`, sin parafrasear), precepto, hecho del cliente, prueba disponible y estado (cumple · no cumple · dudoso · falta dato). Puntos que se revisan siempre, cada uno con su artículo leído en el momento:

- **Permanencia continuada** (Reglamento 126.b): cuenta desde la fecha de entrada probada; resta el tiempo como solicitante de protección internacional; anota cada salida. El art. 126.b no dice qué ausencias toleran la continuidad: si hubo salidas, el requisito es «dudoso», calcula también la fecha más temprana si la oficina considerase interrumpida la permanencia (dos años desde la última entrada) y busca doctrina. Las reglas de ausencias de la larga duración (arts. 176.a y 183.2) solo sirven como argumento de apoyo, no como regla del arraigo.
- **Protección internacional e incompatibilidades** (Reglamento 126.a y 126.h): si hay una solicitud de protección no firme o cualquier procedimiento de autorización en curso, la vía de arraigo queda bloqueada hasta que se resuelva o se desista; dilo como primera conclusión.
- **Antecedentes penales** (Reglamento 126.d y 130.2; LOEX 31.5): España y países de residencia de los cinco años anteriores a la entrada; supuestos en que no hay que aportar el certificado del tercer país (art. 130.2); los antecedentes policiales no deniegan por sí solos (último párrafo del art. 130.2). Calcula si los penales están cancelados o son cancelables con el art. 136 CP.
- **Prohibición de entrada, rechazable y compromiso de no retorno** (Reglamento 126.e y 126.f; 11).
- **Requisito específico de cada arraigo** (Reglamento 127): medios del 100 % del IPREM o informe de integración en el social; contratos con salario mínimo o de convenio y veinte horas semanales en cómputo global en el sociolaboral (lee también el art. 74, al que remite la letra b) del art. 127 para los requisitos del empleador: su letra c) exige en los contratos a tiempo parcial una retribución anual igual al salario mínimo de jornada completa, así que un contrato de pocas horas con salario proporcional es un requisito «dudoso» hasta que haya doctrina; firma de las dos partes, arts. 74.1.b y 130.1.b); formación de los arts. 52.1.b o 52.1.e.5.º y ventana de presentación en el socioformativo; titularidad previa de residencia en el de segunda oportunidad.
- **Familiares de españoles**: categoría del art. 94, convivencia, régimen de orden público del art. 98 y habilitación provisional del art. 97.5. Lee las notas de nulidad que devuelva el conector (la Sentencia del Tribunal Supremo de 8 de julio de 2026 anuló incisos o apartados de los arts. 94.1.f, 97.4, 98.1, 101.1, 159.1, 160.1, 160.2, 166.1, 196.b y 197.2) y, para saber qué palabras exactas se anularon, el fallo con `leer_boe` (`identificador="BOE-A-2026-19632"`). Aplica el texto depurado: lo anulado no se aplica y lo que el fallo declara conforme sigue vigente. En los familiares de españoles importa sobre todo que se anularon los incisos de los arts. 97.4 y 98.1 que imponían la denegación automática por antecedentes penales sin ponderación individualizada en los supuestos del artículo 20 del Tratado de Funcionamiento de la Unión Europea. Ojo: el art. 97.4 exige, para las solicitudes presentadas desde España, los requisitos del art. 38 (su letra e: carecer de antecedentes) y el art. 98.1 solo excluye la denegación automática para las letras distintas de c), g), h) e i) del art. 94.1; si el solicitante tiene antecedentes, trata el requisito como «dudoso» y busca doctrina. El conector no devuelve el Tratado de Funcionamiento de la Unión Europea ni `verificar_escrito` lo identifica (atribuye su artículo a otra norma): nómbralo sin número de artículo o explica el supuesto sin citarlo.
- **Reagrupación**: familiar reagrupable (art. 66), recursos, vivienda con informe de antigüedad máxima de seis meses, seguro y escolarización (art. 67).
- **Cuenta ajena y cuenta propia**: arts. 74, 75 y 84; desde una residencia previa, art. 191 (qué requisitos se exigen según el tiempo de residencia y qué autorizaciones no permiten modificar, art. 191.7).
- **Tasa** (Reglamento 126.g y equivalentes): anota que existe; el importe y el modelo se comprueban en la sede oficial.

Si una solicitud del cliente se presentó antes del 20/05/2025, lee con `leer_boe` la disposición transitoria segunda del Real Decreto 1155/2024 antes de decidir qué reglamento se aplica.

### Paso 3. Riesgos

- **Sancionador**: si el cliente está en situación irregular, lee LOEX 53.1.a y 57 y la doctrina del Supremo sobre la elección entre multa y expulsión; lee LOEX 63.6 (suspensión del expediente preferente por solicitud previa del art. 31.3) y anota su efecto en la estrategia de fechas.
- **Condena no cancelada**: si hay condena por delito doloso castigado con pena privativa de libertad superior a un año, lee LOEX 57.2 (causa de expulsión «salvo que los antecedentes penales hubieran sido cancelados») y 63.1 (se tramita por el procedimiento preferente): es un riesgo principal, exista o no solicitud. Calcula con el art. 136 CP (y el art. 33 CP para clasificar la pena) la fecha desde la que los antecedentes son cancelables, aplicando la regla del apartado 2 si la pena se suspendió, y ponla en el calendario: desde esa fecha desaparecen a la vez la causa de expulsión y el bloqueo del art. 126.d.
- **Denegación**: qué se pierde si se deniega (tasa, tiempo, visibilidad ante la Administración) y qué vía queda después.
- **Incompatibilidades y bloqueos**: arts. 126.a, 126.h y 191.7 del Reglamento.
- **Mantenimiento**: condiciones de prórroga (art. 132.2), causas de extinción (art. 200) y la del socioformativo por falta de matrícula (art. 127.d).
- **Preceptos no disponibles**: si una vía depende de una disposición adicional o transitoria que el conector no devuelve (por ejemplo, la transitoria quinta del Real Decreto 1155/2024), aplica la puerta, no valores esa vía y explica al abogado qué precepto falta. Las adicionales vigésima y vigesimoprimera del Reglamento (arraigo de solicitantes de protección internacional y arraigo extraordinario, añadidas por el Real Decreto 316/2026) sí se leen con `leer_boe` (`identificador="BOE-A-2026-8284"`): la vigésima completa y la vigesimoprimera hasta su apartado 5; el plazo de solicitud de ambas terminó el 30/06/2026, así que solo importan si el cliente ya presentó una de esas solicitudes (en ese caso, además, está en curso y bloquea otras vías por el art. 126.h).

### Paso 4. Calendario

- Fecha más temprana de presentación de cada vía (día en que se cumple la permanencia, ventana del socioformativo, ventana de renovación del título actual).
- Plazo de resolución y sentido del silencio solo si lo dice el artículo del procedimiento que has leído (por ejemplo, arts. 63.4 o 97.6 del Reglamento). Si depende de una disposición adicional, escribe «no disponible en el conector: se comprobará en la resolución o en la sede oficial».
- Obligaciones posteriores a la concesión: alta en Seguridad Social y tarjeta en el plazo del art. 130.5 y 130.6 o del art. 209.

### Paso 5. Coste de oportunidad

Compara las vías viables con estos criterios, cada uno con su precepto leído: duración de la autorización (art. 125.2; art. 95.3), habilitación para trabajar (arts. 131 y 95.1), requisitos de la prórroga (art. 132), posibilidad de reagrupar (art. 95.2), puerta a la modificación (art. 191), cómputo hacia la larga duración (art. 176) y la nacionalidad (`ley="CC"`, art. 22: residencia legal), coste de tasas (art. 126.g frente al carácter gratuito del art. 97.8) y tiempo hasta poder trabajar (habilitación provisional de los arts. 130.5 y 97.5).

## Estrategia y jurisprudencia

- Busca jurisprudencia solo para los requisitos en estado «dudoso»; los que se cumplen o se incumplen con claridad no necesitan doctrina.
- Si tras la consulta y dos reformulaciones no hay doctrina sobre un requisito dudoso (es frecuente en los requisitos nuevos del Real Decreto 1155/2024), no detengas el informe: la puerta se aplica cuando falta el texto del precepto que hay que citar o comprobar, no cuando aún no hay jurisprudencia sobre él. Escribe en el apartado de jurisprudencia «sin doctrina localizada», con las consultas hechas, y valora el requisito solo con el texto leído, como «dudoso». Nunca rellenes el hueco con doctrina de memoria.
- Consultas de partida (ajústalas al hecho concreto):
  - Permanencia: `consulta="arraigo permanencia continuada dos años prueba empadronamiento ausencias"`.
  - Informe de integración: `consulta="arraigo informe de integración no emitido en plazo cualquier medio de prueba"`.
  - Medios del arraigo social: `consulta="arraigo social medios económicos IPREM familiares residentes"`.
  - Contrato del sociolaboral: `consulta="arraigo sociolaboral contrato salario mínimo jornada veinte horas empleador"`.
  - Antecedentes policiales o cancelados: `consulta="antecedentes policiales antecedentes penales cancelados denegación autorización residencia"` con `base="TS"`.
  - Familiar de español a cargo: `consulta="familiar de ciudadano español a cargo dependencia económica autorización de residencia"`.
  - Progenitor de menor español con antecedentes: `consulta="familiar de ciudadano español progenitor menor español antecedentes penales orden público ponderación"`, con `fecha_desde="20/05/2025"`. La doctrina del Supremo sobre el antiguo arraigo familiar (no aplicación automática de los antecedentes al progenitor de un menor ciudadano de la Unión que convive con él o está al corriente de sus obligaciones) se traslada a la letra f) del art. 94.1 porque depende de la ciudadanía europea del menor, no del requisito reglamentario; dilo en el informe.
- Orden de búsqueda: TSJ de la provincia del cliente → todos los TSJ → Supremo. Usa `opciones_busqueda` si la lista sale demasiado amplia.
- **Comprueba qué reglamento aplica cada sentencia**: muchas resoluciones de 2025 y 2026 resuelven solicitudes presentadas con el Reglamento anterior (Real Decreto 557/2011), que exigía otros plazos de permanencia y otras figuras de arraigo. Lee el párrafo y, si la sentencia aplica el reglamento derogado, úsala solo para criterios que no dependan del requisito cambiado (valoración de la prueba, proporcionalidad, antecedentes) y dilo en el informe.
- Lee solo las 2-3 resoluciones que vas a citar (`leer_sentencias`, `parrafos=3`, `terminos` del requisito). En el informe: párrafo literal entre comillas, órgano, fecha, número y ECLI tal como los devolvió la herramienta, y una frase sobre cómo afecta al requisito del cliente. Si la doctrina está dividida, expón las dos líneas.
- Valora la probabilidad de cada vía en términos cualitativos (alta, media, baja) con su motivo; nunca en porcentajes.

### Errores que invalidan el informe

- Confundir el arraigo familiar del Reglamento vigente (art. 127.e) con la autorización de familiar de persona con nacionalidad española (arts. 94 a 98).
- Contar la permanencia desde el primer empadronamiento y no desde la entrada probada, o no restar el tiempo como solicitante de protección internacional (art. 126.b).
- Recomendar una vía sin comprobar que no hay otro procedimiento de autorización en curso (art. 126.h) ni una solicitud de protección internacional no firme (art. 126.a).
- Dar por irrelevantes unos antecedentes «antiguos» sin calcular su cancelación con el art. 136 CP.
- Trasladar a una solicitud nueva los requisitos o plazos de una sentencia que aplica el Real Decreto 557/2011.
- Recomendar una modificación desde una autorización que no la admite (art. 191.7).
- Anunciar importes de tasas o plazos de resolución que no salen de un artículo leído.
- Presentar un resultado como seguro: el informe da una valoración motivada, no una garantía.

## Documento que se entrega

**Informe de viabilidad en Word** (formato de `references/formato-y-organos.md`). Nombre: `informe-viabilidad-<apellido-cliente>-<AAAAMMDD>.docx`. Es un informe, no un escrito: sin súplica; firma del abogado al final.

Cita las normas en el documento como indica el apartado 4 de `references/formato-y-organos.md`, para que `verificar_escrito` las reconozca: «artículo N del Real Decreto 1155/2024» (nunca «del Reglamento de extranjería» ni «del Reglamento aprobado por…»), «artículo N de la Ley Orgánica 4/2000» y «Ley 14/2013, de 27 de septiembre». En esta skill, «Reglamento» es solo una abreviatura de trabajo del Real Decreto 1155/2024. Las letras van delante del número («letra c) del artículo 94.1 del Real Decreto 1155/2024»), nunca pegadas («94.1.c»). Cada cita lleva su norma aunque se repita: un «artículo 127» suelto después de citar el Código Civil o la Ley Orgánica 4/2000 lo comprueba `verificar_escrito` en esa otra norma. No cites artículos «del Real Decreto 316/2026»: `verificar_escrito` identifica ese número con otra norma; cita el artículo modificado del Real Decreto 1155/2024 y di que su redacción es la del Real Decreto 316/2026.

1. **Cabecera**: «INFORME DE VIABILIDAD — EXTRANJERÍA», destinatario, fecha, «Confidencial».
2. **Conclusión** (máximo diez líneas): vía recomendada, fecha más temprana de presentación, dos riesgos principales, qué falta para presentar.
3. **Hechos tenidos en cuenta**: con marcadores para lo no facilitado y la advertencia de que el informe depende de ellos.
4. **Vías estudiadas**: tabla vía · cumple hoy · requisitos pendientes · fecha más temprana · valoración.
5. **Análisis de cada vía**: tabla de requisitos del Paso 2 y un párrafo de valoración.
6. **Jurisprudencia sobre los requisitos dudosos**.
7. **Riesgos**.
8. **Calendario**: tabla fecha · hito · precepto.
9. **Comparativa y recomendación**: coste de oportunidad del Paso 5.
10. **Siguientes pasos**: documentos que reunir (remite a `documentacion-expediente`) y skill que redactará la solicitud.
11. **Límites del informe**: preceptos no disponibles en el conector; tasas, modelos y cita previa se comprueban en la sede oficial.
12. **Normativa consultada**: artículo, norma y «vigente desde».

En la versión para el cliente, sustituye las tablas técnicas por frases cortas y deja los artículos en notas al pie; conserva la conclusión, los riesgos y el calendario. Si el documento no admite notas al pie, numera las remisiones en el texto ([1], [2]…) y pon las notas en el último apartado, cada una con el artículo y su norma completos para que `verificar_escrito` los compruebe. Los párrafos de jurisprudencia se mantienen literales, seguidos de una explicación en lenguaje sencillo.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió antes de empezar.
- [ ] Cada requisito de cada vía se copió del texto devuelto por `buscar_articulo` en esta conversación, con su «vigente desde» y, si las hay, sus notas de nulidad o modificación.
- [ ] Ninguna vía que dependa de una disposición adicional o transitoria no disponible se ha valorado de memoria.
- [ ] Cada ECLI citado se leyó con `leer_sentencias` o se comprobó con `buscar_por_cita`, y se verificó qué reglamento aplica la resolución.
- [ ] Permanencia, antecedentes y plazos calculados con fechas probadas; lo que falta figura con marcador.
- [ ] Sin importes de tasas ni códigos de modelos: remitidos a la sede oficial.
- [ ] `verificar_escrito` pasado sobre el informe completo; cada aviso revisado uno a uno (un «no localizado» o una norma que no es la citada suele venir de una letra pegada al número o de un artículo sin su norma: corrige la forma de citar y vuelve a pasarlo).
- [ ] Resumen en el chat según el apartado 7 del formato: qué se ha preparado y para quién, fechas clave con su precepto, documentos que faltan y riesgos, tabla de jurisprudencia (ECLI · órgano · fecha · qué sostiene) y próximo paso.
