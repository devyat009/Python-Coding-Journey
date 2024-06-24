import os
#from Livro import Livro


# Classe Livro: 
#     Atributos: título, autor, ano de publicação, status de empréstimo. 
#     Métodos: 
#     informacoes(): exibe as informações do livro. 
#     emprestar(): marca o livro como emprestado. 
#     devolver(): marca o livro como devolvido. 


class Livro():
    lista_de_livros = [] # Lista dos livros
    # Exemplo de usar a classe livro:
    # livro1 = Livro('Alin Habbei', 'Aprenda a pilotar um avião até novembro', 2001)
    def __init__(self, autor, titulo, ano_publicacao, status=False):
        #super().__init__()
        self.autor = autor
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.status = status
        Livro.lista_de_livros.append(self)
    
    def informacoes(self):
        for livro in Livro.lista_de_livros:  # Corrigido para usar Livro.lista_de_livros
            print(f'titulo: {livro.titulo}, autor: {livro.autor}, ano: {livro.ano_publicacao}, status: {"Emprestado" if livro.status else "Disponível"}')
    # def adicionar_livro(self):
    #     titulo = input('Digite o titulo do livro: ')
    #     autor = input('Digite o autor do livro: ')
    #     ano_publicacao = input('Digite o ano de publicação: ')
    #     livro = (autor, titulo, ano_publicacao)
    #     self.lista_de_livros.append('titulo': {titulo}, 'autor': {autor}, 'ano': {ano_publicacao})
    #     #self.lista_de_livros.append(livro)
    
    @staticmethod
    def adicionar_livro():
        titulo = input('Digite o título do livro: ')
        autor = input('Digite o autor do livro: ')
        ano_publicacao = int(input('Digite o ano de publicação: '))
        novo_livro = Livro(autor, titulo, ano_publicacao)
        print(f'Livro "{titulo}" adicionado com sucesso!')

    # def remover_livro(self):
    #     self.informacoes()
    #     escolha = input('Digite o titulo do livro: ')
    #     if Livro.titulo == escolha and not Livro.status and Livro.status:
    #         Livro.titulo.remove(escolha)
    #         print('Livro removido com sucesso')
    def remover_livro(self):
        self.informacoes()
        escolher_livro = input('Diga o título do livro que quer devolver: ')
        for livro in Livro.lista_de_livros:
            if livro.titulo == escolher_livro and livro.status:
                livro.devolver()
        
    print('Livro não encontrado ou já está devolvido.')

    # Entender esta porcaria
    def emprestar(self):
        if not self.status:
            self.status = True
            print(f'Livro "{self.titulo}" emprestado com sucesso.')
        else:
            print(f'Livro "{self.titulo}" já está emprestado.')

    def devolver(self):
        if self.status:
            self.status = False
            print(f'Livro "{self.titulo}" devolvido com sucesso.')
        else:
            print(f'Livro "{self.titulo}" já está disponível.')

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

class Cliente():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

    # Informações do Cliente:
    def informacoes(self):
        print (f'Nome do Cliente: {self.nome}')
        print (f'Idade do Cliente: {self.idade}')
    
    # Pegar Livro
    # def pegar_livro(self):
    #     for i in Livro.lista_de_livros:
    #         print(f'Livro {i}'.ljust(20) + '▎' + f'{Livro.titulo}'.ljust(20) + '▎' + f'{Livro.autor}'.ljust(20) + '▎' + f'{Livro.ano}'.ljust(10))
    def pegar_livro(self):
        print("Lista de livros disponíveis:")
        for livro in Livro.lista_de_livros:
            if not livro.status:
                livro.informacoes()
                print('')

        escolher_livro = input('Diga o título do livro que quer pegar: ')
        for livro in Livro.lista_de_livros:
            if livro.titulo == escolher_livro and not livro.status:
                livro.emprestar()
                return
        print('Livro não encontrado ou já está emprestado.')

    
    # Devolver Livro
    def devolver_livro(self):
        # self.livro = livro
        # if livro in self.lista_de_livros:
        #     self.lista_de_livros.remove(livro)
        #     print ('Livro removido com sucesso.')
        # else:
        #     print ('Esse livro não foi emprestado ao cliente.')
        print("Lista de livros disponíveis:")
        for livro in Livro.lista_de_livros:
            if livro.status:
                livro.informacoes()

        escolher_livro = input('Diga o título do livro que quer devolver: ')
        for livro in Livro.lista_de_livros:
            if livro.titulo == escolher_livro and livro.status:
                livro.devolver()
                return
        print('Livro não encontrado ou já está devolvido.')

class Biblioteca():
    def __init__(self):
        self.voltar = Cliente (nome ='Jose', idade = 20)
        #self.livro = Livro(autor, titulo, ano_publicacao=)
        self.livros = Livro.lista_de_livros
        self.livrosad = Livro.adicionar_livro
        # self.livros = Livro (autor= )
    
    def listar_livros(self):
        # if self.livros.lista_de_livros:
        #     for livro in self.livros.lista_de_livros:
        #         print (f' - {livro}')
        # Caso não tenha nenhum livro:
        # if not self.lista_de_livros:
        #     print('⋄ Não tem nenhum livro cadastrado')
        #     return
        Livro.informacoes(self)
        # else:
        #     print ('Nenhum livro na Biblioteca.')

    def adicionar_livro(self): #######
        Livro.adicionar_livro()

    def remover_livro(self):
        Livro.remover_livro(self)

    def finalizar_app(self):
        print ('Saindo da biblioteca.')
        exit()

    def opcao_invalida(self):
        print ('Opção inválida.')
        self.voltar_ao_menu()

    def voltar_ao_menu(self):
        print ('----'*10)
        print ('Pressione "Enter" para voltar ao menu da biblioteca: ')
        input()
        self.main()

    def main(self):
        os.system('cls')
        self.exibir_opcoes()
        self.opcoes()

    def exibir_opcoes(self):
        print ('1 - Ver informações do Cliente.')
        print ('2 - Pegar livro.')
        print ('3 - Devolver livro.')
        print ('4 - Lista de livros')
        print ('5 - Adicionar Livro na biblioteca')
        print ('6 - Remover um Livro da biliooteca.')
        print ('7 - Sair da biblioteca.')

    def opcoes(self):
        while True:
            try:
                print ('')
                escolher_opcao = int(input('O que você deseja fazer na biblioteca?: '))
                print ('----'*10)

                match escolher_opcao:
                    case 1:
                        self.voltar.informacoes()
                        self.voltar_ao_menu()

                    case 2:
                        self.voltar.pegar_livro()
                        self.voltar_ao_menu()

                    case 3:
                        self.voltar.devolver_livro()
                        self.voltar_ao_menu()

                    case 4:
                        self.listar_livros()
                        self.voltar_ao_menu()
                    
                    case 5:
                        self.adicionar_livro()
                        self.voltar_ao_menu()
                    
                    case 6:
                        self.remover_livro()
                    case 7:
                        self.finalizar_app()
                    case _:
                        self.opcao_invalida()
                        self.voltar_ao_menu()

            except  ValueError:
                self.opcao_invalida()
                self.voltar_ao_menu()
test = Biblioteca()

test.main()