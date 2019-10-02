from praxisprojekt_ki_pfadplanung.constants import WIDTH, HEIGHT, EMPTY_SYMBOL
from praxisprojekt_ki_pfadplanung.model.edge import Edge
from praxisprojekt_ki_pfadplanung.model.vertex import Vertex


class Graph:
   
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_directed_edge(self, vertex1, vertex2, weight = 1):
        assert(vertex1 in self.vertices and vertex2 in self.vertices), "Vertices don't exist in the graph!"
        assert(weight >= 0), "Weight must be positive!"
        new_edge = Edge(vertex1, vertex2, weight)
        self.edges.append(new_edge)
        vertex1.add_edge(new_edge)

    def add_undirected_edge(self, vertex1, vertex2, weight=1):
        self.add_directed_edge(vertex1, vertex2, weight)
        self.add_directed_edge(vertex2, vertex1, weight)

    def update_edge_weight(self, vertex1_key, vertex2_key, weight):
        for index, edge in enumerate(self.edges):
            if edge.source.key == vertex1_key and edge.destination.key == vertex2_key:
                edge.weight = weight
                break

    def get_edge(self, vertex1_key, vertex2_key):
        for index, edge in enumerate(self.edges):
            if edge.source.key == vertex1_key and edge.destination.key == vertex2_key:
                return edge
        print "Edge could not be found!"

    def get_vertex(self, vertex_key):
        for index, vertex in enumerate(self.vertices):
            if vertex.key == vertex_key:
                return vertex

    def create_graph_from_labyrinth(self, labyrinth):
        self.vertices = []
        self.edges = []
        id = 0
        existingVerticesKeys = [] # to know quickly which vertices exist already
        newVertex = None
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if labyrinth.Matrix[y][x] == EMPTY_SYMBOL:
                    if(id not in existingVerticesKeys):
                        existingVerticesKeys.append(id)
                        newVertex = Vertex(id, x, y)
                        self.vertices.append(newVertex)
                    else:
                        # search for existing vertex
                        for i in range(len(self.vertices)):
                            if self.vertices[i].key == id:
                                newVertex = self.vertices[i]
                                break
                    assert(newVertex != None), "Vertex exists but could not be found!"

                    # east
                    if x+1 < WIDTH and labyrinth.Matrix[y][x+1] == EMPTY_SYMBOL:
                        if (id+1 not in existingVerticesKeys):
                            # create new vertex
                            eastChildVertex = Vertex(id + 1, x+1, y)
                            # add it to the vertices list
                            self.vertices.append(eastChildVertex)
                            existingVerticesKeys.append(id + 1)
                        else:
                            # search for existing vertex
                            for i in range(len(self.vertices)):
                                if self.vertices[i].key == id+1:
                                    eastChildVertex = self.vertices[i]
                                    break
                        # add child to current vertex
                        #todo newVertex.addChild(eastChildVertex)
                        # add child to eastChild
                        #todo astChildVertex.addChild(newVertex)
                        # create new edges and add it to the edges list
                        self.add_undirected_edge(newVertex, eastChildVertex)

                    # south
                    if y+1 < HEIGHT and labyrinth.Matrix[y+1][x] == EMPTY_SYMBOL:
                        # create new vertex
                        southChildVertex = Vertex(id+WIDTH, x, y+1)
                        # add it to the vertices list
                        self.vertices.append(southChildVertex)
                        existingVerticesKeys.append(id + WIDTH)
                        # add child to current vertex
                        # todo newVertex.addChild(southChildVertex)
                        # add child to eastChild
                        # todo southChildVertex.addChild(newVertex)
                        # create new edges and add it to the edges list
                        self.add_undirected_edge(newVertex, southChildVertex)
                id += 1
                newVertex = None
