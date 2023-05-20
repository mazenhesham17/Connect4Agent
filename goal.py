from constants import ROW, COLUMN, dx, dy
from helper import check_4


def is_goal(board):
    for i in range(ROW)[::-1]:
        for j in range(COLUMN):
            if board[i][j]:
                for k in range(4):
                    if check_4(board, i, j, dx[k], dy[k]):
                        return board[i][j]
    return 0


def is_full(board):
    cnt = 0
    for i in range(ROW)[::-1]:
        for j in range(COLUMN):
            cnt += board[i][j] == 0
    return cnt == 0
