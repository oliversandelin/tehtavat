hinnasto = {"kahvi": 2.50,
            "pulla": 3.00,
            "tee": 2.00,   }
ostoskori =[]
def menu():
    for tuote in hinnasto:
        print(f"{tuote}: {hinnasto[tuote]}€")



def summa():
    yhteensa = 0
    for tuote in hinnasto:
        yhteensa = yhteensa + hinnasto[tuote]
    return yhteensa




while True:
    toiminto = input("Valitse 1 jos haluat menun \n Valitse 2 jos haluat lisätä tilaukseen \n Valitse 3 jos haluat maksaa tilauksen")
    if toiminto not in ["1", "2", "3"]:
        print("Tuntematon toiminto! Yritä uudelleen.")
        continue

    if toiminto == "1":
        menu()
    if toiminto == "2":
        lisa = input("Keerro tuote jonka haluat lisätä")
        ostoskori.append(lisa)

    if toiminto =="3":
        maksettava = summa()
        print("tilauksen loppusumma on", maksettava)
        break
