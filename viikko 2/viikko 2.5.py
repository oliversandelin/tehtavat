leviska = int(input("anna leviska:"))
naula = int(input("anna naula:") )
luoti = int(input("anna luoti:"))
leviska_maara = leviska*20*32*13.3
naula_maara = naula*32*13.3
luoti_maara = luoti*13.3

massa_g = leviska_maara+naula_maara+luoti_maara
massa_k = int(massa_g//1000)
gramma_loput = massa_g%1000
print(massa_k,"kiloa",massa_g,"grammoi")
