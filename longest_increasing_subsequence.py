"""
Given an array of integers arr, create a function that returns the length of the longest increasing subsequence. Note that the subsequence must be strictly increasing.
"""
def lis(arr, i = 0, previous = float("-inf")):
    if i == len(arr):
        return 0
    elif arr[i] <= previous:
        return lis(arr, i+1, previous)
    else:
        return max(1+lis(arr, i+1, arr[i]), lis(arr, i+1, previous))

# Using Dynamic Programming
def lis2(arr):
    if (len(arr) < 2):
        return len(arr)
    dp = [0] * len(arr)
    maxLength = 0
    for i in range(len(arr)):
        maxPreviousLength = 0
        for j in range(i):
            if arr[i] > arr[j]:
                maxPreviousLength = max(maxPreviousLength, dp[j])
        dp[i] = maxPreviousLength + 1
        maxLength = max(maxLength, dp[i])
    return maxLength

# Binary Search Algorithm
def ceilIndex(arr, num):
    left = 0
    right = len(arr) - 1
    while left < right - 1:
        mid = (left+right)//2
        if num == arr[mid]:
            return mid
        elif num < arr[mid]:
            right = mid
        else:
            left = mid
    return right

def lis3(arr):
    if len(arr) < 2:
        return len(arr)
    subsequence = []
    subsequence.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] <= subsequence[0]:
            subsequence[0] = arr[i]
        elif arr[i] > subsequence[-1]:
            subsequence.append(arr[i])
        else:
            subsequence[ceilIndex(subsequence, arr[i])] = arr[i]
    return len(subsequence)

