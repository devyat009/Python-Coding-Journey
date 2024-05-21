# Atividade: Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
# média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
# não um bom aproveitamento (se ficou acima da média 7.0).
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Função para checar se o input do usuario e número:
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
    nota1 = input("Insira a nota 1 do aluno: ")
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(nota1):
        nota1 = float(nota1)
        # Após verificar se a 'nota1'é valida, inicia outro loop para validar a 'nota2':
        while True:
            nota2 = input("Insira a nota 2 do aluno: ")
            if e_numero(nota2):
                nota2 = float(nota2)
                media = (nota1+nota2) / 2
                # Nota mínima para aprovação:
                if media >= 7:
                    print(f"O aluno foi aprovado com uma média de {media}")
                    break
                # Nota de corte:
                else: media < 7
                print("O aluno não foi aprovadado")
                break
            # Caso o input não seja numérico:
            else:
                print("ALERTA! Insira a nota 2 com números. Tente novamente!")
        break
    # Caso o input não seja numérico:
    else:
        print("ALERTA! Insira a nota 1 com números. Tente novamente!")