from praxisprojekt_ki_pfadplanung.model.priority_queue import PriorityQueue, Priority
import math

class DStarLite:
    def __init__(self, graph, start_vertex, goal_vertex):
        self.graph = graph
        self.start_vertex = start_vertex
        self.goal_vertex = goal_vertex
        self.last_vertex = start_vertex
        self.priority_queue = PriorityQueue()
        self.accumulation = 0
        self.rhs = {}
        self.distance = {}
        self.changed_edges = []
        self.change_happened = False

    def initialize(self):
        for index, vertex in enumerate(self.graph.vertices):
            self.rhs[vertex] = float('inf')
            self.distance[vertex] = float('inf')
        self.rhs[self.goal_vertex] = 0
        self.priority_queue.insert(self.goal_vertex,
                                   Priority(self.get_estimation(self.start_vertex, self.goal_vertex), 0))

    def get_estimation(self, vertex1, vertex2):
        return math.sqrt(
            abs(vertex1.positionX - vertex2.positionX) ** 2
            + abs(vertex1.positionY - vertex2.positionY) ** 2)

    def calculate_key(self, vertex):
        k1 = min(self.distance[vertex], self.rhs[vertex]) \
             + self.get_estimation(self.start_vertex, vertex) + self.accumulation
        k2 = min(self.distance[vertex], self.rhs[vertex])
        return Priority(k1, k2)

    def contain(self, vertex):
        return vertex in self.priority_queue.vertices_in_heap

    def update_vertex(self, vertex):
        if self.distance[vertex] != self.rhs[vertex] and self.contain(vertex):
            self.priority_queue.update(vertex, self.calculate_key(vertex))
        elif self.distance[vertex] != self.rhs[vertex] and not self.contain(vertex):
            self.priority_queue.insert(vertex, self.calculate_key(vertex))
        elif self.distance[vertex] == self.rhs[vertex] and self.contain(vertex):
            self.priority_queue.remove(vertex)

    def compute_shortest_path(self):
        while self.priority_queue.top_key() < self.calculate_key(self.start_vertex) or self.rhs[self.start_vertex] > self.distance[self.start_vertex]:
            vertex = self.priority_queue.top()
            old_key = self.priority_queue.top_key()
            new_key = self.calculate_key(vertex)
            if old_key < new_key:
                self.priority_queue.update(vertex, new_key)
            elif self.distance[vertex] > self.rhs[vertex]:
                self.distance[vertex] = self.rhs[vertex]
                self.priority_queue.remove(vertex)
                for index, pred in enumerate(vertex.get_predecessors(self.graph)):
                    if pred != self.goal_vertex:
                        self.rhs[pred] = min(self.rhs[pred], pred.get_edge_weight(vertex) + self.distance[vertex])
                    self.update_vertex(pred)
            else:
                distance_old = self.distance[vertex]
                self.distance[vertex] = float('inf')
                for index, pred in enumerate(vertex.get_predecessors(self.graph)): # | {vertex}
                    if self.rhs[pred] == pred.get_edge_weight(vertex) + distance_old:
                        if pred != self.goal_vertex:
                            minimum = float('inf')
                            for i, succ in enumerate(pred.children):
                                distance = pred.get_edge_weight(succ) + self.distance[succ]
                                if minimum > distance:
                                    minimum = distance
                            self.rhs[pred] = minimum
                    self.update_vertex(pred)


    def find_path_d_star_lite(self):
        assert (len(self.graph.vertices) > 0), "Graph is empty!"
        assert (self.start_vertex in self.graph.vertices), "start_vertex is not in Vertices!"
        assert (self.goal_vertex in self.graph.vertices), "GoalVertex is not in Vertices!"

        last_vertex_costchange = self.start_vertex
        self.initialize()
        self.compute_shortest_path()
        path = self.get_path()
        if len(path) < 2:
            return False
        print self.start_vertex.key,
        repetition = 0
        moment_of_edge_change = len(path) / 2
        while(self.start_vertex != self.goal_vertex):
            assert(self.rhs[self.start_vertex] != float('inf')), "There is no known path!"
            # find next vertex on the path from start to goal
            minimum = float('inf')
            min_vertex = None
            for index, succ in enumerate(self.start_vertex.children):
                distance = self.start_vertex.get_edge_weight(succ) + self.distance[succ]
                if distance < minimum:
                    minimum = distance
                    min_vertex = succ
            last_vertex = self.start_vertex
            self.start_vertex = min_vertex
            print self.start_vertex.key,

            # artificial cost change
            if repetition == moment_of_edge_change and len(path) > 2:
                self.changed_edges.append(self.graph.get_edge(path[len(path)/2 + len(path)/4], path[len(path)/2 + len(path)/4 + 1]))
                self.change_happened = True

            if self.change_happened == True:
                # edge cost changed!
                self.accumulation += self.get_estimation(last_vertex_costchange, self.start_vertex)
                last_vertex_costchange = self.start_vertex
                for index, edge in enumerate(self.changed_edges):
                    old_weight = edge.source.get_edge_weight(edge.destination)
                    self.make_edge_untraversable(edge.source, edge.destination) # Update edge cost

                    if old_weight > edge.source.get_edge_weight(edge.destination):
                        if edge.source != self.goal_vertex:
                            self.rhs[edge.source] = \
                                min(self.rhs[edge.source], edge.source.get_edge_weight(edge.destination) + self.distance[edge.destination])
                    elif self.rhs[edge.source] == old_weight + self.distance[edge.destination]:
                        if edge.source != self.goal_vertex:
                            minimum = float('inf')
                            for index, succ in enumerate(edge.source.children):
                                distance = edge.source.get_edge_weight(succ) + self.distance[succ]
                                if distance < minimum: minimum = distance
                            self.rhs[edge.source] = minimum
                    self.update_vertex(edge.source)
                self.compute_shortest_path()
                path = self.get_path()
                self.change_happened = False
            repetition += 1
        print


    def make_edge_untraversable(self, vertex1_key, vertex2_key):
        self.graph.update_edge_weight(vertex1_key, vertex2_key, float('inf'))
        print "\n!!!"

    def printQueue(self):
        for index, node in enumerate(self.priority_queue.heap):
            print str(node.vertex.key) + ": [" + str(node.priority.k1) + ", " + str(node.priority.k2) + "]"

    def printDistance(self):
        for index, vertex in enumerate(self.graph.vertices):
            print str(vertex.key) + ": " + str(self.distance[vertex])

    # this function is not necessary
    def get_path(self):
        path = []
        min_vertex = None
        currentVertex = self.start_vertex
        path.append(currentVertex.key)
        while currentVertex != self.goal_vertex:
            minimum = float('inf')
            for index, succ in enumerate(currentVertex.children):
                distance = currentVertex.get_edge_weight(succ) + self.distance[succ]
                if distance < minimum:
                    minimum = distance
                    min_vertex = succ
            currentVertex = min_vertex
            path.append(currentVertex.key)
        return path
