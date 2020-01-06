import Tile
import TileGrid
import math

tile_grid = TileGrid.TileGrid()

def main(): #Takes 2 inputs for grid-size and amount of mines then loads the grid
    print("Enter grid size(length = width): ", end="")
    while True:
        try:
            gridSize = int(input())
            print(gridSize)
            if gridSize > 10 or gridSize < 5:
                print("Enter a value between 4 and 11: ", end="")
                continue
            break
        except ValueError:
            print("Enter a value between 4 and 11: ", end="")
            continue

    print("Enter amount of mines: ", end="")
    while True:
        try:
            mines = int(input())
            if mines > gridSize or mines < 3:
                print("Enter a value between 2 and " + str(gridSize + 1) + ": ", end="")
                continue
            break
        except ValueError:
            print("Enter a value between 2 and 100: ", end="")
            continue
    tile_grid.loadGrid(gridSize , gridSize, mines)
    tile_grid.addAdjacentTiles()
    
   
    game()

def game(): #Displats grid then asks for input. You can either flag or open a tile or quit
    while True:
        print(tile_grid,"\n",tile_grid.getMinesRemaining(), " mines remaining.", sep="")
        print("Type in tile position 'xx', or 'quit' to quit.\nYou can also type 'fxx' to mark a tile with a flag: ", end="")
        while True:
            try:
                inp = input()
                if inp.lower() == "quit": #If you type in 'quit' it saves the game and exits
                    tile_grid.save()
                    tile_grid.exitProgram()
                elif inp[0].lower() == "f": #If f is the first letter of the string you flag the tile
                    cord = tile_grid.getCord(inp[1:])
                    if not cord == None: #getCord return none if the tile does not exist
                        tile_grid.flagTile(cord)
                    else:
                        print("You can flag that Tile: ", end="")
                        continue
                else:
                    cord = tile_grid.getCord(inp)
                    if not cord == None:
                        tile_grid.click(cord)
                    else:
                        print("Thats not a Tile: ", end="")
                        continue
                tile_grid.checkWin()
                break
            except (IndexError, ValueError):
                print("Enter correct command: ", end="")
                continue
        if tile_grid.getExit():
            print(tile_grid)
            break
            


main()
    