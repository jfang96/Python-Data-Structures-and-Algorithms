class VertexDistancePair:
    ''' Adapted from GTx CS1332 Java VertexDistancePair Class '''

    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance

    def __str__(self):
        return "Pair with vertex " + str(self.vertex) + " and distance " + str(self.distance)

    def __repr__(self):
        return f"[{str(self.vertex)}, {str(self.distance)}]"

    def __lt__(self, other):
        return self.distance < other.distance
        
    def __eq__(self, other):
        return self.distance == other.distance