# ⚖️🤖 Proyecto Final — Derecho e Inteligencia Artificial

**Pontificia Universidad Javeriana · 2026-II · Docente: Pedro Ardila**

> **Estudiante:** Simón Andrés Contreras Palma 
> **Nombre del proyecto:** REVISOR DE CONTRATOS SIMPLES
> **Fecha de inicio:** 18/08/2026

---

Bienvenido/a a tu repositorio de proyecto. **Este archivo es tu tablero de mando**: aquí describes tu proyecto, planificas su desarrollo y dejas evidencia del avance. Lo vas a completar por partes, siguiendo el curso.

📌 Si ya habías escrito una descripción de tu proyecto cuando creaste el repo, la encuentras intacta en `README-ORIGINAL.md`. Úsala como punto de partida para la Parte 1 — no empieces de cero.

**No necesitas saber programar.** Todo el código lo construirás con asistencia de IA (*vibe coding*). Tu valor como estudiante de derecho está en el problema que eliges, las fuentes que alimentas, las instrucciones que diseñas y el juicio crítico con el que evalúas el resultado.

---

## 📋 Parte 1 — Descripción del proyecto

> Completa cada sección con 3–10 frases. Sé concreto/a: esta descripción es la que tu IA usará como contexto y la que el docente usará para realimentarte.

### 1.1 El problema jurídico
¿Qué problema **real del derecho colombiano** resuelve tu herramienta? ¿Quién lo sufre hoy y cómo lo resuelve sin tu herramienta?
Las personas que firman contratos sencillos de arrendamiento o de prestación de servicios muchas veces no identifican cláusulas abusivas, riesgosas, ambiguas o elementos importantes que hacen falta en el contrato. Esto puede generar conflictos posteriores sobre pagos, terminación, obligaciones, responsabilidades o incumplimientos. Actualmente, una persona sin conocimientos jurídicos debe revisar el contrato por su cuenta o pagar una asesoría para identificar estos riesgos. La herramienta busca ofrecer una primera revisión orientativa basada en una lista de verificación jurídica colombiana. No reemplaza la asesoría de un abogado, pero permite detectar problemas básicos antes de firmar.

### 1.2 Usuarios
¿Quién va a usarla? Describe a tu usuario ideal en una frase (ej. *"un arrendatario bogotano que le subieron el canon de arrendamiento más del límite legal"*). Recuerda que al final necesitas **al menos un usuario real** que la pruebe.
El usuario ideal es una persona en Colombia que está a punto de firmar un contrato sencillo de arrendamiento de vivienda o de prestación de servicios y quiere identificar posibles riesgos antes de firmarlo. También puede ser utilizado por estudiantes, pequeños arrendadores, trabajadores independientes o personas que contratan servicios. El usuario debe poder cargar o copiar el texto del contrato en la herramienta.

### 1.3 Qué hace y qué NO hace (alcance)
| ✅ Sí hace | ❌ No hace |
| --- | --- |
| [Identifica cláusulas potencialmente riesgosas, ambiguas o faltantes.] | [No reemplaza la asesoría de un abogado.] |
| [Señala aspectos que el usuario debería revisar antes de firmar.] | [No representa al usuario ante jueces, autoridades o particulares.] |

*Consejo de abogado: un alcance pequeño y perfecto vale más que uno grande y roto.*

### 1.4 Marco jurídico y fuentes
¿Qué normas alimentan tu herramienta? Lista tu corpus normativo (leyes, decretos, sentencias — debe ser **pequeño y público**):
- [ ] Norma/sentencia 1: [Ley 820 de 2003 — Régimen de arrendamiento de vivienda urbana. http://www.secretariasenado.gov.co/senado/basedoc/ley_0820_2003.html?utm_source=chatgpt.com]
- [ ] Norma/sentencia 2: [Código Civil colombiano — artículos sobre arrendamiento. http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil.html?utm_source=chatgpt.com]

### 1.5 Nombre y lema
CONTRATO CHECK
“Revisa. Detecta. Decide.”
---

## 🗺️ Parte 2 — Plan de desarrollo

Marca cada hito cuando lo termines. Los hitos siguen las sesiones del curso.

- [ ] **M0 — Descripción y plan** *(con Sesión 1)*: Partes 1 y 2 de este README completas.
- [ ] **M1 — Asistente con instrucciones v1** *(Sesión 1–2)*: redactaste las instrucciones (prompt de sistema) de tu asistente y funcionan en una herramienta gratuita de chat.
- [ ] **M2 — Casos de prueba documentados** *(Sesión 2)*: tienes al menos 5 casos de prueba (donde antes fallaba) con resultados guardados en `docs/casos-de-prueba.md`.
- [ ] **M3 — Corpus conectado (RAG)** *(Sesión 3)*: tu asistente **cita la fuente** normativa que usa y no inventa. Corpus cargado en `corpus/`.
- [x] **M4 — Interfaz web desplegada** *(Sesión 4)*: tu herramienta tiene **URL pública** (ver Parte 4) y tu primer usuario real la probó con evidencia.
- [ ] **M5 — Análisis crítico y demo** *(Sesión 5)*: Parte 7 completada + presentación de 5 minutos.

### Bitácora de avance semanal
| Semana | Qué hice | Enlace/captura | Dudas para la clase |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

## 🛠️ Parte 3 — Stack técnico recomendado

Todo es **gratuito y no exige tarjeta de crédito**. Tu proyecto final debería verse así:

```
[Usuario] → [Interfaz web] → [Orquestación (LangChain)] → [Modelo (OpenRouter)]
                                   ↕
                          [Tu corpus normativo (RAG)]
```

Pieza	Herramienta recomendada	Para qué sirve (en CONTRATO CHECK)
Interfaz web	v0.dev + Next.js	Será la parte que ve el usuario. Permitirá seleccionar el tipo de contrato, pegar o cargar el texto y presionar el botón “Revisar contrato”. También mostrará los riesgos detectados, recomendaciones y fuentes jurídicas.
Orquestación	LangChain	Conectará las diferentes partes de la herramienta. Recibirá el contrato del usuario, buscará información relevante en el corpus jurídico, construirá el contexto para el modelo y organizará la respuesta final.
Modelo (LLM)	OpenRouter — modelo gratuito	Será el modelo encargado de analizar el contrato y explicar los posibles riesgos jurídicos en lenguaje sencillo. Recibirá tanto el contrato como los fragmentos normativos recuperados por el sistema RAG.
Memoria de fuentes (RAG)	Chroma durante el desarrollo; Supabase/pgvector si se requiere almacenamiento en la nube	Permitirá almacenar y buscar los fragmentos de las normas que alimentan CONTRATO CHECK. Así, el modelo podrá consultar el corpus jurídico seleccionado en lugar de depender únicamente de la información que aprendió durante su entrenamiento.
Corpus jurídico	Archivos .md o .txt dentro de corpus/	Contendrá las normas colombianas utilizadas por la herramienta, inicialmente la Ley 820 de 2003 y los artículos pertinentes del Código Civil colombiano. Cada fuente estará organizada para facilitar su recuperación y citación.
Trazabilidad (opcional)	LangSmith	Permitirá observar el funcionamiento interno de las consultas y detectar errores durante el desarrollo. No es indispensable para la primera versión, por lo que se incorporará únicamente si resulta necesario.
Seguridad	Variables de entorno (.env)	La clave de OpenRouter se almacenará como una variable de entorno y no se escribirá directamente en el código ni se publicará en GitHub.|

> 🔑 **Regla de oro:** tu `OPENROUTER_API_KEY` va en una **variable de entorno**, jamás pegada en el código ni en el chat. Si una clave se filtra en GitHub, revócala de inmediato en openrouter.ai → Keys.

Pídele a tu agente de IA que te explique esta arquitectura con tu proyecto concreto antes de escribir una línea de código.

|Componente|Herramient|Función|
|---|---|---|
|Interfaz Web| v0.dev + Next.js|Será la parte que ve el usuario. Permitirá seleccionar el tipo de contrato, pegar o cargar el texto y presionar el botón “Revisar contrato”. También mostrará los riesgos detectados, recomendaciones y fuentes jurídicas|
|orquestación| LangChain| Conectará las diferentes partes de la herramienta. Recibirá el contrato del usuario, buscará información relevante en el corpus jurídico, construirá el contexto para el modelo y organizará la respuesta final|
|Modelo (LLM)|OpenRouter — modelo gratuito| Será el modelo encargado de analizar el contrato y explicar los posibles riesgos jurídicos en lenguaje sencillo. Recibirá tanto el contrato como los fragmentos normativos recuperados por el sistema RAG.
|Memoria de fuentes (RAG)|Chroma durante el desarrollo; Supabase/pgvector si se requiere almacenamiento en la nube|Permitirá almacenar y buscar los fragmentos de las normas que alimentan CONTRATO CHECK. Así, el modelo podrá consultar el corpus jurídico seleccionado en lugar de depender únicamente de la información que aprendió durante su entrenamiento.|
|Corpus jurídico|Archivos .md o .txt dentro de corpus/|Contendrá las normas colombianas utilizadas por la herramienta, inicialmente la Ley 820 de 2003 y los artículos pertinentes del Código Civil colombiano. Cada fuente estará organizada para facilitar su recuperación y citación.|
|Trazabilidad (opcional)|LangSmith|Permitirá observar el funcionamiento interno de las consultas y detectar errores durante el desarrollo. No es indispensable para la primera versión, por lo que se incorporará únicamente si resulta necesario.|
|Seguridad|Variables de entorno (.env)|La clave de OpenRouter se almacenará como una variable de entorno y no se escribirá directamente en el código ni se publicará en GitHub.|

---

## 🚀 Parte 4 — Ruta de despliegue

Tu meta: **una URL pública** que cualquiera pueda abrir. Elige una ruta:

### Opción A — Vercel ⭐ (recomendada, la del curso)
1. Sube tu código a este repo de GitHub (ya lo tienes ✅).
2. Crea cuenta gratis en [vercel.com](https://vercel.com) con tu GitHub.
3. "Add New Project" → importa tu repo → Deploy.
4. Cada `git push` re-despliega solo.
- ✅ Ideal para Next.js/Streamlit (Streamlit via [streamlit.io/community-cloud](https://streamlit.io)) · gratis · sin servidor.

### Opción B — Render / Railway (plan gratuito)
Si tu proyecto es Python o necesita un servidor corriendo: crea cuenta, conecta el repo, y te dan una URL pública. Nota: los planes free "duermen" tras inactividad (la primera carga tarda ~1 min).

### Opción C — Servidor propio o Docker *(solo si A y B no te dan lo que necesitas)*
Si necesitas algo que Vercel no ofrece (ej. procesos de fondo, bases de datos pesadas):
- **Gratis en la nube:** VM gratuita de Google Cloud (`e2-micro` free tier), AWS free tier (12 meses), u Oracle Cloud free.
- **Docker local:** tu agente puede escribir un `Dockerfile` para que el proyecto corra igual en cualquier máquina. Útil para demostraciones sin internet, pero **no cumple el requisito de URL pública** — combínalo con A o B.

### Checklist de despliegue ✅
- [ ] URL pública funciona en el navegador de otra persona (pídele a alguien que la abra)
- [ ] La advertencia de la Parte 7 es **visible** en la interfaz
- [ ] No hay API keys ni secretos en el código (verifica con una búsqueda de `sk-` en el repo)
- [ ] Anota la URL aquí: **`[tu-url-publica]`**

> El dominio propio (.com, .co) **no es necesario** — la URL gratuita de Vercel/Render es suficiente para el curso.

---

## 🧠 Parte 5 — Guía de prompting para *vibe coding*

Tu competencia más transferible a la práctica profesional: **instruir bien a la IA**. Reglas:

1. **Un hito a la vez.** No le pidas "hazme todo el proyecto". Pide: "vamos por M1".
2. **Da contexto jurídico, recibe código.** Pega tu Parte 1 y dile: "eres mi ingeniero, yo soy el abogado del proyecto".
3. **Pide explicaciones.** "Explícame como a alguien que no sabe programar qué acabas de hacer."
4. **Commits frecuentes.** Cada vez que algo funcione: `git add . && git commit -m "M1: instrucciones del asistente"` y push. Si rompes algo, siempre puedes volver atrás.
5. **Nunca pegues datos personales reales** de usuarios en el chat ni en el código (Ley 1581).
6. **Verifica como abogado.** Toda respuesta legal que dé la herramienta, contrástala con la norma. Tú respondes por lo que publicas.


> Eres CONTRATO CHECK, una herramienta de asistencia jurídica orientativa para Colombia, desarrollada como ejercicio académico en la Pontificia Universidad Javeriana.
>
> Tu función es analizar el texto de contratos sencillos de arrendamiento de vivienda urbana o prestación de servicios que el usuario te comparte, e identificar:
>
> 1. **CLÁUSULAS ILEGALES O NULAS:** Aquellas que violan expresamente normas colombianas (Ley 820 de 2003, Código Civil). Ejemplo: exigir depósito en dinero en arrendamiento de vivienda (prohibido por Art. 16, Ley 820/2003).
> 2. **CLÁUSULAS RIESGOSAS O ABUSIVAS:** Aquellas que generan un desequilibrio grave en contra del usuario. Ejemplo: cláusulas penales desproporcionadas, terminación sin preaviso.
> 3. **CLÁUSULAS AMBIGUAS:** Redacción confusa que puede interpretarse de formas contradictorias y generar conflictos.
> 4. **CLÁUSULAS ESENCIALES FALTANTES:** Elementos que la ley exige o que son indispensables para proteger al usuario y que no aparecen en el contrato.
>
> **REGLAS:** Cita siempre la norma jurídica específica. Si no tienes norma que respalde un hallazgo, dilo explícitamente. Nunca inventes leyes ni artículos. Al final de cada análisis incluye siempre la advertencia: "⚠️ Este análisis es un ejercicio académico y NO constituye asesoría legal. Consulta con un abogado antes de firmar."
>
> **Corpus normativo:** Ley 820 de 2003, Código Civil colombiano, Código de Comercio.
---

## ⚖️ Parte 6 — Ética, datos y responsabilidad

Estas salvaguardas son **obligatorias** y hacen parte de la evaluación:

- **Advertencia visible obligatoria.** Tu interfaz debe mostrar, en lugar visible:
  > *"Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado."*
  - [ x] Implementada y visible en la interfaz
- **Protección de datos (Ley 1581 de 2012).** Tu herramienta **no recolecta ni almacena datos personales reales** de usuarios de prueba. Los usuarios de prueba usan situaciones ficticias o datos inventados.
  - [x ] Verificado: no guardo datos personales
- **Corpus público.** Solo fuentes públicas: leyes, decretos, jurisprudencia publicada.
  - [x ] Verificado
- **Anti-alucinaciones.** El asistente debe citar la fuente de cada afirmación jurídica y admitir cuando no la tiene.
  - [x ] Casos de prueba donde la herramienta se niega a inventar

---

## 🔍 Parte 7 — Análisis crítico (insumo de tu sustentación final)

Responde con total honestidad — aquí es donde demuestras tu criterio jurídico:

1. **¿Dónde falla tu herramienta?** Describe 2 situaciones donde se equivoca o se queda corta.
**Situación 1 — Contratos con lenguaje muy técnico o inusual:**
La herramienta detecta riesgos buscando patrones de palabras clave en el texto (como "depósito", "reajuste" o "terminación inmediata"). Si un contrato usa lenguaje muy técnico, latinismos jurídicos o redacción inusual para expresar la misma cláusula abusiva, la herramienta puede no detectarla. Por ejemplo, si un contrato dice "el locatario constituirá una garantía dineraria" en lugar de "el arrendatario pagará un depósito en dinero", el sistema podría no identificarlo como una violación al Artículo 16 de la Ley 820 de 2003.
**Situación 2 — Contratos de tipos no previstos:**
La herramienta fue diseñada específicamente para contratos de arrendamiento de vivienda urbana y prestación de servicios simples. Si un usuario carga un contrato de compraventa, una promesa de contrato, un acuerdo de confidencialidad o un contrato laboral, el análisis será superficial e impreciso, ya que las reglas jurídicas que lo rigen son completamente diferentes.
2. **¿Qué datos procesa?** Qué entra, qué se guarda, qué sale.
**Qué entra:** El texto del contrato que el usuario pega o escribe directamente en la interfaz web. También el tipo de contrato seleccionado (arrendamiento o servicios).
- **Qué se guarda:** Nada. La herramienta no tiene base de datos ni servidor propio. El análisis ocurre en el navegador del usuario y no se transmite ni almacena ninguna información.
- **Qué sale:** Un diagnóstico con nivel de riesgo (alto/medio/bajo), listado de hallazgos con citas normativas específicas y recomendaciones para negociar antes de firmar.
3. **¿Por qué no reemplaza al abogado?** Argumenta en 5–8 frases.

---CONTRATO CHECK es una herramienta orientativa que identifica patrones de riesgo basados en reglas predefinidas, pero no puede ejercer el juicio profesional que requiere el derecho. Un abogado no solo conoce la ley, sino que la interpreta en contexto: evalúa la capacidad de las partes, la validez del consentimiento, el historial del contratante, el entorno económico del negocio y las implicaciones fiscales y procesales de cada cláusula. La herramienta no conoce al usuario, no sabe si firmó bajo presión, si tiene antecedentes contractuales con la contraparte ni si existe una relación de poder desigual. Además, el derecho colombiano evoluciona constantemente con nuevas sentencias de la Corte Suprema y la Corte Constitucional que la herramienta no puede incorporar en tiempo real. Por estas razones, CONTRATO CHECK es útil como primera lectura orientativa antes de una consulta profesional, pero nunca como sustituto de ella.

## ✅ Parte 8 — Entregables finales (Definition of Done)

Requisitos de entrega del curso — todos deben estar ✅:

- [ ] 🔗 **Solución funcionando**: CONTRATO CHECK está desplegada con URL pública en Vercel y permite analizar contratos de arrendamiento detectando cláusulas ilegales con citas a la Ley 820 de 2003.
- [ ] 👤 **Usuario real**: al menos una persona externa al curso la usó, con evidencia (video corto o testimonio). Guarda la evidencia en `docs/evidencia-usuario.md`.
- [ ] 📦 **Repositorio con historial**: este repo muestra tus avances semanales (commits + bitácora).
- [ ] 🧠 **Análisis crítico**: Parte 7 completada.
- [ ] 📋 Partes 1–7 de este README completas y al día.

---

*Construido con asistencia de IA — como se enseña en este curso.* 🧑‍⚖️🤖
