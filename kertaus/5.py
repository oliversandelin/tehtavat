while True:
    toiminto = input("Valitse (plussa,miinus, kerto, jako) tai 'lopeta' lopettaaksesi: ")

    if toiminto == "lopeta":
        print("Lopetetaan...")
        break

    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))

    if toiminto == "plussa":
        print("Tulos:", luku1 + luku2)
    elif toiminto == "miinus":
        print("Tulos:", luku1 - luku2)
    elif toiminto == "kerto":
        print("Tulos:", luku1 * luku2)
    elif toiminto == "jako":
        print("Tulos:", luku1 / luku2)
    else:
        print("Tuntematon toiminto!")
