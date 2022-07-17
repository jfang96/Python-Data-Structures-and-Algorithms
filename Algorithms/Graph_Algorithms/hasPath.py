from collections import deque


def hasPath(graph, src, dst):
    if src == dst: return True

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst):
            return True

    return False

def hasPath_bfs(graph, src, dst):
    q = deque()
    q.append(src)

    while q:
        cur = q.popleft()
        if cur == dst: return True
        for neighbor in graph[cur]:
            q.append(neighbor)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

print(hasPath(graph, 'a', 'd'))
print(hasPath_bfs(graph, 'a', 'd'))