---
name: perfil-de-estilo
description: Aprende la forma de escribir del abogado a partir de 3 a 5 escritos suyos y guarda un perfil de estilo que usan todas las skills de redacción de los plugins de Jurisprudenciator. Se ejecuta la primera vez que se usa cualquiera de estos plugins (cuando aún no hay perfil) y cuando el abogado dice «aquí tienes mis modelos», «escribe como yo», «adapta el estilo a mis escritos» o «actualiza mi estilo».
---

# Perfil de estilo del despacho

Convierte 3 a 5 escritos reales del abogado en un perfil que las demás skills siguen al redactar:
sus fórmulas, su estructura, su tono y su forma de citar. Hay un único perfil para todos los plugins de
Jurisprudenciator: se hace una vez y sirve para civil, penal, contencioso, laboral, extranjería y los
que se añadan.

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias.

- **Citas legales de cada modelo** → `verificar_escrito` con el texto de cada escrito: detecta artículos derogados, inexistentes o con la reforma mal atribuida, para que el perfil no herede citas desfasadas.
- **Normas que los modelos citan de forma recurrente** → `buscar_articulo` sobre las que `verificar_escrito` marque, para confirmar su redacción vigente antes de dar la cita por buena o por desfasada.

Cita solo lo que devuelva Jurisprudenciator.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si `verificar_escrito` no responde, reintenta como máximo dos veces; si sigue sin resultado, detén la tarea y díselo al abogado.
4. Nunca sustituyas una consulta por datos de memoria. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Dónde vive el perfil

Busca el perfil en este orden y usa el primero que exista:

1. El archivo `~/.claude/plugins/config/derecho-virtual/perfil-estilo.md` (Claude Code y Cowork).
2. Un documento llamado `perfil-estilo.md` en el conocimiento del proyecto de Claude en el que se trabaja.
3. Lo que Claude recuerde del estilo del abogado (memoria de Claude).

Si existe y el abogado no pide actualizarlo, esta skill no hace nada más: vuelve a la tarea que se estaba haciendo.

## Paso 1 — Pedir los modelos

Pide al abogado **entre 3 y 5 escritos suyos**, en Word o PDF, del trabajo que más hace y, si puede
ser, de tipos distintos (una demanda o solicitud, un recurso, unas alegaciones…). Díselo así de claro:

> Para que todo lo que redacte salga con tu estilo, pásame 3, 4 o 5 escritos tuyos de referencia
> (Word o PDF). Mejor si están anonimizados; si no lo están, no copiaré ningún dato personal.

- Si el perfil del despacho (entrevista inicial del plugin) ya apunta a plantillas del abogado,
  úsalas como modelos en lugar de volver a pedirlas.
- Con menos de 3 escritos, pide los que falten. Si el abogado prefiere no darlos, guarda un perfil
  que diga «Sin modelos: se usa el estilo de la casa» para no volver a preguntar, y sigue.

## Paso 2 — Analizar los modelos

Lee cada escrito completo y anota, con ejemplos literales breves (sin datos personales):

| Aspecto | Qué anotar |
|---|---|
| Encabezamiento y comparecencia | Fórmula exacta con la que se dirige al órgano y se presenta |
| Estructura | Apartados y su orden; numeración (ordinales, romanos, arábigos); títulos |
| Frase y párrafo | Longitud habitual; frases largas o cortas; uso de enumeraciones |
| Tono | Grado de formalidad; primera o tercera persona; firmeza o prudencia |
| Conectores y fórmulas | Expresiones que repite y le caracterizan |
| Citas de ley | Cómo nombra las normas y los artículos |
| Citas de jurisprudencia | Literal entre comillas o paráfrasis; dónde pone órgano, fecha y ECLI |
| Súplica, otrosíes y cierre | Fórmulas exactas, lugar, fecha y firma |
| Maquetación | Fuente, tamaño, interlineado, márgenes, negritas, mayúsculas, sangrías (si se ven en el Word) |
| Lo que nunca hace | Giros o formatos que evita |

Pasa `verificar_escrito` a cada modelo y apunta las citas desfasadas que encuentre.

## Paso 3 — Escribir el perfil

Redacta `perfil-estilo.md` con estas secciones, en frases imperativas que otra skill pueda seguir:

1. **Fórmulas literales** (encabezamiento, comparecencia, súplica, otrosí, cierre).
2. **Estructura** de sus escritos habituales.
3. **Estilo**: frase, párrafo, tono, conectores preferidos y giros que evita.
4. **Citas**: cómo cita normas y jurisprudencia.
5. **Maquetación**.
6. **Citas desfasadas en sus modelos**: lista de lo que marcó `verificar_escrito`, para no repetirlo.
7. **Origen**: tipos de escritos analizados y fecha.

Ningún nombre, DNI o NIE, dirección, número de procedimiento ni dato de un cliente o contrario entra
en el perfil.

## Paso 4 — Guardarlo

- Si puedes escribir archivos persistentes (Claude Code, Cowork), guárdalo en
  `~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, creando las carpetas si no existen.
- Si no (chat de Claude), entrega el archivo `perfil-estilo.md` y pide al abogado que lo añada al
  conocimiento de su proyecto de Claude; ofrécele también que Claude recuerde los puntos clave.

## Paso 5 — Confirmar

Enséñale al abogado un resumen de 6 a 10 líneas del perfil, pregúntale si quiere corregir algo, aplica
sus correcciones y vuelve a la tarea con la que empezó.

## Cómo lo aplican las demás skills

- El perfil manda en fórmulas, estructura, tono, forma de citar y maquetación.
- Las reglas jurídicas mandan sobre el perfil: la puerta de Jurisprudenciator, citar solo lo
  verificado, el órgano y los plazos vigentes y no inventar datos. Si un modelo del abogado usa una
  denominación o una cita desfasada, se escribe la vigente y se le avisa.

## Actualizar el perfil

Cuando el abogado aporte modelos nuevos o pida cambios, repite los pasos 2 a 5 sobre el perfil
existente y anota en «Origen» qué cambió.
