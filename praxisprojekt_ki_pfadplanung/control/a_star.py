import math
from praxisprojekt_ki_pfadplanung.model.dijkstra_vertex import DijkstraVertex

class AStar:
    def __init__(self, graph, start_vertex, goal_vertex):
        self.change_happened = False
        self.dijkstra_vertices = {}
        self.graph = graph
        self.start_vertex = start_vertex
        self.goal_vertex = goal_vertex

    def get_estimation(self, vertex, goal_vertex):
        return math.sqrt(
            abs(vertex.positionX - goal_vertex.positionX) ** 2 + abs(vertex.positionY - goal_vertex.positionY) ** 2)

    def get_smallest_a_star_vertex(self, graph, list, goal_vertex):
        min = float('inf')
        smallest_vertex = None
        for index, vertex in enumerate(list):
            if self.dijkstra_vertices[vertex].distance + self.get_estimation(vertex, goal_vertex) < min:
                min = self.dijkstra_vertices[vertex].distance
                smallest_vertex = vertex
        assert (smallest_vertex != None), "Smallest Vertex could not be found!"
        return smallest_vertex

    def initialize_dijkstra_vertices(self, graph, start_vertex):
        # create for every vertex a dijkstraVertex and add it to a list
        for index, vertex in enumerate(graph.vertices):
            new_dijkstra_vertex = DijkstraVertex()
            # initialize all vertices with infinity
            new_dijkstra_vertex.distance = float('inf')
            self.dijkstra_vertices[vertex] = new_dijkstra_vertex
        # initialize start-vertex with zero distance
        self.dijkstra_vertices[start_vertex].distance = 0

    def find_path_a_star(self):
        assert (len(self.graph.vertices) > 0), "Graph is empty!"
        assert (self.start_vertex in self.graph.vertices), "start_vertex is not in Vertices!"
        assert (self.goal_vertex in self.graph.vertices), "GoalVertex is not in Vertices!"

        self.initialize_dijkstra_vertices(self.graph, self.start_vertex)

        vertex_queue = [self.start_vertex]
        while (len(vertex_queue) > 0):
            vertex = self.get_smallest_a_star_vertex(self.graph, vertex_queue, self.goal_vertex)
            if vertex == self.goal_vertex: break;
            vertex_queue.remove(vertex)
            vertex_distance = self.dijkstra_vertices[vertex].distance
            # iterate through all neighbours and check the new distance
            for index, child in enumerate(vertex.children):
                edge_weight = vertex.get_edge_weight(child)
                if vertex_distance + edge_weight < self.dijkstra_vertices[child].distance:
                    self.dijkstra_vertices[child].distance = vertex_distance + edge_weight
                    self.dijkstra_vertices[child].predecessor = vertex
                    vertex_queue.append(child)   # indirect implementation of the closed-list
        # assert(len(self.get_path()) > 1), "No path could be found!"
        return self.get_path()

    def get_path(self):
        path = []
        path.append(self.goal_vertex.key)
        predecessor = self.dijkstra_vertices[self.goal_vertex].predecessor
        while predecessor != None:
            path.append(predecessor.key)
            predecessor = self.dijkstra_vertices[predecessor].predecessor
        path.reverse()
        return path

    def walk_path(self):
        path = self.find_path_a_star()
        repetition = 0
        step = 0
        moment_of_edge_change = len(path) / 2
        while (self.start_vertex != self.goal_vertex):
            self.start_vertex = self.graph.get_vertex(path[step])
            print self.start_vertex.key,
            # artificial cost change
            if repetition == moment_of_edge_change and len(path) > 2:
                self.make_edge_untraversable(path[len(path)/2 + len(path)/4], path[len(path)/2 + len(path)/4 + 1])

            if self.change_happened == True:
                path = self.find_path_a_star()
                #print path
                if len(path) < 2:
                    return False
                step = 0
                self.change_happened = False
            repetition += 1
            step += 1
        print

    def make_edge_untraversable(self, vertex1_key, vertex2_key):
        self.graph.update_edge_weight(vertex1_key, vertex2_key, float('inf'))
        self.change_happened = True
        print "\n!!! "