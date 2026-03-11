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