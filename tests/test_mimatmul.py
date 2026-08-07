import numpy as np
import pytest

from src.mimatmul import mimatmul


def test_caso_pequeno_conocido():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    resultado = mimatmul(A, B)
    assert np.allclose(resultado, [[19, 22], [43, 50]])


def test_matrices_cuadradas():
    A = [[2, 0, 1], [3, 0, 0], [5, 1, 1]]
    B = [[1, 0, 1], [1, 2, 1], [1, 1, 0]]
    resultado = mimatmul(A, B)
    assert np.allclose(resultado, [[3, 1, 2], [3, 0, 3], [7, 3, 6]])


def test_matrices_rectangulares():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    resultado = mimatmul(A, B)
    assert np.allclose(resultado, [[58, 64], [139, 154]])


def test_comparacion_con_numpy():
    A = np.array([[1, 0, 2, -1], [3, 1, 0, 2], [-2, 1, 1, 0]])
    B = np.array([[1, 2], [0, 1], [3, -1], [1, 0]])
    assert np.allclose(mimatmul(A, B), A @ B)


def test_dimensiones_incompatibles():
    A = [[1, 2], [3, 4]]
    B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(ValueError, match="incompatibles"):
        mimatmul(A, B)
