"""Função lista_grande(n), que recebe como parâmetro um número 
inteiro n e devolve uma lista contendo n números inteiros aleatórios."""


import random
def  lista_grande(n):
    lista = []
    for i in range(n):
        n = random.randrange(0,1000)
        lista.append(n)
    return lista

