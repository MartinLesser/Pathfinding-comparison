from Vertex import Vertex

class VertexDijkstra(Vertex):
    def __init__(self):
        self.predecessor = None
        self.distance = None