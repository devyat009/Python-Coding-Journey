# Atividade: Faça um algoritmo que leia um determinado ano e mostre se ele é ou não
# BISSEXTO.
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
    
def bissexto(string):
    try: 
        if str(string).endswith("0"):
            return True
        elif int(string) % 4 == 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
while True:
    ano = input("Insira o ano para saber se e bissexto: ")
    if e_numero(ano):
        # Convertemos para string para verificar se finaliza em '00'
        ano = str(ano)
        if bissexto(ano):
            print("O ano e bissexto")
        else:
            print("Nao e um ano bissexto")
    else:
        print("Insira um valor numerico")