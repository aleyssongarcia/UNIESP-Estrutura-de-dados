
# Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida, conte quantos números pares e quantos números ímpares existem no vetor ordenado.

def ordenar_contar(valor):
    valor_ordenado = []
    while valor:
        maximo = valor[0]
        for elemento in valor:
            if elemento > maximo:
                maximo = elemento
        valor_ordenado.append(maximo)
        valor.remove(maximo)
    pares = 0
    impares = 0
    for elemento in valor_ordenado:
        if elemento % 2 == 0:
            pares += 1
        else:
            impares += 1
    return valor_ordenado, pares, impares

valor = [5, 4, 3, 2, 1]
valor_ordenado, pares, impares = ordenar_contar(valor)
print(f"valor ordenado: {valor_ordenado}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")

