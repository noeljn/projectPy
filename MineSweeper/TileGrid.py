import Tile
import random
import math
import os
from timeit import default_timer as timer

class TileGrid():
    def __init__(self, size_x = None, size_y = None, mines = None): #Size and mines
        self.size = [size_x, size_y]
        self.allTiles = []
        self.mines = mines
        self.exit = False
        self.flagedMines = 0
        self.startTimer = 0
        self.stopTimer = 0
        self.minesGenerated = False
    
    def exitProgram(self): #sets exit to True
        self.exit = True

    def getExit(self): #Returns exit
        return self.exit

    def flagTile(self, cord):
        tile = self.getTile(cord)
        if tile.getFlaged() and not tile.getOpened():
            self.flagedMines -= 1
            tile.flag()
        elif not tile.getOpened():
            self.flagedMines += 1
            tile.flag()
        
    
    def getMinesRemaining(self):
        return self.mines - self.flagedMines

    def click(self, cord): #If its the first click you generate the mines and start the timer otherwise you flood that tile
        tile = self.getTile(cord)
        if not self.minesGenerated and not tile.getFlaged():
            self.startTimer = timer()
            self.generateMines(tile)
            self.minesGenerated = True
        elif not tile.getOpened() and not tile.getMined() and not tile.getFlaged():
            self.flood(tile)
        elif tile.getMined() and not tile.getFlaged():
            self.lose()

                
    def loadGrid(self, size_x, size_y, mines): #Creates the tiles
        self.size = [size_x, size_y]
        self.mines = mines
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                self.allTiles.append(Tile.Tile(x,y))
    
    def generateMines(self, tile):
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
                        t.mine()
                        lista.append(t)
        #After all mines have been placed we want all Tiles to check how many tiles there are around them
        #Then Flood on the starting Tile
        self.checkMinesNear()
        self.flood(safeTile)
            
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
                    if tile.gridPosition == [(cord[0] + t.gridPosition[0]), (cord[1] + t.gridPosition[1])]:
                        t.adjacentTiles.append(tile)


    def checkMinesNear(self): #Tells all tiles to check how many mines are near them
        for tile in self.allTiles:
            tile.addMinesNear()

    def flood(self, startTile): #Opens all tiles that are in connection with the tile that was click, if that tile has no mines near
        stack = [] #Budget stack

        if(startTile.minesNear == 0):
            stack.append(startTile)
        startTile.openTile()

        while len(stack) > 0 :
            currentTile = stack.pop()
            for t in currentTile.adjacentTiles:
                if t.minesNear == 0 and t.mined == False and t.open == False:
                    stack.append(t)
                if t.mined == False:
                    t.openTile()

    def lose(self): #All tiles are reveald and calls for save
        for tile in self.allTiles:
            tile.openTile()
        self.exit = True
        self.save()
 
    def save(self): #Calculates points and time then saves it all in a top 10 list
        self.stopTimer = timer()
        points = 0
        for t in self.allTiles:
            if t.getMined() and t.getFlaged():
                points += 1
        finalTime = round((self.stopTimer - self.startTimer), 2)
        print("\n\nYour final time was: " + str(finalTime) + "s\nYou placed " + str(points) + " correct flags!")

        with open("toplista.txt", "a+") as f:
            f.write(f"{points},{finalTime}\n")

        with open("toplista.txt", "r") as f:
            content = f.readlines()
            array = []
            for r in content:
                tempContent = r.strip("\n")
                tempContent = tempContent.split(",")
                array.append(tempContent)

            array = sorted(array, key = lambda x: (x[1]))
            array = sorted(array, key = lambda x: (x[0]), reverse = True)
        os.remove("toplista.txt")
        with open("toplista.txt", "w+") as f:
            count = 0
            print("\nToplista")
            for i in array:
                count += 1
                if count > 10:
                    break
                print(str(count) + ". Points:",i[0],"| Final Time:" , i[1])
                f.write(f"{i[0]},{i[1]}\n")

        
        


    def getTile(self, cord): #Get a tile by its position in the xy - plane
        return self.allTiles[cord[0] + cord[1]*self.size[0]]

    def getCord(self, cord): #Checks if input from user is valid
        cord = str(cord).strip()
        pos = []
        pos.append(int(cord[0]))
        pos.append(int(cord[1]))
        if pos[0] > self.size[0] - 1 and pos[1] > self.size[1] - 1:
            return None
        else:
            return pos
