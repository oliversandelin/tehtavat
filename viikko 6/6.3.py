def muunnos(gallonat):
    litrat = gallonat * 3.785
    return round(litrat, 2)

while True:
    syote = float(input("Montako nestegallonaa bensiiniä?: "))
    if syote < 0:
        break
    print(f"Syöttämäsi määrä vastaa {muunnos(syote)} litraa bensiiniä")

