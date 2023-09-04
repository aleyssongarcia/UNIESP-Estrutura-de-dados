# Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número. Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor. 

def segundo_menor(valor):
    unicos = list(set(valor))
    minimo = float('inf')
    segundo_minimo = float('inf')
    for elemento in unicos:
        if elemento < minimo:
            segundo_minimo = minimo
            minimo = elemento
        elif elemento < segundo_minimo:
            segundo_minimo = elemento
    return segundo_minimo

valor = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
segundo_menor_numero = segundo_menor(valor)
print(segundo_menor_numero)
