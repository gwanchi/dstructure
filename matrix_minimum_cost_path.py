"""
Given a matrix of integers matrix of size n*m, where each element matrix[i][j] represents the cost of passing from that cell, create a function returns the cost of the minimum cost path to go from the top left cell to the right bottom cell, knowing that you can only move to the right or to the bottom.
"""


# (Brute Force Approach) Recursive Solution ...
def minimumCostPath(matrix, i=0, j=0):
    n = len(matrix)  # number of rows ...
    m = len(matrix[0])  # number of columns ...
    if i == n - 1 and j == m - 1:
        return matrix[i][j]
    elif i == n - 1:
        return matrix[i][j] + minimumCostPath(matrix, i, j + 1)
    elif j == m - 1:
        return matrix[i][j] + minimumCostPath(matrix, i + 1, j)
    else:
        return matrix[i][j] + min(minimumCostPath(matrix, i + 1, j), minimumCostPath(matrix, i, j + 1))

# A far better result ...
def minimumCostPath2(matrix):
    n = len(matrix)
    m = len(matrix[0])
    costs = [[0] * m for i in range(n)]
    costs[0][0] = matrix[0][0]
    for i in range(1,m):
        costs[0][i] = costs[0][i-1] + matrix[0][i]
    for i in range(1,n):
        costs[i][0] = costs[i-1][0] + matrix[i][0]
    for i in range(1,n):
        for j in range(1,m):
            costs[i][j] = min(costs[i-1][j], costs[i][j-1]) + matrix[i][j]
    return costs[n-1][m-1]


matrix = [[3,10,1,3,7], [6,2,15,11,4], [11,8,14,32,9]]
print(minimumCostPath(matrix))
print(minimumCostPath2(matrix))
