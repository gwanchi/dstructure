"""
Add two numbers as a linked list

You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return self.val


class Solution:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        self.node = None

    def addTwoNumbersRecursive(self, l1, l2, c):
        val = l1.val + l2.val + c
        c = val // 10
        ret = Node(val % 10)

        if l1.next != None or l2.next != None:
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)
            ret.next = self.addTwoNumbersRecursive(l1.next,l2.next,c)
        else:
            if c:
                ret.next = Node(c)
        return ret

    def addTwoNumbersIterative(self, l1, l2):
        a = l1
        b = l2
        c = 0
        ret = current = None

        while a or b:
            val = a.val + b.val + c
            c = val / 10
            if not current:
                ret = current = Node(val % 10)
            else:
                current.next = Node(val % 10)
                current = current.next
            if a.next or b.next:
                if not a.next:
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
            a = a.next
            b = b.next
        return ret

    def __repr__(self):
        _rtn=''
        self.node = self.addTwoNumbersRecursive(self.l1, self.l2, 0)
        # self.node = self.addTwoNumbersIterative(self.l1, self.l2)
        while self.node is not None:
            _rtn += ' ' + str(self.node.val)
            self.node = self.node.next
        return _rtn


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution(l1, l2)
print(answer)
