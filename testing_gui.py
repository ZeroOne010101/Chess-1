import pygame
import os

pygame.init()
image_directory = os.path.join(os.getcwd(), 'Pieces')

screen = pygame.display.mode_ok([100, 100], flags = 0, depth = 0)
image = pygame.image.load(r'black_b.png').convert_alpha()

while True:
    try:
        screen.blit(image, [0, 0])
    except pygame.error:
        print('Some bs happened')
    pygame.display.flip()
