from enum import Enum


class Cores(tuple, Enum):
    PRETO  = (0,   0,   0)
    BRANCO = (255, 255, 255)
    VERDE  = (0,   255, 0)
    VERMELHO = (255, 0,   0)
    AMARELO  = (255, 255, 0)
    CIANO  = (0,   255, 255)