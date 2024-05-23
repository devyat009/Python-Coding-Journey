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

