# Laboratorio 2 – MapReduce con Docker y Python

**Profesor:** Heberth Martínez  
**Tecnologías:** Python, Docker y Docker Compose

## Descripción

En este laboratorio se implementó MapReduce utilizando Python y Docker para procesar archivos CSV y calcular estadísticas agrupadas por categoría y subcategoría.

## Estructura del proyecto

```text
average-by-category/
├── docker-compose.yml
├── Dockerfile
├── mapper.py
├── reducer.py
├── README.md
└── input/
    ├── data.csv
    ├── data2.csv
    └── data_grande.csv
```

## Funcionalidades implementadas

1. **Agrupación por dos columnas:** cálculo del promedio por categoría y subcategoría.
2. **Desviación estándar:** el Reducer calcula el promedio, la desviación estándar poblacional y la cantidad de registros.
3. **Múltiples archivos CSV:** procesamiento automático de archivos ubicados en `input/`, utilizando ordenamiento externo y cálculos incrementales para manejar volúmenes mayores de datos.

## Funcionamiento

- **Mapper:** lee los archivos CSV y organiza los registros.
- **Sort:** ordena los datos por categoría y subcategoría.
- **Reducer:** calcula las estadísticas de cada grupo.

## Ejecución

Desde la carpeta principal del proyecto:

```bash
docker compose up --build
```

## Resultados de la prueba

| Categoría | Subcategoría | Promedio | Desviación | Cantidad |
|---|---|---:|---:|---:|
| A | X | 4.67 | 1.25 | 3 |
| A | Y | 6.00 | 0.00 | 1 |
| B | X | 6.00 | 1.00 | 2 |
| B | Y | 2.00 | 0.00 | 1 |
| C | X | 4.00 | 0.00 | 1 |

La ejecución en Docker finalizó correctamente (`exit code 0`).

## Conclusión

Este laboratorio permitió comprender el funcionamiento de MapReduce mediante sus etapas Mapper, Sort y Reducer. También se implementaron cálculos estadísticos y el procesamiento de múltiples archivos CSV utilizando Python dentro de un contenedor Docker.
