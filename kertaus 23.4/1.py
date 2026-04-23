ihmiset = {
    "john":["john", 30, "engineer"],
    "emily":["emily",25, "artist"],
    "anna": ["anna", 22, "student"],
}
print("johnin nimi ja ikä:", ihmiset["john"][0], ihmiset["john"][1])
ihmiset["emily"][2] = "teacher"
ihmiset["James"] = ["james", 41, "Basketball"]
ihmiset["sophie"] = ["sophie", 35, "doctor"]
del ihmiset["sophie"]
print(ihmiset)