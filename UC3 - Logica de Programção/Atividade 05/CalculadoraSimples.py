# Atividade: Calculadora simples usando def's
# Instrutor: Brunno
# Nome: Higor Stanley
# Data: 03/06/2024
# Últilma Edição: 06/06/2024

# Soma
def soma(a, b):
    resultado = a + b
    print(f'O resultado é: {resultado}')
# Subtração
def subtracao(a, b):
    resultado = a - b
    print(f'O resultado é: {resultado}')
# Divisão
def divisao(a, b):
    resultado = a / b
    print(f'O resultado é: {resultado}')
# Multiplicação
def multiplicacao(a, b):
    resultado = a * b
    print(f'O resultado é: {resultado}')
# Potência
def potencia(a, b):
    resultado = a ** b
    print(f'O resultado é: {resultado}')
# Exibir Titulo
def exbir_titulo():
    print('======= Calculadora =======')
def menu(): 
    print('Bem vindo a calculadora suprema :)')
    print('\n1 - Soma')
    print('2 - Subtração')
    print('3 - Divisão')
    print('4 - Multiplicação')
    print('5 - Potência')
    print('6 - Sair')

def main():
    exbir_titulo()
    menu()
    opcao_escolhida = int(input('Sua escolha é:'))
    numero1 = float(input('Insira o primeiro número: '))
    numero2 = float(input('Insira o segundo número: '))
    match opcao_escolhida:
        case 1:
            soma(numero1, numero2)
        case 2:
            subtracao(numero1, numero2)
        case 3:
            divisao(numero1, numero2)
        case 4:
            multiplicacao(numero1, numero2)
        case 5:
            potencia(numero1, numero2)
        case 6:
            print('Saindo...')
# Executa a main:
main()
