import apparatus

try: #Imports the settings from settings (if there are any)
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

def mainMenu():
    inputNumber = 0
    print("\n1.", vardag.name, "\n2.", kok.name,"\n3. Avsluta\nVälj: ", end="")
    while inputNumber != 3:
        try:    
            inputNumber = int(input()) 
        except ValueError: #Checks for Value error
            print("Välj ett nummer! : ", end="")
            continue
        if inputNumber == 1:
            secMenu(vardag)
        elif inputNumber == 2:
            secMenu(kok)
        elif inputNumber == 3:
            saveSettings()
        else:
            print("Välj ett nummer som finns! : ", end="")
            continue

def secMenu(currentTv): #Handles the second menu
    inputNumber = 0
    while inputNumber != 4: #The menu runs as long as you dont input "4"
        tvInfo(currentTv)
        print("\n\n1. Byt kanal\n2. Sänk ljudvolym\n3. Höj ljudvolym\n4. Gå till huvudmenyn\nVälj: ", end="")
        while True:
            try:
                inputNumber = int(input())
            except ValueError: #Checks for Value errors
                print("Välj ett nummer! : ", end="")
                continue
            if inputNumber == 1: #Handels input from user 
                while True: #Loops until a new kanal has been selected
                    print("Ange kanal nummer: ", end="")
                    try:
                        kanal = int(input())
                        if kanal > 0 and kanal < 100:
                            currentTv.bytKanal(kanal)
                        else:
                            print("Ange en kanal som finns!\n")
                            continue
                        break
                    except ValueError: #Checks for Value errors
                        print("Ange en kanal som finns!\n")
                        continue
            elif inputNumber == 2:
                currentTv.sankVolym()
            elif inputNumber == 3:
                currentTv.hojVolym()
            elif inputNumber == 4:
                mainMenu()
                break
            else:
                print("Välj ett nummer som finns! : ", end="")
                continue

def tvInfo(tv): #Displayes Tv chanal and volym
    print("\n\n" + tv.name, "\nKanal:", tv.getKanal(), "\nLjudvolymen:", tv.getVolym())

def saveSettings(): #Saves settings into settings txt
    f = open("settings.txt", "w+")
    f.write(vardag.getName() + "," + str(vardag.getKanal()) + "," +  str(vardag.getVolym()) + "," + kok.getName() + "," + str(kok.getKanal()) + "," +  str(kok.getVolym()))
    f.close()

mainMenu()