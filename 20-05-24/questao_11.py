# Atividade: Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média até 4.9: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
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
            return True
    except ValueError:
        return False

# Programa em loop para validar o input:
while True:
    nota1 = input("Insira a nota 1 do aluno: ")
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(nota1):
        nota1 = float(nota1)
        while True:
            nota2 = input("Insira a nota 2 do aluno: ")
            # Usa a função 'e_numero' para validar o input do usuário:
            if e_numero(nota2):
                nota2 = float(nota2)
                media = (nota1+nota2) / 2
                # Caso a média do aluno seja igual ou menor que 4.9 ele está reprovado:
                if media <= 4.9:
                    print("O aluno está REPROVADO:!")
                    break
                # Caso a média do aluno seja igual ou maior que 5 e menor ou igual que 6.9, ele está em recuperação:
                elif media >= 5.0 <= 6.9:
                    print("O aluno está em RECUPERAÇÃO!")
                    break
                # Caso a média do aluno seja maior que 7.0 ele está aprovado:
                elif media > 7.0:
                    print("O aluno está APROVADO!")
                    break
            # Caso o input não seja numérico:
            else:
                print("Insira um valor numerico para nota 2. Tente novamente!")
        break
    # Caso o input não seja numérico:
    else:
        print("Insira um valor numerico para a nota 1. Tente novamente!")