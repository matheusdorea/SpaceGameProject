import pygame
from config import LARGURA, ALTURA
from coresEnum import Cores

def tela_fim(superficie, mensagem, cor):
    superficie.fill(Cores.PRETO)
    fonte_grande = pygame.font.SysFont(None, 80)
    txt = fonte_grande.render(mensagem, True, cor)
    r = txt.get_rect(center=(LARGURA//2, ALTURA//2))
    superficie.blit(txt, r)
    sub = pygame.font.SysFont(None, 36).render("Pressione R para reiniciar", True, Cores.BRANCO)
    superficie.blit(sub, sub.get_rect(center=(LARGURA//2, ALTURA//2 + 80)))
    pygame.display.flip()