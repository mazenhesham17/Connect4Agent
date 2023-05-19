from constants import ROW , COLUMN
from helper import valid
def estimate(cnt_ai, cnt_com, cnt_empty):
    if cnt_ai==4:
       return 100
    elif cnt_ai==2 and cnt_empty==2:
        return 2
    elif cnt_ai==3 and cnt_empty==1:
        return 5
    elif cnt_com==3 and cnt_empty==1:
        return -4
    return 0



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
    center = []
    mid=COLUMN // 2
    for i in range(ROW):
       center.append(board[i][mid])
    cnt = center.count(1)*3
    score += cnt
    return score

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