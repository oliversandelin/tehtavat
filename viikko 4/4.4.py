import random
oikealuku = random.randint (1,10)
while True:
    arvaus = float(input("arvaa luku 1-10"))
    if arvaus < oikealuku:
       print("isompi")
    if arvaus > oikealuku:
       print("pienempi")
    if arvaus == oikealuku:
     print("oikein")
     break


