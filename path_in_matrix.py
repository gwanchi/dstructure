"""
Given a matrix of size n*m that contains only 0s and 1s, where 0 means that the cell is empty and 1 means that there is a wall in that cell, create a function that returns the number of paths that we can take to go from the top left cell to the right bottom cell, knowing that you can move to the right or to the bottom only.
"""
def paths(matrix, i=0, j=0):
    n=len(matrix)
    m=len(matrix[0])
    if i > n-1 or j > m-1 or matrix[i][j] == 1:
        return 0
    elif i == n-1 and j == m-1:
        return 1
    else:
        return paths(matrix, i+1, j) + paths(matrix, i, j+1)

# number of paths up to each cell ...
def paths2(matrix):
    n=len(matrix)
    m=len(matrix[0])
    dp = [([0] * m) for i in range(n)]
    if matrix[0][0] == 1: dp[0][0] = 0
    else: dp[0][0] = 1
    for i in range(1,m):
        if matrix[0][i] == 1: dp[0][i] = 0
        else: dp[0][i] = dp[0][i-1]
    for i in range(1, n):
        if matrix[i][0] == 1: dp[i][0] = 0
        else: dp[i][0] = dp[i-1][0]
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j] == 1: dp[i][j] = 0
            else: dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]

