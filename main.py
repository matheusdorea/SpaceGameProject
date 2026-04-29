import pygame
from pygame.locals import *
from sys import exit
from config import ALTURA, LARGURA
from coresEnum import Cores
from estadosEnum import Estados
from nave import Nave

# ============================================================
# CONFIGURAÇÕES GLOBAIS
# ============================================================
pygame.init()

# Definindo tamanho da tela
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Defender")

clock = pygame.time.Clock()
FPS = 60

#Criação de objetos
def criar_jogo():
    nave = Nave(LARGURA // 2, ALTURA // 2)

    return nave

# GameLoop
def main():
    # Definindo Objetos
    nave = criar_jogo()

    # Definindo estado inicial do jogo
    estado = Estados.ESTADO_JOGANDO

    while True:
        clock.tick(FPS)

        # ---------- EVENTOS ----------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                #retirar
                if event.key == K_r and Estados.ESTADO_JOGANDO:
                    nave.refletida= not nave.refletida

        # ---------- INPUT CONTÍNUO ----------
        if estado == Estados.ESTADO_JOGANDO:
            teclas = pygame.key.get_pressed()
            if teclas[K_w] or teclas[K_UP]:
                nave.mover_frente()
            if teclas[K_s] or teclas[K_DOWN]:
                nave.mover_tras()
            if teclas[K_a] or teclas[K_LEFT]:
                nave.girar(-1)
            if teclas[K_d] or teclas[K_RIGHT]:
                nave.girar(+1)

        # --------- DESENHANDO NA TELA ----------
        if estado == Estados.ESTADO_JOGANDO:
            TELA.fill(Cores.PRETO)

            nave.desenhar(TELA)

            pygame.display.flip()

if __name__ == "__main__":
    main()