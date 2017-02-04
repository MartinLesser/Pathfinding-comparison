from Vertex import Vertex

class Edge:
    def __init__(self, vertex1, vertex2, weight):
        # Todo: assert vertex??
        self.tuple = (vertex1, vertex2)
        self.weight = weight