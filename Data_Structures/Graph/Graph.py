from collections import OrderedDict, deque
from VertexDistancePair import VertexDistancePair

class Graph:
    ''' Adapted from GTx CS1332 Java Graph Class '''
    def __init__(self, edges = []):
        self.adjacencyList = OrderedDict() # Map of Vertex to other vertices
        self.edges = edges
        self.directed = False
        
        for edge in self.edges:
            self.adjacencyList.setdefault(edge.u, [])
            self.adjacencyList.setdefault(edge.v, [])
            self.adjacencyList.get(edge.u).append(VertexDistancePair(edge.v, edge.weight))
            if not edge.directed:
                self.adjacencyList.get(edge.v).append(VertexDistancePair(edge.u, edge.weight))
            else:
                self.directed = True

    def getEdgeList(self):
        return self.edges

    def getAdjacencyList(self):
        res = ""
        for key, value in self.adjacencyList.items():
            res += f"{key}: {value}\n"
        return res

    def bfs(self, startVertex):
        ''' Breadth First Search '''
        
        # Check if startVertex is in the graph
        if startVertex not in self.adjacencyList:
            return "Start vertex not found!"
        
        res = []
        vertexQ = deque() # Vertex queue
        vs = set() # Visited Set
        vs.add(startVertex)
        vertexQ.append(startVertex)

        while vertexQ: # While queue is not empty
            v = vertexQ.popleft()
            res.append(v)
            for w in self.adjacencyList.get(v): # Look at all adjacent vertices (w)
                if w.vertex not in vs:
                    vs.add(w.vertex)
                    vertexQ.append(w.vertex)
        
        return res
    
    def dfs(self, startVertex):
        ''' Depth First Search '''

         # Check if startVertex is in the graph
        if startVertex not in self.adjacencyList:
            return "Start vertex not found!"

        res = []
        vs = set() # Visited Set

        def dfsHelper(self, vertex, vs, res):
            res.append(vertex)
            vs.add(vertex)
            for w in self.adjacencyList.get(vertex):
                if w.vertex not in vs:
                    dfsHelper(self, w.vertex, vs, res)

        dfsHelper(self, startVertex, vs, res)

        return res

    def dijkstras(self, startVertex):
        return