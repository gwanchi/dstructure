"""
Given an amount of money, and a set of possible coins, create a function that returns the minimum number of coins needed to make that amount. Note that if there exists no combination to do so, the function must return -1.
"""
def coinChangeRec(amount, coins):
    if amount == 0:
        return 0
    minCoins = float("inf")
    for coin in coins:
        if (amount-coin) >= 0:
            minCoins = min(minCoins, 1 + coinChangeRec(amount-coin, coins))
    return minCoins

def coinChange(amount, coins):
    minCoins = coinChangeRec(amount, coins)
    return -1 if minCoins == float("inf") else minCoins

def coinChange2(amount, coins):
    nbCoinsArr = [float("inf")]*(amount+1)
    nbCoinsArr[0] = 0
    for i in range(1, amount+1):
        minCoins = float("inf")
        for coin in coins:
            if (i-coin) >= 0:
                minCoins = min(minCoins, 1 + nbCoinsArr[i-coin])
        nbCoinsArr[i] = minCoins
    return -1 if nbCoinsArr[amount] == float("inf") else nbCoinsArr[amount]

