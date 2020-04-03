import random, pygame, sys
from pygame.locals import *
from snake import *
from food import Food


class Game:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.food = Food(w/2, h/2)
        self.player = Snake(40, 40)
        self.player2 = Snake(100,100)
        self.canvas = Canvas(self.width, self.height, "Testing...")
        self.gridwh = 20
        self.mv = None

    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.K_ESCAPE:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                if self.player.facing != 1:
                    self.mv = 0

            if keys[pygame.K_LEFT]:
                if self.player.facing != 0:
                    self.mv = 1

            if keys[pygame.K_UP]:
                if self.player.facing != 3:
                    self.mv = 2

            if keys[pygame.K_DOWN]:
                if self.player.facing != 2:
                    self.mv = 3


            if self.player.location == self.food.location:
                self.player.eat()
                self.player.eaten += 1
                self.food.respawn()

            elif self.player.location in self.player.length[:-1] or self.player.location in self.player.set_pieces:
                self.player.respawn()

            if 0 <= self.player.x < self.width and 0 <= self.player.y < self.height:
                pass
            else:
                self.player.respawn()


            if self.player.x % 20 == 0 and self.player.y % 20 == 0:
                if self.mv == 0:
                    self.player.turn(0)
                elif self.mv == 1:
                    self.player.turn(1)
                elif self.mv == 2:
                    self.player.turn(2)
                elif self.mv == 3:
                    self.player.turn(3)
            
            self.player.move(self.player.facing)

            # Update Canvas
            self.canvas.draw_background()
            self.player.draw(self.canvas.get_canvas())
            ###
            self.player.draw_sets(self.canvas.get_canvas())
            ###
            # self.player2.draw(self.canvas.get_canvas())
            self.food.draw(self.canvas.get_canvas())
            self.canvas.update()

        pygame.quit()

class Canvas:

    def __init__(self, w, h, name="None"):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.flip()

    def draw_text(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", size)
        render = font.render(text, 1, (0,0,0))

        self.screen.draw(render, (x,y))

    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill((244,241,187))


