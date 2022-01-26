"""
Given a binary tree of integers root, create a function that reverses it left to right in-place
"""
def reverse_tree(tree):
    if tree is None:
        return
    tree.left , tree.right = tree.right, tree.left
    reverse_tree(tree.left)
    reverse_tree(tree.right)
