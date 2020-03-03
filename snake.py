import pygame as pygame
from food import Food
import random



class Snake:

    w = h = 20

    def __init__(self, x, y, colour=(0, 255, 0), facing=0):
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        self.eaten = 0
        self.length = []
        self.colour = colour
        self.facing = facing
        self.colour_border = (0, 0, 0)
        self.velocity = 5
        if self.colour == (0, 0, 0):
            self.colour_border = (255, 255, 255)

    def draw(self, g):

        if len(self.length) > 3 + self.eaten:
            del self.length[0]

        self.location = (self.x, self.y)

        for x, y in self.length:
            pygame.draw.rect(g, self.colour, (x, y, 20, 20))

        self.length.append(self.location)

    def move(self, direction):
        if direction == 0:
            self.x += 5
            self.facing = 0
        elif direction == 1:
            self.x -= 5
            self.facing = 1
        elif direction == 2:
            self.y -= 5
            self.facing = 2
        elif direction == 3:
            self.y += 5
            self.facing = 3
        

    def respawn(self):
        self.x, self.y = random.randint(10, 20)*5, random.randint(10, 20)*5
        self.length = []
        self.eaten = 0
        self.facing = 0
