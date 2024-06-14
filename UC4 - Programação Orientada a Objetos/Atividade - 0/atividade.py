
class Aluno():
    """
    Classe que representa um aluno.

    Atributos de Classe:
    lista (list): Lista compartilhada entre todas as instâncias da classe Aluno.

    Atributos de Instância:
    nome (str): Nome do aluno.
    lista_notas (list): Lista de notas do aluno.
    """
    lista = []
    def __init__(self, nome):
        self.nome = nome
        self.lista_notas = []
    def pegar_notas(self):
        
        quantidade = int(input('Insira a quantidade de notas a ser inseriada: '))
        for i in range(quantidade):
            nota = float(input(f'Insira a nota {i+1}: '))
            self.lista_notas.append(nota)
    def calcular_media(self):
        media = sum(self.lista_notas) / len(self.lista_notas)
        return media
        
Higor = Aluno('Higor')

Higor.pegar_notas()
print(f'O aluno {Higor.calcular_media()}')