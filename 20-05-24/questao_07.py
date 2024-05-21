# Atividade: Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
# para todos, mas especialmente para mulheres. Faça um programa que leia nome,
# sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
#   - Homens ganham 5% de desconto
#   - Mulheres ganham 13% de desconto
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
    nome, sexo, compra = input("Insira o NOME do cliente, sexo e valor da compra separadas por ',': ").split(',')
    nome = str(nome)
    sexo = str(nome).lower
    
    if e_numero(compra):
        compra = float(compra)
        if sexo == 'feminino' or sexo == 'mulher':
            desconto = (- compra * 13/100) + compra 
            print(f"O desconto da cliente {nome} foi aplicado, Total a pagar R$:{desconto} ")
            break
        else: sexo == 'masculino' or sexo == 'homem'
        desconto = (- compra * 5/100) + compra 
        print(f"O desconto do cliente {nome} foi aplicado, Total a pagar R$:{desconto} ")
        break
    else: 
        print("Insira um valor valido para a compra")
    