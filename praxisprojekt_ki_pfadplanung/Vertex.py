import copy
#x = copy.copy(y)        # make a shallow copy of y
#x = copy.deepcopy(y)    # make a deep copy of y

class Vertex:
    def __init__(self, key, value = None, origVertex = None):
        if (origVertex == None):
            self.key = key
            self.value = value
            self.children = []
            self.predecessor = None
            self.distance = None
        else:
            # copy constructor
            self.key = origVertex.key
            self.value = origVertex.value
            self.children = copy.deepcopy(origVertex.children)
        # custom code for subclass to override
        self.load()

    def load(self):
        pass

    def addChild(self, child):
        self.children.append(child)