
class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.infinity = 99999

    def createCustomGraph(self):
        None
    
    def printGraph(self):
        print 'Vertices:'
        for i,val in enumerate(self.vertices):
            print str(val.key) + ' : ',
            children = val.children
            for i, val in enumerate(children):
                print str(val.key),
            print
        print 'Edges:'
        for i,val in enumerate(self.edges):
            print 'Edge = (' + str(val.tuple[0].key) + ', ' + str(val.tuple[1].key) + ')' + ' : weight(' + str(val.weight) + ')'

    def printDijkstraGraph(self):
        print 'Vertices:'
        for index,vertex in enumerate(self.vertices):
            print str(vertex.key) + ' : Distance = ' + str(vertex.distance) \
                  + ' Predecessor = ' + str( 'None' if (vertex.predecessor == None) else vertex.predecessor.key)

    def getVertexWithSmallestDistance(self, list):
        min = self.infinity
        smallestVertex = None
        for index, vertex in enumerate(list):
            if vertex.distance < min:
                min = vertex.distance
                smallestVertex = vertex
        return smallestVertex

    def getDistance(self, vertex1, vertex2):
        for index,edge in enumerate(self.edges):
            if edge.tuple[0] == vertex1 and edge.tuple[1] == vertex2:
                return edge.weight
        return False

    def findAllPathsDijkstra(self):
        assert (len(self.vertices) > 0),"Graph is empty!"
        for index,vertex in enumerate(self.vertices):
            # initialize start node with distance 0 everything else with infinity
            if vertex.key == self.startNode_key:
                vertex.distance = 0
            else:
                vertex.distance = self.infinity

        unvisitedNodes = [self.startNode]
        visitedNodes = []
        while(len(unvisitedNodes) > 0):
            vertex = self.getVertexWithSmallestDistance(unvisitedNodes)
            unvisitedNodes.remove(vertex)
            visitedNodes.append(vertex)
            # iterate through all neighbours and check the new distance
            for index,child in enumerate(vertex.children):
                # add unvisited neighbours to the list of unvisited nodes
                if not child in visitedNodes and not child in unvisitedNodes:
                    unvisitedNodes.append(child)
                if child in unvisitedNodes and vertex.distance + self.getDistance(vertex, child) < child.distance:
                    child.distance = vertex.distance + self.getDistance(vertex, child)
                    child.predecessor = vertex

    def findPathDijkstra(self, goalNode):
        assert (len(self.vertices) > 0),"Graph is empty!"
        self.findAllPathsDijkstra()
        assert(goalNode in ), "Goal is beyond the labyrinth!"
        path=[]
        for index,vertex in enumerate(self.vertices):
            if vertex.key == goalID:
                goalNode = vertex
                break
        assert(goalNode in self.vertices), "Goal can not be reached from start-point!"
        path.append(goalID)
        predecessor = goalNode.predecessor
        while predecessor != None:
            path.append(predecessor.key)
            predecessor = predecessor.predecessor
        path.reverse()
        return path