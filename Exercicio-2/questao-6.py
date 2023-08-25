# Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        total = self.preco*self.quantidade
        return f"O produto: {self.nome}, levando a quantidade: {self.quantidade}, custa: {total:.2f}"
    

valor_total_produto = Produto("Caneta Big Azul", 2.99, 5)

print(valor_total_produto.calcular_total())