# 7- Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método chamado “detalhes” que retorna uma string com as informações do carro.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano do Modelo: {self.ano}"
    
carro = Carro("HB20", "Evolution 1.0", 2023)
print(carro.detalhes())