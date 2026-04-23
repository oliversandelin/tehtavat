try:
    numero = int(input("Anna numero: "))
    jako = 10 / numero
    print("tulos on", jako)
except ZeroDivisionError:
    print("virhe nollalla ei voi jakaa")

except ValueError:
    print("ei vohka jakaa")
finally:
    print("tämä ajetaan aina")

print("ohjelma suoritettu")