import Tile
import random
import math

class TileGrid:
    def __init__(self, size_x, size_y, mines):
        self.size = [size_x, size_y]
        self.allTiles = []
        self.mines = mines
        self.tileSize = 20
        self.minesGenerated = False

    def Click(self, cord):
        tile = self.GetTile(cord)
        if not self.minesGenerated and not tile.Flaged():
            self.GenerateMines(tile)
            self.minesGenerated = True
        elif not tile.Opened() and not tile.Flaged() and not tile.Mined():
            self.Flood(tile)
        elif not tile.Flaged() and tile.Mined():
            self.Lose()

    def FlagTile(self, cord):
        tile = self.GetTile(cord)
        if self.minesGenerated and not tile.Opened():
            tile.Flag()
                
    def LoadGrid(self):
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                self.allTiles.append(Tile.Tile(x,y))
    
    def GenerateMines(self, tile):
        #Starting tile and all tiles around it should be a save-tile
        safeTile = tile
        lista = []
        for tile in safeTile.adjacentTiles:
            lista.append(tile)
        lista.append(safeTile)

        #Loops until all mines have been randomized
        i = 0
        while(i < self.mines):
            i+=1
            cord = [random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1)]
            self.check = True
            for tile in lista: #Checks if cord already is mined or is a safeTile
                if tile.gridPosition == cord:
                    self.check = False
                    i+=-1
            if self.check:
                for t in self.allTiles: #Mines the Tile and adds the Tile to the list of safeTiles
                    if t.gridPosition == cord:
                        t.Mine()
                        lista.append(t)
        #After all mines have been placed we want all Tiles to check how many tiles there are around them
        #Then Flood on the starting Tile
        self.CheckMinesNear()
        self.Flood(safeTile)
            

    def addAdjacentTiles(self): #Adds the tiles around a tile to the list -> adjacentTiles
        for t in self.allTiles:
            for cord in t.adjacentCords:
                for tile in self.allTiles:
                    if tile.gridPosition == [(cord[0] + t.gridPosition[0]), (cord[1] + t.gridPosition[1])]:
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

    #Returns False if you lose and True if you win, and 0 if neither
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

    def GetTile(self, cord): #Get a tile by its position in the xy - plane
        pos = []
        pos.append(int(math.floor(cord[0]/self.tileSize)))
        pos.append(int(math.floor(cord[1]/self.tileSize)))

        return self.allTiles[pos[0] + pos[1]*self.size[0]] #Returns the tile with given cord

    def Draw(self, canvas):
        for tile in self.allTiles:
            tile.Draw(canvas)

    def Lose(self):
        for t in self.allTiles:
            t.OpenTile()
        print("You suck!")