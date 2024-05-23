# Atividade: Uma empresa precisa reajustar o salário dos seus funcionários, dando um
# aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
# o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
# No final, mostre o seu novo salário, baseado na tabela a seguir:
# - Mulheres
# - Menos de 15 anos de empresa: +5%
# - De 15 até 20 anos de empresa: +12%
# - Mais de 20 anos de empresa: +23%
# - Homens
# - Menos de 20 anos de empresa: +3%
# - De 20 até 30 anos de empresa: +13%
# - Mais de 30 anos de empresa: +25%

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
    salario = input("insira salario: ")
    if e_numero(salario):
        salario = float(salario)
        while True:
            anos = input("Insira a quantidade de anos: ")
            if e_numero(anos):
                anos = int(anos)
                while True:
                    genero = input("Insira o gênero do funcionário: ")
                    if e_letra(genero) and genero in ["masculino", "feminino"]:
                        genero = str(genero).lower()
                        # Caso o gênero sejá feminino:
                        if genero == 'feminino':
                            if 15 > anos:
                                    salario = salario * 5/100 + salario      
                            elif 15 >= anos < 20:
                                    salario = salario * 12/100 + salario
                            elif 20 < anos:
                                    salario = salario * 23/100 + salario
                        # Caso o gênero sejá masculino:
                        elif genero == 'masculino':
                            if 15 > anos:
                                    salario = salario * 3/100 + salario
                            elif 15 >= anos < 20:
                                    salario = salario * 13/100 + salario
                            elif 20 < anos:
                                    salario = salario * 25/100 + salario
                        print(f"O novo salário com o reajuste será de R$ {salario}")
                        break
                    # Caso o input do usuário não sejá nenhuma das duas opções fornecidas:
                    else:
                        print("ALERTA! Insira feminino ou masculino para o gênero. Tente novamente!")
                break
            # Caso o input do usuário não seja números:
            else:
                print("ALERTA! Insira números para os anos. Tente novamente!")
        break
    # Caso o input do usuário não seja números:
    else:
        print("ALERTA! Insira números para o salário. Tente novamente!")