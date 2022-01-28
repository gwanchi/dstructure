"""
Given a non-empty array of non-negative integers arr, where each element represents the maximum jump that we can perform from that index, create a boolean function that checks if we can reach the last index starting from the first one.
"""
def canJump(arr, i=0):
    if i == len(arr)-1:
        return True
    for j in range(1, arr[i]+1):
        if canJump(arr, i+j):
            return True
    return False

def canJump2(arr):
    n=len(arr)
    dp=[False]*n
    dp[0]=True
    for i in range(n):
        if not dp[i]:
            return False
        elif i+arr[i] >= n-1:
            return True
        else:
            for j in range(1, arr[i]+1):
                dp[i+j] = True
    return dp[n-1]

def canJump3(arr):
    n=len(arr)
    maxIndex=0
    for i in range(n):
        if i > maxIndex:
            return False
        else:
            maxIndex = max(maxIndex, i+arr[i])
    return maxIndex >= n-1

def canJump4(arr):
    adjList = {}
    for i in range(len(arr)):
        adjList[i]=[]
        for j in range(1, arr[i]+1):
            if (i+j) < len(arr):
                adjList[i].append(i+j)
    queue = [0]
    visited = {0}
    i = 0
    while i < len(queue):
        vertex = queue[i]
        i += 1
        if vertex == len(arr)-1:
            return True
        for neighbor in adjList[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return False