---
name: burofax-draft
description: Redactar burofax saliente en Word desde el intake. Aplica filtros como sin perjuicio o MASC. Genera checklist post-envio con acuse y certificado de contenido. Usar con redactar burofax.
---

# Redacción de burofax

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Base jurídica del apartado SEGUNDO (p. ej. arts. 1100 y 1124 CC, art. 36 LAU) y mención MASC del art. 5 LO 1/2025, con su redacción vigente** → `buscar_articulo` (`ley` y `articulo` de cada precepto).
- **Destinatario sociedad: denominación exacta, CIF y domicilio social inscrito, para que el burofax llegue y acredite la notificación** → `buscar_empresa_mercantil` (por nombre o CIF).
- **Burofax sobre un inmueble (fianza, desahucio, propiedad horizontal): identificación del inmueble con su referencia catastral** → `consultar_catastro` (+ `callejero_catastro` si la dirección no casa).
- **Jurisprudencia, si se cita alguna** → `buscar_sentencias` (`jurisdiccion="CIVIL"`) + `leer_sentencias` (`parrafos=3`); si la aporta el cliente, `buscar_por_cita`.
- **Revisión del texto antes de enviarlo** → `verificar_escrito`.

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

## Cuándo activar

- Tras `/burofax-intake` con intake.md ya escrito
- "Redactar burofax", "saca el borrador"

## Prerrequisitos

- `burofaxes/<slug>/intake.md` existe y está completo

## Flujo

### 1. Leer intake

Cargar todos los campos.

### 2. Validación pre-redacción

- ¿Hay destinatario con datos completos?
- ¿Plazo razonable (mínimo 15 días, 30 si MASC)?
- ¿Pretensión concreta?
- ¿Documentos a adjuntar identificados?

Si falta algo crítico: parar y volver al intake.

### 3. Redactar Word

Estructura base (adaptar según tipo):

```
[Membrete del despacho / Logotipo si lo hay]

[Lugar y fecha]

A:
[Nombre/Razón social del destinatario]
[NIF/CIF]
[Domicilio completo]

ASUNTO: [Reclamación de cantidad / Requerimiento de cumplimiento / Cese y desistimiento /
        Devolución de fianza / Documentación MASC art. 5 Ley 1/2025]
PROCEDENCIA: Don/Doña [Cliente]

[Si MASC:] EL PRESENTE BUROFAX CONSTITUYE INTENTO DE MASC AL AMPARO DEL ART. 5 DE LA
LEY ORGÁNICA 1/2025 DE EFICIENCIA DEL SERVICIO PÚBLICO DE JUSTICIA.

[Si "sin perjuicio":] EL CONTENIDO DEL PRESENTE BUROFAX SE EFECTÚA SIN PERJUICIO Y SIN
RECONOCIMIENTO ALGUNO DE HECHOS POR PARTE DEL REMITENTE.

Muy Sr./Sra.:

Mediante el presente burofax, en nombre y por cuenta de [cliente], de quien tengo
encomendada la dirección letrada, me dirijo a usted en relación con [asunto] para
exponerle los siguientes hechos y formularle el siguiente requerimiento:

PRIMERO.- HECHOS

[Hechos del intake, redactados como narración profesional pero directa]

SEGUNDO.- BASE JURÍDICA

[Cita de artículos + interpretación + jurisprudencia si procede — sin sobrecargar]

TERCERO.- REQUERIMIENTO

En virtud de cuanto antecede, REQUIERO a usted para que en el plazo improrrogable de
[N] DÍAS HÁBILES contados desde la recepción del presente burofax, proceda a:

[Pretensión concreta: pagar la cantidad de [...] €; cumplir la obligación de [...];
cesar en [...]; devolver [...]; firmar el documento [...]]

Le advierto que el incumplimiento de este requerimiento implicará el ejercicio de las
acciones judiciales correspondientes, sin más previo aviso, incluyendo:
- Demanda [monitorio / ordinario / verbal / desahucio]
- Reclamación de intereses legales y de demora
- Reclamación de costas conforme al art. 394 LEC

[Si MASC:] Asimismo, le hago saber que este burofax sirve a los efectos del art. 5
de la LO 1/2025, quedando acreditado el intento previo de medio adecuado de solución
de controversias en caso de que su parte no atienda la presente comunicación dentro
del plazo concedido.

Sin otro particular, quedo a la espera de su respuesta dentro del plazo concedido.

Atentamente,

[Firma del cliente o del letrado, según se haya elegido en intake]
[Nombre + DNI/NIF]
[Si letrado: colegiado nº + Colegio]
```

### 4. Maquetación

- Times New Roman 11-12
- A4
- Márgenes 2,5 cm
- Justificado
- Cabecera del despacho si hay membrete
- Pie con datos de contacto

### 5. Checklist post-envío

Crear `burofaxes/<slug>/checklist.md`:

```markdown
# Checklist post-envío — Burofax [slug]

## Antes de enviar
- [ ] Verificar datos del destinatario completos
- [ ] Documentos a adjuntar listos
- [ ] Importe sellos / coste burofax calculado

## Envío
- [ ] Por Correos con ACUSE DE RECIBO + CERTIFICADO DE CONTENIDO (imprescindible)
- [ ] Fecha de envío: ____________
- [ ] Nº de seguimiento: ____________

## Post-envío
- [ ] Recoger acuse de recibo cuando llegue
- [ ] Recoger certificado de contenido
- [ ] Archivar ambos en `burofaxes/<slug>/` (escaneados o PDF)
- [ ] Anotar fecha de entrega como inicio del plazo concedido

## Vigilancia del plazo
- Fecha de entrega: ____________
- Plazo concedido: ____ días
- Vencimiento del plazo: ____________
- [ ] Si vence sin respuesta: actualizar asunto y proceder a demanda

## Si hay respuesta
- [ ] Triagear vía `/burofax-received` aplicado a la respuesta
- [ ] Decidir: aceptar / contra-oferta / demanda
```

### 6. Actualizar log

Si el burofax acredita MASC del art. 5 Ley 1/2025, y hay asunto relacionado:
- `masc_acreditado: si` en `_log.yaml`
- Apuntar fecha + slug del burofax en `matter.md` del asunto

### 7. Output

- Word .docx en `burofaxes/<slug>/burofax-v1.docx`
- Checklist en `burofaxes/<slug>/checklist.md`
- Decision tree:

> 1. **Imprimir y llevar a Correos** — recordatorio del acuse + certificado de contenido
> 2. **Editar tono o plazo** — dime cambios
> 3. **Si es MASC: actualizar asunto** — `/actualizar-asunto <slug-asunto>`

## Reglas

1. **Acuse de recibo + certificado de contenido** son OBLIGATORIOS para acreditar tanto la entrega como el contenido. Sin certificado de contenido, no se prueba lo que se dijo.
2. **Plazo en días naturales o hábiles**: especificar. Default civil = hábiles para coherencia con LEC.
3. **Firma del letrado o cliente**: respeta lo elegido en intake; si dudoso, recomendar firma del cliente (el letrado representa pero el requerimiento es del cliente).
4. **Si es MASC**, indicarlo expresamente. Sin esa mención, podría no servir como MASC del art. 5.
5. **NO bluff.** Si el burofax dice "demandaré", el cliente tiene que estar preparado para hacerlo.
