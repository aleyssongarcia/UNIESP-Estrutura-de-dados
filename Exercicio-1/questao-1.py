# 1 - Faça um programa que calcule a media de tres numros inseridos pelo usuario.

soma = 0

for i in range(3):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / 3

print(f"A média dos números é: {media}")

# ou a maneira abaixo tambem pode ser utilizado, sem a otimização.

nota1 = float(input('Digite a Primeira nota: '))
nota2 = float(input('Digite a Segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print(f'Sua media das notas {nota1}, {nota2}, {nota3} è {media}')