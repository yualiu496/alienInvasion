import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((1200, 800))
screen.fill((230,100,100))
pygame.display.set_caption("Alien Invasion")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Game Over")
            sys.exit()

    pygame.display.flip()