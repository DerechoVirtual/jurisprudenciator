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
