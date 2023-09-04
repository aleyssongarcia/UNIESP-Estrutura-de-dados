#Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o algoritmo de seleção.

def selecao(valor):
    n = len(valor)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if valor[min_index] > valor[j]:
                min_index = j
        valor[i], valor[min_index] = valor[min_index], valor[i]
    return valor