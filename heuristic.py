from constants import ROW , COLUMN
from helper import valid

def estimate(cnt_ai, cnt_com, cnt_empty):
    if cnt_ai==4:
       return 9999999
    elif cnt_ai==2 and cnt_empty==2:
        return 999
    elif cnt_ai==3 and cnt_empty==1:
        return 9999
    elif cnt_com == 4:
        return -999999
    elif cnt_com==3 and cnt_empty==1:
        return -8888
    elif cnt_com == 2 and cnt_empty == 2:
        return -888
    return 0

def get_score_row(board, row, col):
    cnt_ai=(board[row][col]==1)+(board[row+1][col]==1)+(board[row+2][col]==1)+(board[row+3][col]==1)
    cnt_com=(board[row][col]==2)+(board[row+1][col]==2)+(board[row+2][col]==2)+(board[row+3][col]==2)
    cnt_empty=(board[row][col]==0)+(board[row+1][col]==0)+(board[row+2][col]==0)+(board[row+3][col]==0)
    return estimate(cnt_ai, cnt_com, cnt_empty)

def get_score_col(board, row, col):
    cnt_ai=(board[row][col]==1)+(board[row][col+1]==1)+(board[row][col+2]==1)+(board[row][col+3]==1)
    cnt_com=(board[row][col]==2)+(board[row][col+1]==2)+(board[row][col+2]==2)+(board[row][col+3]==2)
    cnt_empty=(board[row][col]==0)+(board[row][col+1]==0)+(board[row][col+2]==0)+(board[row][col+3]==0)
    return estimate(cnt_ai, cnt_com, cnt_empty)

def get_score_main_diagonal(board, row, col):
    cnt_ai=(board[row][col]==1)+(board[row+1][col-1]==1)+(board[row+2][col-2]==1)+(board[row+3][col-3]==1)
    cnt_com=(board[row][col]==2)+(board[row+1][col-1]==2)+(board[row+2][col-2]==2)+(board[row+3][col-3]==2)
    cnt_empty=(board[row][col]==0)+(board[row+1][col-1]==0)+(board[row+2][col-2]==0)+(board[row+3][col-3]==0)
    return estimate(cnt_ai, cnt_com, cnt_empty)

def get_score_secondary_diagonal(board, row, col):
    cnt_ai=(board[row][col]==1)+(board[row+1][col+1]==1)+(board[row+2][col+2]==1)+(board[row+3][col+3]==1)
    cnt_com=(board[row][col]==2)+(board[row+1][col+1]==2)+(board[row+2][col+2]==2)+(board[row+3][col+3]==2)
    cnt_empty=(board[row][col]==0)+(board[row+1][col+1]==0)+(board[row+2][col+2]==0)+(board[row+3][col+3]==0)
    return estimate(cnt_ai ,cnt_com,cnt_empty)


def hfun(board):
    score = 0
    for row in range (ROW):
        for col in range(COLUMN):
            if valid(row + 3, col):
                score +=  get_score_row(board, row, col)
            if valid(row, col + 3):
                score +=  get_score_col(board, row, col)
            if valid(row + 3, col + 3):
                score +=  get_score_secondary_diagonal(board, row, col)
            if valid(row + 3, col - 3):
                score +=  get_score_main_diagonal(board, row, col)
    cnt = board.count(1) + board.count(2)
    for i in range(ROW):
        for j in range(COLUMN):
            if board[i][j] == 1:
                score += (  4 - abs( 3 - j )  )*1000
            else:
                score -= (4 - abs(3 - j))*1000
    return score

