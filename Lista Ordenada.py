def  ordenada(lista):
    x = sorted(lista)
    a = 0
    for i in lista:
        if i != x[a]:
            return False

        else:
            a += 1
            return True



