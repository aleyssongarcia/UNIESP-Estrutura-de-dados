# Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'. 

entrada = input("Digite uma lista de nomes separados por vírgula: ")

nomes = entrada.split(',')

nomes_com_A = []

for nome in nomes:
    nome = nome.strip()
    if nome.startswith('A') or nome.startswith('a'):
        nomes_com_A.append(nome)

print("Nomes que começam com 'A':")
for nome in nomes_com_A:
    print(nome)
