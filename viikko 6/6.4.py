lista=[]
def tulos(lista):
    summa = sum(lista)
    return summa

while True:
    syote = input("Syötä haluamasi määrä kokonaislukuja, tyhjä syöte pysäyttää loopin: ")
    if syote == "":
        break
    lista.append(int(syote))

print(f"Syötteen summa: {tulos(lista)}")