# 1- Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado “calcular_area” que retorna a área do círculo. 

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        pi = 3.14
        area = pi * (self.raio ** 2)
        return area


raio_do_circulo = 5
circulo = Circulo(raio_do_circulo)
area_do_circulo = circulo.calcular_area()

print(f"A área do círculo com raio {raio_do_circulo} é {area_do_circulo}")
