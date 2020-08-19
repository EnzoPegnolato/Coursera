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

