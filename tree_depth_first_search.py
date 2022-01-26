"""
Given a binary tree of integers root, create 3 functions to print the elements, one for pre-order, one for in-order, and one in postorder.
Pre-order: print root data, then print left subtree, then print right subtree.
In-order: print left subtree, then print root data, then print right subtree
Post-order: print left subtree, then print right subtree, then print root data
"""

def dfspreoder(root):
    if root is None:
        return
    print(root.data)
    dfspreoder(root.left)
    dfspreoder(root.right)

def dfsinorder(root):
    if root is None:
        return
    dfsinorder(root.left)
    dfsinorder(root.data)
    dfsinorder(root.left)

def dfspostorder(root):
    if root is None:
        return
    dfspostorder(root.left)
    dfspostorder(root.right)
    dfspostorder(root.data)

