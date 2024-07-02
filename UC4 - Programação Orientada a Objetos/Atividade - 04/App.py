# Descrição:
# Crie um sistema de cadastro de restaurante e seu respectivo cardápio em Python utilizando Programação
# Orientada a Objetos (POO).

# O sistema deve possuir as seguintes Classes e cada uma delas deve ser feita em um:

# • Restaurante:
#     o nome
#     o Categoria (Pizzaria, Japonesa, Fastfood, Churrascaria...)

# Imports
from modelos.Restaurante import Restaurante
from modelos.Cardapio.ItemCardapio import ItemCardapio
from modelos.Cardapio.Bebida import  Bebida
from modelos.Cardapio.Prato import Prato
from modelos.Avaliacao import Avaliacao
import os
class App():
    """
    Serve como o programa em si para chamar as classes
    
    Versão: 1.1
    -----------
    Autor: Higor Stanley aka Devyat009
    """

    def __init__(self):
        '''
        Ignorado por enquanto...
        '''
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
        print('\nTitulo PLACEHOLDER')

    def opcoes_inicio(self):
        print(f'┏{('━'*48).ljust(40)}┓')
        print(f'┃ {('〔 1 - Listar Restaurantes                  〕').ljust(45)}┃')
        print(f'┃ {('〔 2 - Alterar Estado de Restaurante        〕').ljust(45)}┃')
        print(f'┃ {('〔 3 - GG EZ PZ LMN SQZY                    〕').ljust(45)}┃')
        print(f'┃ {('〔 4 - GG EZ PZ LEMON SQUEZYY               〕').ljust(45)}┃')
        print(f'┃ {('〔 5 - Sair                                 〕').ljust(45)}┃')
        print(f'┗{('━'*48).ljust(40)}┛')

    def paineldorestaurante(self, restaurante):
        """
        Informações:
        ------------
        Função que chama o menu do painel e suas opções
        """
        os.system('cls')
        # for restaurante in Restaurante.lista_restaurantes:
        #     print(f"Bem-vindo ao '{restaurante['restaurante_nome']}'")
        #     print(f"{i} - Opção {i}")
        print(f'\nBem-vindo ao {restaurante._nome}')
        print(f'1 - Listar Cardapio')
        print(f'2 - Voltar')
        while True:
            escolha = int(input('Escolha: '))
            match escolha:
                case 1:
                    restaurante.mostrar_cardapio_prato()
                    restaurante.mostrar_cardapio_bebida()
                    break
                case 2:
                    os.system('cls')
                    app.main()

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
                    
                    confirmacacao = input('Deseja acessar algum restaurante? (s/n)\n').lower()
                    if confirmacacao == 's':
                        alvo = input('Digite o número correspondente ao restaurante: ')
                        alvo = int(alvo)
                        if 0 < alvo <= len(Restaurante.lista_restaurantes):
                            restaurante_escolhido = Restaurante.lista_restaurantes[alvo - 1]
                            print(f'Você escolheu o restaurante {restaurante_escolhido._nome}...')
                            #app.limpar_terminal()
                            app.paineldorestaurante(restaurante_escolhido)
                            break
                    else:
                        app.limpar_terminal()
                        app.main()
                case 2:
                    os.system('cls')
                    print('Os restaurantes foram listado, selecione o desejado para alterar o estado pelo seu número.')
                    Restaurante.listar_restaurantes()
                    escolha = int(input('▶ Digite o número do estabelecimento em que deseja alterar o estado: '))
                    Restaurante.alterar_status_alvo(escolha)
                    Restaurante.listar_restaurantes()
                case 3:
                    app.paineldorestaurante()
                case 4:
                    pass
                case 5:
                    print('Saindo...')
                    break
                case _:
                    print('Insira uma opção valida.')
                    app.limpar_terminal()
                    
# Adição de restaurantes e categoria exemplo:
r1 = Restaurante('Restaurante A', 'Italiana')
r2 = Restaurante('Restaurante B', 'Japonesa')
r3 = Restaurante('Restaurante C', 'Brasileira')
r4 = Restaurante('Restaurante D', 'FastFood')

# Trocar status do restaurante exemplo:
r4.alterar_status()

# Adicao de bebidas exemplo:
b_suco = ItemCardapio('Suco Laranja', 6.00)
b_pepsi = Bebida('Pepsi', '1L', 9.00)

r1.adicionar_no_cardapio_bebida(b_suco)
r2.adicionar_no_cardapio_bebida(b_pepsi)

# Adicionar algumas avaliações exemplo:
r1.receber_avaliacao('João', 8)
r1.receber_avaliacao('Francisco', 6)

r2._lista_avaliacao.append({'nota': 3})
r2._lista_avaliacao.append({'nota': 7})

# Rodar o programa.
app = App()
app.main()

# print('─'*50)
#sucudipera = Bebida('Suco di Pera', '250ml', 12.00)
#print(sucudipera)


# print('─'*67)
# 
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