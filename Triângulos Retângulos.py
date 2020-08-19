


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

    def retangulo(self):
        if (self.a ** 2) == (self.b ** 2) + (self.c ** 2) or (self.b ** 2) == (self.a ** 2) + (self.c ** 2) or (self.c ** 2) == (self.b ** 2) + (self.a ** 2):
            return True
        else:
            return False
