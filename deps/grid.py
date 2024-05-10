# class to keep the current cell grid
class Grid:
    def __init__(self, minTh, maxTh, borTh, BOX_SIZE, TILE_SIZE):
        # set grid and the min and max amount of cells around for the cell to stay alive
        self.grid = [[0 for _ in range(int(BOX_SIZE/TILE_SIZE))] for _ in range(int(BOX_SIZE/TILE_SIZE))]
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
        newGrid = self.grid
        Grid = self.grid
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
                    if x >= 0 and x < len(Grid) and y >= 0 and y < len(Grid):
                        cell = (x, y)
                        if cell in usedCells:
                            pass
                        else:
                            summ = 0-Grid[x][y]
                            usedCells.append(cell)
                            for k in range(3):
                                for l in range(3):
                                    Cx = x-1+k
                                    Cy = y-1+l
                                    if Cx >= 0 and Cx < len(Grid) and Cy >= 0 and Cy < len(Grid):
                                        print((Cx, Cy), Grid[Cx][Cy])
                                        summ += Grid[Cx][Cy]
                            print(x, y, summ)
                            if Grid[x][y]:
                                if summ > self.minTh and summ < self.maxTh:
                                    reincarnate.append(cell)
                                    newGrid[x][y] = 1
                                else:
                                    newGrid[x][y] = 0
                            else:
                                if summ == 3:
                                    reincarnate.append(cell)
                                    newGrid[x][y] = 0
                                else:
                                    newGrid[x][y] = 0
        self.grid = newGrid
        self.cells = reincarnate
        return newGrid
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