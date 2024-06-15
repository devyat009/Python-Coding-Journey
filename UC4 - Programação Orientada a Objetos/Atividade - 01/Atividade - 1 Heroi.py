class Heroi():
    lista_nome = []
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
    },
    {
        "nome": "Raio de Gelo",
        "descricao": "Dispara um raio de gelo que causa dano direto e pode congelar o alvo temporariamente.",
    }]
    
    lista_poder_guerreiro = [{
        "nome": "Ataque Pesado",
        "descricao": "Um ataque poderoso avassalador",
        "dano": "50"
    },
    {
        "nome": "Ataque com escudo",
        "descricao": "Um ataque que utiliza seu escudo para causar dano",
        "dano": "15"
    }]
    lista_fraqueza_mago = [{
        "nome": "Ataque Pesado"
    },
    {
        "nome": "Ataque com escudo"
    }
    ]


    def __init__(self):
        self.nome
        self.selecionar_poder
        self.classe
        self.ponto_fraco
    
    # def __init__(self, nome, classe, poder, ponto_fraco):
    #     self.nome = nome
    #     self.poder = poder
    #     self.classe = classe
    #     self.ponto_fraco = ponto_fraco
    def nome(self):
        self.lista_nome.append(self.nome)
    # def mostrar_info(self):
        """
        The function "mostrar_info" is a Python method that is currently commented out and intended to
        display information about an object's name and class.
        """
    #     print(f"Nome: {self.nome}")
    #     print(f"Classe: ")
    @  classmethod
    def classe(cls):
        print("Selecione a Classe para o seu personagem:")
        for i, classe in enumerate(cls.lista_classe, start=1):
            print(f"{i}. {classe['nome']}")

    @classmethod
    def selecionar_poder(cls):
        print("Lista de Poderes disponíveis para Mago:")
        for i, poder in enumerate(cls.lista_poder_mago, start=1):
            print(f"{i}. {poder['nome']} - {poder['descricao']}")

        escolha = int(input("Selecione o número correspondente ao poder desejado: "))
        poder_selecionado = cls.lista_poder_mago[escolha - 1]
        return poder_selecionado
        
    def ponto_fraco(self):
        pass

t = Heroi()