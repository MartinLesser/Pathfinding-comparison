from Graph import Graph

graph = Graph()
#labyrinth.printMatrix()
graph.createCustomGraph()
#graph.printGraph()
#graph.findAllPathsDijkstra()
#graph.printDijkstraGraph()
path = graph.findPathDijkstra(7,0)
print path