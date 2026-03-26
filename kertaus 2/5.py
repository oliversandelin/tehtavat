def suurin_arvo(luku1, luku2, luku3):
    suurin = max(luku1, luku2, luku3)
    return suurin

eka = float(input("anna ensimmäinen luku"))
toka = float(input("anna toinen luku"))
kolmas = float(input("anna kolmas"))

vastaus = suurin_arvo(eka, toka, kolmas)

print(f"suurin on {vastaus}")