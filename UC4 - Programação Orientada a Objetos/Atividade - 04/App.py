# Descrição:
# Crie um sistema de cadastro de restaurante e seu respectivo cardápio em Python utilizando Programação
# Orientada a Objetos (POO).

# O sistema deve possuir as seguintes Classes e cada uma delas deve ser feita em um:

# • Restaurante:
#     o nome
#     o Categoria (Pizzaria, Japonesa, Fastfood, Churrascaria...)
from modelos.Restaurante import Restaurante

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

    
    @classmethod
    def cadapio_churras(cls):
        for i, item in enumerate(cls.lista_cardapio_churrascaria_pg1, start=1):
            print(f'{i} - {item["item"].ljust(13)} {'─'*15} {item["valor"]:.2f}')

    def cardapio_Bebidas(self):
        pass

    def login_banner(self):
        print('''
______          _                              _       
| ___ \        | |                            | |      
| |_/ /___  ___| |_ __ _ _   _ _ __ __ _ _ __ | |_ ___ 
|    // _ \/ __| __/ _` | | | | '__/ _` | '_ \| __/ _ \
| |\ \  __/\__ \ || (_| | |_| | | | (_| | | | | ||  __/
\_| \_\___||___/\__\__,_|\__,_|_|  \__,_|_| |_|\__\___|
''')
#main = App()
#main.cadapio_churras()
        
main = Restaurante('Jose', 'Test')
main.listar_restaurantes()
main.restaurante_add('Churras do Sul', 'Churrascaria')
main.listar_restaurantes()
print('─'*50)
print(main)