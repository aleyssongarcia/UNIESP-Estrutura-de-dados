# Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que serve como chave para realizar a ordenação crescente ou decrescente. 
def ordenar(valor, crescente=True):
    n = len(valor)
    for i in range(n):
        for j in range(i+1, n):
            if (valor[i] > valor[j] and crescente) or (valor[i] < valor[j] and not crescente):
                valor[i], valor[j] = valor[j], valor[i]
    return valor

valor = [5, 4, 3, 2, 1]
valor_ordenado = ordenar(valor, crescente=True)
print(valor_ordenado)

valor = [1, 2, 3, 4, 5]
valor_ordenado = ordenar(valor, crescente=False)
print(valor_ordenado)
