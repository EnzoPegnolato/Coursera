def ordena(lista):

    for i in range(len(lista) - 1):

        for h in range(i + 1,len(lista)):
            if lista[i] > lista[h]:
                lista[i], lista[h] = lista[h],lista[i]
            else:
                pass
    return lista



