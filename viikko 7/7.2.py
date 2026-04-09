nimet = set()

while True:
    n = input("anna nimi")
    if n == "":
        break
    if n in nimet:
        print("aiemmin syötetty nimi")
    else:
        print("uusi nimi")
        nimet.add(n)
print("\nSyötetyt nimet:")
for n in nimet:
    print(n)
