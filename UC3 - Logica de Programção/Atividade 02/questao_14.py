# Atividade: [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes
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

