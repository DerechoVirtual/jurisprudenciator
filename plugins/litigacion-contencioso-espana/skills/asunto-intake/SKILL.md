---
name: asunto-intake
description: Intake de un nuevo asunto contencioso-administrativo. Recoge identificación, conflictos, acto impugnado, agotamiento de la vía previa, plazo de caducidad del art. 46 LJCA, órgano y procedimiento, triage de riesgo y expediente. Usar con nuevo asunto o intake este asunto.
---

# Intake de asunto — Litigación contencioso-administrativa

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Caducidad del bloque 6 y umbrales de procedimiento, apelación y competencia** → `buscar_articulo` (`ley="LJCA"`, artículos 8, 46, 78 y 81) cuando el dato no esté en las anclas.
- **Plazos de la vía previa y prescripción de la responsabilidad patrimonial** → `buscar_articulo` (`ley="LPAC"`, artículos 67, 122 y 124).
- **Cliente, contraparte o adjudicatario que es una sociedad** (conflictos, legitimación, acuerdo corporativo) → `buscar_empresa_mercantil` (denominación o CIF).
- **Asunto ligado a un inmueble** (urbanismo, expropiación, IBI, plusvalía, ruina, responsabilidad viaria) → `consultar_catastro` (referencia catastral o dirección; `callejero_catastro` si la vía no casa) para fijar referencia, superficie y uso.
- **Acto municipal fundado en una ordenanza** (sanción, licencia, tributo local) → `buscar_ordenanzas` + `leer_ordenanza` con `articulo`.
- **Primera valoración de la tesis** → `buscar_sentencias` (`jurisdiccion="CONTENCIOSO"`; `base="TS"`, o `base="AN"` con `provincia` para el criterio del TSJ o de los juzgados). En el intake solo se busca; se leen únicamente las resoluciones que se vayan a citar.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, criterio del TEAC...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- "Nuevo asunto", "intake", "abrir asunto", "vamos a empezar con este caso"
- Cuando llega una **notificación de un acto administrativo** que el cliente quiere recurrir
- Cuando se agota la vía administrativa y hay que decidir si se va al contencioso
- Tras `/requerimiento-judicial-triage` cuando el triage escala a asunto
- Cuando el despacho defiende a la Administración y se le notifica un recurso interpuesto

## Prerrequisito

`~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/CLAUDE.md` debe estar configurado. Si no, parar y derivar a `/cold-start-interview`.

> ⛔ **Aquí no hay MASC.** El intento de MASC de la LO 1/2025 es requisito de procedibilidad del orden **civil**. En contencioso **no existe**. Lo que sí se rastrea, y bloquea, es el **agotamiento de la vía administrativa** (art. 25.1 LJCA).

## Flujo

### Bloque 1: Identificación

Vía `AskUserQuestion`:
- **Nombre corto del asunto** → slug con patrón `descriptor-materia-año`. **Sin nombre del cliente** (ver `PROTECCION-DATOS.md`).
- **Cliente** — se registra en `matter.md`, nunca en el slug ni en el nombre del asunto.
- **Tipo de asunto:** sancionador / urbanismo / responsabilidad-patrimonial / personal-función-pública / tributario-local / extranjería / contratación-pública / subvenciones / expropiación / seguridad-social / otros
- **Administración demandada:** estatal / autonómica (indicar CCAA) / local (indicar entidad) / institucional — **más el órgano concreto autor del acto**.

### Bloque 2: Conflictos

Comprobar contra el método configurado en CLAUDE.md:
- ¿Es el cliente actual o de los últimos 5 años?
- ¿Se defiende habitualmente a esa Administración en otros asuntos? (conflicto duro si el despacho la asiste)
- ¿Hay codemandados o interesados personados que sean clientes? (aseguradora, adjudicatario, tercero beneficiado por el acto)
- Si cualquier conflicto: detener intake y avisar. Si es soft, registrar y seguir.

### Bloque 3: Fuente y encargo

- ¿Cómo llega el cliente? (recomendación / web / turno de oficio / colaborador)
- ¿Hoja de encargo firmada? Si no, recordar firmar antes de actos procesales (`/hoja-encargo`).
- ¿Provisión de fondos? Cuantía + cobrada o pendiente.
- Advertir del tope de costas: **1/3 de la cuantía del proceso** por cada favorecido; cuantía indeterminada = **18.000 €** a estos solos efectos (art. 139.4 LJCA).

### Bloque 4: Acto impugnado — el dato del que cuelga todo

- **Acto impugnado:** identificación exacta (órgano, referencia, fecha del acto).
- **Naturaleza:** acto expreso / acto presunto (silencio) / disposición general / inactividad (art. 29) / vía de hecho (art. 30).
- **`fecha_notificacion`** — fecha de notificación o publicación. **Es el dato crítico del intake.** Si el cliente no la recuerda, pedir el justificante de notificación antes de seguir; sin ella no se puede calcular la caducidad.
- **¿Pone fin a la vía administrativa?** (art. 25.1 LJCA). Si es acto de trámite, comprobar si es **cualificado** (decide el fondo, impide continuar, produce indefensión o perjuicio irreparable).
- ¿Es firme y consentido, o confirmatorio de otro anterior no recurrido? → riesgo de inadmisión (art. 69.c LJCA).

### Bloque 5: Vía administrativa previa

**`via_previa`:** agotada / pendiente-alzada / pendiente-reposición / no-procede

- **Alzada** (arts. 121-122 LPAC): **1 mes** si el acto es expreso; **en cualquier momento** si es presunto. Resolución en 3 meses; silencio negativo.
- **Reposición** potestativa (arts. 123-124 LPAC): **1 mes** si el acto es expreso; **en cualquier momento** si es presunto. Resolución en 1 mes; silencio negativo.
- Si la vía **no está agotada** y cabe alzada: marcar `via_previa: pendiente-alzada` y derivar a `/recurso-alzada-reposicion-ca`. **El contencioso no se puede interponer todavía.**

> ⚠️ **Errata frecuente:** el plazo de **3 meses** para recurrir el acto presunto era el art. 115.1 de la derogada **Ley 30/1992**. Desde la Ley 39/2015 se recurre **«en cualquier momento»**. No citar nunca 3 meses.

### Bloque 6: Plazo de caducidad — calcular AHORA

**`fecha_caducidad_interposicion`** — art. 46 LJCA:

| Supuesto | Plazo | Desde |
|---|---|---|
| Acto expreso que agota la vía | **2 meses** | Día siguiente a la notificación/publicación |
| Acto presunto | **6 meses** | Día siguiente a producirse el acto presunto |
| Disposición general | **2 meses** | Día siguiente a la publicación |
| Tras reposición (expresa o presunta) | **2 meses** | Día siguiente a la notificación o a la desestimación presunta (art. 46.4) |
| Inactividad (art. 29) | **2 meses** | Día siguiente al vencimiento de los plazos del art. 29 |
| Vía de hecho **con** requerimiento | **10 días** | Día siguiente al fin del plazo del art. 30 |
| Vía de hecho **sin** requerimiento | **20 días** | Día en que se inició la actuación material |
| Lesividad | **2 meses** | Día siguiente a la declaración de lesividad |

- **Agosto** (art. 128.2 LJCA): **no corre** ningún plazo de la LJCA — **salvo derechos fundamentales, donde agosto SÍ es hábil**. Aplicarlo al cálculo y decirlo.
- Aplicar el **margen de seguridad interno** del CLAUDE.md y anotar la fecha de presentación objetivo, no solo la de vencimiento.
- Si es **responsabilidad patrimonial** aún en vía administrativa: la reclamación prescribe en **1 año** (art. 67 LPAC); en daños físicos o psíquicos el año corre desde la **curación o la determinación del alcance de las secuelas**.

> ⚠️ **Es caducidad, no prescripción.** No se interrumpe con burofax, reclamación extrajudicial ni requerimiento. Vencido el plazo, el acto es firme y consentido y el recurso se inadmite (art. 69.e LJCA). Si el plazo está vencido o al límite, **decirlo antes de aceptar el encargo**.

### Bloque 7: Posición procesal, órgano, procedimiento y cuantía

- **`side`:** recurrente / demandada (Administración) / codemandado (aseguradora, interesado, adjudicatario)
- **`cuantia`** + **`cuantia_determinada`** ("sí" / "no"). Decide dos cosas:
  - **Procedimiento abreviado:** cuantía **≤ 30.000 €** (art. 78.1 LJCA), o por materia: **personal** al servicio de las AAPP, **extranjería**, inadmisión de peticiones de **asilo político** y **disciplina deportiva en dopaje**. El tráfico **no** es materia de abreviado: entra por cuantía.
  - **Apelabilidad:** excluida por cuantía si **≤ 30.000 €** (art. 81.1.a LJCA). Advertir al cliente al intake: puede no haber segunda instancia.
- **`procedimiento`:** ordinario / abreviado / DDFF / otro
  - **DDFF** (arts. 114-121 LJCA): interposición en **10 días** (art. 115.1) y **agosto hábil**. Si el asunto tiene componente de derecho fundamental, valorarlo aquí — el plazo es brutalmente corto.
- **`organo`:** Juzgado CA nº [X] de [lugar] / Sala TSJ / AN / TS. Verificar competencia objetiva (art. 8 LJCA): entidades locales (excluido el planeamiento urbanístico), CCAA en personal y sanciones **≤ 60.000 €** y responsabilidad patrimonial **≤ 30.050 €**, Administración periférica del Estado (se exceptúan actos **> 60.000 €**), extranjería.
- Si es demandada la Administración y el despacho actúa como recurrente, anotar quién ostenta su representación (Abogacía del Estado / Letrado de la CCAA / Letrado consistorial).

### Bloque 8: Representación y defensa — art. 23 LJCA

- **Juzgados (unipersonales):** procurador **potestativo**; abogado siempre preceptivo. Si se confiere la representación al abogado, a él se le notifican las actuaciones.
- **Salas (TSJ, AN, TS):** procurador **preceptivo** + abogado.
- **Funcionarios** en defensa de sus derechos estatutarios: pueden comparecer **por sí mismos** (salvo separación de inamovibles), con uso obligatorio de sistemas electrónicos.
- Decidir y registrar `procurador` (o `no-designado` si es potestativo y no se designa).

> ⚠️ No aplicar el art. 23 **LEC** (regla civil de los 2.000 € y el monitorio). Es otra norma y otra jurisdicción.

### Bloque 9: Documentos del art. 45.2 LJCA

Comprobar al intake, porque su falta es la causa de inadmisión más frecuente y evitable:
- a) Documento acreditativo de la **representación**.
- b) Documento acreditativo de la **legitimación** cuando derive de transmisión (herencia u otro título).
- c) Copia o traslado del **acto impugnado**, o indicación del expediente o del diario oficial.
- d) ⚠️ **Personas jurídicas: acuerdo corporativo** — documento que acredite el cumplimiento de los requisitos para entablar acciones según sus normas o estatutos. **No basta el poder.** Verificar SIEMPRE que existe acuerdo del órgano competente.
- e) **Sindicatos** ex art. 19.1.k): acreditación de la afiliación, de la comunicación al afiliado y de su **autorización expresa**.

Subsanación: **10 días** (art. 45.3 LJCA); si no, el órgano se pronuncia sobre el archivo.

### Bloque 10: Expediente administrativo

**`expediente_administrativo`:** no-reclamado / reclamado / recibido / incompleto-ampliación-pedida

- Se reclama al órgano autor del acto al admitirse el recurso (art. 48.1 LJCA); remisión en **20 días improrrogables** (art. 48.3).
- Si no llega: reiteración y **multas coercitivas de 300 a 1.200 €** cada 20 días a la autoridad responsable (art. 48.7).
- ¿Tiene ya el cliente copia del expediente de la vía administrativa? Pedirla — permite trabajar antes de que llegue el judicial.

### Bloque 11: Medida cautelar

**`medida_cautelar`:** no-pedida / pedida / concedida / denegada

- Valorar al intake: ¿la ejecución del acto puede hacer **perder su finalidad legítima al recurso** (art. 130.1 LJCA)?
- Solicitable en **cualquier estado del proceso** (art. 129), en **pieza separada** (art. 131).
- Si hay especial urgencia, valorar **cautelarísima** inaudita parte (art. 135) — decidirlo ahora, no después.
- Si el acto es una sanción con ejecutividad inminente o una orden de demolición, marcar como cuestión de primer orden y derivar a `/medidas-cautelares-ca`.

### Bloque 12: Triage de riesgo y materialidad

Aplicar matriz severidad × probabilidad del CLAUDE.md:
- Severidad y probabilidad (alta/media/baja) según las bandas configuradas.
- Etiqueta resultante (Crítico / Prioritario / Rutina / Vigilar) → `_log.yaml`: critico / alto / medio / bajo.
- **Materialidad:** cuantía relativa al cliente, relación con el cliente, impacto reputacional o en su actividad (una clausura o una inhabilitación pesan más que su cuantía).

### Bloque 13: Conservación documental

- ¿Riesgo de pérdida de prueba? (comunicaciones con la Administración, justificantes de notificación, informes técnicos, partes médicos).
- Marcar `conservacion_documental: pending` para que `/conservacion-documental --emitir` genere la comunicación al cliente.

### Bloque 14: Posición inicial

- **Tesis del asunto** en 2-3 frases (la "historia" que vamos a contar).
- **Motivos de impugnación** candidatos: incompetencia, vicio de procedimiento, desviación de poder, falta de motivación, error en la valoración, proporcionalidad de la sanción, prescripción o caducidad del procedimiento administrativo.
- **Puntos débiles ya identificados** (empezando por los de admisibilidad, art. 69 LJCA).
- Cuestión jurídica central en una línea.

## Salida

1. Crear carpeta `~/.claude/plugins/config/derecho-virtual/litigacion-contencioso-espana/matters/<slug>/`
2. Escribir `matter.md` con:
   - Cabecera `RESERVADO Y CONFIDENCIAL — SECRETO PROFESIONAL DEL ABOGADO`
   - Datos identificativos y **administración demandada + órgano autor**
   - **Acto impugnado + fecha de notificación**
   - **Vía previa y su estado**
   - **Plazo de caducidad calculado** (con el cómputo escrito, no solo la fecha)
   - Órgano judicial, procedimiento y cuantía
   - Hechos, pretensión y motivos de impugnación
   - Estado del expediente administrativo
   - Medida cautelar
   - Triage de riesgo · Tesis inicial · Representación · Próximos pasos
3. Crear `history.md` con primera entrada `[AAAA-MM-DD] INTAKE — asunto creado.`
4. Crear subcarpetas `escritos/`, `jurisprudencia/`
5. Añadir fila a `matters/_log.yaml`:

```yaml
- slug: sancion-trafico-2026
  name: Sanción de tráfico — recurso contra resolución del Ayuntamiento
  status: open
  side: recurrente
  risk: medio
  type: sancionador
  cliente: "[CLIENTE]"
  administracion_demandada: local — [ÓRGANO] del [AYUNTAMIENTO]
  acto_impugnado: Resolución sancionadora exp. [EXPEDIENTE] — multa y detracción de puntos
  fecha_notificacion: 2026-05-04
  via_previa: agotada
  fecha_caducidad_interposicion: 2026-07-04  # 2 meses, art. 46.1 LJCA — confirmado en doble control
  procedimiento: abreviado   # cuantía ≤ 30.000 €, art. 78.1 LJCA
  organo: Juzgado CA nº [X] de [LUGAR]
  cuantia: 500
  cuantia_determinada: "sí"
  expediente_administrativo: no-reclamado
  medida_cautelar: no-pedida
  procurador: no-designado   # potestativo ante Juzgados, art. 23.1 LJCA
  representacion_administracion: "[ÓRGANO] — letrado consistorial"
  next_deadline: 2026-06-26  # presentación objetivo: margen de seguridad sobre la caducidad
  materiality: baja
  related_matters: []
  conservacion_documental: pending
  opened: 2026-05-13
  last_updated: 2026-05-13
  notas: "Vía agotada. Abreviado: se inicia por demanda (art. 78.2 LJCA), no por escrito de interposición. Apelación excluida por cuantía (art. 81.1.a) — advertido al cliente."
```

> **YAML:** entrecomillar los valores `"sí"` / `"no"` de `cuantia_determinada`. Sin comillas, `no` se interpreta como el booleano `false`.

6. Si workspaces de asunto están habilitados (default sí), preguntar: "¿Hacer este asunto el activo?" Si sí, escribir en CLAUDE.md → `## Workspaces de asuntos` → `Asunto activo: <slug>`.

## Reglas

1. **NUNCA crear asunto sin chequeo de conflictos.** Si hay conflicto duro, parar.
2. **Calcular la caducidad en el intake, no después.** Es el dato que decide si el asunto tiene sentido aceptar. Sin `fecha_notificacion` no hay intake completo: pedirla y bloquear.
3. **Es caducidad, no prescripción.** No hay interrupción por reclamación extrajudicial. No citar los arts. 1964/1968/1969 CC: son de otra jurisdicción.
4. **Vía previa sin agotar bloquea el contencioso** (art. 25.1 LJCA). Si cabe alzada, primero la alzada.
5. **Nunca exigir MASC.** Si una skill lo pide en un asunto contencioso, es contaminación del fork civil: ignorarlo y avisar.
6. **Agosto:** art. 128.2 LJCA — no corre ningún plazo de la LJCA, **salvo DDFF, donde agosto es hábil**. No citar el art. 133 LEC.
7. **Abreviado:** se inicia **por demanda** (art. 78.2 LJCA), no por escrito de interposición. No hay plazo de 20 días del art. 52.1 en abreviado.
8. **Datos personales:** el slug y el `name` no llevan nombre del cliente. En `_log.yaml`, terceros con marcadores `[CLIENTE]`, `[PROCURADOR]`, `[ÓRGANO]`. Nunca DNI, IBAN, direcciones ni teléfonos.
9. **Fechas en formato AAAA-MM-DD.** Convertir relativas ("la semana que viene") a absolutas.
10. **No inventar plazos ni umbrales.** Fuente única: `references/anclas-normativas-ca.md`. Lo que no esté ahí, se verifica con `buscar_articulo` o se marca `[verificar]`.
