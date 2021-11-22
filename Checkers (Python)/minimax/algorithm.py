'''This is where the AI algorithm'''

from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)


# minimax algorithm
def minimax(board, depth, max_player, game):
    if depth <= 0 or board.winner() is not None:
        return board.evaluate(), board

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(board, WHITE, game):
            evaluation, _ = minimax(move, depth - 1, False, game)
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

        return max_eval, best_move

    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(board, RED, game):
            evaluation, _ = minimax(move, depth - 1, True, game)

            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move

        return min_eval, best_move

# simulating the move for AI to get future data


def simulate_move(piece, move, board, game, skip):
    board.move_piece(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

# getting all the moves in board so AI can get the best decision


def get_all_moves(board, colour, game):
    moves = []

    for piece in board.get_all_pieces(colour):
        valid_move = board.get_valid_moves(piece)
        for move, skip in valid_move.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

# drawing what AI do


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw_board(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(1)
