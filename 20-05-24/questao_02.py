# Atividade: Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
# dela e depois mostre se ela pode ou não votar.
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
    ano_nascimento = input("Insira seu ano de nascimento para saber se pode votar: ")
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(ano_nascimento):
        ano_nascimento = int(ano_nascimento)
        # Caso a idade do usuário seja maior que 18:
        if 2024 - ano_nascimento > 18:
            print("Você está apto a votar.")
            break
        # Caso a idade do usuário seja 0:
        elif ano_nascimento - 2024 == 0:
            print("Pessoas em que não nasceram não podem votar.")
            break
        # Caso a idade do usuário seja menor que 18:
        else:  2024 - ano_nascimento < 18
        print("Infelizmente você e menor de idade.")
        break
    # Caso o input não seja numérico:
    else:
        print("ALERTA! Insira os anos com números. Tente novamente!")