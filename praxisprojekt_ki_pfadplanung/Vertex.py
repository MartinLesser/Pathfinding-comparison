
class Vertex:
    def __init__(self, key, positionX = 0, positionY = 0, value = None):
        self.key = key
        self.value = value
        self.edges = []
        self.positionX = positionX
        self.positionY = positionY

    def addEdge(self, edge):
        self.edges.append(edge)

    @property
    def children(self):
        return [edge.tuple[1] for edge in self.edges]