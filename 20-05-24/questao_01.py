# Atividade: Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso,
# exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

import math;

# Funcao para checar se o input e numero
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

while True:   
    velocidade = input("Insira a velocidade do carro: ")
    # Valida 
    if e_numero(velocidade):
        velocidade = float(velocidade)
        if velocidade > 80:
            multa = (velocidade - 80) * 5
            print(f"Seu veiculo foi multado em R${multa} por trafegar em velocidade acima da permitida")
        elif velocidade < 0:
            print("Insira um valor acima de 0")
        elif velocidade == 0:
            print("O carro esta parado") 
        else:
            print("A velocidade esta dentro do limite da via")
    else:
        print("Insira uma velocidade com numeros e tente novamente")