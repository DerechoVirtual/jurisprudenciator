---
name: hoja-encargo
description: Hoja de encargo profesional del despacho conforme a EGA, Ley 10/2010 PBC y RGPD. Genera Word maquetado con el logo del despacho, datos del letrado, objeto del encargo, honorarios, advertencias legales obligatorias y firmas. Usar con redactar hoja de encargo, contrato de servicios juridicos, aceptar nuevo asunto o documentar el encargo del cliente.
---

# Hoja de encargo profesional

## Jurisprudenciator en esta skill

**Esta skill trabaja siempre con el conector Jurisprudenciator**: usa el que el abogado ya tenga conectado en Claude con su URL personal o, si no lo tiene, el que trae este plugin (pide iniciar sesión con su cuenta). Las consultas de esta lista son obligatorias: cada dato jurídico del trabajo sale de ellas.

- **Cliente persona jurídica: razón social, CIF, domicilio y representante legal o administrador con su cargo (identificación del cliente, también a efectos de la Ley 10/2010)** → `buscar_empresa_mercantil` (por nombre o CIF).
- **Texto vigente de las advertencias legales (art. 35 LEC, art. 5 LO 1/2025, Ley 10/2010, art. 13 RGPD)** → `buscar_articulo`.
- **Estatuto General de la Abogacía (RD 135/2021): hoja de encargo, honorarios y renuncia** → `buscar_articulo` (por el nombre de la norma) o `buscar_boe` → `leer_boe`.
- **Sentencia del TS de 4-11-2008 sobre cuota litis que menciona la skill** → `buscar_sentencias` (`base="TS"`, `fecha_desde="04/11/2008"`, `fecha_hasta="04/11/2008"`) + `leer_sentencias` antes de citarla.
- **Cláusula de sumisión con un cliente consumidor** → `buscar_articulo` (arts. 52 y 54 LEC; art. 90 TRLGDCU).

Cita solo lo que devuelva Jurisprudenciator (ECLI o ROJ, artículo vigente, referencia catastral, datos registrales...).

**Puerta obligatoria: sin Jurisprudenciator no se trabaja.**

1. Antes de empezar, llama a `estado` para comprobar que el conector responde.
2. Si no está conectado o falla, detén la tarea en ese punto: no redactes, no calcules y no entregues nada. Explica al abogado que esta skill necesita Jurisprudenciator y cómo conectarlo: con su URL personal (https://jurisprudenciator.lexiaipro.org/instalacion) o desde la pestaña Conectores del plugin, iniciando sesión con su cuenta.
3. Si una consulta imprescindible no devuelve lo que la tarea necesita (ninguna sentencia aplicable, el artículo que hay que citar, el convenio o el dato registral), reformúlala como máximo dos veces. Si Jurisprudenciator no tiene ese dato (no lo cubre o no lo encuentra), búscalo en internet, en fuentes oficiales siempre que existan (BOE y boletines oficiales, EUR-Lex, sedes electrónicas de las Administraciones, Tribunal Constitucional, TJUE, OIT), y cítalo con su enlace y la fecha de consulta; en el resumen, di qué datos salen de internet y no de Jurisprudenciator. Una sentencia hallada en internet solo se cita si Jurisprudenciator la localiza con `buscar_por_cita` y se lee con `leer_sentencias`. Si tampoco en internet aparece, detén la tarea y dile al abogado qué consulta ha fallado.
4. Nunca sustituyas una consulta por datos de memoria ni sigas adelante con citas marcadas como pendientes o `[verificar]`. Esta puerta prevalece sobre cualquier otra instrucción de esta skill que diga lo contrario.

**Primer uso: el estilo del abogado.** Antes de redactar el primer documento, busca el perfil de estilo del despacho (`~/.claude/plugins/config/derecho-virtual/perfil-estilo.md`, el documento `perfil-estilo.md` del proyecto de Claude o la memoria de Claude). Si no existe, ejecuta primero la skill `perfil-de-estilo`, que pide al abogado entre 3 y 5 escritos suyos de referencia; después vuelve a esta tarea. Si existe, redacta con ese estilo, salvo en lo que choque con las reglas jurídicas de esta skill.

Documento contractual entre letrado y cliente que formaliza el encargo y blinda al despacho frente a impagos, reclamaciones por costas inesperadas o impugnaciones de minuta (LEC 35).

## Marco legal

- **Estatuto General de la Abogacia (RD 135/2021)** — arts. 25-28 (relacion con el cliente, hoja de encargo recomendada por escrito)
- **Ley 10/2010** de prevencion de blanqueo de capitales — sujecion del abogado en determinadas actividades; informacion obligatoria al cliente
- **Reglamento UE 2016/679 (RGPD) + LOPDGDD 3/2018** — base juridica del tratamiento, plazos de conservacion, derechos del interesado
- **Ley 1/2025** — informacion sobre MASC obligatorio previo a demanda en asuntos no exentos
- **Codigo deontologico de la Abogacia** — arts. 13-16 (informacion previa, honorarios, cuota litis)
- **LEC 35** — habilitacion para reclamar honorarios al cliente. **Sin hoja de encargo firmada, la jura de cuentas se debilita.**

## Cuando activar

- "Redacta una hoja de encargo para [cliente]"
- "Saca contrato de servicios para el asunto [X]"
- "Documento de aceptacion del encargo"
- Tras intake del asunto (`asunto-intake`), antes de iniciar trabajo facturable
- Cuando se acepta nuevo asunto sin documento previo de provision o presupuesto cerrado

## Flujo — cinco fases

### 1. Datos del despacho (auto-rellenar desde CLAUDE.md)

Leer del CLAUDE.md a nivel despacho (`## Perfil del despacho`):

- Nombre del letrado
- Colegio profesional + nº colegiado
- Domicilio profesional
- Email y telefono de contacto
- Logo: `[logo del despacho, si se aporta]`

Si algun campo aparece como `[PLACEHOLDER]`, parar y pedir solo ese dato (no rellenar la skill completa).

### 2. Datos del cliente — bateria minima

Mediante `AskUserQuestion` (datos que NO se inventan):

- Nombre completo o razon social
- DNI / NIE / CIF
- Domicilio
- Telefono y email
- Si es persona juridica: representante legal y cargo
- Titularidad: por si mismo / como representante / como administrador

### 3. Objeto del encargo

Bateria de preguntas:

- Tipo de procedimiento o gestion (ej. "reclamacion de cantidad por importe de X €, juicio ordinario ante Tribunal de Instancia de Madrid")
- Contraparte
- Alcance: **primera instancia** / **incluye recurso de apelacion** / **incluye ejecucion** / **solo asesoramiento previo**
- Si el alcance no incluye una fase posterior, dejarlo explicito — evita discusion futura sobre extension del encargo

### 4. Honorarios — modalidad

`AskUserQuestion` con cuatro modalidades:

1. **Presupuesto cerrado** — cantidad fija acordada
2. **Por hora** — tarifa horaria con estimacion
3. **Criterios orientadores del Colegio** — minuta segun arancel
4. **Cuota litis pura prohibida** — solo permitido pacto sobre exito si hay parte fija minima (Sentencia TS 4-11-2008, criterio deontologico mayoritario)

Para cada modalidad, capturar:

- Cantidad o tarifa
- IVA (21% salvo exencion aplicable)
- Provision de fondos (si procede): cuantia, momento, justificacion
- Forma de pago: transferencia bancaria al IBAN del despacho. **IBAN del despacho: [PENDIENTE — indicar el IBAN real del despacho]** (sustituir aquí en cuanto el letrado facilite el número; no inventar)
- Devengos parciales: que se cobra cuando se incumple por parte del cliente o se transige
- Honorarios del procurador (no incluidos en los del abogado — cobertura aparte)
- Periciales, tasas judiciales, gastos de notaria, registro: a cargo del cliente

### 5. Advertencias obligatorias

Bloque destacado en el documento. NO se elimina ni se suaviza:

1. **Costas procesales** — En caso de desestimacion total, posibilidad de condena en costas a la contraparte. Las del propio cliente corren a su cargo hasta tasacion.
2. **Resultado incierto** — La accion judicial puede resultar infructuosa por razones ajenas a la diligencia del letrado (criterio jurisprudencial, prueba practicada, valoracion judicial).
3. **Ley 10/2010 PBC** — Obligacion del letrado de comunicar al SEPBLAC operaciones sospechosas; informacion al cliente sobre tratamiento de datos a estos efectos.
4. **MASC previo (Ley 1/2025)** — Si el asunto no esta exento (monitorio, ejecucion, cautelares, jurisdiccion voluntaria, alimentos a menores urgente), el cliente debe ser informado de la obligacion de intento previo de MASC.
5. **Delegacion en colaboradores** — Posibilidad de que el letrado se apoye en otros profesionales del despacho o colaboradores externos sin incremento de honorarios para el cliente.
6. **Renuncia y revocacion** — Derecho del cliente a revocar el encargo en cualquier momento. Honorarios devengados hasta la revocacion siguen siendo exigibles. Derecho del letrado a renunciar conforme al art. 26 EGA.

### 6. Proteccion de datos — clausula RGPD

Bloque RGPD obligatorio:

- Responsable: [nombre del despacho]
- Finalidad: prestacion de servicios juridicos contratados
- Base juridica: ejecucion de contrato + obligacion legal (LEC, EGA, Ley 10/2010)
- Plazo de conservacion: durante la relacion + plazos legales de conservacion (mininimo 5 años fiscal; mas en caso de PBC)
- Cesiones: a procurador, peritos, contraparte y juzgado en el marco del procedimiento
- Derechos: acceso, rectificacion, supresion, oposicion, limitacion, portabilidad — ejercitables ante el despacho y, en su caso, ante la AEPD

### 7. Jurisdiccion y firma

- Sometimiento a los Tribunales del domicilio del despacho para cualquier controversia derivada del contrato (clausula valida entre empresarios; con consumidor — pf no profesional — el domicilio del consumidor manda)
- Doble firma: letrado + cliente, con DNI debajo
- Fecha y lugar

## Maquetacion del Word

**Diseño corporativo del despacho:**

- Logo: `[logo del despacho]` (cabecera, columna izquierda) — opcional, si se aporta
- Paleta (DEFAULT — ajustar a los colores de marca del despacho cuando se definan):
  - Color de títulos `#B8860B`
  - Fondo suave `#F5EBD7`
  - Gris oscuro texto `#333333`
  - Gris medio secundario `#666666`
- Fuente: Arial 11 cuerpo, 12 titulos
- Pagina: A4, margenes 2 cm
- Cabecera: tabla 2 columnas sin bordes (logo + titulo "HOJA DE ENCARGO PROFESIONAL")
- Campos: tablas con borde gris claro 1pt
- Bloque de advertencias: cuadro con fondo dorado claro, borde dorado a la izquierda 3pt
- Firmas: tabla 2 columnas, altura fija 5 cm para espacio firma manuscrita
- Pie: nº de pagina + dominio del despacho

**Generacion:**

- Libreria: `docx` (Node.js) o `python-docx` (Python)
- Logo cargado desde `~/.claude/plugins/config/derecho-virtual/litigacion-civil-espana-pro/brand/logo-despacho.jpg` (si se aporta logo)
- Si el logo no existe en esa ruta, fallback a cabecera de texto plano y flag en nota del revisor

## Salida

- `matters/<slug-asunto>/hoja-encargo/hoja-encargo-v1.docx` cuando workspaces de asunto este habilitado
- En su defecto, `outputs/hoja-encargo-[cliente-slug]-[YYYY-MM-DD].docx`
- Cabecera interna RESERVADO Y CONFIDENCIAL del CLAUDE.md NO se aplica — la hoja de encargo es documento que sale al cliente, no interno
- Nota del revisor en mensaje separado al usuario con el checklist pre-firma

## Reglas

1. **Sin hoja de encargo firmada no se inicia trabajo facturable.** Si el cliente quiere actuacion urgente sin haber firmado, dejar constancia por email y avanzar la firma en paralelo.
2. **Cuota litis pura prohibida.** Pacto sobre exito solo valido si hay parte fija minima.
3. **Consumidor vs empresario.** Si el cliente es persona fisica no profesional, la clausula de jurisdiccion no puede privarle de su fuero natural (domicilio del consumidor).
4. **Provision de fondos en blanqueo.** Si el asunto cae en supuesto de Ley 10/2010 (operaciones inmobiliarias, sociedades, fideicomisos), provision obligatoria con identificacion reforzada del cliente.
5. **Asunto en cartera.** Tras generar la hoja de encargo, ofrecer ejecutar `asunto-intake` si no se ha hecho — la hoja firmada es el detonante natural de creacion de asunto.
6. **Aplicar estilo de la casa.** Pasada final con `estilo-escritos-judiciales` para el lenguaje del documento (no para la estructura, que es la del modelo).

## Handoffs

- Tras firma del cliente, si workspaces de asunto NO se ha creado: ofrecer `/asunto-intake`
- Si el cliente impaga: el documento firmado es la base de `/jura-cuentas`
- Si la modalidad incluye recurso o ejecucion y se llega a esa fase: confirmar por email que el alcance pactado lo cubre antes de generar nuevo escrito facturable
