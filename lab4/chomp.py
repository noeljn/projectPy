import math

class Chomp:

    def __init__(self, x, y): #Makes the board, Size: x*y
        self.board = []
        for i in range(1,x + 1):
            self.board.append([])
            for ii in range(1,y + 1):
                self.board[i - 1].append((i*10 + ii))
        self.board[0][0] = "P"

    def getBoard(self): #Prints out the board
        for i in range(len(self.board)):
            print(self.board[i])

    def eatBoard(self, nbr):  #Input number -> splits the nbr and deletes below and to the right of the nbr
        y = nbr % 10 #splits number into cords
        x = math.floor(nbr/10)
        if y == 1:
            for i in range(x - 1, len(self.board)):
                del self.board[x - 1]
        else:
            for i in range(x - 1, len(self.board)):
                del self.board[i][y-1:len(self.board)]
    
    def checkWin(self): #Check for a win -> by checking if P is the only "number" left
        if self.board == [["P"]]:
            self.getBoard()
            return True
        return False

    def checkNumber(self, nbr): #Checks in a number is in the board
        try:
            for i in range(0, len(self.board)):
                if nbr in self.board[i]:
                    return True
            print("Invalid number")
            return False
        except:
            return False

def main():
    board = Chomp(6,6)
    board.getBoard()
    player = 1

    while True:
        try:
            if(player == 1):
                blocknummer = int(input("Första spelarens tur, välj ett blocknummer: "))
            else:
                blocknummer = int(input("Andra spelarens tur, välj ett blocknummer: "))
            if board.checkNumber(blocknummer) == False:
                continue
        except:
            continue
        board.eatBoard(blocknummer)

        if board.checkWin():
            if player == 1:
                print("Spelet är slut. Vinnare är första spelaren!")
            else:
                print("Spelet är slut. Vinnare är andra spelaren!")
            break

        board.getBoard()
        player = -player

main()