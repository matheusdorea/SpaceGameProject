from math import radians, degrees, atan2, sin, cos
from config import desenhar_poligono
from coresEnum import Cores
from formasEnum import Formas
from transformacoes import *


class NaveInimiga:
    VELOCIDADE = 1.5

    def __init__(self, x, y, escala=1.0):
        self.x = x
        self.y = y
        self.escala = escala
        self.angulo = 0
        self.viva = True

    def pontos_transformados(self):
        M = matriz_translacao(self.x, self.y) @ matriz_rotacao(self.angulo) @ matriz_escala(self.escala, self.escala)
        return aplicar_transformacao(Formas.FORMA_INIMIGA, M)

    def atualizar(self, alvo_x, alvo_y):
        #perseguição simples
        dx = alvo_x - self.x
        dy = alvo_y - self.y
        angulo_alvo = degrees(atan2(-dx, dy))
        self.angulo = angulo_alvo
        a = radians(self.angulo)
        self.x += -sin(a) * self.VELOCIDADE
        self.y +=  cos(a) * self.VELOCIDADE

    def colidiu_com(self, outro_x, outro_y, raio = 20):
        dist = ((self.x - outro_x)**2 + (self.y - outro_y)**2) ** 0.5
        return dist < raio

    def desenhar(self, superficie):
        pontos = self.pontos_transformados()
        desenhar_poligono(superficie, Cores.VERMELHO, pontos)