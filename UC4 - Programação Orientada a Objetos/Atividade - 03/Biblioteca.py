# Classe Biblioteca: 

#     Atributos: lista de livros disponíveis, lista de clientes cadastrados. 
#     Métodos: 
#     adicionar_livro(livro): adiciona um livro à lista de livros disponíveis. 
#     remover_livro(livro): remove um livro da lista de livros disponíveis. 
#     listar_livros(): lista todos os livros disponíveis na biblioteca. 
#     registrar_cliente(cliente): cadastra um novo cliente na biblioteca. 
#     remover_cliente(cliente): remove um cliente da lista de clientes cadastrados. 
#     listar_clientes(): lista todos os clientes cadastrados na biblioteca. 
#     emprestar_livro(cliente, livro): permite que um cliente empreste um livro da biblioteca. 
#     devolver_livro(cliente, livro): permite que um cliente devolva um livro à biblioteca.

class Biblioteca(Livro):
    def __init__(self):
        super().__init__(self)
        
    def adiconar_livro(livro):
        autor = input('Adicione o nome do autor do livro: ')
        titulo = input('Insira o título do livro: ')
        ano_publicacao = input('Insira o ano de publicação: ')