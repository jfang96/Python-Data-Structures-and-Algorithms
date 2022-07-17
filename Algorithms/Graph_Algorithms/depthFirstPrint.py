def depthFirstPrint(graph, source):
    stack = [source]
    while stack:
        cur = stack.pop()
        print(cur)
        for neighbor in graph[cur]:
            stack.append(neighbor)


def depthFirstPrint_recursive(graph, source):
    if not graph: return
    print(source)
    for neighbor in graph[source]:
        depthFirstPrint_recursive(graph, neighbor)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depthFirstPrint(graph, 'a')
depthFirstPrint_recursive(graph, 'a')