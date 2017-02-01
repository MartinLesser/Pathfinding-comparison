
class Node:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.children = []
        self.predecessor = None # only necessary for dijkstra
        self.distance = None # only necessary for dijkstra

    def addChild(self, node, edgeWeight):
        edge = {node.key : edgeWeight}
        self.children.append(edge)