Kirjasto = {
    "HP": ["JK",2001,"fantasia"],
    "Munkki": ["Saulus",2007,"kauhu"]
}
print(Kirjasto,["HP"][0], Kirjasto["Munkki"][2])
Kirjasto["Munkki"][2]="Python"
Kirjasto["Saulus"]=["Saulus",2025,"kauhu"]
del Kirjasto["Munkki"]
print(Kirjasto)