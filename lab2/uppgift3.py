i = 1 #Count for while
sum = 0 # Summan av alla pakets kostnad
antal_paket = int(input("Hur många paket vill du skicka: "))

# Summerar alla pakets priser
while i <= antal_paket: 
    print("Ange vikt för paket", i, ": ", end="" )
    vikt = float(input(""))
    if vikt < 2 and vikt > 0:
        sum += (vikt*30)
    elif vikt >= 2 and vikt < 6:
        sum += (vikt*28)
    elif vikt >= 6 and vikt < 12:
        sum += (vikt*25)
    else: 
        sum += (vikt*23)
    i+=1
print("Det kommer att kosta", round(sum,1), "Kr") # Skriver ut priset för alla paket