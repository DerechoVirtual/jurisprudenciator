# Litigación civil España

Plugin de litigación civil, mercantil y de familia para despachos de abogados en España (LO 1/2025, LEC vigente, EGA). Gestiona la cartera de asuntos y redacta los escritos del proceso civil apoyándose en el conector **Jurisprudenciator** para la jurisprudencia, la legislación vigente, la verificación de citas, el Catastro y el Registro Mercantil.

## Primer uso: tu estilo

La primera vez que el plugin vaya a redactar, te pedirá entre 3 y 5 escritos tuyos de referencia y aprenderá tu forma de escribir: fórmulas, estructura, tono, forma de citar y maquetación. El perfil se guarda una sola vez y lo usan todos los plugins de Jurisprudenciator. Puedes actualizarlo cuando quieras con la skill `perfil-de-estilo`.

## Conector principal: Jurisprudenciator

**¿Ya tienes Jurisprudenciator en Claude?** Lo normal es tenerlo conectado con tu URL personal (https://jurisprudenciator.lexiaipro.org/instalacion): las skills usan ese. Si no, conecta el que trae el plugin e inicia sesión con tu cuenta. Endpoint del plugin: `https://mcp.jurisprudenciator.lexiaipro.org/mcp`.

- **Jurisprudencia oficial** del Tribunal Supremo, la Audiencia Nacional, los TSJ, las Audiencias Provinciales y los juzgados, además del Tribunal Constitucional y del TJUE, con el párrafo literal para citar y su ECLI o ROJ.
- **Artículos vigentes** de leyes españolas y normas de la UE (LEC, CC, LAU, LPH, LSC, TRLGDCU, LO 1/2025, Directiva 93/13/CEE...) y **verificación de las citas** de un borrador antes de presentarlo.
- **BOE y BORME**, **Registro Mercantil** (estado, domicilio y administradores de una sociedad), **Catastro**, criterio de **Hacienda y del TEAC**, **ordenanzas municipales** y **convenios colectivos**.

Cada skill explica, en su apartado «Jurisprudenciator en esta skill», qué dato sale de qué herramienta.

**Sin Jurisprudenciator no se trabaja.** Cada skill empieza comprobando el conector (`estado`) y saca de él todos los datos jurídicos. Si no está conectado, falla o no devuelve lo que la tarea necesita (sentencias, el artículo, el convenio...), la skill se detiene y pide conectarlo: nunca sigue de memoria ni con citas pendientes.

## Documentación del despacho

**Conectores del despacho (opcionales).** El plugin trae también Google Drive, Gmail, Google Calendar, Microsoft 365 (Outlook, OneDrive, SharePoint), Dropbox, Box y DocuSign. Conecta solo los que uses; en la app de Claude están en la pestaña Conectores del plugin. Sirven para los documentos, el correo, los señalamientos y la firma, nunca como fuente de jurisprudencia o legislación. Los asuntos pueden guardarse en una carpeta local o en cualquiera de esos servicios. Se indica en `/cold-start-interview` y se cambia con `/customize`.

## Instalación

Añade el marketplace de Jurisprudenciator: https://jurisprudenciator.lexiaipro.org/plugins

- En Claude Code:

  ```
  claude plugin marketplace add https://jurisprudenciator.lexiaipro.org/plugins
  claude plugin install litigacion-civil-espana@jurisprudenciator
  ```

- En la app: `+` → «Añadir plugins...» → pega la URL del marketplace y elige **litigacion-civil-espana**.

Después, configura el despacho con `/cold-start-interview`.

## Skills

Incluye las skills de cartera de asuntos y de redacción de escritos: intake y briefing de asuntos, demandas, contestaciones, recursos (reposición, apelación, casación y queja), ejecución y oposición a la ejecución, declinatoria, medidas cautelares, nulidad de cláusulas abusivas, conclusiones y prueba, incidente de nulidad, terminación anticipada, MASC, cronologías, cuadros de elementos, interrogatorios, tasaciones de costas, burofax, hoja de encargo y más. La configuración del despacho se hace con `/cold-start-interview` y `/customize`.

## Perfil y privacidad

El `CLAUDE.md` incluido es una plantilla vacía: no se carga automáticamente como contexto. La skill `/cold-start-interview` lo lee para crear un perfil privado y `/customize` permite modificarlo. No guardes datos reales del despacho o de clientes en el repositorio público.

Los conectores de documentos, correo, calendario y firma son opcionales y requieren la autorización del usuario. Gmail y Google Calendar se seleccionan entre los conectores nativos de Claude; sus entradas no anuncian una URL MCP pública.

[Política de privacidad](https://jurisprudenciator.lexiaipro.org/politica-de-privacidad) · [Soporte](https://jurisprudenciator.lexiaipro.org/incidencias) · [Términos del servicio](https://jurisprudenciator.lexiaipro.org/terminos-y-condiciones)

## Ejemplos para la revisión

Usar datos ficticios y una cuenta de Jurisprudenciator autorizada. No utilizar expedientes reales para pruebas.

1. Configura el plugin para un despacho civil ficticio y comprueba la conexión con Jurisprudenciator.
2. Prepara un borrador de demanda de reclamación de cantidad: factura ficticia de 3.000 euros impagada. Pregunta los hechos y documentos que falten y verifica las citas.
3. Revisa las citas de este borrador civil de ejemplo con Jurisprudenciator e identifica lo que no se puede verificar.

## Resolución de problemas

Si no aparecen las herramientas, conecta Jurisprudenciator en Claude y comprueba `estado`. Si la cuenta no tiene acceso o ha agotado su cuota, revisa su estado en la web. Si falta una fuente imprescindible, la skill se detiene: no se completa con citas inventadas. Los conectores del despacho son opcionales. Para un problema persistente, usa [Soporte](https://jurisprudenciator.lexiaipro.org/incidencias), indicando el plugin y el error sin adjuntar credenciales ni datos de clientes.

[Privacidad de este plugin](PRIVACY.md): datos tratados, conectores opcionales y conservación.
