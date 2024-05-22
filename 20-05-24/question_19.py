# Atividade: Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
# aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
# carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
# que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
# quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
# tabela a seguir:
# - Carros populares (aluguel de R$90 por dia)
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km
# - Carros de luxo (aluguel de R$150 por dia)
# - Até 200Km percorridos: R$0,30 por Km
# - Acima de 200Km percorridos: R$0,25 por Km
# Data: 22/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Função para checar se o input do usuário é uma string:
def e_letra(string):
    try:
        if string.isalpha():
            string = str
            return True
        else:
            return False
    except ValueError:
        return False

#
def diavalor(string):
    if carro_tipo == 'popular':
        string = string * 90
    elif carro_tipo == 'luxo':

# Mudar o valor baseado no carro
def carro_tipo(tipo, int dia):
        tipo= str(tipo).lower
        if tipo == 'popular':
            tipo = diavalor * 90
        elif tipo== 'luxo':

        else:
            print("Insira apenas uma das duas opções: Popular ou Luxo")


while True:
    carro_tipo = input("Escolha o tipo de carro: Popular ou Luxo")
    if e_letra(carro):
        carro_tipo = str(carro_tipo).lower
        if carro_tipo == 'popular':
        elif carro_tipo == 'luxo':
        else:
            print("Insira apenas uma das duas opções: Popular ou Luxo")
    # Caso o input do usuário seja diferente de letras:
    else:
        print("ALERTA! Insira apenas letras para o tipo de carro. Tente Novamente!")