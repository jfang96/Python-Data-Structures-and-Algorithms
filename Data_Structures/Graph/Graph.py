from collections import OrderedDict
from VertexDistancePair import VertexDistancePair

class Graph:
    ''' Adapted from GTx CS1332 Java Graph Class '''
    def __init__(self, edges):
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
