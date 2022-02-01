"""
Given an array of integers arr, create a function than returns all its possible permutations without duplicates, the order doesn't matter.
"""
def getPermutations(arr):
    if len(arr) < 2:
        return [arr]
    else:
        permutations = []
        for i in range(len(arr)):
            if arr[i] not in arr[:i]:
                remaining = arr.copy()
                remaining.pop(i)
                remainingPermutations = getPermutations(remaining)
                removedElement = [arr[i]]
                for permutation in remainingPermutations:
                    permutations.append(removedElement + permutation)
        return permutations

def getNextGreaterPermutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i == -1:
        return arr
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = arr[:i:-1]
    return arr

def getPermutations2(arr):
    if len(arr) < 2:
        return [arr]
    arr = sorted(arr)
    permutations = [arr.copy()]
    greatestPermutation = arr[::-1]
    while arr != greatestPermutation:
        arr = getNextGreaterPermutation(arr)
        permutations.append(arr.copy())
    return permutations