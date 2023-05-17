ROW = 6
COLUMN = 7


def make_2d(n, m):
    temp = [[0 for _ in range(m)] for _ in range(n)]
    return temp


# return the winner or 0
def check_vertical(board):
    for i in range(COLUMN):
        cnt, last = 0, 0
        for j in range(ROW):
            if board[j][i] == last:
                cnt += 1
            else:
                cnt, last = 1, board[j][i]
            if cnt == 4 and board[j][i]:
                return board[j][i]
    return 0


# return the winner or 0
def check_horizontal(board):
    for i in range(ROW):
        cnt, last = 0, 0
        for j in range(COLUMN):
            if board[i][j] == last:
                cnt += 1
            else:
                cnt, last = 1, board[i][j]
            if cnt == 4 and board[i][j]:
                return board[i][j]
    return 0


# return if this (i , j) win
def check_diagonal(board, i, j):
    temp_i, temp_j = i, j
    # check the main diagonal
    cnt, last = 0, 0
    while i >= 0 and j < COLUMN:
        if board[i][j] == last:
            cnt += 1
        else:
            cnt, last = 1, board[i][j]
        if cnt == 4 and board[i][j]:
            return True
        i -= 1
        j += 1
    i, j, cnt, last = temp_i, temp_j, 0, 0
    # check the secondary diagonal
    while i >= 0 and j >= 0:
        if board[i][j] == last:
            cnt += 1
        else:
            cnt, last = 1, board[i][j]
        if cnt == 4 and board[i][j]:
            return True
        i -= 1
        j -= 1
    return False


def is_goal(board):
    player = check_vertical(board)
    if player:
        return player
    player = check_horizontal(board)
    if player:
        return player
    for i in range(ROW)[::-1]:
        for j in range(COLUMN):
            player = check_diagonal(board, i, j)
            if player:
                return player
    return 0


if __name__ == '__main__':
    playground = make_2d(ROW, COLUMN)
    lst = [[1, 0, 1, 0, 0, 0, 1],
           [0, 1, 0, 1, 0, 1, 0],
           [0, 0, 1, 0, 1, 0, 0],
           [0, 0, 0, 1, 2, 1, 0],
           [0, 0, 1, 2, 1, 0, 0],
           [0, 1, 2, 2, 1, 1, 0]]
    # for i in range(ROW)[::-1]:
    for i in range(ROW):
        for j in range(COLUMN):
            print(check_diagonal(lst, i, j), end=" ")
        print('\n')
    print(check_horizontal(lst))
    print(playground)