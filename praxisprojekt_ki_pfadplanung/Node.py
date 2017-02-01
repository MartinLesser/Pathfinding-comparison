
class Node:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.edges = {}
        self.predecessor = None # only necessary for dijkstra
        self.distance = None # only necessary for dijkstra

    def addEdge(self, nodeKey, edgeWeight = 1):
        self.edges[nodeKey] = edgeWeight