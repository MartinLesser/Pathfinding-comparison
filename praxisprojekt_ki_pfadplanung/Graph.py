from constants import CONST_WIDTH
from constants import CONST_HEIGHT
from constants import CONST_EMPTY_SYMBOL
from Vertex import Vertex
from VertexDijkstra import VertexDijkstra
from Edge import Edge

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        startNode_x = 0 # for labyrinth
        startNode_y = 0 # for labyrinth
        self.startNode_key = startNode_y * CONST_WIDTH + startNode_x
        self.startNode = None
        self.infinity = 99999

    def createCustomGraph(self):
        None

    def createGraph(self, labyrinth):
        id = 0
        existingVerticesKeys = [] # to know quickly which vertices exist already
        newVertex = None
        for y in range(CONST_HEIGHT):
            for x in range(CONST_WIDTH):
                if labyrinth.Matrix[y][x] == CONST_EMPTY_SYMBOL:
                    if(id not in existingVerticesKeys):
                        existingVerticesKeys.append(id)
                        newVertex = Vertex(id)
                        self.vertices.append(newVertex)
                    else:
                        # search for existing vertex
                        for i in range(len(self.vertices)):
                            if self.vertices[i].key == id:
                                newVertex = self.vertices[i]
                                break
                    assert(newVertex != None), "Vertex exists but could not be found!"

                    # east
                    if x+1 < CONST_WIDTH and labyrinth.Matrix[y][x+1] == CONST_EMPTY_SYMBOL:
                        if (id+1 not in existingVerticesKeys):
                            # create new vertex
                            eastChildVertex = Vertex(id + 1)
                            # add it to the vertices list
                            self.vertices.append(eastChildVertex)
                            existingVerticesKeys.append(id + 1)
                        else:
                            # search for existing vertex
                            for i in range(len(self.vertices)):
                                if self.vertices[i].key == id+1:
                                    eastChildVertex = self.vertices[i]
                                    break
                        # add child to current vertex
                        newVertex.addChild(eastChildVertex)
                        # add child to eastChild
                        eastChildVertex.addChild(newVertex)
                        # create new edges and add it to the edges list
                        self.edges.append(Edge(newVertex, eastChildVertex))
                        self.edges.append(Edge(eastChildVertex, newVertex))

                    # south
                    if y+1 < CONST_HEIGHT and labyrinth.Matrix[y+1][x] == CONST_EMPTY_SYMBOL:
                        # create new vertex
                        southChildVertex = Vertex(id+CONST_WIDTH)
                        # add it to the vertices list
                        self.vertices.append(southChildVertex)
                        existingVerticesKeys.append(id + CONST_WIDTH)
                        # add child to current vertex
                        newVertex.addChild(southChildVertex)
                        # add child to eastChild
                        southChildVertex.addChild(newVertex)
                        # create new edges and add it to the edges list
                        self.edges.append(Edge(newVertex, southChildVertex))
                        self.edges.append(Edge(southChildVertex, newVertex))

                    if(id == self.startNode_key): self.startNode = newVertex
                id += 1
                newVertex = None
        #print sorted(existingVerticesKeys)
    
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

    def findPathDijkstra(self, goal_x, goal_y):
        assert (len(self.vertices) > 0),"Graph is empty!"
        self.findAllPathsDijkstra()
        assert(goal_x < CONST_WIDTH and goal_y < CONST_HEIGHT), "Goal is beyond the labyrinth!"
        path=[]
        # id of the goal node
        goalID = goal_y * CONST_WIDTH + goal_x
        goalNode = None
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