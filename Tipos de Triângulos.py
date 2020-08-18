"""Define a classe Triangulo cujo construtor recebe 3 valores 
inteiros correspondentes aos lados a, b e c de um triângulo.
A classe triângulo também possui um método perimetro, que não 
recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.
Possui, também, um método tipo_lado, que não recebe parâmetros
e devolve uma string dizendo se o triângulo é isósceles (dois lados iguais),
equilátero (todos os lados iguais) e escaleno (todos os lados diferentes) """

class Triangulo():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def  tipo_lado(self):
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return "escaleno"
        elif self.a == self.b and self.a == self.c and self.b == self.c:
            return "equilátero"
        else:
            return "isósceles"

