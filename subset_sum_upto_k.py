"""
Given an array of strictly positive integers arr and an integer k, create a function that returns the number of subsets that sum up to k
"""
def subsetsThatSumUpToK(arr, k, i = 0, sum = 0):
    if sum == k:
        return 1
    elif sum > k or i >= len(arr):
        return 0
    else:
        return subsetsThatSumUpToK(arr, k, i+1, sum + arr[i]) + subsetsThatSumUpToK(arr, k, i+1, sum)

def subsetsThatSumUpToK2(arr, k, i=0, sum=0, memoiz=None):
    if memoiz is None:
        memoiz = {}
    key = str(i) + " " + str(sum)
    if memoiz.get(key) is not None:
        return memoiz[key]
    elif sum == k:
        return 1
    elif sum > k or i >= len(arr):
        return 0
    else:
        nbSubsets = subsetsThatSumUpToK2(arr, k, i+1,sum + arr[i], memoiz) + subsetsThatSumUpToK2(arr, k, i+1, sum, memoiz)
        memoiz[key] = nbSubsets
        return nbSubsets