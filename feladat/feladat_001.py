# feladat_001
'''
Kérjük be a billentyűzetről a nevünket, és irassuk ki a képernyőre!
A billentyűről minidg szöveget (string-et) olvasunk be!
type(változó) --- visszaadja a változó tipusát
'''
vnev = input("Kérek egy vezetéknevet: ")
knev = input("Kérek egy keresztnevet: ")
print(f"A megadott név a következő: {vnev} {knev}")

print(f"A vnev változó tipusa: {type(vnev)}")
print(f"A vnev változó tipusa: {type(knev)}")


