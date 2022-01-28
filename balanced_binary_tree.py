"""
Given a binary tree of integers root, create a boolean function that checks if it's a balanced binary tree. A binary tree is considered as balanced if its left and right subtree are balanced, and the difference between their heights is at most 1
"""
def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
    if root is None:
        return True
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    return isBalanced(root.left) and isBalanced(root.right) and abs(leftHeight-rightHeight) <= 1

def isBalanced2(root, height=None):
    if height is None:
        height = [0]
    if root is None:
        return True
    leftHeight = [0]
    rightHeight = [0]
    isLeftBalanced = isBalanced2(root.left, leftHeight)
    isRightBalanced = isBalanced2(root.right, rightHeight)
    height[0] = 1 + max(leftHeight[0], rightHeight[0])
    return isLeftBalanced and isRightBalanced and abs(leftHeight[0]-rightHeight[0]) <= 1