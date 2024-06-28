import os
from modelos.cardapio.Bebida import Bebida

class Restaurante:
    """
    Informações:
    ------------
    Classe capaz de adicionar novos restaurantes, listar eles e alterar o estado do estabelicimento.
    
    Versão: 1.2
    -----------
    Autor: Higor Stanley aka Devyat009
    """
    lista_restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo= True
        self._cardapio_bebida= []
        self._cardapio_prato = [] # Lista separada pois os pratos tem descrições grandes
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

    @classmethod
    def alterar_status_alvo(cls, alvo):
        """
        Informações:
        -------------
        Capaz de listar os restaurantes de forma enumerada para ser capaz de alterar o estado

        Parametro:
        -----------
        alvo - Número alvo para alterar o estado
        
        """
        if 0 < alvo <= len(cls.lista_restaurantes):
            cls.listar_restaurantes[alvo - 1]
            Restaurante.alterar_status()
            print('O restaurante foi alterado com sucesso')

    def adicionar_no_cardapio_bebida(self, item):
        """
        Informações:
        ---------------
        Responsavel por adiciopnar itens no cardapio 
        
        Uso:
        ------------
        bebida = Bebida('Bebida Exemplo', '250ml', 5.99)

        restaurante_exemplo.adicionar_no_cardapio(bebida)

        """
        self._cardapio_bebida.append(item)

    def adicionar_no_cardapio_prato(self, item):
        """
        Informações:
        ---------------
        Responsavel por adiciopnar itens no cardapio 
        
        Uso:
        ------------
        prato = Prato('Prato Exemplo', 5.99, 'Descrição do prato')

        restaurante_exemplo.adicionar_no_cardapio(prato)

        """
        self._cardapio_prato.append(item)

    def mostrar_cardapio_bebida(self):
        """
        Informações:
        ------------
        Função de Restaurante
        """
        print(f'╾{"─"*30} Bebidas Disponíveis {"─"*30}╼')
        print(f'{"╾─╼"} {("ITEM").ljust(15)} ╾{"─"*17}╼ {("    DESCRIÇÃO").ljust(17)} ╾{"─"*2}╼ {("PREÇO").ljust(10)}')
        for i in self._cardapio_bebida:
            print(f'{i}')

    def mostrar_cardapio_prato(self):
        """
        Informações:
        ------------
        Função de Restaurante para mostrar o cardapio em especifico:
        """
        print(f'╾{"─"*30} Pratos Disponíveis {"─"*30}╼')
        print(f'{"╾─╼"} {("ITEM").ljust(15)} ╾{"─"*17}╼ {("PREÇO").ljust(10)} ╾{"─"*2}╼ {("    DESCRIÇÃO").ljust(60)}')
        for i in self._cardapio_prato:
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