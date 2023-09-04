#Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o algoritmo de seleção.

def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if vetor[min_index] > vetor[j]:
                min_index = j
        vetor[i], vetor[min_index] = vetor[min_index], vetor[i]
    return vetor