#Räknar ut bränsleförbrukning för en bil, genom att använda des körsträcka och förbrukat bränsle

km = float(input("Ange körsträcka i km: "))
bransle = float(input("Ange förbrukat bränsle i liter: "))

print("Bränsleförbrukningen för bilen är ", round((bransle*100)/km,3) , "l/100km")