# Atividade: Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou
# ÍMPAR.
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Funcao para checar se o input e numero
def e_numero(string):
    try:
        if string.isnumeric():
            formata_int = int(string)
            return True
        else:
            formata_float = float(string)
            return True
    except ValueError:
        return False
    
while True:
    numero = input("Insira um numero, par que possa verificar se e impar ou par")
    if e_numero(numero):
        numero = float(numero)
        if numero % 2 == 0:
            print(f"O número {numero} é par")
        else:
            print(f"O número {numero} é ímpar")
    else:
        print("Insira um valor NUMERICO")