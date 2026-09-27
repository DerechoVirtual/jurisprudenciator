---
name: subsuncion-juridica
description: Jurisprudencia SIEMPRE con el conector MCP jurisprudenciator (tools buscar_sentencias, buscar_por_cita, leer_sentencias); es la unica via. Pulido y revision de escritos para conectar jurisprudencia con hechos concretos del asunto. Transforma citas sueltas en argumentacion subsuntiva. Usar con pulir escrito o conectar jurisprudencia.
---

# Subsunción jurídica — pulido del escrito

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Doctrina concreta de cada cita** (el «elemento jurisprudencial» del paso 4) → `leer_sentencias` (`citas`, `parrafos=3`, `terminos` del punto) para trabajar con el párrafo literal y no con una paráfrasis.
- **Verificar los ECLI o ROJ ya citados** → `buscar_por_cita`.
- **Redundancia: localizar la más reciente o la dictada en unificación de doctrina** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`, `fecha_desde`) y `opciones_busqueda` para acotar.
- **Sustituir una cita que no aterriza en los hechos** → `buscar_sentencias` con la cuestión jurídica concreta del caso (anonimizada) + `leer_sentencias`.
- **Revisión final** → `verificar_escrito` con el texto completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- AUTOMÁTICAMENTE tras `redactar-demanda-despido`, `reclamacion-cantidad`, `extincion-contrato-trabajador`, `recurso-suplicacion`, `recurso-casacion-unificacion-doctrina`, etc.
- Petición explícita: "pulir escrito", "conectar jurisprudencia con hechos"
- Cuando una primera versión cita STS pero no la conecta al caso concreto

## Patrón a corregir (citas "sueltas")

❌ MAL:

> "...la jurisprudencia del Tribunal Supremo en STS [ECLI] establece que el impago salarial
> debe ser grave y persistente. En el presente caso, la empresa no pagaba..."

✅ BIEN (subsuntivo):

> "...la jurisprudencia de la Sala IV del Tribunal Supremo, en STS [ECLI], exige que el
> impago o retraso salarial sea GRAVE y PERSISTENTE para activar la extinción del art. 50.1.b)
> ET, sin que sea preciso el elemento de culpabilidad empresarial. Aplicada esta doctrina al
> presente caso, no estamos ante un retraso aislado: la empresa adeuda tres mensualidades
> completas (Doc. Nº 5, nóminas impagadas) y ha abonado con retrasos de entre 20 y 45 días
> las seis anteriores (Doc. Nº 6, extractos bancarios). Concurre, por tanto, la gravedad y
> persistencia que el Supremo exige para declarar extinguido el contrato con derecho a la
> indemnización del despido improcedente."

## Flujo

### 1. Leer escrito

Cargar el documento generado por skill aguas arriba.

### 2. Localizar citas jurisprudenciales

Identificar cada STS (Sala IV) / STSJ / TJUE / TC citada.

### 3. Para cada cita, comprobar:

- ¿Hay HECHOS del caso citados expresamente?
- ¿La cita lleva al "por tanto, aplicado al caso concreto..."?
- ¿Se nombra el Documento Nº [X] que sostiene la conexión?

### 4. Si la cita está "suelta"

Reescribir la frase añadiendo:
- **El elemento jurisprudencial concreto** (qué doctrina sienta la STS)
- **La subsunción al caso** (hecho concreto del cliente que materializa el elemento)
- **La conclusión jurídica derivada** (qué tiene que hacer el tribunal)

### 5. Eliminar redundancia

Si dos STS dicen lo mismo, citar la más reciente y la dictada en unificación de doctrina (RCUD). No abrumar con jurisprudencia repetitiva.

### 6. Output

Escrito pulido + diff frente al original, marcando los cambios.

## Reglas

1. **Jurisprudencia que no conecta es jurisprudencia perdida.** Si una cita no aterriza en el caso, fuera.
2. **Cada cita = un punto subsuntivo concreto.** No "como la jurisprudencia mayoritaria entiende..." (vago) sino "como la STS [ECLI] establece que [doctrina concreta], aplicado al presente caso [hecho concreto]..."
3. **Documentos Nº [X] son la cuerda** entre hechos y doctrina. Si la frase no menciona el documento, no está subsumiendo.
4. **NO inventar.** Si no se puede aterrizar la cita con los documentos existentes, marcar `[REVISAR: jurisprudencia citada no aterrizada — eliminar o sustituir]`.
