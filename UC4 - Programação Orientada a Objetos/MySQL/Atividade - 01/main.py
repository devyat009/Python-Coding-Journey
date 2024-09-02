from sqlConnection import MySQLConnection
import os
class main():
    def __init__(self):
        self.database = MySQLConnection()

    def clear_screen(self):
        # Clear the terminal screen based on the OS
        os.system('cls')
    def menu_options(self):
        print('''
            1 - Adicionar
            2 - Ler
            3 - Update
            4 - Delete
            5 - Aplicar mudanças
            6 - Sair
            ''')
    def comeback(self):
        inp = input('Pressione Enter para retornar...')
        self.menu_options()
        os.system('cls')

    def menu(self):
        os.system('cls')
        while True:
            self.menu_options()
            try:
                user_input = int(input('Selecione uma opção: '))
                match user_input:
                    case 1:
                        os.system('cls')
                        print('Adicionar foi selecionado...')
                        data1 = input('Insira o nome do item: ')
                        data2 = input('Insira o valor do item: ')
                        self.database.add_item(data1, data2)
                        self.database.read_table()
                        self.comeback()
                        
                    case 2:
                        os.system('cls')
                        self.database.read_table()
                        self.comeback()
                    case 3:
                        os.system('cls')
                        print('Update foi selecionado...')
                        self.database.read_table()
                        target = input('Insira o nome do item: ')
                        value = input('Insira o novo valor para o item: ')
                        self.database.update_table(target, value)
                        self.database.read_table()
                        self.comeback()
                    case 4:
                        os.system('cls')
                        print('Deletar foi selecionado...')
                        self.database.read_table()
                        target = input('Selecione o ID: ')
                        self.database.delete_item(target)
                        self.database.read_table()
                        self.comeback()
                    case 5:
                        os.system('cls')
                        self.database.commit_changes()
                        print('Mudanças foram aplicadas')
                        self.comeback
                    case 6:
                        os.system('cls')
                        print('Saindo...')
                        self.database.close_database()
                        break
                    case _:
                        print('Insira um opção valida...')
            except ValueError:
                print('Input inválido, insira um número... ')
    
app = main()
app.menu()