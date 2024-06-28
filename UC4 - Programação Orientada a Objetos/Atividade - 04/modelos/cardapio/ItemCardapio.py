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

    
    lista_cardapio_custom = []
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f'{(self._nome).ljust(15)}{"─"*15}{"─"*4} R$ {self._preco:.2f}'
    


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
            