"""
Given a string str made of digits, create a function that returns with how many ways we can decode it, knowing that 1 is decoded as the letter A, 2 is decoded as the letter B, and so on until 26 that is decoded as the letter Z
"""


def waysToDecode(str, i=0):
    n = len(str)
    if n == 0 or (i < n and str[i] == "0"):
        return 0
    elif i >= n - 1:
        return 1
    elif "10" <= (str[i] + str[i + 1]) <= "26":
        return waysToDecode(str, i + 1) + waysToDecode(str, i + 2)
    else:
        return waysToDecode(str, i + 1)


def waysToDecode2(str):
    n = len(str)
    if n == 0 or str[0] == "0":
        return 0
    beforePrevious = 1
    previous = 1
    for i in range(1, n):
        current = 0
        if str[i] != "0":
            current += previous
        if "10" <= (str[i - 1] + str[i]) <= "26":
            current += beforePrevious
        previous, beforePrevious = current, previous
    return previous


print(waysToDecode2("1348976633882293948585"))
