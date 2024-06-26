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


print('─'*67)
KiGordo = Restaurante('KiGordo', 'FastFood')
ChurradoSul = Restaurante('Churras do Sul', 'Churrascaria')
#ChurradoSul.alterar_status(False)
ChurradoSul.alterar_status()
Restaurante.listar_restaurantes()

print(Restaurante.lista_restaurantes)
print(ChurradoSul)
# print('─'*50)