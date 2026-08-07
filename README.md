# P0-Mosqueira-Javiera

Proyecto 0 — Introducción al benchmarking y al trabajo con agentes de IA.
Ramo: Métodos Computacionales en Ingeniería en Obras Civiles.

## Propósito general del proyecto

El objetivo de este proyecto es preparar un ambiente de trabajo para el resto
del curso e introducir una forma de desarrollo basada en agentes de inteligencia
artificial (OpenCode). El proyecto incluye:

- investigar las características del computador (`src/system_info.py`);
- implementar una multiplicación de matrices con ciclos explícitos de Python
  (`src/mimatmul.py`);
- verificar esa implementación con pruebas automáticas
  (`tests/test_mimatmul.py`);
- comparar su rendimiento contra la operación optimizada de NumPy mediante un
  benchmark (`src/benchmark.py`).

## Computador

Características del equipo evaluado (obtenidas con `src/system_info.py` y
verificadas con herramientas del sistema operativo):

- Sistema operativo: Windows 11 (arquitectura AMD64)
- Versión de Python: 3.14.7
- Procesador: Intel(R) Core(TM) Ultra 9 185H
- Núcleos físicos: 16 · Procesadores lógicos: 22
- Memoria RAM total: 31.42 GB
- GPU: NVIDIA GeForce RTX 4070 Laptop GPU + Intel(R) Arc(TM) Graphics

Los datos completos se encuentran en `data/system_info.json`.

## Instalación

Comandos para crear y activar el ambiente virtual (PowerShell):

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Para instalar las dependencias:

```
pip install -r requirements.txt
```

## Ejecución

Ejecutar las pruebas automáticas:

```
pytest
```

Obtener la información del computador:

```
python src\system_info.py
```

(El comando del benchmark se agregará cuando se implemente la Etapa 4.)

## Resultados

(En construcción: se agregarán el archivo `data/benchmark_results.csv` y la
figura `figures/benchmark.png`.)

## Uso de OpenCode

(En construcción: reflexión sobre el trabajo con el agente.)

## Estado actual del proyecto

- Etapa 1 (ambiente de desarrollo): completada.
- Etapa 2 (información del computador): completada.
- Etapa 3 (implementación de `mimatmul` y pruebas): completada (5 pruebas en verde).
- Etapa 4 (benchmark): pendiente.
- Etapa 5 (documentación y revisión final): pendiente.
