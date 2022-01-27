"""
Given a binary tree root, create a boolean function that checks if it's a binary search tree. Note that in a binary search tree, every node must be strictly greater than all nodes on its left subtree, and strictly smaller than all nodes on its right subtree.
"""
def isBst(root, min = float("-inf"), max = float("inf")):
    if root is None:
        return True
    elif root.data <= min or root.data >= max:
        return False
    else:
        return isBst(root.left, min, root.data) and isBst(root.right, root.data, max)
