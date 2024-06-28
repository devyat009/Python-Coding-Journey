# Atividade: Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou
# ÍMPAR.
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Função para checar se o input do usuário e número:
def e_numero(string):
    try:
        if string.isnumeric():
            string = int(string)
            return True
        else:
            string = float(string)
            return True
    except ValueError:
        return False

# Programa em loop para validar o input:
while True:
    numero = input("Insira um número, par que possa verificar se e ímpar ou par: ")
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(numero):
        numero = float(numero)
        # Caso o número seja divisivel por 2 até 0 com resultado 0 ele é PAR:
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        # Caso o número seja divisivel por 2 até 0 com resultado 1 ele é ÍMPAR:
        else:
            print(f"O número {numero} é ímpar.")
    # Caso o input não seja numérico:
    else:
        print("ALERTA! Insira um valor om números. Tente novamente!")