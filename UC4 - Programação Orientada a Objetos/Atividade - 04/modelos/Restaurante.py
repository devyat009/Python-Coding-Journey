import os
from modelos.cardapio.Bebida import Bebida

class Restaurante:
    """
    Informações:
    ------------
    Classe capaz de adicionar novos restaurantes, listar eles e alterar o estado do estabelicimento.
    
    Versão: 1.1
    -----------
    Autor: Higor Stanley aka Devyat009
    """
    lista_restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo= True
        self._cardapio = []
        # Adiciona o restaurante na lista de restaurantes.
        Restaurante.lista_restaurantes.append({'restaurante_nome': nome, 'restaurante_categoria': categoria, 'ativo': self.ativo}) 
    
    def __str__(self):
        """
        Feito para não retorna valor de mémoria.
        """
        return f'{(self._nome).ljust(15)}{"─"*15}   {(self._categoria).ljust(12)} {"─"*4} {self.ativo}'

    @property
    def ativo(self):
        """
        Ativa e Desativa o status do restaurante.
        """
        if self._ativo:
            return 'Ativado'
        else:
            return 'Desativado'
    
    def alterar_status(self):
        """
        Informações:
        ------------
        Utilizado para alterar o status de Ativado ou para Desativado.
        """
        self._ativo = not self._ativo
        for restaurante in Restaurante.lista_restaurantes:
            if restaurante['restaurante_nome'] == self._nome:
                restaurante['ativo'] = self.ativo

    @classmethod
    def listar_restaurantes(cls):
        """
        Informações:
        -------------
        Capaz de listar os restaurantes com titulo e a lista abaixo ajustados.
        
        """
        if not cls.lista_restaurantes:
            print('⚠ A lista de restaurantes está vazia ⚠')
            return
        # Imprimir a lista de de restaurantes 
        print(f'{"╾─╼"} {("RESTAURANTE").ljust(15)} ╾{"─"*13}╼ {("CATEGORIA").ljust(15)} ╾{"─"*2}╼ {("STATUS").ljust(10)}')
        for i, restaurante in enumerate(cls.lista_restaurantes, start=1):
           print(f'⤍ {i} {(restaurante["restaurante_nome"]).ljust(15)} {"─"*15} {(restaurante["restaurante_categoria"]).ljust(15)} {"─"*4} {restaurante["ativo"]}')

    def adicionar_no_cardapio(self, item):
        """
        Informações:
        ---------------
        Responsavel por adiciopnar itens no cardapio 
        
        Uso:
        ------------
        bebida = Bebida('Bebida Exemplo', '250ml', 5.99)

        restaurante_exemplo.adicionar_no_cardapio(bebida)

        """
        self._cardapio.append(item)

    def mostrar_cardapio(self):
        """
        Informações:
        ------------

        """
        print(f'{"╾─╼"} {("ITEM").ljust(11)} ╾{"─"*13}╼ {("TAMANHO").ljust(7)} ╾{"─"*2}╼ {("PREÇO").ljust(10)}')
        for i in self._cardapio:
            print(f'{i}')

    @classmethod
    def restaurante_add(cls, nome, categoria):
        """
        Informações:
        ------------
        Responsavel por adicionar novos restaurantes a lista de restaurantes.

        Uso:
        ------------
        Restaurante.restaurante_add('Exemplo de Restaurante', 'Churrascaria')
        """
        cls.lista_restaurantes.append({'restaurante_nome': nome, 'restaurante_categoria': categoria})