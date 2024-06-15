from Cliente import Cliente
from Conta import Conta
cliente1 = Cliente()
def cadastrar_ui(): # Resolver problema de 2 cadastros 
    print('Bem vindo ao Cadastro do banco Faz u L')
    nome = input('Insira seu nome: ')
    cpf = int(input('Insira seu CPF: '))
    conta1 = Conta(nome, cpf) # Cadasro do arquivo Conta
    cliente1.cadastro() # Cadastro do arquivo Cliente
# Login do Banco
def banco_login():
    print('''Escolha a opção:\n1- Login\n2- Cadastrar''')
    escolha1 = int(input('Escolha:'))
    match escolha1:
        case 1:
            pass
        case 2:
            cadastrar_ui()
# Interface de interação do banco
def banco_interface():
    conta = Conta()
    print('''Escolha uma das opções:
          1 - Consultar Saldo
          2 - Deposito
          3 - Saque''')
    escolha = int(input('Escolha: '))
    match escolha:
        case 1:
            conta.saldo_usuario()
        case 2:
            valor = float(input('Insira o valor do depósito:'))
            conta.deposito(valor)
        case 3:
            pass

