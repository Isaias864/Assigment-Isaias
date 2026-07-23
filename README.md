# InvesTrack — Panel de seguimiento de cartera de inversión

Aplicación web que carga una cartera de inversión, calcula su rendimiento total como KPI principal y ofrece herramientas de análisis y proyección financiera.

**App en vivo:** https://assigment-isaias.vercel.app/
**Repositorio:** https://github.com/Isaias864/Assigment-Isaias

---

## Qué hace

- Calcula el **KPI principal**: rendimiento total de la cartera en porcentaje.
- Muestra el desglose de ganancia o pérdida por cada activo con barras bidireccionales.
- Calcula un **score de diversificación** basado en el índice de concentración Herfindahl-Hirschman.
- Incluye un **cuestionario de perfil de riesgo** que despliega una cartera modelo de ejemplo con fines educativos.
- Ofrece un **proyector de interés compuesto** y una **calculadora de meta de ahorro**.

> Aviso: es un proyecto académico con datos de ejemplo. No constituye asesoría de inversión.

---

## Stack técnico

| Capa | Tecnología | Función en el proyecto |
|---|---|---|
| Interfaz | HTML5, CSS3 | Estructura y diseño. Variables CSS para el sistema de color, CSS Grid para el layout responsivo. |
| Lógica | JavaScript (vanilla, ES6) | Cálculo del KPI, diversificación, interés compuesto y meta de ahorro. Renderizado dinámico del DOM. |
| Datos | CSV + respaldo en código | `portfolio.csv` se carga con `fetch`. Si falla, se usa una tabla definida en el código. |
| Validación | Python + Pandas | `kpi_pandas.py` recalcula el KPI de forma independiente para verificar la fórmula. |
| Versionado | Git + GitHub | Control de versiones con commits por etapa. |
| Hosting | Vercel | Despliegue continuo: reconstruye automáticamente en cada push a `main`. |
| Copiloto IA | Claude (Anthropic) | Generación de código, explicación de conceptos y diagnóstico de errores. |
| Editor | Cursor / VSCode | Edición de código y terminal para comandos Git. |

### Estructura de archivos

```
/
├── index.html                    # Aplicación completa (HTML + CSS + JS)
├── portfolio.csv                 # Datos de la cartera
├── kpi_pandas.py                 # Verificación del KPI con Pandas
├── DOCUMENTO_DE_PLANEACION.md    # Documento de planeación del proyecto
└── README.md                     # Este archivo
```

### Decisiones técnicas

**JavaScript vanilla en lugar de un framework.** El flujo de datos es lineal: se cargan datos, se calculan métricas, se pintan. React habría añadido compilación y dependencias sin resolver ningún problema real del proyecto.

**Vercel en lugar de GitHub Pages.** Se eligió por su despliegue automático desde GitHub y porque sus logs de build son legibles, lo cual fue clave para diagnosticar el fallo controlado de despliegue.

**Cálculo en el cliente.** Toda la aritmética corre en el navegador, lo que permite servir la app como sitio estático: respuesta instantánea y sin servidor que mantener.

---

## Bitácora de desarrollo

| Etapa | Qué se hizo | Checkpoint superado |
|---|---|---|
| 1 | Estructura del proyecto y esqueleto HTML | Abre en local sin errores de consola |
| 2 | `git init`, repositorio en GitHub, primer push | Archivos visibles en GitHub |
| 3 | Importación y despliegue en Vercel | URL pública responde |
| 4 | Carga de datos, cálculo del KPI y desglose por activo | KPI en pantalla coincide con el de Pandas |
| 5 | Diversificación, perfil de riesgo, proyector y meta de ahorro | Calculadoras responden bien ante casos borde |
| 6 | Fallo de despliegue controlado y corrección | Historial de Vercel con intento fallido y exitoso |

---

## Uso de IA en el desarrollo

Todo el proyecto se desarrolló usando **Claude** como copiloto. La IA no se utilizó como generador ciego de código: cada bloque se revisó, se probó en el navegador y se validó numéricamente antes de integrarlo.

### Prompts principales utilizados

**1. Definición del proyecto**
> "Necesito hacer una app web para mi clase, algo de finanzas, de invertir. Dame una idea que esté interesante y que sirva para mostrar un KPI."

Este prompt derivó en la definición del alcance y en la elección del rendimiento total de la cartera como KPI principal.

**2. Construcción de la aplicación base**
> "Ayúdame paso a paso a crear la aplicación, bien explicado."

Se generó `index.html` con la carga de datos, el cálculo del KPI y el desglose por activo, junto con el CSV y el script de verificación en Pandas.

**3. Ampliación de funcionalidades**
> "¿Cómo podemos mejorar la app y meterle más cosas? Un plan financiero, recomendar en qué invertir, ETFs o algo así."

Aquí la IA señaló un límite importante: recomendar instrumentos concretos sería asesoría financiera, algo que no corresponde a un proyecto académico. La propuesta se reformuló hacia un cuestionario de perfil de riesgo con carteras modelo etiquetadas explícitamente como material educativo. **Esta corrección de rumbo cambió el diseño del producto** y quedó reflejada en el alcance del documento de planeación.

**4. Depuración**
> "No me aparece nada en GitHub." / "Se queda cargando, no me carga."

La IA guió un diagnóstico por descarte: verificar con `git status` y `git log`, identificar que el commit existía pero no se había empujado al remoto, y resolverlo con `git push -u origin main`. En el segundo caso, comprobar el estado del despliegue en Vercel permitió determinar que la aplicación sí estaba publicada y que el problema era de caché del navegador.

### Limitaciones observadas de la IA

- **No siempre distingue el contexto exacto del error.** En un momento reporté un mensaje de "not found" y la IA asumió que se refería al script de Python cuando en realidad hablaba de otra cosa. Hizo falta que yo precisara la situación para que el diagnóstico fuera correcto.
- **Genera código con supuestos del entorno que no siempre se cumplen.** El primer script de Pandas leía el CSV desde una URL, pero el kernel donde debía ejecutarse no tenía acceso a internet. Hubo que sustituirlo por una versión con los datos definidos en el código.
- **Deja marcadores de posición.** El script traía `TU-APP.vercel.app` como ejemplo y hay que reemplazarlo por el dominio real; copiarlo tal cual produce un error.

La conclusión práctica es que la IA acelera mucho la escritura de código, pero la verificación y el criterio sobre qué construir siguen siendo responsabilidad de quien desarrolla.

---

## Reproducir el proyecto en local

```bash
git clone https://github.com/Isaias864/Assigment-Isaias.git
cd Assigment-Isaias

# Servir con un servidor local para que el CSV cargue correctamente
python3 -m http.server 8000
# Abrir http://localhost:8000
```

Abrir `index.html` con doble clic también funciona, pero el navegador bloquea la lectura del CSV por el protocolo `file://` y la app usará los datos de respaldo.

Para verificar el KPI con Pandas:

```bash
python3 kpi_pandas.py
```

---

## Autoevaluación

**Lo que salió bien.** El proyecto quedó desplegado, público y funcional, con un KPI que se calcula correctamente y se verifica por dos vías independientes. El desarrollo siguió etapas con checkpoints reales en lugar de improvisarse, y el historial de commits refleja ese proceso. La aplicación maneja casos borde que en una primera versión habrían tronado: tasa cero, plazo cero, meta ya alcanzada y fallo en la carga del CSV.

**Lo que me costó.** La parte de Git fue lo más difícil. Tuve un momento en que el commit estaba hecho pero nada aparecía en GitHub, y no entendía por qué. Aprendí que hacer commit y hacer push son cosas distintas: el commit guarda en mi computadora, el push es lo que manda el código al servidor. También perdí tiempo con un problema que resultó ser caché del navegador, cuando la app llevaba rato bien publicada.

**Lo que haría distinto.** Escribiría el documento de planeación **antes** de empezar a programar y no después. En este proyecto la lógica funcionó, pero fue porque el alcance era pequeño; en algo más grande, programar sin plano habría sido caro. También separaría el CSS y el JavaScript en archivos aparte para que el proyecto escale mejor.

**Qué sigue.** El paso natural sería conectar una API de precios para que los valores se actualicen solos, y agregar persistencia para que el usuario pueda guardar su propia cartera en vez de usar los datos de ejemplo.
