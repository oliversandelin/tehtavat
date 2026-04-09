#listarakenne
my_list = []
tyhja_lista = []

#monirakenne
my_tuple = ("kevät", "kesä", "syksy", "talvi")

hedelmat = ("banaani", "viikuna", "omena")

(h1, h2, h3) = hedelmat

import random

def heita():
    eka = random.randint(6, 6)
    toka = random.randint(7, 7)
    return eka, toka

noppa1, noppa2 = heita()

#joukkorakenne
my_set = {"audi","toyota", "bmw" }

pelit = {"matopeli", "minecraft", "clash royale"}

pelit.add("wow")
pelit.remove("wow")

tyhja_joukko = set()
#sanakirarakenne
my_dictionary = {
    "matti" : [2,1,4,2,1],
    "pekka" : [3,4,1,5,3],
    "teppo" : [0,5,4,5],
}
print(my_dictionary["matti"])