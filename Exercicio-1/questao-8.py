# Faça um programa que determine se um número é primo ou não. 
 
numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print("O número não é primo.")
else:
    divisores = 0

    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            divisores += 1
            break

    if divisores == 0:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
