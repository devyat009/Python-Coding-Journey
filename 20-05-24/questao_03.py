# Atividade: Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
# média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
# não um bom aproveitamento (se ficou acima da média 7.0).
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Funcao para checar se o input e numero
def e_numero(string):
    try:
        if string.isnumeric():
            formata_int = int(string)
            return True
        else:
            formata_float = float(string)
            return True
    except ValueError:
        return False

# Loop inciado para validar os inputs
while True:
    nota1 = input("Insira a nota 1 do aluno: ")
    if e_numero(nota1):
        nota1 = float(nota1)
        while True:
            nota2 = input("Insira a nota 2 do aluno: ")
            if e_numero(nota2):
                nota2 = float(nota2)
                media = (nota1+nota2) / 2
                # Nota minima para aprovacao
                if media >= 7:
                    print(f"O aluno foi aprovado com uma media de {media}")
                    break
                # Nota de corte
                else: media < 7
                print("O aluno não foi aprovadado")
                break
            # Caso o input nao seja numerico
            else:
                print("Insira a nota 1 com numeros e tente novamente")
        break
    # Caso o input nao seja numerico
    else:
        print("Insira a nota 1 com numeros e tente novamente")