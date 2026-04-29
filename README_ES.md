# Análisis de Mercado de Videojuegos

## Resumen Ejecutivo

Este proyecto analiza ventas históricas de videojuegos para identificar patrones útiles en planeación comercial y campañas de marketing. El enfoque es de inteligencia de mercado, no solo de exploración descriptiva.

El análisis estudia ciclos de vida de plataformas, rentabilidad por género, diferencias regionales, relación entre reseñas y ventas, y pruebas estadísticas sobre calificaciones de usuarios.

## Problema de Negocio

Una tienda online de videojuegos necesita identificar plataformas, géneros y regiones con mayor potencial comercial para planear campañas futuras.

La pregunta central es:

> ¿Qué señales de mercado ayudan a identificar juegos y segmentos con mayor potencial de éxito?

## Objetivo Técnico

Limpiar, analizar e interpretar datos históricos de ventas de videojuegos mediante un flujo reproducible en Python. El análisis se enfoca en:

- evolución de ventas por plataforma
- momentum reciente de plataformas
- ventas globales y regionales
- desempeño por género
- relación entre reseñas y ventas
- pruebas de hipótesis sobre calificaciones de usuarios

## Dataset

El dataset contiene registros de videojuegos con columnas como:

| Columna | Significado |
|---|---|
| `Name` | Título del juego |
| `Platform` | Consola o plataforma |
| `Year_of_Release` | Año de lanzamiento |
| `Genre` | Género |
| `NA_sales` | Ventas en Norteamérica, en millones |
| `EU_sales` | Ventas en Europa, en millones |
| `JP_sales` | Ventas en Japón, en millones |
| `Other_sales` | Ventas en otras regiones, en millones |
| `Critic_Score` | Calificación de críticos sobre 100 |
| `User_Score` | Calificación de usuarios sobre 10 |
| `Rating` | Clasificación ESRB |

## Metodología

### 1. Preparación de Datos

El pipeline normaliza nombres de columnas, convierte años y calificaciones a formato numérico, trata valores `tbd` como faltantes, rellena clasificaciones ESRB faltantes como `Unknown` y calcula `global_sales` como suma de ventas regionales.

### 2. Ciclo de Vida de Plataformas

El proyecto estima cómo las plataformas suben, alcanzan su pico y caen con el tiempo. Esto permite separar plataformas obsoletas de plataformas relevantes para planeación futura.

### 3. Selección de Ventana de Mercado

Se usa una ventana reciente para que el análisis sea más útil en decisiones prospectivas. Los datos antiguos ayudan a entender ciclos, pero los años recientes tienen mayor valor comercial.

### 4. Desempeño por Plataforma y Género

El análisis compara ventas por plataforma y género para identificar segmentos de mayor impacto.

### 5. Perfiles Regionales

Norteamérica, Europa y Japón se analizan por separado según plataformas, géneros y clasificaciones ESRB principales. Esto muestra dónde conviene localizar la estrategia.

### 6. Señales de Reseñas

Se revisan correlaciones entre calificaciones de críticos/usuarios y ventas. En general, las reseñas de críticos suelen estar más asociadas a ventas que las de usuarios.

### 7. Pruebas de Hipótesis

Se comparan dos casos:

1. Calificaciones promedio de usuarios para Xbox One y PC.
2. Calificaciones promedio de usuarios para juegos de Acción y Deportes.

Se usa prueba de Levene para evaluar igualdad de varianzas antes de aplicar la prueba t independiente.

## Resultados

Hallazgos principales:

- El ciclo de vida de plataformas importa: dominar antes no implica seguir siendo relevante.
- Las plataformas recientes son más útiles para campañas futuras que plataformas históricas.
- El desempeño por género cambia entre regiones.
- Japón tiene preferencias distintas a Norteamérica y Europa.
- Las calificaciones de críticos suelen ser más informativas comercialmente que las de usuarios.
- Las pruebas de hipótesis añaden disciplina estadística más allá de la comparación visual.

## Impacto

Este proyecto puede apoyar:

- segmentación de campañas
- planeación de inventario
- priorización de mercados
- decisiones por plataforma/género
- estrategia regional de marketing

## Estructura del Repositorio

```text
video-game-market-analysis/
├── data/
│   └── games.csv
├── notebooks/
│   ├── project_EN.ipynb
│   └── project_ES.ipynb
├── src/
│   ├── preprocessing.py
│   ├── analysis.py
│   └── hypothesis.py
├── reports/
│   └── figures/
├── README.md
├── README_EN.md
├── README_ES.md
├── docs/
├── requirements.txt
└── .gitignore
```

## Cómo Ejecutar

```bash
pip install -r requirements.txt
jupyter notebook notebooks/project_ES.ipynb
```

## Próximos Pasos

- Agregar modelo predictivo para estimar nivel esperado de ventas.
- Crear dashboard para comparar plataformas y géneros.
- Incorporar datos de mercado más recientes.
- Añadir variables de publisher/desarrollador si están disponibles.
- Extender pruebas estadísticas con alternativas no paramétricas.
