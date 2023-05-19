from constants import ROW, COLUMN
def put(board, col, player):
    for i in range(ROW)[::-1]:
        if board[i][col] == 0:
            board[i][col] = player
            return i
    return -1