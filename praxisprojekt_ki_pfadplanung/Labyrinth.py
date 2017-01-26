import random
random.seed(5) #to work with the same result every time
import constants


class Labyrinth:  
    def __init__(self):
        self.constantObj = constants.Constants()
        self.worm_x = 0
        self.worm_y = 0
        self.wormholeLength = 10
        self.numWormholes = 3
        self.Matrix = [[self.constantObj.CONST_WALL_SYMBOL for x in range(self.constantObj.CONST_WIDTH)] for y in range(self.constantObj.CONST_HEIGHT)]
    
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
        
    def checkDirections(self):
        possibleDirections = []
        # north
        if self.worm_y-1 >= 0:
            possibleDirections += [0]
        # east
        if self.worm_x+1 < self.constantObj.CONST_WIDTH:
            possibleDirections += [1]
        # south
        if self.worm_y+1 < self.constantObj.CONST_HEIGHT:
            possibleDirections += [2]
        # west
        if self.worm_x-1 >= 0:
            possibleDirections += [3]
        assert (len(possibleDirections) > 1),"No direction is passable!"
        return possibleDirections    


    def createWormhole(self):
        # random start corner
        rnd = random.randint(0,3)
        # north-west start corner
        if rnd == 0:
            self.worm_x = 0
            self.worm_y = 0
        # north-east start corner
        if rnd == 1:
            self.worm_x = self.constantObj.CONST_WIDTH-1
            self.worm_y = 0
        # south-west start corner
        if rnd == 2:
            self.worm_x = 0
            self.worm_y = self.constantObj.CONST_HEIGHT-1
        # south-east start corner
        if rnd == 3:
            self.worm_x = self.constantObj.CONST_WIDTH-1
            self.worm_y = self.constantObj.CONST_HEIGHT-1
        x = self.worm_x
        y = self.worm_y
        self.Matrix[x][y] = self.constantObj.CONST_EMPTY_SYMBOL
        for i in range(self.wormholeLength): 
            possibleDirections = self.checkDirections()
            possibleDirectionsTemp = possibleDirections[:]
            directionFound = False
            while(not directionFound):
                # if possibleDirectionsTemp is empty
                if len(possibleDirectionsTemp) == 0:
                    rnd = random.randint(0,len(possibleDirections)-1)
                    direction = possibleDirections[rnd]
                    directionFound = True
                else:
                    if len(possibleDirectionsTemp) > 1:
                        rnd = random.randint(0,len(possibleDirectionsTemp)-1)
                    else:
                        rnd = 0
                    direction = possibleDirectionsTemp[rnd]
                # north
                if direction == 0:
                    y = self.worm_y  - 1
                    x = self.worm_x
                # east
                if direction == 1:
                    y = self.worm_y 
                    x = self.worm_x + 1
                # south
                if direction == 2:
                    y = self.worm_y  + 1
                    x = self.worm_x
                # west
                if direction == 3:
                    y = self.worm_y
                    x = self.worm_x - 1

                if self.Matrix[x][y] == self.constantObj.CONST_EMPTY_SYMBOL and directionFound == False:
                    possibleDirectionsTemp.remove(direction)
                else:
                    directionFound = True

            self.Matrix[x][y] = self.constantObj.CONST_EMPTY_SYMBOL
            self.worm_y = y
            self.worm_x = x                                    

    def printMatrix(self):
        for y in range(self.constantObj.CONST_HEIGHT): 
            print("")
            for x in range(self.constantObj.CONST_WIDTH):
                print self.Matrix[y][x],
        print

    def makeLabyrinth(self):
        for i in range(self.numWormholes): 
            self.createWormhole()