# Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número. Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.

def terceiro_maior(valor):
    unicos = list(set(valor))
    primeiro = segundo = terceiro = float('-inf')
    for elemento in unicos:
        if elemento > primeiro:
            terceiro = segundo
            segundo = primeiro
            primeiro = elemento
        elif elemento > segundo:
            terceiro = segundo
            segundo = elemento
        elif elemento > terceiro:
            terceiro = elemento
    return terceiro

valor = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
terceiro_maior_numero = terceiro_maior(valor)
print(terceiro_maior_numero)
