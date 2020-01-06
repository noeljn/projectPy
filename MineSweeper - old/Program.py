import Tile
import TileGrid

tile_grid = TileGrid.TileGrid(5,5,3)

def main():
    tile_grid.LoadGrid()
    print(tile_grid)
    print("Input a cord: ", end="")
    while True:
        try:
            inp = input()
            if tile_grid.CheckInput(inp):
                print("Enter correct cord: ", end="")
                continue
            break
        except ValueError:
            print("Enter correct cord: ")
            continue
    tile_grid.addAdjacentTiles()
    tile_grid.GenerateMines(inp)
    
    game()

def game():
    while True:
        print(tile_grid)
        print("Input a cord: ", end="")
        while True:
            try:
                inp = input()
                if tile_grid.CheckInput(inp):
                    print("Enter correct cord: ", end="")
                    continue
                break
            except:
                print("Enter correct cord: ", end="")
                continue
        tile_grid.ClickTile(inp)    


main()
    