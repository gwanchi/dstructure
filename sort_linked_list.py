"""
Given a linked list list, create a function that sorts it in ascending order. Note that the function returns nothing, the list must be sorted in-place.
"""

# Sorting using Bubble Sort
def sortArray(arr):
    i = 0
    while i < len(arr):
        j = 0
        while (j+1) < len(arr):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i += 1

# sort linked list
def sortllist(list):
    i = list.head
    while i:
        j = list.head
        while j.next:
            if j.data > j.next.data:
                j.data, j.next.data = j.next.data, j.data
            j = j.next
        i = i.next