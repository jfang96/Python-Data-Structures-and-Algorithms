def buildGraph(edges):
    graph = {}

    for nodeA, nodeB in edges:
        graph.setdefault(nodeA, []).append(nodeB)
        graph.setdefault(nodeB, []).append(nodeA)

    return graph


# edges = [
#     ['i', 'j'],
#     ['k', 'i'],
#     ['m', 'k'],
#     ['k', 'l'],
#     ['o', 'n']
# ]


# print(buildGraph(edges))