import Labyrinth

def createGraph():
    graph = {}
    id = 0
    for y in range(Labyrinth.width): 
        for x in range(Labyrinth.height):
            if Labyrinth.Matrix[x][y] == Labyrinth.empty_symbol:
                list = []
                # north
                if y-1 >= 0 and Labyrinth.Matrix[x][y-1] == Labyrinth.empty_symbol:
                    list.append(id-Labyrinth.width)
                # east
                if x+1 < Labyrinth.width and Labyrinth.Matrix[x+1][y] == Labyrinth.empty_symbol:
                    list.append(id+1)
                # south
                if y+1 < Labyrinth.height and Labyrinth.Matrix[x][y+1] == Labyrinth.empty_symbol:
                    list.append(id+Labyrinth.width)
                # west
                if x-1 >= 0 and Labyrinth.Matrix[x-1][y] == Labyrinth.empty_symbol:
                    list.append(id-1)
                
                graph[id] = list
            id += 1
    return graph