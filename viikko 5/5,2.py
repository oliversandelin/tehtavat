luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luku = int(syote)
    luvut.append(luku)

luvut.sort(reverse=True)

print("Viisi suurinta lukua ovat:")
for luku in luvut[:5]:
    print(luku)