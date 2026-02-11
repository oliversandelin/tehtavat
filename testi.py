
sukupuoli = input("Oletko M vai N? ")

if sukupuoli == "M":
    hemogloniarvo_m = int(input("Mikä on sinun hemogloniarvo? "))
    if hemogloniarvo_m < 134: print("alhainen hemoglobiiniarvo")
    elif 134 <= hemogloniarvo_m <= 195: print("Normaalit hemoglobiiniarvo")
    elif hemogloniarvo_m > 195: print("Korkea hemoglobiiniarvo")

if sukupuoli == "N":
    hemogloniarvo_n = int(input("Mikä on sinun hemogloniarvo? "))
    if hemogloniarvo_n < 117: print("alhainen hemoglobiiniarvo")
    elif 117 <= hemogloniarvo_n <= 175: print("Normaalit hemoglobiiniarvo")
    elif hemogloniarvo_n > 175: print("Korkea hemoglobiiniarvo")

