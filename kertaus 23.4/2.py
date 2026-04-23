opiskelijat = {
"john" : ["john", 1, "Engineer"],
"emily" : ["emily", 2, "Artist"],
"Anna" : ["Anna", 2, "PE"]
}
print("johnin vuosiluokka ja emilyn lempiaine", opiskelijat["john"][1], opiskelijat["emily"][2])
opiskelijat["john"][2]="insinöörimatikka"
opiskelijat["Lebron"]=["Lebron",2,"kuvataide"]
del opiskelijat["Anna"]
print(opiskelijat)