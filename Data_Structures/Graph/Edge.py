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

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        if self.directed ^ other.directed:
            return False

        if self.directed:
            return self.weight == other.weight and self.u == other.u and self.v == other.v
        
        return self.weight == other.weight and (self.u == other.u and self.v == other.v) or (self.u == other.v and self.v == other.u)

    def __hash__(self):
        return (0 if self.u is None else hash(self.u) \
            ^ 0 if self.v is None else hash(self.v) \
                ^ self.weight \
                    ^ 1 if self.directed else 0)
        