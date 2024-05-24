# Atividade: Crie um programa que leia o tamanho de três segmentos de reta.
# Analise seus comprimentos e diga se é possível formar um triângulo com essas retas.
# Matematicamente, para três segmentos formarem um triângulo,
# o comprimento de cada lado deve ser menor que a soma dos outros dois
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# ERRO NA DEF
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
    a, b, c = input("Insira o seguimentos da reta serapados por ',': ").split(',')
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(a):
        a = float(a)
        # Loop novamente para validar o segundo input:
        while True:
            # Usa a função 'e_numero' para validar o input do usuário:
            if e_numero(b):
                b = float(b)
                while True:
                    if e_numero(c):
                        c = float(c)
                        # Caso os valores sejam, o comprimento seja menor que os outros dois:
                        if a < b + c or b < a + c or c < b + a:
                            print("É possível fazer um triângulo com os valores fornecidos.")
                            break
                        else:
                            print("NÃO e possível fazer um triângulo comos valores fornecidos.")
                            break
                    # Caso o input não seja numérico:
                    else:
                        print("ALERTA! Insira um valor com números para C. Tente novamente!")
                        c = input("\n Qual o valor de C: ")
                break
            # Caso o input não seja numérico:
            else:
                print("ALERTA! Insira um valor com números para B. Tente novamente!")
                b = input("\n Qual o valor de B: ")
        break
    # Caso o input não seja numérico:
    else:
        print("ALERTA! Insira um valor com números para A. Tente novamente!")
        a = input("\n Qual o valor de A: ")