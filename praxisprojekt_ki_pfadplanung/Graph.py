from constants import CONST_WIDTH
from constants import CONST_HEIGHT
from constants import CONST_EMPTY_SYMBOL
from Vertex import Vertex
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
            
    def findAllPathsDijkstra(self):
        assert (len(self.graph) > 0),"Graph is empty!"
        # extend each item in graph and add previous node and distance
        for key, value in self.graph.items():
            node = {}
            node['prev'] = None
            # initialize start node with distance 0 everything else with infinity
            if key == 0:
                node['dist'] = 0
            else:
                node['dist'] = self.infinity
            value.append(node)
            
        unvisitedNodes = [self.startNode_key]
        visitedNodes = []
        while(len(unvisitedNodes) > 0):
            unvisitedNodes.sort()
            nodeID = unvisitedNodes[0]
            unvisitedNodes.remove(nodeID)
            visitedNodes.append(nodeID)
            # iterate through all neighbours and check the new distance
            for i, val in enumerate(self.graph[nodeID]):
                if isinstance(val, int):
                    distance = self.graph[nodeID][len(self.graph[nodeID])-1]['dist']
                    neighbourID = val
                    # add unvisited neighbours to the list of unvisited nodes
                    if not neighbourID in visitedNodes and not neighbourID in unvisitedNodes:
                        unvisitedNodes.append(neighbourID)
                    if neighbourID in unvisitedNodes and distance + 1 < self.graph[neighbourID][len(self.graph[neighbourID])-1]['dist']: 
                        self.graph[neighbourID][len(self.graph[neighbourID])-1]['dist'] = distance + 1 # constant distance between adjacent fields
                        self.graph[neighbourID][len(self.graph[neighbourID])-1]['prev'] = nodeID 

    def findPathDijkstra(self, goal_x, goal_y):
        assert (len(self.graph) > 0),"Graph is empty!"
        self.findAllPathsDijkstra()
        assert(goal_x < CONST_WIDTH and goal_y < CONST_HEIGHT), "Goal is beyond the labyrinth"
        path=[]
        # id of the goal node
        goalID = goal_y * CONST_WIDTH + goal_x
        #
        assert(goalID in self.graph), "Goal can not be reached from start-point!"
        path.append(goalID)
        previousNodeID = self.graph[goalID][len(self.graph[goalID])-1]['prev']
        while previousNodeID != None:           
            path.append(previousNodeID)
            previousNodeID = self.graph[previousNodeID][len(self.graph[previousNodeID])-1]['prev']
        path.reverse()
        return path