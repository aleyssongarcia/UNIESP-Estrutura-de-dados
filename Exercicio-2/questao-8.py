# Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado “calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
        total = sum(self.notas)
        media = total / len(self.notas)
        return media

aluno1 = Aluno("Aleysson", [10.0, 9.5, 8.0, 7.5])
media_aluno1 = aluno1.calcular_media()
print(f"A média de {aluno1.nome} é {media_aluno1:.2f}")