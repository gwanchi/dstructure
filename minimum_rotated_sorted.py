"""
Given a non-empty rotated sorted array of integers arr that has no duplicates, create a function that returns the minimum.
Note that the array is sorted in ascending order, and that it's rotated by an unknown number of positions to the right.
"""
def minimum(arr):
    left = 0
    right = len(arr) - 1
    if arr[right] > arr[left]: return arr[left]
    while left < right:
        mid = (left + right)//2
        if arr[mid+1] < arr[mid] : return arr[mid+1]
        elif arr[mid] < arr[mid-1]: return arr[mid]
        elif arr[mid] > arr[right]: left = mid+1
        else: right = mid-1
    return arr[left]

def minimumRec(arr, left, right):
    if left >= right:
        return arr[left]
    elif arr[right] > arr[left]:
        return arr[left]
    mid = (left+right)//2
    if arr[mid+1] < arr[mid]:
        return arr[mid+1]
    elif arr[mid] < arr[mid-1]:
        return arr[mid]
    elif arr[mid] > arr[right]:
        return minimumRec(arr, mid+1, right)
    else:
        return minimumRec(arr, left, mid-1)

def minimum2(arr):
    return minimumRec(arr, 0, len(arr)-1)