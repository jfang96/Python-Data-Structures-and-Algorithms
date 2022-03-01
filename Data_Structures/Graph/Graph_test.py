from Graph import Graph
from Edge import Edge
from Vertex import Vertex

import unittest

class testGraph(unittest.TestCase):
    ''' Test cases for graph algorithms. Adapted from GTx CS1332 GraphAlgorithmsStudentTests Class '''

    def setUp(self) -> None: 
        self.a = Vertex("a")
        self.b = Vertex("b")
        self.c = Vertex("c")
        self.d = Vertex("d")
        self.e = Vertex("e")
        self.f = Vertex("f")
        self.one = Vertex(1)
        self.two = Vertex(2)
        self.three = Vertex(3)
        self.four = Vertex(4)
        self.five = Vertex(5)
        self.six = Vertex(6)
        self.seven = Vertex(7)

        self.graph = Graph()
        self.directedGraph = Graph()

        # Setup undirected graph with letters 
        self.edges = []
        self.edges.append(Edge(self.a, self.b, 3, False))
        self.edges.append(Edge(self.a, self.c, 5, False))
        self.edges.append(Edge(self.a, self.d, 4, False))
        self.edges.append(Edge(self.b, self.e, 3, False))
        self.edges.append(Edge(self.b, self.f, 5, False))
        self.edges.append(Edge(self.c, self.d, 2, False))
        self.edges.append(Edge(self.d, self.e, 1, False))
        self.edges.append(Edge(self.e, self.f, 2, False))

        self.graph = Graph(self.edges)

        # Setup directed graph with numbers
        self.edgesDirected = []
        self.edgesDirected.append(Edge(self.one, self.two, 1, True))
        self.edgesDirected.append(Edge(self.one, self.three, 1, True))
        self.edgesDirected.append(Edge(self.one, self.four, 1, True))
        self.edgesDirected.append(Edge(self.three, self.five, 1, True))
        self.edgesDirected.append(Edge(self.five, self.four, 1, True))
        self.edgesDirected.append(Edge(self.four, self.six, 1, True))
        self.edgesDirected.append(Edge(self.five, self.seven, 1, True))
        self.edgesDirected.append(Edge(self.seven, self.six, 1, True))

        self.directedGraph = Graph(self.edgesDirected)
        

    def test_creation(self):
        print("Graph:")
        print(self.graph.getEdgeList())
        print()
        print(self.graph.getAdjacencyList())
        print()

        print("Directed Graph:")
        print(self.directedGraph.getEdgeList())
        print()
        print(self.directedGraph.getAdjacencyList())
        self.assertTrue(1)
    
    
    def test_bfs(self):
        bfsCorrect = []
        bfsCorrect.append(self.a)
        bfsCorrect.append(self.b)
        bfsCorrect.append(self.c)
        bfsCorrect.append(self.d)
        bfsCorrect.append(self.e)
        bfsCorrect.append(self.f)

        bfsAnswer = self.graph.bfs(self.a)
        print(f"BFS Answer: {bfsAnswer}\nBFS Correct: {bfsCorrect}")
        self.assertEqual(bfsCorrect, bfsAnswer)

    def test_bfsDirected(self):
        bfsCorrect = []
        bfsCorrect.append(self.one)
        bfsCorrect.append(self.two)
        bfsCorrect.append(self.three)
        bfsCorrect.append(self.four)
        bfsCorrect.append(self.five)
        bfsCorrect.append(self.six)
        bfsCorrect.append(self.seven)

        bfsAnswer = self.directedGraph.bfs(self.one)
        print(f"BFS Answer: {bfsAnswer}\nBFS Correct: {bfsCorrect}")
        self.assertEqual(bfsCorrect, bfsAnswer)

    def test_dfs(self):
        dfsCorrect = []
        dfsCorrect.append(self.a)
        dfsCorrect.append(self.b)
        dfsCorrect.append(self.e)
        dfsCorrect.append(self.d)
        dfsCorrect.append(self.c)
        dfsCorrect.append(self.f)

        dfsAnswer = self.graph.dfs(self.a)
        print(f"DFS Answer: {dfsAnswer}\nDFS Correct: {dfsCorrect}")
        self.assertEqual(dfsCorrect, dfsAnswer)

    def test_dfsDirected(self):
        dfsCorrect = []
        dfsCorrect.append(self.one)
        dfsCorrect.append(self.two)
        dfsCorrect.append(self.three)
        dfsCorrect.append(self.five)
        dfsCorrect.append(self.four)
        dfsCorrect.append(self.six)
        dfsCorrect.append(self.seven)

        dfsAnswer = self.directedGraph.dfs(self.one)
        print(f"DFS Answer: {dfsAnswer}\nDFS Correct: {dfsCorrect}")
        self.assertEqual(dfsCorrect, dfsAnswer)

if __name__ == '__main__':
    unittest.main()