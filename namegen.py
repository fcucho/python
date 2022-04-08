import random
#generador de nombres aleatorio
def vowels():
    vlet = ['a', 'e', 'i', 'o', 'u']
    n  = random.randint(0,(len(vlet) - 1))
    return vlet[n]

def consonants():
    vlet = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    n  = random.randint(0,(len(vlet) - 1))
    return vlet[n]


length = int(input("ingrese el largo del nombre"))
nombre = ""
for i in range(0, length):
    if (i % 2 == 1):
        nombre += consonants()
    else:
        nombre += vowels()

print(nombre)