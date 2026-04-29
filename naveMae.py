from config import LARGURA, desenhar_poligono
from coresEnum import Cores
from formasEnum import Formas
from transformacoes import *

class NaveMae:
    COUNTDOWN_INIMIGO = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.escala = 1
        self.hp = 10
        self.viva = True
        self._sentido_escala = 1
        self._cooldown = 0
        self.novo_inimigo = False
        self.direcao = 1

    def pontos_transformados(self):
        M = (matriz_translacao(self.x, self.y) @
             matriz_rotacao(self.angulo) @
             matriz_escala(self.escala, self.escala))
        return aplicar_transformacao(Formas.FORMA_MAE, M)

    def atualizar(self):
        self.angulo += 0.5    # rotação constante (demonstra rotação)

        self._cooldown -= 1

        if self._cooldown <= 0:
            self.novo_inimigo = True
            self._cooldown = self.COUNTDOWN_INIMIGO
        
        # Movimentação da nave
        self.x += 1 * self.direcao
        if self.x >= LARGURA - 50 or self.x <= 50:
            self.direcao *= -1

        # Pulsação de escala — demonstra escala dinâmica
        self.escala += 0.005 * self._sentido_escala
        if self.escala >= 1.4 or self.escala <= 0.8:
            self._sentido_escala *= -1
    
    def colidiu_com(self, px, py, raio=45):
        dist = ((self.x - px)**2 + (self.y - py)**2) ** 0.5
        return dist < raio * self.escala

    def receber_dano(self):
        self.hp -= 1
        if self.hp <= 0:
            self.viva = False

    def desenhar(self, superficie):
        pontos = self.pontos_transformados()
        cor = Cores.VERDE if self.hp > 5 else Cores.VERMELHO
        desenhar_poligono(superficie, cor, pontos)