farenheit = float(input("anna farenheit"))

tila = (farenheit - 32)*5/9
print(tila)

sekuntti = float(input("anna sekuntti"))
tunti = sekuntti//3600
minuutit = (sekuntti%3600)//60
sekunnit = sekuntti%60
print({tunti},{minuutit},{sekunnit})