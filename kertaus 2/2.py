luvut = []

while True:

    arvo = int(input("anna arvo"))
    if arvo == 0:
        break

    luvut.append(arvo)

    print(f"lista: {luvut}")

    print(f"lista: {sorted(luvut)}")

