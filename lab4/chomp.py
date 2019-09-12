import math

class Chomp:

    def __init__(self, x, y): #Makes the board; size: x*y
        self.board = []
        for i in range(1,x + 1):
            self.board.append([])
            for ii in range(1,y + 1):
                self.board[i - 1].append((i*10 + ii))
        self.board[0][0] = "P "

    def getBoard(self): #Prints out the board
        for i in range(len(self.board)):
            print(" ".join(map(str, self.board[i]))) #Uses map to construct one big string

    def eatBoard(self, nbr):  #Input number -> splits the nbr into cords -> Deletes everyhting to the right and below of that cord
        y = nbr % 10 
        x = math.floor(nbr/10)

        for i in range(x - 1, len(self.board)):
            del self.board[i][y-1:len(self.board)]
    
    def checkWin(self): #Check for a win -> by checking if P is the only "number" left
        totalLen = 0 #if the total len of all lists == 1 -> P must be the only piece left
        for i in range(0, len(self.board)):
            totalLen += int(len(self.board[i]))
        if totalLen == 1:
            self.getBoard()
            return True
        return False

    def checkNumber(self, nbr): #Checks if a number is on the board
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
    player = 1 #Keep tab on whos turn it is

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