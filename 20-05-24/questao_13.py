# Atividade: Desenvolva um programa que leia o nome de um funcionário, seu salário,
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
# acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - Entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%
# Data: 21/05/2024
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


# Programa em loop para validar o input:
while True:
    nome = input("Insira o nome do funcionário: ")
    if e_letra(nome):
        nome = str(nome)
        while True:
            salario = input("Agora insira o salário do funcionário:")
            if e_numero(salario):
                salario = float(salario)
                while True:
                    anos = input("Agora inira a quantidade de anos que está na empresa: ")
                    if e_numero(anos):
                        anos = int(anos)
                        # Matematica
                        # Caso seja até 3 anos:
                        if 0 >= anos and anos < 2.9:
                            salario = (3/100 * salario) + salario  
                            print(f"O novo salário de acordo com o reajuste do salário do funcionário {nome}, é de R$ {salario}")
                            break
                        # Caso seja entre 3 e 10 anos:
                        elif 3 <= anos <= 10:
                            salario = (12/100 * salario) + salario
                            print(f"O novo salário de acordo com o reajuste do salário do funcionário {nome}, é de R$ {salario}")
                            break
                        # Caso seja acima de 10 anos:
                        elif anos > 10:
                            salario = (20/100 * salario) + salario
                            print(f"O novo salário de acordo com o reajuste do salário do funcionário {nome}, é de R$ {salario}")
                            break
                    # Caso o input não seja numérico:
                    else:
                        print("ALERTA! Insira um valor com números para os anos. Tente novamente!")
                break
            # Caso o input não seja numérico:
            else:
                print("ALERTA! Insira um valor com números para o salário. Tente novamente!")
        break
    # Caso o input do usuário não seja letras:
    else:
        print("ALERTA! Insira apenas letras para o nome. Tente Novamente!")