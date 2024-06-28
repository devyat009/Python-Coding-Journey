# Atividade: Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024

produto = float(input('Insira o preço do produto: '))

#Magimatica
valor_final = -produto * (5/100) + produto
#Resposta do Programa
print('O valor do produto com 5% de desconto é de: {:.2f}'.format(valor_final))