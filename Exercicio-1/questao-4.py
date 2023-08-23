# Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.
def calcular_media_pares(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]
    
    if len(numeros_pares) == 0:
        return 0
    
    soma_pares = sum(numeros_pares)
    media = soma_pares / len(numeros_pares)
    return media

entrada = input("Digite uma lista de números separados por espaços: ")

lista_numeros = [int(num) for num in entrada.split()]

media_pares = calcular_media_pares(lista_numeros)
print(f"A média dos números pares é: {media_pares}")