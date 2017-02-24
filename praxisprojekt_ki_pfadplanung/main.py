from praxisprojekt_ki_pfadplanung.model.graph import Graph
from praxisprojekt_ki_pfadplanung.model.vertex import Vertex
from praxisprojekt_ki_pfadplanung.view.output import Output
from praxisprojekt_ki_pfadplanung.control.pathfinding_algorithms import PathfindingAlgorithms

def main():
    graph = Graph()
    output = Output()
    pf = PathfindingAlgorithms()
    vertex1 = Vertex(1, 25, 100)
    graph.add_vertex(vertex1)
    vertex2 = Vertex(2, 75, 100)
    graph.add_vertex(vertex2)
    vertex3 = Vertex(3, 100, 90)
    graph.add_vertex(vertex3)
    vertex4 = Vertex(4, 100, 40)
    graph.add_vertex(vertex4)
    vertex5 = Vertex(5, 75, 25)
    graph.add_vertex(vertex5)
    vertex6 = Vertex(6, 25, 25)
    graph.add_vertex(vertex6)
    vertex7 = Vertex(7, 10, 50)
    graph.add_vertex(vertex7)

    graph.add_undirected_edge(vertex1, vertex7, 4)
    graph.add_undirected_edge(vertex7, vertex6, 2)
    graph.add_undirected_edge(vertex1, vertex5, 10)
    graph.add_undirected_edge(vertex6, vertex5, 3)
    graph.add_undirected_edge(vertex5, vertex4, 9)
    graph.add_undirected_edge(vertex5, vertex3, 7)
    graph.add_undirected_edge(vertex2, vertex3, 2)

    #output.print_graph(graph)
    #pf.find_all_paths_dijkstra(graph, vertex1)
    #output.print_dijkstra_graph(graph)
    #print pf.get_path_dijkstra(graph, vertex1, vertex2)
    #print pf.find_path_dijkstra(graph, vertex1, vertex2)
    print pf.find_path_a_star(graph, vertex1, vertex2)
    output.draw_graph(graph)

if __name__ == "__main__": main()

