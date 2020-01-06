import Tile
import TileGrid
import math

tile_grid = TileGrid.TileGrid()

def main():
    print("Enter grid size(length = width): ", end="")
    while True:
        try:
            gridSize = int(input())
            print(gridSize)
            if gridSize > 10 or gridSize < 5:
                print("Enter a value between 4 and 11: ", end="")
                continue
            break
        except:
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
        except:
            print("Enter a value between 2 and 100: ", end="")
            continue
    tile_grid.loadGrid(gridSize , gridSize, mines)
    tile_grid.addAdjacentTiles()
    
   
    game()

def game():
    while True:
        print(tile_grid,"\n",tile_grid.getMinesRemaining(), " mines remaining.", sep="")
        print("Type in tile position 'xx', or 'quit' to quit.\nYou can also type 'fxx' to mark a tile with a flag: ", end="")
        while True:
            try:
                inp = input()
                if inp.lower() == "quit":
                    tile_grid.save()
                    tile_grid.exitProgram()
                elif inp[0].lower() == "f":
                    cord = tile_grid.getCord(inp[1:])
                    tile_grid.flagTile(cord)
                else:
                    cord = tile_grid.getCord(inp)
                    if not cord == None:
                        tile_grid.click(cord)
                    else:
                        print("Enter correct cord: ", end="")
                        continue
                break
            except:
                print("Enter correct cord: ", end="")
                continue
        if tile_grid.getExit():
            print(tile_grid)
            break
            


main()
    