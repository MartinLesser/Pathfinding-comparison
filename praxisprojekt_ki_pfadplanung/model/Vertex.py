
class Vertex:
    def __init__(self, key, positionX = 0, positionY = 0, value = None):
        self.key = key
        self.value = value
        self.edges = []
        self.positionX = positionX
        self.positionY = positionY

    def addEdge(self, edge):
        self.edges.append(edge)

    def getEdge(self, vertex2):
        for index,edge in enumerate(self.edges):
            if edge.destination == vertex2:
                return edge.weight
        print "Edge could not be found!"

    @property
    def children(self):
        return [edge.destination for edge in self.edges]