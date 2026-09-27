# Extranjería España

Plugin de Derecho de extranjería español para despachos de abogados. Prepara, con las normas
vigentes y jurisprudencia real, las solicitudes, memorias, alegaciones y recursos de un despacho de
extranjería: arraigos, reagrupación familiar, residencia y trabajo, familiares de españoles y de
ciudadanos de la Unión, estudiantes, movilidad internacional, larga duración, nacionalidad,
protección internacional, víctimas, menores, expulsiones, internamiento en CIE y recursos
administrativos y contencioso-administrativos. Conforme al Reglamento aprobado por el Real Decreto
1155/2024 (vigente desde el 20 de mayo de 2025) y a la Ley Orgánica 4/2000.

## Primer uso: tu estilo

La primera vez que el plugin vaya a redactar, te pedirá entre 3 y 5 escritos tuyos de referencia y aprenderá tu forma de escribir: fórmulas, estructura, tono, forma de citar y maquetación. El perfil se guarda una sola vez y lo usan todos los plugins de Jurisprudenciator. Puedes actualizarlo cuando quieras con la skill `perfil-de-estilo`.

## Conector principal: Jurisprudenciator

**¿Ya tienes Jurisprudenciator en Claude?** Lo normal es tenerlo conectado con tu URL personal
(https://jurisprudenciator.lexiaipro.org/instalacion): las skills usan ese. Si no, conecta el que trae
el plugin e inicia sesión con tu cuenta.

Cada skill saca de Jurisprudenciator el texto vigente de cada artículo (Ley Orgánica 4/2000,
Reglamento, Código Civil, Ley 12/2009, normas de la Unión) y la jurisprudencia de los TSJ, la
Audiencia Nacional, el Tribunal Supremo, el Tribunal Constitucional y el TJUE con su párrafo literal y
su ECLI, y revisa las citas del escrito antes de entregarlo.

**Sin Jurisprudenciator no se trabaja.** Cada skill empieza comprobando el conector (`estado`) y saca
de él todos los datos jurídicos. Si no está conectado, falla o no devuelve lo que la tarea necesita,
la skill se detiene y pide conectarlo: nunca sigue de memoria ni con citas pendientes.

**Conectores del despacho (opcionales).** El plugin trae también Google Drive, Gmail, Google Calendar,
Microsoft 365 (Outlook, OneDrive, SharePoint), Dropbox, Box y DocuSign. Conecta solo los que uses; en la
app de Claude están en la pestaña Conectores del plugin.

## Instalación

En la app de Claude: *Personalizar → Plugins → Añadir marketplace*, pega
https://github.com/DerechoVirtual/jurisprudenciator e instala **Extranjería España**.

## Skills

| Bloque | Skills |
|---|---|
| Entrada del caso | `extranjeria-intake`, `informe-viabilidad-extranjeria`, `documentacion-expediente` |
| Arraigo | `arraigo-social`, `arraigo-sociolaboral`, `arraigo-socioformativo`, `arraigo-familiar`, `arraigo-segunda-oportunidad` |
| Circunstancias excepcionales y víctimas | `razones-humanitarias`, `victimas-violencia-genero-sexual`, `victimas-trata`, `menores-extranjeros` |
| Residencia y trabajo | `residencia-no-lucrativa`, `reagrupacion-familiar`, `trabajo-cuenta-ajena`, `trabajo-cuenta-propia`, `movilidad-internacional-ley-14-2013` |
| Familias, estudios y larga duración | `familiares-de-espanoles`, `ciudadanos-ue-y-familiares`, `estudiantes-y-busqueda-empleo`, `larga-duracion`, `renovacion-modificacion-extincion` |
| Nacionalidad, asilo y visados | `nacionalidad-residencia`, `nacionalidad-otras-vias`, `proteccion-internacional-apatridia`, `visados-denegacion` |
| Expulsión y frontera | `expulsion-procedimiento-sancionador`, `internamiento-cie`, `denegacion-entrada-devolucion`, `prohibicion-entrada-antecedentes` |
| Recursos | `recurso-administrativo-extranjeria`, `recurso-contencioso-extranjeria` |

Empieza por `extranjeria-intake`: reúne los datos del caso, detecta urgencias y te lleva a la skill
que toca.

## Qué datos envía

El plugin no ejecuta programas en tu equipo. Las consultas jurídicas se envían al conector de
Jurisprudenciator (`https://mcp.jurisprudenciator.lexiaipro.org/mcp`) con tu cuenta. Busca siempre por
la cuestión jurídica, nunca por el nombre, el NIE o el pasaporte del cliente. Los conectores opcionales
solo se usan si los conectas tú, con tu cuenta de cada servicio. Lo que redacta Claude son borradores
para revisión del abogado; no es asesoramiento jurídico.
