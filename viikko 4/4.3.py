pienin = None
suurin = None
while True:
    try:
        luku = input("Anna lukuja: ")

        if luku == "":
            break
        luku = float(luku)
        if pienin == None or pienin > luku:
            pienin = luku
        if suurin == None or suurin < luku:
            suurin = luku
    except:
        print("Syöte ei kelpaa")
print(f"Pienin luku oli: {pienin}")
print(f"Suurin luku oli: {suurin}")









