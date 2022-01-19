"""
Sorting a list with 3 unique numbers

Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:

Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]

Solution 1:

This solution counts the number of 1, 2, and 3, in the list, and then creates a new list with the same numbers of 1, 2, and 3!

This solution takes O(n) time to iterate through all the elements, and takes O(n) space to create the new list. Can we do better?

Solution 2:

We can actually sort the list in place if there are only 3 unique numbers. The general idea is to swap the lowest number to the leftmost index that is not sorted yet, and swap the highest number to the rightmost index that is not sorted yet.

In this case, we have one_idx that represents the leftmost index that is not sorted (so everything left of one_idx is a 1), and three_idx that represents the rightmost index that is not sorted( so everything right of three_idx is a 3).

We go through each element in the list and swap with one_idx if we see a 1, or swap with the three_idx if we see a 3. If the element is a 2 it is in the middle of the list already and no action needs to be done.

This code has a time complexity of O(n), as we only iterate through each element in the list once (once elements are swapped away we will never 'see' them again). The space complexity is O(1) as we are just swapping elements in the list.
"""

def sortNums(nums):
    one_idx = 0 # represents the leftmost index that is not 0
    three_idx = len(nums) - 1 # Represents the rightmost index that is not 2

