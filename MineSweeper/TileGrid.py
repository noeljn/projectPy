import Tile
import random

class TileGrid():
    def __init__(self, size_x, size_y):
        self.size = [size_x, size_y]
        self.allTiles = []
        self.mines = size_x * size_y

    def ClickTile(self, cord):
        cord = str(cord)
        tile = 0
        for t in self.allTiles:
            if "Tile_{}_{}".format(cord[0], cord[1]) == t.name:
                t.OpenMine()
                

    def LoadGrid(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.allTiles.append(Tile.Tile(x,y))
    
    def GenerateMines(self, cord):
        cord = str(cord)
        safeTile = 0
        for t in self.allTiles:
            if "Tile_{}_{}".format(cord[0], cord[1]) == t.name:
                safeTile = t
                safeTile.OpenMine()
        lista = []
        lista.append(safeTile)
        i = 0
        while(i < self.size[0]*2):
            i+=1
            cord = [random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1)]
            cord = "Tile_{}_{}".format(cord[0], cord[1])
            self.check = True
            for tile in lista: #Checks if cord already is mined or is a safeTile
                if tile.name == cord:
                    self.check = False
                    i+=-1
            if self.check:
                for t in self.allTiles: #Mines the Tile and adds the Tile to the list of safeTiles
                    if t.name == cord:
                        t.Mine()
                        lista.append(t)
            
    def __str__(self): #Returns the board of mines
        string = ""
        for y in range(self.size[1]):
            string += "\n"
            string += " ".join(str(self.allTiles[x]) for x in range(y*self.size[0], y*self.size[0] + self.size[0]))
        return string

    def addAdjacentTiles(self): #Adds the tiles around a tile to the list -> adjacentTiles
        for t in self.allTiles:
            for cord in t.adjacentCords:
                for tile in self.allTiles:
                    if tile.name == "Tile_{}_{}".format(cord[0] + t.gridPosition[0], cord[1] + t.gridPosition[1]):
                        t.adjacentTiles.append(tile)

    def CheckMinesNear(self):
        for tile in self.allTiles:
            tile.MinesNear()