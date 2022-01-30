"""
Given two linked lists list1 and list2 that represent two positive integers, create a function that returns the linked list that represents their sum
"""
def addTwoLinkedLists(list1, list2):
    output = LinkedList()
    ptr1 = list1.head
    ptr2 = list2.head
    tail = None
    carry = 0
    while ptr1 or ptr2 or carry > 0:
        digit1 = ptr1.data if ptr1 else 0
        digit2 = ptr2.data if ptr2 else 0
        nextDigit = (digit1 + digit2 + carry) % 10
        carry = (digit1 + digit2 + carry) // 10
        newNode = Node(nextDigit)
        if output.head is None:
            output.head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next
        ptr1 = ptr1.next if ptr1 else None
        ptr2 = ptr2.next if ptr2 else None
    return output