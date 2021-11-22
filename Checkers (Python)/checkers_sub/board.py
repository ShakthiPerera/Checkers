'''This class is reprsenting the checkers board'''

import pygame
from .constant import BLACK, RED, SQUARE_SIZE, ROW, COL, WHITE
from .piece import Piece


class Board:
    # initializing
    def __init__(self):
        self.board = []
        self.red_pieces = self.white_pieces = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    # drawing the square items in the board
    def draw_square(self, win):
        win.fill(BLACK)
        for row in range(ROW):
            for col in range(row % 2, COL, 2):
                pygame.draw.rect(
                    win,
                    RED,
                    (row * SQUARE_SIZE,
                     col * SQUARE_SIZE,
                     SQUARE_SIZE,
                     SQUARE_SIZE))

    # creating the board in data types
    def create_board(self):
        for row in range(ROW):
            self.board.append([])
            for col in range(COL):
                if col % 2 == (row + 1) % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    # removing a piece from data type
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.colour == RED:
                    self.red_pieces -= 1
                else:
                    self.white_pieces -= 1

    # Finding the winner
    def winner(self):
        if self.red_pieces == 0:
            return WHITE
        elif self.white_pieces == 0:
            return RED

        return None

    # drawing the board with pieces
    def draw_board(self, win):
        self.draw_square(win)
        for row in range(ROW):
            for col in range(COL):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_pieces(win)

    # AI function for evaluating
    def evaluate(self):
        return self.white_pieces - self.red_pieces + \
            self.white_kings * 2 - self.red_kings * 2

    # getting the all pieces in the board
    def get_all_pieces(self, colour):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.colour == colour:
                    pieces.append(piece)

        return pieces

    # moving the pieces and making them kings
    def move_piece(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == ROW - 1 or row == 0:
            piece.make_king()
            if piece.colour == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    # getting the piece
    def get_piece(self, row, col):
        return self.board[row][col]

    # getting the valid move a piece can get
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.colour == RED or piece.king:
            moves.update(self.traverse_left(
                row - 1, max(row - 3, -1), -1, piece.colour, left))
            moves.update(self.traverse_right(
                row - 1, max(row - 3, -1), -1, piece.colour, right))
        if piece.colour == WHITE or piece.king:
            moves.update(self.traverse_left(
                row + 1, min(row + 3, ROW), 1, piece.colour, left))
            moves.update(self.traverse_right(
                row + 1, min(row + 3, ROW), 1, piece.colour, right))

        return moves

    # getiing the valid moves in left side of the piece
    def traverse_left(self, start, stop, step, colour, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROW)
                    moves.update(
                        self.traverse_left(
                            r + step,
                            row,
                            step,
                            colour,
                            left - 1,
                            skipped=last))
                    moves.update(
                        self.traverse_right(
                            r + step,
                            row,
                            step,
                            colour,
                            left + 1,
                            skipped=last))
                break
            elif current.colour == colour:
                break
            else:
                last = [current]

            left -= 1

        return moves

    # getiing the valid moves in right side of the piece
    def traverse_right(self, start, stop, step, colour, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COL:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROW)
                    moves.update(
                        self.traverse_left(
                            r + step,
                            row,
                            step,
                            colour,
                            right - 1,
                            skipped=last))
                    moves.update(
                        self.traverse_right(
                            r + step,
                            row,
                            step,
                            colour,
                            right + 1,
                            skipped=last))
                break
            elif current.colour == colour:
                break
            else:
                last = [current]

            right += 1

        return moves
