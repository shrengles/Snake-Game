import sys
import random
import pygame as pyg
from pygame.locals import *
from snake import *
from food import Food

pyg.init()
PL2 = False
HEIGHT, WIDTH = 800, 600
FPS = 15
FPSCLOCK = pyg.time.Clock()
screen = pyg.display.set_mode((HEIGHT, WIDTH))
canvas = pyg.Surface((WIDTH, HEIGHT))

pyg.display.set_caption('Snake Game by shrengers')

active_snakes = []

player1 = Snake(HEIGHT/2, WIDTH/2, screen, colour=(255, 255, 255))
active_snakes.append(player1)
food = Food(random.randint(1, 39)*20, random.randint(1, 29)*20, screen)

if PL2:
    player2 = Snake(HEIGHT/2, WIDTH - 40, screen,
                    colour=(0, 0, 0), facing='left')
    active_snakes.append(player2)

while True:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_LEFT and player1.facing != 'right' and player1.facing != 'left':
                player1.facing = 'left'
            elif event.key == pyg.K_RIGHT and player1.facing != 'left' and player1.facing != 'right':
                player1.facing = 'right'
            elif event.key == pyg.K_UP and player1.facing != 'down' and player1.facing != 'up':
                player1.facing = 'up'
            elif event.key == pyg.K_DOWN and player1.facing != 'up' and player1.facing != 'down':
                player1.facing = 'down'

            elif event.key == pyg.K_a and player2.facing != 'right' and player2.facing != 'left':
                player2.facing = 'left'
            elif event.key == pyg.K_d and player2.facing != 'left' and player2.facing != 'right':
                player2.facing = 'right'
            elif event.key == pyg.K_w and player2.facing != 'down' and player2.facing != 'up':
                player2.facing = 'up'
            elif event.key == pyg.K_s and player2.facing != 'up' and player2.facing != 'down':
                player2.facing = 'down'

            elif event.key == pyg.K_p:
                print(player1.length)
                print([i.length for i in active_snakes])
            elif event.key == pyg.K_f:
                food.respawn()
            elif event.key == pyg.K_r:
                player1.respawn()

    for player in active_snakes:

        if player.location == food.location:
            player.eaten += 1
            food.respawn()

        elif any(player.location in i.length for i in active_snakes if i != player) or player.location in player.length[:-1]:
            player.respawn(random.randint(10, 20)*20, random.randint(10, 20)*20)
            player.facing = 'right'

        if 0 <= player.x < HEIGHT and 0 <= player.y < WIDTH:
            pass
        else:
            player.respawn(random.randint(10, 20)*20, random.randint(10, 20)*20)
            player.facing = 'right'

        screen.fill((80, 80, 80))
        # if player.x % 20 == 0 and player.y % 20 == 0:
        player.move(player.facing)

        player.draw()
        food.draw()

        pyg.display.flip()
        FPSCLOCK.tick(FPS)
