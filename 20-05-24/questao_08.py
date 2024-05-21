# Atividade: Faça um algoritmo que pergunte a distância que um passageiro deseja
# percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
# viagens até 200Km e R$0.45 para viagens mais longas.
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

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
    km = input("Insira a quantidade de KM em que deseja percorer: ")
    if e_numero(km):
        km = float(km)
        if km <= 200:
            print(f"O preco da passagem sera de: R${km*0.50}")
            break
        elif km > 200:
            print(f"O preco da passagem sera de: R${km*0.45}")
            break
    else:
        print("Insira um valor numerico")