---
name: conflicto-colectivo
description: >-
  Redaccion de demanda de conflicto colectivo (arts. 153-162 LRJS) sobre interpretacion o aplicacion de norma estatal, convenio colectivo, pacto o decision empresarial de caracter colectivo SIN extinciones de contratos, incluidas MSCT colectivas y practicas de empresa. Usar con "conflicto colectivo", "interpretacion del convenio", "practica de empresa", "MSCT colectiva", "demanda del comite o sindicato". Requisito previo: la medida colectiva NO comporta extincion de puestos de trabajo. Si la empresa ha extinguido contratos por la via del art. 51 ET, el cauce es la impugnacion del despido colectivo, con caducidad de 20 dias → /impugnacion-despido-colectivo.
---

# Proceso de conflicto colectivo (arts. 153-162 LRJS)

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Texto literal del precepto controvertido del convenio y su vigencia** (denuncia, ultraactividad, convenio sucesor) → `buscar_convenio` (sector y territorio) + `leer_convenio` (`articulo` del precepto discutido) y `vigencia_convenio`.
- **Comisión paritaria y procedimiento de solución de conflictos del convenio (requisito del art. 156 LRJS)** → `leer_convenio` (`buscar_en="comisión paritaria"`).
- **Doctrina interpretativa de la Sala Cuarta y de las Salas de lo Social de la AN y de los TSJ** → `buscar_sentencias` (`jurisdiccion="SOCIAL"`, `base="TS"`; `base="AN"` para AN y TSJ) + `leer_sentencias` (`parrafos=3`, `terminos` del concepto discutido).
- **Arts. 153-162 LRJS y arts. 82-86 ET (eficacia y vigencia del convenio)** → `buscar_articulo`.
- **Empresas demandadas y posible grupo de empresas** → `buscar_empresa_mercantil`.
- **Revisión del borrador** → `verificar_escrito` con el texto completo.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, código y artículo del convenio, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Marco normativo

- **Objeto** (art. 153 LRJS): demandas que afecten a intereses generales de un **grupo genérico de trabajadores** sobre la aplicación e interpretación de una norma estatal, convenio colectivo, pactos o decisiones empresariales de carácter colectivo — incluidas las MSCT colectivas y las suspensiones/reducciones del art. 47 ET —, así como la impugnación de decisiones de descuelgue y prácticas de empresa.
- **Legitimación activa** (art. 154 LRJS): sindicatos cuyo ámbito de actuación se corresponda o sea más amplio que el del conflicto; asociaciones empresariales en conflictos de ámbito superior a la empresa; empresarios y órganos de representación (comité, delegados) en conflictos de empresa o ámbito inferior.
- **Competencia objetiva/territorial**: Juzgado de lo Social / Sección de lo Social si el conflicto no excede de la circunscripción; Sala de lo Social del TSJ si excede del ámbito de un órgano y no de la CCAA (art. 7.a LRJS); Sala de la AN si excede de una CCAA (art. 8 LRJS) — determinar el **ámbito real del conflicto** antes de elegir órgano.
- **Requisito previo** (art. 156 LRJS): intento de conciliación o mediación en los términos del art. 63 (SMAC u órgano paritario del convenio). Lo acordado en esa conciliación tiene la eficacia de un convenio colectivo si las partes ostentan legitimación suficiente.
- **Demanda** (art. 157 LRJS): además de los requisitos generales, designación **general** de trabajadores y empresas afectados y, cuando se pidan condenas de dar/hacer, los datos que permitan la ulterior individualización sin nuevo litigio.
- **Tramitación urgente y preferente** (art. 159 LRJS): preferencia absoluta salvo tutela DDFF; agosto hábil (art. 43.4).
- **Sentencia** (art. 160 LRJS): efectos de **cosa juzgada sobre los procesos individuales** pendientes o futuros de idéntico objeto (art. 160.5); ejecutable en los términos del art. 247 LRJS si es de condena cuantificable.
- **Efecto suspensivo**: la iniciación del conflicto colectivo **paraliza los pleitos individuales** de igual objeto (art. 160.6 — la suspensión se acuerda aunque esté señalado el juicio).
- Recurso: suplicación siempre (art. 191.3.f) o casación ordinaria si conoce en instancia el TSJ/AN (art. 205 ss.).

## Fase 1 — Documentación a pedir

- Norma, convenio, pacto o decisión empresarial cuya interpretación/aplicación se discute (texto literal del precepto controvertido).
- Comunicaciones de la empresa (anuncio de la medida, actas del periodo de consultas si MSCT colectiva).
- Certificación del intento de conciliación/mediación (SMAC o comisión paritaria, según el convenio).
- Datos del ámbito: centros afectados, número aproximado y grupo genérico de trabajadores.
- Acta o acuerdo del órgano que decide demandar (comité/sección sindical) — legitimación.

## Fase 2 — Batería de preguntas (AskUserQuestion)

- ¿Quién demanda? (sindicato / comité / empresa) — comprobar correspondencia entre ámbito del demandante y ámbito del conflicto (art. 154).
- ¿Ámbito territorial real del conflicto? (un centro / provincia / varias CCAA) → fija el órgano competente.
- ¿Interpretación de norma/convenio o impugnación de decisión empresarial colectiva (MSCT, descuelgue, práctica de empresa)?
- ¿El convenio establece un procedimiento propio de solución de conflictos (mediación/arbitraje paritario)? — agotarlo si es requisito.
- ¿Hay pleitos individuales en curso con el mismo objeto? (advertir suspensión, art. 160.6).
- ¿Pretensión declarativa pura o de condena? Si condena: preparar los datos de individualización (art. 157.1.a).

## Fase 3 — Estructura del escrito

1. Encabezamiento: órgano competente según ámbito, demandante colectivo con acreditación de legitimación (marcadores genéricos), demandada(s).
2. **HECHOS**: ámbito del conflicto (empresas, centros, grupo genérico de trabajadores afectados) → norma o decisión controvertida y su texto → interpretación aplicada por la empresa y controversia surgida → intento de conciliación/mediación (fecha, órgano, resultado).
3. **FUNDAMENTOS DE DERECHO**: competencia (arts. 6-8 LRJS según ámbito) → adecuación del proceso y legitimación (arts. 153-155 LRJS) → conciliación previa (art. 156) → fondo: interpretación defendida, con canon hermenéutico (arts. 3 y 1281 ss. CC; art. 82 ET para convenios) y jurisprudencia verificada.
4. **SUPLICO**: pretensión declarativa (interpretación correcta) y/o de condena colectiva, con los datos de individualización si procede.
5. **OTROSÍES**: prueba documental y, en su caso, pericial; comunicación de pleitos individuales suspendidos.

## Fase 4 — Verificación y entrega

- Doble check de legitimación y de órgano competente (los dos motivos de inadmisión más frecuentes).
- Verificar jurisprudencia interpretativa vía jurisprudenciator (Sala IV y Sala de lo Social de la AN para convenios sectoriales).
- Pulir con `/estilo-escritos-judiciales`. Entregar en Word (.docx).

---

**Nota de anonimización**: cualquier dato real de sindicato, empresa, comité o trabajadores presente en la plantilla de origen se sustituye por marcador genérico.
