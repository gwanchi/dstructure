"""
Given an undirected graph of integers graph, represented by an adjacency list, and an integer root, create a function that prints its values in depth first search, by considering the vertex whose value is root as the arbitrary node.
"""
def dfs(graph, root, visited=None):
    if visited is None:
        visited = set()
    if root in visited:
        return
    else:
        print(root)
        visited.add(root)
        for neighbor in graph.adjList[root]:
            dfs(graph, neighbor, visited)