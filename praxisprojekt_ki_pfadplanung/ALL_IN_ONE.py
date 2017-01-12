import random
random.seed(5)

width, height = 8, 8 
Matrix = [['#' for x in range(width)] for y in range(height)] 
wormholeLength = 10
numberOfWormholes = 3
worm_x = 0
worm_y = 0
wall_symbol = '#'
empty_symbol = '.'
startNode_x = 0
startNode_y = 0
startNode_id = startNode_y * width + startNode_x
infinity = 99999

def checkDirections():
    possibleDirections = []
    # north
    if worm_y-1 >= 0:
        possibleDirections += [0]
    # east
    if worm_x+1 < width:
        possibleDirections += [1]
    # south
    if worm_y+1 < height:
        possibleDirections += [2]
    # west
    if worm_x-1 >= 0:
        possibleDirections += [3]
    assert (len(possibleDirections) > 1),"No direction is passable!"
    return possibleDirections    
    

def createWormhole():
    global worm_x, worm_y
    rnd = random.randint(0,3)
    if rnd == 0:
        worm_x = 0
        worm_y = 0
    if rnd == 1:
        worm_x = width-1
        worm_y = 0
    if rnd == 2:
        worm_x = 0
        worm_y = height-1
    if rnd == 3:
        worm_x = width-1
        worm_y = height-1
    x = worm_x
    y = worm_y
    Matrix[x][y] = empty_symbol
    for i in range(wormholeLength): 
        possibleDirections = checkDirections()
        possibleDirectionsTemp = possibleDirections[:]
        directionFound = False
        while(not directionFound):
            # if possibleDirectionsTemp is empty
            if len(possibleDirectionsTemp) == 0:
                rnd = random.randint(0,len(possibleDirections)-1)
                direction = possibleDirections[rnd]
                directionFound = True
            else:
                if len(possibleDirectionsTemp) > 1:
                    rnd = random.randint(0,len(possibleDirectionsTemp)-1)
                else:
                    rnd = 0
                direction = possibleDirectionsTemp[rnd]
            # north
            if direction == 0:
                y = worm_y  - 1
                x = worm_x
            # east
            if direction == 1:
                y = worm_y 
                x = worm_x + 1
            # south
            if direction == 2:
                y = worm_y  + 1
                x = worm_x
            # west
            if direction == 3:
                y = worm_y
                x = worm_x - 1
            
            if Matrix[x][y] == empty_symbol and directionFound == False:
                possibleDirectionsTemp.remove(direction)
            else:
                directionFound = True
                
        Matrix[x][y] = empty_symbol
        worm_y = y
        worm_x = x                                    
                
def printMatrix():
    for x in range(width): 
        print("")
        for y in range(height):
            print Matrix[y][x],
    print
            
def makeLabyrinth():
    for i in range(numberOfWormholes): 
        createWormhole()

def createGraph():
    graph = {}
    id = 0
    for y in range(width): 
        for x in range(height):
            if Matrix[x][y] == empty_symbol:
                list = []
                # north
                if y-1 >= 0 and Matrix[x][y-1] == empty_symbol:
                    list.append(id-width)
                # east
                if x+1 < width and Matrix[x+1][y] == empty_symbol:
                    list.append(id+1)
                # south
                if y+1 < height and Matrix[x][y+1] == empty_symbol:
                    list.append(id+width)
                # west
                if x-1 >= 0 and Matrix[x-1][y] == empty_symbol:
                    list.append(id-1)
                
                graph[id] = list
            id += 1
    #print
    #print graph
    return graph

def Dijkstra():
    graph = createGraph()
    # extend each item in graph and add previous node and distance
    for key, value in graph.items():
        node = {}
        node['prev'] = None
        # initialize start node with distance 0 everything else with infinity
        if key == 0:
            node['dist'] = 0
        else:
            node['dist'] = infinity
        value.append(node)
    
    for key, value in graph.items():
        print key, value
    
    unvisitedNodes = [startNode_id]
    visitedNodes = []
    while(len(unvisitedNodes) > 0):
        unvisitedNodes.sort()
        nodeID = unvisitedNodes[0]
        unvisitedNodes.remove(nodeID)
        visitedNodes.append(nodeID)
        # iterate through all neighbours and check the new distance
        for i, val in enumerate(graph[nodeID]):
            if isinstance(val, int):
                distance = graph[nodeID][len(graph[nodeID])-1]['dist']
                neighbourID = val
                # add unvisited neighbours to the list of unvisited nodes
                if not neighbourID in visitedNodes and not neighbourID in unvisitedNodes:
                    unvisitedNodes.append(neighbourID)
                if neighbourID in unvisitedNodes and distance + 1 < graph[neighbourID][len(graph[neighbourID])-1]['dist']: 
                    graph[neighbourID][len(graph[neighbourID])-1]['dist'] = distance + 1 # constant distance between adjacent fields
                    graph[neighbourID][len(graph[neighbourID])-1]['prev'] = nodeID 
    print "#####################################################"
    for key, value in graph.items():
        print key, value
                    
    
makeLabyrinth()
printMatrix()
Dijkstra()
