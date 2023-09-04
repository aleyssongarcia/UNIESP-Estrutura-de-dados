import numpy as np
# Criando a Class
class Listasequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
# Cria uma função que imprime a lista
    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range (self.ultima_posicao +1):
                print(i, "-", self.valores[i])
# Insete dados na Lista
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print("Capacidade máxima atingida")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
# Pesquisa dados que estão presentes na Lista
    def pesquisar (self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
# Exclui dados presentes na Lista
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
    
    # ordenar
    def ordenar(self):
        self.valores[:self.ultima_posicao + 1] = np.sort(self.valores[:self.ultima_posicao + 1])


#Criando objeto
x=Listasequencial(5)
#Imprimindo as infomações, inserindo, imprimindo e excluindo.
x.insere(9)
x.insere(5)
x.insere(25)
x.insere(15)
x.insere(55)
x.ordenar()
x.imprime()
print(f'O Valor 25 está no index: ', x.pesquisar(25))
x.excluir(5)
x.imprime()