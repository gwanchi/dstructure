"""
Given a non-empty array of integers arr, create a function that returns the index of the peak element. We consider an element as peak if it's greater than or equal to its neighbors, the next and previous element, and the first element have at most one neighbor only. And if there are multiple peaks in arr, just return the index of one of them.
"""
def find_peak(arr):
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]<arr[mid+1]:
            left=mid+1
        else:
            right = mid
    return left