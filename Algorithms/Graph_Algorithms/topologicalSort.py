# Pick an unvisited node
# Beginning at the selected node, dfs, exploring only unvisited nodes
# On the recursive callback of the DFS, add current node to the topoligical ordering in reverse order

def topologicalSort(graph):
    visited = set()
    N = len(graph)
    ordering = [None] * N
    index = N-1

    def dfs(node):
        nonlocal index
        if node in visited:
            return index
        visited.add(node)
        for neighbor in graph[node]:
            index = dfs(neighbor)
        ordering[index] = node
        return index - 1

    for node in graph:
        index = dfs(node)

    return ordering
        
    

graph = {
    'a': ['b', 'c'],
    'b': ['c', 'd'],
    'c': ['f'],
    'd': ['f', 'e'],
    'e': [],
    'f': []
}

print(topologicalSort(graph))