#Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor do meio quando o vetor é ordenado. Certifique-se de que sua função funcione para vetores com um número ímpar de elementos.

def mediana(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(i+1, n):
            if vetor[i] > vetor[j]:
                vetor[i], vetor[j] = vetor[j], vetor[i]
    if n % 2 == 1:
        return vetor[n // 2]
    else:
        return (vetor[n // 2 - 1] + vetor[n // 2]) / 2

vetor = [5, 4, 3, 2, 1]
mediana_vetor = mediana(vetor)
print(mediana_vetor)
