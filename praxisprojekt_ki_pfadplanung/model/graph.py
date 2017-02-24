"""
This module ...
"""

from praxisprojekt_ki_pfadplanung.model.edge import Edge

class Graph:
    # ToDo: comments
    """
    Class xyz

    Attributes
    ----------
    classes_ : array of shape = [n_classes] or a list of such arrays
        The classes labels (single output problem),
        or a list of arrays of class labels (multi-output problem).
    feature_importances_ : array of shape = [n_features]
        The feature importances. The higher, the more important the
        feature. The importance of a feature is computed as the (normalized)
        total reduction of the criterion brought by that feature.  It is also
        known as the Gini importance [4]_.
    max_features_ : int,
        The inferred value of max_features.
    """
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.dijkstra_vertices = {}

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
    


