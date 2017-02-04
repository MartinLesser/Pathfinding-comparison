from Vertex import Vertex

class DijkstraVertex(Vertex):
    def __init__(self):
        self.predecessor = None
        self.distance = None