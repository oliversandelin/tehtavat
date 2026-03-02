import random

piste_maara = int(input("Montako pistettä haluat?: "))

kierros = 0
osumat = 0

while kierros < piste_maara:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2+y**2 < 1:
        osumat = osumat + 1

    kierros = kierros + 1

pii_likiarvo = 4 * osumat / piste_maara

print(f"Piin likiarvo {piste_maara} pisteellä on: {pii_likiarvo}")

