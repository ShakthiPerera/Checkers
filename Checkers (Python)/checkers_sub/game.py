'''This is where the game mechanics'''

from .board import Board
from .constant import RED, BLUE, WHITE, ROW, COL, SQUARE_SIZE
import pygame


class Game:

    def __init__(self, win):
        self._init()
        self.win = win

    # updating the board after a change in the board
    def update(self):
        self.board.draw_board(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # init method
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    # reset method
    def reset(self):
        self._init()

    # selecting a position
    def select(self, row, col):
        if self.selected:
            if not self._move(row, col):
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)

        if piece != 0 and piece.colour == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)

            return True

        return False

    # drawing the valid moves of a piece
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(
                self.win,
                BLUE,
                (col *
                 SQUARE_SIZE +
                 SQUARE_SIZE //
                 2,
                 row *
                 SQUARE_SIZE +
                 SQUARE_SIZE //
                 2),
                15)

    # moving mechanics
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move_piece(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    # finding the winner
    def winner(self):
        return self.board.winner()

    # changing the turn
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    # getting the board data type
    def get_board(self):
        return self.board

    # ai moving
    def ai_move(self, board):
        self.board = board
        self.change_turn()
