# -*- coding: utf-8 -*-

print("Izdelava jedilnega lista")

meni = {}
meni_file = open("meni.txt", "w+")

meni_file.write("JEDILNI LIST" + "\n" + "\n")

while True:
    jed = raw_input("Prosim, vnesite ime jedi: ")
    cena = raw_input("Vnesite ceno jedi: ")
    print("Jed: " + jed + " " + cena + " €")

    meni_file.write(jed + "  " + cena + "€" + "\n")

    nadaljuj = raw_input("Želite dodati še kakšno jed? Da/Ne ")

    if nadaljuj.lower() == "ne":
        break

meni_file.close()

print("Konec")