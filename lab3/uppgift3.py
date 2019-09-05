import random

dice = int(input("Hur många tärningar? "))
throws = int(input("Hur många kast? "))
count = 0
array = []

while True: #Ska gå tills vi manuelt avbryter loopen
    if count == throws or count == 0: #Ska hända före kasten har börjat och efter alla kast är klara
        if "A" ==  input("Enter för att starta. [A] för att avsluta "):
            break
        else:
            count = 0
    for d in range(0,dice):  #Vi ska bara loopa denna ett vist antal gånger och då är for en bra loop
        array.append(random.randint(1,6))
        print("Tärning", d+1, ":", array[d])
    print("Du fick", array)
    array = []
    count+=1
    if count == throws:
        continue
    elif "n" == input("Vill du kasta igen? [j/n] "):
        count = throws
