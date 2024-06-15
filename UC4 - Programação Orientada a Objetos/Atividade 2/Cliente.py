
class Cliente():
    lista_cliente = []
    def __init__(self):
        self.nome = None
        self.cpf = None
        
    # Identifica se há um cadastro na lista de cliente
    def encontrar_cliente(self):
        for cliente in self.lista_cliente:
            if cliente['nome'] == self.nome:
                print('Cliente encontrado.')
                return cliente
        print('Cliente não encontrado.')
        return None # Retorna nada
    
    # Verifica o CPF
    def verifica_cpf(self, cpf):
        if isinstance(cpf, int) and len(str(cpf)) == 8:
            return True
        else:
            return False
        
    # Realizar Cadastro
    def cadastro(self):
        if not self.lista_cliente:
            print('Não há pessoas cadastradas')
        print('Vamos cadastrar...\n')
        user_nome = input('Insira o seu nome: ')
        
        self.nome = user_nome
        while True:
            user_cpf = int(input('Insira o CPF: '))
            if self.verifica_cpf(user_cpf):
                self.lista_cliente.append({'nome': user_nome, 'cpf': user_cpf, 'saldo':0.0, 'depositos': []}) 
                print('Cliente cadastrado com sucesso.')
                return
            else:
                print('Coloque 8 digitos para o cpf!')
                
            
    

