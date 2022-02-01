"""
Given a binary search tree (binary tree which root must be greater that all the root in its left sub tree and less that all of the roots in its right sub tree ) root, and an integer num, create a function that deletes the node that contains num then returns root.
"""
def getMinNode(root):
    while root.left is not None:
        root = root.left
    return root

def deleteNodeBst(root, num):
    if root is None:
        return None
    elif num < root.data:
        root.left = deleteNodeBst(root.lef, num)
    elif num > root.data:
        root.right = deleteNodeBst(root.right, num)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = getMinNode(root.right)
            root.data = successor.data
            root.right = deleteNodeBst(root.right, successor.data)
    return root