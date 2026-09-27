---
name: tutela-derechos-fundamentales
description: >-
  Redaccion de demanda de tutela de derechos fundamentales y libertades publicas en el orden social (arts. 177-184 LRJS) cuando la relacion laboral CONTINUA: acoso, discriminacion, represalias por garantia de indemnidad, libertad sindical, intimidad y desconexion digital. Incluye indicios, inversion de carga probatoria e indemnizacion del art. 183. Usar con "que cese el acoso pero sigo trabajando", "discriminacion en el trabajo", "garantia de indemnidad", "libertad sindical", "vulneracion de derechos fundamentales sin despido". Dos exclusiones: si la vulneracion se ha materializado en un DESPIDO, el cauce correcto es siempre la demanda de despido pidiendo la nulidad → /redactar-demanda-despido; si el trabajador quiere extinguir el contrato por ese mismo incumplimiento, /extincion-contrato-trabajador.
---

# Tutela de derechos fundamentales y libertades públicas (arts. 177-184 LRJS)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Doctrina constitucional sobre indicios, inversión de la carga y garantía de indemnidad, que es el corazón del escrito** → `buscar_sentencias` (`base="TC"`) + `leer_sentencias` (`parrafos=3`); cada STC que se cite por número se comprueba con `buscar_por_cita` (`"STC nnn/aaaa"`).
- **Cuantificación del daño moral del art. 183 LRJS** → doctrina de la Sala Cuarta con `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`) + `leer_sentencias`, y banda orientativa de la LISOS con `buscar_articulo` (`ley="LISOS"`, `articulo="40"`).
- **Arts. 177-184 LRJS y norma de desarrollo del derecho invocado** (Ley 15/2022, LO 3/2007, LOLS) → `buscar_articulo`.
- **Discriminación con base en el derecho de la Unión** (igualdad de trato, Directivas 2000/78/CE y 2006/54/CE) → `buscar_sentencias` (`base="TJUE"`) y `buscar_articulo` (`ley="Directiva 2006/54/CE"`).
- **Empresa demandada** (denominación exacta, CIF, domicilio social y administradores) → `buscar_empresa_mercantil`.
- **Revisión del borrador: toda cita se verifica antes de usarla** → `verificar_escrito` con el texto completo y `buscar_por_cita` sobre cada ECLI o ROJ.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Marco normativo

- **Ámbito** (art. 177.1 LRJS): cualquier vulneración de derechos fundamentales y libertades públicas en el ámbito de la relación de trabajo, incluida la producida por terceros. Legitimación del trabajador; coadyuvancia del sindicato (art. 177.2).
- **Ministerio Fiscal siempre parte** (art. 177.3 LRJS) — citarlo en el encabezamiento.
- **Excepciones de encauzamiento** (art. 184 LRJS): despido, extinción art. 50, MSCT, vacaciones, materia electoral, movilidad, conciliación de la vida familiar e impugnación de convenios se tramitan por SU modalidad propia aunque se invoque un derecho fundamental — pero con las garantías de la tutela acumuladas (art. 178.2, 26.5 LRJS): urgencia, Fiscal, indemnización del 183. Elegir bien la puerta de entrada ANTES de redactar.
- **Conciliación previa**: exenta, salvo que la parte quiera intentarla (art. 64.1 LRJS).
- **Tramitación urgente y preferente** (art. 179.1 LRJS): agosto hábil (art. 43.4).
- **Contenido de la demanda** (art. 179.3 LRJS): expresar con claridad los hechos constitutivos de la vulneración, el derecho o libertad infringidos y la **cuantía de la indemnización** con especificación de daños y perjuicios — la cuantificación NO es opcional.
- **Indicios e inversión de la carga** (art. 181.2 LRJS): acreditados indicios de vulneración, corresponde al demandado la justificación objetiva y razonable de su medida. El escrito debe construir los indicios uno a uno (panorama indiciario), no afirmarlos en abstracto.
- **Sentencia** (art. 182 LRJS): declaración de la vulneración, nulidad radical de la conducta, cese inmediato, reposición de la situación e indemnización.
- **Indemnización** (art. 183 LRJS): daño moral resarcible aun sin prueba de perjuicios económicos exactos; criterio orientativo habitual: cuantías de la LISOS — razonar la banda y el importe elegidos, nunca cifra arbitraria.
- **Medidas cautelares** (art. 180 LRJS): suspensión de los efectos del acto impugnado en supuestos cualificados (libertad sindical, huelga, acoso, violencia sobre la mujer...).
- Recurso: la sentencia tiene siempre acceso a suplicación (art. 191.3.f LRJS).

## Fase 1 — Documentación a pedir

- Relato cronológico detallado de los hechos (fechas, autores, testigos de cada episodio).
- Soportes: correos, WhatsApps, grabaciones, partes médicos, denuncias internas o ante la ITSS, actas sindicales.
- Hitos que anclen la conexión temporal del indicio (p. ej. reclamación previa del trabajador → represalia inmediata: garantía de indemnidad).
- Si hay afectación a la salud: informes médicos (aplicar el aviso de datos de salud — no reproducir diagnósticos de terceros en plantillas).

## Fase 2 — Batería de preguntas (AskUserQuestion)

- ¿Qué derecho fundamental concreto se invoca? (igualdad/no discriminación 14 CE; integridad 15 CE; intimidad 18 CE; libertad sindical 28.1 CE; tutela judicial efectiva/garantía de indemnidad 24 CE...).
- ¿La conducta encaja en una modalidad del art. 184? → derivar a `/redactar-demanda-despido`, `/extincion-contrato-trabajador`, etc., acumulando las garantías de tutela.
- ¿Qué indicios concretos hay y qué documento sostiene cada uno?
- ¿Contra quién se dirige? (empresa y, en su caso, persona física causante — art. 177.4 LRJS permite dirigirla contra el sujeto causante).
- ¿Cuantificación de la indemnización del art. 183? — construir el razonamiento (banda LISOS, duración, gravedad, reiteración).
- ¿Se necesitan medidas cautelares del art. 180?

## Fase 3 — Estructura del escrito

1. Encabezamiento: órgano competente, actora (marcadores genéricos), demandados (empresa y persona física si procede) **y Ministerio Fiscal** (art. 177.3 LRJS).
2. **HECHOS**: relación laboral → episodios de la vulneración en orden cronológico, cada uno con su soporte → panorama indiciario explicitado ("indicio primero..., indicio segundo...") → daños producidos (morales y, en su caso, materiales) con las bases de cuantificación.
3. **FUNDAMENTOS DE DERECHO**: jurisdicción y competencia → adecuación de la modalidad (arts. 177-179 LRJS; o justificación de la acumulación si se va por el art. 184) → derecho fundamental vulnerado (precepto CE + desarrollo: Ley 15/2022, LO 3/2007, LOLS según el caso) → doctrina de indicios e inversión de carga (art. 181.2 LRJS + doctrina constitucional, verificada) → contenido de la condena (art. 182) → indemnización (art. 183, con el razonamiento de cuantía).
4. **SUPLICO**: declaración de la vulneración; nulidad radical de la conducta; cese inmediato; reposición de la situación anterior; indemnización de [X] € por daño moral (y material en su caso).
5. **OTROSÍES**: medidas cautelares del art. 180 si proceden; proposición de prueba (interrogatorio con apercibimiento 91.2, testifical, documental, pericial psicológica).

## Fase 4 — Verificación y entrega

- Comprobar la puerta procesal (¿art. 184 obliga a otra modalidad?).
- Verificar doctrina de indicios y cuantías indemnizatorias con `buscar_por_cita` y `leer_sentencias` de Jurisprudenciator.
- Ministerio Fiscal citado. Cuantía del 183 razonada.
- Pulir con `/estilo-escritos-judiciales`. Entregar en Word (.docx).

---

**Nota de anonimización**: cualquier dato identificativo real de terceros (víctima, acosador, testigos, empresa) presente en documentos de origen se sustituye por marcador genérico y nunca se reproduce. Si hay datos de salud, aplicar el aviso reforzado de las skills de Seguridad Social.
