'''This class is representing a piece in tha checkers board'''

import pygame
from .constant import CROWN, RED, GREY, WHITE, SQUARE_SIZE, CROWN


class Piece:

    # constants for piece
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False

        if self.colour == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos(row, col)

    # calculating the position of pieces
    def calc_pos(self, row, col):
        self.x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = row * SQUARE_SIZE + SQUARE_SIZE // 2

    # making a piece king
    def make_king(self):
        self.king = True

    # drawing a piece
    def draw_pieces(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius)
        if self.king:
            pygame.Surface.blit(
                win,
                CROWN,
                (self.x -
                 CROWN.get_width() //
                 2,
                 self.y -
                 CROWN.get_height() //
                 2))

    # moving a piece
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos(row, col)
