from Vertex import Vertex

class VertexDijkstra(Vertex):
    def load(self):
        self.predecessor = None
        self.distance = None