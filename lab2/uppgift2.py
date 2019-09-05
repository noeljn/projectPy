#Räknar ut hur mycket ett paket kostar, via en if statment
vikt = float(input("Hur mycket väger paketet: "))
if vikt < 2 and vikt > 0:
    print("Det kommer att kosta ", round(vikt*30,2), "Kr")
elif vikt >= 2 and vikt < 6:
    print("Det kommer att kosta ", round(vikt*28,2), "Kr")
elif vikt >= 6 and vikt < 12:
    print("Det kommer att kosta ", round(vikt*25,2), "Kr")
else: 
    print("Det kommer att kosta ", round(vikt*23,2), "Kr")