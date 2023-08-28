# 3- Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        calculo_area = self.base * self.altura
        return calculo_area

base_area = 4
altura_area = 6
retangulo = Retangulo(base_area, altura_area)
area_total_retangulo = retangulo.calcular_area()
print(f"A area total do Retangulo é: {area_total_retangulo}")


    