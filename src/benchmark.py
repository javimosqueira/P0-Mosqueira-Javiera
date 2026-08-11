import csv
import os
import sys
import time

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.mimatmul import mimatmul

TAMANOS = [32, 64, 96, 128, 160, 192]
REPETICIONES = 3


def medir(func, A, B):
    """Mide los segundos que tarda func(A, B) usando un reloj de alta resolución."""
    inicio = time.perf_counter()
    func(A, B)
    fin = time.perf_counter()
    return fin - inicio


rng_cal = np.random.default_rng(1)
A_cal = rng_cal.random((16, 16))
B_cal = rng_cal.random((16, 16))
mimatmul(A_cal, B_cal)
A_cal @ B_cal

filas = []
for n in TAMANOS:
    rng = np.random.default_rng(n)
    A = rng.random((n, n))
    B = rng.random((n, n))
    for rep in range(1, REPETICIONES + 1):
        filas.append(["mimatmul", n, rep, medir(mimatmul, A, B)])
        filas.append(["numpy", n, rep, medir(lambda a, b: a @ b, A, B)])

os.makedirs("data", exist_ok=True)
os.makedirs("figures", exist_ok=True)

with open("data/benchmark_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["metodo", "tamano", "repeticion", "tiempo_segundos"])
    writer.writerows(filas)

por_metodo = {"mimatmul": {}, "numpy": {}}
for metodo, n, rep, t in filas:
    por_metodo[metodo].setdefault(n, []).append(t)

plt.figure(figsize=(8, 5))
for metodo, color in [("mimatmul", "tab:blue"), ("numpy", "tab:orange")]:
    ns = sorted(por_metodo[metodo])
    medias = [sum(por_metodo[metodo][n]) / len(por_metodo[metodo][n]) for n in ns]
    for n, valores in por_metodo[metodo].items():
        plt.scatter([n] * len(valores), valores, color=color, alpha=0.5, s=20)
    plt.plot(ns, medias, marker="o", color=color, label=metodo)

plt.xlabel("Tamaño de la matriz (n × n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Benchmark: mimatmul vs NumPy")
plt.yscale("log")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("figures/benchmark.png", dpi=150)
print("Resultados guardados en data/benchmark_results.csv y figures/benchmark.png")
