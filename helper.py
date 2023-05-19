from constants import ROW, COLUMN, dx, dy


def make_2d(n, m):
    temp = [[0 for _ in range(m)] for _ in range(n)]
    return temp

def valid(r,c):
    if 0 <= r < ROW and 0 <= c < COLUMN:
        return True
    else:
        return False

def valid_cols(boards):
    lst = []
    for i in range(COLUMN):
        if boards[0][i] == 0:
            lst.append(i)
    return lst

def check_4(board, i, j, di, dj):
    if not valid( i + 3*di , j + 3*dj ):
        return False
    flag = True
    for k in range(4):
        flag &= board[i][j] == board[i + k*di][j + k*dj]
    return flag

