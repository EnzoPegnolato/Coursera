"""A função soma_lista(lista) recebe como parâmetro uma lista de números inteiros e devolve,
usando recursão, um número inteiro correspondente à soma dos elementos desta lista."""


def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])


