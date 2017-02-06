from Vertex import Vertex
from Edge import Edge

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.infinity = 99999

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def addEdge(self, vertex1, vertex2, weight = 1):
        assert(vertex1 in self.vertices and vertex2 in self.vertices), "Vertices don't exist in the graph!"
        newEdge = Edge(vertex1, vertex2, weight)
        self.edges.append(newEdge)
        vertex1.children.append(vertex2)
    
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

    def findAllPathsDijkstra(self, startVertex):
        assert (len(self.vertices) > 0),"Graph is empty!"
        for index,vertex in enumerate(self.vertices):
            # initialize start node with distance 0 everything else with infinity
            if vertex.key == startVertex.key:
                vertex.distance = 0
            else:
                vertex.distance = self.infinity

        unvisitedNodes = [startVertex]
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

    def findPathDijkstra(self, startVertex, goalVertex):
        assert (len(self.vertices) > 0),"Graph is empty!"
        assert (startVertex in self.vertices), "startVertex is not in Vertices!"
        assert (goalVertex in self.vertices), "GoalVertex is not in Vertices!"
        self.findAllPathsDijkstra(startVertex)
        path=[]
        path.append(goalVertex.key)
        predecessor = goalVertex.predecessor
        while predecessor != None:
            path.append(predecessor.key)
            predecessor = predecessor.predecessor
        path.reverse()
        return path