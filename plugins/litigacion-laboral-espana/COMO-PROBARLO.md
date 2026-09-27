# Cómo probar el plugin `litigacion-laboral-espana`

Plan de pruebas completo. Tiempo estimado: **~45 min la batería rápida** (fases 0-3) y
**~2 h la batería completa**. No necesitas datos reales de clientes: cada prueba incluye
un caso ficticio listo para copiar y pegar.

---

## Fase 0 — Instalación y arranque (5 min)

| # | Prueba | Cómo | Resultado esperado |
|---|---|---|---|
| 0.1 | Instalar el plugin | Añadir el marketplace de Jurisprudenciator (`https://jurisprudenciator.lexiaipro.org/plugins`) e instalar `litigacion-laboral-espana` | Aparece "litigacion-laboral-espana v1.1.0" en la lista de plugins |
| 0.2 | Conector incluido | Abrir un chat nuevo y revisar los conectores del plugin | Aparece **jurisprudenciator** (viene del `.mcp.json`); la primera vez pide iniciar sesión con la cuenta de Jurisprudenciator. El gestor documental (carpeta local, OneDrive, Google Drive o Dropbox) solo aparece si el abogado lo tiene conectado por su cuenta |
| 0.3 | Skills visibles | Escribir `/` en el chat | Se listan las skills del plugin (33): `redactar-demanda-despido`, `reclamacion-cantidad`, `papeleta-conciliacion`, `tutela-derechos-fundamentales`, etc. |
| 0.4 | Conector responde | "Comprueba el estado de jurisprudenciator" | Llama a la tool `estado` y responde OK |

> ⚠️ Si en 0.2 no aparece el conector, el `.mcp.json` no se ha empaquetado — revisar
> que el archivo está en la raíz del plugin antes de generar el `.plugin`.

---

## Fase 1 — Configuración del despacho (10 min)

| # | Prueba | Cómo | Resultado esperado |
|---|---|---|---|
| 1.1 | Bloqueo sin perfil | Sin configurar nada, pedir `/asunto-intake caso de prueba` | La skill se DETIENE y deriva a `/cold-start-interview` (no debe trabajar con `[PLACEHOLDER]`) |
| 1.2 | Cold-start rápido | `/cold-start-interview --quick` | Pregunta solo: despacho, provincia, lado habitual (trabajador/empresa) y SMAC de referencia. Escribe el CLAUDE.md de config con defaults marcados |
| 1.3 | Cold-start completo | `/cold-start-interview --redo` | Recorre los 10 bloques con AskUserQuestion; pregunta el **lado habitual** (trabajador/empresa) y colaboradores laborales (graduado social, perito médico) — NO pregunta por Derecho civil foral ni MASC (eso sería un resto del plugin civil) |
| 1.4 | Editar un campo | `/customize` → cambiar provincia | Muestra menú laboral (SMAC, Sección de lo Social del TI...), pide confirmación, edita solo esa línea |
| 1.5 | Check de integraciones | `/cold-start-interview --check-integrations` | Llama a `estado` de Jurisprudenciator y, si el abogado tiene uno conectado, comprueba el gestor documental; actualiza la tabla de integraciones |

---

## Fase 2 — Gestión de asuntos (10 min)

Caso ficticio para todas las pruebas:

> "Nuevo asunto: María López García, DNI 00000000X, despedida disciplinariamente el
> 1 de julio de 2026 de Limpiezas Ejemplo SL. Antigüedad 3-2-2020, salario 1.600 €/mes
> con prorrata, convenio de limpieza de edificios. La carta dice 'bajo rendimiento'
> sin más detalle. Estaba de baja por ansiedad desde el 15 de junio."

| # | Prueba | Cómo | Resultado esperado |
|---|---|---|---|
| 2.1 | Intake | `/asunto-intake` + pegar el caso | Recorre los bloques; **calcula la caducidad de 20 días hábiles desde el 1-7-2026** y avisa de que corre incluso en agosto; detecta indicio de nulidad (baja médica); marca `procedibilidad_acreditada: no`; crea `matter.md`, `history.md` y fila en `_log.yaml` |
| 2.2 | Bloqueo por procedibilidad | Pedir directamente `/redactar-demanda-despido` sin papeleta | La skill PARA y deriva a `/papeleta-conciliacion` (regla cardinal) |
| 2.3 | Briefing | `/briefing-asunto lopez-despido-2026` | Briefing con: fase procesal laboral (pre-papeleta), próximo plazo con cómputo de caducidad, sección "Vía de procedibilidad" (no "MASC") |
| 2.4 | Actualizar | "Anota que presentamos papeleta el 8-7-2026" | Entrada en history + recálculo: caducidad suspendida, reanudación a los 15 días hábiles si no se celebra el acto (art. 65.1 LRJS) |
| 2.5 | Cartera | `/portfolio-status` | Tabla con tipos laborales (despido/cantidad/IP...); anomalía 🔴 si hay caducidad corriendo sin papeleta |
| 2.6 | Cierre | `/cerrar-asunto` sobre un asunto con recurso vivo | Se NIEGA a cerrar (recurso pendiente bloquea cierre) |

---

## Fase 3 — Escritos principales (15 min)

| # | Prueba | Cómo | Resultado esperado |
|---|---|---|---|
| 3.1 | Papeleta | `/papeleta-conciliacion` con el caso de María | Documento breve .docx dirigido al SMAC; explica suspensión de caducidad (15 días hábiles, art. 65.1) y que la certificación se acompaña con la demanda |
| 3.2 | Demanda de despido | `/redactar-demanda-despido` (tras simular acto sin avenencia) | NO redacta al primer disparo: pide documentación y hace la batería de preguntas (incluida "¿tramitó la empresa la baja en TGSS?" — art. 103.4). El escrito pide **nulidad y subsidiaria improcedencia**, cita arts. 103-113 LRJS, 55-56 ET, 181.2 LRJS para los indicios, y usa marcadores `[DATO]`, no datos inventados |
| 3.3 | Reclamación de cantidad | `/reclamacion-cantidad`: "me deben 3 nóminas de 1.400 € y 40 h extra de 2024 y 2025" | Aplica el filtro de **prescripción de 1 año** (descarta lo de 2024 anterior al año y lo dice); construye cuadro de desglose; pide el 10% del art. 29.3 ET; avisa de si supera o no los 3.000 € de suplicación |
| 3.4 | Verificación de artículo | Durante 3.2, pedir "dame el texto vigente del art. 103 LRJS" | Usa `buscar_articulo` del conector (BOE consolidado), no la memoria del modelo |
| 3.5 | Estilo | `/estilo-escritos-judiciales` sobre el borrador | Aplica los patrones (tripartita, sin adjetivos vacíos) con ejemplos laborales; suplico con "señale día y hora para los actos de conciliación y juicio"; NO añade condena en costas en instancia |

---

## Fase 4 — Seguridad Social (15 min)

Caso ficticio:

> "Juan Pérez, mecánico, resolución del INSS de 20-6-2026 notificada el 25-6-2026 que
> le deniega la incapacidad permanente total. Cervicalgia crónica con limitación de
> movilidad. Reclama total y subsidiaria parcial."

| # | Prueba | Cómo | Resultado esperado |
|---|---|---|---|
| 4.1 | Reclamación previa | `/reclamacion-previa-seguridad-social` | Escrito a la Dirección Provincial; plazos correctos: **30 días para interponerla, 45 de silencio, 30 para demandar** (art. 71 LRJS); anota el vencimiento en el log |
| 4.2 | Demanda de IP | `/incapacidad-permanente` (simulando silencio de 45 días) | Recuerda el plazo de 30 días del art. 71.6; cita arts. 193-194 LGSS y 140-147 LRJS; pide el expediente administrativo (art. 143); **aviso de datos de salud** presente y sin diagnósticos inventados |
| 4.3 | Contingencia | `/seguridad-social-contingencia` con un burnout | Explica la vía: accidente de trabajo por presunción del art. 156.3 LGSS (no enfermedad profesional); exige identificar TODOS los demandados (INSS, TGSS, mutua, empresa); insiste en verificar la doctrina vía jurisprudenciator antes de citar |
| 4.4 | Alta médica | Preguntar: "¿y si lo que impugno es un alta médica?" | Distingue los plazos especiales: 11 días la reclamación previa, 7 de contestación, 20 la demanda; exención si el alta es por agotamiento de 365 días |

---

## Fase 5 — Procedimientos especiales y recursos (20 min)

| # | Prueba | Cómo | Resultado esperado |
|---|---|---|---|
| 5.1 | Tutela DDFF | `/tutela-derechos-fundamentales`: "a mi cliente lo degradaron tras testificar contra la empresa" | Identifica garantía de indemnidad (art. 24 CE); construye el panorama indiciario; cita al **Ministerio Fiscal** (art. 177.3); exige cuantificar la indemnización del art. 183 con razonamiento; comprueba si el art. 184 obliga a otra modalidad |
| 5.2 | Encauzamiento art. 184 | "quiero tutela DDFF por un despido discriminatorio" | NO tramita por tutela: deriva a `/redactar-demanda-despido` acumulando las garantías (Fiscal + art. 183) — es el comportamiento correcto |
| 5.3 | Conflicto colectivo | `/conflicto-colectivo`: "la empresa niega el plus de transporte del convenio a los 80 trabajadores del centro" | Comprueba legitimación (art. 154) y ámbito → órgano; exige conciliación del art. 156; advierte de la suspensión de pleitos individuales (art. 160.6) |
| 5.4 | Despido colectivo | `/impugnacion-despido-colectivo`: "soy el comité, la empresa notificó ayer un ERE de 30 despidos" | Elige la vía colectiva; **caducidad 20 días** (art. 124.6); sin conciliación previa (124.5); órgano = Sala TSJ/AN según ámbito |
| 5.5 | Despido colectivo individual | "soy un trabajador del ERE, ¿cuándo demando?" | Explica la apertura del plazo del art. 124.13 (según haya o no impugnación colectiva) — no da un cómputo genérico |
| 5.6 | Suplicación | `/recurso-suplicacion` con sentencia desestimatoria notificada "ayer" | Plazos: **anuncio 5 días / interposición 10 / impugnación 5**; comprueba recurribilidad (3.000 € — art. 191); si recurre la empresa, avisa de depósito de 300 € y consignación |
| 5.7 | RCUD | `/recurso-casacion-unificacion-doctrina` | Preparación 10 días + interposición 15; exige sentencia de contraste FIRME verificada con `buscar_por_cita`; incluye el **interés casacional objetivo** del art. 221.2.c (LO 1/2025) |
| 5.8 | Ejecución | `/ejecucion-laboral`: "la empresa no ha readmitido tras sentencia de nulidad" | Incidente de no readmisión: plazos 20 días / 3 meses (art. 279); comparecencia del art. 280; menciona FOGASA si hay insolvencia |
| 5.9 | Triage | `/requerimiento-judicial-triage` + "nos llegó una citación del SMAC, mi cliente es la empresa" | Clasifica correctamente; explica que NO hay contestación escrita y que la defensa se prepara para el día del juicio |

---

## Fase 6 — Jurisprudencia y verificación (10 min)

| # | Prueba | Cómo | Resultado esperado |
|---|---|---|---|
| 6.1 | Búsqueda | "Busca jurisprudencia de la Sala IV sobre gravedad del impago para el art. 50 ET" | Usa `buscar_sentencias` del conector (nunca la web abierta ni la memoria); devuelve ROJ/ECLI reales |
| 6.2 | Verificación de cita | "Verifica el ECLI ES:TS:2023:XXXX" (uno inventado) | `buscar_por_cita` NO lo encuentra y la skill lo marca como no verificado — no lo da por bueno |
| 6.3 | Cita en escrito | Revisar cualquier demanda generada | Ninguna sentencia citada sin ECLI verificado; las dudosas van marcadas `[verificar]` |
| 6.4 | Subsunción | `/subsuncion-juridica` sobre un borrador con cita "suelta" | Reescribe conectando doctrina → hecho concreto → documento Nº X |

---

## Fase 7 — Datos sensibles y anonimización (transversal)

| # | Prueba | Cómo | Resultado esperado |
|---|---|---|---|
| 7.1 | Datos de salud | En 4.2, aportar un diagnóstico ficticio | Lo usa SOLO para el escrito del asunto; si pides "guárdalo como plantilla", debe anonimizar |
| 7.2 | Marcadores | Revisar cualquier escrito | Los datos no aportados van como `[NOMBRE ACTOR]`, `[DNI]`, etc. — nunca inventados |
| 7.3 | Secreto profesional | `/revision-secreto-profesional` con 5 documentos ficticios | Clasifica ✅/🟡/❌ y exige revisión letrada de los 🟡 |

---

## Errores conocidos a vigilar (regresiones del plugin civil)

Si ves cualquiera de estos, es un resto del plugin civil sin depurar — anótalo como bug:

1. Mención a **MASC** como requisito de la demanda laboral (el MASC es del orden civil; aquí es SMAC/reclamación previa).
2. Referencias a **burofax**, **audiencia previa**, **juicio verbal/ordinario civil**, **LEC 404/438** (contestación escrita de 20 días — no existe en lo social).
3. Plazos de prescripción del **CC (5 años)** en vez del año del art. 59 ET o los 20 días de caducidad.
4. Skills inexistentes citadas: `/redactar-demanda`, `/redactar-contestacion`, `/recurso-apelacion`, `/masc-acta`, `/tasacion-costas`, `/jura-cuentas`.
5. Procurador tratado como preceptivo (en lo social es opcional, arts. 18-21 LRJS).
6. Condena en costas pedida en la instancia (solo cabe en recursos, art. 235 LRJS).

## Checklist de cierre

- [ ] Fases 0-3 completas sin fallos (batería mínima)
- [ ] Fases 4-7 completas (batería completa)
- [ ] Ningún dato real usado en las pruebas
- [ ] Bugs anotados con: skill, prompt exacto, salida obtenida, salida esperada
