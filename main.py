# sortingAlgorithm
# by @0N3IR0S
# 2020

import pygame
import random
import time

# initialize pyGame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("sortingAlgorithm by @0N3IR0S")

# FPS limitation
clock = pygame.time.Clock()

# main loop
game_exit = False
run_once = False
while not game_exit:
    for event in pygame.event.get():
        # Quit Program
        if event.type == pygame.QUIT:
            game_exit = True

    # run this code only once
    while not run_once:
        run_once = True

        # game screen
        screen.fill((0, 0, 0))

        # create random array
        random_list = [random.randrange(5, 400, 5) for i in range(86)]

        # sort this shit
        for i in random_list:
            k = 85
            for j in range(0, k):
                if random_list[j + 1] > random_list[j]:
                    random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
                k -= 1

                screen.fill((0, 0, 0))

                xx = 0
                for l in range(99, 701, 7):
                    pygame.draw.rect(screen, (255, 255, 255), [(800 - l), 500, 5, (random_list[xx] * -1)])
                    xx += 1
            pygame.display.update()

    # update display
    pygame.display.update()
    clock.tick(30)

# quit
pygame.quit()
