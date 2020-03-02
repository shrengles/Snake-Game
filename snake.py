import pygame as pyg
from food import Food



class Snake:

    def __init__(self, x, y, display, colour=(0, 255, 0), facing='right'):
        self.x = x
        self.y = y
        self.display = display
        self.location = (self.x, self.y)
        self.eaten = 0
        self.length = []
        self.colour = colour
        self.facing = facing
        self.colour_border = (0, 0, 0)
        self.velocity = 5
        if self.colour == (0, 0, 0):
            self.colour_border = (255, 255, 255)

    def draw(self):

        if len(self.length) > 3 + self.eaten:
            del self.length[0]

        self.location = (self.x, self.y)

        for x, y in self.length:
            pyg.draw.rect(self.display, self.colour_border, (x,  y, 20, 20), 2)
            pyg.draw.rect(self.display, self.colour, (x+2, y+2, 18, 18))

        self.length.append(self.location)

    def move(self, direction):
        if direction == 'up':
            self.y -= 20
            self.facing = 'up'
        elif direction == 'down':
            self.y += 20
            self.facing = 'down'
        elif direction == 'left':
            self.x -= 20
            self.facing = 'left'
        elif direction == 'right':
            self.x += 20
            self.facing = 'right'

    def respawn(self, x, y):
        self.x, self.y = x, y
        self.length = []
        self.eaten = 0
