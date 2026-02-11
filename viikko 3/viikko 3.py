import math
kuhan_mitta = float(input("anna kuhan mitta"))
alamittaisuus = (37-kuhan_mitta)

if kuhan_mitta < 37:print(alamittaisuus,"CM liian lyht laske kuha takaisin järveen")
if kuhan_mitta > 37:print("Onnittelut et ole täysin turha")

hytin_luokka = input("Mikä on sinun hytti luokkasi?: LUX, A, B, C")
if hytin_luokka == "LUX": print("LUX on parvekkeellinen hytti yläkannella.")
elif hytin_luokka == "A": print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytin_luokka == "B": print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytin_luokka == "C": print("C on ikkunaton hytti autokannen alapuolella.")
else: print("Virheellinen hyttiluokka")



