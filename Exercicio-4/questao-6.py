
# Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida, conte quantos números pares e quantos números ímpares existem no vetor ordenado.

def ordenar_contar(vetor):
    vetor.sort(reverse=True)
    pares = 0
    impares = 0
    for elemento in vetor:
        if elemento % 2 == 0:
            pares += 1
        else:
            impares += 1
    return vetor, pares, impares

vetor = [5, 4, 3, 2, 1]
vetor_ordenado, pares, impares = ordenar_contar(vetor)
print(f"Vetor ordenado: {vetor_ordenado}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
