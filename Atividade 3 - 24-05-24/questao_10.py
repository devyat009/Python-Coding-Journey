# Atividade: Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final: 
# a) Quantos homens foram cadastrados 
# b) Quantas mulheres foram cadastradas 
# c) A média de idade do grupo 
# d) A média de idade dos homens 
# e) Quantas mulheres tem mais de 20 anos 
# Data: 27/05/2024
# Instrutor: Brunno
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

# Função de identificar o sexo:
def sexu(string):
    try:
        string.lower
        if string.isalpha():
            if string == 'feminino' or string == 'mulher' or string == 'masculino' or string == 'homem':
                return True
        else:
            return False
    except ValueError:
        return False
    
# Listas
homemSex_lista = []
homemIdad_lista = []
mulherSex_lista = []
mulherIda_lista = []

while True:
    # Quantidade de pessoas em que o usuário ira escolher:
    quantidade = input('Insira a quantidade de pessoas: ')
    if e_numero(quantidade):
        quantidade = int(quantidade)
        for i in range(0,quantidade):
            
            while True:
                idade = input(f'Insira a idade da pessoa {i+1}: ')
                if e_numero(idade):
                    idade = int(idade)
                    while True:
                        ############################################################################## DEF SEXO GOSTOSO
                        # Obetemos o sexo, é ja deixamos em letra minuscula com o .lower
                        sexo = input(f'\nInsira o sexo desta pessoa {i+1}: ')
                        sexo.lower
                        if sexu(sexo):
                            if sexo == 'homem' or sexo == 'masculino':
                                homemIdad_lista.append(idade)
                                homemSex_lista.append(sexo)
                                
                            elif sexo == 'mulher' or sexo == 'feminino':
                                mulherIda_lista.append(idade)
                                mulherSex_lista.append(sexo)
                               
                            # Fora do escopo estabelicido:
                            else:
                                print('Insira informações validas, como idade com números e sexo com letras. Cheque sua ortografia.')
                            break
                        # Caso o input não seja o sexo correot:
                        else:
                            print("\nALERTA! Insira o sexo, feminino ou masculino. Tente novamente!")
                    break
                # Caso o input não seja numérico:
                else:
                    print("\nALERTA! Insira um valor om números. Tente novamente!")
        break    
    # Caso o input não seja numérico:
    else:
        print("\nALERTA! Insira um valor om números. Tente novamente!")

# Descobrir a quantidade de mulheres acimad e 20 anos:
mais_de_vinte = sum(1 for idade in mulherIda_lista if idade >= 20)
# Quantidade de pessoas cadastradas:
# Homens:
homem_quantidade = len(homemIdad_lista)
print(f'A) A quantidade de homens foi de: {homem_quantidade}')
# Mulheres:
mulher_quantidade = len(mulherIda_lista)
print(f'B) A quantidade de homens foi de: {mulher_quantidade}')
# Calculamos a média de todo o grupo:
media_total = sum(homemIdad_lista + mulherIda_lista) / quantidade
print(f'C) A média de idade do grupo: {media_total:.2f}')

# Calculamos a média apenas dos homens:
if homemIdad_lista:
    media_homem = sum(homemIdad_lista) / len(homemIdad_lista)
else:
    media_homem = 0
print(f'D) A média de idade dos homens é: {media_homem:.2f}')

# Print da quantidade de mulheres com mais de 20 anos:
print(f'E) A quantidade de mulheres com mais de 20 anos é de: {mais_de_vinte}')