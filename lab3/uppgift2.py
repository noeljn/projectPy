rader = int(input("Ange ett tal mellan 1-9: "))
kolumner = int(input("Ange ett till tal mellan 1-9: "))

count_rader = 1
count_kolumner = 1

print("",end="   ")
for x in range(1,kolumner + 1):
    print("{0:<2d}".format(x), end=" ")

while count_rader <= rader:
    print("")
    print(count_rader, end=": ")
    count_kolumner = 1
    while count_kolumner <= kolumner:
        tal = count_kolumner*count_rader
        print("{0:<2d}".format(tal), end=" ")
        count_kolumner += 1
    count_rader += 1
print("")
    