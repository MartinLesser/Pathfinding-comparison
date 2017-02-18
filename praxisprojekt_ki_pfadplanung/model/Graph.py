from praxisprojekt_ki_pfadplanung.model.Edge import Edge

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.dijkstraVertices = {}

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def addDirectedEdge(self, vertex1, vertex2, weight = 1):
        assert(vertex1 in self.vertices and vertex2 in self.vertices), "Vertices don't exist in the graph!"
        assert(weight >= 0), "Weight must be positive!"
        newEdge = Edge(vertex1, vertex2, weight)
        self.edges.append(newEdge)
        vertex1.addEdge(newEdge)

    def addUndirectedEdge(self, vertex1, vertex2, weight=1):
        self.addDirectedEdge(vertex1, vertex2, weight)
        self.addDirectedEdge(vertex2, vertex1, weight)
    


