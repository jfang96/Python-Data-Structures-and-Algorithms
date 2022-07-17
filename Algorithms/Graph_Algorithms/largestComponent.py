def largestComponent(graph):
    largest = 0
    visited = set()

    def dfs(graph, node):
        if node in visited:
            return 0
        visited.add(node)
        size = 1
        for neighbor in graph[node]:
            size += dfs(graph, neighbor)
        return size

    for node in graph:
        largest = max(largest, dfs(graph, node))
    
    return largest


graph = {
    1: [2, 3], 
    2: [1], 
    3: [1, 4, 5], 
    4: [3], 
    5: [3], 
    6: [7], 
    7: [6]
}


print(largestComponent(graph))
