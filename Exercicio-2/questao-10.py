# 10- Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário do funcionário. 

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self):
        porcento = (self.salario*0.15)
        aumento = porcento + self.salario
        return f"{self.nome}, que ocupa o cargo de {self.cargo}, teve seu salario de {self.salario}, atualizado com o reajuste de 15% para {aumento:.2f}"


funcionario_aumento = Funcionario("Aleysson", 5800, "Engenherio de Dados")
print(funcionario_aumento.aumentar_salario())