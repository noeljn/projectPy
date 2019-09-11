import apparatus

def main():
    vardag = apparatus.tv("Vardagsrums TV")
    kok = apparatus.tv("Köks TV")

    mainMenu(vardag, kok)

def mainMenu(tv1,tv2):
    inputNumber = 0
    print("1.", tv1.name, "\n2.", tv2.name,"\n3. Avsluta")
    while inputNumber != 3:
        inputNumber = int(input("Välj: "))
        if inputNumber == 1:
            secMenu(tv1,tv2,tv1)
        elif inputNumber == 2:
            secMenu(tv1,tv2,tv2)
        elif inputNumber == 3:
            die()
        
def tvInfo(tv):
    print(tv.name, "\nKanal:", tv.getKanal(), "\nLjudvolymen:", tv.getVolym())

def secMenu(tv1,tv2,currentTv):
    inputNumber = 0
    
    while inputNumber != 4:
        tvInfo(currentTv)
        print("\n\n1. Byt kanal\n2. Sänk ljudvolym\n3. Höj ljudvolym\n4. Gå till huvudmenyn\n")
        inputNumber = int(input("Välj: "))
        if inputNumber == 1:
            currentTv.bytKanal(int(input("Ange kanal nummer: ")))
        elif inputNumber == 2:
            currentTv.sankVolym()
        elif inputNumber == 3:
            currentTv.hojVolym()
        elif inputNumber == 4:
            mainMenu(tv1,tv2)

def die():
    print("does som cool shit")

     

main()