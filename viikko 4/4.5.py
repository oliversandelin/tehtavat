
käyttäjätunnus = "python"
salasana = "rules"
q=5
while  q>0:
   salasana1 = input("syötä salasana")
   käyttis = input("suötä käyttäjätunnus")

   if salasana1 == salasana and käyttis==käyttäjätunnus:
       print("oikein")
       break
   else:
       q-=1
       if q > 0:
           print(f"kirjautumistiedot syötettiin väärin. {q} yritystä jäljellä")
       if q==0:
           print("pääsy evätty")
           break

