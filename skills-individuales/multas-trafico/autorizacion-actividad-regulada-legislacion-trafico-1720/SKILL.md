---
name: autorizacion-actividad-regulada-legislacion-trafico-1720
description: "Prepara o revisa en España: Autorización para una actividad regulada por la legislación de tráfico y seguridad vial. Requiere el conector Jurisprudenciator."
---

# Autorización para una actividad regulada por la legislación de tráfico y seguridad vial

Usa esta skill cuando el usuario pida preparar o revisar este documento en Derecho español.

## Jurisprudenciator obligatorio

1. Llama a `estado` en el conector Jurisprudenciator antes de empezar. Si el conector no está disponible, detén la redacción y remite a [Instalación de Jurisprudenciator](https://jurisprudenciator.com/instalacion).
2. Verifica el marco y su vigencia en la fecha pertinente con `buscar_articulo`. Si desconoces el identificador de una norma, localízala con `buscar_boe` y ábrela con `leer_boe`.
3. Para fundamentación jurisprudencial, usa `buscar_sentencias` y `leer_sentencias`. Para citas aportadas, usa `buscar_por_cita` y comprueba el texto con `leer_sentencias`. Usa únicamente citas respaldadas por el resultado consultado.
4. Si una comprobación jurídica imprescindible falla, identifica el punto pendiente y detén la entrega del escrito hasta verificarlo.

## Datos del asunto

- Autoridad, expediente y notificación, hecho atribuido, prueba disponible y norma vigente en la fecha pertinente.
- Autoridad destinataria, solicitante, objeto preciso, documentos exigidos y acuse o resolución si ya existe expediente.

## Preparación y entrega

1. Separa hechos acreditados, versión del cliente y datos pendientes. Solicita las fechas o documentos imprescindibles y anonimiza las consultas al conector.
2. Confirma vía y fase, destinatario, legitimación, plazo y requisitos aplicables. Si el tipo de documento no encaja con los hechos, explica al usuario el motivo antes de elegir otra vía.
3. Redacta un borrador original para el encargo. Adapta la estructura al documento, conecta cada fundamento con los hechos y concreta la pretensión o actuación. Señala datos pendientes con marcadores explícitos.
4. Llama a `verificar_escrito` sobre el texto que cita normas o sentencias, corrige las citas señaladas y deja junto al borrador las verificaciones, fuentes y datos pendientes. Identifica el resultado como borrador para revisión.
