from modelos.cardapio.ItemCardapio import ItemCardapio
class Bebida(ItemCardapio):
    """
    Informações:
    ------------
    Sub classe responsável por armazenar o tamanho de bebidas.

    Paremetros:
    -----------
    nome - Nome da bebida

    tamanho - Tamanho da bebida

    preco - Preço de valor float 

    Versão: 1.1
    ---------
    Autor: Higor Stanley aka Devyat009
    """
    tamanho_bebida = [
        {'tamanho': '250ml'}, {'tamanho': '369ml'},{'tamanho': '1L'},{'tamanho': '600ml'},
    ]
    lista_cardapio_universal_bebidas= [
        {'item': 'Coca Cola','tamanho': '250ml', 'valor': 3.49},
        {'item': 'Coca Cola', 'valor': 6.49},
        {'item': 'Pepsi', 'tamanho': '250ml', 'valor': 3.69},
        {'item': 'Cerveja BRAHMA', 'tamanho': '369ml', 'valor': 6.00},
        {'item': 'Cerveja BRAHMA 1L', 'valor': 12.99 },
        {'item': 'Água','tamanho': '250ml', 'valor': 1.99}
    ]
    """
    Cardapio UNIVERSAL de bebidas
    """

    def __init__(self, nome, tamanho, preco):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'{"╾─╼"} {(self._nome).ljust(15)} ╾{"─"*17}╼ {(self._tamanho).ljust(17)} {"─"*4} R$ {self._preco:.2f}'
    