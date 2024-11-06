import pygame
import random

# Definimos los colores
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

class Rectangulo:
    def __init__(self, window):
        self.window = window
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)
        self.color = random.choice((ROJO, VERDE, AZUL))
        self.x = random.randrange(0, window.get_width() - self.width)
        self.y = random.randrange(0, window.get_height() - self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clickedInside(self, mousePoint):
        return self.rect.collidepoint(mousePoint)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    def area(self):
        return self.width * self.height

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()
