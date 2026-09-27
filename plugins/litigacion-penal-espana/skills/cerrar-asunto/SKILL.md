---
name: cerrar-asunto
description: Cerrar un asunto penal. Captura el modo de terminacion (sobreseimiento libre o provisional, archivo, sentencia absolutoria o condenatoria, conformidad, prescripcion), verifica que no queda ejecutoria viva y archiva fuera de la cartera activa sin borrar. Usar con cerrar asunto o asunto terminado.
---

# Cerrar asunto — penal

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Prescripción de la pena y cancelación de antecedentes tras una condena** → `buscar_articulo` (`ley="CP"`, `articulo="133"`, `"134"` y `"136"`).
- **Costas en caso de absolución** → `buscar_articulo` (`ley="LECrim"`, `articulo="240"`).
- **Ejecutoria viva: indulto, requisitoria o edicto publicados** → `novedades_boe` (por órgano, número de procedimiento o fecha de la sentencia, nunca por el nombre del cliente; periodos de hasta 31 días) → `leer_boe`.
- **Resoluciones que se guardan como precedente en las lecciones del asunto** → `buscar_por_cita`, para archivarlas con el ECLI verificado.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- "Cerrar [slug]", "[asunto] está terminado"
- Auto firme de **sobreseimiento libre** (art. 637 LECrim) o **provisional** (art. 641 LECrim)
- Auto de **sobreseimiento provisional y archivo** por autor desconocido (art. 779.1.1.ª LECrim)
- **Sentencia absolutoria** firme
- **Sentencia condenatoria** firme **con la ejecutoria ya agotada** ← ver la regla 2
- **Conformidad** prestada y sentencia firme, con la ejecución cumplida
- **Prescripción** del delito (art. 131 CP) o de la pena (art. 133 CP) declarada
- Retirada del encargo o venia a otro compañero

> ⚠️ **Sentencia firme ≠ asunto cerrado.** Es el error estructural del cierre en penal. Ver regla 2.

## Prerrequisito

Base de asuntos en
`~/.claude/plugins/config/derecho-virtual/litigacion-penal-espana/matters/`.

## Flujo

### 1. Verificar pertinencia

- Comprobar `status: open` en `_log.yaml`. Si ya está `closed`, avisar y no duplicar.
- Si `next_deadline` está a < 14 días, preguntar dos veces.
- **Comprobar firmeza**: ¿está agotado el plazo de recurso?
  - Apelación contra sentencia de la **Sección de lo Penal**: **10 días** desde la notificación
    (art. 790.1 LECrim). Ojo: si se pidió copia de las grabaciones en los **3 días** siguientes a la
    notificación, el plazo **se reanuda** al entregarse las copias — la firmeza se corre.
  - Preparación de casación: **5 días** desde la última notificación (art. 856 LECrim).
  - Víctima contra el auto de sobreseimiento: **20 días**, aunque no se hubiera mostrado parte
    (art. 779.1.1.ª LECrim). Un sobreseimiento no es firme mientras ese plazo corra.
- **Comprobar que no hay ejecutoria viva** (ver § 6). Si la hay, **no se cierra**: `fase: ejecucion`.

### 2. Capturar modo de terminación

Vía `AskUserQuestion`:

- **Modo de terminación:**
  - **Sobreseimiento libre — art. 637 LECrim**, indicando el ordinal:
    - `637.1.º` — no existen indicios racionales de haberse perpetrado el hecho
    - `637.2.º` — el hecho no es constitutivo de delito
    - `637.3.º` — aparecen exentos de responsabilidad criminal los procesados
  - **Sobreseimiento provisional — art. 641 LECrim**, indicando el ordinal:
    - `641.1.º` — no resulta debidamente justificada la perpetración del delito
    - `641.2.º` — hay delito pero no hay motivos suficientes para acusar a persona determinada
  - **Sobreseimiento y archivo por autor desconocido** — art. 779.1.1.ª LECrim
  - **Sentencia absolutoria** firme
  - **Sentencia condenatoria** firme — **con ejecutoria agotada** (§ 6)
  - **Sentencia de conformidad** — art. 785.4 a 785.11 LECrim (abreviado) o art. 801 LECrim (juicio
    rápido ante el juzgado de guardia), con ejecución cumplida
  - **Prescripción del delito** (art. 131 CP) o **de la pena** (art. 133 CP), declarada
  - **Retirada de la acusación** (nuestra, si íbamos de acusación particular)
  - **Inhibición / acumulación a otra causa** (apuntar slug o procedimiento receptor)
  - **Renuncia o retirada del encargo** / venia a otro letrado
- **Pena finalmente impuesta** (si condena): tipo, extensión, accesorias, y si quedó **suspendida**
  (art. 80 CP) o sustituida.
- **Responsabilidad civil**: cuantía fijada, cobrada o pagada, y si la asumió una aseguradora.
- **Costas**: impuestas a la contraparte / al cliente / de oficio `[verificar el pronunciamiento
  exacto en el fallo]`.
- **Recursos pendientes**: sí (cuál, por quién) / no.
- **Antecedentes penales**: ¿la condena genera antecedente? ¿Fecha estimada de cancelación
  (art. 136 CP `[verificar plazos]`)?
- **Honorarios cobrados / pendientes.**

> **Distinción que hay que capturar bien, porque cambia el cierre:**
> el **sobreseimiento libre** cierra el asunto materialmente; el **sobreseimiento provisional** no:
> la causa puede reabrirse si aparecen nuevos elementos, **mientras el delito no haya prescrito**.
> Por eso, al cerrar por 641 o por 779.1.1.ª, se **conserva** `prescripcion_delito.fecha_estimada` en
> el log y se avisa al cliente de que el archivo no es una absolución.

### 3. Lecciones (opcional)

- Una frase: qué aprendiste del asunto.
- ¿Cambiarías algo de la estrategia con la perspectiva de hoy? (¿Se controló el art. 324 a tiempo?
  ¿Se pidieron las diligencias de descargo mientras había plazo? ¿La conformidad se negoció desde la
  posición correcta?)
- ¿Algo debe viajar al `CLAUDE.md` del despacho? (p. ej. "este instructor prorroga siempre en el
  último día: pedir la comparecencia con antelación").

### 4. Actualizar estado

#### `matters/<slug>/matter.md`

Añadir sección al final:
```
---

## Cierre — [AAAA-MM-DD]

**Modo de terminación:** [tipo + artículo y ordinal]
**Firmeza:** [fecha en que ganó firmeza + plazo de recurso agotado que lo acredita]
**Pena impuesta:** [—  / tipo y extensión] · **Suspendida (art. 80 CP):** [no / sí — plazo y condiciones]
**Responsabilidad civil:** [cuantía fijada / cobrada / pagada / aseguradora]
**Costas:** [pronunciamiento del fallo]
**Antecedentes:** [no genera / genera — cancelación estimada AAAA-MM-DD (art. 136 CP) [verificar]]
**Recursos pendientes:** [no / sí: <descripción>]
**Ejecutoria:** [no procede / agotada el AAAA-MM-DD]
**Honorarios:** [cobrados / pendientes]

**Reapertura posible:** [no (sobreseimiento libre / absolución) /
sí — sobreseimiento provisional, mientras el delito no prescriba: AAAA-MM-DD]

**Lección:** [una frase]
```

#### `matters/<slug>/history.md`

```
[AAAA-MM-DD] CIERRE — [modo de terminación + artículo]. [resumen 1-2 frases]
```

#### `matters/_log.yaml`

- `status: closed`
- `closed: AAAA-MM-DD`
- `outcome: <modo de terminación + artículo>`
- `fase: ejecucion` **si** queda ejecutoria → entonces **NO** se cierra (ver regla 2)
- `last_updated`: hoy
- **Conservar** `prescripcion_delito.fecha_estimada` si el cierre fue por sobreseimiento provisional
  o archivo: es el dato que dice cuándo el archivo se vuelve definitivo de hecho.
- Si hay recurso pendiente: **NO cerrar** — preguntar si crear sub-asunto de recurso y mantener el
  principal `stayed`.

### 5. Archivar artefactos

NO mover archivos. Quedan donde están en `matters/<slug>/` para histórico.

Si los workspaces de asunto están habilitados y el asunto cerrado era el activo, escribir
`Asunto activo: ninguno` en el CLAUDE.md de configuración.

### 6. ⚠️ Comprobación de ejecutoria — antes de cerrar cualquier condena

**Una sentencia condenatoria firme abre la ejecutoria, no cierra el asunto.** Comprobar, una por una:

- [ ] **Liquidación de condena** practicada y **aprobada**, con abono del tiempo de detención y
      prisión provisional sufridos por la misma causa.
- [ ] **Suspensión de la ejecución (art. 80 CP)**: ¿se ha resuelto? Si se concedió:
      - **plazo de suspensión** y **condiciones** impuestas → el asunto sigue vivo hasta que venza,
        porque el incumplimiento la revoca;
      - condición del **art. 80.2.3.ª**: responsabilidades civiles satisfechas o **compromiso** de
        satisfacerlas conforme a la capacidad económica, y decomiso del art. 127 hecho efectivo;
      - si los hechos son anteriores al **10-4-2026**, comprobar que se invocó la **LO 1/2026** en lo
        que favorece: no computan los antecedentes de delitos que, por su naturaleza o
        circunstancias, **carezcan de relevancia** para valorar la probabilidad de comisión de
        delitos futuros (art. 80.2.1.ª). Es un argumento nuevo (art. 2.2 CP).
      - suspensión del **art. 80.5** (dependencia de sustancias del art. 20.2.º): penas **≤ 5 años**,
        con certificación de deshabituación o tratamiento; las **recaídas no** equivalen a abandono
        salvo abandono definitivo.
      - delito perseguible previa denuncia o querella → **audiencia al ofendido** antes de conceder
        la suspensión (art. 80.6).
- [ ] **Responsabilidad civil**: fijada, requerida, ¿cobrada o pagada? ¿Embargos vivos?
- [ ] **Penas accesorias y no privativas de libertad**: trabajos en beneficio de la comunidad,
      privación del permiso de conducir, inhabilitación, prohibiciones del art. 57 CP — ¿cumplidas?
- [ ] **Multa**: ¿pagada, fraccionada, o pendiente con **responsabilidad personal subsidiaria** por
      impago? `[verificar régimen antes de citarlo]`
- [ ] **Decomiso** (art. 127 CP) ejecutado o pendiente.
- [ ] **Piezas de situación** cerradas.
- [ ] **Cancelación de antecedentes** (art. 136 CP `[verificar plazos]`): anotar la fecha estimada y
      ofrecer recordatorio al cliente. Importa: los antecedentes cancelados o que debieran estarlo
      **no computan** para la reincidencia (art. 22.8.ª CP) ni para la suspensión (art. 80.2.1.ª).

**Si queda cualquier casilla sin marcar → el asunto NO se cierra.** Se deja `status: open` con
`fase: ejecucion` y `next_deadline` en el hito vivo (revisión de la suspensión, pago pendiente,
liquidación por aprobar). Cerrar aquí es perder el control de la revocación de la suspensión, que es
donde el cliente acaba entrando en prisión.

### 7. Si el cierre implica seguimiento

- **Ejecutoria viva** → `/ejecucion-penal-liquidacion-condena-suspension-catalogo`. No se cierra.
- **Suspensión concedida** → el asunto sigue abierto hasta que venza el plazo. `next_deadline` = fin
  del plazo de suspensión.
- **Sobreseimiento provisional (art. 641) o archivo (779.1.1.ª)** → cerrar, pero conservar la fecha
  de prescripción y explicar al cliente que **no es una absolución** y que la causa puede reabrirse.
- **Sobreseimiento libre (art. 637)** → cierre material. Valorar solicitud de cancelación de la
  anotación de la causa `[verificar cauce]`.
- **Recurso que puede interponer la contraparte o el Fiscal** → no cerrar hasta que venza su plazo.
- **Cancelación de antecedentes** → ofrecer recordatorio con la fecha estimada.
- **Honorarios pendientes** → registrar en `outcome`; el asunto puede cerrarse igual.
- **Aprendizaje que toca al despacho** → proponer línea concreta y abrir `/customize`.

### 8. Output

```
✅ Asunto [slug] cerrado.

**Modo de terminación:** [tipo + artículo y ordinal]
**Firmeza:** [fecha]
**Pena:** [— / tipo y extensión] · **Suspendida:** [no / sí]
**Responsabilidad civil:** [€ / —]
**Ejecutoria:** [no procede / agotada]
**Archivado:** matters/<slug>/ (intacto, retenido en cartera con status=closed)

[Si el cierre fue por sobreseimiento provisional o archivo:]
⚠️ **Reapertura posible** mientras el delito no prescriba: [fecha estimada, art. 131 CP].
No es una absolución — comunicarlo al cliente en estos términos.

[Si hay seguimientos:]
**Pendiente:** [cancelación de antecedentes AAAA-MM-DD / honorarios]
**Sugerido:** [siguiente comando]
```

## Reglas

1. **No borrar.** Cerrar = `status: closed`. Los archivos quedan para histórico.
2. **⚠️ Sentencia firme ≠ asunto cerrado.** Toda condena abre **ejecutoria**: liquidación de condena,
   suspensión (art. 80 CP) con su plazo y condiciones, responsabilidad civil, decomiso, accesorias,
   cancelación de antecedentes. **Con la ejecutoria viva el asunto no se cierra**: `fase: ejecucion`.
   El § 6 es una comprobación obligatoria, no una sugerencia.
3. **Recurso vivo bloquea el cierre.** El asunto solo se cierra cuando es firme, y la firmeza se
   acredita con el plazo agotado: 10 días de apelación (art. 790.1 LECrim, con la reanudación por
   petición de copia de las grabaciones), 5 días de preparación de casación (art. 856), 20 días de la
   víctima contra el sobreseimiento (art. 779.1.1.ª). Si hay recurso vivo → `status: stayed` o
   sub-asunto.
4. **Sobreseimiento libre y provisional no son lo mismo y no se cierran igual.** El del art. 641 y el
   archivo del 779.1.1.ª conservan la fecha de prescripción en el log y exigen advertir al cliente de
   que la causa puede reabrirse.
5. **Verificar el artículo y el ordinal antes de escribirlos** en el `outcome`. Un cierre etiquetado
   "sobreseimiento" a secas no sirve: el ordinal del 637 o del 641 es lo que determina si hay cosa
   juzgada, si cabe reapertura y qué se le puede decir al cliente.
6. **Prohibido inventar penas, plazos o artículos.** Lo que no esté en
   `references/anclas-normativas-penal.md` se verifica con `buscar_articulo` o se marca `[verificar]`.
7. **Lecciones que viajan al despacho** se escriben al CLAUDE.md de configuración, no a la carpeta del
   asunto cerrado.
8. **El cierre no cambia el régimen de datos.** Un asunto cerrado sigue conteniendo datos del
   **art. 10 RGPD** (infracciones y condenas penales) y, si hubo condena, **antecedentes**. No se
   exporta, no se comparte y no se vuelca a `_log.yaml` nada identificativo.
