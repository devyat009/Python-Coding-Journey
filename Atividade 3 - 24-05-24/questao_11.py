# Atividade:  Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando 
# no final: 
# a) Qual foi a média de altura do grupo 
# b) Quantas pessoas pesam mais de 90Kg 
# c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m 
# d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg. 
# Data: 27/05/2024
# Instrutor: Brunno
# Autor: Higor Stanley

# Quantidade de pessoas em que o usuário ira escolher:
quantidade = int(input('Insira a quantidade de pessoas: '))
# Listas
altura_lista = []
peso_lista = []

for i in range(0,quantidade):
    altura= float(input(f'Insira a altura da pessoa {i+1} em METROS: '))
    altura_lista.append(altura)
    # Obetemos o peso.
    peso = float(input(f'\nInsira o peso desta pessoa {i+1}: '))
    peso_lista.append(peso)

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
