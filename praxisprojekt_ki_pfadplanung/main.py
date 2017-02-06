from Labyrinth import Labyrinth
from Graph import Graph
from Vertex import Vertex
from VertexDijkstra import VertexDijkstra

labyrinth = Labyrinth()
graph = Graph()
labyrinth.createCustomLabyrinth()
#labyrinth.printMatrix()
graph.createGraph(labyrinth)
#graph.printGraph()
#graph.findAllPathsDijkstra()
#graph.printDijkstraGraph()
path = graph.findPathDijkstra(7,0)
print path