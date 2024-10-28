# Atividade: Faça um algoritmo que leia um determinado ano e mostre se ele é ou não
# BISSEXTO.
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

# Função para checar se o ano inserido é bissexto:
def bissexto(string):
    try: 
        # Caso termine em '0' retorna verdadeiro:
        if int(string) % 400 == 0:
            return True
        # Caso seja divisível por '4' retorna verdadeiro:
        elif int(string) % 4 == 0:
            return True
        elif int(string) % 100 == 0:
            return True
        else:
            return False
    except ValueError:
        return False

# Programa em loop para validar o input:
while True:
    ano = input("Insira o ano para saber se e bissexto: ")
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(ano):
        # Convertemos para string para verificar se finaliza em '00':
        ano = str(ano)
        # Usa a função 'bissexto' para validar se é um ano bissexto:
        if bissexto(ano):
            print("O ano é bissexto.")
        # Caso não seja um ano bissexto:
        else:
            print("Não é um ano bissexto.")
    # Caso o input não seja numérico:
    else:
        print("ALERTA! Insira um valor com números. Tente novamente!")