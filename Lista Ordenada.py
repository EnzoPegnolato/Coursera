"""A função ordenada(lista) recebe uma lista com números inteiros como parâmetro
e devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada."""


def  ordenada(lista):
    x = sorted(lista)
    a = 0
    for i in lista:
        if i != x[a]:
            return False

        else:
            a += 1
            return True



