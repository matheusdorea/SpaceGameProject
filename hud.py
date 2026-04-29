import pygame

from config import ALTURA
from coresEnum import Cores
from nave import Nave

def desenhar_hud(fonte_hub, superficie, nave: Nave):
    txt = fonte_hub.render(f"Vidas: {nave.vidas}", True, Cores.BRANCO)
    superficie.blit(txt, (10, 10))
    controles = "W=frente  S=trás  A/D=girar  SPACE=atirar  R=reflexão"
    txt3 = pygame.font.SysFont(None, 22).render(controles, True, (180,180,180))
    superficie.blit(txt3, (10, ALTURA - 25))