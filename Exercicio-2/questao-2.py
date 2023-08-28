# 2- Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método  chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def detalhes(self):
        return f" Titulo: {self.titulo}, Autor: {self.autor}"
    
livro_1 = Livro("Harry Potter e a Pedra Fisolofal", "JK")
detalhes_livro_1 = livro_1.detalhes()
print(detalhes_livro_1)

livro_2 = Livro("O homem mais inteligente da Historia", "Augusto Cury")
detalhes_livro_2 = livro_2.detalhes()
print(detalhes_livro_2)