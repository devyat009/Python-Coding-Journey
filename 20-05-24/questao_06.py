# Atividade: Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
# situação em relação ao alistamento militar.
#   - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
#   - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do Alistamento.
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
    ano_nascimento = input("Insira seu ano de nascimento para saber sua situacao em relacao ao alistamento militar: ")

    if e_numero(ano_nascimento):
        ano_nascimento = int(ano_nascimento)
        if 2024 - ano_nascimento > 18:
            anos = (2024 - ano_nascimento) - 18 
            print(f"Ja se passaram {anos} anos do alistamento")
            break
        elif 2024 - ano_nascimento == 0:
            print("Pessoas em que não nasceram não podem se alistar")
            break
        elif 2024 - ano_nascimento < 18:
            anos = (2024 - ano_nascimento)
            anos = 18 - anos
            print(f"Infelizmente você e menor de idade e falta {anos} anos para seu alistamento")
            break
    else:
        print("Insira os anos com números e tente novamente")