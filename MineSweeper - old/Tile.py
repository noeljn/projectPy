class Tile:
    def __init__(self, x, y):
        self.name = "Tile_{}_{}".format(x,y)
        self.gridPosition = [x,y]
        self.minesNear = 0
        self.mined = False
        self.open = False
        self.flaged = False
        self.adjacentCords = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
        self.adjacentTiles = [] 

    def Mine(self):
        self.mined = True

    def Mined(self):
        return self.mined

    def OpenTile(self):
        self.open = True
    
    def Opened(self):
        return self.open

    def MinesNear(self):
        for tile in self.adjacentTiles:
            if tile.mined:
                self.minesNear += 1

    def __str__(self):
        if self.open == False:
            return  str(self.gridPosition[0]) + str(self.gridPosition[1])
        elif self.mined:
            return "M "
        else:
            return str(self.minesNear) + " "