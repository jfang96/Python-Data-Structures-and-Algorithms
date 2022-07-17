from collections import deque

def breadthFirstPrint(graph, source):
    q = deque()
    q.append(source)

    while q:
        cur = q.popleft()
        print(cur)
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

breadthFirstPrint(graph, 'a')