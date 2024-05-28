# Atividade:  Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando 
# no final: 
# a) Qual foi a média de altura do grupo 
# b) Quantas pessoas pesam mais de 90Kg 
# c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m 
# d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg. 
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

# Listas
altura_lista = []
peso_lista = []

while True:
     # Quantidade de pessoas em que o usuário ira escolher:
    quantidade = input('Insira a quantidade de pessoas: ')
    if e_numero(quantidade):
        quantidade = int(quantidade)
        
        for i in range(1, quantidade+1):
            while True:
                altura= input(f'\nInsira a altura da pessoa {i} em METROS: ')
                if e_numero(altura):
                    altura = float(altura)
                    # Adiconamos a lista:
                    altura_lista.append(altura)
                    while True:
                        # Obetemos o peso.
                        peso = input(f'Insira o peso desta pessoa {i}: ')
                        if e_numero(peso):
                            peso = float(peso)
                            # Caso o input não seja numérico:
                            peso_lista.append(peso)
                            break
                        else:
                            print("\nALERTA! Insira um valor om números. Tente novamente!")
                    break
                # Caso o input não seja numérico:
                else:
                    print("\nALERTA! Insira um valor om números. Tente novamente!")

        # Para saber a média de todo o grupo:
        media = sum(altura_lista) / quantidade
        print(f'A média de altura de todo o grupo de pessoas foi de: {media:.2f}')

        # Quantos pesam mais de 90kg:
        maisdeNoventa = sum(1 for peso in peso_lista if peso > 90)
        print(f'B - A quantidade de pessoas que pesam mais de 90Kg é de: {maisdeNoventa} pessoas')

        # Caso medem mais de 1.90m pesam mais de 100Kg:
        condicao1 = sum(1 for altura, peso in zip(altura_lista, peso_lista) if altura < 1.60 and peso <= 50)
        print(f'C - A quantidade de pessoas que medem mais de 1.60m pesam menos de 50Kg é de: {condicao1} pessoas')

        # Caso medem mais de 1.90m pesam mais de 100Kg:
        condicao2 = sum(1 for altura, peso in zip(altura_lista, peso_lista) if altura >= 1.90 and peso >= 100)
        print(f'D - A quantidade de pessoas que medem mais de 1.90m pesam mais de 100Kg é de: {condicao2} pessoas')
        
        #Sair do loop
        break
    # Caso o input não seja numérico:
    else:
        print("\nALERTA! Insira um valor om números. Tente novamente!")
