import copy
#x = copy.copy(y)        # make a shallow copy of y
#x = copy.deepcopy(y)    # make a deep copy of y

class Vertex:
    def __init__(self, key, positionX = 0, positionY = 0, value = None, origVertex = None):
        if (origVertex == None):
            self.key = key
            self.value = value
            self.children = []
            self.predecessor = None
            self.distance = None
            self.positionX = positionX
            self.positionY = positionY
        else:
            # copy constructor
            self.key = origVertex.key
            self.value = origVertex.value
            self.children = copy.deepcopy(origVertex.children)
            self.predecessor = origVertex.predecessor
            self.distance = origVertex.distance
            self.positionX = origVertex.positionX
            self.positionY = origVertex.positionY

        # custom code for subclass to override
        self.load()

    def load(self):
        pass

    def addChild(self, child):
        self.children.append(child)