lentoasemat = {}
while True:
    toiminto = input("Valitse \n A: Jos haluat lisätä lentoaseman. \n B: Jos haluat hakea lentoasemaa \n C: jos halaut lopettaa.").upper()
    if toiminto == "C":
        break
    if toiminto == "A":
        icao = input("syota lentoaseman icao:")
        nimi = input("syota lentoaseman nimi:")
        lentoasemat[icao] = nimi
    if toiminto == "B":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")
    else:
        print("virheelinen syote")