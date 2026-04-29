from math import cos, radians, sin

import pygame

from config import ALTURA, LARGURA
from coresEnum import Cores
from transformacoes import *


class Projetil:
    VELOCIDADE = 10
    RAIO = 4

    def __init__(self, x, y, angulo):
        self.x = x
        self.y = y
        self.angulo = angulo
        a = radians(angulo)
        self.vx = sin(a) * self.VELOCIDADE
        self.vy = -cos(a) * self.VELOCIDADE

    def atualizar(self):
        T = matriz_translacao(self.vx, self.vy)
        [(self.x, self.y)] = aplicar_transformacao([(self.x, self.y)], T)

    def fora_da_tela(self):
        return (self.x < 0 or self.x > LARGURA or
                self.y < 0 or self.y > ALTURA)

    def desenhar(self, superficie):
        pygame.draw.circle(superficie, Cores.AMARELO, (int(self.x), int(self.y)), self.RAIO)