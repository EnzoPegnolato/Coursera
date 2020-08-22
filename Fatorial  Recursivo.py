"""A função fatorial(x) recebe como parâmetro um número inteiro e devolve, 
utilizando recursividade, um número inteiro correspondente ao fatorial de x."""

def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x - 1)
