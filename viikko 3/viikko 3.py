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


sukupuoli = input("Oletko M vai N? ")
arvo = int(input("Mikä on sinun hemoglobiiniarvo? "))

if sukupuoli == "M" and arvo < 134: print("alhainen hemoglobiiniarvo")
elif sukupuoli == "M" and 134 <= arvo <= 195: print("Normaalit hemoglobiiniarvo")
elif sukupuoli == "M" and arvo > 195: print("Korkea hemoglobiiniarvo")

if sukupuoli == "N" and arvo < 117: print("alhainen hemoglobiiniarvo")
elif sukupuoli == "N" and 117 <= arvo <= 175: print("Normaalit hemoglobiiniarvo")
elif sukupuoli == "N" and arvo > 175: print("Korkea hemoglobiiniarvo")

vuosiluku = int(input("anna vuosiluku"))
if vuosiluku > 0:
    if (vuosiluku % 4 == 0 and vuosiluku % 100!=0) or (vuosiluku % 400 == 0):
        print(vuosiluku,"on karkaus vuosi")
    else:
        print(vuosiluku,"ei ole karkaus vuosi")


