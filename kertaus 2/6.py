def yhteenlasku(a,b):
    return a+b
def vahennyslasku(a,b):
    return a-b
def kertolasku(a,b):
    a*b
def jakolasku(a,b):
    if b==0:
        return "nollalla ei voi jakaa"
    return a/b






print(("\n-----Tervettuloa käyttämään laskinta-----"))
while True:
    toiminto = input("Valitse \n A:Yhteenlasku \n B: Vähennyslasku, \n C: Kertolasku \n D: Jakolasku \n tai X: lopettaaksesi: ").upper()

    if toiminto == "X":
        print("Lopetetaan...")
        break

    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))

    if toiminto == "A":
        print("Tulos:", luku1 + luku2)
    elif toiminto == "B":
        print("Tulos:", luku1 - luku2)
    elif toiminto == "C":
        print("Tulos:", luku1 * luku2)
    elif toiminto == "D":
        print("Tulos:", luku1 / luku2)
    else:
        print("Tuntematon toiminto!")