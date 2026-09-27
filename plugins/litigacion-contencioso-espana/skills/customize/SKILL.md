---
name: customize
description: Editar un campo del perfil de despacho contencioso-administrativo sin re-correr todo el cold-start. Cambiar CCAA y normativa autonomica, organos judiciales (Juzgados de lo CA, Sala del TSJ, AN, TS Sala Tercera), areas de practica, posicion procesal, colaboradores, calibracion de riesgo, plantillas, integraciones. Usar con cambiar mi perfil o customize.
---

# Customize — editar un campo concreto

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Re-comprobar integraciones (campo 13)** → `estado`.
- **CCAA o municipios nuevos (campo 5)** →`buscar_ordenanzas` con los municipios añadidos, para decir al abogado si sus ordenanzas están cubiertas.
- **Ajustes en cadena por órganos colegiados o contratación pública** → `buscar_articulo` (`ley="LJCA"`, artículos 23 y 44).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Cambiar mi [campo]"
- "Actualizar mi perfil"
- "Editar [sección]"
- "Añadir procurador / perito / plantilla"
- "Ahora también litigo en [CCAA / provincia]"
- "He empezado a llevar [urbanismo / expropiación / contratación]"

## Flujo

### 1. Comprobar que hay perfil

Leer `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/CLAUDE.md`. Si no existe o tiene `[PLACEHOLDER]` masivos, derivar a `/cold-start-interview` — customize no es el camino para configurar desde cero.

### 2. Detectar qué campo

Si el usuario nombra el campo, ir directo. Si no, mostrar menú:

```
¿Qué cambiamos?
1. Identidad del despacho (forma jurídica, colegio, colegiado, provincia, contacto)
2. Áreas de práctica CA (sancionador, urbanismo, resp. patrimonial, personal,
   tributario local, extranjería, contratación, subvenciones, expropiación…)
3. Clientes (perfil típico; si defiende también a la Administración)
4. Rol y posición procesal (recurrente / Administración demandada /
   codemandado-aseguradora / variable) y Administraciones demandadas
5. CCAA de actuación y normativa autonómica y local aplicable
6. Órganos judiciales habituales (Juzgados de lo CA, Sala del TSJ, AN, TS Sala Tercera)
   y órganos administrativos de recurso (TEAR/TEAL, tribunales de contratación, jurados
   de expropiación)
7. Colaboradores (procurador / perito médico / arquitecto-urbanista / económico-tasador)
8. Calibración de riesgo (apetito / bandas / autoridad para desistir o allanarse / RC)
9. Estilo de la casa (voz, briefing al cliente, entregable, plantillas)
10. Almacenamiento documental (carpeta raíz —local, OneDrive, Google Drive o Dropbox—, patrón de slug)
11. Calendario y plazos (margen de seguridad, doble control)
12. Honorarios / encargo (IBAN, modalidad habitual)
13. Integraciones (`jurisprudenciator` —re-comprobar con `estado`— y, opcionalmente, el gestor documental que el abogado tenga conectado)
14. Documentos semilla (apuntadores a plantillas)
```

### 3. Hacer el cambio

Vía `AskUserQuestion`:
- Mostrar valor actual
- Pedir nuevo valor
- Confirmar antes de escribir

### 4. Validaciones y ajustes en cadena

- **Provincia o CCAA cambia → revisar órganos judiciales habituales** (Juzgados de lo CA y Sala del TSJ son territoriales; preguntar si también cambian) **y revisar normativa autonómica aplicable**, que cambia con la CCAA.
- **Se añade normativa autonómica nueva → recordar el límite del conector:** `jurisprudenciator` cubre BOE estatal, jurisprudencia, doctrina DGT y ordenanzas de los municipios cubiertos; **la normativa autonómica y los BOP no cubiertos no son accesibles**. Advertir de que el plugin pedirá el texto al usuario y no la citará de memoria.
- **Se añaden órganos colegiados (Sala del TSJ, AN, TS) → revisar procurador:** ante órganos colegiados el procurador es **preceptivo** (art. 23.2 LJCA); ante los Juzgados de lo CA es **potestativo**. Si no hay procurador de cabecera registrado, avisar.
- **Posición procesal cambia a `Administración demandada` → revisar conflictos**: el despacho no puede recurrir contra la misma Administración a la que defiende. Avisar expresamente.
- **Posición procesal cambia a `codemandado — aseguradora` → revisar áreas**: suele implicar responsabilidad patrimonial y perito médico.
- **Se añade responsabilidad patrimonial sanitaria → revisar perito médico** y advertir de que la historia clínica contiene **datos de salud, categoría especial del art. 9 RGPD** (ver `/conservacion-documental`).
- **Se añade contratación pública → recordar el art. 44.1 LJCA**: las decisiones de los órganos que resuelven el recurso especial en materia de contratación se recurren **directamente, sin requerimiento ni recurso administrativo previo**.
- **Colegio profesional cambia → revisar nº de colegiado** (no encaja a otro colegio).
- **Cambio masivo de calibración de riesgo → recomendar `/cold-start-interview --redo`.**

### 5. Escribir

Editar `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/CLAUDE.md` modificando solo la línea o sección afectada. Mantener el resto idéntico. Anotar el cambio en `## Historial de cambios` con la fecha.

El perfil de este plugin es autónomo; el cambio se guarda solo en su `CLAUDE.md` y **no se comparte con ningún otro plugin**. En particular, **no** toca el perfil de ningún plugin de litigación civil, que vive en otro directorio de config.

### 6. Output

```
✅ Actualizado.

**Campo:** [nombre]
**Antes:** [valor anterior]
**Ahora:** [valor nuevo]

[Si dispara otras revisiones:]
**Posibles ajustes en cadena:** [sugerencias]
```

## Reglas

1. **Un campo por sesión.** Si el usuario quiere cambiar varios, hacerlos secuencialmente uno a uno, confirmando cada uno.
2. **NUNCA borrar campos.** Si el usuario quiere "vaciar" un campo, dejar `[PENDIENTE]` con nota, no borrar la fila.
3. **NUNCA escribir en el `CLAUDE.md` de la raíz del plugin** — es la plantilla vacía que viaja con el plugin. Todo cambio va a la ruta de config.
4. **Cero datos reales fuera de la ruta de config.** En menús, ejemplos y mensajes de esta skill, los datos personales van siempre entre corchetes: `[CLIENTE]`, `[DNI]`, `[DOMICILIO]`, `[IBAN]`, `[LETRADO]`.
5. **No ofrecer campos de otra jurisdicción.** No hay MASC, ni Derecho civil foral, ni Tribunales de Instancia, ni Audiencias Provinciales en este perfil. Si el usuario los pide, explicar que el plugin es exclusivamente contencioso-administrativo.
6. **No afirmar plazos ni umbrales de memoria.** Comprobar en `references/anclas-normativas-ca.md` o verificar con `buscar_articulo`; en su defecto, marcar `[verificar]`.
