"""
Given an array of integers arr, create a function that returns the length of the longest consecutive sequence that can be found in arr.
"""
def longestConsecutiveSequence(arr):
    if len(arr) < 2:
        return len(arr)
    maxLength = 1
    values = set(arr)
    for element in values:
        left = element
        while left-1 in values:
            left -= 1
        right = element
        while right+1 in values:
            right += 1
        maxLength = max(maxLength, right-left+1)
    return maxLength

def longestConsecutiveSequence2(arr):
    if len(arr) < 2:
        return len(arr)
    arr.sort()
    maxLength = 1
    length = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]+1:
            length += 1
        elif arr[i] == arr[i-1]:
            pass
        else:
            length = 1
        maxLength = max(maxLength, length)
    return maxLength

def longestConsecutiveSequence3(arr):
    if len(arr) < 2:
        return len(arr)
    maxLength = 1
    values = set(arr)
    for element in values:
        if element-1 in values:
            continue
        else:
            right = element
            while right+1 in values:
                right += 1
    return maxLength

