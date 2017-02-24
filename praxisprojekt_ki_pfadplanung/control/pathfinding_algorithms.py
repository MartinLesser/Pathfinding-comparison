"""
This module ...
"""

from praxisprojekt_ki_pfadplanung.model.dijkstra_vertex import DijkstraVertex
import math

class PathfindingAlgorithms:
    def __init__(self):
        pass

    def get_estimation(self, vertex, goal_vertex):
        return math.sqrt(
            abs(vertex.positionX - goal_vertex.positionX) ** 2 + abs(vertex.positionY - goal_vertex.positionY) ** 2)

    def get_vertex_with_smallest_distance(self, graph, list):
        min = float('inf')
        smallest_vertex = None
        for index, vertex in enumerate(list):
            if graph.dijkstra_vertices[vertex].distance < min:
                min = graph.dijkstra_vertices[vertex].distance
                smallest_vertex = vertex
        assert(smallest_vertex != None), "Smallest Vertex could not be found!"
        return smallest_vertex

    def get_smallest_a_star_vertex(self, graph, list, goal_vertex):
        min = float('inf')
        smallest_vertex = None
        for index, vertex in enumerate(list):
            if graph.dijkstra_vertices[vertex].distance + self.get_estimation(vertex, goal_vertex) < min:
                min = graph.dijkstra_vertices[vertex].distance
                smallest_vertex = vertex
        assert (smallest_vertex != None), "Smallest Vertex could not be found!"
        return smallest_vertex

    def initialize_dijkstra_vertices(self, graph, start_vertex):
        # create for every vertex a dijkstraVertex and add it to a list
        for index, vertex in enumerate(graph.vertices):
            new_dijkstra_vertex = DijkstraVertex()
            # initialize all vertices with infinity
            new_dijkstra_vertex.distance = float('inf')
            graph.dijkstra_vertices[vertex] = new_dijkstra_vertex
        # initialize start-vertex with zero distance
        graph.dijkstra_vertices[start_vertex].distance = 0

    def get_path(self, graph, goal_vertex):
        path = []
        path.append(goal_vertex.key)
        predecessor = graph.dijkstra_vertices[goal_vertex].predecessor
        while predecessor != None:
            path.append(predecessor.key)
            predecessor = graph.dijkstra_vertices[predecessor].predecessor
        path.reverse()
        return path

    def find_all_paths_dijkstra(self, graph, start_vertex):
        # ToDo: comments
        """
        Returns the index of the leaf that each sample is predicted as.
        .. versionadded:: 0.17
        Parameters
        ----------
        X : array_like or sparse matrix, shape = [n_samples, n_features]
            The input samples. Internally, it will be converted to
            ``dtype=np.float32`` and if a sparse matrix is provided
            to a sparse ``csr_matrix``.
        check_input : boolean, (default=True)
            Allow to bypass several input checking.
            Don't use this parameter unless you know what you do.
        Returns
        -------
        X_leaves : array_like, shape = [n_samples,]
            For each datapoint x in X, return the index of the leaf x
            ends up in. Leaves are numbered within
            ``[0; self.tree_.node_count)``, possibly with gaps in the
            numbering.
        """
        assert (len(graph.vertices) > 0), "Graph is empty!"
        self.initialize_dijkstra_vertices(graph, start_vertex)

        vertex_queue = [start_vertex]
        while (len(vertex_queue) > 0):
            vertex = self.get_vertex_with_smallest_distance(graph, vertex_queue)
            vertex_queue.remove(vertex)
            vertex_distance = graph.dijkstra_vertices[vertex].distance
            # iterate through all neighbours and check the new distance
            for index, child in enumerate(vertex.children):
                if graph.dijkstra_vertices[child].distance == float('inf'):
                    vertex_queue.append(child)
                edge_weight = vertex.get_edge_weight(child)
                if vertex_distance + edge_weight < graph.dijkstra_vertices[child].distance:
                    graph.dijkstra_vertices[child].distance = vertex_distance + edge_weight
                    graph.dijkstra_vertices[child].predecessor = vertex

    def get_path_dijkstra(self, graph, start_vertex, goal_vertex):
        assert (len(graph.vertices) > 0), "Graph is empty!"
        assert (start_vertex in graph.vertices), "start_vertex is not in Vertices!"
        assert (goal_vertex in graph.vertices), "GoalVertex is not in Vertices!"
        self.find_all_paths_dijkstra(graph, start_vertex)
        return self.get_path(graph, goal_vertex)

    def find_path_dijkstra(self, graph, start_vertex, goal_vertex):
        assert (len(graph.vertices) > 0), "Graph is empty!"
        assert (start_vertex in graph.vertices), "start_vertex is not in Vertices!"
        assert (goal_vertex in graph.vertices), "GoalVertex is not in Vertices!"
        self.initialize_dijkstra_vertices(graph, start_vertex)

        vertex_queue = [start_vertex]
        while (len(vertex_queue) > 0):
            vertex = self.get_vertex_with_smallest_distance(graph, vertex_queue)
            if vertex == goal_vertex: break
            vertex_queue.remove(vertex)
            vertex_distance = graph.dijkstra_vertices[vertex].distance
            # iterate through all neighbours and check the new distance
            for index, child in enumerate(vertex.children):
                if graph.dijkstra_vertices[child].distance == float('inf'):
                    vertex_queue.append(child)
                edge_weight = vertex.get_edge_weight(child)
                if vertex_distance + edge_weight < graph.dijkstra_vertices[child].distance:
                    graph.dijkstra_vertices[child].distance = vertex_distance + edge_weight
                    graph.dijkstra_vertices[child].predecessor = vertex
        return self.get_path(graph, goal_vertex)

    def find_path_a_star(self, graph, start_vertex, goal_vertex):
        assert (len(graph.vertices) > 0), "Graph is empty!"
        assert (start_vertex in graph.vertices), "start_vertex is not in Vertices!"
        assert (goal_vertex in graph.vertices), "GoalVertex is not in Vertices!"

        self.initialize_dijkstra_vertices(graph, start_vertex)

        vertex_queue = [start_vertex]
        while (len(vertex_queue) > 0):
            vertex = self.get_smallest_a_star_vertex(graph, vertex_queue, goal_vertex)
            if vertex == goal_vertex: break;
            vertex_queue.remove(vertex)
            vertex_distance = graph.dijkstra_vertices[vertex].distance
            # iterate through all neighbours and check the new distance
            for index, child in enumerate(vertex.children):
                edge_weight = vertex.get_edge_weight(child)
                if vertex_distance + edge_weight < graph.dijkstra_vertices[child].distance:
                    graph.dijkstra_vertices[child].distance = vertex_distance + edge_weight
                    graph.dijkstra_vertices[child].predecessor = vertex
                    vertex_queue.append(child)   # indirect implementation of the closed-list
        return self.get_path(graph, goal_vertex)

# ToDO: Zeitmessen + Zufaellige Graphen erzeugen mit zufaelliger Groesse