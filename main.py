# sortingAlgorithm
# by @0N3IR0S
# 2020

import pygame
from random import randint

# initialize pyGame
pygame.init()

# create screen
game_screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("sortingAlgorithm by @0N3IR0S")

# FPS limitation
clock = pygame.time.Clock()

# main loop
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        # Quit Program
        if event.type == pygame.QUIT:
            game_exit = True

    # game screen
    game_screen.fill((0, 0, 0))

    # create random array
    

    # update display
    pygame.display.update()
    clock.tick(30)

# quit
pygame.quit()
