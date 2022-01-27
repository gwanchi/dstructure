"""
Given a linked list of integers list, create a boolean function that checks if it's a palindrome linked list in constant space complexity.
"""
def is_palindromelist(list):
    length = 0
    temp = list.head
    while temp:
        length += 1
        temp = temp.next
    left = list.head
    for i in range(length//2):
        right = list.head
        for j in range(length-i-1):
            right = right.next
        if left.data != right.data:
            return False
        left = left.next
    return True

def is_palindromelist2(list):
    slow=fast=list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow = reverse_list(slow)
    head = list.head
    while slow:
        if slow.data != head.data:
            return False
        slow = slow.next
        head = head.next
    return True

def reverse_list(list):
    previous=None
    current=list.head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    list.head = previous

