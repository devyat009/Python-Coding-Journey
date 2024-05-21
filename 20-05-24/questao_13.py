# Atividade: Desenvolva um programa que leia o nome de um funcionário, seu salário,
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
# acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - Entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Função para checar se o input do usuário é número:
def e_numero(string):
    try:
        if string.isnumeric():
            string = int(string)
            return True   
        else:
            string = float(string)
            return False # Colocamos False para termos apenas valores inteiros
    except ValueError:
        return False

# Função para checar se o input do usuário é uma string:
def e_letra(string):
    try:
        if string.isStr():
            string = str
            while True:


# Programa em loop para validar o input: