"""
Given a non-empty binary tree root, create a function that returns the maximum path sum. Note that for this problem, a path goes from a node to another one by traversing edges between them, and that the path must have at least one node, and it does not have to pass by the root
"""
def dfs(root, globalMaxSum):
    if root is None:
        return float("-inf")
    else:
        left = dfs(root.left, globalMaxSum)
        right = dfs(root.right, globalMaxSum)
        maxFromTop = max(root.data, root.data + left, root.data + right)
        maxNoTop = max(maxFromTop, root.data + left + right)
        globalMaxSum[0] = max(globalMaxSum[0], maxNoTop)
        return  maxFromTop

def maxPathSum(root):
    globalMaxSum = [float("-inf")]
    dfs(root, globalMaxSum)
    return globalMaxSum[0]

