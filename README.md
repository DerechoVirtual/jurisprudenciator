# Jurisprudenciator para Claude

Plugins de Jurisprudenciator para la app de Claude (chat y Cowork): el conector de jurisprudencia y
legislación española y un plugin por orden jurisdiccional (civil, penal, contencioso-administrativo y
laboral) y otro de extranjería. Cada skill consulta Jurisprudenciator antes de escribir una cita: sentencias con su párrafo
literal y su ECLI, artículos vigentes, verificación de citas, Catastro, Registro Mercantil, convenios
colectivos, doctrina del TEAC y ordenanzas municipales. Si Jurisprudenciator no responde, la skill se
detiene: nunca cita de memoria.

## Instalación en la app de Claude

1. Abre **Personalizar → Plugins → Añadir marketplace**.
2. Pega esta dirección:

   ```
   https://github.com/DerechoVirtual/jurisprudenciator
   ```

3. Instala **Jurisprudenciator** y los plugins de las materias en las que trabajes: civil, penal,
   contencioso-administrativo, laboral o extranjería.
4. Si ya tienes Jurisprudenciator conectado en Claude con tu URL personal, no hace falta nada más. Si
   no, en la pestaña **Conectores** del plugin conecta Jurisprudenciator e inicia sesión con tu cuenta
   (gratis en https://jurisprudenciator.lexiaipro.org).

En esa misma pestaña puedes conectar, si los usas, Google Drive, Gmail, Google Calendar,
Microsoft 365 (Outlook, OneDrive, SharePoint), Dropbox, Box y DocuSign.

## Primer uso: tu estilo

La primera vez que un plugin vaya a redactar, te pedirá entre 3 y 5 escritos tuyos de referencia y
aprenderá tu forma de escribir (skill `perfil-de-estilo`). El perfil se guarda una vez y lo usan todos.

## Plugins

| Plugin | Qué trae |
|---|---|
| `jurisprudenciator` | El conector y la guía de sus herramientas. |
| `litigacion-civil-espana` | Civil, mercantil y familia (LEC, LO 1/2025). |
| `litigacion-penal-espana` | Penal (LECrim, CP). |
| `litigacion-contencioso-espana` | Contencioso-administrativo (LJCA, Leyes 39 y 40/2015). |
| `litigacion-laboral-espana` | Laboral y Seguridad Social (LRJS, ET, LGSS). |
| `extranjeria-espana` | Extranjería: arraigos, reagrupación, residencia y trabajo, nacionalidad, asilo, expulsiones y recursos (LO 4/2000 y RD 1155/2024). |

## Qué datos envía

Los plugins no ejecutan programas en tu equipo. Las consultas jurídicas se envían al conector de
Jurisprudenciator (`https://mcp.jurisprudenciator.lexiaipro.org/mcp`) con tu cuenta. Los conectores
opcionales solo se usan si los conectas tú, con tu cuenta de cada servicio. Lo que redacta Claude son
borradores para revisión del abogado; no es asesoramiento jurídico.

© Derecho Virtual, S.L. Todos los derechos reservados. Ver `LICENSE`.
