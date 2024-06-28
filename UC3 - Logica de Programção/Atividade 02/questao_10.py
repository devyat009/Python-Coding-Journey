# Atividade: Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
# na tela uma das mensagens abaixo:
# - O primeiro valor é o maior
# - O segundo valor é o maior
# - Não existe valor maior, os dois são iguais
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
            return False # Colocamos False para termos apenas valores inteiros
    except ValueError:
        return False

# Programa em loop para validar o input:
while True:
    valor1 = input("Insira o primeiro valor a ser comparado: ")
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(valor1):
        valor1 = int(valor1)
        while True:
            valor2 = input("Insira o segundo valor a ser comparado: ")
            # Usa a função 'e_numero' para validar o input do usuário:
            if e_numero(valor2):
                valor2 = int(valor2)
                # Caso o primeiro valor inserido seja mairor:
                if valor1 > valor2:
                    print(f"O primeiro valor {valor1} é maior.")
                    break
                # Caso o segundo valor inserido seja maior:
                elif valor2 > valor1:
                    print(f"O segundo valor {valor2} é maior.")
                    break
            # Caso o input não seja numérico:
            else:
                print("ALERTA! Insira um valor inteiro para o segundo valor. Tente novamente!")
        break
    # Caso o input não seja numérico:
    else:
        print("ALERTA! Insira um valor inteiro para o primeiro valor. Tente novamente!")