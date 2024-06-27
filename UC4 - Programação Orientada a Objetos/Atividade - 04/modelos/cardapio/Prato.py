class Prato:
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
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    def __str__(self):
        return f'{(self._nome).ljust(15)}{"─"*15}   {(self._tamanho).ljust(12)} {"─"*4} {self._preco}'