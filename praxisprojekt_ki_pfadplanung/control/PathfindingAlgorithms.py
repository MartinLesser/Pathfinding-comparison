from praxisprojekt_ki_pfadplanung.model.DijkstraVertex import DijkstraVertex
import math

class PathfindingAlgorithms:
    def __init__(self):
        pass

    def getEstimation(self, vertex, goalVertex):
        return math.sqrt(
            abs(vertex.positionX - goalVertex.positionX) ** 2 + abs(vertex.positionY - goalVertex.positionY) ** 2)

    def getVertexWithSmallestDistance(self, graph, list):
        min = float('inf')
        smallestVertex = None
        for index, vertex in enumerate(list):
            if graph.dijkstraVertices[vertex].distance < min:
                min = graph.dijkstraVertices[vertex].distance
                smallestVertex = vertex
        assert(smallestVertex!=None), "Smallest Vertex could not be found!"
        return smallestVertex

    def getSmallestAStarVertex(self, graph, list, goalVertex):
        min = float('inf')
        smallestVertex = None
        for index, vertex in enumerate(list):
            if graph.dijkstraVertices[vertex].distance + self.getEstimation(vertex, goalVertex) < min:
                min = graph.dijkstraVertices[vertex].distance
                smallestVertex = vertex
        assert (smallestVertex != None), "Smallest Vertex could not be found!"
        return smallestVertex

    def initializeDijkstraVertices(self, graph, startVertex):
        # create for every vertex a dijkstraVertex and add it to a list
        for index, vertex in enumerate(graph.vertices):
            newDijkstraVertex = DijkstraVertex()
            # initialize all vertices with infinity
            newDijkstraVertex.distance = float('inf')
            graph.dijkstraVertices[vertex] = newDijkstraVertex
        # initialize start-vertex with zero distance
        graph.dijkstraVertices[startVertex].distance = 0

    def getPath(self, graph, goalVertex):
        path = []
        path.append(goalVertex.key)
        predecessor = graph.dijkstraVertices[goalVertex].predecessor
        while predecessor != None:
            path.append(predecessor.key)
            predecessor = graph.dijkstraVertices[predecessor].predecessor
        path.reverse()
        return path

    def findAllPathsDijkstra(self, graph, startVertex):
        assert (len(graph.vertices) > 0), "Graph is empty!"
        self.initializeDijkstraVertices(graph, startVertex)

        unvisitedNodes = [startVertex]
        visitedNodes = []
        while (len(unvisitedNodes) > 0):
            vertex = self.getVertexWithSmallestDistance(graph, unvisitedNodes)
            unvisitedNodes.remove(vertex)
            visitedNodes.append(vertex)
            # iterate through all neighbours and check the new distance
            for index, child in enumerate(vertex.children):
                # add unvisited neighbours to the list of unvisited nodes
                if not child in visitedNodes and not child in unvisitedNodes:
                    unvisitedNodes.append(child)
                if child in unvisitedNodes and \
                                        graph.dijkstraVertices[vertex].distance + vertex.getEdge(child) \
                                < graph.dijkstraVertices[child].distance:
                    graph.dijkstraVertices[child].distance = graph.dijkstraVertices[vertex].distance + vertex.getEdge(child)
                    graph.dijkstraVertices[child].predecessor = vertex

    def getPathDijkstra(self, graph, startVertex, goalVertex):
        assert (len(graph.vertices) > 0), "Graph is empty!"
        assert (startVertex in graph.vertices), "startVertex is not in Vertices!"
        assert (goalVertex in graph.vertices), "GoalVertex is not in Vertices!"

        self.findAllPathsDijkstra(graph, startVertex)

        return self.getPath(graph, goalVertex)

    def findPathDijkstra(self, graph, startVertex, goalVertex):
        assert (len(graph.vertices) > 0), "Graph is empty!"
        assert (startVertex in graph.vertices), "startVertex is not in Vertices!"
        assert (goalVertex in graph.vertices), "GoalVertex is not in Vertices!"
        self.initializeDijkstraVertices(graph, startVertex)

        unvisitedNodes = [startVertex]
        visitedNodes = []
        while (len(unvisitedNodes) > 0):
            vertex = self.getVertexWithSmallestDistance(graph, unvisitedNodes)
            if vertex == goalVertex: break
            unvisitedNodes.remove(vertex)
            visitedNodes.append(vertex)
            # iterate through all neighbours and check the new distance
            for index, child in enumerate(vertex.children):
                # add unvisited neighbours to the list of unvisited nodes
                if not child in visitedNodes and not child in unvisitedNodes:
                    unvisitedNodes.append(child)
                if child in unvisitedNodes and \
                                        graph.dijkstraVertices[vertex].distance + vertex.getEdge(child) \
                                < graph.dijkstraVertices[child].distance:
                    graph.dijkstraVertices[child].distance = graph.dijkstraVertices[vertex].distance + vertex.getEdge(child)
                    graph.dijkstraVertices[child].predecessor = vertex
        return self.getPath(graph, goalVertex)

    def findPathAStar(self, graph, startVertex, goalVertex):
        assert (len(graph.vertices) > 0), "Graph is empty!"
        assert (startVertex in graph.vertices), "startVertex is not in Vertices!"
        assert (goalVertex in graph.vertices), "GoalVertex is not in Vertices!"

        self.initializeDijkstraVertices(graph, startVertex)

        vertexQueue = [startVertex]
        while (not (vertexQueue[0] == goalVertex and len(vertexQueue) == 1)):
            vertex = self.getSmallestAStarVertex(graph, vertexQueue, goalVertex)
            vertexQueue.remove(vertex)
            # iterate through all neighbours and check the new distance
            for index, child in enumerate(vertex.children):
                # add unvisited neighbours to the list of unvisited nodes
                if graph.dijkstraVertices[vertex].distance + vertex.getEdge(child) < graph.dijkstraVertices[
                    child].distance:
                    graph.dijkstraVertices[child].distance = graph.dijkstraVertices[vertex].distance + vertex.getEdge(child)
                    graph.dijkstraVertices[child].predecessor = vertex
                    vertexQueue.append(child)
        return self.getPath(graph, goalVertex)

# ToDO: Zeitmessen + Zufaellige Graphen erzeugen mit zufaelliger Groesse