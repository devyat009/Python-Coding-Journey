# Atividade: Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso,
# exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

import math;

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
    velocidade = input("Insira a velocidade do veículo: ")
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(velocidade):
        velocidade = float(velocidade)
        # Caso a velocidade for acima de 80 multar:
        if velocidade > 80:
            multa = (velocidade - 80) * 5
            print(f"Seu veículo foi multado em R${multa} por trafegar em velocidade acima da permitida.")
            break
        # Caso a velocidade seja negativa:
        elif velocidade < 0:
            print("Insira um valor acima de 0")
            break
        # Caso o veículo esteja parado:
        elif velocidade == 0:
            print("O carro está parado")
            break
        else:
            print("A velocidade está dentro do limite da via.")
    # Caso o input não seja numérico:
    else:
        print("ALERTA! Insira uma velocidade com números. Tente novamente!")