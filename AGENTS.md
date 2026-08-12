# AGENTS.md

Instrucciones permanentes para OpenCode en el proyecto P0-Mosqueira-Javiera.

## Propósito del proyecto

Proyecto 0 del ramo Métodos Computacionales en Ingeniería en Obras Civiles.
Introducción al benchmarking y al trabajo con agentes de IA (OpenCode).
Incluye información del computador, una multiplicación de matrices implementada
con ciclos de Python, pruebas automáticas, un benchmark y un gráfico de resultados.

## Estructura del repositorio

```
P0-Mosqueira-Javiera/
├── README.md
├── AGENTS.md
├── requirements.txt
├── src/
│   ├── system_info.py
│   ├── mimatmul.py
│   └── benchmark.py
├── tests/
│   └── test_mimatmul.py
├── data/
│   ├── system_info.json
│   └── benchmark_results.csv
└── figures/
    └── benchmark.png
```

## Comandos importantes

- Ejecutar las pruebas: `python -m pytest`
- Ejecutar el benchmark: `python src/benchmark.py`
- Ejecutar la información del computador: `python src/system_info.py`

## Reglas

- Mantener el código sencillo, ejecutable y fácil de explicar.
- Prohibido inventar mediciones, resultados o información del computador.
- Conservar los datos originales generados (data/) y las figuras (figures/).
- Ejecutar las pruebas después de modificar el código.
- Prohibido crear matrices que puedan agotar la memoria.
- Prohibido realizar operaciones destructivas de Git (force push, reset hard, etc.).
- OpenCode no debe realizar commits ni push sin autorización explícita del usuario.
- Prohibido subir claves de API, contraseñas, llaves SSH, tokens, credenciales o información privada al repositorio.

