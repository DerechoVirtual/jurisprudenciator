# Contratos Laborales y Asesoría Empresarial

Plugin de asesoría laboral de empresa y de despidos para despachos de abogados y graduados sociales.
Prepara lo que la empresa necesita en el día a día (contratos de trabajo tras la reforma de 2021,
pactos, teletrabajo, alta dirección, modificaciones y traslados, permisos, registro de jornada,
sanciones, ERTE, sucesión de empresa, planes de igualdad, protocolo de acoso, canal de denuncias,
Inspección de Trabajo) y la extinción del contrato (cartas de despido con audiencia previa, finiquitos
y cálculo de indemnizaciones). Trae también el laboral de siempre: papeleta de conciliación, demanda de
despido, reclamación de cantidad, extinción a instancia del trabajador y tutela de derechos
fundamentales. Conforme al Estatuto de los Trabajadores, la Ley Reguladora de la Jurisdicción Social y
los convenios colectivos vigentes.

## Primer uso: tu estilo

La primera vez que el plugin vaya a redactar, te pedirá entre 3 y 5 escritos tuyos de referencia y aprenderá tu forma de escribir: fórmulas, estructura, tono, forma de citar y maquetación. El perfil se guarda una sola vez y lo usan todos los plugins de Jurisprudenciator. Puedes actualizarlo cuando quieras con la skill `perfil-de-estilo`.

## Conector principal: Jurisprudenciator

**¿Ya tienes Jurisprudenciator en Claude?** Lo normal es tenerlo conectado con tu URL personal
(https://jurisprudenciator.lexiaipro.org/instalacion): las skills usan ese. Si no, conecta el que trae
el plugin e inicia sesión con tu cuenta.

Cada skill saca de Jurisprudenciator el texto vigente de cada artículo, el convenio colectivo aplicable
y sus artículos, la jurisprudencia de la Sala Cuarta del Tribunal Supremo, de los TSJ, del Tribunal
Constitucional y del TJUE con su párrafo literal y su ECLI, y los datos registrales de la empresa, y
revisa las citas antes de entregar el documento.

**Sin Jurisprudenciator no se trabaja.** Cada skill empieza comprobando el conector (`estado`) y saca
de él todos los datos jurídicos. Si no está conectado, falla o no devuelve lo que la tarea necesita,
la skill se detiene y pide conectarlo: nunca sigue de memoria ni con citas pendientes.

**Conectores del despacho (opcionales).** El plugin trae también Google Drive, Gmail, Google Calendar,
Microsoft 365 (Outlook, OneDrive, SharePoint), Dropbox, Box y DocuSign. Conecta solo los que uses; en la
app de Claude están en la pestaña Conectores del plugin.

## Instalación

En la app de Claude: *Personalizar → Plugins → Añadir marketplace*, pega
https://github.com/DerechoVirtual/jurisprudenciator e instala **Contratos Laborales y Asesoría
Empresarial**.

## Skills

| Bloque | Skills |
|---|---|
| Entrada y cálculos | `laboral-empresa-intake`, `convenio-aplicable`, `calculo-indemnizacion-despido`, `finiquito-liquidacion` |
| Contratación | `contrato-trabajo-modalidad`, `periodo-prueba`, `pactos-contrato-trabajo`, `teletrabajo-acuerdo`, `alta-direccion`, `falso-autonomo-trade` |
| Gestión de la relación | `modificacion-sustancial-condiciones`, `movilidad-geografica-funcional`, `permisos-conciliacion-adaptacion`, `registro-jornada-horas-extra`, `sanciones-disciplinarias`, `erte-suspension-reduccion`, `sucesion-empresa-contratas` |
| Cumplimiento | `plan-igualdad-registro-retributivo`, `protocolo-acoso-laboral`, `canal-denuncias-informantes`, `inspeccion-trabajo-alegaciones` |
| Extinción (empresa) | `carta-despido-disciplinario`, `carta-despido-objetivo`, `despido-colectivo-empresa` |
| Despidos y reclamaciones | `papeleta-conciliacion`, `redactar-demanda-despido`, `reclamacion-cantidad`, `extincion-contrato-trabajador`, `tutela-derechos-fundamentales` |

Empieza por `laboral-empresa-intake`: identifica si defiendes a la empresa o al trabajador, calcula los
plazos que ya corren y te lleva a la skill que toca.

## Qué datos envía

El plugin no ejecuta programas en tu equipo. Las consultas jurídicas se envían al conector de
Jurisprudenciator (`https://mcp.jurisprudenciator.lexiaipro.org/mcp`) con tu cuenta. Busca siempre por
la cuestión jurídica, nunca por el nombre o el DNI del trabajador (sí por el nombre o el CIF de la
empresa en el Registro Mercantil). Los conectores opcionales solo se usan si los conectas tú, con tu
cuenta de cada servicio. Lo que redacta Claude son borradores para revisión del abogado; no es
asesoramiento jurídico.

## Ejemplos para la revisión

Usar datos ficticios y una cuenta de Jurisprudenciator autorizada. No utilizar expedientes reales para pruebas.

1. Prepara la carta de despido disciplinario de un trabajador ficticio de hostelería en Madrid por ausencias injustificadas, con la comunicación de audiencia previa.
2. Calcula la indemnización por despido improcedente de un trabajador ficticio con antigüedad anterior a 2012.
3. Prepara la papeleta de conciliación y la demanda de despido nulo de una trabajadora ficticia despedida durante el embarazo.

## Resolución de problemas

Si no aparecen las herramientas, conecta Jurisprudenciator en Claude y comprueba `estado`. Si la cuenta no tiene acceso o ha agotado su cuota, revisa su estado en la web. Si falta una fuente imprescindible, la skill se detiene: no se completa con citas inventadas. Las tablas salariales de los convenios hay que aportarlas: el conector no las devuelve de forma fiable. Los conectores del despacho son opcionales. Para un problema persistente, usa [Soporte](https://jurisprudenciator.lexiaipro.org/incidencias), indicando el plugin y el error sin adjuntar credenciales ni datos de clientes.

[Privacidad de este plugin](PRIVACY.md): datos tratados, conectores opcionales y conservación.
