# Atividade: Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
# situação em relação ao alistamento militar.
#   - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
#   - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do Alistamento.
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
    ano_nascimento = input("Insira seu ano de nascimento para saber sua situação em relação ao alistamento militar: ")
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(ano_nascimento):
        ano_nascimento = int(ano_nascimento)
        # Caso já seja mair de 18 anos:
        if 2024 - ano_nascimento > 18:
            anos = (2024 - ano_nascimento) - 18 
            print(f"Já se passaram {anos} anos do alistamento.")
            break
        # Caso tenha 0 anos:
        elif 2024 - ano_nascimento == 0:
            print("Pessoas em que não nasceram não podem se alistar.")
            break
        # Caso ainda não tenha 18 anos:
        elif 2024 - ano_nascimento < 18:
            anos = (2024 - ano_nascimento)
            anos = 18 - anos
            print(f"Infelizmente você e menor de idade e falta {anos} anos para seu alistamento.")
            break
    # Caso o input não seja numérico:
    else:
        print("ALERTA! Insira os anos com números e tente novamente")