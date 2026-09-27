---
name: documentacion-expediente
description: >-
  Lista de documentos de un trámite de extranjería y revisión de un expediente ya reunido. Saca del
  artículo de procedimiento del Reglamento aprobado por el Real Decreto 1155/2024 cada documento
  exigido (arraigos y circunstancias excepcionales, visados, reagrupación, cuenta ajena y propia,
  familiares de españoles, larga duración, renovaciones) y comprueba los requisitos formales
  (pasaporte en vigor, antecedentes penales, legalización o apostilla, traducción, empadronamiento),
  la forma de presentación, la representación, la tasa y la cita previa (sin importes ni códigos: se
  comprueban en la sede oficial) y los plazos de subsanación. Entrega una checklist en Word. Úsala con
  «qué papeles necesita», «lista de documentos», «revisa el expediente antes de presentar», «falta
  algo para el arraigo». Para contestar un requerimiento ya notificado usa
  recurso-administrativo-extranjeria.
---

# Documentación del expediente de extranjería

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Documentos que exige el procedimiento** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, el artículo de procedimiento de la vía: `"130"` circunstancias excepcionales, `"38"` a `"41"` visados, `"63"` no lucrativa, `"68"` reagrupación, `"77"` cuenta ajena, `"85"` cuenta propia, `"96"` y `"97"` familiares de españoles, `"177"` y `"184"` larga duración, `"159"` y `"160"` menores, `"64"`, `"71"`, `"80"` y `"86"` renovaciones; y el artículo de requisitos de esa vía).
- **Identidad y documentos del extranjero** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, artículos `"38"`, `"130"`, `"200"`, `"205"`, `"207"`, `"209"` y `"210"`).
- **Antecedentes penales** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, `articulo="126"` y `articulo="130"`; `ley="LOEX"`, `articulo="31"`).
- **Lugar de presentación, comparecencia personal y representación** → `buscar_articulo` (`ley="BOE-A-2024-24099"`, `articulo="193"` y `articulo="197"`; `ley="LPAC"`, artículos `"5"`, `"14"`, `"16"` y `"66"`).
- **Lengua, copias y documentos que ya tiene la Administración** → `buscar_articulo` (`ley="LPAC"`, artículos `"15"`, `"27"` y `"28"`).
- **Tasa y subsanación** → `buscar_articulo` (`ley="LOEX"`, `articulo="44"`; `ley="BOE-A-2024-24099"`, `articulo="130"` o el del procedimiento; `ley="LPAC"`, artículos `"68"`, `"73"` y `"118"`).
- **Criterio judicial sobre documentos defectuosos o aportados tarde** → `buscar_sentencias` (`base="AN"`, `jurisdiccion="CONTENCIOSO"`, `tipo_organo="TSJ"`) + `leer_sentencias` (`parrafos=3`).
- **Qué inciso anuló exactamente el Tribunal Supremo** → `leer_boe` (`identificador="BOE-A-2026-19632"`): devuelve el fallo de la sentencia de 8 de julio de 2026 y el auto de rectificación de 1 de septiembre de 2026 con el texto literal de cada inciso anulado. Úsalo siempre que `buscar_articulo` traiga una nota de nulidad de un «inciso destacado»: el conector no conserva el resaltado y, sin el fallo, no se sabe qué palabras se anularon.
- **Revisión del documento antes de entregarlo** → `verificar_escrito` con el texto completo, y `buscar_por_cita` sobre cada ECLI que no se haya leído en esta conversación.

Cita solo lo que devuelva Jurisprudenciator (artículo vigente, ECLI o ROJ con su párrafo literal...). En el documento, cita el Reglamento como «artículo N del Real Decreto 1155/2024»: es la forma que reconoce `verificar_escrito` (con «Reglamento de Extranjería» da la cita por inexistente). Las letras y los apartados de un artículo «bis» se escriben delante: «letra a) del artículo 53.1 de la Ley Orgánica 4/2000», «apartado 2 del artículo 63 bis de la Ley Orgánica 4/2000», nunca «artículo 53.1.a» ni «63 bis.2»: con la letra pegada al número, `verificar_escrito` no enlaza la norma que sigue y comprueba el artículo en la norma citada antes (da por buena una cita equivocada o por inexistente una correcta).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar o el requisito que hay que comprobar), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo usarla

- La vía ya está elegida y hay que decirle al cliente qué documentos reunir y con qué formalidades.
- El cliente trae una carpeta y hay que revisar, antes de presentar, si está completa y si cada documento sirve.
- Después de `informe-viabilidad-extranjeria`, para convertir la vía recomendada en una lista de trabajo.
- Para preparar el contenido de una subsanación: esta skill dice qué documento falta y cómo debe venir; el escrito que lo acompaña lo redacta `recurso-administrativo-extranjeria`.
- No la uses para decidir la vía (usa `extranjeria-intake` o `informe-viabilidad-extranjeria`) ni para valorar si se cumple un requisito de fondo discutible.

## Datos que hay que reunir antes de redactar

Los datos con ★ son imprescindibles; sin ellos no se elabora la lista.

1. ★ **Trámite exacto**: tipo de autorización o visado, inicial, prórroga, renovación o modificación.
2. ★ **Dónde está el extranjero y dónde se presenta**: oficina de extranjería de la provincia (España) u oficina consular (extranjero).
3. ★ **Provincia de residencia** o de destino, para el órgano competente.
4. ★ **Quién presenta**: el propio extranjero, el empleador, el familiar español, el reagrupante o el abogado como representante.
5. ★ **Fecha prevista de presentación**: las vigencias se comprueban a esa fecha.
6. ★ **Nacionalidad y países de residencia de los últimos cinco años anteriores a la entrada**: determinan qué certificados de antecedentes y qué legalización o apostilla hacen falta.
7. ★ Si se trata de revisar un expediente: **los documentos reunidos** (archivos o relación detallada con fecha de expedición de cada uno).
8. ★ Si hay un requerimiento notificado: **copia y fecha de notificación**.
9. Opcional: edad (menor de edad penal), menores a cargo en edad escolar, discapacidad o necesidad de apoyo, empadronamientos anteriores.

## Requisitos y comprobaciones

### 1. Lista base desde el artículo del procedimiento

Lee con `buscar_articulo` el artículo de procedimiento y el de requisitos de la vía. Cada documento que mencione el texto es una fila de la checklist con su artículo y letra. No añadas documentos que el texto no exija salvo como «prueba recomendada», y di por qué la recomiendas. Si el texto devuelto trae una nota de nulidad o de modificación, trabaja con el texto depurado y anota la nota.

Si el trámite termina en un visado (reagrupación familiar, cuenta ajena o familiar de español que está fuera de España), la checklist tiene **dos fases**: la de la oficina de extranjería (artículo del procedimiento, por ejemplo el art. 68) y la del consulado (arts. 38 y 40: plazo para pedir el visado, originales de los documentos de parentesco, pasaporte con la vigencia mínima del art. 38.d, antecedentes del art. 38.e, certificado médico del art. 38.i y tasa del visado). Comprueba ya, a la fecha de presentación, las vigencias que exigirá la segunda fase: un pasaporte válido para presentar puede no serlo para el visado.

Comprueba también que cada persona para la que se piden los documentos está dentro del ámbito del precepto (por ejemplo, en la reagrupación, los hijos solo si son menores de dieciocho años al solicitar o tienen una discapacidad o un estado de salud que les impide proveer a sus necesidades, art. 66.1.c). Si alguien no entra, no le hagas lista: márcalo como **bloqueante** en el apartado de bloqueantes, cita el precepto y deriva su caso a `informe-viabilidad-extranjeria`.

### 2. Requisitos formales que se revisan en todos los expedientes

- **Pasaporte**: «copia completa» y «en vigor» cuando lo diga el artículo (por ejemplo, Reglamento 130.1.a); en los visados de residencia, la vigencia mínima que fije el art. 38.d. Si está caducado en una solicitud inicial, es **bloqueante**: se renueva en el consulado antes de presentar. El art. 210 solo sirve si el consulado no puede documentarlo (con acta notarial que lo acredite) y el art. 200.2.f solo afecta a quien ya es titular de una autorización (causa de extinción). Pide también la copia completa del pasaporte anterior si en él consta el sello de entrada (art. 207): el nuevo no lo tendrá.
- **Antecedentes penales**: certificado de los países de residencia de los cinco años anteriores a la entrada cuando la persona sea mayor de edad penal (Reglamento 130.2 o el artículo de la vía); en los visados, el de los países de residencia de los últimos cinco años (art. 38.e). La mayoría de edad penal se fija con el art. 19 del Código Penal (`ley="CP"`). Comprueba si concurre alguno de los supuestos del art. 130.2 que eximen de aportarlo. El de España lo recaba de oficio la oficina (art. 130.2): no lo pidas al cliente salvo que el artículo de su vía diga otra cosa.
- **Vigencia de certificados**: el Reglamento no fija una caducidad general del certificado de antecedentes; anota la fecha de expedición y comprueba la vigencia que indique el propio certificado y el criterio publicado en la sede oficial. Cuando el artículo sí fija antigüedad (por ejemplo, el informe de vivienda del art. 67.2, seis meses), escríbela con su precepto.
- **Documentos públicos extranjeros**: la legalización o apostilla no está regulada en el Reglamento y el conector no devuelve el Convenio de La Haya de 1961 ni la lista de Estados parte (solo el Real Decreto 1497/2011 sobre las autoridades españolas que apostillan). Marca en cada documento extranjero «apostilla o legalización: comprobar en la fuente oficial según el país emisor» y no lo cites como norma en ningún escrito.
- **Lengua**: lee el art. 15 LPAC; todo documento en otra lengua se acompaña de traducción al castellano (o a la cooficial cuando proceda). La clase de traducción que acepta la oficina se comprueba en la sede oficial.
- **Copias y originales**: lee los arts. 27 y 28 LPAC (copias, cotejo excepcional, derecho a no aportar lo que ya obra en la Administración); señala qué documentos puede obtener de oficio la oficina.
- **Empadronamiento y prueba de permanencia**: el padrón histórico es la prueba central de la permanencia, pero no la única; lista las pruebas complementarias con fecha (asistencia sanitaria, escolarización, cursos, transferencias, contratos de alquiler). Comprueba con la búsqueda de jurisprudencia de abajo qué valor da el TSJ de la provincia al padrón aislado.
- **Informes autonómicos o municipales** (integración del art. 127.c, vivienda del art. 67.2): el artículo fija el plazo de emisión; guarda el justificante de la solicitud con fecha, porque si no se emite en plazo el requisito se puede acreditar por otros medios probando el retraso.
- **Contratos, medios y seguros**: contrato firmado por las dos partes cuando se exija (art. 130.1.b); en el arraigo sociolaboral y en la cuenta ajena, fecha de comienzo condicionada a la eficacia de la autorización (art. 74.1.b), requisitos del empleador del art. 74 (al corriente con Hacienda y la Seguridad Social, medios del art. 76) y, si el contrato es a tiempo parcial, la retribución anual del art. 74.1.c, que es un riesgo de fondo que se anota y se deriva a `informe-viabilidad-extranjeria`; certificación bancaria con los datos del art. 62.3 cuando se acrediten medios en cuentas extranjeras; seguro de enfermedad cuando lo pida la vía (arts. 61.2.b o 67.3); escolarización de menores (arts. 67.4 y 80.3).

### 3. Presentación, representación y órgano

- Órgano competente: art. 193.2 del Reglamento (provincia de residencia efectiva) salvo que la vía fije otro.
- Circunstancias excepcionales: solicitud personal del extranjero, con las excepciones de menores y personas con discapacidad (art. 130.1).
- Comparecencia personal y representación: lee el art. 197 completo. Anota cómo se entiende cumplida la comparecencia personal (presencial o electrónica) y qué formas de representación admite (apoderamiento notarial o apud acta, convenios de habilitación, Registro Electrónico de Colaboradores). Lee la nota que el conector devuelve sobre la nulidad del apartado 2 (obligación de relación electrónica): el fallo del Tribunal Supremo (`leer_boe`, `identificador="BOE-A-2026-19632"`) anula el art. 197.2 «en su integridad», así que la relación electrónica no es obligatoria por ese precepto (salvo para quien ya esté obligado por el art. 14.2 LPAC, como el abogado).
- Si presenta el abogado en ejercicio de su profesión, lee el art. 14.2 LPAC (obligación de relacionarse electrónicamente) y el art. 68.4 LPAC (subsanación electrónica y fecha de presentación).
- Lugares de presentación: art. 16.4 LPAC. Contenido mínimo de la solicitud: art. 66 LPAC.

### 4. Tasa y cita previa

- La tasa existe por el art. 44 LOEX y es requisito cuando lo diga la vía (por ejemplo, Reglamento 126.g); algunas vías son gratuitas (lee el art. 97.8 para familiares de españoles). **No escribas importes, modelos ni códigos**: la checklist dice «tasa: comprobar importe y modelo vigentes en la sede oficial y adjuntar justificante de pago».
- La cita previa no está en la norma: la checklist dice «cita previa o presentación electrónica: comprobar disponibilidad en la sede oficial» y remite a la forma de presentación del art. 197.

### 5. Subsanación y documentos que llegan tarde

- Plazo del requerimiento: el que fije el artículo de la vía (por ejemplo, el máximo del art. 130.3 o del art. 97.6) y, en su defecto, el art. 68.1 LPAC; ampliación del art. 68.2 LPAC cuando haya dificultad especial.
- Consecuencia de no atender: desistimiento y archivo (art. 130.3; art. 68.1 LPAC). La actuación se admite si llega antes o dentro del día en que se notifique la resolución que tenga por transcurrido el plazo (art. 73.3 LPAC).
- En vía de recurso no se valoran documentos que se pudieron aportar antes (art. 118.1 LPAC): por eso el expediente se presenta completo o se subsana en plazo.

### 6. Revisión de un expediente ya reunido

Recorre los documentos uno por uno y, para cada uno, comprueba y anota:

1. Que corresponde a una fila de la lista base (si no, «no exigido»: valora si aporta prueba útil).
2. Identidad coherente con el pasaporte: nombre, apellidos, transliteración, fecha y lugar de nacimiento.
3. Vigencia a la fecha prevista de presentación y fecha de expedición.
4. Firma de quien debe firmar; páginas completas; legibilidad.
5. Traducción completa (incluidos sellos y apostilla) y apostilla o legalización según el país.
6. Coherencia de fondo con el requisito (por ejemplo, jornada y salario del contrato frente al art. 127.b; periodo que cubre el padrón frente a la permanencia exigida).
7. Clasificación: **bloqueante** (sin él no se presenta), **subsanable** (se puede presentar y completar) o **correcto**.
8. Orden: numera los documentos en el mismo orden que la tabla y que el índice que acompañará a la solicitud.

### 7. Defectos que se repiten y que hay que buscar expresamente

- Copia solo de la página de datos del pasaporte cuando el artículo pide «copia completa».
- Pasaporte que caduca antes de la fecha prevista de presentación o, en visados de residencia, sin la vigencia mínima del art. 38.d.
- Certificado de antecedentes de un solo país cuando el cliente residió en otro durante los cinco años anteriores a la entrada.
- Traducción que omite la apostilla, los sellos o las notas marginales del original.
- Contrato firmado solo por el empleador, o con jornada o salario por debajo de lo que exige el artículo de la vía.
- Informe autonómico o municipal pedido tarde y sin justificante de la solicitud.
- Nombres transliterados de forma distinta en pasaporte, certificados y padrón, sin documento que explique la coincidencia.
- Justificante de tasa ausente o correspondiente a otro trámite.
- Representación no acreditada en alguna de las formas del art. 197.4 del Reglamento o del art. 5 LPAC.

## Estrategia y jurisprudencia

- Presenta completo: cada requerimiento abre un riesgo de desistimiento y retrasa la resolución.
- Pide primero lo que tarda (certificados de antecedentes extranjeros con su legalización o apostilla, informes autonómicos o municipales) y planifica con la fecha de expedición a la vista.
- Guarda y aporta los justificantes de haber pedido informes y certificados: sirven para acreditar el retraso de la Administración y para responder a un requerimiento.
- Consultas útiles (`base="AN"`, `jurisdiccion="CONTENCIOSO"`, `tipo_organo="TSJ"`, `provincia` del cliente si hay resultados). En `provincia` va la sede de la Sala del TSJ que conoce de la provincia del cliente, no la provincia misma cuando no coinciden (por ejemplo, para Almería, «Granada»; ocurre en las comunidades con varias sedes de Sala, como Andalucía, Canarias o Castilla y León): si la respuesta dice «Sin resultados en [provincia]», repite con la sede antes de caer al Supremo. Consultas de partida:
  - `consulta="requerimiento subsanación extranjería desistimiento archivo documentación aportada fuera de plazo"`.
  - `consulta="certificado antecedentes penales apostilla legalización denegación autorización residencia"`.
  - `consulta="arraigo acreditación permanencia empadronamiento cualquier medio de prueba"`.
  - `consulta="copia completa del pasaporte en vigor requerimiento autorización residencia"`.
- Usa la doctrina para advertir al cliente del riesgo de un documento dudoso, no para rellenar la checklist: la checklist se basa en los artículos leídos. Si la cita en una nota, párrafo literal con órgano, fecha y ECLI tal como los devolvió `leer_sentencias`.

## Documento que se entrega

**Checklist en Word** (formato de `references/formato-y-organos.md`, tablas en horizontal si no caben). Nombre: `checklist-<tramite>-<apellido-cliente>-<AAAAMMDD>.docx`.

Cita las normas en el documento como indica el apartado 4 de `references/formato-y-organos.md`, para que `verificar_escrito` las reconozca: «artículo N del Real Decreto 1155/2024» (nunca «del Reglamento de extranjería» ni «del Reglamento aprobado por…»), «artículo N de la Ley Orgánica 4/2000» y «Ley 14/2013, de 27 de septiembre». En esta skill, «Reglamento» es solo una abreviatura de trabajo del Real Decreto 1155/2024. Las letras van delante del número («letra c) del artículo 94.1 del Real Decreto 1155/2024»), nunca pegadas («94.1.c»). Cada cita lleva su norma aunque se repita: un «artículo 127» suelto después de citar el Código Civil o la Ley Orgánica 4/2000 lo comprueba `verificar_escrito` en esa otra norma. No cites artículos «del Real Decreto 316/2026»: `verificar_escrito` identifica ese número con otra norma; cita el artículo modificado del Real Decreto 1155/2024 y di que su redacción es la del Real Decreto 316/2026.

1. **Cabecera**: trámite y vía; órgano competente con su precepto; forma de presentación y quién presenta; fecha prevista de presentación.
2. **Tabla de documentos**: nº · documento · precepto que lo exige · requisitos formales (en vigor, fecha de expedición, apostilla o legalización, traducción) · estado (aportado, falta, defectuoso, no exigible) · acción correctora · responsable · fecha límite.
3. **Documentos que obtiene la Administración de oficio**: no se piden al cliente.
4. **Pruebas recomendadas**: no exigidas por el artículo, con el motivo.
5. **Tasa y cita previa**: sin importes ni códigos; «comprobar en la sede oficial».
6. **Bloqueantes y subsanables**: resumen en dos listas.
7. **Plazos**: subsanación y obligaciones posteriores a la concesión (alta en Seguridad Social y tarjeta), con precepto.
8. **Comprobaciones fuera del conector**: apostilla o legalización por país, clase de traducción, modelo oficial, tasa, cita previa.
9. **Normativa consultada**: artículo, norma y «vigente desde».

Para el cliente, añade una versión en lista simple («Traiga…») sin columnas técnicas.

## Comprobación final

- [ ] Puerta cumplida: `estado` respondió antes de empezar.
- [ ] Cada fila de la checklist tiene el artículo del que sale, leído con `buscar_articulo` en esta conversación, con su nota de nulidad o modificación si la hay.
- [ ] Vigencias comprobadas a la fecha prevista de presentación; ninguna vigencia inventada.
- [ ] Ni importes de tasas ni códigos de modelos; apostilla, traducción y cita previa remitidas a la sede o fuente oficial.
- [ ] Ningún ECLI sin leer con `leer_sentencias` o comprobar con `buscar_por_cita`.
- [ ] Marcadores en los datos del cliente que no se han facilitado.
- [ ] `verificar_escrito` pasado sobre el texto completo; cada aviso revisado uno a uno (un «no localizado» o una norma que no es la citada suele venir de una letra pegada al número o de un artículo sin su norma: corrige la forma de citar y vuelve a pasarlo).
- [ ] Resumen en el chat según el apartado 7 del formato: qué se ha preparado y para qué órgano, plazos con su precepto, documentos bloqueantes y riesgos, tabla de jurisprudencia citada (si la hay) y próximo paso (pedir los documentos que tardan o presentar).
