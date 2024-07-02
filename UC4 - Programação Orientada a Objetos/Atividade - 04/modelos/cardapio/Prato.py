from modelos.Cardapio.ItemCardapio import ItemCardapio
class Prato(ItemCardapio):
    """
    Informações:
    ------------
    Sub classe responsável por armazenar a descrição de pratos.

    Paremetros:
    -----------
    - nome - Nome da bebida.

    - preco - Preço de valor float.

    - descricao - Descricao do prato adicionado.

    Versão: 1.0
    ---------
    Autor: Higor Stanley aka Devyat009
    """
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    def __str__(self):
        return f'{"╾─╼"} {str(self._nome).ljust(15)} ╾{"─"*17}╼ {str(self._preco).ljust(10)} ╾{"─"*2}╼ {str(self._descricao).ljust(60)}'