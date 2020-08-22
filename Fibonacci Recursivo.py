"""A função fibonacci(n) recebe como parâmetro um número inteiro e devolve, utilizando 
recursividade, um número inteiro correspondente ao n-ésimo elemento da sequência de Fibonacci."""


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
