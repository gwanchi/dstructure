def formingMagicSquare(s):
    cost = []
    t = [
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
    ]
    for i in range(8):
        j = 0
        for k in range(3):
            for l in range(3):
                cost[i] = cost[i] + abs(t[i][j] - s[k][l])
                j+=1
    return min(cost)

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
print(formingMagicSquare(s))