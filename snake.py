import pygame as pygame
from food import Food
import random



class Snake:

    w = h = 20

    def __init__(self, x, y, colour=(155, 193, 188), facing=0):
        self.set_pieces = []
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

        if len(self.length) > 3 * 4 + self.eaten * 4:
            del self.length[0]

        self.location = (self.x, self.y)

        for x, y in self.length:
            pygame.draw.rect(g, self.colour, (x, y, 20, 20))

        self.length.append(self.location)

    def set(self):
        for i in range(len(self.length[2::])):
            self.set_pieces.append(self.length[i])

    def draw_sets(self, g):
        for x, y in self.set_pieces:
            pygame.draw.rect(g, (128, 128, 128), (x, y, 20, 20))
            
        
    def move(self, direction):
        if direction == 0:
            self.x += 5
        elif direction == 1:
            self.x -= 5
        elif direction == 2:
            self.y -= 5
        elif direction == 3:
            self.y += 5

    def turn(self, direction):
        if direction == 0:
            self.facing = 0
        elif direction == 1:
            self.facing = 1
        elif direction == 2:
            self.facing = 2
        elif direction == 3:
            self.facing = 3

    @staticmethod
    def random_colour():
        levels = range(32,224,32)
        return tuple(random.choice(levels) for _ in range(3))

    def eat(self):
        self.set()
        self.colour = self.random_colour()
        
    def respawn(self):
        self.x, self.y = random.randint(10, 20)*20, random.randint(10, 20)*20
        self.set_pieces = []
        self.length = []
        self.eaten = 0
        self.facing = 0
