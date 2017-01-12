import random
random.seed(5)

width, height = 8, 8 
Matrix = [['#' for x in range(width)] for y in range(height)] 
wormholeLength = 10
numberOfWormholes = 3
worm_x = 0
worm_y = 0
wall_symbol = '#'
empty_symbol = '.'


def checkDirections():
    possibleDirections = []
    # north
    if worm_y-1 >= 0:
        possibleDirections += [0]
    # east
    if worm_x+1 < width:
        possibleDirections += [1]
    # south
    if worm_y+1 < height:
        possibleDirections += [2]
    # west
    if worm_x-1 >= 0:
        possibleDirections += [3]
    assert (len(possibleDirections) > 1),"No direction is passable!"
    return possibleDirections    
    

def createWormhole():
    global worm_x, worm_y
    rnd = random.randint(0,3)
    if rnd == 0:
        worm_x = 0
        worm_y = 0
    if rnd == 1:
        worm_x = width-1
        worm_y = 0
    if rnd == 2:
        worm_x = 0
        worm_y = height-1
    if rnd == 3:
        worm_x = width-1
        worm_y = height-1
    x = worm_x
    y = worm_y
    Matrix[x][y] = empty_symbol
    for i in range(wormholeLength): 
        possibleDirections = checkDirections()
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
                y = worm_y  - 1
                x = worm_x
            # east
            if direction == 1:
                y = worm_y 
                x = worm_x + 1
            # south
            if direction == 2:
                y = worm_y  + 1
                x = worm_x
            # west
            if direction == 3:
                y = worm_y
                x = worm_x - 1
            
            if Matrix[x][y] == empty_symbol and directionFound == False:
                possibleDirectionsTemp.remove(direction)
            else:
                directionFound = True
                
        Matrix[x][y] = empty_symbol
        worm_y = y
        worm_x = x                                    
                
def printMatrix():
    for x in range(width): 
        print("")
        for y in range(height):
            print Matrix[y][x],
    print
            
def makeLabyrinth():
    for i in range(numberOfWormholes): 
        createWormhole()