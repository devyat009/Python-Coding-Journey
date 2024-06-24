# Classe Livro: 
#     Atributos: título, autor, ano de publicação, status de empréstimo. 
#     Métodos: 
#     informacoes(): exibe as informações do livro. 
#     emprestar(): marca o livro como emprestado. 
#     devolver(): marca o livro como devolvido. 

from Biblioteca import Biblioteca # Importa a biblioteca
class Livro(Biblioteca):
    lista_de_livros = [] # Lista dos livros
    
    def __init__(self, autor, titulo, ano_publicacao, status=False):
        super().__init__()
        self.autor = autor
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.status = status
        Livro.lista_de_livros.append(self)
    
    def informacoes(self):
        for livro in Livro.lista_de_livros:  # Corrigido para usar Livro.lista_de_livros
            print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}, Status: {"Emprestado" if livro.status else "Disponível"}')

    def emprestar(self):
        pass
    def devolver(self):
        pass
b = Biblioteca()
livro1 = Livro('Alin Habbei', 'Aprenda a pilotar um avião até novembro', 2001)
livro1.informacoes()
