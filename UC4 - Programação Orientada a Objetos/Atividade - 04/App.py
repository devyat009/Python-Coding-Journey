#Atualizações nos atalhos do teclado … Em quinta-feira, 1 de agosto de 2024, os atalhos de teclado do Drive serão atualizados para oferecer a navegação por letras iniciais.Saiba mais
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

class App():
    """
    Serve como o programa em si para chamar as classes
    
    Versão: 1.1
    -----------
    Autor: Higor Stanley aka Devyat009
    """
    
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

    def login_banner(self):
        print('''
______          _                              _       
| ___ \        | |                            | |      
| |_/ /___  ___| |_ __ _ _   _ _ __ __ _ _ __ | |_ ___ 
|    // _ \/ __| __/ _` | | | | '__/ _` | '_ \| __/ _ \
| |\ \  __/\__ \ || (_| | |_| | | | (_| | | | | ||  __/
\_| \_\___||___/\__\__,_|\__,_|_|  \__,_|_| |_|\__\___|
''')

    def opcoes_inicio():
        print(f'┏{('━'*32).ljust(25)}┓')
        print(f'┃ {('〔 1 - GG EZ〕 ').ljust(29)}┃')
        print(f'┃ {('〔 2 - GG EZ PZ〕 ').ljust(29)}┃')
        print(f'┃ {('〔 3 - GG EZ PZ LMN SQZY 〕').ljust(29)}┃')
        print(f'┃ {('〔 4 - GG EZ PZ LEMON SQUEZYY〕').ljust(29)}┃')
        print(f'┗{('━'*32).ljust(25)}┛')

print('─'*67)
KiGordo = Restaurante('KiGordo', 'FastFood')
ChurradoSul = Restaurante('Churras do Sul', 'Churrascaria')
#ChurradoSul.alterar_status(False)
ChurradoSul.alterar_status()
Restaurante.listar_restaurantes()

# print('─'*50)
#sucudipera = Bebida('Suco di Pera', '250ml', 12.00)
#print(sucudipera)
print(App.opcoes_inicio())

print('─'*67)
suco = ItemCardapio('Suco Laranja', 6.00)
suco2 = Bebida('Laranjola', '300ml', 12.00)
suco1 = Bebida('Vodka Kadov', '1L', 35.00)
print(suco)
print(suco2)
print('─'*67)
ChurradoSul.adicionar_no_cardapio(suco1)
ChurradoSul.mostrar_cardapio()