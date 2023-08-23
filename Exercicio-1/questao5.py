# Faça um programa que leia uma lista de números e retorne a média dos números pares.


# Solicita ao usuário que insira uma lista de números separados por espaço
entrada = input("Digite uma lista de números separados por espaço: ")

# Converte a entrada em uma lista de inteiros
lista_numeros = [int(numero) for numero in entrada.split()]

# Filtra os números pares e calcula a média
numeros_pares = [numero for numero in lista_numeros if numero % 2 == 0]
media = sum(numeros_pares) / len(numeros_pares) if numeros_pares else "Não há números pares na lista."

# Exibe o resultado
print("A média dos números pares é:", media)