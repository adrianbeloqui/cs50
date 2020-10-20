"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def _count_player_moves(board, player):
    moves = 0
    def add_moves(num):
        nonlocal moves
        moves += num
    [add_moves(row.count(player)) for row in board]
    return moves

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = _count_player_moves(board, X)
    o = _count_player_moves(board, O)
    if x == o or o > x:
        return X
    if x > o:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    states = set()
    width = len(board)
    for i in range(width):
        for j in range(width):
            if board[i][j] is EMPTY:
                states.add((i, j))
    return states

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    i, j = action
    if new_board[i][j] is not EMPTY:
        raise Exception('Illegal movement')
    else:
        new_board[i][j] = player(new_board)
    return new_board

def _row_winner(row):
    for p in (X, O):
        moves = [j == p for j in row]
        if all(moves):
            return p
    return None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal winner
    for row in board:
        winner_player = _row_winner(row)
        if winner_player:
            return winner_player

    # Column winner
    for i in range(len(board[0])):
        col = [board[j][i] for j in range(len(board))]
        winner_player = _row_winner(col)
        if winner_player:
            return winner_player

    diagonals = [[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]
    for i in range(len(board)):
        diagonals[0][i] = board[i][i]
        diagonals[1][i] = board[i][(i * -1) - 1]

    for diag in diagonals:
        winner_player = _row_winner(diag)
        if winner_player:
            return winner_player

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        for row in board:
            if not all(row):
                return False
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    p = winner(board)
    if not p:
        return 0
    if p is X:
        return 1
    return -1

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) is X:
            _, action = max_val(board, -math.inf, math.inf)
            return action
        else:
            _, action = min_val(board, -math.inf, math.inf)
            return action

def max_val(board, alpha, beta):
    if terminal(board):
        return utility(board), None
 
    v = -math.inf
    bestAction = None
    for action in actions(board):
        value, _ = min_val(result(board, action), alpha, beta)
        if value > v:
            bestAction = deepcopy(action)
            v = value
            alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v, bestAction

def min_val(board, alpha, beta):
    if terminal(board):
        return utility(board), None

    v = math.inf
    bestAction = None
    for action in actions(board):
        value, _ = max_val(result(board, action), alpha, beta)
        if value < v:
            bestAction = deepcopy(action)
            v = value
            beta = min(beta, v)
        if beta <= alpha:
            break
    return v, bestAction
