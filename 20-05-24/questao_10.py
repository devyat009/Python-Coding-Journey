# Atividade: Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
# na tela uma das mensagens abaixo:
# - O primeiro valor é o maior
# - O segundo valor é o maior
# - Não existe valor maior, os dois são iguais
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

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
    
while True:
    valor1 = input("Insira o primeiro valor a ser comparado: ")
    if e_numero(valor1):
        valor1 = int(valor1)
        while True:
            valor2 = input("Insira o segundo valor a ser comparado: ")
            if e_numero(valor2):
                valor2 = int(valor2)
                if valor1 > valor2:
                    print(f"O primeiro valor {valor1} e maior")
                    break
                elif valor2 > valor1:
                    print(f"O segundo valor {valor2} e maior")
                    break
            else:
                print("Insira um valor inteiro para o segundo valor")
        break
    else:
        print("Insira um valor inteiro para o primeiro valor")