import apparatus

try:
    f = open("settings.txt", "r")
    if f.mode == "r":
        content = f.read()
        content = content.split(",")
        vardag = apparatus.tv("Vardagsrums TV", int(content[1]), int(content[2]))
        kok = apparatus.tv("Köks TV", int(content[4]), int(content[5]))
    else:
        vardag = apparatus.tv("Vardagsrums TV")
        kok = apparatus.tv("Köks TV")
except:
    vardag = apparatus.tv("Vardagsrums TV")
    kok = apparatus.tv("Köks TV")


def main():
    mainMenu()

def mainMenu():
    inputNumber = 0
    print("1.", vardag.name, "\n2.", kok.name,"\n3. Avsluta")
    while inputNumber != 3:
        try:
            print("Välj: ", end="")
            inputNumber = int(input())
            if inputNumber == 1:
                secMenu(vardag)
            elif inputNumber == 2:
                secMenu(kok)
            elif inputNumber == 3:
                saveSettings()
            else:
                print("Välj ett nummer som finns!\n")
                continue
        except:
            print("Välj ett nummer!\n")
            continue

def secMenu(currentTv):
    inputNumber = 0
    while inputNumber != 4:
        tvInfo(currentTv)
        print("\n\n1. Byt kanal\n2. Sänk ljudvolym\n3. Höj ljudvolym\n4. Gå till huvudmenyn\nVälj: ", end="")
        while True:
            try:
                inputNumber = int(input())
                print(inputNumber)
                if inputNumber == 1:
                    while True:
                        print("Ange kanal nummer: ", end="")
                        try:
                            kanal = int(input())
                            if kanal > 0 and kanal < 100:
                                currentTv.bytKanal(kanal)
                            else:
                                print("Ange en kanal som finns!\n")
                                continue
                            break
                        except:
                            print("Ange en kanal som finns!\n")
                            continue
                elif inputNumber == 2:
                    currentTv.sankVolym()
                elif inputNumber == 3:
                    currentTv.hojVolym()
                elif inputNumber == 4:
                    mainMenu()
                else:
                    print("Välj ett nummer som finns!\nVälj: ", end="")
                    continue
                break
            except:
                print("Välj ett nummer!\nVälj: ", end="")
                continue

def tvInfo(tv):
    print("\n\n" + tv.name, "\nKanal:", tv.getKanal(), "\nLjudvolymen:", tv.getVolym())


def saveSettings():
    f = open("settings.txt", "w+")
    f.write(vardag.getName() + "," + str(vardag.getKanal()) + "," +  str(vardag.getVolym()) + ",")
    f.write(kok.getName() + "," + str(kok.getKanal()) + "," +  str(kok.getVolym())) 
    f.close()

main()