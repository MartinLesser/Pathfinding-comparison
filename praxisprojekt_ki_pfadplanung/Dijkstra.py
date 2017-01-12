import Graph

startNode_x = 0
startNode_y = 0
startNode_id = startNode_y * width + startNode_x
infinity = 99999

def Dijkstra():
    graph = Graph.createGraph()
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