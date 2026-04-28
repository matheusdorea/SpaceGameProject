import pygame
from pygame.locals import *
from sys import exit
from config import ALTURA, LARGURA
from coresEnum import Cores
from estadosEnum import Estados
from hud import desenhar_hud
from nave import Nave
from naveInimiga import NaveInimiga
from projetil import Projetil

# ============================================================
# CONFIGURAÇÕES GLOBAIS
# ============================================================
pygame.init()

# Definindo tamanho da tela
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Defender")

#definindo fps
clock = pygame.time.Clock()
FPS = 60

#definindo fonte
fonte_hub = pygame.font.SysFont(None, 30)

#Criação de objetos
def criar_jogo():
    nave = Nave(LARGURA // 2, ALTURA // 2)
    inimigos = [
        NaveInimiga(100, 100)
    ]
    projeteis = []

    return nave, inimigos, projeteis

# GameLoop
def main():
    # Definindo Objetos
    nave, inimigos, projeteis = criar_jogo()

    # Definindo estado inicial do jogo
    estado = Estados.ESTADO_JOGANDO

    while True:
        clock.tick(FPS)

        # ---------- EVENTOS ----------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

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
            if teclas[K_SPACE]:
                tiro = nave.atirar()
                if tiro:
                    projeteis.append(tiro)

        # --------- ATUALIZANDO ----------------
        if estado == Estados.ESTADO_JOGANDO:
            nave.atualizar()

            for p in projeteis[:]:
                p.atualizar()
                if p.fora_da_tela():
                    projeteis.remove(p)
                    continue

                #colisão de projétil com inimigo
                for inimigo in inimigos[:]:
                    if inimigo.viva and inimigo.colidiu_com(p.x, p.y):
                        inimigos.remove(inimigo)
                        projeteis.remove(p)
                        break

            for inimigo in inimigos[:]:
                inimigo.atualizar(nave.x, nave.y)

                if inimigo.viva and nave.colidiu_com(inimigo.x, inimigo.y):
                    nave.vidas -= 1
                    inimigos.remove(inimigo)
                    break

        # --------- DESENHANDO NA TELA ----------
        if estado == Estados.ESTADO_JOGANDO:
            TELA.fill(Cores.PRETO)

            for p in projeteis:
                p.desenhar(TELA)
            for i in inimigos:
                i.desenhar(TELA)

            nave.desenhar(TELA)
                
            desenhar_hud(fonte_hub, TELA, nave)
            pygame.display.flip()

if __name__ == "__main__":
    main()