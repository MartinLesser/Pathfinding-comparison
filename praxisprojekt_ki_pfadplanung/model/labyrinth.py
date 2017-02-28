import random
from enum import Enum
from praxisprojekt_ki_pfadplanung.constants import WIDTH, HEIGHT, WALL_SYMBOL, EMPTY_SYMBOL, \
                                                    NUM_WORMHOLES, WORMHOLE_LENGTH, DIRECTION_CHANGE_CHANCE

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Labyrinth:
    def __init__(self, seed = 1):
        self.worm_x = 0
        self.worm_y = 0
        self.x = 0
        self.y = 0
        random.seed(seed)  # to work with the same result every time
        self.Matrix = [[WALL_SYMBOL for x in range(WIDTH)] for y in range(HEIGHT)]

    def createCustomLabyrinth(self):
        self.Matrix = [['.', '.', '#', '#', '#', '.', '.', '.'],
                       ['#', '.', '.', '#', '.', '.', '#', '.'],
                       ['.', '.', '.', '#', '.', '#', '#', '.'],
                       ['.', '#', '.', '#', '.', '.', '#', '.'],
                       ['.', '.', '.', '.', '#', '.', '#', '.'],
                       ['.', '#', '#', '.', '.', '.', '.', '.'],
                       ['.', '#', '#', '.', '#', '#', '#', '#'],
                       ['.', '.', '.', '.', '#', '#', '#', '#'], ]

    def createTinyCustomLabyrinth(self):
        self.Matrix = [['.', '.', '#'],
                       ['#', '.', '#'],
                       ['.', '.', '.']]

    def checkDirections(self):
        possibleDirections = []
        # north
        if self.worm_y - 1 >= 0:
            possibleDirections.append(Direction.NORTH)
        # east
        if self.worm_x + 1 < WIDTH:
            possibleDirections.append(Direction.EAST)
        # south
        if self.worm_y + 1 < HEIGHT:
            possibleDirections.append(Direction.SOUTH)
        # west
        if self.worm_x - 1 >= 0:
            possibleDirections.append(Direction.WEST)
        assert (len(possibleDirections) > 1), "No direction is passable!"
        return possibleDirections

    def set_wormhole_start(self):
        self.worm_x = random.randint(0, WIDTH - 1)
        self.worm_y = random.randint(0, HEIGHT - 1)
        self.x = self.worm_x
        self.y = self.worm_y
        self.Matrix[self.x][self.y] = EMPTY_SYMBOL


    def createWormhole(self):
        self.set_wormhole_start()
        x = self.x
        y = self.y
        for i in range(WORMHOLE_LENGTH):
            possibleDirections = self.checkDirections()
            possibleDirectionsTemp = possibleDirections[:]
            directionFound = False
            direction = possibleDirections[0]
            while (not directionFound):
                # if all passable directions are already empty take a random passable direction
                if len(possibleDirectionsTemp) == 0:
                    rnd = random.randint(0, len(possibleDirections) - 1)
                    direction = possibleDirections[rnd]
                    directionFound = True
                else:
                    if len(possibleDirectionsTemp) > 1:
                        rnd = random.randint(0, len(possibleDirectionsTemp) - 1)
                        if direction not in possibleDirectionsTemp:
                            direction = possibleDirectionsTemp[rnd]
                        elif random.randint(0, 100) <= DIRECTION_CHANGE_CHANCE:  # chance to change direction
                            direction = possibleDirectionsTemp[rnd]
                    else:
                        direction = possibleDirectionsTemp[0]
                # north
                if direction == Direction.NORTH:
                    y = self.worm_y - 1
                    x = self.worm_x
                # east
                if direction == Direction.EAST:
                    y = self.worm_y
                    x = self.worm_x + 1
                # south
                if direction == Direction.SOUTH:
                    y = self.worm_y + 1
                    x = self.worm_x
                # west
                if direction == Direction.WEST:
                    y = self.worm_y
                    x = self.worm_x - 1

                if self.Matrix[x][y] == EMPTY_SYMBOL and directionFound == False:
                    possibleDirectionsTemp.remove(direction)
                else:
                    directionFound = True

            self.Matrix[x][y] = EMPTY_SYMBOL
            self.worm_y = y
            self.worm_x = x

    def printMatrix(self):
        for y in range(HEIGHT):
            print("")
            for x in range(WIDTH):
                print self.Matrix[y][x],
        print

    def makeLabyrinth(self):
        for i in range(NUM_WORMHOLES):
            self.createWormhole()