import matplotlib.pyplot as plt
import networkx as nx

class Output:
    def printGraph(self, graph):
        print 'Vertices:'
        for index,vertex in enumerate(graph.vertices):
            print str(vertex.key) + ' : ',
            children = vertex.children
            for i, vertex in enumerate(children):
                print str(vertex.key),
            print
        print 'Edges:'
        for i,vertex in enumerate(graph.edges):
            print 'Edge = (' + str(vertex.source.key) + ', ' + str(vertex.destination.key) + ')' + ' : weight(' + str(vertex.weight) + ')'

    def drawGraph(self, graph):
        G = nx.Graph()
        for index, vertex in enumerate(graph.vertices):
            G.add_node(vertex.key, pos=(vertex.positionX, vertex.positionY))
        for index, edge in enumerate(graph.edges):
            G.add_edge(edge.source.key,edge.destination.key, weight=edge.weight)
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw(G, pos, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.savefig('simple_graph')
        plt.show()


    def printDijkstraGraph(self, graph):
        assert(graph.dijkstraVertices), "Dijkstra-function has not been called yet!"
        print 'Vertices:'
        for index,vertex in enumerate(graph.vertices):
            print str(vertex.key) + ' : Distance = ' + str(graph.dijkstraVertices[vertex].distance) \
                  + ' Predecessor = ' + str( 'None' if (graph.dijkstraVertices[vertex].predecessor == None)
                                                               else graph.dijkstraVertices[vertex].predecessor.key)