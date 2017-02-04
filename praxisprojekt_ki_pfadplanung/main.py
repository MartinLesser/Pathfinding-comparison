from Labyrinth import Labyrinth
from Graph import Graph

labyrinth = Labyrinth()
graph = Graph()
labyrinth.createCustomLabyrinth()
labyrinth.printMatrix()
graph.createGraph(labyrinth)
graph.printGraph()
#path = graph.findPathDijkstra(7,0)
#print path