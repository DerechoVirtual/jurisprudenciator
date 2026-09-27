# Jurisprudenciator

El conector Jurisprudenciator para Claude y la guía de sus herramientas: jurisprudencia oficial española
(Tribunal Supremo, Audiencia Nacional, TSJ, Audiencias Provinciales, juzgados, Tribunal Constitucional y
TJUE) con su párrafo literal y su ECLI, texto vigente de cualquier artículo, verificación de las citas de
un escrito, BOE y BORME, Registro Mercantil, doctrina de Hacienda y del TEAC, ordenanzas municipales,
Catastro y convenios colectivos. La skill `jurisprudenciator` explica qué herramienta usar para cada
cosa y detiene el trabajo si el conector no responde: nunca se cita de memoria.

## Primer uso: tu estilo

La primera vez que se vaya a redactar, Claude te pedirá entre 3 y 5 escritos tuyos de referencia y
aprenderá tu forma de escribir con la skill `perfil-de-estilo`. El perfil lo usan todos los plugins de
Jurisprudenciator.

## Conectores

Si ya tienes Jurisprudenciator conectado en Claude con tu URL personal
(https://jurisprudenciator.lexiaipro.org/instalacion), se usa ese; si no, conecta el que trae el plugin e
inicia sesión con tu cuenta. El plugin trae también, opcionales, Google Drive, Gmail, Google Calendar,
Microsoft 365, Dropbox, Box y DocuSign.

## Qué datos envía

Las consultas jurídicas se envían al conector de Jurisprudenciator
(`https://mcp.jurisprudenciator.lexiaipro.org/mcp`) con tu cuenta. Busca por la cuestión jurídica, nunca
por los datos personales del cliente. Los conectores opcionales solo se usan si los conectas tú.

## Ejemplos para la revisión

Usar datos ficticios y una cuenta de Jurisprudenciator autorizada. No utilizar expedientes reales para pruebas.

1. Comprueba que Jurisprudenciator responde y explícame qué herramientas tengo.
2. Busca jurisprudencia del Tribunal Supremo sobre la cláusula de gastos hipotecarios y cítame el párrafo clave con su ECLI.
3. ¿Qué dice hoy el artículo 394 de la Ley de Enjuiciamiento Civil?

## Resolución de problemas

Si no aparecen las herramientas, conecta Jurisprudenciator en Claude y comprueba `estado`. Si la cuenta no tiene acceso o ha agotado su cuota, revisa su estado en la web. Si falta una fuente imprescindible, la skill se detiene: no se completa con citas inventadas. Los conectores del despacho son opcionales. Para un problema persistente, usa [Soporte](https://jurisprudenciator.lexiaipro.org/incidencias), indicando el plugin y el error sin adjuntar credenciales ni datos de clientes.

[Privacidad de este plugin](PRIVACY.md): datos tratados, conectores opcionales y conservación.
