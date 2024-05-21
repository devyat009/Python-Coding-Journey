# Atividade: Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
# dela e depois mostre se ela pode ou não votar.
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
    ano_nascimento = input("Insira seu ano de nascimento para saber se pode votar: ")

    if e_numero(ano_nascimento):
        ano_nascimento = int(ano_nascimento)
        if 2024 - ano_nascimento > 18:
            print("Você está apto a votar")
            break
        elif ano_nascimento - 2024 == 0:
            print("Pessoas em que não nasceram não podem votar")
            break
        else:  2024 - ano_nascimento < 18
        print("Infelizmente você e menor de idade")
        break
    else:
        print("Insira os anos com números e tente novamente")