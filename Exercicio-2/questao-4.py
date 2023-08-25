# Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente métodos “depositar” e “sacar” para manipular o saldo

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}"
        else:
            return "O valor do depósito deve ser maior que zero."

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                return f"Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}"
            else:
                return "Saldo insuficiente para realizar o saque."
        else:
            return "O valor do saque deve ser maior que zero."

conta = ContaBancaria("Aleysson", 4000) 

print(conta.depositar(500))
print(conta.sacar(200)) 