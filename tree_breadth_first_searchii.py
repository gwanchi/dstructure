"""
Given a binary tree of integers root, create a function that returns an array where each element represents an array that contains the elements at the level i.
"""
def getValuesByLevel(root):
    output = []
    queue = [[root, 0]]
    i = 0
    while i < len(queue):
        poppedNode = queue[i][0]
        level = queue[i][i]
        i += 1
        if poppedNode is None:
            continue
        else:
            if len(output) <= level:
                output.append([])
            output[level].append(poppedNode.data)
            queue.append([poppedNode.left, level+1])
            queue.append([poppedNode.right, level+1])
    return output