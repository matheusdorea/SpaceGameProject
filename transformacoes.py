import numpy as np
from math import cos, sin, radians


def matriz_translacao(dx, dy):
    """Translação via matriz homogênea."""
    return np.array([
        [1, 0, dx],
        [0, 1, dy],
        [0, 0,  1]
    ], dtype=float)

def matriz_rotacao(angulo_graus):
    """Rotação em torno da origem."""
    a = radians(angulo_graus)
    return np.array([
        [cos(a), -sin(a), 0],
        [sin(a),  cos(a), 0],
        [0,       0,      1]
    ], dtype=float)

def matriz_escala(sx, sy):
    """Escala uniforme ou não-uniforme."""
    return np.array([
        [sx, 0,  0],
        [0,  sy, 0],
        [0,  0,  1]
    ], dtype=float)

def matriz_reflexao(eixo="x"):
    """Reflexão em relação ao eixo x ou y."""
    if eixo == "x":
        return np.array([
            [1,  0, 0],
            [0, -1, 0],
            [0,  0, 1]
        ], dtype=float)
    else:  # eixo y
        return np.array([
            [-1, 0, 0],
            [0,  1, 0],
            [0,  0, 1]
        ], dtype=float)

def aplicar_transformacao(pontos, matriz):
    """
    Recebe lista de pontos (x, y) e uma matriz 3x3.
    Retorna os pontos transformados.
    """
    resultado = []
    for (x, y) in pontos:
        v = np.array([x, y, 1], dtype=float)
        t = matriz @ v
        resultado.append((t[0], t[1]))
    return resultado