
# Sistema de Análisis de Ventas

Proyecto académico desarrollado para la materia de Gestión Colaborativa, Control de Versiones y Organización Empresarial utilizando Git, GitHub, Jira y Python.

---

## Integrantes del Equipo

- Lucas Perez – Líder de Proyecto
- Lucas Perez – Desarrollador
- Lucas Perez – QA Tester

---

## Escenario Elegido

### Escenario B – Análisis de Ventas de una Pequeña Empresa

El proyecto tiene como objetivo analizar información de ventas para generar indicadores básicos que permitan interpretar el desempeño comercial de la empresa.

---

## Dataset Utilizado

Se utilizó un dataset de ventas simuladas en formato CSV con información de:

- fecha de venta
- monto de ventas
- identificador de registro

Ejemplo de estructura:

| id | sales_date | sales_amount |
|----|------------|---------------|
| 2 | 2024-01-01 | 4986 |
| 3 | 2024-01-02 | 5143 |

El dataset fue almacenado dentro de la carpeta:

datos/ventas.csv

---

## Estructura del Proyecto

repo-proyecto/

├── datos/
│   └── ventas.csv

├── scripts/
│   └── analisis_ventas.py

├── resultados/
│   ├── grafico_ventas.png
│   └── resumen_ventas.csv

├── README.md

└── .gitignore

---

## Funcionalidades Implementadas

El sistema permite:

- importar el dataset de ventas
- calcular ventas totales
- calcular promedio de ventas
- identificar ventas máximas y mínimas
- identificar períodos de mayor volumen de ventas
- generar gráficos de evolución temporal
- exportar resultados del análisis

---

## Tecnologías Utilizadas

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Jira
- Google Colab

---

## Instrucciones de Ejecución

### 1. Clonar repositorio

git clone <URL_DEL_REPOSITORIO>

### 2. Ingresar al proyecto

cd repo-proyecto

### 3. Ejecutar script principal

python scripts/analisis_ventas.py

---

## Resultados Generados

### Gráfico de evolución de ventas

resultados/grafico_ventas.png

### Resumen estadístico exportado

resultados/resumen_ventas.csv

---

## Flujo de Trabajo Utilizado

Durante el desarrollo se utilizó un flujo de trabajo basado en Scrum utilizando Jira para:

- gestión de historias de usuario
- planificación de sprint
- seguimiento de subtareas
- validación QA
- trazabilidad entre tareas y commits

Además, se utilizaron ramas Git y Pull Requests para simular un entorno colaborativo de desarrollo.

---

## Buenas Prácticas Aplicadas

- uso de ramas feature
- commits descriptivos asociados a Jira
- revisión QA
- documentación técnica
- estructura organizada del repositorio
- uso de rutas relativas para compatibilidad con Google Colab

---
