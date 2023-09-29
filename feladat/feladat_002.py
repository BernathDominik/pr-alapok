# feladat_002
"""
Kérjünk be a billentyűzetről két egész számot és irassuk ki két szám összegét a képernyőre!
"""

szam_1 = int(input("Kérek egy számot:"))
szam_2 = int(input("Kérek egy számot:"))
szam_3 = float (szam_1)
osszeg = szam_1 + szam_2
print(f"A megadott két szám összege: {szam_1 + szam_2}")
print(f"A megadott két szám összege: {osszeg}")
print(f"A szam_1 változó tipusa: {type(szam_1)}")
print(f"A szam_2 változó tipusa: {type(szam_2)}")
print(f"Az osszeg változó tipusa: {type(osszeg)}")
print(f"A szam_3 változó értéke: {szam_3}")
print(f"A szam_3 változó típusa: {type(szam_3)}")
