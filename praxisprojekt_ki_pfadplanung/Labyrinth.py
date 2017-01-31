from constants import CONST_WIDTH
from constants import CONST_HEIGHT
from constants import CONST_WALL_SYMBOL

class Labyrinth:  
    def __init__(self):
        self.Matrix = [[CONST_WALL_SYMBOL for x in range(CONST_WIDTH)] for y in range(CONST_HEIGHT)]
    
    def createCustomLabyrinth(self):
        self.Matrix = [ ['.','.','#','#','#','.','.','.'],
                        ['#','.','.','#','.','.','#','.'],
                        ['.','.','.','#','.','#','#','.'],
                        ['.','#','.','#','.','.','#','.'],
                        ['.','.','.','.','#','.','#','.'],
                        ['.','#','#','.','.','.','.','.'],
                        ['.','#','#','.','#','#','#','#'],
                        ['.','.','.','.','#','#','#','#'],]
    
    def createTinyCustomLabyrinth(self):
        self.Matrix = [ ['.','.','#'],
                        ['#','.','#'],
                        ['.','.','.']]

    def printMatrix(self):
        for y in range(CONST_HEIGHT):
            print("")
            for x in range(CONST_WIDTH):
                print self.Matrix[y][x],
        print