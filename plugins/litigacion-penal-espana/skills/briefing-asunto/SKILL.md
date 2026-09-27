---
name: briefing-asunto
description: Briefing profundo de un asunto penal. Fase, delitos y ley aplicable, control del plazo de instruccion del art. 324 LECrim, prescripcion, situacion personal y medidas cautelares, linea de defensa, proximo plazo y re-evaluacion de riesgo. Usar con briefing o donde estamos con el asunto.
---

# Briefing de asunto — penal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Jurisprudencia clave del asunto** → `buscar_sentencias` (`jurisdiccion="PENAL"`, `base="TS"` para la Sala Segunda; `base="AN"` para AN, TSJ, AP y juzgados) + `leer_sentencias` con `parrafos=3` para el párrafo literal con su ECLI.
- **ECLI o ROJ ya anotados en el asunto** → `buscar_por_cita` antes de reutilizarlos en el briefing.
- **Plazo del art. 324 LECrim y prescripción (arts. 131 y 132 CP)** → `buscar_articulo` si el log no trae la redacción verificada.
- **Pena del delito imputado y ley más favorable** → `buscar_articulo` (`ley="CP"`): indica desde cuándo rige la redacción y qué norma la dio.
- **Comprobación previa del conector** (paso de *pre-flight*) → `estado`; si no responde, se aplica la puerta obligatoria de abajo y el briefing se detiene.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- "Briefing de [slug]", "ponme al día con [asunto]"
- "Dónde estamos con [asunto]"
- Antes de: reunión con el cliente, declaración del investigado, comparecencia del art. 505,
  audiencia preliminar (art. 785), juicio oral, vistilla, llamada con el procurador o negociación de
  conformidad con la acusación
- Cuando un colaborador (procurador, perito) pide estado

## Prerrequisito

Base de asuntos en
`~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/matters/`.

## Flujo

### 1. Identificar asunto

Si no se da slug, listar candidatos por:
- Asunto activo en CLAUDE.md
- Asuntos con `next_deadline` próximo
- Asuntos con **instrucción próxima a vencer** (art. 324) o con `art_324_3_alerta: sí`
- Últimos actualizados

### 2. Leer fuentes

- `matters/<slug>/matter.md` — intake, tesis y línea de defensa
- `matters/<slug>/history.md` — eventos
- Fila correspondiente de `_log.yaml`
- Escritos en `matters/<slug>/escritos/` (lista con fechas)
- Jurisprudencia archivada en `matters/<slug>/jurisprudencia/`
- Cronología si existe en `matters/<slug>/cronologia.md`

### 3. Comprobaciones obligatorias antes de escribir el briefing

No son opcionales. Se hacen siempre, aunque nadie las pregunte:

1. **⚠️ Art. 324 LECrim.** Calcular días que restan hasta `fecha_vencimiento_instruccion`.
   ¿Hay prórroga acordada? ¿Su auto se dictó **antes** del vencimiento anterior? ¿Alguna prórroga
   está recurrida? Si `art_324_3_alerta: sí`, el briefing **abre** con eso.
2. **Prescripción del delito** (art. 131 CP): días/años restantes hasta
   `prescripcion_delito.fecha_estimada`. ¿Hay paralización del procedimiento que reactive el cómputo
   (art. 132.2)?
3. **Ley aplicable en el tiempo** (art. 2 CP): ¿los hechos son anteriores a la **LO 1/2026**
   (10-4-2026) o a la **LO 1/2025** (3-4-2025)? Si sí, ¿se ha hecho la **comparación de penas** y se
   ha pedido la redacción **más favorable** (art. 2.2 CP)? Si no consta, es una **cuestión abierta**.
4. **Situación personal**: si hay **prisión provisional**, días transcurridos y **límite del
   art. 504**; si se superan las **2/3 partes** del máximo, señalarlo (504.6 → tramitación
   preferente).
5. **Plazo de recurso abierto**: ¿la última notificación abrió plazo y sigue vivo?

### 4. Sintetizar briefing

Estructura:

```
**[Slug] — [Nombre del asunto]**
Posición: [defensa / acusación particular / acusación popular / actor civil / responsable civil subs.]
Fase: [diligencias previas / instrucción / intermedia / juicio oral / recurso / ejecución]
Procedimiento: [abreviado / sumario / juicio rápido / delito leve / jurado / menores]
Órgano: [ÓRGANO] · [nº de procedimiento]
Delitos: [tipo — art. X CP] (+ agravantes invocadas)
Fecha de los hechos: [AAAA-MM-DD] → CP aplicable: [redacción]
Situación personal: [libertad / libertad provisional / prisión provisional / medidas 544 bis]
Medidas cautelares: [ninguna / 544 bis / 544 ter / prisión / fianza-embargo]
Estado: [open / stayed]
Riesgo: [icono + nivel]
Materialidad: [alta/media/baja]

---

## ⚠️ Plazo de instrucción — art. 324 LECrim
Incoación: [fecha] · Vencimiento: [fecha] · **Restan: [N] días**
Prórrogas: [N] — [fecha de auto de cada una / ninguna]
Art. 324.3: [✅ sin incidencias / ⚠️ ALERTA — diligencias posteriores al vencimiento sin auto previo]
[Si hay alerta: listar las diligencias afectadas y la consecuencia — no son válidas.]

## Prescripción del delito — art. 131 CP
Plazo: [X años] · Fecha estimada: [fecha] · **Restan: [N]**
[Interrupciones/suspensiones relevantes del art. 132.2, si las hay.]

## Tesis y línea de defensa
[2-3 frases — la historia que sostenemos]
Línea dominante: [atipicidad / autoría no acreditada / prueba ilícita art. 11.1 LOPJ /
presunción de inocencia / eximente o atenuante / prescripción / nulidad art. 324.3 / conformidad]

## Posición procesal actual
[En qué punto exacto: declaración pendiente / instrucción viva con diligencias pedidas /
traslado para escrito de defensa / juicio señalado / recurso interpuesto / ejecutoria abierta]

## Hitos desde la última actualización
[Eventos de history.md — fechas + qué ocurrió]

## Próximo plazo crítico
[Fecha + qué hay que hacer + cómputo con su norma:
"Escrito de defensa: 10 días comunes desde el traslado del 2026-07-17 (art. 784.1 LECrim) → vence 2026-07-31"]

## Estado de la prueba
De cargo: [qué tiene la acusación y qué le falta]
De descargo: [qué tenemos, qué falta pedir, qué caduca]
Ilicitud / cadena de custodia: [puntos de ataque]

## Responsabilidad civil
Reclamado: [€] · Aseguradora: [sí/no] · Reparación: [nada / parcial / compromiso ofrecido]
[Impacto en art. 80.2.3.ª CP: la reparación o el compromiso condiciona la suspensión.]

## Conformidad
[no planteada / negociando / prestada] — [pena ofrecida vs. pena solicitada]
[Frontera de los 2 años del art. 80 CP: ¿la conformidad la cruza a favor?]

## Cuestiones abiertas
- [pregunta 1 que necesita decisión]
- [pregunta 2 que necesita información del cliente]

## Re-evaluación de riesgo
[¿Sigue siendo X o ha cambiado? Si cambia, propuesta de nuevo nivel y razón — solo por hechos.]

## Jurisprudencia clave en el asunto
- [Resolución verificada con jurisprudenciator — punto que sostiene]
- ..

## Conservación documental
[Acreditada al cliente / pendiente / liberada]
```

### 5. Decision tree

> **¿Qué hago ahora?**
> 1. **Redactar el siguiente escrito** — `/escrito-defensa-calificacion`,
>    `/alegaciones-oposicion-sobreseimiento`, `/querella-catalogo`,
>    `/personacion-acusacion-particular-catalogo`, `/recurso-apelacion-sentencia-penal-catalogo`,
>    `/recurso-casacion-penal-catalogo`
> 2. **Pedir diligencias** — `/solicitud-diligencias-instruccion-catalogo` (antes, comprobar que
>    queda plazo del art. 324: una diligencia pedida fuera de plazo no se acuerda)
> 3. **Mover medidas cautelares** — `/medidas-cautelares-penales-catalogo`
> 4. **Actualizar history con nuevos hitos** — `/actualizar-asunto <slug>`
> 5. **Cronología de los hechos** — `/cronologia <slug>`
> 6. **Cuadro de elementos del tipo** — `/cuadro-elementos <slug>` · subsunción —
>    `/subsuncion-juridica <slug>`
> 7. **Preparar interrogatorio** — `/preparacion-interrogatorio <slug> <declarante>`
> 8. **Valorar conformidad** — `/conformidad-penal-catalogo`
> 9. **Tirar de jurisprudencia** — conector MCP `jurisprudenciator` (`buscar_sentencias`)

## Reglas

1. **El briefing abre por el art. 324.** Si la instrucción vence en menos de 60 días, o si
   `art_324_3_alerta: sí`, eso va **arriba del todo**, antes que la tesis. Es lo único que caduca de
   forma irreversible y silenciosa.
2. **No reinventar la tesis.** Si `matter.md` tiene tesis, usarla. Si en `history.md` se cambió,
   marcarlo.
3. **Cómputo penal, no civil:** todos los días y horas son hábiles **para la instrucción**
   (art. 201 LECrim); **agosto** y **del 24 de diciembre al 6 de enero** son inhábiles salvo
   actuaciones declaradas urgentes (art. 183 LOPJ); los términos son improrrogables salvo disposición
   expresa (art. 202 LECrim). El plazo del art. 324 es de **meses**, de fecha a fecha.
4. **Toda pena, plazo o artículo del briefing sale de `references/anclas-normativas-penal.md`** o se
   verifica en el acto con `buscar_articulo`. Lo demás va marcado `[verificar]`.
5. **Pre-flight check** del conector `jurisprudenciator` antes de citar jurisprudencia nueva.
   Prohibido inventar ECLI, ROJ, fechas, ponentes o fundamentos.
6. **La ley aplicable se comprueba en cada briefing**, no solo en el intake: si los hechos son
   anteriores al 10-4-2026, la comparación de penas del art. 2.2 CP es una cuestión abierta hasta que
   conste hecha.
7. **No narrar acciones del plugin** ("estoy leyendo history.md..."). Solo el briefing limpio.
8. **El briefing puede contener nombres** (es un documento de trabajo bajo secreto profesional), pero
   **nunca DNI, domicilios ni antecedentes penales reales**, y **nunca** se vuelca su contenido
   identificativo a `_log.yaml`. Art. 10 RGPD.
