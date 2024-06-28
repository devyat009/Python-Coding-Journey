# Atividade:  Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final: 
# a) Qual é a média de idade do grupo 
# b) Quantas pessoas tem mais de 18 anos 
# c) Quantas pessoas tem menos de 5 anos 
# d) Qual foi a maior idade lida 
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
# Lista
pessoas = []

# Loop do programa para validações:
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
                    pessoas.append(idade)
                    break
                # Caso o input não seja numérico:
                else:
                    print("\nALERTA! Insira um valor com números. Tente novamente!")
        # Calculamos a média:
        media = sum(pessoas) / quantidade
        print(f'A média: {media:.2f}')\

        # Descobrimos quantos são maiores de idade:
        maior_de_dezoito = sum(1 for idade in pessoas if idade >= 18)
        print(f'Tem {maior_de_dezoito} maiores de 18 anos de idade.')

        # Descobrimos quantos são tem menos de 5 anos
        menor_de_cinco = sum(1 for idade in pessoas if idade < 5)
        print(f'Tem {menor_de_cinco} com menos de 5 anos de idade.')
        
        #Sair do loop
        break
    # Caso o input não seja numérico:
    else:
        print("\nALERTA! Insira um valor com números. Tente novamente!")

    

    
