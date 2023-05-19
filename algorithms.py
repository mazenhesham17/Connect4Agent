from goal import is_goal
from heuristic import *
from helper import valid_cols
from move import put


import math
import random

def minimax(playground,player,depth):
    if is_goal(playground):
        #if the state is goal then the opposite player of the current player is winner
        if player == 1:
            return None, -math.inf
        else:
            return None, math.inf
    if len(valid_cols(playground))==0:
        return None,0
    if depth==0:
        return None,hfun(playground)
    if player==1:
        cols=valid_cols(playground)
        #dummy values
        col=cols[0]
        val = -100000000000000
        for c in cols:
            idx = put(playground,c,player)
            if idx != -1:
                res=minimax(playground,2,depth-1)[1]
                playground[idx][c] = 0
                if res >= val:
                    val=res
                    col=c
        return col,val

    else:
        cols = valid_cols(playground)
        # dummy values
        col = cols[0]
        val = 100000000000000
        for c in cols:
            idx = put(playground,c,player)
            if idx != -1:
                res = minimax(playground, 1,depth-1)[1]
                playground[idx][c]=0
                if res <= val:
                    val = res
                    col = c
        return col, val


def minimax_alphabeta(playground,player,alpha,beta,depth):
    if is_goal(playground):
        #if the state is goal then the opposite player of the current player is winner
        if player == 1:
            return None, -math.inf
        else:
            return None, math.inf
    if len(valid_cols(playground))==0:
        return None,0
    if depth==0:
        return None,hfun(playground)
    if player==1:
        cols=valid_cols(playground)
        #dummy values
        col=cols[0]
        val = -100000000000000
        for c in cols:
            idx = put(playground,c,player)
            if idx != -1:
                res=minimax_alphabeta(playground,2,alpha,beta,depth-1)[1]
                playground[idx][c] = 0
                if res > val:
                    val=res
                    col=c
                if alpha < val:
                    alpha = val
                if alpha >= beta:
                    break
        return col,val

    else:
        cols = valid_cols(playground)
        # dummy values
        col = cols[0]
        val = 100000000000000
        for c in cols:
            idx = put(playground,c,player)
            if idx != -1:
                res = minimax_alphabeta(playground, 1,alpha,beta,depth-1)[1]
                playground[idx][c]=0
                if res < val:
                    val = res
                    col = c
                if beta > val:
                    beta = val
                if alpha >= beta:
                    break
        return col, val


