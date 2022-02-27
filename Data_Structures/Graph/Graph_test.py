from Graph import Graph
from Edge import Edge
from Vertex import Vertex

import unittest

class testGraph(unittest.TestCase):

    def setUp(self) -> None: 
       
        # Setup undirected graph with letters 
        a = Vertex("a")
        b = Vertex("b")
        c = Vertex("c")
        d = Vertex("d")
        e = Vertex("e")
        f = Vertex("f")

        edges = []
        edges.append(Edge(a, b, 3, False))
        edges.append(Edge(a, c, 5, False))
        edges.append(Edge(a, d, 4, False))
        edges.append(Edge(b, e, 3, False))
        edges.append(Edge(b, f, 5, False))
        edges.append(Edge(c, d, 2, False))
        edges.append(Edge(d, e, 1, False))
        edges.append(Edge(e, f, 2, False))

        graph = Graph(edges)

        # Setup directed graph with numbers
        one = Vertex(1)
        two = Vertex(2)
        three = Vertex(3)
        four = Vertex(4)
        five = Vertex(5)
        six = Vertex(6)
        seven = Vertex(7)

        print(graph.getEdgeList())
        print()
        print(graph.getAdjacencyList())

        edgesDirected = []
        edgesDirected.append(Edge(one, two, 1, True))
        edgesDirected.append(Edge(one, three, 1, True))
        edgesDirected.append(Edge(one, four, 1, True))
        edgesDirected.append(Edge(three, five, 1, True))
        edgesDirected.append(Edge(five, four, 1, True))
        edgesDirected.append(Edge(four, six, 1, True))
        edgesDirected.append(Edge(five, seven, 1, True))
        edgesDirected.append(Edge(seven, six, 1, True))

        directedGraph = Graph(edgesDirected)

        print(directedGraph.getEdgeList())
        print()
        print(directedGraph.getAdjacencyList())

    def test_add(self):
        self.assertTrue(1)

if __name__ == '__main__':
    unittest.main()