from Cliente import Cliente
class Conta(Cliente):
    def __init__(self, nome, cpf):
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        
    def encontrar_cliente(self):
        for cliente in self.lista_cliente:
            if cliente['nome'] == self.nome and cliente['cpf'] == self.cpf:
                print('Cliente validado...')
                return cliente
        print('Cliente não encontrado.')
        return None
    
    def saldo_usuario(self):
        cliente = self.encontrar_cliente()
        if cliente:
            print(f"Olá {self.nome}, seu saldo é de: R${cliente['saldo']:.2f}")
        else:
            print("Cliente não encontrado.")
    
    def deposito(self, valor):
        cliente = self.encontrar_cliente()
        if cliente:
            if valor > 0:
                cliente['saldo'] += valor
                cliente['depositos'].append(valor)
                print(f'O depósito de R${valor:.2f} realizado com sucesso')
            else:
                print('Valor de dpósito inválido.')
        else:
            print('O cliente não foi encontrado.')
            
    def saque(self, valor):
        cliente = self.encontrar_cliente()
        if cliente:
            if 0 < valor <= cliente['saldo']:
                cliente['saldo'] -= valor
                print(f'O saque de R${valor::.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente ou valor de saque inválido')
        else:
            print('O cliente não foi encontrado')
    
    def saque_especial(self):
        cliente = self.encontrar_cliente()
        if cliente:
            if cliente['saldo'] == 0:
                print('Você pode realizar o saque especial, atente-se que podera sacar até R$1.000 tendo um juros de 14%.')
                escolha = int(input('Digite o valor para saque:'))
                while True:
                    if escolha <= 1000:
                        saque = 0.14*escolha + escolha
                        print(f'Você sacou R${escolha}')
                        print(f'Você esta devendo R${saque}')
                        return
                    else:
                        print('Valor não permitido')
            else:
                print('Você não pode realiza saque especial.')