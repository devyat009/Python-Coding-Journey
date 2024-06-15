from Cliente import Cliente
class Conta(Cliente):
    def __init__(self, nome, cpf):
        super().__init__()
        self.nome = None
        self.cpf 
    
        
    def encontrar_cliente(self):
        for cliente in self.lista_cliente:
            if cliente['nome'] == self.nome and cliente['cpf'] == self.cpf:
                return cliente
        return None
    
    def saldo_usuario(self):
        cliente = self.encontrar_cliente()
        if cliente:
            print(f"Olá {self.nome}, seu saldo é de: R${cliente['saldo']:.2f}")
        else:
            print("debug - SALDO - Cliente não encontrado.")
    
    def deposito(self, valor):
        cliente = self.encontrar_cliente()
        if cliente:
            if valor > 0:
                cliente['saldo'] += valor
                cliente['depositos'].append(valor)
                print(f'O depósito de R${valor:2f} realizado com sucesso')
            else:
                print('Valor de dpósito inválido.')
        else:
            print('O cliente não foi encontrado.')
            
    def saque(self, valor):
        cliente = self.encontrar_cliente()
        if cliente:
            if 0 < valor <= cliente['saldo']:
                cliente['saldo'] -= valor
                print(f'O saque de R${valor:2.f} realizado com sucesso.')
            else:
                print('Saldo insuficiente ou valor de saque inválido')
        else:
            print('O cliente não foi encontrado')