import Labyrinth
import Graph
#import Dijkstra

labyrinth = Labyrinth.Labyrinth()
graph = Graph.Graph()
#labyrinth.makeLabyrinth()
labyrinth.createCustomLabyrinth()
labyrinth.printMatrix()
#graph.createGraph(labyrinth)
graph.createGraph(labyrinth)
#graph.printGraph()
graph.findPathDijkstra()