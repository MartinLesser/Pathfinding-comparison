import Labyrinth
import Graph

labyrinth = Labyrinth.Labyrinth()
graph = Graph.Graph()
labyrinth.createCustomLabyrinth()
labyrinth.printMatrix()
graph.createGraph(labyrinth)
graph.printGraph()
#path = graph.findPathDijkstra(7,0)
#print path