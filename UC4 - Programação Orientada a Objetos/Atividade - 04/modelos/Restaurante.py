import os

class Restaurante:
    lista_restaurantes = [
    
    ]

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo= True
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
    
    # def alterar_status(self):
    #     if self._ativo == True:
    #         return 'DESATIVADO'
    #     elif self._ativo == False:
    #         return 'ATIVADO'
    
    def alterar_status(self):
        self._ativo = not self._ativo

    # def alterar_status(self, true):
    #     self._ativo = true

    
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
        print(f'{"╾─╼"} {('RESTAURANTE').ljust(15)} ╾{"─"*13}╼ {('CATEGORIA').ljust(15)} ╾{"─"*2}╼ {('STATUS').ljust(10)}')
        for i, restaurante in enumerate(cls.lista_restaurantes, start=1):
           print(f'⤍ {i} {(restaurante["restaurante_nome"]).ljust(15)} {"─"*15} {(restaurante["restaurante_categoria"]).ljust(15)} {"─"*4} {restaurante["ativo"]}')
    

    
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
