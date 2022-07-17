class DisjointSet:
    ''' Utility class implementing the disjoint-set data structure. 
        Adapted from GTx CS1332 Java DisjointSet Class '''
    def __init__(self):
        self.parent = self
        self.rank = 0

    def find(self):
        ''' Finds and returns the root element of this disjoint set. '''
        if self.parent is not self:
            self.parent = self.parent.find()

        return self.parent

    def union(self, other):
        ''' Merges this disjoint set with another disjoint set. '''
        xRoot = self.find()
        yRoot = other.find()

        if xRoot == yRoot:
            return
        
        if xRoot.rank < yRoot.rank:
            xRoot.parent = yRoot
        elif xRoot.rank > yRoot.rank:
            yRoot.parent = xRoot
        else:
            yRoot.parent = xRoot
            xRoot.rank += 1