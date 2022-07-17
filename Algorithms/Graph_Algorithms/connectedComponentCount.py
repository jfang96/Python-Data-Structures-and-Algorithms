def connectedComponentCount(graph):
    count = [0]
    visited = set()

    def dfs(graph, node):
        if node in visited:
            return
        visited.add(node)
        count[0] += 1
        for neighbor in graph[node]:
            dfs(graph, neighbor)

    for node in graph:
        dfs(graph, node)

    return count[0]


graph = {
    'i': ['j', 'k'], 
    'j': ['i'], 
    'k': ['i', 'm', 'l'], 
    'm': ['k'], 
    'l': ['k'], 
    'o': ['n'], 
    'n': ['o']
}

print(connectedComponentCount(graph))