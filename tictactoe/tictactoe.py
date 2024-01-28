"""
Tic Tac Toe Player
"""

import math
import copy

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    else:
        X_count = 0
        O_count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    X_count += 1
                if board[i][j] == O:
                    O_count += 1
        if X_count > O_count:
            return O
        else:
            return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    row = action[0]
    column = action[1]
    if new_board[row][column] != EMPTY:
        raise IndexError
    new_board[row][column] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        t = 0
        for j in range(2):
            if board[i][j] == board[i][j+1]:
                t += 1
            else:
                break
        if t == 2:
            return board[i][j]
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    return None

        



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not winner(board):
        return False
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False 
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    utility_number_1 = 1
    utility_number_minus1 = -1
    utility_number_0 = 0
    if winner(board) == X:
        return utility_number_1
    elif winner(board) == 0:
        return utility_number_minus1
    else:
        return utility_number_0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player = player(board)
    if current_player == 0:
        value, move = Min_Value(board)
    else:
        value, move = Max_Value(board)
    return move

    
def Max_Value(board):
    v = float('-inf')
    move = None
    for action in actions(board):
        aux, act = Min_Value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move
    return v, move

def Min_Value(board):
    v = float('inf')
    move = None
    for action in actions(board):
        aux, act = Max_Value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == -1:
                return v, move
    return v, move
                
