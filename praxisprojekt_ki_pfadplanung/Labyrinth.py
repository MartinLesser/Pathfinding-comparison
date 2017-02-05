from constants import CONST_WIDTH
from constants import CONST_HEIGHT
from constants import CONST_WALL_SYMBOL

class Labyrinth:  
    def __init__(self):
        self.Matrix = [[CONST_WALL_SYMBOL for x in range(CONST_WIDTH)] for y in range(CONST_HEIGHT)]
    
    def createCustomLabyrinth(self):
        self.Matrix = [['.', '.', '#', '#', '#', '.', '.', '.'],
                       ['#', '.', '.', '#', '.', '.', '#', '.'],
                       ['.', '.', '.', '#', '.', '#', '#', '.'],
                       ['.', '#', '.', '#', '.', '.', '#', '.'],
                       ['.', '.', '.', '.', '#', '.', '#', '.'],
                       ['.', '#', '#', '.', '.', '.', '.', '.'],
                       ['.', '#', '#', '.', '#', '#', '#', '#'],
                       ['.', '.', '.', '.', '#', '#', '#', '#'], ]

        '''
        self.Matrix = [['00',   '01',    '#',    '#',    '#',    '05',   '06',   '07'],
                       [ '#',   '09',   '10',    '#',   '12',    '13',    '#',   '15'],
                       ['16',   '17',   '18',    '#',   '20',     '#',    '#',   '23'],
                       ['24',    '#',   '26',    '#',   '28',    '29',    '#',   '31'],
                       ['32',   '33',   '34',   '35',    '#',    '37',    '#',   '39'],
                       ['40',    '#',    '#',   '43',   '44',    '45',   '46',   '47'],
                       ['48',    '#',    '#',   '51',    '#',     '#',    '#',    '#'],
                       ['56',   '57',   '58',   '59',    '#',     '#',    '#',    '#'], ]
        '''
    
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