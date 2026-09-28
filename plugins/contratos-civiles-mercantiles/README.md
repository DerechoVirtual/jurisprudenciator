# Contratos Civiles y Mercantiles

Plugin de contratación civil y mercantil española para despachos de abogados. Redacta los contratos
más habituales del despacho, revisa los que llegan de la otra parte con un semáforo de riesgos,
prepara contrapropuestas y lleva el incumplimiento hasta la puerta del juzgado: requerimiento,
resolución, vicios ocultos, reclamación de la deuda con monitorio y el intento de negociación previo
que exige la Ley Orgánica 1/2025. Conforme al Código Civil, el Código de Comercio, la Ley de
Arrendamientos Urbanos (tras la Ley 12/2023), la Ley de Sociedades de Capital y la normativa de
consumidores.

## Primer uso: tu estilo

La primera vez que el plugin vaya a redactar, te pedirá entre 3 y 5 escritos tuyos de referencia y aprenderá tu forma de escribir: fórmulas, estructura, tono, forma de citar y maquetación. El perfil se guarda una sola vez y lo usan todos los plugins de Jurisprudenciator. Puedes actualizarlo cuando quieras con la skill `perfil-de-estilo`.

## Conector principal: Jurisprudenciator

**¿Ya tienes Jurisprudenciator en Claude?** Lo normal es tenerlo conectado con tu URL personal
(https://jurisprudenciator.lexiaipro.org/instalacion): las skills usan ese. Si no, conecta el que trae
el plugin e inicia sesión con tu cuenta.

Cada skill saca de Jurisprudenciator el texto vigente de cada artículo, la jurisprudencia de la Sala
Primera del Tribunal Supremo, de las Audiencias Provinciales y del TJUE con su párrafo literal y su
ECLI, los datos del Registro Mercantil de las sociedades que firman y los datos catastrales de los
inmuebles, y revisa las citas antes de entregar el documento. Cada contrato va con una nota para el
abogado que justifica sus cláusulas críticas.

**Sin Jurisprudenciator no se trabaja.** Cada skill empieza comprobando el conector (`estado`) y saca
de él todos los datos jurídicos. Si no está conectado, falla o no devuelve lo que la tarea necesita,
la skill se detiene y pide conectarlo: nunca sigue de memoria ni con citas pendientes.

**Conectores del despacho (opcionales).** El plugin trae también Google Drive, Gmail, Google Calendar,
Microsoft 365 (Outlook, OneDrive, SharePoint), Dropbox, Box y DocuSign. Conecta solo los que uses; en la
app de Claude están en la pestaña Conectores del plugin.

## Instalación

En la app de Claude: *Personalizar → Plugins → Añadir marketplace*, pega
https://github.com/DerechoVirtual/jurisprudenciator e instala **Contratos Civiles y Mercantiles**.

## Skills

| Bloque | Skills |
|---|---|
| Entrada y control | `contratos-intake`, `verificacion-partes-contrato`, `revision-contrato-semaforo`, `negociacion-contrapropuesta`, `condiciones-generales-consumidores`, `dictamen-interpretacion-contrato`, `modificacion-novacion-cesion` |
| Inmuebles | `contrato-arras`, `compraventa-inmueble`, `arrendamiento-vivienda`, `arrendamiento-local-negocio` |
| Comercio y servicios | `compraventa-mercantil`, `prestacion-servicios`, `contrato-obra`, `agencia-distribucion-franquicia`, `prestamo-reconocimiento-deuda` |
| Sociedades, propiedad intelectual y datos | `pacto-de-socios`, `compraventa-participaciones`, `confidencialidad-nda`, `licencia-cesion-propiedad-intelectual`, `encargo-tratamiento-datos` |
| Incumplimiento | `requerimiento-cumplimiento`, `resolucion-por-incumplimiento`, `vicios-ocultos-saneamiento`, `reclamacion-deuda-monitorio`, `masc-propuesta-acuerdo` |

Empieza por `contratos-intake`: identifica qué necesita el cliente y te lleva a la skill que toca.

## Qué datos envía

El plugin no ejecuta programas en tu equipo. Las consultas jurídicas se envían al conector de
Jurisprudenciator (`https://mcp.jurisprudenciator.lexiaipro.org/mcp`) con tu cuenta. Busca siempre por
la cuestión jurídica, nunca por el nombre o el DNI de un particular (sí por el nombre o el CIF de una
sociedad en el Registro Mercantil). Los conectores opcionales solo se usan si los conectas tú, con tu
cuenta de cada servicio. Lo que redacta Claude son borradores para revisión del abogado; no es
asesoramiento jurídico.

## Ejemplos para la revisión

Usar datos ficticios y una cuenta de Jurisprudenciator autorizada. No utilizar expedientes reales para pruebas.

1. Prepara un contrato de arras penitenciales para la compra de una vivienda ficticia en Madrid, con la nota que justifique la calificación de las arras.
2. Revisa con semáforo un contrato de distribución exclusiva ficticio desde la posición del distribuidor.
3. Prepara el requerimiento de pago y la petición de monitorio por una factura comercial impagada ficticia, con los intereses de demora calculados.

## Resolución de problemas

Si no aparecen las herramientas, conecta Jurisprudenciator en Claude y comprueba `estado`. Si la cuenta no tiene acceso o ha agotado su cuota, revisa su estado en la web. Si falta una fuente imprescindible, la skill se detiene: no se completa con citas inventadas. Los conectores del despacho son opcionales. Para un problema persistente, usa [Soporte](https://jurisprudenciator.lexiaipro.org/incidencias), indicando el plugin y el error sin adjuntar credenciales ni datos de clientes.

[Privacidad de este plugin](PRIVACY.md): datos tratados, conectores opcionales y conservación.
