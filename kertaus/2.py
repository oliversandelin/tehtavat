tuntipalkka = float(input("tuntipalkka: "))
print("tuntipalkka", tuntipalkka)
tunnit = float(input("tunnit: "))
print("tunnit", tunnit)


päivä = input("päivä")
print("päivä",päivä)
if päivä == "sunnuntai" or päivä == "Sunnuntai":
    spalkka = tuntipalkka*tunnit*2
    print("päivän palkka", spalkka)

else:
    palkka = tuntipalkka*tunnit
    print("päivän palkka", palkka)

