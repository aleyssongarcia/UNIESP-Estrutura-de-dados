# Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que serve como chave para realizar a ordenação crescente ou decrescente. 
def ordenar(vetor, crescente=True):
    n = len(vetor)
    for i in range(n):
        for j in range(i+1, n):
            if (vetor[i] > vetor[j] and crescente) or (vetor[i] < vetor[j] and not crescente):
                vetor[i], vetor[j] = vetor[j], vetor[i]
    return vetor

vetor = [5, 4, 3, 2, 1]
vetor_ordenado = ordenar(vetor, crescente=True)
print(vetor_ordenado)

vetor = [1, 2, 3, 4, 5]
vetor_ordenado = ordenar(vetor, crescente=False)
print(vetor_ordenado)
