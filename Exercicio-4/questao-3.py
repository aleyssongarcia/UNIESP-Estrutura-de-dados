#Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`.

def maximo_minimo(valor):
    maximo = valor[0]
    minimo = valor[0]
    for elemento in valor:
        if elemento > maximo:
            maximo = elemento
        if elemento < minimo:
            minimo = elemento
    return maximo, minimo
valor = [5, 4, 3, 2, 1]
maximo, minimo = maximo_minimo(valor)
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
