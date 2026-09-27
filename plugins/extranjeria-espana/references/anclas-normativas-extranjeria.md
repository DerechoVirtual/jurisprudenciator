# Anclas normativas de extranjería

Mapa de dónde está cada figura. Da el número de artículo, **no su contenido**: el texto vigente se
pide siempre a Jurisprudenciator (`buscar_articulo`) antes de citarlo o de comprobar un requisito.

## Contenido

1. Cómo pedir cada norma a Jurisprudenciator
2. Reglamento de extranjería (Real Decreto 1155/2024)
3. Ley Orgánica 4/2000 (LOEX)
4. Nacionalidad
5. Protección internacional y apatridia
6. Ciudadanos de la Unión y sus familiares
7. Procedimiento y recursos
8. Límites conocidos del conector

## 1. Cómo pedir cada norma a Jurisprudenciator

Usa en `buscar_articulo` exactamente el valor de la columna `ley`. Algunas normas **solo** se
localizan bien por su identificador del BOE.

| Norma | `ley` | Aviso |
|---|---|---|
| LO 4/2000, de derechos y libertades de los extranjeros (LOEX) | `LOEX` | |
| Reglamento de la LOEX (Real Decreto 1155/2024), vigente desde el 20/05/2025 | `BOE-A-2024-24099` | Nunca por su nombre: «Reglamento de Extranjería» devuelve otra norma. |
| Ley 14/2013, de apoyo a los emprendedores (movilidad internacional, arts. 61 y ss.) | `BOE-A-2013-10074` | Nunca «Ley 14/2013»: devuelve una ley autonómica. |
| Real Decreto 240/2007 (ciudadanos UE/EEE y sus familiares) | `Real Decreto 240/2007` | |
| Ley 12/2009, de asilo y protección subsidiaria | `Ley 12/2009` | |
| Real Decreto 203/1995 (reglamento de asilo) | `Real Decreto 203/1995` | |
| Real Decreto 865/2001 (estatuto de apátrida) | `Real Decreto 865/2001` | |
| Código Civil (nacionalidad, arts. 17 a 28) | `CC` | |
| Real Decreto 1004/2015 (nacionalidad por residencia) | `Real Decreto 1004/2015` | |
| Ley 20/2011, del Registro Civil | `Ley 20/2011` | |
| Orden JUS/1625/2016 (tramitación de la nacionalidad por residencia) | `Orden JUS/1625/2016` | Su anexo de documentos no se obtiene. |
| Ley 40/2015 (régimen jurídico del sector público) | `Ley 40/2015` | |
| Ley de Enjuiciamiento Criminal | `LECrim` | |
| Código Penal | `CP` | |
| LO 1/2004 (violencia de género) | `LO 1/2004` | |
| LO 10/2022 (libertad sexual) | `LO 10/2022` | |
| Directiva 2011/36/UE (trata) | `Directiva 2011/36/UE` | |
| Ley 20/2022, de Memoria Democrática | `Ley 20/2022` | Sus disposiciones adicionales no se obtienen (ver apartado 8). |
| Real Decreto 162/2014 (centros de internamiento de extranjeros) | `Real Decreto 162/2014` | |
| Ley 39/2015 (LPAC) | `LPAC` | |
| Ley 29/1998 (LJCA) | `LJCA` | |
| LO 6/1985 (LOPJ) | `LOPJ` | |
| Constitución | `CE` | |
| Ley de Enjuiciamiento Civil | `LEC` | |
| Ley Orgánica 1/1996, de protección jurídica del menor | `Ley Orgánica 1/1996` | |
| Ley 1/1996, de asistencia jurídica gratuita | `Ley 1/1996` | |
| Directiva 2004/38/CE (libre circulación) | `Directiva 2004/38/CE` | |
| Directiva 2003/86/CE (reagrupación familiar) | `Directiva 2003/86/CE` | |
| Directiva 2008/115/CE (retorno) | `Directiva 2008/115/CE` | |
| Directiva 2003/109/CE (residentes de larga duración) | `Directiva 2003/109/CE` | |
| Reglamentos (UE) 2018/1860 y 2018/1861 (Sistema de Información Schengen) | `Reglamento (UE) 2018/1861` | Comprueba el título del artículo devuelto. |
| LO 7/2021 (datos personales en el ámbito penal y policial) | `Ley Orgánica 7/2021` | |
| Ley 41/2002 (autonomía del paciente) | `Ley 41/2002` | |
| Reglamento (UE) 2024/1347 (requisitos de protección internacional) | `Reglamento (UE) 2024/1347` | |
| Reglamento (UE) 2024/1348 (procedimiento común de protección internacional) | `Reglamento (UE) 2024/1348` | |
| Reglamento (UE) 2024/1351 (gestión del asilo y la migración) | `Reglamento (UE) 2024/1351` | |
| Reglamento (UE) 2024/1356 (triaje en las fronteras exteriores) | `Reglamento (UE) 2024/1356` | |
| Reglamento (UE) 2016/399 (Código de fronteras Schengen) | `Reglamento (UE) 2016/399` | |
| Reglamento (CE) 810/2009 (Código de visados) | `Reglamento (CE) 810/2009` | |
| Orden PRE/1282/2007 (medios económicos para la entrada) | — | `buscar_articulo` no la encuentra: léela con `leer_boe` e `identificador="BOE-A-2007-9608"`. |

Para normas que no estén en esta tabla, localízalas antes con `buscar_boe` y usa el identificador
BOE que devuelva. Para saber si un artículo se ha reformado, no uses `buscar_boe`: lee la línea
«redacción vigente dada por…» y las notas «Téngase en cuenta…» que devuelve `buscar_articulo`.

## 2. Reglamento de extranjería (`ley="BOE-A-2024-24099"`)

El Reglamento ha sido **anulado en parte por el Tribunal Supremo** (sentencias de 8 y 29 de julio de 2026,
publicadas con las referencias BOE-A-2026-19632 y BOE-A-2026-19633; afectan, entre otros, a los arts. 94.1.f, 97.4, 98.1, 101,
159, 160, 166, 196 y 197; `buscar_articulo` solo dice «inciso destacado»: para saber qué inciso se
anuló, lee el fallo con `leer_boe` e `identificador="BOE-A-2026-19632"`) y **modificado** por el Real Decreto 316/2026, vigente desde el 16/04/2026
(BOE-A-2026-8284): arts. 97 (entre otros, 97.1.c y 97.5: solicitud desde España de hijos mayores y ascendientes), 126,
127, 130, 132, 172.2, 190 y 191, y las disposiciones adicionales segunda y novena; deroga la disposición transitoria quinta y añade
las disposiciones adicionales vigésima y vigesimoprimera (arraigo de solicitantes de protección
internacional y arraigo extraordinario, con plazo de solicitud hasta el 30/06/2026). `buscar_articulo`
no devuelve esas disposiciones adicionales; `leer_boe` con `identificador="BOE-A-2026-8284"` trae la
vigésima completa y la vigesimoprimera hasta su apartado 5. `buscar_articulo`
devuelve el texto con notas que empiezan por «Téngase en cuenta que se declara la nulidad…»: léelas
siempre. Lo anulado no se aplica ni se cita como requisito, y muchas sentencias de TSJ recientes
aplican aún el Reglamento anterior (Real Decreto 557/2011, con otra numeración): comprueba qué
reglamento aplicó cada sentencia antes de trasladar su doctrina.

| Materia | Artículos |
|---|---|
| Entrada, requisitos, medios económicos, denegación de entrada | 1-18 (denegación: 15) |
| Salida, devoluciones, salidas obligatorias | 19-24 (devoluciones: 23) |
| Visados: definición, presentación, procedimiento, resolución | 25-28 |
| Visados de estancia de larga duración por estudios | 34-36 |
| Visados de residencia; familiares de personas con nacionalidad española | 37-41 (familiares de españoles: 41) |
| Visados de búsqueda de empleo (general, hijos o nietos de español de origen, ocupaciones) | 43-45 |
| Situaciones de estancia; prórroga de estancia | 47-51 |
| Estancia de larga duración por estudios, movilidad, voluntariado, formación; familiares; acceso al empleo | 52-59 |
| Residencia temporal: supuestos | 60 |
| Residencia temporal no lucrativa | 61-64 |
| Reagrupación familiar | 65-71 |
| Residencia temporal y trabajo por cuenta ajena; situación nacional de empleo; cambio de empleador; renovación | 72-81 |
| Residencia temporal y trabajo por cuenta propia | 82-87 |
| Excepciones a la autorización de trabajo | 88-89 |
| Retorno voluntario | 90-92 |
| Familiares de personas con nacionalidad española | 93-99 |
| Actividades de temporada | 100-112 |
| Gestión colectiva de contrataciones en origen | 113-123 |
| Circunstancias excepcionales: definición | 124 |
| Arraigo: tipos (segunda oportunidad, sociolaboral, social, socioformativo, familiar) | 125 |
| Arraigo: requisitos generales y específicos | 126-127 |
| Razones humanitarias | 128 |
| Colaboración con autoridades, seguridad nacional, interés público | 129 |
| Circunstancias excepcionales: procedimiento, autorización de trabajo, prórroga | 130-132 |
| Mujer víctima de violencia de género | 133-136 |
| Víctima de violencia sexual | 137-141 |
| Colaboración contra redes organizadas | 142-147 |
| Víctimas de trata de seres humanos (identificación, periodo de reflexión, autorización) | 148-155 |
| Trabajadores transfronterizos | 156-158 |
| Menores: nacidos en España, acompañados, desplazamientos temporales | 159-164 |
| Menores extranjeros no acompañados; determinación de edad; mayoría de edad | 165-174 |
| Residencia de larga duración-UE | 175-181 |
| Residencia de larga duración nacional | 182-185 |
| Recuperación de la larga duración | 186-189 |
| Modificaciones de situación (estudios → residencia y trabajo; residencia → residencia y trabajo) | 190-192 |
| Competencias, persona a cargo, lugares de presentación y representación | 193-198 |
| Extinción de autorizaciones | 199-203 |
| NIE, documentos, tarjeta de identidad de extranjero | 205-211 |
| Procedimiento sancionador: normas generales, caducidad y prescripción | 215-224 |
| Procedimiento ordinario | 225-232 |
| Procedimiento preferente | 233-236 |
| Procedimiento simplificado | 237-239 |
| Expulsión: supuestos, iniciación, cautelares, resolución, ejecución | 241-248 |
| Multas | 249-252 |

## 3. LOEX (`ley="LOEX"`)

| Materia | Artículos |
|---|---|
| Derechos de los extranjeros (educación, trabajo, asistencia jurídica gratuita...) | 3-15 y 22 |
| Reagrupación familiar | 16-19 |
| Garantías jurídicas y recursos | 20-22 |
| Entrada, visados, salida | 25-28 |
| Estancia y residencia; residencia temporal (arraigo en el art. 31.3) | 29-31 |
| Mujeres víctimas de violencia de género o sexual | 31 bis |
| Residencia de larga duración (incluido su apartado 3 bis) | 32 |
| Menores | 35 |
| Autorizaciones de trabajo | 36-43 |
| Infracciones y sanciones | 50-56 |
| Expulsión | 57-58 |
| Colaboración contra redes; víctimas de trata | 59 y 59 bis |
| Retorno | 60 |
| Medidas cautelares e internamiento | 61-62 sexies |
| Procedimiento preferente y ordinario de expulsión | 63 y 63 bis |
| Ejecución de la expulsión | 64 |

## 4. Nacionalidad

- Código Civil (`CC`): arts. 17 a 28 (origen, opción, carta de naturaleza, residencia en el art. 22, pérdida, recuperación).
- Real Decreto 1004/2015: procedimiento de nacionalidad por residencia, pruebas DELE y CCSE (art. 6).
- Ley 20/2011 del Registro Civil (`Ley 20/2011`): inscripción de la nacionalidad (art. 68).

## 5. Protección internacional y apatridia

- Ley 12/2009 (`Ley 12/2009`) y Real Decreto 203/1995.
- Pacto europeo de Migración y Asilo: Reglamentos (UE) 2024/1347, 2024/1348 y 2024/1351. Antes de
  aplicarlos, comprueba con `buscar_articulo` su fecha de aplicación y si la norma española se ha
  adaptado (`buscar_boe` con «protección internacional» y fechas recientes).
- Apatridia: Real Decreto 865/2001.

## 6. Ciudadanos de la Unión y sus familiares

- Real Decreto 240/2007 y Directiva 2004/38/CE.
- Los familiares de **personas con nacionalidad española** tienen desde 2025 régimen propio en el
  Reglamento (arts. 93 a 99), distinto del de los familiares de ciudadanos de otros Estados de la Unión.

## 7. Procedimiento y recursos

- LPAC (`LPAC`): silencio (arts. 21, 24), subsanación (art. 68), recursos de alzada y reposición (arts. 112 y ss.; plazos en los arts. 122 y 124).
- LJCA (`LJCA`): competencia en materia de extranjería (art. 8.4), plazo del recurso (art. 46), procedimiento abreviado (art. 78), medidas cautelares (arts. 129 y ss.).
- LOPJ (`LOPJ`, art. 84): desde la LO 1/2025 los recursos van al **Tribunal de Instancia, Sección de lo Contencioso-Administrativo**.

## 8. Límites conocidos del conector

- `buscar_articulo` no devuelve **disposiciones adicionales ni transitorias** (por ejemplo, la
  disposición adicional octava de la Ley 20/2022 o las transitorias del Reglamento).
- `buscar_articulo` no devuelve artículos con sufijo compuesto como «588 bis a».
- `leer_boe` devuelve solo el principio de una norma larga. Excepción útil: `leer_boe` con
  `identificador="BOE-A-2024-24099"` sí devuelve completas las disposiciones transitorias primera y
  segunda del Real Decreto 1155/2024 (autorizaciones vigentes y solicitudes anteriores al 20/05/2025).
- El Reglamento derogado se consulta con `ley="Real Decreto 557/2011"` (solo para entender
  sentencias que lo aplicaron).

- `leer_convenio` suele devolver la publicación original del convenio y no las tablas salariales
  vigentes (van en anexos o en revisiones registradas aparte, que `vigencia_convenio` sí lista). Si la
  tabla vigente no aparece, pídesela al abogado o deja marcador: no afirmes que un salario la cumple.
- El **Tratado de Funcionamiento de la Unión Europea** no está disponible: `buscar_articulo` no lo
  encuentra ni por sigla ni por nombre, y `verificar_escrito` atribuye sus artículos a otra norma. Para
  la ciudadanía europea del menor (art. 20 TFUE), apóyate en la jurisprudencia del TJUE y del Supremo
  leída con `leer_sentencias`, que transcribe el precepto, y no cites el Tratado de memoria.
- **Real Decreto 316/2026**: `verificar_escrito` lo confunde con el Real Decreto 68/2026 y `buscar_boe`
  no lo encuentra por su número. Cítalo por su identificador (BOE-A-2026-8284), léelo con `leer_boe` e
  ignora el veredicto de `verificar_escrito` sobre él.
- Jurisprudencia de un TSJ: usa en `provincia` la **sede de la Sala** (Granada, Sevilla o Málaga en
  Andalucía; Las Palmas o Santa Cruz de Tenerife en Canarias…), no la provincia del cliente: con una
  provincia que no es sede, el buscador responde «Sin resultados» y cae al Supremo.
- Si una consulta devuelve «no localizado» para un artículo que debería existir, repítela antes de
  concluir nada: ha habido caídas temporales de unos minutos.
- Durante caídas de la base de normativa de la Unión, `buscar_articulo` puede devolver el artículo de
  otra norma sin avisar. Comprueba siempre que el título de la norma devuelta es el que pediste.

Si el asunto depende de uno de esos preceptos y Jurisprudenciator no devuelve su texto, se aplica
la puerta obligatoria de la skill: la tarea se detiene y se explica al abogado qué precepto falta.
