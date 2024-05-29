# Atividade: Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela  
# qual foi o maior e qual foi o menor preço digitado. 
# Data: 27/05/2024
# Instrutor: Brunno
# Autor: Higor Stanley

# Pede as informações para o usuário:
quantidade = int(input('Insira a quantidade de produtos que dejesa inserir o preço: '))
produtos = []

for i in range(0, quantidade):
    produ = float(input(f'Insira o preço do produto {i+1}: R$ '))
    produtos.append(produ)
    produtos.sort()

# A respota do programa:
print(f'O menor preço foi de: R${produtos[0]}')
print(f'O maior preço foi de: R${produtos[-1]}')