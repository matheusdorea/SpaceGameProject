import pygame
from pygame.locals import *
from sys import exit
import numpy as np
from math import cos, sin, radians

from coresEnum import Cores
from estadosEnum import Estados

# ============================================================
# CONFIGURAÇÕES GLOBAIS
# ============================================================
pygame.init()

# Definindo tamanho da tela
LARGURA, ALTURA = 900, 700
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Defender")

clock = pygame.time.Clock()
FPS = 60

def main():
    # Definindo estado inicial do jogo
    estado = Estados.ESTADO_JOGANDO

    while True:
        clock.tick(FPS)

        # ---------- EVENTOS ----------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        if estado == Estados.ESTADO_JOGANDO:
            TELA.fill(Cores.PRETO)


        pygame.display.flip()

if __name__ == "__main__":
    main()