import Tile
import random

class TileGrid():
    def __init__(self, size_x, size_y, mines):
        self.size = [size_x, size_y]
        self.allTiles = []
        self.mines = mines

    def ClickTile(self, cord):
        tile = self.GetTile(cord)
        if tile.open == False and tile.flaged == False:
            self.Flood(tile)

                
    def LoadGrid(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.allTiles.append(Tile.Tile(x,y))
    
    def GenerateMines(self, cord):
        ##Find the all the safe Tiles
        safeTile = self.GetTile(cord)
        lista = []
        for tile in safeTile.adjacentTiles:
            lista.append(tile)
        lista.append(safeTile)

        #Loops until all mines have been randomized
        i = 0
        while(i < self.mines):
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
        #After all mines have been placed we want all Tiles to check how many tiles there are around them
        #Then Flood on the starting Tile
        self.CheckMinesNear()
        self.Flood(safeTile)
            
    def __str__(self): #Returns the board of mines
        string = " "
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

    def Flood(self, startTile):
        stack = [] #Budget stack

        if(startTile.minesNear == 0):
            stack.append(startTile)
        startTile.OpenTile()

        while len(stack) > 0 :
            currentTile = stack.pop()
            for t in currentTile.adjacentTiles:
                if t.minesNear == 0 and t.mined == False and t.open == False:
                    stack.append(t)
                if t.mined == False:
                    t.OpenTile()

    def CheckWin(self): #Checks if all Tiles that shoud be open are and that all mines are not open
        win = 0
        for tile in self.allTiles:
            if tile.mined and tile.open:
                win = False
                return win
            elif tile.mined == False and tile.open == False:
                return win
        win = True
        return win

    def RevealTiles(self):
        for tile in self.allTiles:
            tile.OpenTile()
    
    def GetTile(self, cord):
        cord = str(cord).strip()
        for t in self.allTiles:
            if "Tile_{}_{}".format(cord[0], cord[1]) == t.name:
                return t

    def CheckInput(self, cord):
        try:
            cord = str(cord).strip()
            for t in self.allTiles:
                if "Tile_{}_{}".format(cord[0], cord[1]) == t.name:
                    return False
            return True
        except:
            return True
