import random

maara = int(input("montako noppaa:"))
summa = 0

for noppa in range(maara):
    heitto = random.randint(1,6)
    print(heitto)
    summa += heitto
    print("summaksi tuli",summa)
