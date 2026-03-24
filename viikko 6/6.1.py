import random

def nopan_heitto():
    return random.randint(1, 6)

tulos = 0

while tulos != 6:
    tulos = nopan_heitto()
    print(tulos)