class Heroi:
    lista_nome = []
    lista_classe = ['Mago', 'Guerreiro']
    lista_poder_mago = [
        {
            "nome": "Bola de Fogo",
            "descricao": "Conjura uma esfera de chamas que causa dano em uma área específica.",
        },
        {
            "nome": "Escudo Arcano",
            "descricao": "Cria um escudo mágico que absorve parte do dano recebido por um período de tempo.",
        },
        {
            "nome": "Raio de Gelo",
            "descricao": "Dispara um raio de gelo que causa dano direto e pode congelar o alvo temporariamente.",
        },
        {
            "nome": "Teletransporte",
            "descricao": "Teleporta o mago para um local específico dentro de um alcance determinado.",
        }
    ]
    
    lista_fraqueza = []

    def __init__(self, nome, classe, poder, ponto_fraco):
        self.nome = nome
        self.classe = classe
        self.poder = poder
        self.ponto_fraco = ponto_fraco

    def adicionar_nome(self):
        self.lista_nome.append(self.nome)

    def mostrar_info(self):
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Poder: {self.poder}")
        print(f"Ponto Fraco: {self.ponto_fraco}")

    @classmethod
    def selecionar_poder(cls):
        print("Lista de Poderes disponíveis para Mago:")
        for index, poder in enumerate(cls.lista_poder_mago, start=1):
            print(f"{index}. {poder['nome']} - {poder['descricao']}")

        escolha = int(input("Selecione o número correspondente ao poder desejado: "))
        poder_selecionado = cls.lista_poder_mago[escolha - 1]
        return poder_selecionado

# Exemplo de uso
nome = input('Insira o nome do seu personagem: ')
classe = input('Selecione a classe (Mago ou Guerreiro): ')

# Verifica se a classe é válida
if classe not in Heroi.lista_classe:
    print("Classe inválida!")
else:
    if classe == 'Mago':
        poder_selecionado = Heroi.selecionar_poder()
    else:
        poder_selecionado = None  # Para o Guerreiro, poderia implementar uma escolha de habilidades específicas

    ponto_fraco = input('Insira o ponto fraco do seu personagem: ')

    heroi = Heroi(nome, classe, poder_selecionado['nome'], ponto_fraco)
    heroi.adicionar_nome()

    # Mostra informações do herói criado
    print("\nInformações do Herói:")
    heroi.mostrar_info()
