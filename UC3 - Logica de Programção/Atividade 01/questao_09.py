# Atividade: Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar Considere $1,00 = R$5,16.
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024

reais = float(input('Insira a quantidade de reais em que possui: '))
# Magimatica
dollar = reais / 5.16
#Resposta do programa, com valor do float formatado
print('A quantidade em poderá comprar de dolares com R$', reais,'será de: ${:.2f}'.format(dollar))