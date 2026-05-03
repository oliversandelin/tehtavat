while True:
    ika = int(input("anna ikäsi"))
    if ika <15:
        print("ikä ei riitä odota vielä", 15-ika, "vuotta")
        break
    else:
        print("saat katsoa elokuvaa")