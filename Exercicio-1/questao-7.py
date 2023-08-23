# Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário. 

valor_limite = int(input("Digite um valor limite para a sequência de Fibonacci: "))

fibonacci = [0, 1]

while fibonacci[-1] + fibonacci[-2] <= valor_limite:
    proximo_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_numero)

print("Sequência de Fibonacci até", valor_limite, ":")
print(fibonacci)
