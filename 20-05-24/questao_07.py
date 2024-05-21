# Atividade: Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
# para todos, mas especialmente para mulheres. Faça um programa que leia nome,
# sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
#   - Homens ganham 5% de desconto
#   - Mulheres ganham 13% de desconto
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
    nome, sexo, compra = input("Insira o nome do cliente, sexo e valor da compra separadas por ',': ").split(',')
    nome = str(nome)
    sexo = str(nome).lower
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(compra):
        compra = float(compra)
        # Caso o clieten seja do sexo Feminino:
        if sexo == 'feminino' or sexo == 'mulher':
            desconto = (- compra * 13/100) + compra 
            print(f"O desconto da cliente {nome} foi aplicado, Total a pagar R$:{desconto} ")
            break
        # Caso o clieten seja do sexo Masculino:
        else: sexo == 'masculino' or sexo == 'homem'
        desconto = (- compra * 5/100) + compra 
        print(f"O desconto do cliente {nome} foi aplicado, Total a pagar R$:{desconto} ")
        break
    # Caso o input não seja numérico:
    else: 
        print("ALERTA! Insira um valor com números para valor da compra.")
    