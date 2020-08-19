import random
def  lista_grande(n):
    lista = []
    for i in range(n):
        n = random.randrange(0,1000)
        lista.append(n)
    return lista

