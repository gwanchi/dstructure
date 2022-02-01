"""
Given two words as strings word1 and word2, create a function that returns the minimum number of operations required to convert word1 to word2. Note that we have 3 possible operations, we can either insert a character, or remove a charater, or replace a character.
"""
def minDistance(word1, word2, i=0, j=0):
    if i == len(word1):
        return len(word2)-j
    elif j == len(word2):
        return len(word1)-1
    elif word1[i] == word2[j]:
        return minDistance(word1, word2, i+1, j+1)
    else:
        return 1 + min(minDistance(word1, word2, i+1, j), minDistance(word1, word2, i, j+1), minDistance(word1, word2, i+1, j+1))

def minDistance2(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[0] * (m+1) for i in range(n+1)]
    for i in range(m+1): dp[0][i] = i
    for i in range(n+1): dp[i][0] = i
    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n][m]

