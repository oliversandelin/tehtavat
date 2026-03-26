def kuusi(koko):
    print("Tämä on kuusi!")

    for i in range(1, koko + 1):

        valit_alussa = koko - i

        tahdet = i * 2 - 1

        print(" " * valit_alussa + "*" * tahdet)

    print(" " * (koko - 1) + "*")


kuusi(67)