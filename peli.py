import time
import random

# 1. Tietokanta: Lista, joka sisältää sanakirjoja (kysymys + vastaus)
arvoitukset = [
    {
        "kysymys": "Mikä kastuu, kun se kuivaa?",
        "vastaus": "pyyhe"
    },
    {
        "kysymys": "Mitä enemmän otat, sitä enemmän jätät taaksesi. Mikä se on?",
        "vastaus": "askeleet"
    },
    {
        "kysymys": "Omistat sen, mutta muut käyttävät sitä enemmän kuin sinä itse. Mikä se on?",
        "vastaus": "nimi"
    },
    {
        "kysymys": "Sillä on jalat, mutta se ei kävele. Sillä on selkä, mutta ei selkärankaa. Mikä se on?",
        "vastaus": "tuoli"
    },
    {
        "kysymys": "Mikä kulkee maailman ympäri, mutta pysyy nurkassa?",
        "vastaus": "postimerkki"
    }
]


def pelaa_arvoituspeli():
    pisteet = 0

    print("--- TERVETULOA ARVOITUSPELIIN ---")
    print("Vastaa yhdellä sanalla (perusmuodossa).")
    time.sleep(1)  # Pieni tauko tunnelman luomiseksi

    # 2. Sekoitetaan lista, jotta peli on aina erilainen
    random.shuffle(arvoitukset)

    # 3. Käydään jokainen arvoitus läpi loopilla
    for kierros, arvoitus in enumerate(arvoitukset, start=1):
        print(f"\nKYSYMYS {kierros}:")
        print(arvoitus["kysymys"])

        user_vastaus = input(
            "Vastauksesi: ").lower().strip()  # Muutetaan pieniksi kirjaimiksi ja poistetaan turhat välilyönnit

        # 4. Tarkistetaan vastaus
        # Huom: "in" tarkistaa, löytyykö sana vastauksesta (esim. "Se on pyyhe" -> hyväksytään)
        if arvoitus["vastaus"] in user_vastaus:
            print(">> OIKEIN! Hienosti hoksattu.")
            pisteet += 1
        else:
            print(f">> VÄÄRIN. Oikea vastaus oli: {arvoitus['vastaus']}")

        time.sleep(1)

    # 5. Lopetus
    print("\n-----------------------------")
    print(f"Peli ohi! Sait {pisteet} / {len(arvoitukset)} pistettä.")

    if pisteet == len(arvoitukset):
        print("Täydellinen suoritus! Olet nero!")
    elif pisteet == 0:
        print("Voi ei... Ensi kerralla paremmin!")


# Käynnistys
if __name__ == "__main__":
    pelaa_arvoituspeli()