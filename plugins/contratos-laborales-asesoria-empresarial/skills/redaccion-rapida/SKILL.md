---
name: redaccion-rapida
description: Redacta en 2-3 minutos cualquier escrito, recurso, contrato o documento largo de los plugins de Jurisprudenciator con un equipo de subagentes que escriben las secciones a la vez, y entrega el Word. Úsala cuando otra skill del plugin vaya a redactar un documento para presentar o entregar, y cuando el abogado pida «redáctalo rápido», «en paralelo» o «con subagentes».
---

# Redacción rápida con equipo de subagentes

Tú diriges; el equipo redacta. Preparas el caso y el plan, lanzas a la vez un subagente
`redactor-seccion` por sección, ensamblas con el script y entregas el Word. La skill del escrito
(demanda, recurso, contrato…) aporta el contenido jurídico; esta aporta el método y el reloj.

**Objetivo de tiempo, desde que tienes los hechos:** preparación ≤ 45 s · equipo ≤ 90 s ·
ensamblado, revisión y entrega ≤ 45 s. Total: 2-3 minutos.

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga
conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin. Las consultas
las hacen los subagentes, cada uno solo para su sección: `buscar_articulo`, `buscar_sentencias` +
`leer_sentencias`, `buscar_empresa_mercantil`, `consultar_catastro` y `verificar_escrito`.

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Paso 1 — Arranque (un solo mensaje, todo en paralelo)

Lanza a la vez, en el mismo mensaje:

- `estado` de Jurisprudenciator (la puerta);
- la lectura de la documentación que haya aportado el abogado y del perfil de estilo;
- la mesa de trabajo:
  `python "${CLAUDE_SKILL_DIR}/scripts/escrito.py" iniciar --tipo "<tipo de escrito>" --cliente "<apellido>" --dir "<carpeta>"`
  (`<carpeta>`: la del asunto si existe —p. ej. `matters/<slug>/escritos`—; si no, la carpeta de
  trabajo actual). Devuelve en JSON las rutas de `caso.md`, `secciones/`, `fuentes/` y del Word.
  Si `${CLAUDE_SKILL_DIR}` no se ha sustituido, el script está en `scripts/escrito.py` junto a este
  archivo.
- si el escrito lleva una cifra que usarán varias secciones y depende de una norma (indemnización,
  intereses, cuantía, cómputo de un plazo), el `buscar_articulo` de esa norma; el cálculo lo haces
  tú en el paso 3, con Python si hace falta.

Esa es la única investigación que haces tú: los registros, convenios, artículos y sentencias de
cada sección los consulta su redactor. **Hecho cuando:** el conector responde y tienes las rutas.
Si el conector falla, para (puerta).

## Paso 2 — Datos del caso

Responde con la documentación las preguntas y comprobaciones que pida la skill del escrito
(procedimiento, cuantía, competencia, plazos, requisitos previos, prueba). Pregunta al abogado
solo lo que cambie la estructura del escrito y no se deduzca de lo aportado (a quién defiende, qué
se pide), en **una única** ronda de como máximo cuatro preguntas. Todo lo demás que falte se
redacta como `[PENDIENTE: dato]` y se lista en la entrega. Si la skill exige un requisito previo
que no se cumple (por ejemplo, el intento de MASC no acreditado), dilo y para como ella indique.
La puerta detiene el escrito cuando falta algo imprescindible para el fondo; un dato accesorio que
no aparece (un convenio que no cambia lo que se pide, un dato registral) va como `[PENDIENTE]` y
se avisa en la entrega.

## Paso 3 — `caso.md` y el plan (escríbelo con Write, ≤ 600 palabras)

`caso.md` es lo único que comparten los subagentes y lo que les evita leer la skill entera: todo
lo que necesiten va aquí, en estilo telegráfico.

1. **Escrito**: tipo, procedimiento, órgano exacto según la skill, cuantía, posición del cliente.
2. **Partes y profesionales**: datos de identificación; abogado y procurador (del perfil o del
   CLAUDE.md del despacho; si faltan, `[PENDIENTE]`).
3. **Hechos**: cronología concisa con fechas, importes y el documento que prueba cada hecho.
4. **Documentos**: numeración única (DOCUMENTO Nº 1, 2…) que usarán todas las secciones.
5. **Pretensiones y cifras**: principal, subsidiarias y accesorias, con sus importes ya
   calculados, y toda cifra o fecha que vayan a usar varias secciones (cuantía, indemnización,
   salario regulador, vencimiento del plazo). Las secciones se escriben a la vez: lo que una
   calcule por su cuenta no llega a las demás.
6. **Reglas para el equipo** (≤ 8 líneas, sacadas de la skill del escrito): denominación del órgano
   y de los funcionarios, normas y umbrales que no se pueden equivocar, tribunal y orden de la
   jurisprudencia, formato de cita del perfil de estilo y cualquier prohibición de la skill.
7. **Plan**: una tabla con una fila por sección: `NN | nombre | contenido | palabras | búsquedas`.
   En «búsquedas», las consultas concretas de esa sección (1-2 de jurisprudencia con sus términos
   y los artículos que citará), para que el redactor no tenga que explorar.

**Cómo se reparte el plan:**

- Una sección por cada fundamento de fondo, motivo de recurso, alegación de fondo o bloque de
  cláusulas que necesite su propia investigación. Cada sección investiga lo suyo: ninguna búsqueda
  se repite entre secciones.
- Encabezamiento, comparecencia y hechos en una sección (dos si los hechos pasan de 1.200 palabras).
- Fundamentos procesales (competencia, procedimiento, legitimación, postulación, requisitos
  previos, cuantía) en una sección.
- Cierre en una sección: intereses y costas si proceden, súplica o solicito, otrosíes, lugar,
  fecha, firmas y relación de documentos.
- Extensión total = páginas pedidas × 380 palabras (punto medio del intervalo; si nadie la pide,
  la habitual de ese escrito según la skill). Repártela entre las secciones: cada una entre 300 y
  1.300 palabras. Entre 3 y 8 secciones: un escrito corto (3-4 páginas) lleva 3; uno largo, hasta 8.
- Un documento de una o dos páginas (burofax, comunicación al cliente, escrito de trámite) no
  necesita equipo: redáctalo tú en un único archivo de `secciones/`, con sus consultas lanzadas en
  paralelo, y sigue en el paso 5.
- Numera las secciones con dos cifras en el orden final (`01`, `02`…): el ensamblador las une por
  ese orden y numera solo los hechos, fundamentos, motivos y cláusulas.

## Paso 4 — El equipo (un solo mensaje con todas las llamadas)

Lanza en **un único mensaje** una llamada al subagente `redactor-seccion` por sección del plan
(en la lista de agentes aparece con el prefijo del plugin, por ejemplo
`litigacion-civil-espana:redactor-seccion`; el de cualquier plugin de Jurisprudenciator sirve).
Encargo de cada uno, breve:

```
Carpeta: <carpeta>  (lee caso.md)
Sección NN — <nombre>: <contenido>. Extensión: <palabras> palabras.
Búsquedas: <las de su fila del plan>.
Escribe secciones/NN-<nombre>.md y fuentes/NN.md.
Perfil de estilo: <ruta o «no hay»>.
<Solo si la sección lo necesita: «Estructura de tu sección: <ruta SKILL.md>, apartado <nombre>.»>
<Si toca: «Esta sección abre con el rótulo FUNDAMENTOS DE DERECHO.»>
```

Espera a que terminen todos. **Hecho cuando:** cada sección tiene su archivo. Si un subagente
contesta «SIN CONECTOR», aplica la puerta. Si otro falla o deja su sección vacía, relánzalo solo
a él una vez; si vuelve a fallar, redacta tú esa sección.

## Paso 5 — Ensamblado y comprobación

```
python "${CLAUDE_SKILL_DIR}/scripts/escrito.py" ensamblar "<carpeta>" --salida "<ruta del Word>" --palabras <extensión total del plan>
```

Ruta del Word: con el nombre de archivo que fije la skill del escrito; si no fija ninguno, la que
devolvió `iniciar`.

Devuelve en JSON los errores, avisos, datos pendientes, palabras y segundos transcurridos, y deja
`escrito.md` e `informe.md` (tabla de fuentes) en la carpeta.

- **Errores** (código de salida 2): una cita que ningún subagente leyó, una marca sin resolver o
  una sección vacía. Corrígelos con Edit en el archivo de la sección —sustituye la cita por una de
  las fuentes leídas o retírala— y vuelve a ensamblar. No se entrega con errores.
- **Avisos de estilo**: varía las frases repetidas con Edit.

## Paso 6 — Lectura de coherencia (una pasada)

Lee `escrito.md` una vez y comprueba que encajan las piezas que escribieron manos distintas:
cada fundamento se apoya en hechos que existen, los números de documento coinciden con `caso.md`,
la súplica pide lo que los fundamentos justifican y ninguna idea se repite entre secciones.
Corrige con Edit solo lo que falle y vuelve a ensamblar. No reescribas secciones enteras.

## Paso 7 — Entrega

- Ruta del Word.
- En tres líneas: qué se pide, con qué fundamento y el punto fuerte del caso.
- La tabla de fuentes de `informe.md` (sentencias con ECLI, normas, registros e internet).
- Datos `[PENDIENTE]` que debe completar el abogado.
- Tiempo total (el campo `segundos` del ensamblado).
- Lo que la skill del escrito pida añadir al resumen (próximos pasos, plazos, presentación).

## Sin subagentes

Si en este entorno no puedes lanzar subagentes (por ejemplo, en el chat sin Cowork), sigue los
mismos pasos tú solo: redacta las secciones del plan una a una en sus archivos, haz las consultas
de cada sección en paralelo y ensambla con el script. Si tampoco puedes ejecutar código, entrega
el texto completo con el formato del escrito y avisa de que hay que pasarlo a Word.
