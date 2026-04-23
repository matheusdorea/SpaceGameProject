import pygame


LARGURA, ALTURA = 900, 700

# Desenhar Polígono
def desenhar_poligono(superficie, cor, pontos, largura=2):
    """Desenha polígono a partir de lista de pontos (float)."""
    pts_int = [(int(x), int(y)) for (x, y) in pontos]
    pygame.draw.polygon(superficie, cor, pts_int, largura)