#Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`.

def maximo_minimo(vetor):
    maximo = vetor[0]
    minimo = vetor[0]
    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
        if elemento < minimo:
            minimo = elemento
    return maximo, minimo
vetor = [5, 4, 3, 2, 1]
maximo, minimo = maximo_minimo(vetor)
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
