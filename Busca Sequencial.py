""" A função busca(lista, elemento) busca um determinado elemento em
uma lista e devolve o índice correspondente à posição do elemento encontrado.
Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False. Sem o uso do método Index"""

def busca(lista, elemento):
    b = 0
    for i in lista:
        if i == elemento:
            while b <= len(lista) -1:
                if i == lista[b]:
                    return b
                else:
                    b += 1



    return False

