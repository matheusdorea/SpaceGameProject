from coresEnum import Cores
from formasEnum import Formas
from config import ALTURA, LARGURA, desenhar_poligono
from transformacoes import *


class Nave:
    """Nave controlada pelo jogador."""
    VELOCIDADE     = 4
    VEL_ROTACAO    = 4    # graus por frame
    COOLDOWN_TIRO  = 20   # frames entre tiros

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.escala = 1.0
        self.vidas = 3
        self._cooldown = 0
        self.refletida = False

    # ------ transformações ------

    def _pontos_transformados(self):
        """
        Pipeline de transformação:
          1. Escala
          2. Rotação
          3. Reflexão (opcional)
          4. Translação para posição mundial
        """
        M_escala   = matriz_escala(self.escala, self.escala)
        M_rotacao  = matriz_rotacao(self.angulo)
        M_reflexao = matriz_reflexao("y") if self.refletida else np.eye(3)
        M_trans    = matriz_translacao(self.x, self.y)

        # Composição: aplica da direita para a esquerda
        M = M_trans @ M_reflexao @ M_rotacao @ M_escala

        return aplicar_transformacao(Formas.FORMA_NAVE, M)
    
    def girar(self, direcao):
        """direcao: +1 (horário) ou -1 (anti-horário)."""
        self.angulo += direcao * self.VEL_ROTACAO

    def mover_frente(self):
        a = radians(self.angulo)
        dx = -sin(a) * self.VELOCIDADE
        dy = -cos(a) * self.VELOCIDADE
        self.x = (self.x + dx) % LARGURA   # wrap de tela
        self.y = (self.y + dy) % ALTURA

    def mover_tras(self):
        a = radians(self.angulo)
        dx = sin(a) * self.VELOCIDADE
        dy = cos(a) * self.VELOCIDADE
        self.x = (self.x + dx) % LARGURA
        self.y = (self.y + dy) % ALTURA


    def desenhar(self, superficie):
        pontos = self._pontos_transformados()
        desenhar_poligono(superficie, Cores.CIANO, pontos)