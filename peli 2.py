import random




def arvaa_numero():
        # 1. Tietokone valitsee satunnaisen luvun väliltä 1-100
        salainen_luku = random.randint(1, 100)
        arvaus = None
        yritykset = 0

        print("Tervetuloa Arvaa Numero peliin! ")
        print("Olen valinnut luvun väliltä 1-100. Yritä arvata se (ei ole 67).")

        # 2. Pelisilmukka: jatkuu kunnes arvaus on oikein
        while arvaus != salainen_luku:
            try:
                # Kysytään pelaajalta syötettä
                syote = input("Anna arvauksesi: ")
                arvaus = int(syote)
                yritykset += 1

                # 3. Tarkistetaan arvaus
                if arvaus < salainen_luku:
                    print("Liian pieni! Yritä uudelleen.")
                elif arvaus > salainen_luku:
                    print("Liian suuri! Yritä uudelleen.")
                else:
                    print(f"Onneksi olkoon! Arvasit oikein {yritykset} yrityksellä!")

            except ValueError:
                print("Virhe: Kirjoita vain numeroita.")


    # Käynnistetään peli
if __name__ == "__main__":
        arvaa_numero()