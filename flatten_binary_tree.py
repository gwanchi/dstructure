"""
Given a binary tree root, create a function that flattens it to a linked list in-place by following the preorder traversal
"""
def flattenTree(root):
    if root is None:
        return
    else:
        flattenTree(root.left)
        flattenTree(root.right)
        rightSubtree = root.right
        root.right = root.left
        root.left = None
        temp = root
        while temp.right is not None:
            temp = temp.right
        temp.right = rightSubtree