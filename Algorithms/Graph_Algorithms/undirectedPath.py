from buildGraph import buildGraph


def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    visited = set()

    def hasPath (graph, src, dst):
        if src not in graph or dst not in graph: return False
        if src == dst: return True
        if src in visited: return False

        visited.add(src)
        
        for neighbor in graph[src]:
            if hasPath(graph, neighbor, dst): 
                return True
        
        return False

    return hasPath(graph, nodeA, nodeB)

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


print(undirectedPath(edges, 'm', 'a'))