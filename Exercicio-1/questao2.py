# Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

try:
    numero = int(input('digite um numero: '))

    if numero % 2 == 0:
        print(f'Numero {numero} é par.')
    else:
        print(f'numero {numero}  impar.')

except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro.")
