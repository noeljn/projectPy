import Tile
import TileGrid

tile_grid = TileGrid.TileGrid(10,10)

def main():
    tile_grid.LoadGrid()
    print(tile_grid)
    print("Input a cord: ")
    while True:
        try:
            inp = input()
            break
        except ValueError:
            print("Enter correct cord: ")
            continue
    tile_grid.GenerateMines(inp)
    tile_grid.addAdjacentTiles()
    tile_grid.CheckMinesNear()
    game()

def game():
    while True:
        print(tile_grid)
        print("Input a cord: ", end="")
        while True:
            try:
                inp = input()
                break
            except ValueError:
                print("Enter correct cord: ", end="")
                continue
        tile_grid.ClickTile(inp)
            


main()
    