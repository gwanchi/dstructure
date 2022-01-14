"""
Reverse a Linked List

Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

Example:

Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL

Iterative Solution: Traverse the list. Change each node's next pointer to point to the previous element in the list. Since this is a singly linked list and the nodes do not store their previous elements, the previous element must be stored in a temporary variable. We must also store the next node before changing the reference to the previous value.

Recursive Solution: Assume the list has m nodes. Assume you are at node k and that the rest of the list from k+1 to m has already been reversed. Thus, we want node k+1's next node to point to our current node, k. We also know that k+1 is k.next. So, in order to ensure that k+1's next node points to k, we need k.next.next = k. We also need to be sure to set the final node's next node to null, otherwise we will have a cycle.

Time Complexity: The iterative solution has complexity O(n), where n is the length of the list. The recursive solution also has complexity O(n).
Space Complexity: The iterative solution is O(1). The recursive solution is O(n), which comes from the stack space used for recursion. The recursion depth could be up to n levels deep.

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output+= " "
            node = node.next
            # print(id(node))
        print(output)

    # Iterative Solution using temporary variables
    def reverseIteratively(selfself, head):
        previous=None
        current = head
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode

    # Recursive Solution
    def reverseRecursively(self, head):
        # print(id(head))
        # Ensures there are no cycles in the program
        if not head or not head.next:
            return head
        node = self.reverseRecursively(head.next)
        head.next.next = head
        head.next = None
        return node

# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial List: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4