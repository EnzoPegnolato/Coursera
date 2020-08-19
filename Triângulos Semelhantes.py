""" Define a classe Triangulo cujo construtor recebe 3 valores 
    inteiros correspondentes aos lados a, b e c de um triângulo.
    Métodos dentro da classe: 
    * def perimetro() = Não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo
    * def tipo_lado() = Não recebe parâmetros e devolve uma string dizendo se o triângulo é isósceles (dois lados iguais)  
      equilátero (todos os lados iguais) e escaleno (todos os lados diferentes).
    * def retangulo() = Não recebe parâmetro e retorna se o triângulo é retângulo ou não.
    * def semelhantes() = Recebe um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro."""


class Triangulo():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return "escaleno"
        elif self.a == self.b and self.a == self.c and self.b == self.c:
            return "equilátero"
        else:
            return "isósceles"

    def retangulo(self):
        if (self.a ** 2) == (self.b ** 2) + (self.c ** 2) or (self.b ** 2) == (self.a ** 2) + (self.c ** 2) or (self.c ** 2) == (self.b ** 2) + (self.a ** 2):
            return True
        else:
            return False

    def semelhantes(self,triangulo):
        if self.tipo_lado() == triangulo.tipo_lado():
            return True
        else:
            return False






