from goal import is_goal
from heuristic import *


def minimax(playground, player, depth):
    if is_goal(playground):
        winner = is_goal(playground)
        # if the state is goal then the opposite player of the current player is winner
        if winner == 1:
            return None, 4000
        else:
            return None, -4000
    if len(move(playground)) == 0:
        return None, 0
    if depth == 0:
        return None, h(playground)
    if player == 1:
        cols = move(playground)
        # dummy values
        col = cols[0]
        val = -100000000000000
        for c in cols:
            r = get_row(playground, c)
            playground[r][c] = 1
            res = minimax(playground, 2, depth - 1)[1]
            playground[r][c] = 0
            if res > val:
                val = res
                col = c
        return col, val

    else:
        cols = move(playground)
        # dummy values
        col = cols[0]
        val = 100000000000000
        for c in cols:
            r = get_row(playground, c)
            playground[r][c] = 2
            res = minimax(playground, 1, depth - 1)[1]
            playground[r][c] = 0
            if res < val:
                val = res
                col = c
        return col, val


def minimax_alphabeta(playground, player, alpha, beta, depth):
    if is_goal(playground):
        # if the state is goal then the opposite player of the current player is winner
        if is_goal(playground) == 1:
            return None, 4000
        else:
            return None, -4000
    if len(move(playground)) == 0:
        return None, 0
    if depth == 0:
        return None, h(playground)
    if player == 1:
        cols = move(playground)
        # dummy values
        col = cols[0]
        val = -100000000000000
        for c in cols:
            r = get_row(playground, c)
            playground[r][c] = 1
            res = minimax(playground, 2, depth - 1)[1]
            playground[r][c] = 0
            if res > val:
                val = res
                col = c
            if alpha < val:
                alpha = val
            if alpha >= beta:
                break
        return col, val

    else:
        cols = move(playground)
        # dummy values
        col = cols[0]
        val = 100000000000000
        for c in cols:
            r = get_row(playground, c)
            playground[r][c] = 2
            res = minimax(playground, 1, depth - 1)[1]
            playground[r][c] = 0
            if res < val:
                val = res
                col = c
            if beta > val:
                beta = val
            if alpha >= beta:
                break
        return col, val
