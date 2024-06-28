# Atividade: Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
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

while True:
    print("\nOpcoes disponiveis no JoKenPo: Pedra, Papel e Tesoura")
    jogador1 = input("Jogador 1 - Insira sua escolha no jogo JokenPo:")
    if e_letra(jogador1):
        jogador1 = str(jogador1)
        jogador1 = jogador1.lower()
        while True:
            jogador2 = input("\nJogador 2 - Insira sua escolha no jogo JokenPo:")
            if e_letra(jogador2):
                jogador2 =  str(jogador2)
                jogador2 = jogador2.lower()
                try:
                    if jogador1 == 'pedra' and jogador2 == 'papel':
                        print("O jogador 2 venceu, parabéns!")
                    elif jogador1 == 'papel' and jogador2 == 'pedra':
                        print("O jogador 1 venceu, parabéns!")
                    elif jogador1 == 'pedra' and jogador2 == 'tesoura':
                        print("O jogador 1 venceu, parabéns!")
                    elif jogador1 == 'tesoura' and jogador2 == 'pedra':
                        print("O jogador 2 venceu, parabéns!")
                    elif jogador1 == 'tesoura' and jogador2 == 'papel':
                        print("O jogador 1 venceu, parabéns!")
                    elif jogador1 == 'papel' and jogador2 == 'tesoura':
                        print("O jogador 2 venceu, parabéns!")
                    else:
                        print("Jogada inválidada")
                except:
                    print("Jogada inválidada 1")
            else:
                print("\nALERT! Insira palavras sem números. Tente Novamente!\n")
            break
    else:
        print("\nALERT! Insira palavras sem números. Tente Novamente!\n")