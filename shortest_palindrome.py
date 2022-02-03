"""
Given a string str, create a function that returns the shortest palindrome that we can get aby adding characters in front of str. Note that a palindrome is a string that can be read in the same way from the left and from the right.
"""

def getLpsArr(str):
    lpsArr = [0]*len(str)
    length = 0
    i = 1
    while i < len(str):
        if str[i] == str[length]:
            length += 1
            lpsArr[i] = length
            i += 1
        elif length > 0:
            length = lpsArr[length-1]
        else:
            lpsArr[i] = 0
            i += 1
    return lpsArr

def shortestPalindrome(str):
    mirrorLength = 0
    for i in range(len(str)+1):
        if str[:i] == str[:i][::-1]:
            mirrorLength = i
    return str[mirrorLength:][::-1] + str

def shortestPalindrome2(str):
    concatenation = str + "#" + str[::-1]
    lpsArr = getLpsArr(concatenation)
    mirrorLength = lpsArr[-1]
    return str[mirrorLength:][::-1] + str

print(shortestPalindrome2("acbcabcbb"))