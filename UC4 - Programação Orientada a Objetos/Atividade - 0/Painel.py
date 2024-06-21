from Cliente import Cliente
from Conta import Conta
cliente1 = Cliente()
def cadastrar_ui():
    print('Bem vindo ao Cadastro')
    cliente1.cadastro()
    
def banco_logo():
    print('''
██████╗  █████╗ ███╗   ██╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔═══██╗
██████╔╝███████║██╔██╗ ██║██║     ██║   ██║
██╔══██╗██╔══██║██║╚██╗██║██║     ██║   ██║
██████╔╝██║  ██║██║ ╚████║╚██████╗╚██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ''')
def banco_minhaconta():
    print('''
███╗   ███╗██╗███╗   ██╗██╗  ██╗ █████╗      ██████╗ ██████╗ ███╗   ██╗████████╗ █████╗ 
████╗ ████║██║████╗  ██║██║  ██║██╔══██╗    ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗
██╔████╔██║██║██╔██╗ ██║███████║███████║    ██║     ██║   ██║██╔██╗ ██║   ██║   ███████║
██║╚██╔╝██║██║██║╚██╗██║██╔══██║██╔══██║    ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██║
██║ ╚═╝ ██║██║██║ ╚████║██║  ██║██║  ██║    ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝''')
# Login do Banco
def banco_login():
    banco_logo()
    print('Escolha a opção:\n1- Login\n2- Cadastrar')
    escolha1 = int(input('Escolha:'))
    if escolha1 == 1:
        nome = input('Insira seu nome: ').lower()
        cpf = int(input('Insira seu CPF: '))
        cliente1.nome = nome
        cliente1.cpf = cpf
        if cliente1.encontrar_cliente():
            print('Login realizado com sucesso.')
            banco_interface(nome, cpf) # Envia o nome cpf para a interface do banco
        else:
            print('Cliente não encontrado.\n')
            banco_login()
    elif escolha1 == 2:
        cadastrar_ui()
        banco_login()
        
# Interface de interação do banco
def banco_interface(nome, cpf):
    conta1 = Conta(nome, cpf)
    while True:
        banco_minhaconta()
        print('''Escolha uma das opções:
1 - Consultar Saldo
2 - Deposito
3 - Saque
4 - Saque Especial
5- Sair''')
        escolha = int(input('Escolha: '))
        
        if escolha == 1:
        
                conta1.saldo_usuario()
        elif escolha == 2:
                valor = float(input('Insira o valor do depósito:'))
                conta1.deposito(valor)
        elif escolha == 3:
                valor = float(input('Insira o valor do depósito:'))
                conta1.saque(valor)
        elif escolha == 4:
            print('Bem vindo ao saque especial')
            conta1.saque_especial()
            break
        elif escolha == 5:
            print('Saindo...')
            break
        else:
            print('Escolha inválida, tente novamente...')

banco_login()
