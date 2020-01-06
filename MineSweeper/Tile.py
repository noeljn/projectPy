class Tile:
    def __init__(self, x, y):
        self.gridPosition = [x,y]
        self.minesNear = 0
        self.mined = False
        self.open = False
        self.flaged = False
        self.adjacentCords = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
        self.adjacentTiles = [] 

    def mine(self):
        self.mined = True

    def flag(self):
        self.flaged = not self.flaged

    def getFlaged(self):
        return self.flaged

    def getMined(self):
        return self.mined

    def openTile(self):
        self.open = True
    
    def getOpened(self):
        return self.open

    def addMinesNear(self):
        for tile in self.adjacentTiles:
            if tile.mined:
                self.minesNear += 1

    def __str__(self):
        if self.flaged:
            return "F"
        elif self.open == False:
            return  "*"
        elif self.mined:
            return "M"
        else:
            return str(self.minesNear)