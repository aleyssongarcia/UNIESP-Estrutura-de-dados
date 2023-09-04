#Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor do meio quando o vetor é ordenado. Certifique-se de que sua função funcione para vetores com um número ímpar de elementos.

def mediana(valor):
    n = len(valor)
    for i in range(n):
        for j in range(i+1, n):
            if valor[i] > valor[j]:
                valor[i], valor[j] = valor[j], valor[i]
    if n % 2 == 1:
        return valor[n // 2]
    else:
        return (valor[n // 2 - 1] + valor[n // 2]) / 2

valor = [5, 4, 3, 2, 1]
mediana_valor = mediana(valor)
print(mediana_valor)
