# Descrição:
# Crie um sistema de cadastro de restaurante e seu respectivo cardápio em Python utilizando Programação
# Orientada a Objetos (POO).

# O sistema deve possuir as seguintes Classes e cada uma delas deve ser feita em um:

# • Restaurante:
#     o nome
#     o Categoria (Pizzaria, Japonesa, Fastfood, Churrascaria...)
from modelo.Restaurante import Restaurante

class App():
    """
    Informações:
    ------------
    Serve como o programa em si para chamar as classes
    """
    lista_cardapio_churrascaria_pg1= [
        {'item': 'Paleta', 'valor': 19.90},
        {'item': 'Picanha', 'valor': 19.90},
        {'item': 'Maminha', 'valor': 19.90},
        {'item': 'Alcatra', 'valor': 19.90},
        {'item': 'Contra Filé', 'valor': 19.90},
        {'item': 'Patinho', 'valor': 19.90},
        {'item': 'Pernil', 'valor': 19.90},
        {'item': 'Tilápia', 'valor': 19.90},
    ]
    """
    Cardapio de Churrasco Pagina 1
    """
    lista_cardapio_universal_bebidas= [
        {'item': 'Coca Cola 250ml', 'valor': 3.49},
        {'item': 'Coca Cola 600ml', 'valor': 6.49},
        {'item': 'Pepsi 250ml', 'valor': 3.69},
        {'item': 'Cerveja BRAHMA 369ml', 'valor': 6.00},
        {'item': 'Cerveja BRAHMA 1L', 'valor': 12.99 },
        {'item': 'Água 250ml', 'valor': 1.99}
    ]
    """
    Cardapio UNIVERSAL de bebidas
    """
    
    @classmethod
    def cadapio_churras(cls):
        """
        Informações:
        ------------
        Metódo para imprimir o cardapio, facilmente mutavel no ctrl-c e ctrl-v
        """
        for i, item in enumerate(cls.lista_cardapio_churrascaria_pg1, start=1):
            print(f'{i} - {item["item"].ljust(13)} {("─"*15)} {item["valor"]:.2f}')

    @classmethod
    def cardapio_bebidas(cls):
        """
        Informações:
        ------------
        Metódo para imprimir o cardapio de bebidas, facilmente mutavel no ctrl-c e ctrl-v
        """
        for i, item in enumerate(cls.lista_cardapio_universal_bebidas, start= 1):
            print(f'{i} - {item["item"].ljust(13)} {("─"*15)} {item["valor"]:.2f}')

    def login_banner(self):
        print('''
______          _                              _       
| ___ \        | |                            | |      
| |_/ /___  ___| |_ __ _ _   _ _ __ __ _ _ __ | |_ ___ 
|    // _ \/ __| __/ _` | | | | '__/ _` | '_ \| __/ _ \
| |\ \  __/\__ \ || (_| | |_| | | | (_| | | | | ||  __/
\_| \_\___||___/\__\__,_|\__,_|_|  \__,_|_| |_|\__\___|
''')
main = App()
main.cadapio_churras()
print('─'*50)
main = Restaurante('Jose', 'Test')
main.listar_restaurantes()
print('─'*50)
main.restaurante_add('Churras do Sul', 'Churrascaria')
main.listar_restaurantes()
print('─'*50)
print(main)