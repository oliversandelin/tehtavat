import random

nopan_tahkot = int(input("Kuinka monisivuinen noppa heitetään?: "))
def nopan_heitto():
    return random.randint(1, nopan_tahkot)

tulos = 0

while tulos != nopan_tahkot:
    tulos = nopan_heitto()
    print(tulos)








