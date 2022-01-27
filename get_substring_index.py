"""
Given two strings st1 and str2, create a function that returns the first index where we can find str2 in str1. If we cannot find str2 in str1, the function must return -1.
13 - Get substring index ...
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

def substrIndex(str1, str2):
    n = len(str1)
    m = len(str2)
    if m > n : return -1
    if m ==n : return 0 if str2 == str1 else -1
    if str2 == "" : return 0
    lpsArr = getLpsArr(str2)
    j = 0
    i = 0
    while i < n and j < m:
        if str1[i] == str2[j]:
            i += 1
            j += 1
        elif j > 0:
            j = lpsArr[j-1]
        else:
            i += 1
    return -1 if j < m else i-j
