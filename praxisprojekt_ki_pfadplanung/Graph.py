from DijkstraVertex import DijkstraVertex
from Edge import Edge
import math
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.infinity = 99999
        self.dijkstraVertices = {}

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def addDirectedEdge(self, vertex1, vertex2, weight = 1):
        assert(vertex1 in self.vertices and vertex2 in self.vertices), "Vertices don't exist in the graph!"
        newEdge = Edge(vertex1, vertex2, weight)
        self.edges.append(newEdge)
        vertex1.addEdge(newEdge)

    def addUndirectedEdge(self, vertex1, vertex2, weight=1):
        assert (vertex1 in self.vertices and vertex2 in self.vertices), "Vertices don't exist in the graph!"
        newEdge1 = Edge(vertex1, vertex2, weight)
        newEdge2 = Edge(vertex2, vertex1, weight)
        self.edges.append(newEdge1)
        self.edges.append(newEdge2)
        vertex1.addEdge(newEdge1)
        vertex2.addEdge(newEdge2)
    
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

    def drawGraph(self):
        G = nx.Graph()
        for index, vertex in enumerate(self.vertices):
            G.add_node(vertex.key, pos=(vertex.positionX, vertex.positionY))
        for index, edge in enumerate(self.edges):
            G.add_edge(edge.tuple[0].key,edge.tuple[1].key, weight=edge.weight)
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw(G, pos, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.savefig('simple_graph')
        plt.show()


    def printDijkstraGraph(self):
        print 'Vertices:'
        for index,vertex in enumerate(self.vertices):
            print str(vertex.key) + ' : Distance = ' + str(self.dijkstraVertices[vertex].distance) \
                  + ' Predecessor = ' + str( 'None' if (self.dijkstraVertices[vertex].predecessor == None)
                                                               else self.dijkstraVertices[vertex].predecessor.key)

    def getEstimation(self, vertex, goalVertex):
        return math.sqrt(abs(vertex.positionX-goalVertex.positionX)**2 + abs(vertex.positionY-goalVertex.positionY)**2)

    def getVertexWithSmallestDistance(self, list):
        min = self.infinity
        smallestVertex = None
        for index, vertex in enumerate(list):
            if self.dijkstraVertices[vertex].distance < min:
                min = self.dijkstraVertices[vertex].distance
                smallestVertex = vertex
        return smallestVertex

    def getSmallestASternVertex(self, list, goalVertex):
        min = self.infinity
        smallestVertex = None
        for index, vertex in enumerate(list):
            if self.dijkstraVertices[vertex].distance + self.getEstimation(vertex, goalVertex) < min:
                min = self.dijkstraVertices[vertex].distance
                smallestVertex = vertex
        return smallestVertex

    def getDistance(self, vertex1, vertex2):
        for index,edge in enumerate(vertex1.edges):
            if edge.tuple[1] == vertex2:
                return edge.weight
        print "Edge could not be found!"

    def findAllPathsDijkstra(self, startVertex):
        assert (len(self.vertices) > 0),"Graph is empty!"
        # create for every vertex a dijkstraVertex and add it to a list
        for index,vertex in enumerate(self.vertices):
            newDijkstraVertex = DijkstraVertex()
            # initialize start node with distance 0 everything else with infinity
            if vertex.key == startVertex.key:
                newDijkstraVertex.distance = 0
            else:
                newDijkstraVertex.distance = self.infinity
            self.dijkstraVertices[vertex] = newDijkstraVertex

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
                if child in unvisitedNodes and \
                                        self.dijkstraVertices[vertex].distance + self.getDistance(vertex, child) \
                                                                                < self.dijkstraVertices[child].distance:
                    self.dijkstraVertices[child].distance = self.dijkstraVertices[vertex].distance + self.getDistance(vertex, child)
                    self.dijkstraVertices[child].predecessor = vertex

    def getPathDijkstra(self, startVertex, goalVertex):
        assert (len(self.vertices) > 0),"Graph is empty!"
        assert (startVertex in self.vertices), "startVertex is not in Vertices!"
        assert (goalVertex in self.vertices), "GoalVertex is not in Vertices!"
        self.findAllPathsDijkstra(startVertex)
        path=[]
        path.append(goalVertex.key)
        predecessor = self.dijkstraVertices[goalVertex].predecessor
        while predecessor != None:
            path.append(predecessor.key)
            predecessor = self.dijkstraVertices[predecessor].predecessor
        path.reverse()
        return path
# TODO: all algorithms use the same dictionary!
    def findPathDijkstra(self, startVertex, goalVertex):
        assert (len(self.vertices) > 0),"Graph is empty!"
        assert (startVertex in self.vertices), "startVertex is not in Vertices!"
        assert (goalVertex in self.vertices), "GoalVertex is not in Vertices!"
        # create for every vertex a dijkstraVertex and add it to a list
        for index,vertex in enumerate(self.vertices):
            newDijkstraVertex = DijkstraVertex()
            # initialize start node with distance 0 everything else with infinity
            if vertex.key == startVertex.key:
                newDijkstraVertex.distance = 0
            else:
                newDijkstraVertex.distance = self.infinity
            self.dijkstraVertices[vertex] = newDijkstraVertex

        unvisitedNodes = [startVertex]
        visitedNodes = []
        while(len(unvisitedNodes) > 0):
            vertex = self.getVertexWithSmallestDistance(unvisitedNodes)
            if vertex == goalVertex: break
            unvisitedNodes.remove(vertex)
            visitedNodes.append(vertex)
            # iterate through all neighbours and check the new distance
            for index,child in enumerate(vertex.children):
                # add unvisited neighbours to the list of unvisited nodes
                if not child in visitedNodes and not child in unvisitedNodes:
                    unvisitedNodes.append(child)
                if child in unvisitedNodes and \
                                        self.dijkstraVertices[vertex].distance + self.getDistance(vertex, child) \
                                                                                < self.dijkstraVertices[child].distance:
                    self.dijkstraVertices[child].distance = self.dijkstraVertices[vertex].distance + self.getDistance(vertex, child)
                    self.dijkstraVertices[child].predecessor = vertex
        path = []
        path.append(goalVertex.key)
        predecessor = self.dijkstraVertices[goalVertex].predecessor
        while predecessor != None:
            path.append(predecessor.key)
            predecessor = self.dijkstraVertices[predecessor].predecessor
        path.reverse()
        return path

    def findPathAStar(self, startVertex, goalVertex):
        assert (len(self.vertices) > 0),"Graph is empty!"
        assert (startVertex in self.vertices), "startVertex is not in Vertices!"
        assert (goalVertex in self.vertices), "GoalVertex is not in Vertices!"
        # create for every vertex a dijkstraVertex and add it to a list
        for index, vertex in enumerate(self.vertices):
            newDijkstraVertex = DijkstraVertex()
            # initialize start node with distance 0 everything else with infinity
            if vertex.key == startVertex.key:
                newDijkstraVertex.distance = 0
            else:
                newDijkstraVertex.distance = self.infinity
            self.dijkstraVertices[vertex] = newDijkstraVertex

        vertexQueue = [startVertex]
        while(not(vertexQueue[0] == goalVertex and len(vertexQueue) == 1)):
            vertex = self.getSmallestASternVertex(vertexQueue, goalVertex)
            vertexQueue.remove(vertex)
            # iterate through all neighbours and check the new distance
            for index,child in enumerate(vertex.children):
                # add unvisited neighbours to the list of unvisited nodes
                if self.dijkstraVertices[vertex].distance + self.getDistance(vertex, child) < self.dijkstraVertices[child].distance:
                    self.dijkstraVertices[child].distance = self.dijkstraVertices[vertex].distance + self.getDistance(vertex, child)
                    self.dijkstraVertices[child].predecessor = vertex
                    vertexQueue.append(child)
        path = []
        path.append(goalVertex.key)
        predecessor = self.dijkstraVertices[goalVertex].predecessor
        while predecessor != None:
            path.append(predecessor.key)
            predecessor = self.dijkstraVertices[predecessor].predecessor
        path.reverse()
        return path

    ## ToDO: Zeitmessen + Zufaellige Graphen erzeugen mit zufaelliger Groesse