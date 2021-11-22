'''This where the main game progarmming'''

import pygame
from checkers_sub.constant import HEIGHT, WIDTH, SQUARE_SIZE, RED, WHITE
from checkers_sub.game import Game
from minimax.algorithm import minimax

# Frame per second
FPS = 60

# setting a display for game
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# setting a game caption
pygame.display.set_caption("CHECKERS")

# getting the row and coloumn after a mouse button down


def get_mouse_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# main funtion


def main():

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            _, new_board = minimax(game.get_board(), 3, 1, game)
            game.ai_move(new_board)

        # to be able to play with AI
        '''
        elif game.turn == RED :
            _, new_board = minimax(game.get_board(), 3, 0, game)
            game.ai_move(new_board)
        '''

        if game.winner() is not None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos)
                game.select(row, col)

        game.update()
        # pygame.time.delay(1000)

    pygame.quit()


main()
