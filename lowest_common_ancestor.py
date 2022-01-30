"""
Given a binary tree root and two integers num1 and num2, create a function that returns the lowest common ancestor of num1 and num2. The lowest common ancestor is the deepest node in root that has both num1 and num2 as descendants, and we consider a node as a descendant of itself.
"""


def getPath(root, path, num):
    if root is None:
        return False
    path.append(root)
    if root.data == num:
        return True
    if getPath(root.left, path, num) or getPath(root.right, path, num):
        return True
    path.pop()
    return False


def lowestCommonAncestor(root, num1, num2):
    pathNum1 = []
    pathNum2 = []
    if not getPath(root, pathNum1, num1) or not getPath(root, pathNum2, num2):
        return None
    minLength = min(len(pathNum1), len(pathNum2))
    i = 0
    while i < minLength:
        if pathNum1[i].data == pathNum2[i].data:
            i += 1
        else:
            break
    return pathNum1[i - 1]

def lowestCommonAncestor2(root, num1, num2):
    if root is None:
        return None
    if root.data == num1 or root.data == num2:
        return root
    leftLCA = lowestCommonAncestor2(root.left, num1, num2)
    rightLCA = lowestCommonAncestor2(root.right, num1, num2)
    if leftLCA is not None and rightLCA is not None:
        return root
    return leftLCA if leftLCA is not None else rightLCA

