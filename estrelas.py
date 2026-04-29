import numpy as np
from math import cos, sin
import pygame
import random

class SistemaDEstrelas:
    NUM_ESTRELAS = 150
    ESCALA = 300  # distância "focal" das estrelas

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        self.estrelas = self._gerar_estrelas()

    def _gerar_estrelas(self):
        """Gera pontos aleatórios numa esfera de raio ~1."""
        estrelas = []
        for _ in range(self.NUM_ESTRELAS):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            z = random.uniform(-1, 1)
            tamanho = random.randint(1, 3)
            brilho = random.randint(150, 255)
            estrelas.append({
                "ponto": [[x], [y], [z]],
                "tamanho": tamanho,
                "brilho": brilho
            })
        return estrelas

    def _multiply_matrix(self, a, b):
        return (np.array(a) @ np.array(b)).tolist()

    def atualizar(self):
        self.angle_x += 0.002
        self.angle_y += 0.003
        self.angle_z += 0.001

    def desenhar(self, superficie):
        rotation_x = [
            [1, 0, 0],
            [0, cos(self.angle_x), -sin(self.angle_x)],
            [0, sin(self.angle_x),  cos(self.angle_x)]
        ]
        rotation_y = [
            [cos(self.angle_y), 0, sin(self.angle_y)],
            [0, 1, 0],
            [-sin(self.angle_y), 0, cos(self.angle_y)]
        ]
        rotation_z = [
            [cos(self.angle_z), -sin(self.angle_z), 0],
            [sin(self.angle_z),  cos(self.angle_z), 0],
            [0, 0, 1]
        ]
        projection_matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]

        for estrela in self.estrelas:
            p = estrela["ponto"]

            rx = self._multiply_matrix(rotation_x, p)
            ry = self._multiply_matrix(rotation_y, rx)
            rz = self._multiply_matrix(rotation_z, ry)

            p2d = self._multiply_matrix(projection_matrix, rz)

            x = (p2d[0][0] * self.ESCALA) + self.largura / 2
            y = (p2d[1][0] * self.ESCALA) + self.altura / 2

            b = estrela["brilho"]
            cor = (b, b, b)
            pygame.draw.circle(superficie, cor, (int(x), int(y)), estrela["tamanho"])