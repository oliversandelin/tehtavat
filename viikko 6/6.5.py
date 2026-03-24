def karsinta(lista):
    parilliset=[]
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

while True:
    syote=int(input("syötä luku, tyhjä lopettaa: "))
    if syote == "":
        break
print(karsinta(syote))