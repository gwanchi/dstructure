"""
Given a positive integer n, create a function that returns the number of possible ways to put n queens in an n*n chessboard such that no two queens attack each other. Note that two queens attack each other when they are on the same row, column, or diagonal.
"""
def isNotAttacked(board, row, col):
    i = row-1
    jLeft = col-1
    jRight = col+1
    while i >= 0:
        if board[i][col] == 'Q' or (jLeft >= 0 and board[i][jLeft] == 'Q') or (jRight < len(board) and board[i][jRight] == 'Q'):
            return False
        else:
            i -= 1
            jLeft -= 1
            jRight += 1
    return True

def nQueensRec(n, board, row):
    if row >= n:
        return 1
    sumWays = 0
    for i in range(n):
        if isNotAttacked(board, row, i):
            board[row][i] = 'Q'
            sumWays += nQueensRec(n, board, row+1)
            board[row][i] = '.'
    return sumWays

def nQueens(n):
    board = [['.'] * n for i in range(n)]
    return nQueensRec(n, board, 0)

print(nQueens(8))