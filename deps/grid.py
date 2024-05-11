# class to keep the current cell grid
class Grid:
    def __init__(self, minTh, maxTh, borTh, BOX_SIZE, TILE_SIZE):
        # set grid and the min and max amount of cells around for the cell to stay alive
        self.size = int(BOX_SIZE/TILE_SIZE)
        self.newGrid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.grid = self.newGrid
        self.minTh = minTh
        self.maxTh = maxTh
        self.borTh = borTh
        self.cells = []
    # set x and y cell to alive
    def set(self, x, y):
        self.grid[x-1][y-1] = 1
        self.cells.append((x-1, y-1))
    # simulate 1 itteration for the game of life
    def simulate(self):
        # set variables
        GRID = self.grid
        usedCells = []
        # lol
        reincarnate = []
        
        # mother cell
        for mothercell in self.cells:
            # check cells around it
            for i in range(3):
                for j in range(3):
                    # child cell
                    x = mothercell[0]-1+i
                    y = mothercell[1]-1+j
                    if x >= 0 and x < len(GRID) and y >= 0 and y < len(GRID):
                        cell = (x, y)
                        if cell in usedCells:
                            pass
                        else:
                            summ = 0-GRID[x][y]
                            usedCells.append(cell)
                            for k in range(3):
                                for l in range(3):
                                    Cx = x-1+k
                                    Cy = y-1+l
                                    if Cx >= 0 and Cx < len(GRID) and Cy >= 0 and Cy < len(GRID):
                                        summ += GRID[Cx][Cy]
                            if GRID[x][y]:
                                if summ >= self.minTh and summ <= self.maxTh:
                                    reincarnate.append(cell)
                            else:
                                if summ == 3:
                                    reincarnate.append(cell)
        
        # restart grid and cells becouse of python toombfoolery:
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for cell in reincarnate:
            self.grid[cell[0]][cell[1]] = 1
        self.cells = reincarnate
        return self.cells
    # function to print the grid to console
    def print(self):
        printMap = ""
        # contruct the print
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[j][i]:
                    # alive cell represented as X
                    printMap += "X "
                else:
                    # dead cell represented in -
                    printMap += "- "
            printMap += "\n"
        # Print it to console
        print(printMap)