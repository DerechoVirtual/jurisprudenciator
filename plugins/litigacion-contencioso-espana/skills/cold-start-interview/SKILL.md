---
name: cold-start-interview
description: Configurar el perfil de despacho de litigacion contencioso-administrativa en España. Captura areas (sancionador, urbanismo, responsabilidad patrimonial, personal, tributario local, extranjeria, contratacion, subvenciones, expropiacion), CCAA y normativa autonomica, organos judiciales, posicion procesal, colaboradores y estilo de la casa. Usar con configurar plugin, cold-start, setup, redo.
---

# Cold-start del plugin de litigación contencioso-administrativa

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Comprobación de integraciones del bloque 11 (`--check-integrations`)** → `estado`. Si responde, marcar ✓; si no, detener la configuración hasta que Jurisprudenciator esté conectado.
- **Aviso de cobertura del bloque 4** → `buscar_ordenanzas` con los municipios que indique el abogado, para decirle desde el principio si sus ordenanzas están cubiertas (si no lo están, lo dice en una llamada: no reintentar).
- **Reglas de postulación y plazos que se escriben en el perfil** (bloques 6 y 9) → `buscar_articulo` (`ley="LJCA"`, artículos 23 y 128).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

---

Esta skill escribe `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/CLAUDE.md` con el perfil de práctica. Sin completar este paso, las demás skills paran y piden ejecutarlo.

> ⛔ **Ámbito.** Este plugin es **exclusivamente contencioso-administrativo**. No preguntar por áreas civiles, mercantiles, de familia, laborales ni penales, y **no preguntar nunca por MASC**: el intento de MASC de la LO 1/2025 es requisito de procedibilidad del orden **civil** y **no se aplica** en esta jurisdicción. El equivalente funcional aquí es el **agotamiento de la vía administrativa** (art. 25.1 LJCA).

## Cuándo activar

- Primera instalación del plugin (el `CLAUDE.md` de config no existe o está con marcadores `[PLACEHOLDER]`)
- Petición explícita: "configura el plugin", "cold-start", "setup", "vuelve a preguntarme el perfil"
- Flag `--redo` o `--check-integrations`

## Flujo de la entrevista

### Bloque 0: Comprobación previa

1. Leer `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/CLAUDE.md` si existe.
2. Si existe y NO tiene `[PLACEHOLDER]`, preguntar: "Ya tienes una configuración previa. ¿Quieres (a) re-correr todo desde cero, (b) editar un campo concreto con `/customize`, o (c) solo comprobar integraciones?"
3. Si no existe o tiene marcadores, seguir el flujo.

### Bloque 1: Identidad del despacho

Vía `AskUserQuestion` (bloques de 2-4 preguntas):

- Nombre del letrado / despacho
- Forma jurídica (abogado ejerciente individual / SLP / SCP / multiprofesional)
- Colegio profesional (ICAM / ICAB / ICAV / otro)
- Nº de colegiado
- Provincia de actuación habitual
- Años ejerciendo
- Correo y teléfono de contacto

→ Sección `## Identidad del despacho` de la plantilla.

### Bloque 2: Áreas de práctica contencioso-administrativas

Multi-selección (marcar todas las que trabaje el despacho):

- **Sancionador** (tráfico, disciplina, actividad, consumo, extranjería sancionadora)
- **Urbanismo y ordenación del territorio** (licencias, disciplina, planeamiento, ruina)
- **Responsabilidad patrimonial** (sanitaria, viaria, funcionamiento de servicios)
- **Función pública y personal** (oposiciones, provisión, retribuciones, disciplina)
- **Tributario y recaudación local y autonómico** (apremio, derivación de responsabilidad)
- **Extranjería**
- **Seguridad Social y actas de liquidación** (impugnación en vía contenciosa)
- **Contratación pública** (recurso especial, adjudicación, modificados)
- **Subvenciones y ayudas** (reintegro)
- **Expropiación forzosa y justiprecio**
- **Autorizaciones judiciales** (entrada en domicilio, art. 8.6 LJCA)
- **Otros** (campo libre)

Después, pregunta abierta: **asuntos más frecuentes** (los tipos concretos que más entran).

→ Sección `## Áreas de práctica contencioso-administrativas`.

### Bloque 3: Clientes

- Perfil típico: particulares / pymes / empresas / entidades locales / asociaciones y plataformas
- **¿Defiende también a la Administración?** (No / Sí — indicar cuáles). Determina si el despacho puede aparecer en posición de demandada y condiciona el chequeo de conflictos.

→ Sección `## Clientes`.

### Bloque 4: Rol y posición procesal

- **Posición por defecto:**
  - `recurrente` (lo habitual — el despacho impugna actos de la Administración)
  - `Administración demandada` (letrado de servicio jurídico o defensa externa de una AAPP)
  - `codemandado — aseguradora` (típico en responsabilidad patrimonial: la compañía aseguradora de la Administración comparece como codemandada)
  - `variable`
- **Administraciones habitualmente demandadas:** estatal / autonómica (indicar CCAA) / local (indicar municipios o entidades) / institucional (organismos, agencias, universidades)
- **CCAA de actuación y normativa autonómica y local aplicable** — pregunta obligatoria, no es opcional:
  - ¿En qué CCAA litiga?
  - ¿Qué normativa autonómica maneja habitualmente? (ley urbanística autonómica, ley de función pública autonómica, ley de salud, normativa de actividades…)
  - ¿Qué ordenanzas municipales son recurrentes? (indicar municipios)

> ⚠️ **Advertir al usuario en este bloque, con estas palabras:** buena parte del Derecho administrativo material es **autonómico y local**. El conector `jurisprudenciator` cubre **BOE (Derecho estatal)**, jurisprudencia, doctrina DGT y **ordenanzas municipales de los municipios cubiertos**. La normativa **autonómica** (boletines autonómicos) y los **BOP no cubiertos** **no son accesibles**. En esos casos el plugin **pedirá la norma al usuario** y **no la citará de memoria**. Por eso conviene que el usuario indique aquí qué normativa autonómica usa y, si puede, dónde tiene el texto.

→ Sección `## Rol y posición procesal`. Si la plantilla no tiene fila para los órganos del Bloque 5, añadir la fila `Órganos judiciales habituales` **dentro de esta sección** (no crear secciones nuevas).

### Bloque 5: Órganos judiciales habituales

Preguntar cuáles usa realmente (no todos aplican a todos los despachos):

- **Juzgados de lo Contencioso-Administrativo nº [X] de [lugar]** — órgano unipersonal; el más habitual (actos de entidades locales, personal y sanciones ≤ 60.000 € de CCAA, resp. patrimonial de CCAA ≤ 30.050 €, Administración periférica del Estado, extranjería — art. 8 LJCA)
- **Juzgados Centrales de lo Contencioso-Administrativo** (si trabaja asuntos de ámbito estatal de su competencia)
- **Sala de lo Contencioso-Administrativo del TSJ de [CCAA]** — órgano colegiado
- **Audiencia Nacional, Sala de lo Contencioso-Administrativo** — órgano colegiado
- **Tribunal Supremo, Sala Tercera** — casación
- Órganos administrativos de recurso previos: TEAR/TEAL, tribunales administrativos de contratación pública, jurados de expropiación — preguntar cuáles

> ⚠️ **No preguntar por Tribunales de Instancia ni Audiencias Provinciales.** Son órganos del orden civil/penal y no intervienen en esta jurisdicción.

### Bloque 6: Colaboradores clave

Preguntar uno a uno; permitir "no aplica":

- **Procurador de cabecera** (nombre + colegio + provincia).
  > Explicar al usuario: en el contencioso el procurador es **potestativo ante los órganos unipersonales** (Juzgados de lo CA) y **preceptivo ante los órganos colegiados** (Salas de TSJ, AN y TS) — **art. 23 LJCA** (redacción del RD-ley 6/2023, en vigor 20-3-2024). El abogado es siempre preceptivo. Si ante el Juzgado se confiere la representación al abogado, a él se le notifican las actuaciones. **No aplica la regla civil del art. 23 LEC ni el umbral de los 2.000 €: es otra norma y otro orden.**
- **Perito médico** (imprescindible en responsabilidad patrimonial sanitaria)
- **Perito arquitecto / ingeniero / urbanista** (urbanismo, disciplina, ruina, licencias, actividad)
- **Perito económico / tasador** (justiprecio expropiatorio, lucro cesante, valoración de daños, cuantía)
- Otros colaboradores externos (abogado de apoyo, gestoría, detective)

→ Sección `## Colaboradores clave`.

### Bloque 7: Apetito al riesgo y RC profesional

- Postura general (cita libre): p. ej. "agotar siempre la vía administrativa aunque sea potestativa" / "recurrir solo con informe pericial en mano" / "pelear cualquier asunto del cliente"
- Bandas de severidad cuantitativas (alta / media / baja en €)
- Bandas de probabilidad (alta / media / baja en %)
- Cobertura RC profesional: aseguradora + límite por siniestro + franquicia
- Umbral de comunicación urgente al cliente
- **Escalera de autoridad para desistir o allanarse** (cuantías + decisor + documento de respaldo). En contencioso las decisiones críticas son **desistimiento** (art. 74 LJCA), **allanamiento** (art. 75) y **satisfacción extraprocesal** (art. 76), no la transacción civil.

→ Sección `## Apetito al riesgo y RC profesional`.

### Bloque 8: Almacenamiento documental y estilo de la casa

- Carpeta raíz de asuntos: una carpeta local (ej. `C:/Asuntos/`), OneDrive, Google Drive o Dropbox si el abogado lo tiene conectado
- Patrón de slug por defecto: `descriptor-materia-año` (DEFAULT). **Advertir: el slug no debe contener el nombre del cliente** si el repositorio se comparte o sincroniza.
- ¿Comparte con el cliente por correo o por carpeta compartida?
- Voz redaccional: por defecto la pluma de la casa (`estilo-escritos-judiciales`). Confirmar o pedir muestras de escritos reales para calibrar.
- Entregable: Word `.docx` maquetado para LexNET (DEFAULT).
- Briefing al cliente: formato + tono + cadencia.

→ Secciones `## Herramientas y tecnología` y `## Estilo de la casa`.

### Bloque 9: Calendario y plazos — reglas de la casa

Confirmar con el usuario (los dos primeros son **derecho imperativo**, no preferencia: se informan, no se negocian):

- **Naturaleza de los plazos de interposición: caducidad.** No se interrumpen por reclamación extrajudicial ni por burofax. Perdido el plazo, el acto deviene firme y consentido (art. 69.e LJCA).
- **Agosto: no corre ningún plazo de la LJCA, SALVO en el procedimiento de protección de derechos fundamentales, donde agosto es hábil** (art. 128.2 LJCA).
- Margen de seguridad interno (DEFAULT: presentar con **7 días naturales** de antelación al vencimiento) — configurable.
- Doble control de plazo (DEFAULT: sí) — configurable.

→ Sección `## Calendario y plazos — reglas de la casa`.

### Bloque 10: Honorarios / encargo

- IBAN del despacho (para la hoja de encargo)
- Modalidad de honorarios habitual
- Confirmar que la advertencia de costas al cliente sigue el **art. 139 LJCA**, con el **tope del tercio de la cuantía del proceso por cada favorecido** (art. 139.4, RD-ley 6/2023)

→ Sección `## Honorarios / encargo`.

### Bloque 11: Integraciones (`--check-integrations`)

Comprobar disponibilidad real (no solo configuración):

- Conector `jurisprudenciator` (viene con el plugin) → **única** vía de jurisprudencia y legislación; llamar a `estado` y comprobar que responde. Si funciona, marcar ✓
- Gestor documental (opcional) → si el abogado tiene conectado OneDrive, Google Drive o Dropbox, comprobar que responde listando la carpeta raíz de asuntos; si trabaja con una carpeta local, anotarlo así. El plugin no instala ningún gestor documental.
- Scheduled-tasks MCP → comprobar disponibilidad

→ Sección `## Integraciones disponibles`.

### Bloque 12: Documentos semilla (opcional)

Preguntar si tiene plantillas existentes que pueda apuntar (modelos de interposición, de demanda, hoja de encargo, minuta, política RGPD). **Solo apuntadores; no copiar el contenido al perfil.**

## Salida

Escribir todo a `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/CLAUDE.md`. Si el directorio padre no existe, crearlo.

Usar como esqueleto **la plantilla `CLAUDE.md` de la raíz del plugin**, reemplazando cada `[PLACEHOLDER]` / `[PENDIENTE]` por las respuestas y respetando su estructura de secciones y tablas. No inventar secciones nuevas; si un dato capturado no tiene fila, añadir la fila en la sección temáticamente correcta.

Bloques de la plantilla que **no se preguntan y se copian tal cual** (son marco normativo, no preferencia del usuario): `## Ámbito del plugin`, el bloque del conector en `## Jurisprudencia y legislación`, y la nota de ámbito territorial.

Para campos con multi-elección (áreas de práctica, bandas, integraciones), mantener la estructura de lista de checkboxes o de tabla de la plantilla.

Registrar la fecha en `## Historial de cambios`.

Después de escribir el archivo, mostrar al usuario:

- "✅ Configurado. Tu perfil está en `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/CLAUDE.md`."
- Próximo paso sugerido: "Crea tu primer asunto con `/asunto-intake [nombre-asunto]`."
- Si el conector salió ✗: "jurisprudenciator no respondió — no se podrá buscar ni verificar jurisprudencia ni legislación, y las citas se marcarán como `[verificar]`. Activa el conector jurisprudenciator en el chat/proyecto."
- Si el usuario declaró normativa autonómica: "Recuerda: la normativa autonómica que has indicado **no** es accesible por el conector. Cuando un escrito la necesite, el plugin te pedirá el texto."

## Variantes

- `--redo`: ignora el archivo existente; sobreescribe.
- `--check-integrations`: NO re-pregunta; solo actualiza la tabla `## Integraciones disponibles`.
- `--quick`: versión de 2 minutos con solo: identidad del despacho, provincia y CCAA de actuación, áreas de práctica principales, posición procesal por defecto y órgano judicial habitual. Pone defaults razonables en lo demás y marca esos campos con `# DEFAULT — editar después con /customize`.

## Reglas

1. **NUNCA escribir datos del usuario en el `CLAUDE.md` que viaja con el plugin.** Siempre en la ruta de config (`~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/CLAUDE.md`). La plantilla de la raíz queda intacta y vacía.
2. **Cero datos reales fuera de la ruta de config.** Ningún ejemplo, muestra o salida de esta skill puede contener DNI, NIE, CIF, IBAN, nombres, direcciones, teléfonos ni correos reales: siempre marcadores entre corchetes.
3. **NUNCA continuar con campos `[PLACEHOLDER]`** cuando una skill de trabajo los pida. Detenerse y pedir al usuario que complete con cold-start o `/customize`.
4. **El cold-start es FORMAL:** no asumir respuestas, preguntar todo. Solo `--quick` y `--check-integrations` permiten defaults.
5. **No preguntar por MASC, burofax, Derecho civil foral, Tribunales de Instancia ni Audiencias Provinciales.** No pertenecen a esta jurisdicción.
6. **Plazos y umbrales:** no afirmar ninguno que no esté en `references/anclas-normativas-ca.md` o que no se haya verificado en el momento con `buscar_articulo`.
