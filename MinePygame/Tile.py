import pygame

class Tile:
    def __init__(self, x, y):
        self.gridPosition = [x,y]
        self.minesNear = 0
        self.mined = False
        self.open = False
        self.flaged = False
        self.size = [20,20]
        self.image = pygame.transform.scale((pygame.image.load('Resources\cell.png')), (self.size[0], self.size[1]))#Loads the image then transforms it into the right size
        self.adjacentCords = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
        self.adjacentTiles = [] 

    def Mine(self):
        self.mined = True

    def Flaged(self):
        return self.flaged

    def Flag(self):
        if self.flaged:
            self.image = pygame.transform.scale((pygame.image.load('Resources\cell.png')), (self.size[0], self.size[1]))
        else:
            self.image = pygame.transform.scale((pygame.image.load('Resources\lag.png')), (self.size[0], self.size[1]))
        self.flaged = not self.flaged
        
    def Mined(self):
        return self.mined

    def OpenTile(self): #Its a little long, I dont like it
        self.open = True
        if self.mined: #Bad switch statment to change picture
            self.image = pygame.transform.scale((pygame.image.load('Resources\mine.png')), (self.size[0], self.size[1]))
        elif self.minesNear == 0 and not self.flaged:
            self.image = pygame.transform.scale((pygame.image.load('Resources\cell_0.png')), (self.size[0], self.size[1]))
        elif self.minesNear == 1 and not self.flaged:
            self.image = pygame.transform.scale((pygame.image.load('Resources\cell_1.png')), (self.size[0], self.size[1]))
        elif self.minesNear == 2 and not self.flaged:
            self.image = pygame.transform.scale((pygame.image.load('Resources\cell_2.png')), (self.size[0], self.size[1]))
        elif self.minesNear == 3 and not self.flaged:
            self.image = pygame.transform.scale((pygame.image.load('Resources\cell_3.png')), (self.size[0], self.size[1]))
        elif self.minesNear == 4 and not self.flaged:
            self.image = pygame.transform.scale((pygame.image.load('Resources\cell_4.png')), (self.size[0], self.size[1]))
        elif self.minesNear == 5 and not self.flaged:
            self.image = pygame.transform.scale((pygame.image.load('Resources\cell_5.png')), (self.size[0], self.size[1]))
        elif self.minesNear == 6 and not self.flaged: 
            self.image = pygame.transform.scale((pygame.image.load('Resources\cell_6.png')), (self.size[0], self.size[1]))
    
    def Opened(self):
        return self.open

    def MinesNear(self):
        for tile in self.adjacentTiles:
            if tile.mined:
                self.minesNear += 1

    def Draw(self, canvas):
        canvas.blit(self.image, (self.gridPosition[0] * 20, self.gridPosition[1] * 20))

    