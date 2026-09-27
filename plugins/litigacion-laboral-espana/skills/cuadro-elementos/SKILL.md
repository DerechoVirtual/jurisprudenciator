---
name: cuadro-elementos
description: Cuadro de elementos de la accion o excepcion. Una fila por elemento juridico a probar con articulo, hecho del caso, prueba y estado. Deteccion de gaps. Usar con cuadro de elementos o que nos falta para probar.
---

# Cuadro de elementos

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Columna «Artículo»: precepto vigente de cada elemento** (ET, LRJS, LGSS, Ley 20/2007) → `buscar_articulo`.
- **Elementos que dependen del convenio** (categoría, salario regulador, pluses, jornada) → `buscar_convenio` + `leer_convenio` (`articulo` o `buscar_en`).
- **Elementos sostenidos por jurisprudencia** («Art. X + STS [ECLI]», regla 2) → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; `base="TC"` para indicios de vulneración de derechos fundamentales) + `leer_sentencias` (`parrafos=3`) y `buscar_por_cita`.
- **Condición de empleador, grupo de empresas o sucesión** (legitimación pasiva) → `buscar_empresa_mercantil`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces; si sigue sin resultado, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

## Cuándo activar

- "Qué nos falta para probar [acción]"
- "¿Tenemos los elementos?"
- "Cuadro de elementos", "element chart", "matriz de prueba"
- Antes de redactar la demanda o de preparar la oposición oral
- En preparación del acto del juicio (art. 85 LRJS)

## Variantes

- `--ofensivo` (default si side=actor): para sostener pretensión propia
- `--defensivo` (default si side=demandado): para rebatir pretensión contraria
- `--cruzado`: cuando hay reconvención (ambos)

## Marco

### Acciones laborales habituales y sus elementos

| Acción | Elementos (resumen) |
|---|---|
| Despido improcedente (arts. 55-56 ET; 103-113 LRJS) | (1) Relación laboral (antigüedad, salario, categoría), (2) Despido con fecha de efectos, (3) Inexactitud/insuficiencia de la causa alegada o defectos formales de la carta, (4) Acción viva (caducidad 20 días + conciliación acreditada), (5) Cálculo de indemnización (salario regulador × antigüedad) |
| Despido nulo (art. 55.5 ET; 108.2, 122.2 LRJS) | (1) Los del despido + (2) Indicio de vulneración de DDFF o causa de nulidad objetiva (embarazo, permisos, reducción de jornada...), (3) Inversión de carga: la empresa debe justificar ajenidad (art. 181.2 LRJS) |
| Extinción art. 50 ET | (1) Relación laboral vigente, (2) Incumplimiento empresarial GRAVE (impago/retrasos continuados, MSCT contra dignidad, otros graves — incl. acoso), (3) Gravedad y persistencia acreditadas, (4) Contrato vivo al ejercitar la acción |
| Reclamación de cantidad (arts. 4.2.f, 26, 29 ET) | (1) Relación laboral, (2) Concepto y periodo devengado (nóminas, convenio), (3) Falta de pago, (4) Cuantificación exacta con desglose, (5) Prescripción 1 año no vencida (art. 59.2 ET), (6) Interés por mora art. 29.3 ET |
| Incapacidad permanente (arts. 193-194 LGSS) | (1) Requisitos de afiliación/cotización según contingencia, (2) Cuadro clínico residual objetivado, (3) Limitaciones funcionales, (4) Incompatibilidad con la profesión habitual (total) o con toda profesión (absoluta), (5) Vía previa agotada (art. 71 LRJS) |
| Determinación de contingencia (arts. 156-157 LGSS) | (1) Proceso de IT/prestación en curso, (2) Hecho o exposición laboral, (3) Nexo causal (o presunción 156.3 LGSS: tiempo y lugar de trabajo), (4) Legitimados pasivos completos (INSS, TGSS, mutua, empresa) |
| Resolución contrato TRADE (Ley 20/2007) | (1) Condición TRADE (≥75% ingresos de un cliente; contrato registrado), (2) Incumplimiento grave del cliente, (3) Cuantificación de facturas/indemnización, (4) Competencia del orden social (art. 2.d LRJS) |
| Tutela DDFF (arts. 177-184 LRJS) | (1) Derecho fundamental concreto invocado, (2) Indicios de vulneración (art. 181.2), (3) Conducta/acto lesivo del empleador o tercero, (4) Daño moral cuantificado con criterio razonado (art. 183) |

## Flujo

### 1. Identificar acción / excepción

Vía `AskUserQuestion`: ¿qué acción se ejercita? ¿qué excepción se opone?

### 2. Listar elementos

Aplicar plantilla de elementos según acción (de la tabla anterior o jurisprudencia específica).

### 3. Cargar evidencia disponible

Leer:
- `matters/<slug>/matter.md` (hechos del intake)
- `matters/<slug>/cronologia.md` si existe
- Documentos del asunto

### 4. Mapping elemento ↔ prueba

Para CADA elemento:
- **Artículo** que lo sostiene (ET, LRJS, LGSS, convenio colectivo, leyes específicas)
- **Hecho concreto** del caso que materializa el elemento
- **Documento** del expediente que lo prueba (Doc Nº X, página Y)
- **Estado**: ✅ probado | 🟡 parcial | 🔴 faltante
- **Si faltante**: qué documento/prueba se necesitaría

### 5. Output

`matters/<slug>/cuadro-elementos.md`:

```markdown
# Cuadro de elementos — [slug]
**Acción:** [ej. Despido nulo, subsidiariamente improcedente (arts. 55-56 ET; 103-113 LRJS)]
**Variante:** [ofensivo / defensivo / cruzado]

| # | Elemento | Artículo | Hecho del caso | Prueba | Estado |
|---|---|---|---|---|---|
| 1 | Relación laboral (antigüedad, salario, categoría) | arts. 1, 8 ET | Alta el 15-3-2019, oficial 1ª, 1.850 €/mes con prorrata | Doc 1 (contrato) + Doc 2 (nóminas) + Doc 3 (vida laboral) | ✅ |
| 2 | Despido con fecha de efectos | art. 55 ET | Carta entregada el 30-4-2026, efectos ese día | Doc 4 (carta de despido) | ✅ |
| 3 | Insuficiencia de la causa (imputaciones genéricas) | art. 55.1 ET; 105.2 LRJS | La carta no concreta hechos ni fechas | Doc 4 + interrogatorio empresa | 🟡 (valoración judicial) |
| 4 | Indicio de nulidad (despido tras baja médica) | art. 55.5 ET; 181.2 LRJS; Ley 15/2022 | Baja por ansiedad iniciada el 12-4-2026; despido 18 días después | Doc 5 (parte de baja) + Doc 6 (WhatsApp del encargado) | 🟡 (indicio — invertir carga) |
| 5 | Acción viva (caducidad + conciliación) | art. 59.3 ET; 103, 65 LRJS | Papeleta SMAC el 8-5-2026 (día 5 de 20) | Doc 7 (papeleta sellada) | ✅ |
| 6 | Cálculo de indemnización | art. 56 ET | 33 días/año desde el alta de 15-3-2019: cuadro adjunto | Doc 2 (nóminas para salario regulador) | ✅ |

## Análisis de cobertura

- Elementos probados: 4/6
- Parciales: 2 (causa insuficiente — valoración judicial; indicio de nulidad — carga probatoria)
- Faltantes: 0

## GAPS

🔴 Ninguno crítico.
🟡 (Elemento 4) Reforzar el indicio de nulidad: pedir al cliente los mensajes completos
   y testifical de compañeros sobre comentarios del encargado tras la baja.

## Próximos pasos

1. Pedir al cliente la conversación íntegra y localizar testigos
2. Si la cobertura está completa, proceder con /redactar-demanda-despido
3. Cronología ofensiva en /cronologia para soportar narrativa de los hechos
```

### 6. Decision tree

> 1. **Si todos ✅** — proceder con `/redactar-demanda-despido`, `/reclamacion-cantidad` o la skill de demanda que toque
> 2. **Si hay 🔴 faltantes** — pedir al cliente documentación o reconsiderar viabilidad
> 3. **Si hay 🟡** — preparar prueba (testifical, pericial, interrogatorio) para el acto del juicio

## Reglas

1. **Pin-cite por cada celda.** Hecho del caso + documento concreto. Sin pin-cite, no se considera probado.
2. **Si la jurisprudencia sostiene un elemento (ej. doctrina de la Sala IV sobre indicios en tutela DDFF)**, añadir al artículo: "Art. X + STS [ECLI]".
3. **GAPS son la salida prioritaria.** El propósito del cuadro es detectar lo que falta, no presumir lo que hay.
4. **Conservador en el estado.** Si dudoso, ✅ → 🟡. Si claramente faltante, 🔴.
