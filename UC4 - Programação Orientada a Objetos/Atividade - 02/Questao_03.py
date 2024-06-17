class Circunferencia():
    def __init__(self, raio):
        self.raio = float(raio)
    def area(self):
        pi = 3.14159265358979323846
        a = pi * raio ** 2
        return a
    def perimetro(self):
        pi = 3.14159265358979323846
        p = 2 * pi * raio
        return p

class Triangulo():
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)
    # def altura():
    #     altura = 1/2 
    def area(self):
        area = (self.base * self.altura) / 2
        return area
    def perimetro(self, lado):
        perimetro = 3 * lado
        return perimetro
class Quadrado():
    def __init__(self, lado):
        self.lado = float(lado)
    def area(self, lado):
        area = self.lado ** 2
        return area
    def perimetro(self, lado):
        perimetro = 4 * self.lado
        return perimetro
    
    
# Tests Quadrado
lado = float(input("\n▸ Insira o lado do quadrado: "))
quad = Quadrado(lado)
print(f"▹ A area do quadrado é:", quad.area(lado))

# Tests Circulo
raio = float(input("▸ Insira o raio da circunferência: "))
cir = Circunferencia(raio)
print("▹ Área da circunferência:", cir.area())
print("▹ Perímetro da circunferência:", cir.perimetro())

# Tests Triangulo
base = float(input("▸ Insira a base do triângulo: "))
altura = float(input("▸ Insira a altura do triângulo: "))
tri = Triangulo(base, altura)
print("▹ Área do triângulo:", tri.area())
lado = float(input("\n▸ Insira o lado do triângulo: "))
print("▹ Perímetro do triângulo:", tri.perimetro(lado))


