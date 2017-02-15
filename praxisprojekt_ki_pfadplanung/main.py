from praxisprojekt_ki_pfadplanung.model.Graph import Graph
from praxisprojekt_ki_pfadplanung.model.Vertex import Vertex
from praxisprojekt_ki_pfadplanung.view.Output import Output
from praxisprojekt_ki_pfadplanung.control.PathfindingAlgorithms import PathfindingAlgorithms

def main():
    graph = Graph()
    output = Output()
    pf = PathfindingAlgorithms()
    vertex1 = Vertex(1, 25, 100)
    graph.addVertex(vertex1)
    vertex2 = Vertex(2, 75, 100)
    graph.addVertex(vertex2)
    vertex3 = Vertex(3, 100, 90)
    graph.addVertex(vertex3)
    vertex4 = Vertex(4, 100, 40)
    graph.addVertex(vertex4)
    vertex5 = Vertex(5, 75, 25)
    graph.addVertex(vertex5)
    vertex6 = Vertex(6, 25, 25)
    graph.addVertex(vertex6)
    vertex7 = Vertex(7, 10, 50)
    graph.addVertex(vertex7)

    graph.addUndirectedEdge(vertex1, vertex7, 4)
    graph.addUndirectedEdge(vertex7, vertex6, 2)
    graph.addUndirectedEdge(vertex1, vertex5, 10)
    graph.addUndirectedEdge(vertex6, vertex5, 3)
    graph.addUndirectedEdge(vertex5, vertex4, 9)
    graph.addUndirectedEdge(vertex5, vertex3, 7)
    graph.addUndirectedEdge(vertex2, vertex3, 2)

    #output.printGraph(graph)
    #pf.findAllPathsDijkstra(graph, vertex1)
    #output.printDijkstraGraph(graph)
    #print pf.getPathDijkstra(graph, vertex1, vertex2)
    #print pf.findPathDijkstra(graph, vertex1, vertex2)
    print pf.findPathAStar(graph, vertex1, vertex2)
    output.drawGraph(graph)

if __name__ == "__main__": main()

