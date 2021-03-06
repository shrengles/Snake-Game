import pygame as pygame
import random


class Food:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = (self.x, self.y)

    def draw(self, g):
        self.location = (self.x, self.y)
        pygame.draw.rect(g, (237, 108, 90), (self.x, self.y, 20, 20))

    def respawn(self, x=39, y=29):
        self.x, self.y = random.randint(1, x)*20, random.randint(1, y)*20
