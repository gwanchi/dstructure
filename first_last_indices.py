"""
First and Last Indices of an Element in a Sorted Array

Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:

Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]

Solution:
While this could be done in O(n) time using the brute force method of iterating twice over the whole array, once from the left and once from the right, there is a more efficient O(log(n)) solution. We use two modified binary searches to find the first and last indices.

The algorithm operates in O(log(n)) time. Binary search cuts the space roughly in half after each iteration, which means that there are at most log(n) iterations. Even with two binary searches, our time complexity is two times O(log(n)).

The space complexity of the algorithm is equivalent to the recursion stack depth, or O(logn). We don't use any additional space otherwise (except for a few variables).

We can also implement this iteratively, in which the space complexity is reduced to O(1) because we remove the recursion stacks.
"""


class Solution:
    def getRange(self, arr, target):
        low = 0
        high = len(arr) - 1
        first = self.binarySearch(arr, low, high, target, True)
        last = self.binarySearch(arr, low, high, target, False)
        return [first, last]

    def binarySearch(self, arr, low, high, target, findLowest):
        if high >= low:
            mid = low + (high - low) // 2
            if findLowest:
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    return self.binarySearch(arr, mid + 1, high, target, findLowest)
                else:
                    return self.binarySearch(arr, low, mid - 1, target, findLowest)
            else:
                if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                    return mid
                elif target < arr[mid]:
                    return self.binarySearch(arr, low, mid - 1, target, findLowest)
                else:
                    return self.binarySearch(arr, mid + 1, high, target, findLowest)
        return -1

    def binarySearchIterative(self, arr, low, high, target, findLowest):
        while high >= low:
            mid = low + (high - low) // 2
            if findLowest:
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                    return mid
                elif target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


# Test program
#arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
arr = [8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
