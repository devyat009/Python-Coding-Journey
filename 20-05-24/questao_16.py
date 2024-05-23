# Atividade: Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
# jogador vai tentar descobrir qual foi o valor sorteado.
# Data: 22/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

import random;

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

while True:
    jogador = input("O computador escolheu um número de 1 a 5, tente advinha qual ele escolheu: ")
    if e_numero(jogador):
        jogador = int(jogador)
        if 1 <= jogador <= 5:
            computador = random.choice([1,2,3,4,5])
            # Caso o jogador acerte o mesmo valor que o computador:
            if jogador == computador:
                print("Vocẽ acertou a escolha do computador!")
                break
            # Caso o jogador erre a escolha do computadar:
            else:
                print(f"Infelimente você errou, o computador escolheu o número {computador}.")
                break
        # Caso o input do usuário não de 1 a 5 como pedido:
        else:
            print("Insira um valor entre 1 a 5.")
    # Caso o input do usuário não seja números:
    else:
        print("ALERTA! Insira um valor com números. Tente novamente!")