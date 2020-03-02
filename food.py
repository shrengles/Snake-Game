import pygame as pyg
import random


class Food:

    def __init__(self, x, y, display):
        self.x = x
        self.y = y
        self.display = display
        self.location = (self.x, self.y)

    def draw(self):
        self.location = (self.x, self.y)
        pyg.draw.rect(self.display, (255, 0, 0), (self.x+2, self.y+2, 18, 18))

    def respawn(self, x=39, y=29):
        self.x, self.y = random.randint(1, x)*20, random.randint(1, y)*20
