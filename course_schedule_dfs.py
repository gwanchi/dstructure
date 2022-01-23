"""
V - Vertexes
E - Edges
"""
from collections import deque

def dfs(graph, vertex, stack, order, visited):
    stack.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor in stack:
            return False
        if neighbor not in visited:
            visited.add(neighbor)
            if not dfs(graph, neighbor, stack, order, visited):
                return False
    stack.remove(vertex)
    order.append(vertex)
    return True

def top_sort(graph):
    visited = set()
    stack= []
    order=[]
    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            dfs(graph, vertex, stack, order, visited)
    return order[::-1]

def course_schedule(n, prerequisites):
    graph = [[] for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
    visited  =set()
    stack=[]
    order=[]
    for course in range(n):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, stack, order, visited):
                return False
    return True

def course_schedule_bfs(n, prerequisites):
    graph = [[] for i in range(n)]
    indegree = [0 for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]]+=1
    order=[]
    queue=deque([i for i in range(n) if indegree[i] == 0])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor]-=1
            if indegree[neighbor]==0:
                queue.append(neighbor)
    return order

