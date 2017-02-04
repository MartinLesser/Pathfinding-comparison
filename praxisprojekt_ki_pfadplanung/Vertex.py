
class Vertex:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.children = []


    def addChild(self, child):
        self.children.append(child)