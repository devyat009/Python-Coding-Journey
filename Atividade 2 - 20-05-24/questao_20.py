# Atividade: Um programa de vida saudável quer dar pontos atividades físicas que podem
#  ser trocados por dinheiro. O sistema funciona assim:
# - Cada hora de atividade física no mês vale pontos
# - Até 10h de atividade no mês: ganha 2 pontos por hora
# - De 10h até 20h de atividade no mês: ganha 5 pontos por hora
# - Acima de 20h de atividade no mês: ganha 10 pontos por hora
# - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
# Faça um programa que leia quantas horas de atividade uma pessoa teve por mês,
#  calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.
# Data: 22/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Função para checar se o input do usuário é número:
def e_numero(string):
    try:
        if string.isnumeric():
            string = int(string)
            return True   
        else:
            string = float(string)
            return True # Colocamos False para termos apenas valores inteiros
    except ValueError:
        return False
    
# Programa em loop para validar o input:
while True:
    horas = input("Insira a quantidade de horas em que exercitou: ")
    if e_numero(horas):
        horas = int(horas)
        # Caso seja menos que 10 horas:
        if horas < 10:
            pontos = 2 * horas
            pontos_valor = 0.05 * pontos
            print(f"Parabéns você ganhou R${pontos_valor}")
            break
        # Caso seja maior que 10 horas e menos de 20:
        elif 10 <= horas <= 20:
            pontos = 5 * horas
            pontos_valor = 0.05 * pontos
            print(f"Parabéns você ganhou R${pontos_valor}")
            break
        # Caso seja maior que 20 horas:
        elif horas > 20:
            pontos = 10 * horas
            pontos_valor = 0.05 * pontos
            print(f"Parabéns você ganhou R${pontos_valor}")
            break
        # Caso o input do usuário não seja valido:
        else:
            print("ALERTA! Insira um valor valido. Tente novamente!")
    # Caso o input do usuário não seja números:
    else:
        print("ALERTA! Insira números. Tente novamente!")
