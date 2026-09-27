# Litigación laboral España

Plugin de litigación laboral y de Seguridad Social para despachos de abogados en España
(LRJS - Ley 36/2011, ET, normativa de Seguridad Social). Todas sus skills se apoyan en el
conector **Jurisprudenciator**, que viene incluido en el plugin.

## Primer uso: tu estilo

La primera vez que el plugin vaya a redactar, te pedirá entre 3 y 5 escritos tuyos de referencia y aprenderá tu forma de escribir: fórmulas, estructura, tono, forma de citar y maquetación. El perfil se guarda una sola vez y lo usan todos los plugins de Jurisprudenciator. Puedes actualizarlo cuando quieras con la skill `perfil-de-estilo`.

## Conector incluido (`.mcp.json`)

- **Jurisprudenciator** (conector remoto) — fuentes oficiales para el despacho. **¿Ya tienes Jurisprudenciator en Claude?** Lo normal es tenerlo conectado con tu URL personal (https://jurisprudenciator.lexiaipro.org/instalacion): las skills usan ese. Si no, conecta el que trae el plugin e inicia sesión con tu cuenta.
  Endpoint: `https://mcp.jurisprudenciator.lexiaipro.org/mcp`
  - Jurisprudencia oficial (Sala Cuarta del TS, Salas de lo Social de la AN y de los TSJ,
    juzgados de lo social, TC y TJUE) con párrafo literal y ECLI: `buscar_sentencias`,
    `opciones_busqueda`, `buscar_por_cita`, `leer_sentencias`, `continuar_lectura`.
  - Legislación vigente y verificación de citas: `buscar_articulo`, `verificar_escrito`.
  - Convenios colectivos (salarios, categorías, jornada, pluses, vigencia): `buscar_convenio`,
    `leer_convenio`, `vigencia_convenio`.
  - Registro Mercantil, BOE y BORME (empresa demandada, concurso, edictos):
    `buscar_empresa_mercantil`, `buscar_boe`, `leer_boe`, `sumario_boe`, `novedades_boe`,
    `sumario_borme`.
  - Además: criterios de Hacienda y doctrina del TEAC, ordenanzas municipales, Catastro, guías
    de redacción (`escritos_disponibles`, `guia_escrito`) y diagnóstico (`estado`).

**Sin Jurisprudenciator no se trabaja.** Cada skill empieza comprobando el conector (`estado`) y saca de él todos los datos jurídicos. Si no está conectado, falla o no devuelve lo que la tarea necesita (sentencias, el artículo, el convenio...), la skill se detiene y pide conectarlo: nunca sigue de memoria ni con citas pendientes.

**Conectores del despacho (opcionales).** El plugin trae también Google Drive, Gmail, Google Calendar, Microsoft 365 (Outlook, OneDrive, SharePoint), Dropbox, Box y DocuSign. Conecta solo los que uses; en la app de Claude están en la pestaña Conectores del plugin. Sirven para los documentos, el correo, los señalamientos y la firma, nunca como fuente de jurisprudencia o legislación.

## Skills

### Requisitos de procedibilidad

- `/papeleta-conciliacion` — papeleta de conciliación/mediación previa (SMAC, arts. 63-68 LRJS).
- `/reclamacion-previa-seguridad-social` — reclamación previa frente al INSS/TGSS/mutua
  (art. 71 LRJS).

### Demandas (basadas en plantillas reales del despacho, anonimizadas)

- `/redactar-demanda-despido` — demanda por despido disciplinario/objetivo/nulo/improcedente.
- `/reclamacion-cantidad` — reclamación de salarios, extras, finiquito y otras cantidades
  (con FOGASA cuando procede).
- `/extincion-contrato-trabajador` — extinción del contrato a instancia del trabajador
  (art. 50 ET), incluido acoso laboral/mobbing.
- `/reclamacion-trade` — resolución de contrato TRADE y reclamación de cantidad.
- `/incapacidad-permanente` — demanda de incapacidad permanente (total/absoluta/gran
  invalidez) frente al INSS.
- `/seguridad-social-contingencia` — determinación de contingencia (accidente de
  trabajo/enfermedad profesional vs. común), incluido burnout.

### Procedimientos especiales

- `/tutela-derechos-fundamentales` — tutela de derechos fundamentales y libertades
  públicas (arts. 177-184 LRJS).
- `/conflicto-colectivo` — proceso de conflicto colectivo (arts. 153-162 LRJS).
- `/impugnacion-despido-colectivo` — impugnación colectiva e individual del despido
  colectivo (art. 124 LRJS).

### Recursos y ejecución

- `/recurso-suplicacion` — recurso de suplicación ante la Sala de lo Social del TSJ.
- `/recurso-casacion-unificacion-doctrina` — RCUD ante el Tribunal Supremo (con el
  requisito de interés casacional objetivo introducido por la LO 1/2025).
- `/ejecucion-laboral` — ejecución dineraria, ejecución de sentencias de despido
  (incidente de no readmisión) y ejecución provisional.

### Gestión del asunto y transversales (adaptadas al orden social)

`asunto-intake`, `cold-start-interview`, `briefing-asunto`, `actualizar-asunto`,
`cerrar-asunto`, `portfolio-status`, `matter-workspace`, `colaboradores-status`,
`hoja-encargo`, `customize`, `estilo-escritos-judiciales`, `subsuncion-juridica`,
`cronologia`, `cuadro-elementos`, `preparacion-interrogatorio`, `conservacion-documental`,
`redactor-escrito-seccion`, `revision-secreto-profesional`, `requerimiento-judicial-triage`.

La configuración del despacho se hace con `/cold-start-interview` y `/customize`.

## Marco normativo

Todas las skills citan la LRJS en su redacción vigente (incluidas las reformas del
RD-ley 6/2023 y de la LO 1/2025: Tribunales de Instancia con Sección de lo Social,
interés casacional objetivo en el RCUD, redacción actual del art. 65 sobre suspensión
de caducidad). El requisito MASC de la LO 1/2025 rige en el orden civil, **no** en el
social: aquí la procedibilidad se cumple con conciliación previa (SMAC) o reclamación
previa de Seguridad Social.

## Aviso sobre datos sensibles

Varias skills (incapacidad permanente, determinación de contingencia, reclamación previa
de Seguridad Social) tratan datos de salud, categoría especial de datos personales.
Estas skills incluyen avisos explícitos para no reproducir diagnósticos ni datos
identificativos reales de terceros en ningún ejemplo o plantilla.

## Pendiente / próximos pasos

Posibles ampliaciones futuras: modalidades de vacaciones y materia electoral,
clasificación profesional, movilidad geográfica y modificación sustancial (arts. 137-138
LRJS como skills propias), demandas de prestaciones distintas a incapacidad (jubilación,
viudedad), impugnación de sanciones (arts. 114-115 LRJS) y procedimiento de oficio.

## Instalación

Añade el marketplace de Jurisprudenciator: https://jurisprudenciator.lexiaipro.org/plugins

- En Claude Code: `/plugin marketplace add https://jurisprudenciator.lexiaipro.org/plugins`
  y después `/plugin install litigacion-laboral-espana@jurisprudenciator`.
- En la app de Claude: añade el marketplace con esa misma dirección desde la gestión de plugins
  e instala «litigacion-laboral-espana».

Ver `COMO-PROBARLO.md` para el plan de pruebas completo.

## Perfil y privacidad

El `CLAUDE.md` incluido es una plantilla vacía: no se carga automáticamente como contexto. La skill `/cold-start-interview` lo lee para crear un perfil privado y `/customize` permite modificarlo. No guardes datos reales del despacho o de clientes en el repositorio público.

Los conectores de documentos, correo, calendario y firma son opcionales y requieren la autorización del usuario. Gmail y Google Calendar se seleccionan entre los conectores nativos de Claude; sus entradas no anuncian una URL MCP pública.

[Política de privacidad](https://jurisprudenciator.lexiaipro.org/politica-de-privacidad) · [Soporte](https://jurisprudenciator.lexiaipro.org/incidencias) · [Términos del servicio](https://jurisprudenciator.lexiaipro.org/terminos-y-condiciones)

## Ejemplos para la revisión

Usar datos ficticios y una cuenta de Jurisprudenciator autorizada. No utilizar expedientes reales para pruebas.

1. Configura un despacho laboral ficticio y comprueba Jurisprudenciator.
2. Prepara una papeleta de conciliación por un despido disciplinario ficticio; pide fecha, salario, antigüedad y carta antes de calcular o redactar.
3. Localiza y verifica el convenio colectivo aplicable a un caso ficticio, preguntando actividad y territorio.

## Resolución de problemas

Si no aparecen las herramientas, conecta Jurisprudenciator en Claude y comprueba `estado`. Si la cuenta no tiene acceso o ha agotado su cuota, revisa su estado en la web. Si falta una fuente imprescindible, la skill se detiene: no se completa con citas inventadas. Los conectores del despacho son opcionales. Para un problema persistente, usa [Soporte](https://jurisprudenciator.lexiaipro.org/incidencias), indicando el plugin y el error sin adjuntar credenciales ni datos de clientes.

[Privacidad de este plugin](PRIVACY.md): datos tratados, conectores opcionales y conservación.
