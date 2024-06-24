class Heroi():
    lista_nome = []
    # Classes:
    lista_classe = [{
        "nome": "Mago"
    },
    {
        "nome": "Guerreiro"
    }                
    ]
    lista_poder_mago = [{
        "nome": "Bola de Fogo",
        "descricao": "Conjura uma esfera de chamas que causa dano em uma área específica.",
        "dano": 45
    },
    {
        "nome": "Raio de Gelo",
        "descricao": "Dispara um raio de gelo que causa dano direto e pode congelar o alvo temporariamente.",
        "dano": 20
    }]
    
    lista_poder_guerreiro = [{
        "nome": "Ataque Pesado",
        "descricao": "Um ataque poderoso avassalador",
        "dano": 50
    },
    {
        "nome": "Ataque com escudo",
        "descricao": "Um ataque que utiliza seu escudo para causar dano",
        "dano": 15
    }]
    lista_fraqueza_mago = [{
        "nome": "Ataque Pesado"
    }
    ]
    lista_fraqueza_guerreiro = [{
        "nome": "Bola de Fogo"
    }]

    def __init__(self, nome=None, classe=None):
        self.nome = nome
        #self.selecionar_poder
        self.classe = classe
        self.poder = None
        self.ponto_fraco = None
        self.vida = 100
        if self.nome: # Adiciona o nome do personagem
            Heroi.lista_nome.append(self.nome)

    def nome(self):
        self.lista_nome.append(self.nome)
    
    def mostrar_info(self): # mostrar as informacoes do personagem
        print(f'Nome: {self.nome}')
        print(f'Classe: {self.classe}')
        if self.poder:
            print(f"Poder: {self.poder['nome']}")
        print(f'Vida: {self.vida}')
    
    
    def escolher_classe(self): # Forma de selecionar a classe 
        print('Selecione a Classe para o seu personagem:')
        for i, classe in enumerate(self.lista_classe, start=1):
            print(f"{i} - {classe['nome']}")
        escolha = int(input('Selecione o número correspondente à classe: '))
        self.classe = Heroi.lista_classe[escolha - 1]['nome']
        
        # Determina o ponto fraco baseado na classe escolhida, adicionar mais classes depois
        if self.classe == "Mago":
            self.ponto_fraco = Heroi.lista_fraqueza_mago[0]
        elif self.classe == "Guerreiro":
            self.ponto_fraco = Heroi.lista_fraqueza_guerreiro[0]
    
    def selecionar_poder(self):
        if self.classe == "Mago":
            poderes = Heroi.lista_poder_mago
        elif self.classe == "Guerreiro":
            poderes = Heroi.lista_poder_guerreiro
        
        
        print('Lista de Poderes disponíveis:')
        for i, poder in enumerate(poderes, start=1):
            print(f"{i}. {poder['nome']} - {poder['descricao']}")

        escolha = int(input('Selecione o número correspondente ao poder desejado: '))
        self.poder = poderes[escolha -1]
    
    # Discartado
    def ponto_fraco(self):
        pass
    
def duelo(heroi1, heroi2):
    print(f"{heroi1.nome} ({heroi1.classe}) vs {heroi2.nome} ({heroi2.classe})")
    
    # Herói 1 ataca Herói 2
    dano1 = heroi1.poder['dano']
    if heroi2.ponto_fraco['nome'] == heroi1.poder['nome']:
        dano1 *= 1.5  # Multiplicador de dano se for o ponto fraco
    heroi2.vida -= dano1
    print(f"{heroi1.nome} usa {heroi1.poder['nome']} causando {dano1} de dano em {heroi2.nome}")

    # Herói 2 ataca Herói 1
    dano2 = heroi2.poder['dano']
    if heroi1.ponto_fraco['nome'] == heroi2.poder['nome']:
        dano2 *= 1.5  # Multiplicador de dano se for o ponto fraco
    heroi1.vida -= dano2
    print(f"{heroi2.nome} usa {heroi2.poder['nome']} causando {dano2} de dano em {heroi1.nome}")

    # Mostrar resultados
    print(f"Vida de {heroi1.nome}: {heroi1.vida}")
    print(f"Vida de {heroi2.nome}: {heroi2.vida}")

    # Determinar vencedor
    if heroi1.vida > heroi2.vida:
        print(f"{heroi1.nome} vence o duelo!")
    elif heroi2.vida > heroi1.vida:
        print(f"{heroi2.nome} vence o duelo!")
    else:
        print("O duelo termina em empate!")
        
        
nome = input('Jogador 1 - Digite o nome do seu personagem: ')
jogador1 = Heroi(nome)
jogador1.escolher_classe()
jogador1.selecionar_poder()
jogador1.mostrar_info()

nome2 = input('Jogador 2 - Digite o nome de seu personagem: ')
jogador2 = Heroi(nome2)
jogador2.escolher_classe()
jogador2.selecionar_poder()
jogador2.mostrar_info()

duelo(jogador1, jogador2)