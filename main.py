import math
import random

ROW = 6
COLUMN = 7


def move(arr):
    cols = []
    for c in range(COLUMN):
        if arr[ROW - 1][c] == 0:
            cols.append(c)
    return cols


def getrow(arr, col):
    for row in range(ROW):
        if arr[row][col] == 0:
            return row


def check(r, c):
    if 0 <= r < ROW and 0 <= c < COLUMN:
        return True
    else:
        return False


def hfun(board):
    score = 0
    for row in range(ROW):
        for col in range(COLUMN):
            if check(row + 3, col):
                score = score + getscore_row(board, row, col)
            if check(row, col + 3):
                score = score + getscore_col(board, row, col)
            if check(row + 3, col + 3):
                score = score + getscore_secondary_diagonal(board, row, col)
            if check(row + 3, col - 3):
                score = score + getscore_main_diagonal(board, row, col)
    return score


def getscore_row(board, row, col):
    cntai = (board[row][col] == 1) + (board[row + 1][col] == 1) + (board[row + 2][col] == 1) + (
                board[row + 3][col] == 1)
    cntcom = (board[row][col] == 2) + (board[row + 1][col] == 2) + (board[row + 2][col] == 2) + (
                board[row + 3][col] == 2)
    cntempty = (board[row][col] == 0) + (board[row + 1][col] == 0) + (board[row + 2][col] == 0) + (
                board[row + 3][col] == 0)
    return estimate(cntai, cntcom, cntempty)


def getscore_col(board, row, col):
    cntai = (board[row][col] == 1) + (board[row][col + 1] == 1) + (board[row][col + 2] == 1) + (
                board[row][col + 3] == 1)
    cntcom = (board[row][col] == 2) + (board[row][col + 1] == 2) + (board[row][col + 2] == 2) + (
                board[row][col + 3] == 2)
    cntempty = (board[row][col] == 0) + (board[row][col + 1] == 0) + (board[row][col + 2] == 0) + (
                board[row][col + 3] == 0)
    return estimate(cntai, cntcom, cntempty)


def getscore_main_diagonal(board, row, col):
    cntai = (board[row][col] == 1) + (board[row + 1][col - 1] == 1) + (board[row + 2][col - 2] == 1) + (
                board[row + 3][col - 3] == 1)
    cntcom = (board[row][col] == 2) + (board[row + 1][col - 1] == 2) + (board[row + 2][col - 2] == 2) + (
                board[row + 3][col - 3] == 2)
    cntempty = (board[row][col] == 0) + (board[row + 1][col - 1] == 0) + (board[row + 2][col - 2] == 0) + (
                board[row + 3][col - 3] == 0)
    return estimate(cntai, cntcom, cntempty)


def getscore_secondary_diagonal(board, row, col):
    cntai = (board[row][col] == 1) + (board[row + 1][col + 1] == 1) + (board[row + 2][col + 2] == 1) + (
                board[row + 3][col + 3] == 1)
    cntcom = (board[row][col] == 2) + (board[row + 1][col + 1] == 2) + (board[row + 2][col + 2] == 2) + (
                board[row + 3][col + 3] == 2)
    cntempty = (board[row][col] == 0) + (board[row + 1][col + 1] == 0) + (board[row + 2][col + 2] == 0) + (
                board[row + 3][col + 3] == 0)
    return estimate(cntai, cntcom, cntempty)


def estimate(cntai, cntcom, cntempty):
    if cntai == 4:
        return 1000
    elif cntai == 2 and cntempty == 2:
        return 500
    elif cntai == 3 and cntempty == 1:
        return 750
    elif cntcom == 4:
        return -1000
    elif cntcom == 2 and cntempty == 2:
        return -500
    elif cntcom == 3 and cntempty == 1:
        return -750
    return 0
