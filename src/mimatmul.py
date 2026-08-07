import numpy as np


def mimatmul(A, B):
    """Multiplica dos matrices usando ciclos explícitos de Python."""
    A = np.asarray(A)
    B = np.asarray(B)

    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("mimatmul solo acepta matrices bidimensionales")

    filas_a, columnas_a = A.shape
    filas_b, columnas_b = B.shape

    if columnas_a != filas_b:
        raise ValueError(
            f"dimensiones incompatibles: A es {A.shape} y B es {B.shape}; "
            f"se requiere columnas de A ({columnas_a}) iguales "
            f"a filas de B ({filas_b})"
        )

    C = np.zeros((filas_a, columnas_b))
    for i in range(filas_a):
        for j in range(columnas_b):
            suma = 0.0
            for k in range(columnas_a):
                suma += A[i, k] * B[k, j]
            C[i, j] = suma
    return C
