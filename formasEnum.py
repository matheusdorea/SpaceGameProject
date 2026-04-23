from enum import Enum


class Formas:
    # Nave do jogador — triângulo apontando para cima (eixo local)
    FORMA_NAVE = [
        (0,  -20),   # ponta
        (-12, 12),   # base esquerda
        (12,  12),   # base direita
    ]

    # Nave inimiga — formato diferente para distinguir
    FORMA_INIMIGA = [
        (0,   15),
        (-15, -10),
        (0,   -5),
        (15,  -10),
    ]

    # Nave mãe — maior, hexagonal
    FORMA_MAE = [
        (0,  -40),
        (35, -20),
        (35,  20),
        (0,   40),
        (-35, 20),
        (-35,-20),
    ]