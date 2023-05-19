ROW = 6
COLUMN = 7


def move(arr):
    cols = []
    for c in range(COLUMN):
        if arr[0][c] == 0:
            cols.append(c)
    return cols


def get_row(arr, col):
    for row in range(ROW)[::-1]:
        if arr[row][col] == 0:
            return row


def check(r, c):
    if 0 <= r < ROW and 0 <= c < COLUMN:
        return True
    else:
        return False


def h(board):
    score = 0
    for row in range(ROW):
        for col in range(COLUMN):
            if check(row + 3, col):
                score = score + get_score_row(board, row, col)
            if check(row, col + 3):
                score = score + get_score_col(board, row, col)
            if check(row + 3, col - 3):
                score = score + get_score_secondary_diagonal(board, row, col)
            if check(row + 3, col + 3):
                score = score + get_score_main_diagonal(board, row, col)
    return score


def get_score_row(board, row, col):
    cnt_ai = (board[row][col] == 1) + (board[row + 1][col] == 1) + (board[row + 2][col] == 1) + (
            board[row + 3][col] == 1)
    cnt_com = (board[row][col] == 2) + (board[row + 1][col] == 2) + (board[row + 2][col] == 2) + (
            board[row + 3][col] == 2)
    cnt_empty = (board[row][col] == 0) + (board[row + 1][col] == 0) + (board[row + 2][col] == 0) + (
            board[row + 3][col] == 0)
    return estimate(cnt_ai, cnt_com, cnt_empty)


def get_score_col(board, row, col):
    cnt_ai = (board[row][col] == 1) + (board[row][col + 1] == 1) + (board[row][col + 2] == 1) + (
            board[row][col + 3] == 1)
    cnt_com = (board[row][col] == 2) + (board[row][col + 1] == 2) + (board[row][col + 2] == 2) + (
            board[row][col + 3] == 2)
    cnt_empty = (board[row][col] == 0) + (board[row][col + 1] == 0) + (board[row][col + 2] == 0) + (
            board[row][col + 3] == 0)
    return estimate(cnt_ai, cnt_com, cnt_empty)


def get_score_secondary_diagonal(board, row, col):
    cnt_ai = (board[row][col] == 1) + (board[row + 1][col - 1] == 1) + (board[row + 2][col - 2] == 1) + (
            board[row + 3][col - 3] == 1)
    cnt_com = (board[row][col] == 2) + (board[row + 1][col - 1] == 2) + (board[row + 2][col - 2] == 2) + (
            board[row + 3][col - 3] == 2)
    cnt_empty = (board[row][col] == 0) + (board[row + 1][col - 1] == 0) + (board[row + 2][col - 2] == 0) + (
            board[row + 3][col - 3] == 0)
    return estimate(cnt_ai, cnt_com, cnt_empty)


def get_score_main_diagonal(board, row, col):
    cnt_ai = (board[row][col] == 1) + (board[row + 1][col + 1] == 1) + (board[row + 2][col + 2] == 1) + (
            board[row + 3][col + 3] == 1)
    cnt_com = (board[row][col] == 2) + (board[row + 1][col + 1] == 2) + (board[row + 2][col + 2] == 2) + (
            board[row + 3][col + 3] == 2)
    cnt_empty = (board[row][col] == 0) + (board[row + 1][col + 1] == 0) + (board[row + 2][col + 2] == 0) + (
            board[row + 3][col + 3] == 0)
    return estimate(cnt_ai, cnt_com, cnt_empty)


def estimate(cnt_ai, cnt_com, cnt_empty):
    if cnt_ai == 4:
        return 1000
    elif cnt_ai == 2 and cnt_empty == 2:
        return 500
    elif cnt_ai == 3 and cnt_empty == 1:
        return 750
    elif cnt_com == 4:
        return -1000
    elif cnt_com == 2 and cnt_empty == 2:
        return -500
    elif cnt_com == 3 and cnt_empty == 1:
        return -750
    return 0
