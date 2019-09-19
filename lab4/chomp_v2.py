import math

def main():
    board = makeList(6,6)
    printBoard(board)
    player = 1 #Keep tab on whos turn it is

    while True:
        try:
            if(player == 1):
                blocknummer = int(input("Första spelarens tur, välj ett blocknummer: "))
            else:
                blocknummer = int(input("Andra spelarens tur, välj ett blocknummer: "))
            if checkNumber(board, blocknummer) == False:
                continue
        except:
            continue
        board = eatBoard(board, blocknummer)

        if checkWin(board):
            if player == 1:
                print("Spelet är slut. Vinnare är första spelaren!")
            else:
                print("Spelet är slut. Vinnare är andra spelaren!")
            break

        printBoard(board)
        player = -player

def makeList(x,y):
    board = []
    for i in range(1,x + 1):
        board.append([])
        for ii in range(1,y + 1):
            board[i - 1].append((i*10 + ii))
    board[0][0] = "P "
    return board

def printBoard(board): #Prints out the board
        for i in range(len(board)):
            print(" ".join(map(str, board[i]))) #Uses map to construct one big string

def eatBoard(board, nbr):  #Input number -> splits the nbr into cords -> Deletes everyhting to the right and below of that cord
    y = nbr % 10 
    x = math.floor(nbr/10)

    for i in range(x - 1, len(board)):
        del board[i][y-1:len(board)] 
    return board
    
def checkWin(board): #Check for a win -> by checking if P is the only "number" left
    totalLen = 0 #if the total len of all lists == 1 -> P must be the only piece left
    for i in range(0, len(board)):
        totalLen += int(len(board[i]))
    if totalLen == 1:
        printBoard(board)
        return True
    return False

def checkNumber(board, nbr): #Checks if a number is on the board
    try:
        for i in range(0, len(board)):
            if nbr in board[i]:
                return True
        print("Invalid number")
        return False
    except:
        return False



main()