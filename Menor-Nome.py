"""A função menor_nome(nomes)  recebe uma lista de strings
com nome de pessoas como parâmetro e devolve o nome mais
curto presente na lista. A função  ignora espaços antes e
depois dos nomes, além de serem devolvidos com a primeira letra maiúscula e seus
demais caracteres minúsculos, independente de como tenha sido
apresentado na lista passada para a função. Quando houver
mais de um nome com o menor comprimento dentre os nomes na
lista, a função  devolve o primeiro nome com o menor comprimento."""

def menor_nome(nomes):
    lista = []
    for i in nomes:
        a = i.strip()
        b = len(a)
        lista.append(b)
    d = min(lista)
    pos = lista.index(d)
    e = nomes[pos]
    m = e.title().strip()
    return m

