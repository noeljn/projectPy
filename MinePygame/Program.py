import Tile
import TileGrid
import pygame

board = [10,10]
mines = 10
tile_grid = TileGrid.TileGrid(board[0],board[1],mines)
canvas = pygame.display.set_mode((board[0]*20, board[1]*20))
pygame.display.set_caption("MineSweeper")


class State:
    running = True
    win = False

def StartGame():
    tile_grid.LoadGrid()
    tile_grid.addAdjacentTiles()
    tile_grid.Draw(canvas)
    #pygame.display.update()
    pygame.display.flip()   
    state = State()
    Main(state)

def Main(state):
    while(state.running):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and state.running:
                if pygame.mouse.get_pressed()[0]: #Check first position in tupler to see if left click was pressed
                    mousePos = pygame.mouse.get_pos()
                    tile_grid.Click(mousePos)
                elif pygame.mouse.get_pressed()[2]: #Right click check
                    mousePos = pygame.mouse.get_pos()
                    tile_grid.FlagTile(mousePos)
                tile_grid.Draw(canvas)
                pygame.display.flip()
                


StartGame()