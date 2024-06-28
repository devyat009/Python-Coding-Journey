# Descrição:
# Crie um sistema de cadastro de restaurante e seu respectivo cardápio em Python utilizando Programação
# Orientada a Objetos (POO).

# O sistema deve possuir as seguintes Classes e cada uma delas deve ser feita em um:

# • Restaurante:
#     o nome
#     o Categoria (Pizzaria, Japonesa, Fastfood, Churrascaria...)

# Imports
from modelos.Restaurante import Restaurante
from modelos.cardapio.ItemCardapio import ItemCardapio
from modelos.cardapio.Bebida import  Bebida
from modelos.cardapio.Prato import Prato
import os
class App():
    """
    Serve como o programa em si para chamar as classes
    
    Versão: 1.1
    -----------
    Autor: Higor Stanley aka Devyat009
    """

    def __init__(self):
        pass
    
    @classmethod
    def cadapio_churras(cls):
        """
        Informações:
        ------------
        Metódo para imprimir o cardapio, facilmente mutavel no ctrl-c e ctrl-v
        """
        for i, item in enumerate(cls.lista_cardapio_churrascaria_pg1, start=1):
            print(f'⤍ {i} - {item["item"].ljust(13)} ╾{("─"*13)}╼ {item["valor"]:.2f}')

    @classmethod
    def cardapio_bebidas(cls):
        """
        Informações:
        ------------
        Metódo para imprimir o cardapio de bebidas, facilmente mutavel no ctrl-c e ctrl-v
        """
        for i, item in enumerate(cls.lista_cardapio_universal_bebidas, start= 1):
            print(f'⤍ {i} - {item["item"].ljust(13)} ╾{("─"*13)}╼ {item["valor"]:.2f}')

    def limpar_terminal(self):
        input('Pressione qualquer tecla para continuar.')
        os.system('cls')
    

    def login_banner(self):
        print('''
______          _                              _       
| ___ \        | |                            | |      
| |_/ /___  ___| |_ __ _ _   _ _ __ __ _ _ __ | |_ ___ 
|    // _ \/ __| __/ _` | | | | '__/ _` | '_ \| __/ _ |
| |\ \  __/\__ \ || (_| | |_| | | | (_| | | | | ||  __/
\_| \_\___||___/\__\__,_|\__,_|_|  \__,_|_| |_|\__\___|
''')

    def opcoes_inicio(self):
        print(f'┏{('━'*48).ljust(40)}┓')
        print(f'┃ {('〔 1 - Listar Restaurantes                  〕').ljust(45)}┃')
        print(f'┃ {('〔 2 - Alterar Estado de Restaurante        〕').ljust(45)}┃')
        print(f'┃ {('〔 3 - GG EZ PZ LMN SQZY                    〕').ljust(45)}┃')
        print(f'┃ {('〔 4 - GG EZ PZ LEMON SQUEZYY               〕').ljust(45)}┃')
        print(f'┃ {('〔 5 - Sair                                 〕').ljust(45)}┃')
        print(f'┗{('━'*48).ljust(40)}┛')


    def main(self):
        """
        A main do programa, onde dara acesso ao programa em si.
        """
        app = App()
        while True:
            app.login_banner()
            app.opcoes_inicio()
            
            escolha = int(input('Escolha: '))
            match escolha:
                case 1:
                    os.system('cls')
                    Restaurante.listar_restaurantes()
                    app.limpar_terminal()
                case 2:
                    os.system('cls')
                    print('Os restaurantes foram listado, selecione o desejado para alterar o estado pelo seu número.')
                    Restaurante.listar_restaurantes()
                    escolha = int(input('▶ Digite o número do estabelecimento em que deseja alterar o estado: '))
                    Restaurante.alterar_status_alvo(escolha)
                    Restaurante.listar_restaurantes()
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    print('Saindo...')
                    break
                case _:
                    print('Insira uma opção valida.')
                    app.limpar_terminal()
                    

print('─'*67)
KiGordo = Restaurante('KiGordo', 'FastFood')
ChurradoSul = Restaurante('Churras do Sul', 'Churrascaria')
#ChurradoSul.alterar_status(False)
ChurradoSul.alterar_status()
# Restaurante.listar_restaurantes()

app = App()
app.main()

# print('─'*50)
#sucudipera = Bebida('Suco di Pera', '250ml', 12.00)
#print(sucudipera)


# print('─'*67)
# suco = ItemCardapio('Suco Laranja', 6.00)
# suco2 = Bebida('Laranjola', '300ml', 12.00)
# suco1 = Bebida('Vodka Kadov', '1L', 35.00)
# carne = Prato('Costela', 19.99, 'Costela banhada no oleo')
# print(suco)
# print(suco2)
# print('─'*67)
# ChurradoSul.adicionar_no_cardapio_bebida(suco1)
# ChurradoSul.adicionar_no_cardapio_prato(carne)
# ChurradoSul.mostrar_cardapio_bebida()
# print('─'*67)
# ChurradoSul.mostrar_cardapio_prato()