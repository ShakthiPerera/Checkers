'''This is the file where all the constants are'''

import pygame

HEIGHT, WIDTH = 800, 800

ROW, COL = 8, 8

SQUARE_SIZE = HEIGHT // ROW

# rgb

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)


CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (45, 22))
