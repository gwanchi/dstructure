"""
Given an undirected graph of integers graph, represented by an adjacency list, and an integer root, create a function that prints its values in depth first search, by considering the vertex whose value is root as the arbitrary node.
"""
def bfs(graph, root):
    queue = [root]
    visited = {root}
    i = 0
    while i < len(queue):
        vertex = queue[i]
        i += 1
        print(vertex)
        for neighbor in graph.adjList[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
