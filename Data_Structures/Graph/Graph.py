from collections import OrderedDict, deque
from DisjointSet import DisjointSet
from VertexDistancePair import VertexDistancePair
import math

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from MinHeap import MinHeap

class Graph:
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

    def size(self):
        return len(self.adjacencyList)

    def getEdgeList(self):
        return self.edges

    def getVertices(self):
        return self.adjacencyList.keys()

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

        vs = set() # Visited Set
        distances = {}
        queue = MinHeap()

        # Set all distances to infinity
        for v in self.adjacencyList:
            distances[v] = math.inf
        
        # Add start vertex distance as 0
        queue.add(VertexDistancePair(startVertex, 0))

        # Go through queue until all nodes have been visited
        while not queue.isEmpty() and len(vs) < self.size():
            vdPair = queue.remove()
            vertex = vdPair.vertex
            dist = vdPair.distance
            if vertex not in vs:
                vs.add(vertex)
                # Update shortest distance 
                distances[vertex] = min(distances[vertex], dist)
                for adjVdPair in self.adjacencyList.get(vertex):
                    adjVertex = adjVdPair.vertex
                    adjDist = adjVdPair.distance
                    if adjVertex not in vs:
                        queue.add(VertexDistancePair(adjVertex, dist+adjDist))

        return distances

    def kruskals(self):
        ''' Kruskal's Algorithm for finding MST '''
        dsMap = {} # Disjoint Set map
        mst = set() # MST Edge set
        queue = MinHeap()

        for edge in self.edges:
            queue.add(edge)
            dsMap[edge.u] = DisjointSet()
            dsMap[edge.v] = DisjointSet()

        while not queue.isEmpty() and len(mst) < self.size() - 1:
            edge = queue.remove()
            uDS = dsMap[edge.u] # Disjoint set of u
            vDS = dsMap[edge.v] # Disjoint set of v
            if not uDS.parent == vDS.parent:
                mst.add(edge)
                uDS.union(vDS)

        return mst

    def prims(self, startVertex):
        ''' Prim's algorithm for finding MST '''
        mst = set() # MST Edge set
        vs = set() # Visited Set
        queue = MinHeap()
        
        for edge in self.edges:
            if edge.u == startVertex or edge.v == startVertex:
                queue.add(edge)

        vs.add(startVertex)

        while not queue.isEmpty() and len(vs) < self.size():
            edge = queue.remove()
            # u-v
            if edge.v not in vs:
                vs.add(edge.v)
                endVertex = edge.v
            # v-u
            elif edge.u not in vs:
                vs.add(edge.u)
                endVertex = edge.u
            else: 
                continue

            mst.add(edge)
            for nextEdge in self.edges:
                # v-w
                if nextEdge.u == endVertex and nextEdge.v not in vs:
                    queue.add(nextEdge)
                # u-w
                if nextEdge.v == endVertex and nextEdge.u not in vs:
                    queue.add(nextEdge)

        return mst