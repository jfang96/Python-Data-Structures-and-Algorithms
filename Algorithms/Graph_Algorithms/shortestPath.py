from collections import deque


def shortestPath(graph, src, dst):
    q = deque()
    visited = set()
    q.append((src, 0))

    while q:
        node, distance = q.popleft()
        if node == dst: return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append((neighbor, distance + 1))
                visited.add(neighbor)

    return -1


graph = {
    1: [2, 3], 
    2: [1], 
    3: [1, 4, 5], 
    4: [3], 
    5: [3], 
    6: [7], 
    7: [6]
}

print(shortestPath(graph, 1, 5))