# Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.
# Solicita um número ao usuário
numero = int(input("Digite um número: "))

print(f'Números pares de 0 até", {numero} :')
for i in range(0, numero + 1, 2):
    print(i)