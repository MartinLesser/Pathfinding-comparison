from constants import CONST_WIDTH
from constants import CONST_HEIGHT
from constants import CONST_EMPTY_SYMBOL

class Graph:
    def __init__(self):
        self.graph = {}
        self.searchTree = {}
        self.startNode_x = 0
        self.startNode_y = 0
        self.startNode_id = self.startNode_y * CONST_WIDTH + self.startNode_x
        self.infinity = 99999
        
    def createGraph(self, labyrinth):
        id = 0
        for y in range(CONST_HEIGHT):
            for x in range(CONST_WIDTH):
                if labyrinth.Matrix[y][x] == CONST_EMPTY_SYMBOL:
                    list = []
                    # north
                    if y-1 >= 0 and labyrinth.Matrix[y-1][x] == CONST_EMPTY_SYMBOL:
                        list.append(id-CONST_WIDTH)
                    # east
                    if x+1 < CONST_WIDTH and labyrinth.Matrix[y][x+1] == CONST_EMPTY_SYMBOL:
                        list.append(id+1)
                    # south
                    if y+1 < CONST_HEIGHT and labyrinth.Matrix[y+1][x] == CONST_EMPTY_SYMBOL:
                        list.append(id+CONST_WIDTH)
                    # west
                    if x-1 >= 0 and labyrinth.Matrix[y][x-1] == CONST_EMPTY_SYMBOL:
                        list.append(id-1)

                    self.graph[id] = list
                id += 1
    
    def printGraph(self):
        for key, value in self.graph.items():
            print key, value
            
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
            
        unvisitedNodes = [self.startNode_id]
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