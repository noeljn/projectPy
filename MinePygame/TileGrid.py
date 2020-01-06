import Tile
import random
import math
import pygame

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 10)

class TileGrid:
    def __init__(self, size_x, size_y, mines):
        self.size = [size_x, size_y]
        self.allTiles = []
        self.mines = mines
        self.flagedMines = 0
        self.tileSize = 20 #in pixels
        self.minesGenerated = False

    def Click(self, cord, canvas):
        tile = self.GetTile(cord)
        if not tile == None:
            if not self.minesGenerated and not tile.Flaged():
                self.GenerateMines(tile)
                self.minesGenerated = True
            elif not tile.Opened() and not tile.Flaged() and not tile.Mined():
                self.Flood(tile)
            elif not tile.Flaged() and tile.Mined():
                self.Lose(canvas)

    def FlagTile(self, cord):
        tile = self.GetTile(cord)
        if not tile == None:
            if self.minesGenerated and not tile.Opened():
                tile.Flag()
            if tile.Flaged():
                self.flagedMines -= 1
            else:
                self.flagedMines += 1

                
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

    def CheckWin(self): #You can win in two ways, if all mines are flaged or if all tiles that are not mines are open
        win = True #Checks if all mines are flaged
        secWin = True #Checks if all tiles that are not mines are open
        for t in self.allTiles:
            if t.Mined() and t.Opened():
                win = False
                secWin = False
            if not t.Mined() and not t.Opened():
                secWin = False
            if t.Mined() and not t.Flaged():
                win = False
        if win or secWin:
            return True
        else: 
            return False

    def GetTile(self, cord): #Get a tile by its position in the xy - plane
        pos = []
        pos.append(int(math.floor(cord[0]/self.tileSize)))
        pos.append(int(math.floor(cord[1]/self.tileSize)))
        if pos[0] > self.size[0] - 1 or pos[1] > self.size[1] - 1: #Check that the click is within the board
            return None
        else:
            return self.allTiles[pos[0] + pos[1]*self.size[0]] #Returns the tile with given cord

    def Draw(self, canvas):
        for tile in self.allTiles:
            tile.Draw(canvas)

    def Lose(self, canvas):
        minesFlaged = 0
        for t in self.allTiles:
            t.OpenTile()
            if t.Mined() and t.Flaged():
                minesFlaged += 1
        
        self.Write(self.size[0]*self.tileSize, self.size[1]*self.tileSize, 'You Lost! Mines Correctly Flaged: ' + str(minesFlaged), canvas)

    def Win(self, canvas):
        self.Write(self.size[0]*self.tileSize, self.size[1]*self.tileSize, 'You Won! Congratulations!', canvas)
    
    def Write(self, x, y, text, canvas):
        textsurface = myfont.render(text, False, (0, 255, 0))
        rect = textsurface.get_rect()
        rect.center = (x, y)
        canvas.blit(textsurface, rect)