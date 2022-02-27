class Edge:
    ''' Adapted from GTx CS1332 Java Edge Class '''
    def __init__(self, u, v, weight, directed):
        self.u = u
        self.v = v
        self.weight = weight
        self.directed = directed

    def __str__(self):
        if self.directed:
            return "Edge from " + self.u + " to " + self.v + " with weight " + str(self.weight)
        else:
            return "Edge between " + self.u + " and " + self.v + " with weight " + str(self.weight)

    def __repr__(self):
        if self.directed:
            return f"[{str(self.u)}->{str(self.v)}, {str(self.weight)}]"
        else:
            return f"[{str(self.u)}-{str(self.v)}, {str(self.weight)}]"