import math

def laske_yksikköhinta(halkaisija_cm, hinta_euro):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala_m2 = math.pi * (sade_m ** 2)
    yksikköhinta = hinta_euro / pinta_ala_m2
    return yksikköhinta

halkaisija1 = float(input("Anna 1. pizzan halkaisija (cm): "))
hinta1 = float(input("Anna 1. pizzan hinta (€): "))

halkaisija2 = float(input("Anna 2. pizzan halkaisija (cm): "))
hinta2 = float(input("Anna 2. pizzan hinta (€): "))

tulos1 = laske_yksikköhinta(halkaisija1, hinta1)
tulos2 = laske_yksikköhinta(halkaisija2, hinta2)

print(f"1. pizzan yksikköhinta: {tulos1:.2f} €/m²")
print(f"2. pizzan yksikköhinta: {tulos2:.2f} €/m²")

if tulos1 < tulos2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif tulos2 < tulos1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat samanarvoisia.")