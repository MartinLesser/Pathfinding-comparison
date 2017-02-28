from praxisprojekt_ki_pfadplanung.model.graph import Graph
from praxisprojekt_ki_pfadplanung.model.vertex import Vertex
from praxisprojekt_ki_pfadplanung.model.labyrinth import Labyrinth
from praxisprojekt_ki_pfadplanung.model.priority_queue import PriorityQueue, Priority
from praxisprojekt_ki_pfadplanung.view.output import Output
from praxisprojekt_ki_pfadplanung.control.dijkstra import Dijkstra
from praxisprojekt_ki_pfadplanung.control.a_star import AStar
from praxisprojekt_ki_pfadplanung.control.d_star_lite import DStarLite
import time

def main():
    #test_a_star()
    test_d_star()

def test_a_star():
    f = open('a_star_performance', 'w')
    output = Output()
    seed = 9
    for i in range(10):
        passable_graph_found = False
        while passable_graph_found == False:
            graph = Graph()
            #print seed
            labyrinth = Labyrinth(seed)
            labyrinth.makeLabyrinth()
            graph.create_graph_from_labyrinth(labyrinth)


            start_vertex = graph.get_vertex(graph.vertices[0].key)
            #print start_vertex.key
            goal_vertex = graph.get_vertex(graph.vertices[len(graph.vertices) - 1].key)
            #print goal_vertex.key

            a_star = AStar(graph, start_vertex, goal_vertex)
            if len(a_star.find_path_a_star()) > 1:
                #print a_star.get_path()
                #output.draw_graph(graph)
                passable_graph_found = True
                start_time = time.time()
                if a_star.walk_path() == False:
                    passable_graph_found = False
                else:
                    f.write("%u\t %s s\n" % (i, time.time() - start_time))
            seed += 1
    f.close()

def test_d_star():
    f = open('d_star_lite_performance', 'w')
    output = Output()
    seed = 9
    for i in range(10):
        passable_graph_found = False
        while passable_graph_found == False:
            graph = Graph()

            labyrinth = Labyrinth(seed)
            labyrinth.makeLabyrinth()
            graph.create_graph_from_labyrinth(labyrinth)
            # output.draw_graph(graph)

            start_vertex = graph.get_vertex(graph.vertices[0].key)
            goal_vertex = graph.get_vertex(graph.vertices[len(graph.vertices) - 1].key)

            dl = DStarLite(graph, start_vertex, goal_vertex)
            dl.initialize()
            dl.compute_shortest_path()
            if len(dl.get_path()) > 1:
                dl.rhs = {}
                dl.distance = {}
                # print dl.get_path()
                # output.draw_graph(graph)
                passable_graph_found = True
                start_time = time.time()
                if dl.find_path_d_star_lite() == False:
                    passable_graph_found = False
                else:
                    f.write("%u\t %s s\n" % (i, time.time() - start_time))
            seed += 1
    f.close()

if __name__ == "__main__": main()

