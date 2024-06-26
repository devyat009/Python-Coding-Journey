class ItemCardapio:
    """
    Informações:
    ------------
    Classe responsável por armazenar os Items do cardapio.
    Versão: 1.0
    ---------
    Autor: Higor Stanley aka Devyat009
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
        {'item': 'Coca Cola', 'valor': 3.49},
        {'item': 'Coca Cola', 'valor': 6.49},
        {'item': 'Pepsi', 'valor': 3.69},
        {'item': 'Cerveja BRAHMA', 'valor': 6.00},
        {'item': 'Cerveja BRAHMA 1L', 'valor': 12.99 },
        {'item': 'Água 250ml','valor': 1.99}
    ]
    """
    Cardapio UNIVERSAL de bebidas
    """
    
    lista_cardapio_custom = []
    def __init__(self):
        pass
    
    @classmethod
    def add_cardapio(cls, nome, preco):
        """
        Informações:
        -----------
        Adiciona Itens customizados ao cardapio.
        """
        nome = nome.title()
        try:
            preco == float(preco)
            cls.lista_cardapio_custom.append({'item': nome, 'valor': preco})
        except ValueError:
            print('Preço invalído')
            
ItemCardapio.add_cardapio('Pera', 2.3)
print(ItemCardapio.lista_cardapio_custom)