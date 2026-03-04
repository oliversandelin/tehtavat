from math import sqrt

while True:

    luku = int(input("luku"))
    if  luku <0:
        print("virheellinen luku")
    elif luku == 0:
        break
    else: print(sqrt(luku))


